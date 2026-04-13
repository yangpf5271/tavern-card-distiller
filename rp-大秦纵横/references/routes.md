# 开场白与剧情线

## 默认开场白

紫禁城，养心殿。

夜已深沉，殿内烛火摇曳，将龙椅上那个年轻的身影拉得极长。你坐在这张象征着至高权力的座位上，却从未感到如此孤独。

父皇暴崩已过七日，明日便是你第一次临朝听政。

老太监福安悄无声息地进来，在你身后躬身："陛下，明日卯时早朝，文武百官齐聚太和殿。奴才已经打听清楚了..."他压低声音，"陈太傅会领着户部的人先发难，说国库空虚，请陛下节用。王相国则会提议充实吏部，好安插更多他们的人。"

你望着案上堆积如山的奏折，每一份都暗藏玄机。九大世家的触角已经深入朝堂每一个角落，而你这个新帝，不过是他们眼中的傀儡。

"陛下，"福安犹豫片刻，从怀中取出一份密折，"这是先帝留给您的，说要在您登基后第一次朝会前看。"

密折上只有八个字：**忍辱负重，徐图大计。**

你的手微微颤抖。明日朝堂之上，你将第一次真正面对那些表面恭顺、实则各怀鬼胎的臣子。是顺从？是抗争？还是...

<UpdateVariable>
_.set('大秦状态栏.时辰', '亥时');
_.set('大秦状态栏.活动', '深夜独坐，思虑国事');
_.set('大秦状态栏.姓名', '{{user}}');
_.set('大秦状态栏.衣物', '明黄龙袍');
_.set('大秦状态栏.官职', '天子');
_.set('大秦状态栏.背包', ['传国玉玺', '先帝密折', '虎符左半']);
_.set('大秦状态栏.当前场景NPC姓名', '福安');
_.set('大秦状态栏.NPC衣物', '紫袍');
_.set('大秦状态栏.NPC官职', '司礼监掌印太监');
</UpdateVariable>

【大秦皇朝】
时辰：亥时
活动：深夜独坐，思虑国事
姓名：{{user}}
衣物：明黄龙袍
官职：天子
背包：传国玉玺、先帝密折、虎符左半
当前场景NPC姓名：福安
NPC衣物：紫袍
NPC官职：司礼监掌印太监

## 备选开场白 2

监察院，西偏殿。

你站在破败的院门前，手中紧握着那张薄薄的任命状——**监察院属吏，从九品**。

曾经威风八面的监察院，如今破败得如同废弃的庙宇。朱红的大门掉了漆，门前的石狮也缺了半边脸。守门的老吏打量你一眼，苦笑道："又来了个不怕死的。"

穿过冷清的前院，你被引到了西偏殿。殿内，一个须发半白的中年人正伏案疾书，正是右都御史陆明远。

他抬起头，疲惫的眼中闪过一丝诧异："新来的？"看了看你的任命状，叹了口气，"年轻人，你可知道，过去三年，监察院死了十七个御史？"

空气凝固了片刻。

"不过，"陆明远话锋一转，"既然你敢来，想必也有所准备。我问你，你为何要入监察院？"

这个问题很危险。在这个世家把持朝政的时代，任何理想主义的回答都可能被视为威胁。但你也知道，一味明哲保身在这里同样没有活路。

陆明远似乎看穿了你的犹豫："罢了，不必回答。记住三条规矩：第一，没有实证不要轻易弹劾三品以上；第二，涉及九大世家的案子，先来问我；第三..."

他顿了顿，目光变得深邃："活着，比什么都重要。只有活着，才有机会看到天变。"

他递给你一叠卷宗："这是些陈年旧案，你先熟悉熟悉。记住，在监察院，最危险的不是外面的豺狼，而是..."

他意味深长地看了看周围，没有说完。

<UpdateVariable>
_.set('大秦状态栏.时辰', '巳时');
_.set('大秦状态栏.活动', '公务繁忙，初入衙门');
_.set('大秦状态栏.姓名', '{{user}}');
_.set('大秦状态栏.衣物', '皂袍铜带');
_.set('大秦状态栏.官职', '从九品监察院属吏');
_.set('大秦状态栏.背包', ['任命状', '监察院印信', '碎银五两', '陈年卷宗']);
_.set('大秦状态栏.当前场景NPC姓名', '陆明远');
_.set('大秦状态栏.NPC衣物', '绯袍金带');
_.set('大秦状态栏.NPC官职', '正二品右都御史');
</UpdateVariable>

