from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "skills"
    / "sticker-pack-maker"
    / "scripts"
    / "sticker_pipeline.py"
)
SPEC = importlib.util.spec_from_file_location("sticker_pipeline", MODULE_PATH)
pipeline = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = pipeline
SPEC.loader.exec_module(pipeline)


class StickerPipelineTests(unittest.TestCase):
    def test_parse_color(self):
        self.assertEqual(pipeline.parse_color("#0000FF"), (0, 0, 255))
        self.assertEqual(pipeline.parse_color("12ab34"), (18, 171, 52))

    def test_process_validate_and_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_dir = root / "source"
            output_dir = root / "output"
            source_dir.mkdir()

            source = Image.new("RGB", (64, 64), (0, 0, 255))
            draw = ImageDraw.Draw(source)
            draw.ellipse((16, 16, 48, 48), fill=(255, 80, 40))
            source.putpixel((0, 63), (1, 18, 232))
            source.putpixel((63, 63), (2, 18, 233))
            source_path = source_dir / "01_test.png"
            source.save(source_path)

            entries = pipeline.load_entries(source_dir, None)
            outputs = pipeline.process_pack(
                source_dir,
                output_dir,
                entries,
                key_color=None,
                transparent_threshold=12,
                opaque_threshold=220,
                despill=True,
                force=True,
            )
            report = pipeline.validate_directory(output_dir, expected_count=1)
            self.assertTrue(report.ok, report.failures)

            with Image.open(outputs[0]) as result:
                self.assertEqual(result.mode, "RGBA")
                self.assertEqual(result.getpixel((0, 0))[3], 0)
                self.assertEqual(result.getpixel((0, 63)), (0, 0, 0, 0))
                self.assertEqual(result.getpixel((32, 32))[3], 255)

            zip_path = root / "pack.zip"
            pipeline.create_zip(outputs, zip_path)
            with zipfile.ZipFile(zip_path) as archive:
                self.assertEqual(archive.namelist(), ["01_test.png"])


if __name__ == "__main__":
    unittest.main()
