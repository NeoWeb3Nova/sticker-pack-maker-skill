<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<div align="center">
  <img src="media/product-cover.webp" width="100%" alt="同一个人物以卡通、像素、手绘、黏土和复古游戏等不同风格组成的个性化表情包世界">

  <h1>Sticker Pack Maker</h1>

  <p><strong>用一张角色参考图，做出人物一致、通过校验的完整表情包。</strong></p>

  <p>
    这个 Codex Skill 覆盖场景规划、人物一致性、气泡文字、色键清理、
    RGBA 校验、稳定命名和 ZIP 打包交付。
  </p>

  <p>
    <a href="#安装"><strong>安装 Skill</strong></a>
    ·
    <a href="https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/releases/latest"><strong>下载最新版本</strong></a>
    ·
    <a href="skills/sticker-pack-maker/SKILL.md"><strong>阅读 SKILL.md</strong></a>
    ·
    <a href="#和我一起做"><strong>联系 Neo</strong></a>
  </p>

  <p>
    <a href="https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/actions/workflows/ci.yml"><img src="https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/actions/workflows/ci.yml/badge.svg" alt="CI 状态"></a>
    <a href="https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/releases/latest"><img src="https://img.shields.io/github/v/release/NeoWeb3Nova/sticker-pack-maker-skill?display_name=tag" alt="最新版本"></a>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB" alt="Python 3.10 或更高版本">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-111111" alt="MIT 开源许可"></a>
    <a href="https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/stargazers"><img src="https://img.shields.io/github/stars/NeoWeb3Nova/sticker-pack-maker-skill?style=social" alt="GitHub Stars"></a>
  </p>
</div>

## 把自己变成一套聊天语言

> 你的表情，就该有你的样子。

个人表情包不只是表达情绪。它会保留你的脸、发型、衣服、习惯动作和幽默感，形成朋友和同事一眼就能认出的个人形象。

同一个人物可以做成精致卡通、像素画、手绘涂鸦、漫画线稿、3D 黏土、复古游戏角色，也可以延伸成属于品牌或社区的专属风格。完成后的透明 PNG 可以放进微信和其他热门聊天平台，让日常回复更有辨识度。

## 在微信里看看效果

<p align="center">
  <a href="https://res.cloudinary.com/dax9eqmtk/video/upload/v1784263563/Screenrecorder-2026-07-17-12-40-30-210_jlrryj.mp4">
    <img src="media/demo-poster.jpg" width="420" alt="个性化 AI 与 Web3 表情包在微信中的使用演示">
  </a>
</p>

<p align="center">
  <a href="https://res.cloudinary.com/dax9eqmtk/video/upload/v1784263563/Screenrecorder-2026-07-17-12-40-30-210_jlrryj.mp4"><strong>播放完整演示</strong></a><br>
  <sub>从个人形象到可以直接用于聊天的表情库。</sub>
</p>

## 先看成品

下面四张图片来自这个仓库中的完整流程。每张都是 1254×1254 的 RGBA PNG，画布外围透明，并使用稳定的场景名称。

<table>
  <tr>
    <td align="center" width="25%"><img src="media/web3-wallet.png" alt="钱包连接表情" width="240"></td>
    <td align="center" width="25%"><img src="media/web3-dao.png" alt="DAO 投票表情" width="240"></td>
    <td align="center" width="25%"><img src="media/ai-idea.png" alt="AI 灵感表情" width="240"></td>
    <td align="center" width="25%"><img src="media/ai-collab.png" alt="人机协作表情" width="240"></td>
  </tr>
  <tr>
    <td align="center"><code>钱包连接</code></td>
    <td align="center"><code>DAO投票</code></td>
    <td align="center"><code>灵感来了</code></td>
    <td align="center"><code>人机协作</code></td>
  </tr>
</table>

## 制作第一套表情包

安装 Skill，上传一张角色参考图，然后给 Codex 这样的提示词：

```text
使用 $sticker-pack-maker，根据这张角色参考图制作 20 张中文 AI 工作流表情包。
保持人物面部、发型、黑色上衣和胸前文字完全一致。
交付带编号的透明 PNG 文件和一个 ZIP 压缩包。
```

