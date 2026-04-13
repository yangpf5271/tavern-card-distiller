# 状态系统定义

以下状态变量在对话过程中被追踪，记录在聊天历史的 frontmatter state 对象中。

## 体力（stamina）
- 默认值: 100
- 说明: 从角色卡中检测到的 体力 系统

## 堕落度（corruption）
- 默认值: 0
- 说明: 从角色卡中检测到的 堕落度 系统

## 状态在 session 文件中的格式

```yaml
state:
  stamina: 100
  corruption: 0
```
