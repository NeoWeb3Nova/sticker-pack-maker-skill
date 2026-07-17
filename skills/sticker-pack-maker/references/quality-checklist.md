# Quality checklist

## Deterministic checks

- Requested file count is exact.
- Every output is PNG in RGBA mode.
- All images have identical dimensions.
- Alpha minimum is 0 and maximum is 255.
- All four outer corners are fully transparent.
- Filenames are numbered, unique, and stable.
- ZIP contains only the intended final PNG files.

Run:

```bash
python scripts/sticker_pipeline.py validate --input-dir OUTPUT --expected-count COUNT
```

## Visual checks

- Character identity matches the reference across the whole pack.
- Outfit and invariant chest/logo text are exact.
- Speech bubble copy is correct, complete, and unobstructed.
- Each sticker has a different pose, prop, emotion, or composition.
- Hands, fingers, arms, faces, and props are anatomically coherent.
- White sticker border is continuous and not cropped.
- Transparent edges have no visible blue halo.
- Intended blue/cyan subject details were not removed.
- The sticker remains legible at 128×128 display size.

## Regeneration policy

Regenerate only failed scenes. Keep accepted source files immutable so a retry cannot reorder or replace the rest of the pack.
