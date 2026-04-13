# 状态系统定义

以下状态变量在对话过程中被追踪，记录在聊天历史的 frontmatter state 对象中。

## 好感度（affection）
- 默认值: 0
- 说明: 从角色卡中检测到的 好感度 系统

## 欲望值（desire）
- 默认值: 0
- 说明: 从角色卡中检测到的 欲望值 系统

## 堕落度（corruption）
- 默认值: 0
- 说明: 从角色卡中检测到的 堕落度 系统

## 嫉妒值（jealousy）
- 默认值: 0
- 说明: 从角色卡中检测到的 嫉妒值 系统

## 状态在 session 文件中的格式

```yaml
state:
  affection: 0
  desire: 0
  corruption: 0
  jealousy: 0
```
