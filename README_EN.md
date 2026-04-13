<div align="center">

# 🧪 Tavern Card Distiller

### SillyTavern Character Card Distiller

**Skip the hassle of deploying SillyTavern — play character cards directly in AI Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/leigegehaha/tavern-card-distiller)](https://github.com/leigegehaha/tavern-card-distiller/stargazers)

English | [中文](README.md)

</div>

---

## 📖 What is this?

SillyTavern has an incredible ecosystem of character cards — thousands of high-quality cards spanning romance, fantasy, adventure, and more. But deploying SillyTavern is a pain: Node.js setup, reverse proxy, API configuration...

**Tavern Card Distiller** extracts the essence from tavern character cards and distills them into structured AI skills. Drop the skill into any AI Agent that supports custom instructions, and you can start immersive roleplay or creative writing immediately.

> No SillyTavern. No reverse proxy. No extra deployment needed.

---

## ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🎴 Multi-format | V1/V2/V3 card specs (PNG/WEBP/JPEG/JSON) |
| 📚 Full Extraction | Character definitions, world books, regex scripts, presets |
| 🖼️ Illustrations | Embedded image extraction + catbox.moe batch download |
| 🔓 Jailbreak | Preset auto-conversion to immersive RP rules |
| 💕 State Tracking | Affection/status systems, persistent chat history |
| 💡 Story Suggestions | 4 plot directions after each response |

---

## 🔓 About Jailbreaking

Quality character cards come with presets — sophisticated prompt engineering techniques that help AI stay in character without content filtering interference. The distiller automatically converts these techniques into natural language rules that AI Agents understand — so the AI acts fully according to character settings without breaking immersion.

---

## 🎬 Demo

### Claude Code Live Demo

https://github.com/leigegehaha/tavern-card-distiller/raw/main/screenshots/claude-code-demo.mp4

<details>
<summary>📸 More Screenshots</summary>

### Claude Code
![Claude Code Demo](screenshots/claude-code-demo.png)

### OpenClaw
![OpenClaw Demo](screenshots/openclaw-demo.png)

### OpenHanoka
![OpenHanoka Demo](screenshots/openhanoka-demo.png)

</details>

---

## 🖼️ Illustration Samples (八等分的群友)

Character cards can include scene illustrations. After distillation, a download script is auto-generated:

<table>
<tr>
<td><img src="rp-八等分的群友/assets/illustrations/神宫寺教室3cwenp.png" width="200"/><br/><sub>Nanami · Classroom</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/高坂樱月邂逅qb31bo.png" width="200"/><br/><sub>Sakuratsuki · Encounter</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/爱丽丝微笑u9o7i3.png" width="200"/><br/><sub>Alice · Smile</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/后藤冬训练fmh67u.png" width="200"/><br/><sub>Goto Fuyu · Training</sub></td>
</tr>
<tr>
<td><img src="rp-八等分的群友/assets/illustrations/美铃帅气kx2lzu.png" width="200"/><br/><sub>Meiling · Cool</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/豆咪巨大猫娘微笑114gy4.png" width="200"/><br/><sub>Doumi · Cat Girl</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/神宫寺走廊jmkihe.png" width="200"/><br/><sub>Nanami · Hallway</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/后藤冬放学偶遇2encyj.png" width="200"/><br/><sub>Goto Fuyu · After School</sub></td>
</tr>
</table>

> Full 161 illustrations available via `download_illustrations.sh` batch download from catbox.moe.

---

## ✅ Compatibility

### AI Agent Software

| Agent | Status | Notes |
|-------|--------|-------|
| **Claude Code** | ✅ Works | Best experience, native skill support |
| **OpenClaw** | ✅ Works | Good results |
| **OpenHanoka** | ✅ Works | Good results |
| WorkBuddy | ❌ Blocked | Software content filtering |
| Codex | ❌ Blocked | Software content filtering |

### Model Recommendations

| Model | Rating | Notes |
|-------|--------|-------|
| **Claude Opus 4.6** | ⭐⭐⭐ Best | Premium choice — best quality and writing |
| **Claude Sonnet** | ⭐⭐ Good | Solid balance of cost and quality |
| **DeepSeek V3.2** | ⭐⭐⭐ Best Value | Best writing among Chinese models, highly recommended |
| Chinese models (Qwen/Doubao) | ⭐ Usable | Most Chinese models work |
| GPT series | ❌ Blocked | Content filtering too strict |

> 💡 **TL;DR**: Money no object → **Claude Opus 4.6**. Best value → **DeepSeek V3.2**

---

## 🚀 Quick Start

1. Clone to your skill directory:
   ```bash
   git clone https://github.com/leigegehaha/tavern-card-distiller.git ~/.claude/skills/tavern-card-distiller
   ```

2. Use trigger words in your Agent: `角色卡`, `蒸馏角色`, `tavern card`, etc.

3. Provide a character card file path — it auto-distills into a usable RP skill.

---

## 🎭 Example Character Cards

The repo includes **11** pre-distilled character card skills covering various genres — school romance, martial arts, fantasy, historical fiction, and more.

See the [Chinese README](README.md) for the full character card table.

---

## 🗺️ Roadmap

- [x] Core distillation engine
- [x] World book, preset, regex extraction
- [x] Jailbreak preset auto-conversion
- [x] catbox.moe illustration batch download
- [ ] AI illustration generation (local image models for real-time scene illustrations)
- [ ] More Agent platform support
- [ ] Web UI for distillation

---

## 📄 License

MIT

---

<div align="center">

**If you find this useful, please give it a ⭐ Star!**

</div>
