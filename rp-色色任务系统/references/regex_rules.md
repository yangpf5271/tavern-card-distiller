# 正则格式规则

以下规则定义了对话文本的格式化方式，请在回复中遵循其意图：

### 萧谴写卡助手v3.5Beta状态栏美化 (disabled)
- 匹配: `<StatusBar>([\s\S]*?)</StatusBar>`
- 替换为: ````
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>故事情节状态</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- 引入YAML解析库 -->
    <script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#9d7cf5',
                        secondary: '#2d2447',
                        dark: '#1a142c',
                        light: '#12101b',
                        lightBg: '#f8fafc',
                        lightCard: '#ffffff',
                        lightText: '#1e293b',
                        lightBorder: '#e2e8f0',
                        jade: {
                            50: '#f0fdfa',
                            100: '#ccfbf1',
                            200: '#99f6e4',
                            300: '#5eead4',
                            400: '#2dd4bf',
                            500: '#14b8a6',
                            600: '#0d9488',
                            700: '#0f766e',
                            800: '#115e59',
                            900: '#134e4a',
                        },
                        classic: {
                            50: '#fefbf5',
                            100: '#fdf6e9',
                            200: '#faeed7',
                            300: '#f5dfb7',
                            400: '#e9c887',
                            500: '#d9a856',
                            600: '#c28c40',
                            700: '#a06c30',
                            800: '#7d5428',
                            900: '#644423',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        serif: ['Georgia', 'Cambria', 'serif'],
                    },
                }
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .card-hover {
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .card-hover:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px -5px rgba(157, 124, 245, 0.2), 0 8px 10px -6px rgba(157, 124, 245, 0.2);
            }
            .theme-transition {
                transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
            }
            .character-card h3 {
                color: white !important;
            }
            .character-card li {
                color: white !important;
            }
            .character-card .text-gray-400 {
                color: rgba(255, 255, 255, 0.8) !important;
            }
            
            .day-mode .status-block {
                background-color: theme('colors.lightCard');
                border-color: theme('colors.lightBorder');
            }
            .day-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(157, 124, 245, 0.1), rgba(157, 124, 245, 0.05));
            }
            .day-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, theme('colors.lightCard'), rgba(157, 124, 245, 0.05));
            }
            .day-mode .text-gray-300,
            .day-mode .text-gray-400,
            .day-mode .text-gray-500 {
                color: #64748b !important;
            }
            .day-mode .border-gray-700\/30,
            .day-mode .border-gray-700\/20 {
                border-color: theme('colors.lightBorder') !important;
            }
            .day-mode .character-card {
                background-color: theme('colors.lightCard');
                border-color: theme('colors.lightBorder');
            }
            .day-mode .character-card h3,
            .day-mode .character-card li,
            .day-mode .character-card .text-gray-400 {
                color: theme('colors.lightText') !important;
            }
            .day-mode .border-l-2 {
                border-color: rgba(157, 124, 245, 0.5) !important;
            }
            .day-mode h3.text-primary {
                color: #7c3aed !important;
            }
            .day-mode .card-hover:hover {
                box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.1), 0 8px 10px -6px rgba(124, 58, 237, 0.1);
            }
            .day-mode .theme-btn.active {
                background-color: #7c3aed;
            }
            
            .jade-mode .status-block {
                background-color: white;
                border-color: theme('colors.jade.200');
            }
            .jade-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(20, 184, 166, 0.1), rgba(20, 184, 166, 0.05));
            }
            .jade-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, white, rgba(20, 184, 166, 0.05));
            }
            .jade-mode .text-gray-300,
            .jade-mode .text-gray-400,
            .jade-mode .text-gray-500 {
                color: theme('colors.jade.700') !important;
            }
            .jade-mode .border-gray-700\/30,
            .jade-mode .border-gray-700\/20 {
                border-color: theme('colors.jade.200') !important;
            }
            .jade-mode .character-card {
                background-color: white;
                border-color: theme('colors.jade.200');
            }
            .jade-mode .character-card h3,
            .jade-mode .character-card li,
            .jade-mode .character-card .text-gray-400 {
                color: theme('colors.jade.900') !important;
            }
            .jade-mode .border-l-2 {
                border-color: rgba(20, 184, 166, 0.5) !important;
            }
            .jade-mode h3.text-primary,
            .jade-mode .text-primary,
            .jade-mode .fa {
                color: theme('colors.jade.600') !important;
            }
            .jade-mode .card-hover:hover {
                box-shadow: 0 10px 25px -5px rgba(20, 184, 166, 0.1), 0 8px 10px -6px rgba(20, 184, 166, 0.1);
            }
            .jade-mode .theme-btn.active {
                background-color: theme('colors.jade.500');
                color: white;
                border-color: theme('colors.jade.600');
            }
            .jade-mode .theme-btn:not(.active):hover {
                background-color: theme('colors.jade.100');
            }
            
            .classic-mode .status-block {
                background-color: theme('colors.classic.50');
                border-color: theme('colors.classic.300');
                box-shadow: 0 2px 8px rgba(100, 68, 35, 0.1);
            }
            .classic-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(217, 168, 86, 0.1), rgba(217, 168, 86, 0.05));
            }
            .classic-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, theme('colors.classic.50'), rgba(217, 168, 86, 0.05));
            }
            .classic-mode .text-gray-300,
            .classic-mode .text-gray-400,
            .classic-mode .text-gray-500 {
                color: theme('colors.classic.700') !important;
            }
            .classic-mode .border-gray-700\/30,
            .classic-mode .border-gray-700\/20 {
                border-color: theme('colors.classic.300') !important;
            }
            .classic-mode .character-card {
                background-color: theme('colors.classic.50');
                border-color: theme('colors.classic.300');
            }
            .classic-mode .character-card h3,
            .classic-mode .character-card li,
            .classic-mode .character-card .text-gray-400 {
                color: theme('colors.classic.900') !important;
            }
            .classic-mode .border-l-2 {
                border-color: rgba(217, 168, 86, 0.5) !important;
            }
            .classic-mode h3.text-primary,
            .classic-mode .text-primary,
            .classic-mode .fa {
                color: theme('colors.classic.700') !important;
            }
            .classic-mode .card-hover:hover {
                box-shadow: 0 10px 25px -5px rgba(217, 168, 86, 0.1), 0 8px 10px -6px rgba(217, 168, 86, 0.1);
            }
            .classic-mode .theme-btn.active {
                background-color: theme('colors.classic.600');
                color: white;
                border-color: theme('colors.classic.700');
            }
            .classic-mode .theme-btn:not(.active):hover {
                background-color: theme('colors.classic.200');
            }
            
            .theme-btn {
                transition: all 0.2s ease;
                width: 28px;
                height: 28px;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 0;
                color: #b1a5c9;
            }
            .theme-btn.active {
                color: white;
                border-color: currentColor;
            }
            .theme-btn:not(.active):hover {
                background-color: rgba(157, 124, 245, 0.1);
                color: #e0d6f2;
            }
            
            /* 为可点击的行动选项添加样式 */
            #options-list li {
                cursor: pointer;
                transition: all 0.2s ease;
            }
            #options-list li:hover {
                background-color: rgba(157, 124, 245, 0.1);
                transform: translateX(2px);
            }
        }
    </style>
