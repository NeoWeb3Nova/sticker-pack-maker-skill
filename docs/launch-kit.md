# Launch kit

This playbook focuses on useful demonstrations and community feedback. Do not buy stars, automate fake engagement, or mass-spam unrelated communities.

## Positioning

**One-line promise:** Turn one character reference into a consistent, validated transparent PNG sticker pack.

**Technical hook:** Image generation is the creative half; deterministic alpha cleanup, validation, resumability, and packaging are the production half.

**Audience:**

- Codex and agent-skill users.
- Community and social-media managers.
- Web3 and AI project operators.
- Indie hackers building branded messaging assets.
- Designers who want repeatable AI-assisted production.

## Launch checklist

1. Add GitHub topics: `codex`, `agent-skill`, `image-generation`, `sticker-pack`, `transparent-png`, `python`, `web3`, `ai`.
2. Confirm the README hero, four examples, CI badge, license, and install prompt render correctly.
3. Publish a tagged `v0.1.0` release with a short demo and installation snippet.
4. Pin the repository on the GitHub profile.
5. Post a 15–30 second screen recording: reference → four generated scenes → transparent checkerboard → ZIP.
6. Ask early users for scene-pack pull requests rather than only asking for stars.

## Ready-to-post: English

### X / LinkedIn

```text
Generating one sticker is easy. Shipping 20 consistent stickers with correct
text, real transparency, stable filenames, and a clean ZIP is the hard part.

I open-sourced Sticker Pack Maker, a Codex Skill that turns one character
reference into a production-ready sticker pack:

• scene planning
• consistency + exact-text prompt locks
• deterministic chroma → RGBA cleanup
• alpha validation
• resumable per-scene generation

MIT licensed: https://github.com/NeoWeb3Nova/sticker-pack-maker-skill

What scene pack should I add next?
```

### Hacker News

```text
Show HN: A Codex Skill for production-ready transparent sticker packs

I built this after discovering that generating an image was the easy step.
The failure-prone parts were maintaining a character across many scenes,
recovering individual failed renders, removing backgrounds without blue halos,
and verifying that every PNG really had a valid alpha channel.

The repo includes the Skill instructions, reusable AI/Web3/workplace scene
manifests, and a tested local chroma-to-RGBA pipeline. Feedback on the alpha
matte and agent workflow would be especially useful.
```

## Ready-to-post: 中文

```text
做一张表情包很容易，难的是稳定交付 20 张：

人物不能漂、中文不能错、每张场景要不同、背景必须是真透明，
中途卡住还得能断点续做，最后要自动校验并打 ZIP。

我把完整流程开源成了 Sticker Pack Maker Codex Skill：

✅ AI / Web3 / 职场场景模板
✅ 人物一致性与精确文字 Prompt
✅ 蓝底转 RGBA 透明软边
✅ 透明通道自动校验
✅ 单张失败单张重试

GitHub： https://github.com/NeoWeb3Nova/sticker-pack-maker-skill

欢迎提一个你最想要的场景包，或者直接贡献 PR。
```

## 30-day cadence

- Day 1: GitHub release, X/LinkedIn post, Chinese community post.
- Day 3: Share a short technical note about why native transparency fails.
- Day 7: Release one community-requested scene pack.
- Day 10: Publish a before/after edge-quality comparison.
- Day 14: Add a contributor showcase to the README.
- Day 21: Ship the most-requested platform preset.
- Day 30: Publish metrics, lessons, and the next roadmap vote.

## Metrics

Track useful adoption signals weekly:

- Unique cloners and repository visitors.
- Install questions and successful-pack reports.
- External contributors and merged scene packs.
- Stars-to-visitors ratio.
- Issues that reveal unclear instructions.

Optimize for successful users and contributors; stars follow demonstrated utility.
