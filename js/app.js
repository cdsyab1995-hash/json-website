// ===== AI JSON - Optimized JavaScript =====

document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navbarLinks = document.querySelector('.navbar-links');
    if (menuToggle && navbarLinks) {
        menuToggle.addEventListener('click', () => navbarLinks.classList.toggle('show'));
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => { if (window.innerWidth <= 768) navbarLinks.classList.remove('show'); });
        });
    }

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

    const formatJSON = () => {
        try {
            const formatted = JSON.stringify(JSON.parse(jsonInput.value), null, 2);
            if (jsonOutput) jsonOutput.value = formatted;
            if (jsonHighlight) jsonHighlight.innerHTML = syntaxHighlight(formatted);
            showMsg(msgFormat, 'JSON formatted successfully!', 'success');
            setStatus(statusBadge, 'Valid JSON', true);
        } catch (e) {
            if (jsonOutput) jsonOutput.value = '';
            if (jsonHighlight) jsonHighlight.innerHTML = '';
            showMsg(msgFormat, 'JSON Error: ' + e.message, 'error');
            setStatus(statusBadge, 'Invalid JSON', false);
        }
    };

    const validateJSON = () => {
        try { JSON.parse(jsonInput.value); showMsg(msgFormat, '✓ Valid JSON!', 'success'); setStatus(statusBadge, 'Valid JSON', true); }
        catch (e) { showMsg(msgFormat, '✗ JSON Error: ' + e.message, 'error'); setStatus(statusBadge, 'Invalid JSON', false); }
    };

    const compressJSON = () => {
        try {
            const compressed = JSON.stringify(JSON.parse(jsonInput.value));
            if (jsonOutput) jsonOutput.value = compressed;
            if (jsonHighlight) jsonHighlight.innerHTML = syntaxHighlight(compressed);
            showMsg(msgFormat, 'JSON compressed successfully!', 'success');
        } catch (e) { showMsg(msgFormat, 'Cannot compress: ' + e.message, 'error'); }
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
                this.innerHTML = '✓ Copied';
                setTimeout(() => { this.innerHTML = this.dataset.original || 'Copy'; }, 2000);
            } catch (err) { console.error('Copy failed:', err); }
        }
    });

    // Clear button
    document.getElementById('btnClear')?.addEventListener('click', () => {
        if (jsonInput) jsonInput.value = '';
        if (jsonOutput) jsonOutput.value = '';
        if (jsonHighlight) jsonHighlight.innerHTML = '';
        hideMsg(msgFormat);
        if (statusBadge) statusBadge.innerHTML = '';
    });

    // Real-time preview
    if (jsonInput) {
        jsonInput.addEventListener('input', debounce(() => {
            const input = jsonInput.value;
            if (!input.trim()) { if (jsonHighlight) jsonHighlight.innerHTML = ''; if (statusBadge) statusBadge.innerHTML = ''; return; }
            try {
                if (jsonHighlight) jsonHighlight.innerHTML = syntaxHighlight(JSON.stringify(JSON.parse(input), null, 2));
                setStatus(statusBadge, 'Valid JSON', true);
            } catch (e) {
                if (jsonHighlight) jsonHighlight.innerHTML = '<span style="color: var(--error)">Invalid: ' + e.message + '</span>';
                setStatus(statusBadge, 'Invalid JSON', false);
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
    function showMsg(el, text, type) { if (el) { el.textContent = text; el.className = 'message show message-' + type; } }
    function hideMsg(el) { if (el) { el.className = 'message'; el.textContent = ''; } }
    function setStatus(el, text, valid) { if (el) { el.innerHTML = '<span class="status-dot ' + (valid ? 'valid' : 'invalid') + '"></span> ' + text; el.className = 'status-badge ' + (valid ? 'success' : 'error'); } }
    function debounce(func, wait) { let timeout; return (...args) => { clearTimeout(timeout); timeout = setTimeout(() => func(...args), wait); }; }

    // ===== Templates =====
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
});
