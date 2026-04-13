# Tavern Card Distiller

将 SillyTavern / TavernAI 酒馆角色卡蒸馏为 AI Agent skill，实现沉浸式角色扮演对话。

**告别繁琐的酒馆部署，直接在 AI Agent 里畅玩角色卡。**

## 这是什么？

玩过 SillyTavern 的朋友都知道，酒馆的角色卡生态非常丰富——几千张高质量角色卡，从校园恋爱到奇幻冒险应有尽有。但部署酒馆太麻烦了：Node.js 环境、反代配置、API 对接，折腾半天可能还跑不起来。

**Tavern Card Distiller** 把酒馆角色卡里的精华提取出来，蒸馏成一个结构化的 AI skill。你把这个 skill 丢进任何支持自定义指令的 AI Agent 里，就能直接开始沉浸式角色扮演或辅助创作小说。

不需要酒馆，不需要反代，不需要任何额外部署。

## 核心功能

- 支持 V1/V2/V3 角色卡规范（PNG/WEBP/JPEG/JSON）
- 自动提取角色定义、世界书、正则脚本、预设指令
- 内置插图提取 + catbox.moe 外链插图批量下载
- 破限预设自动转化为沉浸式角色扮演规则
- 好感度/状态系统、聊天历史持久化、剧情建议
- AI 生成插图（开发中）

## 破限能力

好的角色卡都会带预设，里面包含了一整套让 AI 进入角色、不受内容审查限制的提示词技术。蒸馏器会把这些技术自动转化成 Agent 能理解的自然语言规则——AI 可以完全按照角色设定来行动，该甜的甜，该辣的辣，不会动不动弹一句"作为 AI 我无法……"。

## 效果展示

### Claude Code
![Claude Code 示例](screenshots/claude-code-demo.png)

### OpenClaw
![OpenClaw 示例](screenshots/openclaw-demo.png)

### OpenHanoka
![OpenHanoka 示例](screenshots/openhanoka-demo.png)

## 兼容性

### AI Agent 软件

| Agent 软件 | 状态 | 说明 |
|-----------|------|------|
| Claude Code | ✅ 可用 | 体验最佳，原生支持 skill 系统 |
| OpenClaw | ✅ 可用 | 效果良好 |
| OpenHanoka | ✅ 可用 | 效果良好 |
| WorkBuddy | ❌ 不可用 | 软件审核机制限制 |
| Codex | ❌ 不可用 | 软件审核机制限制 |

### 模型推荐

| 模型 | 状态 | 说明 |
|------|------|------|
| Claude Opus 4.6 | ⭐ 最佳 | 不差钱无脑选，体验最好，文案质量最高 |
| Claude Sonnet | ✅ 推荐 | 性价比不错，效果好 |
| DeepSeek V3.2 | ⭐ 性价比之王 | 国产模型里文案描述最好，强烈推荐 |
| 国产模型（通义/豆包等） | ✅ 基本可用 | 大部分国产模型都能用 |
| GPT 系列 | ❌ 不可用 | 审核太强，无法破限 |

> **总结**：如果不差钱，无脑用 **Claude Opus 4.6**，体验最好，文案也最好。追求性价比，推荐 **DeepSeek V3.2**，国产里最强。

## 使用方法

1. 将此目录放入 `~/.claude/skills/tavern-card-distiller/`（或对应 Agent 的 skill 目录）
2. 在 Agent 中使用触发词：`角色卡`、`蒸馏角色`、`tavern card` 等
3. 提供角色卡文件路径，自动蒸馏为可用的 RP skill

## 目录结构

```
tavern-card-distiller/
├── SKILL.md              # Skill 定义文件
├── scripts/
│   ├── extract_card.py   # 角色卡数据提取
│   ├── generate_skill.py # Skill 生成器
│   └── quick_validate.py # 快速验证工具
├── rp-八等分的群友/       # 示例：多角色群像 RP
├── rp-傲娇大小姐凌夜/    # 示例：校园恋爱 RP
└── rp-母狗学姐白姝颜/    # 示例：调教系 RP
```

## 示例角色卡

仓库包含三个已蒸馏的角色卡 skill 作为示例：

- **八等分的群友**：27岁落魄青年穿越回高中，五位红线牵连者的姻缘故事。161张场景插图。
- **傲娇大小姐凌夜**：曾经霸凌你的傲娇大小姐，如今没你在身边就睡不着。多剧情线。
- **母狗学姐白姝颜**：学生会文艺部部长的双面生活。状态追踪系统。

> 注意：插图 PNG 文件未包含在仓库中。八等分的群友包含 `download_illustrations.sh` 脚本，运行即可从 catbox.moe 批量下载 161 张插图。

## 开发计划

- [x] 角色卡蒸馏核心功能
- [x] 世界书、预设、正则提取
- [x] 破限预设自动转化
- [x] catbox.moe 插图批量下载
- [ ] AI 插图生成（利用本地图片模型，根据剧情实时生成场景插图，包括大尺度内容）
- [ ] 更多 Agent 平台适配

## License

MIT