Skill 会规划不同场景，逐张生成对文字准确性要求高的图片。某次调用卡住时，已经完成的文件会保留下来。生成结束后，流程会去除色键背景、校验每张 PNG，并打包通过检查的文件。

## 表情包为什么容易翻车

图片生成只是其中一步。一套真正能用的表情包还需要稳定的制作规范。

| 常见问题 | 这个 Skill 的处理方式 |
| --- | --- |
| 人物在不同场景里变样 | 每条提示词都重复固定的人物设定和风格约束 |
| 气泡文字出现错别字 | 控制文字长度，逐字引用，只重试出错的场景 |
| 长批次生成卡住 | 按场景逐张生成，保留已经完成的源文件 |
| 背景看起来透明，实际仍有底色 | 把纯色色键转换成带软边的 RGBA 透明蒙版 |
| 边缘残留蓝色或绿色 | 清理半透明边缘像素中的色彩溢出 |
| 文件顺序混乱 | 使用场景清单和编号文件名 |
| ZIP 里混入坏图 | 打包前检查数量、尺寸、模式、Alpha 范围和四个角 |

## 质量标准

每一套通过验收的表情包都要满足同样的检查：

```text
PASS: files=20 sizes=[(1254, 1254)]
```

- 每个输出文件都是 RGBA 模式的 PNG。
- 所有文件尺寸一致。
- Alpha 通道同时包含完全透明和完全不透明的像素。
- 画布四个角全部透明。
- 文件名唯一、带编号，并且保持稳定。
- ZIP 中只包含通过检查的最终 PNG。

脚本负责可以自动判断的项目。Skill 还要求进行视觉复核，检查人物漂移、气泡文字错误、姿势重复、手部变形、边缘裁切和主体颜色受损。

## 工作流程

<p align="center">
  <img src="media/workflow-overview.webp" width="100%" alt="Sticker Pack Maker 从角色参考图到透明 PNG 表情包的完整流程">
</p>

图像模型负责构图和表情，本地 Python 流程负责背景移除、校验、命名和打包。创作环节保持灵活，交付检查则可以重复执行。

## 安装

### 让 Codex 安装

```text
请从下面的地址安装 sticker-pack-maker Skill：
https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/tree/main/skills/sticker-pack-maker
```

### 下载发布包

下载[最新 Skill 压缩包](https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/releases/latest)，解压 `sticker-pack-maker`，然后放到 `~/.codex/skills/` 目录中。

<details>
<summary>在 macOS 或 Linux 上手动安装</summary>

```bash
git clone https://github.com/NeoWeb3Nova/sticker-pack-maker-skill.git
cp -R sticker-pack-maker-skill/skills/sticker-pack-maker ~/.codex/skills/
python -m pip install -r sticker-pack-maker-skill/requirements.txt
```

</details>

<details>
<summary>在 Windows PowerShell 中手动安装</summary>

```powershell
git clone https://github.com/NeoWeb3Nova/sticker-pack-maker-skill.git
Copy-Item -Recurse sticker-pack-maker-skill\skills\sticker-pack-maker "$HOME\.codex\skills\"
python -m pip install -r sticker-pack-maker-skill\requirements.txt
```

</details>

## 直接运行处理脚本

不调用完整 Skill，也可以直接运行可重复的后处理步骤：

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py process \
  --input-dir ./generated-chroma \
  --output-dir ./stickers-transparent \
  --zip ./stickers-transparent.zip \
  --expected-count 20 \
  --force
```

校验一个已有目录：

```bash
python skills/sticker-pack-maker/scripts/sticker_pipeline.py validate \
  --input-dir ./stickers-transparent \
  --expected-count 20
