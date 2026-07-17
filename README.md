<div align="center">
  <img src="media/ai-collab.png" width="260" alt="Human and AI collaboration sticker">
  <h1>Sticker Pack Maker Skill</h1>
  <p><strong>Turn one character reference into a consistent, production-ready transparent PNG sticker pack.</strong></p>
  <p>Scene planning · character consistency · exact bubble text · chroma-key cleanup · RGBA validation · ZIP delivery</p>

  [![CI](https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/actions/workflows/ci.yml)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![GitHub stars](https://img.shields.io/github/stars/NeoWeb3Nova/sticker-pack-maker-skill?style=social)](https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/stargazers)
</div>

## Why this exists

Generating a single sticker is easy. Shipping a coherent pack is not.

The hard parts are keeping the same character across 20+ scenes, getting short text exactly right, recovering from slow or failed generations, producing real transparency instead of a fake white background, and proving every file is valid. This Skill turns that fragile sequence into a repeatable workflow.

<table>
  <tr>
    <td align="center"><img src="media/web3-wallet.png" width="220"><br><b>Web3 workflows</b></td>
    <td align="center"><img src="media/web3-dao.png" width="220"><br><b>Governance scenes</b></td>
    <td align="center"><img src="media/ai-idea.png" width="220"><br><b>AI reactions</b></td>
    <td align="center"><img src="media/ai-collab.png" width="220"><br><b>Human + AI</b></td>
  </tr>
</table>

## What you get

- A reusable Codex Skill with a strict end-to-end workflow.
- Prompt locks for character, style, exact text, and chroma background.
- Starter scene packs for AI, Web3, and workplace messaging.
- A tested Python pipeline that converts flat chroma renders to RGBA PNG.
- Soft alpha edges and fringe despill.
- Automated count, dimensions, alpha, and corner validation.
- Stable naming and ZIP packaging.
- Recovery rules that retry only missing or failed scenes.

## Install

Ask Codex:

```text
Install the sticker-pack-maker skill from
https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/tree/main/skills/sticker-pack-maker
```

Or install manually:

```bash
git clone https://github.com/NeoWeb3Nova/sticker-pack-maker-skill.git
cp -R sticker-pack-maker-skill/skills/sticker-pack-maker ~/.codex/skills/
python -m pip install -r sticker-pack-maker-skill/requirements.txt
```

PowerShell:

```powershell
git clone https://github.com/NeoWeb3Nova/sticker-pack-maker-skill.git
Copy-Item -Recurse sticker-pack-maker-skill\skills\sticker-pack-maker "$HOME\.codex\skills\"
python -m pip install -r sticker-pack-maker-skill\requirements.txt
```

## Use

```text
Use $sticker-pack-maker to create 20 Chinese workplace stickers from this
character reference. Keep the black shirt and exact chest text, use transparent
PNG backgrounds, and deliver individual files plus a ZIP.
```

Other examples:

```text
Use $sticker-pack-maker to create 20 Web3 community stickers.
Use $sticker-pack-maker to turn these 12 scene ideas into Telegram-ready PNG stickers.
Use $sticker-pack-maker to validate and package my existing blue-background renders.
```

## Pipeline

```mermaid
flowchart LR
    A["Character reference"] --> B["Scene manifest"]
    B --> C["One render per scene"]
    C --> D["Flat chroma background"]
    D --> E["Soft alpha + despill"]
    E --> F["RGBA validation"]
    F --> G["Numbered PNGs + ZIP"]
```

The image model handles creative rendering. The local pipeline handles the deterministic part:

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py process \
  --input-dir ./generated-blue \
  --output-dir ./stickers-transparent \
  --zip ./stickers-transparent.zip \
  --expected-count 20 \
  --force
```

Validate an existing pack:

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py validate \
  --input-dir ./stickers-transparent \
  --expected-count 20
```

## Repository layout

```text
skills/sticker-pack-maker/
├── SKILL.md
├── agents/openai.yaml
├── scripts/sticker_pipeline.py
├── references/
└── assets/scene-packs/
tests/
media/
docs/launch-kit.md
```

## Design decisions

- **Generate on chroma, not “transparent.”** Image generators are inconsistent at true alpha. A flat key color gives deterministic post-processing.
- **One image per call for text-critical packs.** It is slower but easier to retry, audit, and resume.
- **Keep planning separate from rendering.** A scene matrix prevents 20 nearly identical poses.
- **Validate every final file.** “Looks transparent” is not the same as a correct RGBA image.

## 中文简介

这是一个把“角色参考图 → 多场景表情包 → 真透明 PNG → 自动校验 → ZIP 打包”完整封装起来的 Codex Skill。它重点解决批量生成时的人物一致性、中文气泡文字、排队恢复、蓝底软边抠图和交付质量问题。

## Roadmap

- [ ] Telegram and WhatsApp dimension presets.
- [ ] Automatic contact sheet generation.
- [ ] Optional local OCR check for bubble text.
- [ ] Additional community-maintained scene packs.
- [ ] Benchmark set for edge quality and character consistency.

## Contributing

Ideas, scene packs, and edge-quality improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

If this saves you from manually cleaning 20 stickers, consider starring the repo and sharing one pack you made.

## License

[MIT](LICENSE). Example images are included for demonstrating the workflow; use your own character references responsibly.