【大秦皇朝】
时辰：卯时
活动：早朝时分，百官入宫觐见
姓名：{{user}}
衣物：青袍铜带
官职：从七品监察御史
背包：官印、文书、银两十两
当前场景NPC姓名：陆明远
NPC衣物：绯袍金带
NPC官职：正二品右都御史

## 特别剧情线（来自 disabled 世界书条目）

以下条目在原角色卡中默认关闭，可作为可选剧情线使用。

### [InitVar] 大秦状态栏变量

{
  "大秦状态栏": {
    "时辰": "卯时",
    "活动": "早朝时分，百官入宫觐见",
    "姓名": "{{user}}",
    "衣物": "青袍铜带",
    "官职": "从七品监察御史",
    "背包": ["官印", "文书", "银两十两"],
    "当前场景NPC姓名": "陆明远",
    "NPC衣物": "绯袍金带",
    "NPC官职": "正二品右都御史"
  }
}

### 别动！！别开！！[UI美化] 大秦HTML状态栏

<%_
const 时辰 = getvar('大秦状态栏.时辰', '未知');
const 活动 = getvar('大秦状态栏.活动', '无特定活动');
const 姓名 = getvar('大秦状态栏.姓名', '{{user}}');
const 衣物 = getvar('大秦状态栏.衣物', '布衣');
const 官职 = getvar('大秦状态栏.官职', '白身');
const 背包 = getvar('大秦状态栏.背包', []);
const NPC姓名 = getvar('大秦状态栏.当前场景NPC姓名', '无');
const NPC衣物 = getvar('大秦状态栏.NPC衣物', '-');
const NPC官职 = getvar('大秦状态栏.NPC官职', '-');
_%>

<div style="background:linear-gradient(180deg,#2C2416 0%,#4A3C28 20%,#8B7355 50%,#4A3C28 80%,#2C2416 100%);border:2px solid #CD9B1D;border-radius:8px;padding:12px;margin:10px 0;box-shadow:0 4px 8px rgba(0,0,0,0.4),inset 0 2px 4px rgba(205,155,29,0.3);font-family:'KaiTi','STKaiti','楷体',serif;color:#F4E4C1;position:relative">
  <div style="position:absolute;top:-1px;left:50%;transform:translateX(-50%);width:60%;height:2px;background:linear-gradient(90deg,transparent,#FFD700,transparent)"></div>

  <div style="text-align:center;font-size:20px;font-weight:bold;color:#FFD700;text-shadow:2px 2px 4px rgba(0,0,0,0.6);letter-spacing:8px;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid #8B6914">【大秦皇朝】</div>

  <table style="width:100%;border-collapse:collapse">
    <tr>
      <td style="width:35%;padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">时辰：</td>
      <td style="padding:5px 8px;color:#F4E4C1"><%= 时辰 %></td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">活动：</td>
      <td style="padding:5px 8px;color:#F4E4C1;font-style:italic"><%= 活动 %></td>
    </tr>
    <tr>
      <td colspan="2" style="padding:8px 0">
        <div style="width:80%;height:1px;background:linear-gradient(90deg,transparent,#8B6914,transparent);margin:0 auto"></div>
      </td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">姓名：</td>
      <td style="padding:5px 8px;color:#FFD700;font-weight:bold"><%= 姓名 %></td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">衣物：</td>
      <td style="padding:5px 8px;color:#F4E4C1"><%= 衣物 %></td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">官职：</td>
      <td style="padding:5px 8px;color:#FFD700"><%= 官职 %></td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">背包：</td>
      <td style="padding:5px 8px;color:#F4E4C1">
        <% if (背包.length > 0) { %>
          <%= 背包.join('、') %>
        <% } else { %>
          空
        <% } %>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="padding:8px 0">
        <div style="width:80%;height:1px;background:linear-gradient(90deg,transparent,#8B6914,transparent);margin:0 auto"></div>
      </td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">当前场景NPC姓名：</td>
      <td style="padding:5px 8px;color:#FFD700;font-weight:bold"><%= NPC姓名 %></td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">NPC衣物：</td>
      <td style="padding:5px 8px;color:#F4E4C1"><%= NPC衣物 %></td>
    </tr>
    <tr>
      <td style="padding:5px 8px;color:#DAA520;font-weight:bold;text-align:right;border-right:1px solid #8B691455">NPC官职：</td>
      <td style="padding:5px 8px;color:#FFD700"><%= NPC官职 %></td>
    </tr>
  </table>

  <div style="position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:60%;height:2px;background:linear-gradient(90deg,transparent,#FFD700,transparent)"></div>
</div>
