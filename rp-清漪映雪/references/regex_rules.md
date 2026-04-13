# 正则格式规则

以下规则定义了对话文本的格式化方式，请在回复中遵循其意图：

### 对ai隐藏状态栏
- 匹配: `<StatusPlaceHolderImpl/>`
- 替换为: ``

### 去除变量更新
- 匹配: `/<UpdateVariable>[\s\S]*?</UpdateVariable>/gm`
- 替换为: ``

### 状态栏 (disabled)
- 匹配: `<StatusPlaceHolderImpl/>`
- 替换为: ````
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>潮汐悲歌 - 状态面板</title>
    <style>
        :root {
            --bg-card: rgba(15, 20, 25, 0.85);
            --border-color: rgba(0, 150, 150, 0.4);
            --shadow-color: rgba(0, 200, 200, 0.2);
            --accent-cyan: #00b894;
            --accent-orange: #fdcb6e;
            --text-primary: #dfe6e9;
            --text-secondary: #b2bec3;
            --text-highlight: #81ecec;
            --radius-md: 6px;
        }
        .tw-container * { box-sizing: border-box; }
        .tw-container {
            font-family: 'Courier New', monospace;
            background-color: transparent;
            color: var(--text-primary);
            padding: 8px;
            max-width: 600px;
            margin: 15px auto;
            line-height: 1.6;
        }
        .tw-card {
            background: var(--bg-card);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            box-shadow: 0 0 15px var(--shadow-color);
            margin-bottom: 12px;
            overflow: hidden;
            backdrop-filter: blur(5px);
        }
        .tw-section-header {
            padding: 10px 15px;
            background: linear-gradient(90deg, rgba(0, 100, 100, 0.3) 0%, rgba(15, 20, 25, 0.1) 100%);
            border-bottom: 1px solid var(--border-color);
            cursor: pointer;
            user-select: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background-color 0.3s ease;
        }
        .tw-section-header:hover { background-color: rgba(0, 150, 150, 0.2); }
        .tw-section-title { font-weight: bold; font-size: 1.1em; color: var(--accent-cyan); text-shadow: 0 0 8px var(--accent-cyan); }
        .tw-chevron { width: 18px; height: 18px; transition: transform 0.4s ease; stroke: var(--text-secondary); }
        .tw-chevron.expanded { transform: rotate(180deg); }
        .tw-section-content {
            max-height: 0;
            overflow: hidden;
            opacity: 0;
            transition: max-height 0.6s ease-out, opacity 0.6s ease-out, padding 0.6s ease-out;
            padding: 0 15px;
        }
        .tw-section-content.expanded { max-height: 2000px; opacity: 1; padding: 15px; }
        .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; }
        .info-item { background: rgba(0,0,0,0.2); padding: 8px; border-radius: 4px; border-left: 3px solid var(--border-color); }
        .info-label { font-size: 0.8em; color: var(--text-secondary); }
        .info-value { font-size: 1em; font-weight: bold; color: var(--text-highlight); }
        .progress-bar { background: var(--border-color); border-radius: 4px; padding: 2px; margin-top: 4px; }
        .progress-fill { background: linear-gradient(90deg, #00b894, #55efc4); height: 14px; border-radius: 2px; transition: width 0.5s ease; text-align: center; color: #2d3436; font-size: 0.8em; line-height: 14px; font-weight: bold; }
        .item-list { list-style: none; padding-left: 0; margin-top: 8px; }
        .item-list li {
            background-color: rgba(0,0,0,0.3);
            border-left: 2px solid var(--accent-cyan);
            padding: 6px 10px; margin-bottom: 5px; border-radius: 2px;
            font-size: 0.9em; cursor: pointer; transition: all 0.2s ease;
        }
        .item-list li:hover { background-color: rgba(0, 150, 150, 0.2); border-color: var(--accent-cyan); transform: translateX(3px); }
        .item-list li.empty { background: none; border: none; color: var(--text-secondary); font-style: italic; cursor: default; }
        .item-list li .item-quantity { float: right; color: var(--text-secondary); }
        .detail-box {
            background: rgba(0,0,0,0.4);
            border: 1px dashed var(--border-color);
            border-radius: 4px;
            padding: 10px;
            margin-top: 10px;
            min-height: 50px;
        }
        .detail-box .detail-title { font-weight: bold; color: var(--accent-orange); }
        .detail-box .detail-content { font-size: 0.9em; color: var(--text-primary); margin-top: 5px; white-space: pre-line; }
        .detail-box .placeholder { color: var(--text-secondary); font-style: italic; }
    </style>
</head>
<body>

<div class="tw-container" id="tw-container-root">
    
    <!-- 船只号状态 -->
    <div class="tw-card">
        <div class="tw-section-header" onclick="toggleTwSection(this)">
            <span class="tw-section-title">🚢 船只状态</span>
            <svg class="tw-chevron" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
        </div>
        <div class="tw-section-content">
            <div class="info-grid">
                <div class="info-item">
                    <span class="info-label">船名</span>
                    <span class="info-value" id="ship-name">寻路者号</span>
                </div>
                <div class="info-item">
                    <span class="info-label">船体等级</span>
                    <span class="info-value" id="ship-tier">1</span>
                </div>
                <div class="info-item">
                    <span class="info-label">当前海域</span>
                    <span class="info-value" id="current-location">潮汐之结周边</span>
                </div>
                 <div class="info-item">
                    <span class="info-label">天气</span>
                    <span class="info-value" id="current-weather">有雾</span>
                </div>
            </div>
            <div class="info-item" style="margin-top: 10px;">
                <span class="info-label">船体结构完整度</span>
                <div class="progress-bar">
                    <div class="progress-fill" id="hull-status-bar" style="width: 100%;">100%</div>
                </div>
            </div>
             <div class="info-item" style="margin-top: 10px;">
                <span class="info-label">船之心</span>
                <span class="info-value" id="ship-core">混合之心 (能量微弱)</span>
            </div>
        </div>
    </div>

    <!-- 已安装模块 -->
    <div class="tw-card">
        <div class="tw-section-header" onclick="toggleTwSection(this)">
            <span class="tw-section-title">⚙️ 已安装模块</span>
            <svg class="tw-chevron" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
        </div>
        <div class="tw-section-content">
            <ul class="item-list" id="module-list"></ul>
            <div class="detail-box" id="module-detail-box">
                <p class="placeholder">点击模块查看详情</p>
            </div>
        </div>
    </div>

    <!-- 船员 -->
    <div class="tw-card">
        <div class="tw-section-header" onclick="toggleTwSection(this)">
            <span class="tw-section-title">👥 船员</span>
            <svg class="tw-chevron" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
        </div>
        <div class="tw-section-content">
            <ul class="item-list" id="crew-list"></ul>
            <div class="detail-box" id="crew-detail-box">
                 <p class="placeholder">点击船员查看详情</p>
            </div>
        </div>
    </div>

    <!-- 背包 -->
    <div class="tw-card">
        <div class="tw-section-header" onclick="toggleTwSection(this)">
            <span class="tw-section-title">🎒 背包</span>
            <svg class="tw-chevron" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
        </div>
        <div class="tw-section-content">
            <div class="info-item">
                <span class="info-label">基础材料</span>
                <ul class="item-list" id="inventory-base"></ul>
            </div>
            <div class="info-item">
                <span class="info-label">特殊材料</span>
                <ul class="item-list" id="inventory-special"></ul>
            </div>
            <div class="info-item">
                <span class="info-label">消耗品</span>
                <ul class="item-list" id="inventory-consumables"></ul>
            </div>
            <div class="detail-box" id="inventory-detail-box">
                <p class="placeholder">点击物品查看详情</p>
            </div>
        </div>
    </div>

</div>

<script>
    (function() {
        // --- 全局函数和变量 ---
        const containerId = `tw-container-root`;

        // 安全地获取MVU变量值
        function safeGet(obj, path, defaultValue = '') {
            const value = _.get(obj, path, defaultValue);
            return Array.isArray(value) && value.length > 0 ? value[0] : value;
        }

        // 切换可折叠区域的显示/隐藏
        window.toggleTwSection = function(headerElement) {
            const content = headerElement.nextElementSibling;
            const chevron = headerElement.querySelector('.tw-chevron');
            const isExpanded = content.classList.toggle('expanded');
            chevron.classList.toggle('expanded', isExpanded);
        };

        // --- 数据更新与渲染逻辑 ---
        function updateTidalWoeStatus() {
            try {
                const currentMessageId = getCurrentMessageId();
                if (currentMessageId === undefined) return;
                
                const messageData = getChatMessages(currentMessageId);
                if (!messageData || messageData.length === 0) return;

                const gameData = messageData[0].data;
                const charData = gameData.stat_data || gameData.display_data;
                if (!charData) return;

                const container = document.getElementById(containerId);
                if (!container) return;

                // --- 更新船只核心信息 ---
                const shipData = safeGet(charData, '寻路者号', {});
                container.querySelector('#ship-name').textContent = safeGet(shipData, '船名', '寻路者号');
                const hullStatus = safeGet(shipData, '船体状态', 100);
                container.querySelector('#hull-status-bar').style.width = `${hullStatus}%`;
                container.querySelector('#hull-status-bar').textContent = `${hullStatus}%`;
                container.querySelector('#ship-tier').textContent = safeGet(shipData, '船体等级', 1);
                const coreType = safeGet(shipData, '船之心.类型', '?');
                const coreStatus = safeGet(shipData, '船之心.状态', '?');
                container.querySelector('#ship-core').textContent = `${coreType} (${coreStatus})`;

                // --- 更新顶部信息 ---
                container.querySelector('#current-location').textContent = safeGet(charData, '当前海域', '?');
                container.querySelector('#current-weather').textContent = safeGet(charData, '天气', '?');
                
                // --- 更新模块列表与详情 ---
                const moduleList = container.querySelector('#module-list');
                const moduleDetailBox = container.querySelector('#module-detail-box');
                const slots = safeGet(shipData, '模块插槽', {});
                let moduleHtml = '';
                for (const slotType in slots) {
                    const installed = safeGet(slots, `${slotType}[0]`, []);
                    if (Array.isArray(installed) && installed.length > 0) {
                        installed.forEach(moduleName => {
                            moduleHtml += `<li data-type="module" data-detail="${slotType}: ${moduleName}">${moduleName}</li>`;
                        });
                    }
                }
                moduleList.innerHTML = moduleHtml || '<li class="empty">无已安装模块</li>';
                addClickListener(moduleList, moduleDetailBox);

                // --- 更新船员列表与详情 ---
                const crewList = container.querySelector('#crew-list');
                const crewDetailBox = container.querySelector('#crew-detail-box');
                const crewData = safeGet(charData, '船员', {});
                let crewHtml = `<li data-type="crew" data-detail="船长 - ${safeGet(charData, '<user>.状态', '正常')}">${safeGet(charData, '<user>.姓名', '{{user}}')}</li>`;
                for (const name in crewData) {
                    crewHtml += `<li data-type="crew" data-detail="${safeGet(crewData, `${name}[0]`)}">${name}</li>`;
                }
                crewList.innerHTML = crewHtml;
                addClickListener(crewList, crewDetailBox);

                // --- 更新背包列表与详情 ---
                const inventoryDetailBox = container.querySelector('#inventory-detail-box');
                const renderInventory = (selector, path, type) => {
                    const listEl = container.querySelector(selector);
                    const items = safeGet(charData, path, []);
                    let html = '';
                    if (Array.isArray(items) && items.length > 0) {
                        items.forEach(item => {
                            if (typeof item === 'object' && item.name) {
                                html += `<li data-type="${type}" data-detail="${item.name}: ${item.description || '无描述'}">${item.name} <span class="item-quantity">x${item.quantity}</span></li>`;
                            } else if (typeof item === 'string') {
                                html += `<li data-type="${type}" data-detail="${item}">${item}</li>`;
                            }
                        });
                    } else {
                        html = '<li class="empty">无</li>';
                    }
                    listEl.innerHTML = html;
                    addClickListener(listEl, inventoryDetailBox);
};
                renderInventory('#inventory-base', '背包.基础材料[0]', '材料');
                renderInventory('#inventory-special', '背包.特殊材料[0]', '材料');
                renderInventory('#inventory-consumables', '背包.消耗品[0]', '消耗品');

            } catch (error) {
                console.error("Tidal Woe Status Bar Error:", error);
            }
        }
        
        // --- 统一的点击事件处理逻辑 ---
        function addClickListener(listElement, detailBox) {
            if (!listElement || !detailBox) return;
            listElement.addEventListener('click', function(event) {
                if (event.target && event.target.tagName === 'LI' && !event.target.classList.contains('empty')) {
                    const detailText = event.target.getAttribute('data-detail');
                    const detailType = event.target.getAttribute('data-type');
                    
                    // 清除同级列表的所有选中状态
                    const allItems = listElement.querySelectorAll('li');
                    allItems.forEach(item => item.style.backgroundColor = 'rgba(0,0,0,0.3)');

                    // 高亮当前选中的项目
                    event.target.style.backgroundColor = 'rgba(0, 150, 150, 0.2)';
                    
                    // 更新详情框
                    detailBox.innerHTML = `
                        <p class="detail-title">${detailType.charAt(0).toUpperCase() + detailType.slice(1)} 详情:</p>
                        <p class="detail-content">${detailText}</p>
                    `;
                }
            });
        }
        
        // --- 初始化与事件监听 ---
        if (typeof _ === 'undefined') {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js';
            document.head.appendChild(script);
            script.onload = () => { eventOn(tavern_events.MESSAGE_UPDATED, updateTidalWoeStatus); };
        } else {
            eventOn(tavern_events.MESSAGE_UPDATED, updateTidalWoeStatus);
        }

        // 初始加载时也尝试更新一次
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(updateTidalWoeStatus, 500);
        });

    })();
</script>

</body>
</html>
````

请将以上正则规则的意图融入你的回复格式中，而非机械执行正则替换。