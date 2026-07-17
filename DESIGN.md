# Design System

## Intent

The repository should feel like a personal sticker universe at midnight: expressive characters, collectible finishes, and a polished product surface. The cover creates desire; the rest of the README earns trust with real output and production detail.

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

Crimson marks decisions and quality gates. Mint indicates a passed check. White sticker borders remain visually dominant. Indigo, cyan, and restrained violet may create depth in campaign artwork; documentation surfaces stay neutral and high contrast.

## Typography

README text uses GitHub's native type system for speed and accessibility. Use short declarative headings, sentence case, and code only for commands or filenames. Avoid all-caps labels and decorative monospace copy.

## Imagery

The product cover sells the outcome: one recognizable identity becoming a personal sticker universe that belongs in everyday conversation. It should feel like launch artwork, not documentation or a pipeline diagram. Use the recurring project character and real sticker language rather than generic AI imagery.

Use a 16:9 composition with:

- One dominant character and a clear emotional focal point.
- Several finished styles, such as cartoon, pixel art, hand-drawn, clay, comic, or retro game.
- A subtle chat context that connects the collection to real use.
- Strong depth, generous edge margins, and readable sticker silhouettes.

Do not place generated text, arrows, steps, checkerboards, or technical validation cues inside the cover. Keep workflow artwork in the "How it works" section. The README supplies accessible, searchable copy below the cover.

## README hierarchy

1. Product cover and one-sentence promise.
2. Primary actions: install, view release, inspect the Skill.
3. Emotional value and real messaging-platform demo.
4. Finished-output proof.
5. A copyable first prompt.
6. The production workflow and quality contract.
7. Installation alternatives, CLI reference, roadmap, and contribution path.

## Components

- Badges communicate build, license, release, Python support, and stars.
- HTML tables are reserved for side-by-side image comparison.
- Details blocks hold secondary installation and implementation information.
- Mermaid is used only when the sequence is easier to understand visually.
- Callouts stay concise and factual.
