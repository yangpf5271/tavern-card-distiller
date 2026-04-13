# Tavern Card Distiller

将 SillyTavern / TavernAI 酒馆角色卡蒸馏为 Claude Code skill，实现沉浸式角色扮演对话。

## 功能

- 支持 V1/V2/V3 角色卡规范（PNG/WEBP/JPEG/JSON）
- 自动提取角色定义、世界书、正则、预设
- 内置插图提取 + catbox.moe 外链插图批量下载
- AI 生成插图（通过 gemini-image-gen）
- 好感度/状态系统、聊天历史、剧情建议
- 破限预设自动转化为沉浸式角色扮演规则

## 使用方法

1. 将此目录放入 `~/.claude/skills/tavern-card-distiller/`
2. 在 Claude Code 中使用触发词：`角色卡`、`蒸馏角色`、`tavern card` 等
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

## License

MIT
