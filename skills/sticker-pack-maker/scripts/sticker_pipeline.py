#!/usr/bin/env python3
"""Turn flat chroma-key sticker renders into validated transparent PNG packs."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from PIL import Image, ImageDraw


PNG_SUFFIX = ".png"


@dataclass(frozen=True)
class Entry:
    source: Path
    filename: str


@dataclass(frozen=True)
class ValidationReport:
    count: int
    sizes: tuple[tuple[int, int], ...]
    failures: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.failures


def parse_color(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"#?([0-9a-fA-F]{6})", value.strip())
    if not match:
        raise argparse.ArgumentTypeError("color must be a 6-digit hex value, e.g. #0000FF")
    raw = match.group(1)
    return tuple(int(raw[i : i + 2], 16) for i in (0, 2, 4))


def sample_border_color(rgb: np.ndarray) -> tuple[int, int, int]:
    border = np.concatenate(
        (rgb[0, :, :], rgb[-1, :, :], rgb[:, 0, :], rgb[:, -1, :]), axis=0
    )
    median = np.median(border.astype(np.float32), axis=0)
    return tuple(int(round(channel)) for channel in median)


def chroma_to_rgba(
    image: Image.Image,
    key_color: tuple[int, int, int] | None = None,
    transparent_threshold: float = 12.0,
    opaque_threshold: float = 220.0,
    despill: bool = True,
) -> Image.Image:
    if opaque_threshold <= transparent_threshold:
        raise ValueError("opaque threshold must be greater than transparent threshold")

    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    rgb = rgba[:, :, :3].astype(np.float32)
    key = key_color or sample_border_color(rgba[:, :, :3])
    key_array = np.asarray(key, dtype=np.float32)

    distance = np.linalg.norm(rgb - key_array, axis=2)
    matte = np.clip(
        (distance - transparent_threshold)
        / (opaque_threshold - transparent_threshold),
        0.0,
        1.0,
    )
    matte = matte * matte * (3.0 - 2.0 * matte)
    source_alpha = rgba[:, :, 3].astype(np.float32) / 255.0
    alpha = np.rint(255.0 * matte * source_alpha).astype(np.uint8)

    # Generated "flat" backgrounds often contain a few units of corner noise.
    # Flood only key-like pixels connected to the canvas edge so those pixels
    # become exactly transparent without erasing isolated blue subject details.
    background_cutoff = max(48.0, transparent_threshold * 3.0)
    candidate = np.where(distance <= background_cutoff, 255, 0).astype(np.uint8)
    connected = Image.fromarray(candidate).copy()
    for point in (
        (0, 0),
        (connected.width - 1, 0),
        (0, connected.height - 1),
        (connected.width - 1, connected.height - 1),
    ):
        if connected.getpixel(point) == 255:
            ImageDraw.floodfill(connected, point, 128)
    alpha[np.asarray(connected) == 128] = 0

    if despill:
        key_channel = int(np.argmax(key_array))
        other_channels = [channel for channel in range(3) if channel != key_channel]
        fringe = (alpha > 0) & (alpha < 250)
        other_max = np.max(rgba[:, :, other_channels], axis=2).astype(np.int16)
        allowance = 24 + np.rint(alpha.astype(np.float32) * 0.08).astype(np.int16)
        limited = np.minimum(
            rgba[:, :, key_channel].astype(np.int16), other_max + allowance
        ).astype(np.uint8)
        rgba[:, :, key_channel] = np.where(
            fringe, limited, rgba[:, :, key_channel]
        )

    rgba[alpha == 0, :3] = 0
    rgba[:, :, 3] = alpha
    return Image.fromarray(rgba, mode="RGBA")


def load_entries(input_dir: Path, manifest: Path | None) -> list[Entry]:
    if manifest is None:
        return [
            Entry(source=path, filename=path.name)
            for path in sorted(input_dir.glob(f"*{PNG_SUFFIX}"))
        ]

    payload = json.loads(manifest.read_text(encoding="utf-8"))
    rows = payload.get("scenes", []) if isinstance(payload, dict) else payload
    if not isinstance(rows, list):
        raise ValueError("manifest must be a JSON array or an object with a scenes array")

    entries: list[Entry] = []
    for position, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"manifest row {position} must be an object")
        source_name = row.get("source")
        filename = row.get("filename")
        if not source_name or not filename:
            raise ValueError(
                f"manifest row {position} requires both source and filename"
            )
        safe_name = Path(str(filename)).name
        if not safe_name.lower().endswith(PNG_SUFFIX):
            safe_name += PNG_SUFFIX
        entries.append(Entry(input_dir / str(source_name), safe_name))
    return entries


def process_pack(
    input_dir: Path,
    output_dir: Path,
    entries: Sequence[Entry],
    key_color: tuple[int, int, int] | None,
    transparent_threshold: float,
    opaque_threshold: float,
    despill: bool,
    force: bool,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    for entry in entries:
        if not entry.source.is_file():
            raise FileNotFoundError(f"missing source image: {entry.source}")
        destination = output_dir / entry.filename
        if destination.exists() and not force:
            raise FileExistsError(f"output exists; pass --force to replace: {destination}")
        with Image.open(entry.source) as image:
            result = chroma_to_rgba(
                image,
                key_color=key_color,
                transparent_threshold=transparent_threshold,
                opaque_threshold=opaque_threshold,
                despill=despill,
            )
            result.save(destination, format="PNG", optimize=True)
        outputs.append(destination)
    return outputs


def validate_directory(
    input_dir: Path, expected_count: int | None = None
) -> ValidationReport:
    files = sorted(input_dir.glob(f"*{PNG_SUFFIX}"))
    failures: list[str] = []
    sizes: set[tuple[int, int]] = set()

    if expected_count is not None and len(files) != expected_count:
        failures.append(f"expected {expected_count} PNG files, found {len(files)}")

    for path in files:
        with Image.open(path) as image:
            sizes.add(image.size)
            if image.mode != "RGBA":
                failures.append(f"{path.name}: mode is {image.mode}, expected RGBA")
                continue
            alpha = image.getchannel("A")
            low, high = alpha.getextrema()
            corners = (
                alpha.getpixel((0, 0)),
                alpha.getpixel((image.width - 1, 0)),
                alpha.getpixel((0, image.height - 1)),
                alpha.getpixel((image.width - 1, image.height - 1)),
            )
            if low != 0 or high != 255:
                failures.append(
                    f"{path.name}: alpha range is ({low}, {high}), expected (0, 255)"
                )
            if any(value != 0 for value in corners):
                failures.append(f"{path.name}: corners are not fully transparent")

    if len(sizes) > 1:
        failures.append(f"inconsistent image dimensions: {sorted(sizes)}")
    return ValidationReport(len(files), tuple(sorted(sizes)), tuple(failures))


def create_zip(files: Iterable[Path], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, arcname=path.name)


def print_report(report: ValidationReport) -> None:
    status = "PASS" if report.ok else "FAIL"
    print(f"{status}: files={report.count} sizes={list(report.sizes)}")
    for failure in report.failures:
        print(f"  - {failure}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build and validate transparent PNG sticker packs."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    process = subparsers.add_parser(
        "process", help="remove chroma background, validate, and optionally zip"
    )
    process.add_argument("--input-dir", type=Path, required=True)
    process.add_argument("--output-dir", type=Path, required=True)
    process.add_argument("--manifest", type=Path)
    process.add_argument("--zip", dest="zip_path", type=Path)
    process.add_argument("--expected-count", type=int)
    process.add_argument("--key-color", type=parse_color)
    process.add_argument("--transparent-threshold", type=float, default=12.0)
    process.add_argument("--opaque-threshold", type=float, default=220.0)
    process.add_argument("--no-despill", action="store_true")
    process.add_argument("--force", action="store_true")

    validate = subparsers.add_parser("validate", help="validate an existing pack")
    validate.add_argument("--input-dir", type=Path, required=True)
    validate.add_argument("--expected-count", type=int)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "validate":
        report = validate_directory(args.input_dir, args.expected_count)
        print_report(report)
        return 0 if report.ok else 1

    entries = load_entries(args.input_dir, args.manifest)
    if not entries:
        print("No PNG source images found.", file=sys.stderr)
        return 2
    expected_count = args.expected_count
    if expected_count is None and args.manifest is not None:
        expected_count = len(entries)

    outputs = process_pack(
        args.input_dir,
        args.output_dir,
        entries,
        args.key_color,
        args.transparent_threshold,
        args.opaque_threshold,
        not args.no_despill,
        args.force,
    )
    report = validate_directory(args.output_dir, expected_count)
    print_report(report)
    if not report.ok:
        return 1
    if args.zip_path:
        create_zip(outputs, args.zip_path)
        print(f"ZIP: {args.zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
