---
name: sticker-pack-maker
description: Create production-ready messaging sticker packs from character reference images and a scene list. Plan distinct scenes, preserve character consistency, generate square stickers with exact speech-bubble text, convert chroma backgrounds into true RGBA transparent PNGs, validate every image, name files, and package ZIP archives. Use when users request sticker packs, emoji packs, reaction images, transparent PNG stickers, or themed series such as workplace, Web3, AI, community, customer-support, or social-media stickers.
---

# Sticker Pack Maker

Create coherent sticker series rather than unrelated one-off illustrations. Preserve the reference character, make every scene semantically distinct, and deliver validated transparent PNG files plus an optional ZIP.

## Output contract

- Produce one square PNG per scene.
- Preserve the character's face, hair, outfit, palette, outline weight, and rendering style.
- Keep requested speech-bubble text exact and legible.
- Use a thick white sticker border.
- Deliver RGBA images with fully transparent outer corners.
- Use stable numbered filenames such as `01_收到.png`.
- Validate the count, dimensions, alpha channel, and corner transparency.

## Workflow

### 1. Establish the pack brief

Derive sensible defaults instead of blocking when details are absent:

- Character: use the supplied reference image.
- Count: use the requested count; otherwise default to 20.
- Canvas: square, at least 1024×1024.
- Language: match the user's language.
- Style: match the reference image.
- Background: final transparent PNG.
- Delivery: individual PNG files and one ZIP.

Record any invariant shirt text, logo, accessories, or forbidden elements. Do not silently replace them.

### 2. Plan non-overlapping scenes

Create a numbered scene manifest before generation. Each scene needs:

- `text`: short bubble copy, usually 2–6 characters for Chinese.
- `action`: a visible pose or prop that communicates the meaning without text.
- `emotion`: a distinct facial expression.
- `filename`: stable numbered output name.

Read [references/scene-planning.md](references/scene-planning.md) when the user requests a themed pack or when more than 10 scenes are needed. Reuse a starter manifest from `assets/scene-packs/` when it fits.

### 3. Generate chroma-key source images

Use the available image-generation tool with the character reference attached. Generate one image per call when exact text and consistency matter; small batches increase latency variance and make failures harder to recover.

Read [references/prompt-patterns.md](references/prompt-patterns.md) and build every prompt from the same character/style lock. Require:

- A perfectly flat, uniform `#0000FF` background.
- No blue elements in the character, props, border, or text.
- One character unless the scene explicitly requires a robot or secondary figure.
- Exact bubble text in quotation marks.
- No watermark, signature, unrelated text, duplicate limbs, or cropped sticker border.

Do not depend on native transparency from the generator. Chroma-key post-processing is deterministic and verifiable.

### 4. Convert to true transparency

Install the lightweight dependencies once:

```bash
python -m pip install -r skills/sticker-pack-maker/requirements.txt
```

Process, validate, and zip a source directory:

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py process \
  --input-dir ./generated-blue \
  --output-dir ./stickers-transparent \
  --zip ./stickers-transparent.zip \
  --expected-count 20 \
  --force
```

When generated filenames are random, provide a JSON manifest with `source` and `filename` fields:

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py process \
  --input-dir ./generated-blue \
  --output-dir ./stickers-transparent \
  --manifest ./manifest.json \
  --zip ./stickers.zip \
  --force
```

The script samples the border color, builds a soft alpha matte, removes chroma spill on fringe pixels, saves RGBA PNG files, validates them, and creates the archive.

### 5. Perform visual QA

Run deterministic validation:

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py validate \
  --input-dir ./stickers-transparent \
  --expected-count 20
```

Then visually inspect every image or at least a contact-sheet-sized view. Regenerate any image with:

- Incorrect or misspelled bubble text.
- Character drift or wrong shirt/logo text.
- Repeated scene composition.
- Extra fingers, limbs, people, or text.
- Blue subject elements damaged by chroma removal.
- Cropped white sticker borders.

Read [references/quality-checklist.md](references/quality-checklist.md) for the full acceptance checklist.

### 6. Deliver and report

Return clickable paths to:

- The transparent PNG directory.
- The ZIP archive.
- One representative preview.

Report the count, dimensions, RGBA validation result, and any regenerated items. Never claim completion while image-generation calls are still queued.

## Recovery rules

- If a generation call stalls, retain completed source images and retry only the missing scene.
- If exact text fails, simplify the composition and regenerate that image alone.
- If chroma removal damages blue subject details, regenerate with a non-blue palette or use a different key color and pass `--key-color`.
- If filenames no longer match scene order, build a manifest instead of relying on timestamps.
- Never delete original generated images during post-processing.

## Resources

- `scripts/sticker_pipeline.py`: chroma removal, RGBA validation, renaming, and ZIP packaging.
- `references/prompt-patterns.md`: generation prompt locks and templates.
- `references/scene-planning.md`: scene diversity framework.
- `references/quality-checklist.md`: deterministic and visual QA.
- `assets/scene-packs/`: reusable AI, Web3, and workplace scene manifests.
