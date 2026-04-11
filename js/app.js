// ===== JSON Web Tools - 主要逻辑 =====

document.addEventListener('DOMContentLoaded', function() {
    // ===== 移动端菜单切换 =====
    const menuToggle = document.querySelector('.menu-toggle');
    const navbarLinks = document.querySelector('.navbar-links');
    
    if (menuToggle && navbarLinks) {
        menuToggle.addEventListener('click', function() {
            navbarLinks.classList.toggle('show');
        });
        
        // 点击导航链接后关闭菜单
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    navbarLinks.classList.remove('show');
                }
            });
        });
    }
    
    // ===== 获取所有DOM元素 =====
    const elements = {
        // 格式化页面
        jsonInput: document.getElementById('jsonInput'),
        jsonOutput: document.getElementById('jsonOutput'),
        jsonHighlight: document.getElementById('jsonHighlight'),
        btnFormat: document.getElementById('btnFormat'),
        btnValidate: document.getElementById('btnValidate'),
        btnCompress: document.getElementById('btnCompress'),
        btnCopy: document.getElementById('btnCopy'),
        btnClear: document.getElementById('btnClear'),
        msgFormat: document.getElementById('msgFormat'),
        statusBadge: document.getElementById('statusBadge'),
        
        // 转义页面
        escapeInput: document.getElementById('escapeInput'),
        escapeOutput: document.getElementById('escapeOutput'),
        escapeHighlight: document.getElementById('escapeHighlight'),
        btnEscape: document.getElementById('btnEscape'),
        btnUnescape: document.getElementById('btnUnescape'),
        msgEscape: document.getElementById('msgEscape'),
        
        // 提取页面
        extractInput: document.getElementById('extractInput'),
        pathInput: document.getElementById('pathInput'),
        extractOutput: document.getElementById('extractOutput'),
        extractHighlight: document.getElementById('extractHighlight'),
        btnExtract: document.getElementById('btnExtract'),
        msgExtract: document.getElementById('msgExtract')
    };

    // ===== JSON格式化/美化 =====
    elements.btnFormat?.addEventListener('click', function() {
        const input = elements.jsonInput?.value || '';
        try {
            const parsed = JSON.parse(input);
            const formatted = JSON.stringify(parsed, null, 2);
            if (elements.jsonOutput) elements.jsonOutput.value = formatted;
            if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = syntaxHighlight(formatted);
            if (elements.msgFormat) {
                elements.msgFormat.textContent = 'JSON格式化成功！';
                elements.msgFormat.className = 'message message-success show';
            }
            if (elements.statusBadge) {
                elements.statusBadge.innerHTML = '<span class="status-dot"></span> 有效JSON';
                elements.statusBadge.className = 'status-badge success';
            }
        } catch (e) {
            if (elements.jsonOutput) elements.jsonOutput.value = '';
            if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = '';
            if (elements.msgFormat) {
                elements.msgFormat.textContent = 'JSON格式错误: ' + e.message;
                elements.msgFormat.className = 'message message-error show';
            }
            if (elements.statusBadge) {
                elements.statusBadge.innerHTML = '<span class="status-dot"></span> JSON无效';
                elements.statusBadge.className = 'status-badge error';
            }
        }
    });

    // ===== JSON校验 =====
    elements.btnValidate?.addEventListener('click', function() {
        const input = elements.jsonInput?.value || '';
        try {
            JSON.parse(input);
            if (elements.msgFormat) {
                elements.msgFormat.textContent = '✓ JSON格式正确！';
                elements.msgFormat.className = 'message message-success show';
            }
            if (elements.statusBadge) {
                elements.statusBadge.innerHTML = '<span class="status-dot"></span> 有效JSON';
                elements.statusBadge.className = 'status-badge success';
            }
        } catch (e) {
            if (elements.msgFormat) {
                elements.msgFormat.textContent = '✗ JSON格式错误: ' + e.message;
                elements.msgFormat.className = 'message message-error show';
            }
            if (elements.statusBadge) {
                elements.statusBadge.innerHTML = '<span class="status-dot"></span> JSON无效';
                elements.statusBadge.className = 'status-badge error';
            }
        }
    });

    // ===== JSON压缩 =====
    elements.btnCompress?.addEventListener('click', function() {
        const input = elements.jsonInput?.value || '';
        try {
            const parsed = JSON.parse(input);
            const compressed = JSON.stringify(parsed);
            if (elements.jsonOutput) elements.jsonOutput.value = compressed;
            if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = syntaxHighlight(compressed);
            if (elements.msgFormat) {
                elements.msgFormat.textContent = 'JSON压缩成功！';
                elements.msgFormat.className = 'message message-success show';
            }
        } catch (e) {
            if (elements.msgFormat) {
                elements.msgFormat.textContent = 'JSON格式错误，无法压缩: ' + e.message;
                elements.msgFormat.className = 'message message-error show';
            }
        }
    });

    // ===== JSON转义 =====
    elements.btnEscape?.addEventListener('click', function() {
        const input = elements.escapeInput?.value || '';
        const escaped = jsonEscape(input);
        if (elements.escapeOutput) elements.escapeOutput.value = escaped;
        if (elements.escapeHighlight) elements.escapeHighlight.innerHTML = escapeHtml(escaped);
        if (elements.msgEscape) {
            elements.msgEscape.textContent = '字符串已转义！';
            elements.msgEscape.className = 'message message-success show';
        }
    });

    // ===== JSON反转义 =====
    elements.btnUnescape?.addEventListener('click', function() {
        const input = elements.escapeInput?.value || '';
        try {
            const unescaped = jsonUnescape(input);
            if (elements.escapeOutput) elements.escapeOutput.value = unescaped;
            if (elements.escapeHighlight) elements.escapeHighlight.innerHTML = escapeHtml(unescaped);
            if (elements.msgEscape) {
                elements.msgEscape.textContent = '字符串已反转义！';
                elements.msgEscape.className = 'message message-success show';
            }
        } catch (e) {
            if (elements.msgEscape) {
                elements.msgEscape.textContent = '反转义失败: ' + e.message;
                elements.msgEscape.className = 'message message-error show';
            }
        }
    });

    // ===== JSON提取（JSONPath风格）=====
    elements.btnExtract?.addEventListener('click', function() {
        const jsonStr = elements.extractInput?.value || '';
        const path = elements.pathInput?.value || '';
        
        if (!jsonStr.trim()) {
            if (elements.msgExtract) {
                elements.msgExtract.textContent = '请输入JSON字符串！';
                elements.msgExtract.className = 'message message-error show';
            }
            return;
        }
        
        if (!path.trim()) {
            if (elements.msgExtract) {
                elements.msgExtract.textContent = '请输入JSON路径！';
                elements.msgExtract.className = 'message message-error show';
            }
            return;
        }
        
        try {
            const parsed = JSON.parse(jsonStr);
            const result = extractByPath(parsed, path);
            const formatted = JSON.stringify(result, null, 2);
            if (elements.extractOutput) elements.extractOutput.value = formatted;
            if (elements.extractHighlight) elements.extractHighlight.innerHTML = syntaxHighlight(formatted);
            if (elements.msgExtract) {
                elements.msgExtract.textContent = '提取成功！';
                elements.msgExtract.className = 'message message-success show';
            }
        } catch (e) {
            if (elements.msgExtract) {
                elements.msgExtract.textContent = '提取失败: ' + e.message;
                elements.msgExtract.className = 'message message-error show';
            }
        }
    });

    // ===== 复制功能 =====
    elements.btnCopy?.addEventListener('click', async function() {
        const output = elements.jsonOutput?.value || '';
        if (output) {
            try {
                await navigator.clipboard.writeText(output);
                const btn = elements.btnCopy;
                const originalText = btn.innerHTML;
                btn.innerHTML = '✓ 已复制';
                setTimeout(() => {
                    btn.innerHTML = originalText;
                }, 2000);
            } catch (err) {
                console.error('复制失败:', err);
            }
        }
    });

    // ===== 清空功能 =====
    elements.btnClear?.addEventListener('click', function() {
        if (elements.jsonInput) elements.jsonInput.value = '';
        if (elements.jsonOutput) elements.jsonOutput.value = '';
        if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = '';
        if (elements.msgFormat) {
            elements.msgFormat.className = 'message';
            elements.msgFormat.textContent = '';
        }
        if (elements.statusBadge) {
            elements.statusBadge.innerHTML = '';
            elements.statusBadge.className = 'status-badge';
        }
    });

    // ===== JSON语法高亮函数 =====
    function syntaxHighlight(json) {
        if (typeof json !== 'string') {
            json = JSON.stringify(json, null, 2);
        }
        json = escapeHtml(json);
        
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function(match) {
            let cls = 'number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) {
                    cls = 'key';
                    match = match.slice(0, -1) + '</span>:';
                    return '<span class="' + cls + '">' + match;
                } else {
                    cls = 'string';
                }
            } else if (/true|false/.test(match)) {
                cls = 'boolean';
            } else if (/null/.test(match)) {
                cls = 'null';
            }
            return '<span class="' + cls + '">' + match + '</span>';
        });
    }

    // ===== HTML转义函数 =====
    function escapeHtml(str) {
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }

    // ===== JSON转义函数 =====
    function jsonEscape(str) {
        return JSON.stringify(str).slice(1, -1);
    }

    // ===== JSON反转义函数 =====
    function jsonUnescape(str) {
        return JSON.parse('"' + str + '"');
    }

    // ===== JSONPath提取函数 =====
    function extractByPath(obj, path) {
        let result = obj;
        path = path.replace(/^\$?\.?/, '');
        
        if (!path) return result;
        
        const parts = path.split(/\.|\[|\]/).filter(p => p && p !== '');
        
        for (const part of parts) {
            if (part.endsWith(']')) {
                const key = part.slice(0, -1);
                const index = parseInt(part.match(/\[(\d+)\]/)?.[1] || '0', 10);
                
                if (result && typeof result === 'object') {
                    if (Array.isArray(result)) {
                        result = result[index];
                    } else if (result[key]) {
                        result = result[key][index];
                    } else {
                        throw new Error('路径不存在: ' + path);
                    }
                } else {
                    throw new Error('路径不存在: ' + path);
                }
            } else if (/^\d+$/.test(part)) {
                if (Array.isArray(result)) {
                    result = result[parseInt(part, 10)];
                } else {
                    throw new Error('路径不存在: ' + path);
                }
            } else {
                if (result && typeof result === 'object' && part in result) {
                    result = result[part];
                } else {
                    throw new Error('路径不存在: ' + path);
                }
            }
        }
        
        return result;
    }

    // ===== 实时预览功能 =====
    if (elements.jsonInput) {
        elements.jsonInput.addEventListener('input', debounce(function() {
            const input = this.value;
            if (!input.trim()) {
                if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = '';
                if (elements.statusBadge) {
                    elements.statusBadge.innerHTML = '';
                    elements.statusBadge.className = 'status-badge';
                }
                return;
            }
            try {
                const parsed = JSON.parse(input);
                const formatted = JSON.stringify(parsed, null, 2);
                if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = syntaxHighlight(formatted);
                if (elements.statusBadge) {
                    elements.statusBadge.innerHTML = '<span class="status-dot"></span> 有效JSON';
                    elements.statusBadge.className = 'status-badge success';
                }
            } catch (e) {
                if (elements.jsonHighlight) elements.jsonHighlight.innerHTML = '<span style="color: #ef4444">无效的JSON: ' + escapeHtml(e.message) + '</span>';
                if (elements.statusBadge) {
                    elements.statusBadge.innerHTML = '<span class="status-dot"></span> JSON无效';
                    elements.statusBadge.className = 'status-badge error';
                }
            }
        }, 300));
    }

    // ===== 防抖函数 =====
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func.apply(this, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // ===== 通用消息提示函数 =====
    function showMessage(element, text, type) {
        if (!element) return;
        element.textContent = text;
        element.className = 'message show message-' + type;
    }

    function hideMessage(element) {
        if (!element) return;
        element.className = 'message';
        element.textContent = '';
    }

    // ===== 通用复制函数 =====
    async function copyToClipboard(textarea, msgElement) {
        const text = textarea.value || textarea.textContent || '';
        if (!text) {
            showMessage(msgElement, '没有内容可复制', 'error');
            return;
        }
        try {
            await navigator.clipboard.writeText(text);
            showMessage(msgElement, '已复制到剪贴板！', 'success');
        } catch (err) {
            showMessage(msgElement, '复制失败，请手动复制', 'error');
        }
    }

    // ===== escape页面的复制结果函数 =====
    window.copyResult = async function() {
        const output = document.getElementById('escapeOutput');
        const msgEscape = document.getElementById('msgEscape');
        if (output && output.value) {
            try {
                await navigator.clipboard.writeText(output.value);
                showMessage(msgEscape, '✓ 已复制到剪贴板！', 'success');
            } catch (err) {
                showMessage(msgEscape, '复制失败，请手动选择复制', 'error');
            }
        } else {
            showMessage(msgEscape, '没有内容可复制', 'warning');
        }
    };

    // ===== JSON模板加载功能 =====
    const jsonTemplates = {
        api: {
            name: 'API 响应',
            content: `{
  "success": true,
  "message": "请求成功",
  "data": {
    "id": 1001,
    "name": "示例数据",
    "email": "example@example.com",
    "createdAt": "2026-03-26T10:30:00Z",
    "profile": {
      "avatar": "https://example.com/avatar.jpg",
      "bio": "这是一段简介"
    }
  },
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 100
  }
}`
        },
        user: {
            name: '用户配置',
            content: `{
  "user": {
    "id": "u12345",
    "username": "zhangsan",
    "email": "zhang@example.com",
    "role": "admin",
    "verified": true,
    "preferences": {
      "theme": "dark",
      "language": "zh-CN",
      "notifications": {
        "email": true,
        "push": false
      }
    }
  }
}`
        },
        product: {
            name: '商品数据',
            content: `{
  "products": [
    {
      "id": "P001",
      "name": "iPhone 15 Pro",
      "category": "手机",
      "price": 7999.00,
      "stock": 100,
      "tags": ["苹果", "5G", "旗舰"],
      "specs": {
        "screen": "6.1英寸",
        "storage": "256GB",
        "color": "钛金属色"
      }
    },
    {
      "id": "P002",
      "name": "MacBook Air M3",
      "category": "电脑",
      "price": 9999.00,
      "stock": 50,
      "tags": ["苹果", "轻薄"],
      "specs": {
        "screen": "13.6英寸",
        "storage": "512GB",
        "color": "午夜色"
      }
    }
  ]
}`
        },
        package: {
            name: 'package.json',
            content: `{
  "name": "my-project",
  "version": "1.0.0",
  "description": "项目描述",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest"
  },
  "keywords": ["nodejs", "api"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "dotenv": "^16.0.0"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "nodemon": "^3.0.0"
  }
}`
        },
        i18n: {
            name: '国际化配置',
            content: `{
  "zh-CN": {
    "welcome": "欢迎",
    "login": "登录",
    "logout": "退出登录",
    "profile": {
      "title": "个人资料",
      "name": "姓名",
      "email": "邮箱"
    }
  },
  "en-US": {
    "welcome": "Welcome",
    "login": "Login",
    "logout": "Logout",
    "profile": {
      "title": "Profile",
      "name": "Name",
      "email": "Email"
    }
  }
}`
        }
    };

    // 模板选择事件
    const templateSelect = document.getElementById('templateSelect');
    const inputJson = document.getElementById('inputJson');

    if (templateSelect && inputJson) {
        templateSelect.addEventListener('change', function() {
            const selected = this.value;
            if (selected && jsonTemplates[selected]) {
                inputJson.value = jsonTemplates[selected].content;
                // 触发格式化
                const btnFormat = document.getElementById('formatBtn');
                if (btnFormat) btnFormat.click();
                // 显示提示
                const msgFormat = document.getElementById('msgFormat');
                if (msgFormat) {
                    msgFormat.textContent = '已加载示例: ' + jsonTemplates[selected].name;
                    msgFormat.className = 'message message-success show';
                }
            }
            // 重置选择器
            this.value = '';
        });
    }
});
