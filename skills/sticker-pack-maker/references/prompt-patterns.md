# Prompt patterns

Use one immutable character/style lock across the entire pack, then add only scene-specific action, emotion, props, and exact text.

## Character and style lock

```text
Create one square messaging sticker matching the recurring chibi character in the attached reference. Preserve the same face, hairstyle, skin tone, body proportions, outfit, chest text, palette, bold dark outlines, warm cel shading, and thick white sticker border. Center the composition with generous padding and crisp edges.
```

State invariant text explicitly:

```text
The black T-shirt must contain exactly “AI” in mint-white letters. Do not write WEB3.
```

## Scene block

```text
Scene: {visible action and props}. Emotion: {expression}. The pose must communicate {intent} without relying on text.
```

Prefer concrete verbs such as pointing, bowing, typing, checking, voting, celebrating, waiting, comparing, or high-fiving. Avoid vague instructions such as “show AI” or “make it dynamic.”

## Exact text block

```text
Add one clean white oval speech bubble with a black outline in the upper right containing exactly the Chinese text “{text}”. Keep every character large, black, and unobstructed.
```

Keep Chinese bubble text short. Generate text-critical stickers individually.

## Chroma and negative lock

```text
Background must be a perfectly flat uniform pure chroma blue #0000FF with no gradient, texture, shadows, glow, or reflections. Use no blue in the subject, props, border, or text. No watermark, signature, unrelated text, misspelling, duplicate limbs, cropped border, or extra human.
```

## Complete template

```text
Create one square messaging sticker matching the recurring chibi character in the attached reference. Preserve {character invariants}. Scene: {action}. Emotion: {emotion}. Add one white oval speech bubble with black outline in the upper right containing exactly “{text}”. Polished 2D kawaii cartoon, bold dark outlines, warm cel shading, thick white sticker border, centered composition, generous padding, crisp edges. Background must be perfectly flat uniform #0000FF with no gradient, texture, shadows, or blue subject elements. No watermark, signature, unrelated text, misspelling, duplicate limbs, cropped border, or extra human.
```

## Retry prompt

When only the text is wrong, do not broaden the request:

```text
Regenerate the same sticker composition and character. Correct only the speech bubble so it reads exactly “{text}”. Keep the pure #0000FF background and all other invariants unchanged.
```
