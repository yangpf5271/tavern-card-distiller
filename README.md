<div align="center">

# 🧪 Tavern Card Distiller

### 酒馆角色卡蒸馏器

**告别繁琐的酒馆部署，直接在 AI Agent 里畅玩角色卡**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/leigegehaha/tavern-card-distiller)](https://github.com/leigegehaha/tavern-card-distiller/stargazers)

[English](README_EN.md) | 中文

</div>

---

## 📖 这是什么？

SillyTavern 的角色卡生态非常丰富——几千张高质量角色卡，从校园恋爱到奇幻冒险应有尽有。但部署酒馆太麻烦了：Node.js 环境、反代配置、API 对接……

**Tavern Card Distiller** 把酒馆角色卡里的精华提取出来，蒸馏成结构化的 AI skill。丢进任何支持自定义指令的 AI Agent，就能直接开始沉浸式角色扮演或辅助创作小说。

> 不需要酒馆，不需要反代，不需要任何额外部署。

---

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 🎴 多格式支持 | V1/V2/V3 角色卡规范（PNG/WEBP/JPEG/JSON） |
| 📚 完整提取 | 角色定义、世界书、正则脚本、预设指令 |
| 📋 13章节标准化模板 | 统一输出结构：核心规则、状态系统、剧情建议、开场白等 |
| 👤 用户身份系统 | 自动识别玩家名字，持久化存储，无需每次输入 |
| 💬 聊天历史 | 多 session 管理，随时从上次中断处继续 |
| 🖼️ 插图系统 | 内置插图提取 + catbox.moe 外链批量下载 + AI 实时生图 |
| 🔓 破限能力 | 三层预设注入自动转化为沉浸式角色扮演规则 |
| 💕 状态追踪 | 好感度/情绪/变量系统，剧情进展实时追踪 |
| 💡 剧情建议 | 每次回复后提供 4 个剧情发展方向 |
| 🌐 跨平台兼容 | Claude Code / OpenClaw / OpenHanoka / Hermes 多平台支持 |

---

## 📋 13 章节标准化模板

蒸馏器生成的每个角色 skill 都包含 13 个标准化章节，保证输出质量和一致性：

| # | 章节 | 内容 |
|---|------|------|
| 1 | Frontmatter | 角色名、描述、触发词 |
| 2 | 核心规则 | 角色沉浸、叙事引擎、行为边界 |
| 3 | 输出配置 | 字数控制、文风切换（轻小说/网文/纯文学/剧本） |
| 4 | 用户身份 | 玩家名字自动识别与持久化 |
| 5 | 聊天历史 | 多 session 管理、存档读档 |
| 6 | 启动菜单 | 新游戏 / 继续游戏两级菜单 |
| 7 | 角色设定 | 从卡片提取的完整角色资料 |
| 8 | 状态系统 | 好感度、情绪、自定义变量追踪 |
| 9 | 写作风格 | 叙事风格指南、格式要求 |
| 10 | 插图系统 | 场景插图触发、下载、多平台发送 |
| 11 | 剧情建议 | 每次回复后 4 个发展方向 |
| 12 | 参考资料 | 世界书、写作指南等外部文档 |
| 13 | 默认开场白 | 角色卡片原始 first_mes |

---

## 🔓 关于破限

好的角色卡都会带预设，里面包含了一整套让 AI 进入角色、不受内容审查限制的提示词技术。

蒸馏器采用**三层注入结构**自动转化这些预设：

| 层级 | 来源 | 转化为 |
|------|------|--------|
| 第一层 | `system_prompt` | 身份重置声明 + 规则系统 |
| 第二层 | NSFW prompt + System notes | 内容自由度 + 感官细节要求 |
| 第三层 | `post_history_instructions` | 禁止 OOC + 输出规范 + 反注入防护 |

AI 可以完全按照角色设定来行动，该甜的甜，该辣的辣，不会动不动弹一句"作为 AI 我无法……"。

---

## 🎬 效果演示

### Claude Code 实机演示

https://github.com/leigegehaha/tavern-card-distiller/raw/main/screenshots/claude-code-demo.mp4

<details>
<summary>📸 更多截图</summary>

### Claude Code
![Claude Code 示例](screenshots/claude-code-demo.png)

### OpenClaw
![OpenClaw 示例](screenshots/openclaw-demo.png)

### OpenHanoka
![OpenHanoka 示例](screenshots/openhanoka-demo.png)

</details>

---

## 🖼️ 插图示例（八等分的群友）

角色卡可包含场景插图，蒸馏后自动生成下载脚本。以下为部分示例：

<table>
<tr>
<td><img src="rp-八等分的群友/assets/illustrations/神宫寺教室3cwenp.png" width="200"/><br/><sub>神宫寺七海 · 教室</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/高坂樱月邂逅qb31bo.png" width="200"/><br/><sub>高坂樱月 · 邂逅</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/爱丽丝微笑u9o7i3.png" width="200"/><br/><sub>爱丽丝 · 微笑</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/后藤冬训练fmh67u.png" width="200"/><br/><sub>后藤冬 · 训练</sub></td>
</tr>
<tr>
<td><img src="rp-八等分的群友/assets/illustrations/美铃帅气kx2lzu.png" width="200"/><br/><sub>美铃 · 帅气</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/豆咪巨大猫娘微笑114gy4.png" width="200"/><br/><sub>豆咪 · 猫娘形态</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/神宫寺走廊jmkihe.png" width="200"/><br/><sub>神宫寺七海 · 走廊</sub></td>
<td><img src="rp-八等分的群友/assets/illustrations/后藤冬放学偶遇2encyj.png" width="200"/><br/><sub>后藤冬 · 放学偶遇</sub></td>
</tr>
</table>

> 完整 161 张插图可通过 `download_illustrations.sh` 脚本从 catbox.moe 批量下载。

### 角色 Skill 中的插图目录

![插图目录预览](screenshots/illustrations-preview.png)

### 多平台插图发送

插图系统自动适配发送平台：微信/飞书等聊天网关自动压缩发送，桌面端 CLI 直接用系统打开。

---

## ✅ 兼容性

### AI Agent 软件

| Agent 软件 | 状态 | 说明 |
|-----------|------|------|
| **Claude Code** | ✅ 可用 | 体验最佳，原生支持 skill 系统 |
| **Hermes** | ✅ 可用 | 完整支持，通过 install-github-skill 一键安装 |
| **OpenClaw** | ✅ 可用 | 效果良好 |
| **OpenHanoka** | ✅ 可用 | 效果良好 |
| WorkBuddy | ❌ 不可用 | 软件审核机制限制 |
| Codex | ❌ 不可用 | 软件审核机制限制 |

### 模型推荐

| 模型 | 推荐度 | 说明 |
|------|--------|------|
| **Claude Opus 4.6** | ⭐⭐⭐ 最佳 | 不差钱无脑选，体验最好，文案质量最高 |
| **Claude Sonnet** | ⭐⭐ 推荐 | 性价比不错，效果好 |
| **DeepSeek V3.2** | ⭐⭐⭐ 性价比之王 | 国产模型里文案描述最好，强烈推荐 |
| 国产模型（通义/豆包等） | ⭐ 可用 | 大部分国产模型都能用 |
| GPT 系列 | ❌ 不可用 | 审核太强，无法破限 |

> 💡 **总结**：不差钱 → **Claude Opus 4.6**；追求性价比 → **DeepSeek V3.2**

---

## 🚀 使用方法

### 方式一：Hermes 一键安装（推荐）

```bash
# 在 Hermes Agent 中直接说：
> 帮我从 GitHub 安装 tavern-card-distiller
```

AI 会自动 clone、配置、验证，安装完成后即可使用。

### 方式二：手动安装

```bash
# 克隆到 skill 目录（以 Claude Code 为例）
git clone https://github.com/leigegehaha/tavern-card-distiller.git ~/.claude/skills/tavern-card-distiller

# 如需多平台同步（Hermes/OpenHanoka 等）
ln -s ~/.claude/skills/tavern-card-distiller ~/.hermes/skills/creative/tavern-card-distiller
```

### 蒸馏角色卡

在 Agent 中使用触发词 `角色卡`、`蒸馏角色`、`tavern card` 等，并提供角色卡文件路径：

```
> 帮我蒸馏这张角色卡：~/Downloads/my-character.png
```

蒸馏器会自动提取角色定义、世界书、预设、插图等内容，生成一个完整的 RP skill 目录（如 `rp-角色名/`）。

### 直接开始聊天

蒸馏完成后，生成的 skill 会自动注册到你的 AI Agent 中。之后只需说出角色名或触发词即可：

```
> 凌夜          ← 直接说角色名即可启动
> 八等分的群友   ← 触发对应角色的 skill
```

AI Agent 会自动加载角色设定、世界观、好感度系统等，进入完全沉浸的角色扮演模式。你可以：
- 🎭 与角色自由对话，推进剧情
- 💕 体验好感度/状态追踪系统
- 🖼️ 在关键剧情节点自动展示场景插图
- 💬 多条剧情线随时切换，聊天历史自动存档
- 💡 每次回复后获得 4 个剧情发展建议

> 💡 **总结**：蒸馏一次，永久可用。蒸馏好的 skill 就像给 AI Agent 装了一个角色扮演模组。

### 已蒸馏角色可直接使用

本仓库已包含 **11 个**蒸馏好的角色卡 skill，克隆后无需蒸馏，直接说出角色名即可开始游玩。

---

## 📁 目录结构

```
tavern-card-distiller/
├── SKILL.md                    # 蒸馏器 Skill 定义（含 13 章节模板）
├── README.md                   # 项目说明（你正在看）
├── README_EN.md                # English version
├── scripts/
│   ├── extract_card.py         # 角色卡数据提取（V1/V2/V3）
│   ├── generate_skill.py       # Skill 生成器（13章节模板）
│   └── quick_validate.py       # 快速验证工具
├── screenshots/                # 演示截图和视频
│
├── rp-八等分的群友/             # 🎭 多角色群像 · 校园姻缘
├── rp-傲娇大小姐凌夜/          # 💜 傲娇校园恋爱
├── rp-母狗学姐白姝颜/          # 🔥 调教系
├── rp-出云国/                  # ⚔️ 日式奇幻
├── rp-天罗宫/                  # 🏯 武侠宫廷
├── rp-大夏王朝/                # 👑 王朝争霸
├── rp-清漪映雪/                # ❄️ 古风唯美
├── rp-兽血沸腾/                # 🐉 奇幻冒险
├── rp-大秦纵横/                # 🗡️ 战国纵横
├── rp-色色任务系统/             # 🎮 任务系统
└── rp-茱莉娅和艾丽卡/          # 🏕️ 1989意大利夏日
```

每个 `rp-*` 目录包含完整的角色 skill：

```
rp-<角色名>/
├── SKILL.md              # 13章节角色主文件
├── user_profile.json     # 用户身份（首次使用时填充）
├── config.json           # 输出配置（字数/文风）
├── chat_history/         # 聊天历史存档
├── references/           # 参考资料
│   ├── world_book.md     # 世界书
│   ├── writing_guide.md  # 写作指南
│   ├── state_system.md   # 状态系统
│   ├── routes.md         # 剧情线
│   ├── regex_rules.md    # 格式规则
│   └── preset.md         # 预设/破限指令
└── assets/               # 插图资源
    ├── illustrations/    # 场景插图
    ├── illustrations_map.json
    └── download_illustrations.sh
```

---

## 🎭 示例角色卡

仓库包含 **11 个**已蒸馏的角色卡 skill：

| 角色卡 | 类型 | 特色 |
|--------|------|------|
| **八等分的群友** | 多角色群像 | 5位红线牵连者，161张场景插图，好感度系统 |
| **傲娇大小姐凌夜** | 校园恋爱 | 多剧情线，好感度阶段，睡眠状态系统 |
| **母狗学姐白姝颜** | 调教系 | 双面性格，状态追踪，道具系统 |
| **出云国** | 日式奇幻 | 沉浸式世界观 |
| **天罗宫** | 武侠宫廷 | 宫廷权谋 |
| **大夏王朝** | 王朝争霸 | 历史架空 |
| **清漪映雪** | 古风唯美 | 诗意叙事 |
| **兽血沸腾** | 奇幻冒险 | 热血战斗 |
| **大秦纵横** | 战国纵横 | 策略博弈 |
| **色色任务系统** | 任务系统 | 系统化玩法 |
| **茱莉娅和艾丽卡** | 夏日冒险 | 1989年意大利露营双女主 |

---

## 🗺️ 开发计划

- [x] 角色卡蒸馏核心功能（V1/V2/V3）
- [x] 世界书、预设、正则提取
- [x] 破限预设三层注入自动转化
- [x] 13 章节标准化模板
- [x] 用户身份系统 + 聊天历史持久化
- [x] catbox.moe 插图批量下载 + 多平台发送
- [x] Hermes 平台完整适配
- [ ] AI 实时插图生成（根据剧情动态生成场景插图）
- [ ] Web UI 蒸馏界面
- [ ] 更多 Agent 平台适配

---

## 📄 License

MIT

---

<div align="center">

**如果觉得有用，请给个 ⭐ Star！**

</div>
