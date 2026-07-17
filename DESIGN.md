# Design System

## Intent

The repository should feel like a sticker production bench at midnight: bright finished characters on a precise, dark working surface. The imagery carries personality; typography and structure carry trust.

## Color

Use a committed palette for generated repository artwork:

```css
:root {
  --color-bg: oklch(0.080 0.000 0);
  --color-surface: oklch(0.150 0.008 10);
  --color-ink: oklch(0.980 0.000 0);
  --color-muted: oklch(0.720 0.015 10);
  --color-primary: oklch(0.560 0.200 10.4);
  --color-accent: oklch(0.840 0.120 165);
}
```

Crimson marks decisions and quality gates. Mint indicates a passed check. White sticker borders remain visually dominant. Do not tint the dark background toward blue or purple.

## Typography

README text uses GitHub's native type system for speed and accessibility. Use short declarative headings, sentence case, and code only for commands or filenames. Avoid all-caps labels and decorative monospace copy.

## Imagery

The Hero visual shows the transformation from one character reference into a finished pack. Use real project stickers, not generic AI imagery. Give every sticker a clean silhouette and enough space to read at repository width.

Use a 16:9 or wider composition with:

- One reference or source panel.
- A compact transformation path.
- A fan or row of finished transparent stickers.
- Small visual cues for alpha, validation, and packaging.

Do not place generated text inside the Hero. The README supplies accessible, searchable copy below it.

## README hierarchy

1. Hero artwork and one-sentence promise.
2. Primary actions: install, view release, inspect the Skill.
3. Finished-output proof.
4. A copyable first prompt.
5. The production workflow and quality contract.
6. Installation alternatives and CLI reference.
7. Starter packs, repository structure, roadmap, and contribution path.

## Components

- Badges communicate build, license, release, Python support, and stars.
- HTML tables are reserved for side-by-side image comparison.
- Details blocks hold secondary installation and implementation information.
- Mermaid is used only when the sequence is easier to understand visually.
- Callouts stay concise and factual.
