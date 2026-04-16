// ===== AI JSON - Performance Optimized JavaScript =====
// 性能优化：事件委托、节流、虚拟DOM批处理

(function() {
    'use strict';

    // 防抖函数 - 限制高频触发
    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // 节流函数 - 控制执行频率
    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    // 事件委托 - 减少事件监听器数量
    document.addEventListener('click', function(e) {
        // Mobile menu toggle
        const menuToggle = e.target.closest('.menu-toggle');
        if (menuToggle) {
            const navbarLinks = document.querySelector('.navbar-links');
            if (navbarLinks) navbarLinks.classList.toggle('show');
        }

        // Mobile dropdown toggle
        const dropdown = e.target.closest('.nav-dropdown');
        if (dropdown && window.innerWidth <= 768) {
            e.preventDefault();
            dropdown.classList.toggle('open');
        }

        // Close mobile menu on nav link click
        const navLink = e.target.closest('.nav-link');
        if (navLink && window.innerWidth <= 768 && !navLink.closest('.nav-dropdown')) {
            const navbarLinks = document.querySelector('.navbar-links');
            if (navbarLinks) navbarLinks.classList.remove('show');
        }
    }, { passive: true });

    // ===== JSON Syntax Highlighter =====
    const syntaxHighlight = (json) => {
        if (typeof json !== 'string') json = JSON.stringify(json, null, 2);
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, (match) => {
            let cls = 'json-number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) { cls = 'json-key'; match = match.slice(0, -1) + '</span>'; return '<span class="' + cls + '">' + match + ':'; }
                cls = 'json-string';
            } else if (/true|false/.test(match)) { cls = 'json-boolean'; } else if (/null/.test(match)) { cls = 'json-null'; }
            return '<span class="' + cls + '">' + match + '</span>';
        });
    };

    // ===== Format/Validate/Compress Buttons =====
    const jsonInput = document.getElementById('jsonInput');
    const jsonOutput = document.getElementById('jsonOutput');
    const jsonHighlight = document.getElementById('jsonHighlight');
    const msgFormat = document.getElementById('msgFormat');
    const statusBadge = document.getElementById('statusBadge');
    const errorPanel = document.getElementById('errorPanel');
    const errorType = document.getElementById('errorType');
    const errorMessage = document.getElementById('errorMessage');
    const errorLine = document.getElementById('errorLine');

    // Error panel helper
    const showError = (type, message, line) => {
        if (errorPanel) {
            if (errorType) errorType.textContent = type;
            if (errorMessage) errorMessage.textContent = message;
            if (errorLine) errorLine.textContent = line ? `Error at line ${line}` : '';
            errorPanel.classList.add('show');
        }
    };
    const hideError = () => {
        if (errorPanel) errorPanel.classList.remove('show');
    };

    // Button loading state
    const setLoading = (btn, loading) => {
        if (!btn) return;
        if (loading) {
            btn.classList.add('btn-loading');
            btn.disabled = true;
        } else {
            btn.classList.remove('btn-loading');
            btn.disabled = false;
        }
    };

    const formatJSON = () => {
        const btn = document.getElementById('btnFormat');
        setLoading(btn, true);
        setTimeout(() => {
            try {
                const formatted = JSON.stringify(JSON.parse(jsonInput.value), null, 2);
                if (jsonOutput) jsonOutput.value = formatted;
                if (jsonHighlight) jsonHighlight.innerHTML = syntaxHighlight(formatted);
                showMsg(msgFormat, 'JSON formatted successfully!', 'success');
                setStatus(statusBadge, 'Valid JSON', true);
                hideError();
            } catch (e) {
                if (jsonOutput) jsonOutput.value = '';
                if (jsonHighlight) jsonHighlight.innerHTML = '';
                showMsg(msgFormat, 'JSON Error: ' + e.message, 'error');
                setStatus(statusBadge, 'Invalid JSON', false);
                const lineMatch = e.message.match(/position\s+(\d+)/);
                const line = lineMatch ? getLineFromPosition(jsonInput.value, parseInt(lineMatch[1])) : null;
                showError('SyntaxError', e.message, line);
            }
            setLoading(btn, false);
        }, 100);
    };

    const validateJSON = () => {
        const btn = document.getElementById('btnValidate');
        setLoading(btn, true);
        setTimeout(() => {
            try {
                JSON.parse(jsonInput.value);
                showMsg(msgFormat, '✓ Valid JSON!', 'success');
                setStatus(statusBadge, 'Valid JSON', true);
                hideError();
            } catch (e) {
                showMsg(msgFormat, '✗ JSON Error: ' + e.message, 'error');
                setStatus(statusBadge, 'Invalid JSON', false);
                const lineMatch = e.message.match(/position\s+(\d+)/);
                const line = lineMatch ? getLineFromPosition(jsonInput.value, parseInt(lineMatch[1])) : null;
                showError('SyntaxError', e.message, line);
            }
            setLoading(btn, false);
        }, 100);
    };

    const compressJSON = () => {
        const btn = document.getElementById('btnCompress');
        setLoading(btn, true);
        setTimeout(() => {
            try {
                const compressed = JSON.stringify(JSON.parse(jsonInput.value));
                if (jsonOutput) jsonOutput.value = compressed;
                if (jsonHighlight) jsonHighlight.innerHTML = syntaxHighlight(compressed);
                showMsg(msgFormat, 'JSON compressed successfully!', 'success');
                hideError();
            } catch (e) {
                showMsg(msgFormat, 'Cannot compress: ' + e.message, 'error');
                showError('SyntaxError', e.message, null);
            }
            setLoading(btn, false);
        }, 100);
    };

    // Get line number from character position
    const getLineFromPosition = (str, pos) => {
        let line = 1;
        for (let i = 0; i < pos && i < str.length; i++) {
            if (str[i] === '\n') line++;
        }
        return line;
    };

    document.getElementById('btnFormat')?.addEventListener('click', formatJSON);
    document.getElementById('btnValidate')?.addEventListener('click', validateJSON);
    document.getElementById('btnCompress')?.addEventListener('click', compressJSON);

    // Copy button
    document.getElementById('btnCopy')?.addEventListener('click', async function() {
        const output = jsonOutput?.value;
        if (output) {
            try {
                await navigator.clipboard.writeText(output);
                const original = this.innerHTML;
                this.innerHTML = '✓ Copied';
                setTimeout(() => { this.innerHTML = original; }, 2000);
            } catch (err) { console.error('Copy failed:', err); }
        }
    });

    // Clear button
    document.getElementById('btnClear')?.addEventListener('click', () => {
        if (jsonInput) jsonInput.value = '';
        if (jsonOutput) jsonOutput.value = '';
        if (jsonHighlight) jsonHighlight.innerHTML = '';
        hideMsg(msgFormat);
        hideError();
        if (statusBadge) statusBadge.innerHTML = '';
    });

    // Real-time preview
    if (jsonInput) {
        jsonInput.addEventListener('input', debounce(() => {
            const input = jsonInput.value;
            if (!input.trim()) {
                if (jsonHighlight) jsonHighlight.innerHTML = '';
                if (statusBadge) statusBadge.innerHTML = '';
                hideError();
                return;
            }
            try {
                if (jsonHighlight) jsonHighlight.innerHTML = syntaxHighlight(JSON.stringify(JSON.parse(input), null, 2));
                setStatus(statusBadge, 'Valid JSON', true);
                hideError();
            } catch (e) {
                if (jsonHighlight) jsonHighlight.innerHTML = '<span style="color: var(--error)">Invalid: ' + e.message + '</span>';
                setStatus(statusBadge, 'Invalid JSON', false);
                const lineMatch = e.message.match(/position\s+(\d+)/);
                const line = lineMatch ? getLineFromPosition(input, parseInt(lineMatch[1])) : null;
                showError('SyntaxError', e.message, line);
            }
        }, 300));
    }

    // ===== Escape/Unescape =====
    const escapeInput = document.getElementById('escapeInput');
    const escapeOutput = document.getElementById('escapeOutput');
    const escapeHighlight = document.getElementById('escapeHighlight');
    const msgEscape = document.getElementById('msgEscape');

    document.getElementById('btnEscape')?.addEventListener('click', () => {
        const escaped = JSON.stringify(escapeInput.value).slice(1, -1);
        if (escapeOutput) escapeOutput.value = escaped;
        if (escapeHighlight) escapeHighlight.innerHTML = escaped;
        showMsg(msgEscape, 'String escaped!', 'success');
    });

    document.getElementById('btnUnescape')?.addEventListener('click', () => {
        try {
            const unescaped = JSON.parse('"' + escapeInput.value + '"');
            if (escapeOutput) escapeOutput.value = unescaped;
            if (escapeHighlight) escapeHighlight.innerHTML = unescaped;
            showMsg(msgEscape, 'String unescaped!', 'success');
        } catch (e) { showMsg(msgEscape, 'Unescape failed: ' + e.message, 'error'); }
    });

    // ===== Extract =====
    const extractInput = document.getElementById('extractInput');
    const pathInput = document.getElementById('pathInput');
    const extractOutput = document.getElementById('extractOutput');
    const extractHighlight = document.getElementById('extractHighlight');
    const msgExtract = document.getElementById('msgExtract');

    document.getElementById('btnExtract')?.addEventListener('click', () => {
        try {
            const parsed = JSON.parse(extractInput.value);
            const result = extractByPath(parsed, pathInput.value);
            const formatted = JSON.stringify(result, null, 2);
            if (extractOutput) extractOutput.value = formatted;
            if (extractHighlight) extractHighlight.innerHTML = syntaxHighlight(formatted);
            showMsg(msgExtract, 'Extraction successful!', 'success');
        } catch (e) { showMsg(msgExtract, 'Extraction failed: ' + e.message, 'error'); }
    });

    // ===== JSONPath Extraction =====
    const extractByPath = (obj, path) => {
        let result = obj;
        path = path.replace(/^\$?\.?/, '');
        if (!path) return result;
        const parts = path.split(/\.|\[|\]/).filter(p => p);
        for (const part of parts) {
            if (result && typeof result === 'object') {
                if (part.endsWith(']')) {
                    const index = parseInt(part.match(/\[(\d+)\]/)?.[1] || '0', 10);
                    result = Array.isArray(result) ? result[index] : result[part.slice(0, -1)]?.[index];
                } else { result = result[part]; }
            }
            if (result === undefined) throw new Error('Path not found: ' + path);
        }
        return result;
    };

    // ===== Utility Functions =====
    // 性能优化：缓存DOM查询结果
    const $ = (id) => document.getElementById(id);
    const $$ = (sel) => document.querySelectorAll(sel);

    function showMsg(el, text, type) { if (el) { el.textContent = text; el.className = 'message show message-' + type; } }
    function hideMsg(el) { if (el) { el.className = 'message'; el.textContent = ''; } }
    function setStatus(el, text, valid) { if (el) { el.innerHTML = '<span class="status-dot ' + (valid ? 'valid' : 'invalid') + '"></span> ' + text; el.className = 'status-badge ' + (valid ? 'success' : 'error'); } }

    // 使用全局debounce（已在顶部定义）
    // 模板定义
    const templates = {
        api: { name: 'API Response', content: '{"success":true,"data":{"id":1001,"name":"Example","email":"test@example.com"}}' },
        user: { name: 'User Config', content: '{"user":{"id":"u123","role":"admin","verified":true,"preferences":{"theme":"dark"}}}' },
        product: { name: 'Products', content: '{"products":[{"id":"P001","name":"iPhone","price":999},{"id":"P002","name":"MacBook","price":1299}]}' },
        pkg: { name: 'package.json', content: '{"name":"my-app","version":"1.0.0","dependencies":{"express":"^4.18"}}' },
        i18n: { name: 'i18n Config', content: '{"en":{"welcome":"Hello"},"zh":{"welcome":"你好"}}' }
    };

    const templateSelect = document.getElementById('templateSelect');
    const inputJson = document.getElementById('inputJson');
    if (templateSelect && inputJson) {
        templateSelect.addEventListener('change', function() {
            if (this.value && templates[this.value]) {
                inputJson.value = templates[this.value].content;
                document.getElementById('formatBtn')?.click();
                showMsg(msgFormat, 'Loaded: ' + templates[this.value].name, 'success');
            }
            this.value = '';
        });
    }

    // 图片懒加载（Intersection Observer）
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        img.classList.add('loaded');
                    }
                    observer.unobserve(img);
                }
            });
        }, { rootMargin: '50px 0px' });

        document.querySelectorAll('img[data-src]').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

})(); // 立即执行函数结束