</head>
<body>
    <!-- YAML格式数据源 -->
    <script id="yaml-data-source" type="text/yaml">
$1
</script>
  
    <div class="container mx-auto px-3 py-4 max-w-3xl">
        <!-- 整合后的状态栏区块 -->
        <div class="status-block mb-4 bg-dark rounded-2xl shadow-lg overflow-hidden border border-gray-700/30 theme-transition">
            <!-- 顶部信息和主题切换栏 -->
            <div class="bg-gradient-to-r from-primary/20 to-primary/5 p-4 rounded-t-2xl border-b border-gray-700/20 theme-transition">
                <div class="flex flex-col md:flex-row justify-between items-center gap-3">
                    <!-- 左侧状态栏标题 -->
                    <div class="flex items-center text-gray-300">
                        <i class="fa fa-bookmark text-primary mr-2"></i>
                        <span class="font-medium" id="status-bar-title">加载中...</span>
                    </div>
                    
                    <!-- 中间日期和地点信息 - 在移动设备上会换行显示 -->
                    <div class="flex flex-wrap items-center justify-center gap-x-4 text-sm text-gray-300">
                        <div class="flex items-center">
                            <span class="emoji mr-1.5"></span>
                            <span id="location-display" class="whitespace-nowrap">加载中...</span>
                        </div>
                        <div class="flex items-center">
                            <span class="emoji mr-1.5"></span>
                            <span id="time-display" class="whitespace-nowrap">加载中...</span>
                        </div>
                    </div>
                    
                    <!-- 右侧主题切换按钮组 - 只保留图标 -->
                    <div class="flex space-x-1">
                        <button data-theme="night" class="theme-btn active rounded-full border border-gray-700/50" title="黑夜模式">
                            <i class="fa fa-moon-o"></i>
                        </button>
                        <button data-theme="day" class="theme-btn rounded-full border border-gray-700/50" title="白天模式">
                            <i class="fa fa-sun-o"></i>
                        </button>
                        <button data-theme="jade" class="theme-btn rounded-full border border-gray-700/50" title="青玉模式">
                            <i class="fa fa-leaf"></i>
                        </button>
                        <button data-theme="classic" class="theme-btn rounded-full border border-gray-700/50" title="古典模式">
                            <i class="fa fa-book"></i>
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- 角色状态详情 -->
            <div class="border-t border-gray-700/20 theme-transition">
                <details class="w-full group">
                    <summary class="w-full px-4 py-3 font-semibold cursor-pointer flex justify-between items-center list-none hover:bg-primary/10 transition-colors theme-transition">
                        <span class="text-gray-300 flex items-center">
                            <i class="fa fa-users text-primary mr-2"></i>角色状态详情
                        </span>
                        <i class="fa fa-chevron-down text-primary transition-transform duration-300 group-open:rotate-180"></i>
                    </summary>
                    
                    <div id="characters-container" class="p-3 space-y-3 overflow-hidden transition-all duration-300">
                        <!-- 角色状态将在这里动态生成 -->
                        <div class="flex justify-center py-8">
                            <div class="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-primary"></div>
                        </div>
                    </div>
                </details>
            </div>
            
            <!-- 行动选项区域 -->
            <div class="border-t border-gray-700/20 bg-gradient-to-b from-dark to-primary/10 rounded-b-2xl theme-transition">
                <h3 class="px-4 pt-3 font-bold text-primary flex items-center">
                    <i class="fa fa-list-alt mr-2"></i>
                    <span id="action-owner">加载中...</span>的行动选项
                </h3>
                <div id="options-container" class="px-4 pb-4">
                    <!-- 将列表样式从list-decimal改为无序列表样式 -->
                    <ul id="options-list" class="list-none space-y-2 text-sm pl-1 py-2">
                        <!-- 行动选项将在这里动态生成 -->
                        <li class="text-gray-400">
                            <div class="flex items-center">
                                <div class="animate-spin rounded-full h-4 w-4 border-t-2 border-b-2 border-primary mr-2"></div>
                                加载选项中...
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 封装与SillyTavern通信的函数
        const triggerQuickReply = (text) => {
            // 检查文本有效性，避免发送空内容
            if (!text || ['…', '...'].includes(text.trim()) || text.trim().length === 0) return;
            // 检查SillyTavern环境并发送命令
            if (typeof triggerSlash === 'function') {
                triggerSlash(`/send ${text}|/trigger`);
            } else {
                console.log('SillyTavern environment not detected. Would send:', text);
            }
        };

        // 页面加载完成后执行
        document.addEventListener('DOMContentLoaded', () => {
            // 初始化主题切换功能
            initThemeToggle();
            
            // 初始化YAML数据源的渲染器
            const storyRenderer = new StoryRenderer('yaml-data-source');
            storyRenderer.init();
            
            // 使用事件委托为行动选项添加点击事件监听器
            document.getElementById('options-container').addEventListener('click', (e) => {
                // 检查点击的是否是选项列表项
                if (e.target.tagName === 'LI' && e.target.closest('#options-list')) {
                    // 获取选项文本并清除首尾空格
                    const optionText = e.target.textContent.trim();
                    // 触发快速回复
                    triggerQuickReply(optionText);
                    
                    // 视觉反馈：短暂高亮选中的选项
                    const originalBg = e.target.style.backgroundColor;
                    e.target.style.backgroundColor = 'rgba(157, 124, 245, 0.2)';
                    setTimeout(() => {
                        e.target.style.backgroundColor = originalBg;
                    }, 300);
                }
            });
        });

        // 初始化主题切换功能
        function initThemeToggle() {
            const themeButtons = document.querySelectorAll('.theme-btn');
            const bodyElement = document.body;
            
            // 检查本地存储中的主题偏好
            const savedTheme = localStorage.getItem('storyTheme') || 'night';
            switchToTheme(savedTheme);
            
            // 绑定点击事件
            themeButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const theme = button.getAttribute('data-theme');
                    switchToTheme(theme);
                    localStorage.setItem('storyTheme', theme);
                });
            });
            
            // 切换到指定主题
            function switchToTheme(theme) {
                // 移除所有主题类
                bodyElement.classList.remove('day-mode', 'jade-mode', 'classic-mode');
                
                // 添加选中主题类
                if (theme === 'day') {
                    bodyElement.classList.add('day-mode');
                } else if (theme === 'jade') {
                    bodyElement.classList.add('jade-mode');
                } else if (theme === 'classic') {
                    bodyElement.classList.add('classic-mode');
                }
                
                // 更新按钮状态
                themeButtons.forEach(btn => {
                    if (btn.getAttribute('data-theme') === theme) {
                        btn.classList.add('active');
                    } else {
                        btn.classList.remove('active');
                    }
                });
            }
        }

        // 故事渲染器类 - 从数据源中提取emoji并动态渲染
        class StoryRenderer {
            constructor(dataSourceId) {
                this.dataSourceId = dataSourceId;
                this.yamlData = null;
                this.rawYamlContent = ""; // 存储原始YAML内容用于提取emoji
                this.rootNode = null;
                this.initElements();
            }

            // 初始化DOM元素引用
            initElements() {
                this.elements = {
                    statusBarTitle: document.getElementById('status-bar-title'),
                    timeDisplay: document.getElementById('time-display'),
                    locationDisplay: document.getElementById('location-display'),
                    charactersContainer: document.getElementById('characters-container'),
                    actionOwner: document.getElementById('action-owner'),
                    optionsList: document.getElementById('options-list')
                };
            }

            // 初始化方法
            init() {
                try {
                    // 从script标签中加载YAML数据
                    this.loadYamlFromScriptTag();
                    // 找到根节点
                    this.findRootNode();
                    this.renderAll();
                    this.setupEventListeners();
                } catch (error) {
                    this.handleError(error);
                }
            }

            // 从script标签加载并解析YAML数据
            loadYamlFromScriptTag() {
                const scriptElement = document.getElementById(this.dataSourceId);
                if (!scriptElement) {
                    throw new Error('未找到id为"yaml-data-source"的script标签');
                }

                // 保存原始YAML内容用于提取emoji
                this.rawYamlContent = scriptElement.textContent.trim();
                if (!this.rawYamlContent) {
                    throw new Error('script标签中的YAML内容为空');
                }

                try {
                    this.yamlData = jsyaml.load(this.rawYamlContent);
                } catch (e) {
                    throw new Error(`YAML解析错误: ${e.message}`);
                }

                if (!this.yamlData || Object.keys(this.yamlData).length === 0) {
                    throw new Error('YAML数据为空或格式不正确');
                }
            }

            // 从文本中提取emoji (匹配Unicode表情符号范围)
            extractEmojis(text) {
                // 匹配常见emoji的正则表达式
                const emojiRegex = /[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu;
                return text.match(emojiRegex) || [];
            }

            // 从指定字段中提取emoji
            getEmojiForField(fieldName) {
                // 在原始YAML内容中查找包含此字段名的行
                const lines = this.rawYamlContent.split('\n');
                for (const line of lines) {
                    // 查找包含字段名且有冒号的行
                    if (line.includes(fieldName) && line.includes(':')) {
                        // 提取冒号后面的内容
                        const valuePart = line.split(':')[1].trim();
                        // 从值部分提取emoji
                        const emojis = this.extractEmojis(valuePart);
                        if (emojis.length > 0) {
                            return emojis[0]; // 返回第一个找到的emoji
                        }
                    }
                }
                return '📌'; // 默认emoji
            }

            // 查找根节点
            findRootNode() {
                const rootNodeNames = Object.keys(this.yamlData);
                if (rootNodeNames.length === 0) {
                    throw new Error('YAML数据中未找到任何根节点');
                }
                
                this.rootNode = rootNodeNames[0];
                this.elements.statusBarTitle.textContent = this.formatNodeName(this.rootNode);
            }

            // 格式化节点名称
            formatNodeName(name) {
                if (/^[A-Za-z]+$/.test(name)) {
                    return name.charAt(0).toUpperCase() + name.slice(1);
                }
                return name;
            }

            // 渲染所有内容
            renderAll() {
                if (!this.rootNode || !this.yamlData[this.rootNode]) {
                    throw new Error('未找到有效的根节点数据');
                }
                
                const rootData = this.yamlData[this.rootNode];
                this.renderHeaderInfo(rootData);
                this.renderCharacters(rootData);
                this.renderActionOptions(rootData);
            }

            // 渲染头部信息（日期和时间和地点）
            renderHeaderInfo(rootData) {
                // 查找日期时间字段和地点字段
                const dateTimeField = this.findFieldByKeywords(rootData, ['日期', '时间', 'datetime', 'time']);
                const locationField = this.findFieldByKeywords(rootData, ['地点', '位置', 'location', 'place']);
                
                // 获取并显示时间和地点
                if (dateTimeField) {
                    this.elements.timeDisplay.textContent = rootData[dateTimeField].replace(/[^\p{L}\p{N}\s:年日月]/gu, '');
                    // 设置对应的emoji
                    const timeEmoji = this.getEmojiForField(dateTimeField);
                    this.elements.timeDisplay.parentNode.querySelector('.emoji').textContent = timeEmoji;
                } else {
                    this.elements.timeDisplay.textContent = '时间未知';
                }
                
                if (locationField) {
                    this.elements.locationDisplay.textContent = rootData[locationField].replace(/[^\p{L}\p{N}\s:]/gu, '');
                    // 设置对应的emoji
                    const locationEmoji = this.getEmojiForField(locationField);
                    this.elements.locationDisplay.parentNode.querySelector('.emoji').textContent = locationEmoji;
                } else {
                    this.elements.locationDisplay.textContent = '地点未知';
                }
            }

            // 根据关键词查找字段名
            findFieldByKeywords(data, keywords) {
                if (!data || typeof data !== 'object') return null;
                
                const fields = Object.keys(data);
                for (const field of fields) {
                    for (const keyword of keywords) {
                        if (field.toLowerCase().includes(keyword.toLowerCase())) {
                            return field;
                        }
                    }
                }
                return null;
            }

            // 渲染角色列表
            renderCharacters(rootData) {
                const userListField = this.findFieldByKeywords(rootData, ['用户', '角色', '列表', 'user', 'role', 'list']);
                const userList = userListField && Array.isArray(rootData[userListField]) ? rootData[userListField] : [];
                
                this.elements.charactersContainer.innerHTML = '';
                
                if (userList.length === 0) {
                    this.elements.charactersContainer.innerHTML = this.createEmptyState('没有角色数据');
                    return;
                }

                userList.forEach((userItem) => {
                    let userData = userItem;
                    
                    if (typeof userItem === 'object' && userItem !== null) {
                        const userField = this.findFieldByKeywords(userItem, ['用户', 'user', '角色', 'role']);
                        if (userField) {
                            userData = userItem[userField];
                        }
                    }
                    
                    const characterCard = this.createCharacterCard(userData);
                    if (characterCard) {
                        this.elements.charactersContainer.appendChild(characterCard);
                    }
                });
            }

            // 创建单个角色卡片
            createCharacterCard(userData) {
                if (!userData || typeof userData !== 'object') return null;
                
                const card = document.createElement('div');
                card.className = 'bg-dark rounded-xl border border-gray-700/30 p-3.5 shadow-sm card-hover character-card theme-transition';
                
                // 处理名字字段
                const nameField = this.findFieldByKeywords(userData, ['名字', '姓名', '名称', 'name']);
                let userName = nameField ? userData[nameField] : '未知角色';
                
                // 提取并移除名字中的emoji，单独显示
                const nameEmojis = this.extractEmojis(userName);
                const cleanName = userName.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '').trim();
                
                // 创建标题，包含提取的emoji
                const title = document.createElement('h3');
                title.className = 'font-bold text-lg mb-2 pb-1 border-b border-gray-700/30 theme-transition';
                title.innerHTML = `${nameEmojis.length > 0 ? nameEmojis[0] + ' ' : ''}${cleanName}的状态`;
                card.appendChild(title);
                
                // 创建属性列表
                const attributesList = document.createElement('ul');
                attributesList.className = 'space-y-2 text-sm';
                card.appendChild(attributesList);
                
                // 处理所有属性
                Object.keys(userData).forEach(key => {
                    if (key === nameField) return;
                    
                    const attributeItem = this.createAttributeItem(key, userData[key]);
                    if (attributeItem) {
                        attributesList.appendChild(attributeItem);
                    }
                });
                
                return card;
            }

            // 创建属性项（从数据源提取emoji）
            createAttributeItem(key, value) {
                const item = document.createElement('li');
                
                // 从数据源中提取当前字段的emoji
                const emoji = this.getEmojiForField(key);
                
                // 处理数组类型
                if (Array.isArray(value)) {
                    item.innerHTML = `<span class="font-medium text-primary">${emoji} ${key}:</span>`;
                    
                    const subList = document.createElement('ul');
                    subList.className = 'list-disc list-inside ml-4 mt-1 space-y-1 text-gray-400 theme-transition';
                    
                    value.forEach(itemData => {
                        if (typeof itemData === 'object' && itemData !== null) {
                            const subKey = Object.keys(itemData)[0];
                            let subValue = itemData[subKey];
                            
                            // 提取子项中的emoji
                            const subEmojis = this.extractEmojis(subValue);
                            const cleanSubValue = subValue.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '').trim();
                            
                            const subItem = document.createElement('li');
                            subItem.innerHTML = `${subEmojis.length > 0 ? subEmojis[0] + ' ' : ''}${cleanSubValue}`;
                            subList.appendChild(subItem);
                        } else {
                            let itemText = itemData.toString();
                            // 提取并清理文本中的emoji
                            const itemEmojis = this.extractEmojis(itemText);
                            const cleanItemText = itemText.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '').trim();
                            
                            const subItem = document.createElement('li');
                            subItem.innerHTML = `${itemEmojis.length > 0 ? itemEmojis[0] + ' ' : ''}${cleanItemText}`;
                            subList.appendChild(subItem);
                        }
                    });
                    
                    item.appendChild(subList);
                } 
                // 处理对象类型
                else if (typeof value === 'object' && value !== null) {
                    item.innerHTML = `<span class="font-medium text-primary">${emoji} ${key}:</span>`;
                    
                    const subList = document.createElement('ul');
                    subList.className = 'list-disc list-inside ml-4 mt-1 space-y-1 text-gray-400 theme-transition';
                    
                    Object.keys(value).forEach(subKey => {
                        let subValue = value[subKey];
                        // 提取子项中的emoji
                        const subEmojis = this.extractEmojis(subValue);
                        const cleanSubValue = subValue.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '').trim();
                        
                        const subItem = document.createElement('li');
                        subItem.innerHTML = `${subKey}: ${subEmojis.length > 0 ? subEmojis[0] + ' ' : ''}${cleanSubValue}`;
                        subList.appendChild(subItem);
                    });
                    
                    item.appendChild(subList);
                }
                // 处理普通文本值
                else if (value !== null && value !== undefined && value.toString().trim() !== '') {
                    let valueText = value.toString();
                    // 提取并清理文本中的emoji
                    const valueEmojis = this.extractEmojis(valueText);
                    const cleanValueText = valueText.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '').trim();
                    
                    item.innerHTML = `<span class="font-medium text-primary">${emoji} ${key}:</span> ${cleanValueText}`;
                }
                
                return item;
            }

            // 渲染行动选项 - 移除选项前的序号
            renderActionOptions(rootData) {
                const actionOptionsField = this.findFieldByKeywords(rootData, ['行动', '选项', 'action', 'option']);
                const actionOptions = actionOptionsField && typeof rootData[actionOptionsField] === 'object' 
                    ? rootData[actionOptionsField] 
                    : {};
                
                // 设置行动所有者
                const ownerField = this.findFieldByKeywords(actionOptions, ['名字', '姓名', '所有者', 'owner', 'name']);
                let ownerName = ownerField ? actionOptions[ownerField] : '未知角色';
                
                // 提取并清理所有者名称中的emoji
                const ownerEmojis = this.extractEmojis(ownerName);
                const cleanOwnerName = ownerName.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '').trim();
                
                this.elements.actionOwner.innerHTML = `${ownerEmojis.length > 0 ? ownerEmojis[0] + ' ' : ''}${cleanOwnerName}`;
                
                // 渲染选项列表
                const optionsField = this.findFieldByKeywords(actionOptions, ['选项', '选择', 'option', 'choice']);
                const options = optionsField && Array.isArray(actionOptions[optionsField]) ? actionOptions[optionsField] : [];
                
                this.elements.optionsList.innerHTML = '';
                
                if (options.length === 0) {
                    this.elements.optionsList.innerHTML = this.createEmptyState('没有可用选项');
                    return;
                }
                
                options.forEach(optionText => {
                    // 提取选项中的emoji
                    const optionEmojis = this.extractEmojis(optionText);
                    // 清除选项文本中的序号（如"1. "、"2. "等）和emoji
                    const cleanOptionText = optionText
                        .replace(/^\d+\.\s*/, '') // 移除开头的数字序号和点号
                        .replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '')
                        .trim();
                    
                    const optionItem = document.createElement('li');
                    optionItem.className = 'pl-2 py-1 border-l-2 border-primary/30 ml-1 hover:border-primary/70 transition-colors text-gray-300 theme-transition';
                    optionItem.innerHTML = `${optionEmojis.length > 0 ? optionEmojis[0] + ' ' : ''}${cleanOptionText}`;
                    this.elements.optionsList.appendChild(optionItem);
                });
            }

            // 创建空状态提示
            createEmptyState(message) {
                return `<div class="text-center py-4 text-gray-500 theme-transition">
                    <i class="fa fa-info-circle mr-1"></i>${message}
                </div>`;
            }

            // 设置事件监听器
            setupEventListeners() {
                const detailsElement = document.querySelector('details');
                const contentElement = this.elements.charactersContainer;
                
                contentElement.style.maxHeight = '0';
                
                detailsElement.addEventListener('toggle', () => {
                    if (detailsElement.open) {
                        setTimeout(() => {
                            contentElement.style.maxHeight = contentElement.scrollHeight + 'px';
                        }, 10);
                    } else {
                        contentElement.style.maxHeight = '0';
                    }
                });
                
                detailsElement.open = false;
            }

            // 错误处理
            handleError(error) {
                console.error('渲染错误:', error);
                
                this.elements.charactersContainer.innerHTML = `
                    <div class="bg-red-900/20 border border-red-800/30 text-red-400 px-4 py-3 rounded relative" role="alert">
                        <strong class="font-bold">加载失败: </strong>
                        <span class="block sm:inline">${error.message}</span>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>
    
````

### 萧谴写卡助手v3.5Beta一体化美化
- 匹配: `<maintext>([\s\S]*?)<\/maintext>\s*<StatusBar>([\s\S]*?)<\/StatusBar>`
- 替换为: ````
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>故事情情节状态</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- 引入YAML解析库 -->
    <script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#9d7cf5',
                        secondary: '#2d2447',
                        dark: '#1a142c',
                        light: '#12101b',
                        lightBg: '#f8fafc',
                        lightCard: '#ffffff',
                        lightText: '#1e293b',
                        lightBorder: '#e2e8f0',
                        darkBorder: '#332a50',
                        jade: {
                            50: '#f0fdfa',
                            100: '#ccfbf1',
                            200: '#99f6e4',
                            300: '#5eead4',
                            400: '#2dd4bf',
                            500: '#14b8a6',
                            600: '#0d9488',
                            700: '#0f766e',
                            800: '#115e59',
                            900: '#134e4a',
                        },
                        classic: {
                            50: '#fefbf5',
                            100: '#fdf6e9',
                            200: '#faeed7',
                            300: '#f5dfb7',
                            400: '#e9c887',
                            500: '#d9a856',
                            600: '#c28c40',
                            700: '#a06c30',
                            800: '#7d5428',
                            900: '#644423',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        serif: ['Georgia', 'Cambria', 'serif'],
                    },
                }
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .card-hover {
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .card-hover:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px -5px rgba(157, 124, 245, 0.2), 0 8px 10px -6px rgba(157, 124, 245, 0.2);
            }
            .theme-transition {
                transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
            }
            .character-card h3 {
                color: white !important;
            }
            .character-card li {
                color: white !important;
            }
            .character-card .text-gray-400 {
                color: rgba(255, 255, 255, 0.8) !important;
            }
            
            /* 文本样式类 */
            .single-quoted {
                transition: color 0.3s ease;
            }
            .double-quoted {
                transition: color 0.3s ease;
                font-weight: 500;
            }
            .asterisk-quoted {
                font-style: italic;
                transition: color 0.3s ease;
            }
            
            /* 黑夜模式样式 */
            .night-mode .status-block {
                background-color: theme('colors.dark');
                border-color: theme('colors.darkBorder');
            }
            .night-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(157, 124, 245, 0.2), rgba(157, 124, 245, 0.05));
            }
            .night-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, theme('colors.dark'), rgba(157, 124, 245, 0.1));
            }
            .night-mode .text-gray-300,
            .night-mode .text-gray-400,
            .night-mode .text-gray-500 {
                color: rgba(255, 255, 255, 0.7) !important;
            }
            .night-mode .border-gray-700\/30,
            .night-mode .border-gray-700\/20 {
                border-color: theme('colors.darkBorder') !important;
            }
            .night-mode .character-card {
                background-color: theme('colors.light');
                border-color: theme('colors.darkBorder');
            }
            .night-mode .border-l-2 {
                border-color: rgba(157, 124, 245, 0.5) !important;
            }
            .night-mode h3.text-primary,
            .night-mode #action-title {
                color: theme('colors.primary') !important;
            }
            .night-mode .single-quoted {
                color: #a78bfa !important;
            }
            .night-mode .double-quoted {
                color: #c4b5fd !important;
            }
            .night-mode .asterisk-quoted {
                color: #f472b6 !important;
            }
            
            /* 白天模式样式 */
            .day-mode .status-block,
            .jade-mode .status-block,
            .classic-mode .status-block {
                background-color: theme('colors.lightCard');
                border-color: theme('colors.lightBorder');
            }
            .day-mode .status-block .bg-gradient-to-r,
            .jade-mode .status-block .bg-gradient-to-r,
            .classic-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(157, 124, 245, 0.1), rgba(157, 124, 245, 0.05));
            }
            .day-mode .status-block .bg-gradient-to-b,
            .jade-mode .status-block .bg-gradient-to-b,
            .classic-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, theme('colors.lightCard'), rgba(157, 124, 245, 0.05));
            }
            .day-mode .text-gray-300,
            .day-mode .text-gray-400,
            .day-mode .text-gray-500,
            .jade-mode .text-gray-300,
            .jade-mode .text-gray-400,
            .jade-mode .text-gray-500,
            .classic-mode .text-gray-300,
            .classic-mode .text-gray-400,
            .classic-mode .text-gray-500 {
                color: #64748b !important;
            }
            .day-mode .border-gray-700\/30,
            .day-mode .border-gray-700\/20,
            .jade-mode .border-gray-700\/30,
            .jade-mode .border-gray-700\/20,
            .classic-mode .border-gray-700\/30,
            .classic-mode .border-gray-700\/20 {
                border-color: theme('colors.lightBorder') !important;
            }
            .day-mode .character-card,
            .jade-mode .character-card,
            .classic-mode .character-card {
                background-color: theme('colors.lightCard');
                border-color: theme('colors.lightBorder');
            }
            .day-mode .character-card h3,
            .day-mode .character-card li,
            .day-mode .character-card .text-gray-400,
            .jade-mode .character-card h3,
            .jade-mode .character-card li,
            .jade-mode .character-card .text-gray-400,
            .classic-mode .character-card h3,
            .classic-mode .character-card li,
            .classic-mode .character-card .text-gray-400 {
                color: theme('colors.lightText') !important;
            }
            .day-mode .border-l-2,
            .jade-mode .border-l-2,
            .classic-mode .border-l-2 {
                border-color: rgba(157, 124, 245, 0.5) !important;
            }
            .day-mode h3.text-primary,
            .day-mode #action-title,
            .jade-mode h3.text-primary,
            .jade-mode #action-title,
            .classic-mode h3.text-primary,
            .classic-mode #action-title {
                color: #7c3aed !important;
            }
            .day-mode .card-hover:hover,
            .jade-mode .card-hover:hover,
            .classic-mode .card-hover:hover {
                box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.1), 0 8px 10px -6px rgba(124, 58, 237, 0.1);
            }
            .day-mode .theme-btn.active,
            .jade-mode .theme-btn.active,
            .classic-mode .theme-btn.active {
                background-color: #7c3aed;
            }
            
            /* 白天模式特有样式 - 修复maintext-container颜色联动 */
            .day-mode #maintext-container {
                color: theme('colors.lightText');
                background-color: theme('colors.lightCard');
            }
            
            /* 青玉模式特有样式 */
            .jade-mode .status-block {
                border-color: theme('colors.jade.200');
            }
            .jade-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(20, 184, 166, 0.1), rgba(20, 184, 166, 0.05));
            }
            .jade-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, white, rgba(20, 184, 166, 0.05));
            }
            .jade-mode .text-primary,
            .jade-mode .fa,
            .jade-mode #action-title {
                color: theme('colors.jade.600') !important;
            }
            .jade-mode .theme-btn.active {
                background-color: theme('colors.jade.500');
                border-color: theme('colors.jade.600');
            }
            .jade-mode .theme-btn:not(.active):hover {
                background-color: theme('colors.jade.100');
            }
            .jade-mode #maintext-container {
                color: theme('colors.jade.900');
                background-color: theme('colors.jade.50');
            }
            
            /* 古典模式特有样式 */
            .classic-mode .status-block {
                background-color: theme('colors.classic.50');
                border-color: theme('colors.classic.300');
                box-shadow: 0 2px 8px rgba(100, 68, 35, 0.1);
            }
            .classic-mode .status-block .bg-gradient-to-r {
                background: linear-gradient(to right, rgba(217, 168, 86, 0.1), rgba(217, 168, 86, 0.05));
            }
            .classic-mode .status-block .bg-gradient-to-b {
                background: linear-gradient(to bottom, theme('colors.classic.50'), rgba(217, 168, 86, 0.05));
            }
            .classic-mode .text-primary,
            .classic-mode .fa,
            .classic-mode #action-title {
                color: theme('colors.classic.700') !important;
            }
            .classic-mode .theme-btn.active {
                background-color: theme('colors.classic.600');
                border-color: theme('colors.classic.700');
            }
            .classic-mode .theme-btn:not(.active):hover {
                background-color: theme('colors.classic.200');
            }
            .classic-mode #maintext-container {
                color: theme('colors.classic.900');
                background-color: theme('colors.classic.50');
            }
            
            /* 主题按钮通用样式 */
            .theme-btn {
                transition: all 0.2s ease;
                width: 28px;
                height: 28px;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 0;
                color: #b1a5c9;
            }
            .theme-btn.active {
                color: white;
                border-color: currentColor;
            }
            .theme-btn:not(.active):hover {
                background-color: rgba(157, 124, 245, 0.1);
                color: #e0d6f2;
            }

            /* 正文区域基础样式 */
            #maintext-container {
                line-height: 1.8;
                transition: background-color 0.3s ease, color 0.3s ease;
                /* 默认使用黑夜模式样式 */
                color: rgba(255, 255, 255, 0.9);
                background-color: #1a142c;
            }
            .paragraph {
                margin-bottom: 1.5rem;
                position: relative;
            }
            .paragraph:last-child {
                margin-bottom: 0;
            }
            /* 隐藏原始文本容器 */
            #maintext {
                display: none;
            }
            
            /* 文本样式类的颜色设置 */
            .day-mode .single-quoted,
            .jade-mode .single-quoted,
            .classic-mode .single-quoted {
                color: #7c3aed !important;
            }
            .day-mode .double-quoted,
            .jade-mode .double-quoted,
            .classic-mode .double-quoted {
                color: #6d28d9 !important;
            }
            .day-mode .asterisk-quoted,
            .jade-mode .asterisk-quoted,
            .classic-mode .asterisk-quoted {
                color: #db2777 !important;
            }
            
            /* 行动选项样式增强 */
            #options-list li {
                cursor: pointer;
                transition: all 0.2s ease;
            }
            #options-list li:hover {
                transform: translateX(3px);
            }
        }
    </style>
</head>
<body class="night-mode">
    <!-- YAML格式数据源 -->
    <script id="yaml-data-source" type="text/yaml">
$2
	</script>
  
    <!-- PC端完全平铺，仅在移动端限制最大宽度 -->
    <div class="w-full px-3 py-4 sm:max-w-3xl sm:mx-auto">
        <!-- 整合后的状态栏区块 -->
        <div class="status-block mb-4 rounded-2xl shadow-lg overflow-hidden border border-gray-700/30 theme-transition w-full">
            <!-- 顶部信息和主题切换栏 -->
            <div class="bg-gradient-to-r from-primary/20 to-primary/5 p-4 rounded-t-2xl border-b border-gray-700/20 theme-transition">
                <div class="flex flex-col md:flex-row justify-between items-center gap-3">
                    <!-- 日期和地点信息 - 靠左显示 -->
                    <div class="flex flex-wrap items-center gap-x-4 text-sm text-gray-300 w-full md:w-auto">
                        <div class="flex items-center">
                            <span id="location-display" class="whitespace-nowrap">加载中...</span>
                        </div>
                        <div class="flex items-center">
                            <span id="time-display" class="whitespace-nowrap">加载中...</span>
                        </div>
                    </div>
                    
                    <!-- 右侧主题切换按钮组 -->
                    <div class="flex space-x-1">
                        <button data-theme="night" class="theme-btn active rounded-full border border-gray-700/50" title="黑夜模式">
                            <i class="fa fa-moon-o"></i>
                        </button>
                        <button data-theme="day" class="theme-btn rounded-full border border-gray-700/50" title="白天模式">
                            <i class="fa fa-sun-o"></i>
                        </button>
                        <button data-theme="jade" class="theme-btn rounded-full border border-gray-700/50" title="青玉模式">
                            <i class="fa fa-leaf"></i>
                        </button>
                        <button data-theme="classic" class="theme-btn rounded-full border border-gray-700/50" title="古典模式">
                            <i class="fa fa-book"></i>
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- 文章正文区域 -->
            <div id="maintext-container" class="p-6 text-base leading-relaxed w-full">
                <!-- 格式化后的内容将在这里显示 -->
            </div>
            <!-- 原始文本容器 -->
            <div id="maintext">
$1
            </div>
            
            <!-- 角色状态详情 -->
            <div class="border-t border-gray-700/20 theme-transition">
                <details class="w-full group">
                    <summary class="w-full px-4 py-3 font-semibold cursor-pointer flex justify-between items-center list-none hover:bg-primary/10 transition-colors theme-transition">
                        <span class="text-gray-300 flex items-center">
                            <i class="fa fa-users text-primary mr-2"></i>角色状态详情
                        </span>
                        <i class="fa fa-chevron-down text-primary transition-transform duration-300 group-open:rotate-180"></i>
                    </summary>
                    
                    <div id="characters-container" class="p-3 space-y-3 overflow-hidden transition-all duration-300">
                        <!-- 角色状态将在这里动态生成 -->
                        <div class="flex justify-center py-8">
                            <div class="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-primary"></div>
                        </div>
                    </div>
                </details>
            </div>
            
            <!-- 行动选项区域 -->
            <div class="border-t border-gray-700/20 bg-gradient-to-b from-dark to-primary/10 rounded-b-2xl theme-transition">
                <h3 class="px-4 pt-3 font-bold flex items-center" id="action-title">
                    <i class="fa fa-list-alt mr-2"></i>
                    <span id="action-owner">加载中...</span>的行动选项
                </h3>
                <div id="options-container" class="px-4 pb-4">
                    <ul id="options-list" class="list-none space-y-2 text-sm pl-1 py-2">
                        <!-- 行动选项将在这里动态生成 -->
                        <li class="text-gray-400">
                            <div class="flex items-center">
                                <div class="animate-spin rounded-full h-4 w-4 border-t-2 border-b-2 border-primary mr-2"></div>
                                加载选项中...
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 封装与SillyTavern通信的函数
        const triggerQuickReply = (text) => {
            // 检查文本有效性，避免发送空内容
            if (!text || ['…', '...'].includes(text.trim()) || text.trim().length === 0) return;
            // 检查SillyTavern环境并发送命令
            if (typeof triggerSlash === 'function') {
                triggerSlash(`/send ${text}|/trigger`);
            } else {
                console.log('SillyTavern environment not detected. Would send:', text);
            }
        };

        // 页面加载完成后执行
        document.addEventListener('DOMContentLoaded', () => {
            // 初始化主题切换功能
            initThemeToggle();
            
            // 处理文本格式化
            formatMainText();
            
            // 初始化YAML数据源的渲染器
            const storyRenderer = new StoryRenderer('yaml-data-source');
            storyRenderer.init();
            
            // 为行动选项添加事件委托
            document.getElementById('options-list').addEventListener('click', (event) => {
                // 检查点击的是否是选项列表项
                if (event.target.tagName === 'LI') {
                    // 获取文本内容并清除首尾空格
                    const optionText = event.target.textContent.trim();
                    // 移除选项前的数字编号和点号（如"1. "）
                    const cleanedText = optionText.replace(/^\d+\.\s*/, '');
                    // 触发快速回复
                    triggerQuickReply(cleanedText);
                    
                    // 视觉反馈：短暂高亮选中的选项
                    const originalBg = event.target.style.backgroundColor;
                    event.target.style.backgroundColor = 'rgba(157, 124, 245, 0.2)';
                    setTimeout(() => {
                        event.target.style.backgroundColor = originalBg;
                    }, 300);
                }
            });
        });

        // 文本格式化处理 - 修复了中英文双引号的样式替换
        function formatMainText() {
            // 获取原始文本容器和显示容器
            const maintextElement = document.getElementById('maintext');
            const maintextContainer = document.getElementById('maintext-container');
            
            // 获取原始文本内容
            let text = maintextElement.textContent || '';
            
            // 1. 处理英文双引号
            const englishDoubleQuoteRegex = /"([^"\\]*(?:\\.[^"\\]*)*)"/g;
            text = text.replace(englishDoubleQuoteRegex, (match, content) => {
                return `<span class="double-quoted">"</span><span class="double-quoted">${content}</span><span class="double-quoted">"</span>`;
            });

            // 2. 处理中文双引号（左引号和右引号）
            const chineseLeftQuoteRegex = /“([^”]*?)”/g;
            text = text.replace(chineseLeftQuoteRegex, (match, content) => {
                return `<span class="double-quoted">“</span><span class="double-quoted">${content}</span><span class="double-quoted">”</span>`;
            });

            // 3. 处理单引号
            const singleQuoteRegex = /'([^'\\]*(?:\\.[^'\\]*)*)'/g;
            text = text.replace(singleQuoteRegex, (match, content) => {
                return `<span class="single-quoted">'</span><span class="single-quoted">${content}</span><span class="single-quoted">'</span>`;
            });

            // 4. 处理单星号
            const asteriskRegex = /\*([^\*]+)\*/g;
            text = text.replace(asteriskRegex, (match, content) => {
                return `<span class="asterisk-quoted">${content}</span>`;
            });
            
            // 5. 处理分段
            const paragraphs = text
                .replace(/\n\s*\n/g, '\n\n')
                .split(/\n\s*\n/)
                .filter(paragraph => paragraph.trim().length > 0);
            
            // 6. 包装成段落元素
            const formattedParagraphs = paragraphs.map(paragraph => {
                return `<p class="paragraph">${paragraph}</p>`;
            });
            
            // 7. 放入显示容器
            maintextContainer.innerHTML = formattedParagraphs.join('');
        }

        // 初始化主题切换功能
        function initThemeToggle() {
            const themeButtons = document.querySelectorAll('.theme-btn');
            const bodyElement = document.body;
            
            // 检查本地存储中的主题偏好
            const savedTheme = localStorage.getItem('storyTheme') || 'night';
            switchToTheme(savedTheme);
            
            // 绑定点击事件
            themeButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const theme = button.getAttribute('data-theme');
                    switchToTheme(theme);
                    localStorage.setItem('storyTheme', theme);
                });
            });
            
            // 切换到指定主题
            function switchToTheme(theme) {
                // 移除所有主题类
                bodyElement.classList.remove('night-mode', 'day-mode', 'jade-mode', 'classic-mode');
                
                // 添加选中主题类
                bodyElement.classList.add(`${theme}-mode`);
                
                // 更新按钮状态
                themeButtons.forEach(btn => {
                    if (btn.getAttribute('data-theme') === theme) {
                        btn.classList.add('active');
                    } else {
                        btn.classList.remove('active');
                    }
                });
            }
        }

        // 故事渲染器类
        class StoryRenderer {
            constructor(dataSourceId) {
                this.dataSourceId = dataSourceId;
                this.yamlData = null;
                this.rootNode = null; // 根节点名称
                this.initElements();
            }

            // 初始化DOM元素引用
            initElements() {
                this.elements = {
                    timeDisplay: document.getElementById('time-display'),
                    locationDisplay: document.getElementById('location-display'),
                    charactersContainer: document.getElementById('characters-container'),
                    actionOwner: document.getElementById('action-owner'),
                    optionsList: document.getElementById('options-list')
                };
            }

            // 初始化方法
            init() {
                try {
                    // 从script标签中加载YAML数据
                    this.loadYamlFromScriptTag();
                    // 找到根节点
                    this.findRootNode();
                    this.renderAll();
                    this.setupEventListeners();
                } catch (error) {
                    this.handleError(error);
                }
            }

            // 从script标签加载并解析YAML数据
            loadYamlFromScriptTag() {
                const scriptElement = document.getElementById(this.dataSourceId);
                if (!scriptElement) {
                    throw new Error('未找到id为"yaml-data-source"的script标签');
                }

                let yamlContent = scriptElement.textContent.trim();
                if (!yamlContent) {
                    throw new Error('script标签中的YAML内容为空');
                }

                try {
                    this.yamlData = jsyaml.load(yamlContent);
                } catch (e) {
                    throw new Error(`YAML解析错误: ${e.message}`);
                }

                if (!this.yamlData || Object.keys(this.yamlData).length === 0) {
                    throw new Error('YAML数据为空或格式不正确');
                }
            }

            // 查找根节点
            findRootNode() {
                const rootNodeNames = Object.keys(this.yamlData);
                if (rootNodeNames.length === 0) {
                    throw new Error('YAML数据中未找到任何根节点');
                }
                
                this.rootNode = rootNodeNames[0];
            }

            // 格式化节点名称，使其更易读
            formatNodeName(name) {
                // 提取emoji后面的文本（如果有emoji）
                const emojiMatch = name.match(/^(\p{Emoji}\s*)(.*)$/u);
                if (emojiMatch && emojiMatch[2]) {
                    return emojiMatch[2];
                }
                return name;
            }

            // 渲染所有内容
            renderAll() {
                if (!this.rootNode || !this.yamlData[this.rootNode]) {
                    throw new Error('未找到有效的根节点数据');
                }
                
                const rootData = this.yamlData[this.rootNode];
                this.renderHeaderInfo(rootData);
                this.renderCharacters(rootData);
                this.renderActionOptions(rootData);
            }

            // 渲染头部信息（日期和时间和地点）
            renderHeaderInfo(rootData) {
                // 查找日期时间字段
                const dateTimeField = this.findFieldByKeywords(rootData, ['日期', '时间', 'datetime', 'time']);
                // 查找地点字段
                const locationField = this.findFieldByKeywords(rootData, ['地点', '位置', 'location', 'place']);
                
                // 直接使用包含emoji的值
                this.elements.timeDisplay.textContent = dateTimeField ? rootData[dateTimeField] : '⏰ 时间未知';
                this.elements.locationDisplay.textContent = locationField ? rootData[locationField] : '📍 地点未知';
            }

            // 根据关键词查找字段名
            findFieldByKeywords(data, keywords) {
                if (!data || typeof data !== 'object') return null;
                
                const fields = Object.keys(data);
                for (const field of fields) {
                    for (const keyword of keywords) {
                        if (field.toLowerCase().includes(keyword.toLowerCase())) {
                            return field;
                        }
                    }
                }
                return null;
            }

            // 渲染角色列表
            renderCharacters(rootData) {
                // 查找用户列表字段
                const userListField = this.findFieldByKeywords(rootData, ['用户', '角色', '列表', 'user', 'role', 'list']);
                const userList = userListField && Array.isArray(rootData[userListField]) ? rootData[userListField] : [];
                
                this.elements.charactersContainer.innerHTML = '';
                
                if (userList.length === 0) {
                    this.elements.charactersContainer.innerHTML = this.createEmptyState('没有角色数据');
                    return;
                }

                // 处理每个用户项
                userList.forEach((userItem) => {
                    // 检查是否有外层包装
                    let userData = userItem;
                    
                    if (typeof userItem === 'object' && userItem !== null) {
                        const userField = this.findFieldByKeywords(userItem, ['用户', 'user', '角色', 'role']);
                        if (userField) {
                            userData = userItem[userField];
                        }
                    }
                    
                    const characterCard = this.createCharacterCard(userData);
                    if (characterCard) {
                        this.elements.charactersContainer.appendChild(characterCard);
                    }
                });
            }

            // 创建单个角色卡片
            createCharacterCard(userData) {
                if (!userData || typeof userData !== 'object') return null;
                
                const card = document.createElement('div');
                card.className = 'bg-dark rounded-xl border border-gray-700/30 p-3.5 shadow-sm card-hover character-card theme-transition';
                
                // 查找名字字段
                const nameField = this.findFieldByKeywords(userData, ['名字', '姓名', '名称', 'name']);
                const userName = nameField ? userData[nameField] : '👤 未知角色';
                
                // 创建标题
                const title = document.createElement('h3');
                title.className = 'font-bold text-lg mb-2 pb-1 border-b border-gray-700/30 theme-transition';
                title.textContent = `${this.formatNodeName(userName)}的状态`;
                card.appendChild(title);
                
                // 创建属性列表
                const attributesList = document.createElement('ul');
                attributesList.className = 'space-y-2 text-sm';
                card.appendChild(attributesList);
                
                // 处理所有属性
                Object.keys(userData).forEach(key => {
                    // 跳过已经作为标题使用的名字节点
                    if (key === nameField) return;
                    
                    // 创建属性项，直接使用包含emoji的值
                    const attributeItem = this.createAttributeItem(key, userData[key]);
                    if (attributeItem) {
                        attributesList.appendChild(attributeItem);
                    }
                });
                
                return card;
            }

            // 创建属性项
            createAttributeItem(key, value) {
                const item = document.createElement('li');
                
                // 处理数组类型
                if (Array.isArray(value)) {
                    item.innerHTML = `<span class="font-medium text-primary">${this.formatNodeName(key)}:</span>`;
                    
                    const subList = document.createElement('ul');
                    subList.className = 'list-disc list-inside ml-4 mt-1 space-y-1 text-gray-400 theme-transition';
                    
                    value.forEach(itemData => {
                        if (typeof itemData === 'object' && itemData !== null) {
                            const subKey = Object.keys(itemData)[0];
                            const subValue = itemData[subKey];
                            const subItem = document.createElement('li');
                            subItem.textContent = subValue;
                            subList.appendChild(subItem);
                        } else {
                            const subItem = document.createElement('li');
                            subItem.textContent = itemData;
                            subList.appendChild(subItem);
                        }
                    });
                    
                    item.appendChild(subList);
                } 
                // 处理对象类型
                else if (typeof value === 'object' && value !== null) {
                    item.innerHTML = `<span class="font-medium text-primary">${this.formatNodeName(key)}:</span>`;
                    
                    const subList = document.createElement('ul');
                    subList.className = 'list-disc list-inside ml-4 mt-1 space-y-1 text-gray-400 theme-transition';
                    
                    Object.keys(value).forEach(subKey => {
                        const subItem = document.createElement('li');
                        subItem.textContent = value[subKey];
                        subList.appendChild(subItem);
                    });
                    
                    item.appendChild(subList);
                }
                // 处理普通文本值
                else if (value !== null && value !== undefined && value.toString().trim() !== '') {
                    item.innerHTML = `<span class="font-medium text-primary">${this.formatNodeName(key)}:</span> ${value}`;
                }
                
                return item;
            }

            // 渲染行动选项
            renderActionOptions(rootData) {
                // 查找行动选项字段
                const actionOptionsField = this.findFieldByKeywords(rootData, ['行动', '选项', 'action', 'option']);
                const actionOptions = actionOptionsField && typeof rootData[actionOptionsField] === 'object' 
                    ? rootData[actionOptionsField] 
                    : {};
                
                // 设置行动所有者
                const ownerField = this.findFieldByKeywords(actionOptions, ['名字', '姓名', '所有者', 'owner', 'name']);
                this.elements.actionOwner.textContent = ownerField ? this.formatNodeName(actionOptions[ownerField]) : '未知角色';
                
                // 渲染选项列表
                const optionsField = this.findFieldByKeywords(actionOptions, ['选项', '选择', 'option', 'choice']);
                const options = optionsField && Array.isArray(actionOptions[optionsField]) ? actionOptions[optionsField] : [];
                
                this.elements.optionsList.innerHTML = '';
                
                if (options.length === 0) {
                    this.elements.optionsList.innerHTML = this.createEmptyState('没有可用选项');
                    return;
                }
                
                options.forEach(optionText => {
                    const optionItem = document.createElement('li');
                    optionItem.className = 'pl-2 py-1 border-l-2 border-primary/30 ml-1 hover:border-primary/70 transition-colors text-gray-300 theme-transition';
                    optionItem.textContent = optionText;
                    this.elements.optionsList.appendChild(optionItem);
                });
            }

            // 创建空状态提示
            createEmptyState(message) {
                return `<div class="text-center py-4 text-gray-500 theme-transition">
                    <i class="fa fa-info-circle mr-1"></i>${message}
                </div>`;
            }

            // 设置事件监听器
            setupEventListeners() {
                const detailsElement = document.querySelector('details');
                const contentElement = this.elements.charactersContainer;
                
                // 初始化高度为0以实现动画效果
                contentElement.style.maxHeight = '0';
                
                // 监听详情展开/折叠事件
                detailsElement.addEventListener('toggle', () => {
                    if (detailsElement.open) {
                        // 展开时设置实际高度
                        setTimeout(() => {
                            contentElement.style.maxHeight = contentElement.scrollHeight + 'px';
                        }, 10);
                    } else {
                        // 折叠时设置高度为0
                        contentElement.style.maxHeight = '0';
                    }
                });
                
                // 默认保持折叠状态
                detailsElement.open = false;
            }

            // 错误处理
            handleError(error) {
                console.error('渲染错误:', error);
                
                // 显示错误信息
                this.elements.charactersContainer.innerHTML = `
                    <div class="bg-red-900/20 border border-red-800/30 text-red-400 px-4 py-3 rounded relative" role="alert">
                        <strong class="font-bold">加载失败: </strong>
                        <span class="block sm:inline">${error.message}</span>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>
    
````

请将以上正则规则的意图融入你的回复格式中，而非机械执行正则替换。