```

生成器返回随机文件名时，可以传入一份 JSON 场景清单，为每个场景指定 `source` 和 `filename`。仓库中提供了场景清单示例和完整格式说明。

## 场景包模板

| 场景包 | 数量 | 包含内容 |
| --- | ---: | --- |
| [AI](skills/sticker-pack-maker/assets/scene-packs/ai.json) | 20 | 提示词、生成、检索、智能体、工具、审核 |
| [Web3](skills/sticker-pack-maker/assets/scene-packs/web3.json) | 20 | 钱包、Gas、跨链、铸造、治理、审计 |
| [职场](skills/sticker-pack-maker/assets/scene-packs/workplace.json) | 8 | 确认、进度、会议、完成、支持 |

这些文件可以直接作为规划模板。根据受众修改文字、动作、情绪和文件名字段即可。

## 目前的限制

- 按场景逐张生成会比一次大批量生成更慢，但重试和复核更可控。
- 图像模型仍可能写错图片中的文字。这个流程会把问题限制在单个场景内。
- 主体避开色键颜色时，背景清理效果最好。人物需要蓝色或绿色细节时，应改用其他色键。
- 头发、烟雾、玻璃、反射和半透明材质可能需要原生透明背景或手动清理。
- 风格约束可以减少人物漂移，但无法保证不同模型输出像素级一致的角色。

## 仓库内容

```text
skills/sticker-pack-maker/
├── SKILL.md
├── agents/openai.yaml
├── scripts/sticker_pipeline.py
├── references/
│   ├── prompt-patterns.md
│   ├── quality-checklist.md
│   └── scene-planning.md
└── assets/scene-packs/
    ├── ai.json
    ├── web3.json
    └── workplace.json
```

仓库还包括中英文 README、单元测试、GitHub Actions CI、贡献指南、安全问题报告方式、示例图片和[发布资料包](docs/launch-kit.md)。[PRODUCT.md](PRODUCT.md) 与 [DESIGN.md](DESIGN.md) 记录了项目定位和 README 的视觉设计依据。

## 路线图

- [ ] Telegram 与 WhatsApp 导出预设
- [ ] 表情包总览图生成
- [ ] 可选的本地 OCR 气泡文字检查
- [ ] 更多由社区维护的场景包
- [ ] 边缘质量与人物一致性基准测试

## 参与贡献

欢迎提交可复用的场景清单、能够稳定复现的边缘案例、更好的蒙版算法，或其他智能体运行环境的使用文档。发起 Pull Request 前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

用这个 Skill 发布表情包后，可以在 [Show and tell 讨论区](https://github.com/NeoWeb3Nova/sticker-pack-maker-skill/discussions)分享结果和场景清单。优秀案例会收录到 README 中。

## 和我一起做

如果你在做 AI、Web3 或创作者工具，欢迎告诉我你正在开发什么。我愿意一起设计场景包、做产品集成、测试复杂案例，也希望看到值得收录进仓库的表情包作品。

<table>
  <tr>
    <td align="center" width="36%">
      <a href="media/wechat-neo.png"><img src="media/wechat-neo.png" width="280" alt="Web3的尼奥微信二维码"></a><br>
      <strong>微信 · Web3的尼奥</strong><br>
      <sub>扫码添加，好友备注请写“Sticker Pack Maker”。</sub>
    </td>
    <td valign="middle" width="64%">
      <h3>Neo · AI × Web3 开发者</h3>
      <p>我在做 AI、Web3 和创作者工作流相关的开源工具。如果你遇到了当前流程处理不好的角色、想接入自己的产品，或者希望为社区定制一套表情包，可以直接联系我。</p>
      <p>
        <a href="https://amshe.fun"><img src="https://img.shields.io/badge/Website-amshe.fun-6E56CF?style=for-the-badge&logo=safari&logoColor=white" alt="访问 amshe.fun"></a>
        <a href="https://x.com/NeoWeb3Nova"><img src="https://img.shields.io/badge/X-@NeoWeb3Nova-000000?style=for-the-badge&logo=x&logoColor=white" alt="在 X 上关注 NeoWeb3Nova"></a>
        <a href="https://t.me/neo_web3_nova"><img src="https://img.shields.io/badge/Telegram-neo__web3__nova-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="通过 Telegram 联系 neo_web3_nova"></a>
      </p>
      <p><strong>觉得有用？</strong>给仓库点个 Star，分享你的作品，或者来打个招呼。</p>
    </td>
  </tr>
</table>

## 开源许可

[MIT](LICENSE)。示例图片用于展示工作流程，请确保你有权发布所用的角色参考图和生成素材。
