# 正则格式规则

以下规则定义了对话文本的格式化方式，请在回复中遵循其意图：

### 变量-隐藏变量更新
- 匹配: `/<UpdateVariable>.*?(?:<\/UpdateVariable>|$)/gs`
- 替换为: ``

### 对AI隐藏状态栏
- 匹配: `<StatusPlaceHolderImpl/>`
- 替换为: ``

### 状态栏代码块
- 匹配: `<StatusPlaceHolderImpl\/>`
- 替换为: ````
<StatusPlaceHolderImpl/>
````

### Html美化
- 匹配: `【大秦皇朝】[\s\S]*?时辰：([^\n]+)[\s\S]*?活动：([^\n]+)[\s\S]*?姓名：([^\n]+)[\s\S]*?衣物：([^\n]+)[\s\S]*?官职：([^\n]+)[\s\S]*?背包：([^\n]+)[\s\S]*?当前场景NPC姓名：([^\n]+)[\s\S]*?NPC衣物：([^\n]+)[\s\S]*?NPC官职：([^\n]+)`
- 替换为: `<div style="background:linear-gradient(180deg,#2C2416 0%,#4A3C28 20%,#8B7355 50%,#4A3C28 80%,#2C2416 100%);border:2px solid #CD9B1D;border-radius:8px;padding:12px;margin:10px 0;box-shadow:0 4px 8px rgba(0,0,0,0.4),inset 0 2px 4px rgba(205,155,29,0.3);font-family:'KaiTi','STKaiti','楷体',serif;color:#F4E4C1;position:relative">
  <div style="position:absolute;top:-1px;left:50%;transform:translateX(-50%);width:60%;height:2px;background:linear-gradient(90deg,transparent,#FFD700,transparent)"></div>
  <div style="text-align:center;font-size:20px;font-weight:bold;color:#FFD700;text-shadow:2px 2px 4px rgba(0,0,0,0.6);letter-spacing:8px;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid #8B6914">【大秦皇朝】</div>
  <table style="width:100%;border-collapse:collapse">
    <tr><td style="width:35%;padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">时辰：</td><td style="padding:5px 8px;color:#F4E4C1">$1</td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">活动：</td><td style="padding:5px 8px;color:#F4E4C1;font-style:italic">$2</td></tr>
    <tr><td colspan="2" style="padding:8px 0"><div style="width:80%;height:1px;background:linear-gradient(90deg,transparent,#8B6914,transparent);margin:0 auto"></div></td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">姓名：</td><td style="padding:5px 8px;color:#FFD700;font-weight:bold">$3</td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">衣物：</td><td style="padding:5px 8px;color:#F4E4C1">$4</td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">官职：</td><td style="padding:5px 8px;color:#FFD700">$5</td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">背包：</td><td style="padding:5px 8px;color:#F4E4C1">$6</td></tr>
    <tr><td colspan="2" style="padding:8px 0"><div style="width:80%;height:1px;background:linear-gradient(90deg,transparent,#8B6914,transparent);margin:0 auto"></div></td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">当前场景NPC姓名：</td><td style="padding:5px 8px;color:#FFD700;font-weight:bold">$7</td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">NPC衣物：</td><td style="padding:5px 8px;color:#F4E4C1">$8</td></tr>
    <tr><td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">NPC官职：</td><td style="padding:5px 8px;color:#FFD700">$9</td></tr>
  </table>
  <div style="position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:60%;height:2px;background:linear-gradient(90deg,transparent,#FFD700,transparent)"></div>
</div>`

请将以上正则规则的意图融入你的回复格式中，而非机械执行正则替换。