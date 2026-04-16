#!/usr/bin/env python3
"""
创建 P1 工具页面：JWT Decoder, Hash Generator, UUID Generator
"""
import os
import re

BASE_DIR = r'd:\网站开发-json\pages'

# 读取参考页面获取模板
def get_template():
    with open(r'd:\网站开发-json\pages\regex-tester.html', 'r', encoding='utf-8') as f:
        return f.read()

def create_jwt_decoder():
    """创建 JWT Decoder 页面"""
    template = get_template()
    
    content = template.replace(
        'Regex Tester',
        'JWT Decoder'
    ).replace(
        'regex-tester',
        'jwt-decoder'
    ).replace(
        'Regular Expression Tester',
        'JWT Decoder'
    ).replace(
        'Test and debug regular expressions with real-time matching',
        'Decode and inspect JWT tokens with ease'
    ).replace(
        'JSON Web Token decoder and validator for developers',
        'JSON Web Token decoder and validator for developers'
    ).replace(
        '<meta name="keywords" content="regex tester online, regular expression tool',
        '<meta name="keywords" content="jwt decoder online, json web token parser'
    ).replace(
        '<p class="lead">Decode JWT tokens and inspect their header, payload, and signature.</p>',
        '<p class="lead">Decode JWT tokens and inspect their header, payload, and signature.</p>'
    ).replace(
        '''        <div class="tool-container">
            <div class="input-section">
                <div class="section-header">
                    <h2>Input</h2>
                    <div class="section-actions">
                        <button class="btn-icon" onclick="loadSample()" title="Load Sample">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                            </svg>
                            Sample
                        </button>
                        <button class="btn-icon" onclick="clearInput()" title="Clear">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="3 6 5 6 21 6"></polyline>
                                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Clear
                        </button>
                    </div>
                </div>
                <textarea id="regexInput" placeholder="Enter your regular expression here...&#10;&#10;Example: \\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"></textarea>
            </div>

            <div class="output-section">
                <div class="section-header">
                    <h2>Options</h2>
                </div>
                <div class="flags-container">
                    <label class="flag-option">
                        <input type="checkbox" id="flagGlobal" checked>
                        <span class="flag-label">Global (g)</span>
                    </label>
                    <label class="flag-option">
                        <input type="checkbox" id="flagCaseInsensitive">
                        <span class="flag-label">Case Insensitive (i)</span>
                    </label>
                    <label class="flag-option">
                        <input type="checkbox" id="flagMultiline">
                        <span class="flag-label">Multiline (m)</span>
                    </label>
                </div>
                <div class="section-header" style="margin-top: 1.5rem;">
                    <h2>Test String</h2>
                </div>
                <textarea id="testInput" placeholder="Enter text to test against...&#10;&#10;Example: Contact us at support@example.com or sales@company.org"></textarea>
            </div>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Results</h2>
                <div class="match-count" id="matchCount">0 matches found</div>
            </div>
            <div class="results-content" id="resultsContent">
                <div class="no-results">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <p>Enter a regular expression and test string to see matches</p>
                </div>
            </div>
        </div>

        <section class="quick-reference">
            <h2>Quick Reference</h2>
            <div class="reference-grid">
                <div class="reference-card">
                    <h3>Character Classes</h3>
                    <ul>
                        <li><code>.</code> - Any character</li>
                        <li><code>\\d</code> - Digit (0-9)</li>
                        <li><code>\\w</code> - Word character</li>
                        <li><code>\\s</code> - Whitespace</li>
                        <li><code>[abc]</code> - Any of a, b, or c</li>
                        <li><code>[^abc]</code> - Not a, b, or c</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Anchors</h3>
                    <ul>
                        <li><code>^</code> - Start of string</li>
                        <li><code>$</code> - End of string</li>
                        <li><code>\\b</code> - Word boundary</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Quantifiers</h3>
                    <ul>
                        <li><code>*</code> - 0 or more</li>
                        <li><code>+</code> - 1 or more</li>
                        <li><code>?</code> - 0 or 1</li>
                        <li><code>{n}</code> - Exactly n</li>
                        <li><code>{n,}</code> - n or more</li>
                        <li><code>{n,m}</code> - Between n and m</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Groups</h3>
                    <ul>
                        <li><code>(abc)</code> - Capture group</li>
                        <li><code>(?:abc)</code> - Non-capture group</li>
                        <li><code>x|y</code> - Alternation</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="common-patterns">
            <h2>Common Patterns</h2>
            <div class="patterns-grid">''',
        '''        <div class="tool-container">
            <div class="input-section">
                <div class="section-header">
                    <h2>JWT Token</h2>
                    <div class="section-actions">
                        <button class="btn-icon" onclick="loadSample()" title="Load Sample">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                            </svg>
                            Sample
                        </button>
                        <button class="btn-icon" onclick="clearInput()" title="Clear">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="3 6 5 6 21 6"></polyline>
                                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Clear
                        </button>
                    </div>
                </div>
                <textarea id="jwtInput" placeholder="Paste your JWT token here...&#10;&#10;Example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"></textarea>
            </div>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Decoded Token</h2>
                <div class="token-status" id="tokenStatus">
                    <span class="status-badge">Not Decoded</span>
                </div>
            </div>
            <div class="decoded-container" id="decodedContainer">
                <div class="no-results">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                        <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                    </svg>
                    <p>Paste a JWT token to decode it</p>
                </div>
            </div>
        </div>

        <section class="jwt-info">
            <h2>What is JWT?</h2>
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="16" y1="13" x2="8" y2="13"></line>
                            <line x1="16" y1="17" x2="8" y2="17"></line>
                        </svg>
                    </div>
                    <h3>Header</h3>
                    <p>Contains metadata about the token type and algorithm used for signing (e.g., HS256, RS256).</p>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                    </div>
                    <h3>Payload</h3>
                    <p>Contains the claims - user data like user ID, roles, permissions, and expiration time.</p>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        </svg>
                    </div>
                    <h3>Signature</h3>
                    <p>Verifies the token wasn't tampered with. Cannot be decoded - only verified with the secret key.</p>
                </div>
            </div>
        </section>

        <section class="quick-reference">
            <h2>JWT Algorithms</h2>
            <div class="reference-grid">
                <div class="reference-card">
                    <h3>HMAC (Symmetric)</h3>
                    <ul>
                        <li><code>HS256</code> - HMAC using SHA-256</li>
                        <li><code>HS384</code> - HMAC using SHA-384</li>
                        <li><code>HS512</code> - HMAC using SHA-512</li>
                    </ul>
                    <p style="margin-top: 0.5rem; font-size: 0.85rem; color: var(--text-muted);">Uses a shared secret key</p>
                </div>
                <div class="reference-card">
                    <h3>RSA (Asymmetric)</h3>
                    <ul>
                        <li><code>RS256</code> - RSA using SHA-256</li>
                        <li><code>RS384</code> - RSA using SHA-384</li>
                        <li><code>RS512</code> - RSA using SHA-512</li>
                    </ul>
                    <p style="margin-top: 0.5rem; font-size: 0.85rem; color: var(--text-muted);">Uses public/private key pair</p>
                </div>
                <div class="reference-card">
                    <h3>ECDSA</h3>
                    <ul>
                        <li><code>ES256</code> - ECDSA using P-256</li>
                        <li><code>ES384</code> - ECDSA using P-384</li>
                        <li><code>ES512</code> - ECDSA using P-521</li>
                    </ul>
                    <p style="margin-top: 0.5rem; font-size: 0.85rem; color: var(--text-muted);">Elliptic curve algorithm</p>
                </div>
                <div class="reference-card">
                    <h3>None</h3>
                    <ul>
                        <li><code>none</code> - No signature</li>
                    </ul>
                    <p style="margin-top: 0.5rem; font-size: 0.85rem; color: var(--text-muted);">⚠️ Insecure - use with caution</p>
                </div>
            </div>
        </section>'''
    ).replace(
        'common-patterns',
        'jwt-info'
    ).replace(
        '''    <div class="patterns-grid">
                <button class="pattern-btn" data-pattern="\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b" data-desc="Email address">
                    Email
                </button>
                <button class="pattern-btn" data-pattern="https?:\\/\\/[\\w\\-._~:/?#[\\]@!$&'()*+,;=%]+" data-desc="URL">
                    URL
                </button>
                <button class="pattern-btn" data-pattern="\\d{4}[-/]\\d{2}[-/]\\d{2}" data-desc="Date (YYYY-MM-DD or YYYY/MM/DD)">
                    Date
                </button>
                <button class="pattern-btn" data-pattern="\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}" data-desc="IPv4 address">
                    IPv4
                </button>
                <button class="pattern-btn" data-pattern="#[A-Fa-f0-9]{6}" data-desc="Hex color code">
                    Hex Color
                </button>
                <button class="pattern-btn" data-pattern="\\+?[1-9]\\d{1,14}" data-desc="Phone number (E.164)">
                    Phone
                </button>
                <button class="pattern-btn" data-pattern="\\$[\\d,]+\\.\\d{2}" data-desc="USD currency">
                    USD
                </button>
                <button class="pattern-btn" data-pattern="[A-Z]{2}[0-9]{2}[A-Z0-9]{4,30}" data-desc="IBAN">
                    IBAN
                </button>
            </div>
        </section>''',
        '''    <div class="patterns-grid">
                <button class="pattern-btn" data-pattern="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" data-desc="Sample JWT with HS256">
                    Sample JWT
                </button>
                <button class="pattern-btn" data-pattern="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.POstGetfAytaZS82wHcjoGyoCLcBrBzp7YRgJr7jRligtFnnPJ1WEfGEt0g0YVlmGy4RQW15VRLq1Xj8D7XJE8W05YPVTT5JVFm2nMsW8Yl_4U2UVmM8L5xqMqT3LdJib8Kqs3jQWEaF92B36URKQ9wp3F5WY3XwL4Bb6g8jTCg7E9Fqh8S4t6Dv7_5M0R4a8i7F5R1L7G3qJw1N2k7X9B0r3P9V5J8Kq2L4M6N8O2P3Q6R9S2T4U7V9W1X2Y5Z8A1B4C7D2E5F8G3H6I9J2K5L8M1N4O7P2Q5R8S3T6U9V2W5X8Y3Z1A4B7C2D5E8F3G6H9I2J5K8L1M4N7O2P5Q8R3S6T9U2V5W8X3Y6Z1A4B7C2D5E8F3G6H9I2J5K8L1M4N7O2P5Q8R3S6T9U2V5W8X3Y6Z1A4B7C2D5E8F3G6H9I2J5K8L1M4N7O2P5Q8R3S6T9U2V5W8" data-desc="RS256 JWT (public key auth)">
                    RS256 JWT
                </button>
            </div>
        </section>'''
    ).replace(
        '''function loadSample() {
    document.getElementById('regexInput').value = '\\\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\\\.[A-Z|a-z]{2,}\\\\b';
    document.getElementById('testInput').value = 'Contact us at support@example.com or sales@company.org or test@sub.domain.co.uk';
    testRegex();
}''',
        '''function loadSample() {
    document.getElementById('jwtInput').value = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1MTYyMzkwMjIsImV4cCI6MTc0NzI2NzgwMn0.oW8LJ3oZ7kH2X8xqFkNqZp1YwT3rS5vI9mK2xP6nO8w';
    decodeJWT();
}'''
    ).replace(
        '''function testRegex() {
    const pattern = document.getElementById('regexInput').value;
    const testStr = document.getElementById('testInput').value;
    const resultsContent = document.getElementById('resultsContent');
    const matchCount = document.getElementById('matchCount');
    
    if (!pattern || !testStr) {
        resultsContent.innerHTML = '<div class="no-results"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg><p>Enter a regular expression and test string to see matches</p></div>';
        matchCount.textContent = '0 matches found';
        return;
    }
    
    let flags = '';
    if (document.getElementById('flagGlobal').checked) flags += 'g';
    if (document.getElementById('flagCaseInsensitive').checked) flags += 'i';
    if (document.getElementById('flagMultiline').checked) flags += 'm';
    
    try {
        const regex = new RegExp(pattern, flags);
        const matches = testStr.match(regex) || [];
        
        matchCount.textContent = matches.length + ' match' + (matches.length !== 1 ? 'es' : '') + ' found';
        
        if (matches.length === 0) {
            resultsContent.innerHTML = '<div class="no-results"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg><p>No matches found</p></div>';
            return;
        }
        
        let html = '<div class="match-list">';
        matches.forEach((match, index) => {
            const highlighted = testStr.replace(regex, (m) => `<mark class="match-highlight">${m}</mark>`);
            html += '<div class="match-item">';
            html += '<div class="match-number">Match ' + (index + 1) + '</div>';
            html += '<div class="match-value">' + escapeHtml(match) + '</div>';
            html += '<div class="match-position">Position: ' + testStr.indexOf(match) + '-' + (testStr.indexOf(match) + match.length) + '</div>';
            html += '</div>';
        });
        html += '</div>';
        
        html += '<div class="highlighted-preview">';
        html += '<h3>Highlighted Preview</h3>';
        html += '<div class="preview-text">' + highlighted.replace(/\\n/g, '<br>') + '</div>';
        html += '</div>';
        
        resultsContent.innerHTML = html;
    } catch (e) {
        resultsContent.innerHTML = '<div class="error-message"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg><p>Invalid regular expression: ' + escapeHtml(e.message) + '</p></div>';
        matchCount.textContent = 'Error';
    }
}''',
        '''function decodeJWT() {
    const input = document.getElementById('jwtInput').value.trim();
    const container = document.getElementById('decodedContainer');
    const status = document.getElementById('tokenStatus');
    
    if (!input) {
        container.innerHTML = '<div class="no-results"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg><p>Paste a JWT token to decode it</p></div>';
        status.innerHTML = '<span class="status-badge">Not Decoded</span>';
        return;
    }
    
    const parts = input.split('.');
    if (parts.length !== 3) {
        container.innerHTML = '<div class="error-message"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg><p>Invalid JWT format. A JWT has 3 parts separated by dots (header.payload.signature)</p></div>';
        status.innerHTML = '<span class="status-badge error">Invalid Format</span>';
        return;
    }
    
    try {
        const header = JSON.parse(base64UrlDecode(parts[0]));
        const payload = JSON.parse(base64UrlDecode(parts[1]));
        
        // Determine token status
        let statusClass = 'success';
        let statusText = 'Valid';
        if (payload.exp && payload.exp < Date.now() / 1000) {
            statusClass = 'expired';
            statusText = 'Expired';
        } else if (payload.exp) {
            statusText = 'Valid';
        }
        
        status.innerHTML = '<span class="status-badge ' + statusClass + '">' + statusText + '</span>';
        
        let html = '<div class="decoded-parts">';
        
        // Header
        html += '<div class="decoded-section">';
        html += '<div class="decoded-header">';
        html += '<h3>Header</h3>';
        html += '<span class="part-label">JWT Part 1</span>';
        html += '</div>';
        html += '<div class="decoded-content">';
        html += '<div class="token-part raw">' + escapeHtml(parts[0]) + '</div>';
        html += '<div class="parsed-json">' + formatJSON(header) + '</div>';
        html += '</div>';
        html += '</div>';
        
        // Payload
        html += '<div class="decoded-section">';
        html += '<div class="decoded-header">';
        html += '<h3>Payload</h3>';
        html += '<span class="part-label">JWT Part 2</span>';
        html += '</div>';
        html += '<div class="decoded-content">';
        html += '<div class="token-part raw">' + escapeHtml(parts[1]) + '</div>';
        html += '<div class="parsed-json">' + formatPayloadClaims(payload) + '</div>';
        html += '</div>';
        html += '</div>';
        
        // Signature
        html += '<div class="decoded-section">';
        html += '<div class="decoded-header">';
        html += '<h3>Signature</h3>';
        html += '<span class="part-label">JWT Part 3</span>';
        html += '</div>';
        html += '<div class="decoded-content">';
        html += '<div class="token-part signature">' + escapeHtml(parts[2]) + '</div>';
        html += '<p class="signature-note"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>Signature cannot be decoded. To verify, you need the secret key.</p>';
        html += '</div>';
        html += '</div>';
        
        html += '</div>';
        
        container.innerHTML = html;
    } catch (e) {
        container.innerHTML = '<div class="error-message"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg><p>Failed to decode JWT: ' + escapeHtml(e.message) + '</p></div>';
        status.innerHTML = '<span class="status-badge error">Decode Error</span>';
    }
}

function base64UrlDecode(str) {
    // Convert base64url to base64
    str = str.replace(/-/g, '+').replace(/_/g, '/');
    // Pad with = if necessary
    while (str.length % 4) str += '=';
    return atob(str);
}

function formatPayloadClaims(payload) {
    let html = '<div class="claims-list">';
    
    // Standard claims
    const standardClaims = ['iss', 'sub', 'aud', 'exp', 'nbf', 'iat', 'jti'];
    const claimLabels = {
        iss: 'Issuer',
        sub: 'Subject',
        aud: 'Audience',
        exp: 'Expires',
        nbf: 'Not Before',
        iat: 'Issued At',
        jti: 'JWT ID'
    };
    
    for (const claim of standardClaims) {
        if (payload.hasOwnProperty(claim)) {
            let value = payload[claim];
            let displayValue = value;
            
            if (claim === 'exp' || claim === 'iat' || claim === 'nbf') {
                const date = new Date(value * 1000);
                displayValue = value + ' (' + formatDate(date) + ')';
            }
            
            html += '<div class="claim-item">';
            html += '<span class="claim-name">' + claim + '</span>';
            html += '<span class="claim-label">' + claimLabels[claim] + '</span>';
            html += '<span class="claim-value">' + displayValue + '</span>';
            html += '</div>';
        }
    }
    
    // Other claims
    for (const key of Object.keys(payload)) {
        if (!standardClaims.includes(key)) {
            html += '<div class="claim-item custom">';
            html += '<span class="claim-name">' + key + '</span>';
            html += '<span class="claim-value">' + escapeHtml(JSON.stringify(payload[key])) + '</span>';
            html += '</div>';
        }
    }
    
    html += '</div>';
    return html;
}

function formatDate(date) {
    return date.toLocaleString();
}'''
    ).replace(
        'function escapeHtml(',
        '''function escapeHtml('''
    ).replace(
        '''document.getElementById(\'regexInput\').addEventListener(\'input\', testRegex);
document.getElementById(\'testInput\').addEventListener(\'input\', testRegex);
document.getElementById(\'flagGlobal\').addEventListener(\'change\', testRegex);
document.getElementById(\'flagCaseInsensitive\').addEventListener(\'change\', testRegex);
document.getElementById(\'flagMultiline\').addEventListener(\'change\', testRegex);

document.querySelectorAll(\\.pattern-btn\\).forEach(btn => {
    btn.addEventListener(\\'click\\', () => {
        document.getElementById(\\'regexInput\\').value = btn.dataset.pattern;
        testRegex();
    });
});''',
        '''document.getElementById('jwtInput').addEventListener('input', decodeJWT);

document.querySelectorAll('.pattern-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.getElementById('jwtInput').value = btn.dataset.pattern;
        decodeJWT();
    });
});'''
    ).replace(
        '''document.getElementById('regexInput').addEventListener('input', testRegex);
document.getElementById('testInput').addEventListener('input', testRegex);
document.getElementById('flagGlobal').addEventListener('change', testRegex);
document.getElementById('flagCaseInsensitive').addEventListener('change', testRegex);
document.getElementById('flagMultiline').addEventListener('change', testRegex);''',
        '''document.getElementById('jwtInput').addEventListener('input', decodeJWT);'''
    )
    
    # 修改CSS
    content = content.replace(
        '''.tool-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
}''',
        '''.tool-container {
    margin-bottom: 2rem;
}'''
    ).replace(
        '''.flags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.flag-option {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--bg-secondary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
}

.flag-option:hover {
    background: var(--bg-tertiary);
}

.flag-option input {
    width: 18px;
    height: 18px;
    cursor: pointer;
}

.flag-label {
    font-family: var(--font-mono);
    font-size: 0.9rem;
}''',
        '''.decoded-section {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.decoded-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--border-color);
}

.decoded-header h3 {
    margin: 0;
    font-size: 1.1rem;
}

.part-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    background: var(--bg-tertiary);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
}

.decoded-content {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.token-part {
    padding: 1rem;
    border-radius: 8px;
    font-family: var(--font-mono);
    font-size: 0.85rem;
    word-break: break-all;
    line-height: 1.6;
}

.token-part.raw {
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
}

.token-part.signature {
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.3);
}

.signature-note {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    color: var(--text-muted);
    margin: 0;
}

.signature-note svg {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
}

.claims-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.claim-item {
    display: grid;
    grid-template-columns: 80px 1fr auto;
    gap: 1rem;
    padding: 0.75rem;
    background: var(--bg-tertiary);
    border-radius: 6px;
    align-items: center;
}

.claim-item.custom {
    grid-template-columns: 1fr auto;
    background: var(--bg-primary);
    border: 1px dashed var(--border-color);
}

.claim-name {
    font-family: var(--font-mono);
    font-weight: 600;
    color: var(--primary);
}

.claim-label {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.claim-value {
    font-family: var(--font-mono);
    font-size: 0.9rem;
    text-align: right;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.35rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}

.status-badge.success {
    background: rgba(34, 197, 94, 0.15);
    color: #22c55e;
}

.status-badge.error,
.status-badge.expired {
    background: rgba(239, 68, 68, 0.15);
    color: #ef4444;
}

.status-badge {
    background: var(--bg-tertiary);
    color: var(--text-muted);
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.info-card {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.5rem;
}

.info-icon {
    width: 48px;
    height: 48px;
    background: var(--primary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
}

.info-icon svg {
    width: 24px;
    height: 24px;
    color: white;
}

.info-card h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}

.info-card p {
    margin: 0;
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
}'''
    ).replace(
        '.highlighted-preview {',
        '''.decoded-container .no-results {
    text-align: center;
    padding: 4rem 2rem;
}

.decoded-container .no-results svg {
    width: 64px;
    height: 64px;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.decoded-container .no-results p {
    color: var(--text-muted);
    font-size: 1rem;
}

.highlighted-preview {'''
    ).replace(
        'font-size: 1.25rem;',
        'font-size: 1.25rem; margin-top: 1.5rem;'
    )
    
    output_path = os.path.join(BASE_DIR, 'jwt-decoder.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[OK] jwt-decoder.html created')
    return True

def create_hash_generator():
    """创建 Hash Generator 页面"""
    template = get_template()
    
    content = template.replace(
        'Regex Tester',
        'Hash Generator'
    ).replace(
        'regex-tester',
        'hash-generator'
    ).replace(
        'Regular Expression Tester',
        'Hash Generator'
    ).replace(
        'Test and debug regular expressions with real-time matching',
        'Generate MD5, SHA-1, SHA-256, SHA-512 hashes instantly'
    ).replace(
        'JSON Web Token decoder and validator for developers',
        'Generate cryptographic hashes from any text or file'
    ).replace(
        '<meta name="keywords" content="regex tester online, regular expression tool',
        '<meta name="keywords" content="hash generator online, md5 generator, sha256 hash'
    ).replace(
        '''        <div class="tool-container">
            <div class="input-section">
                <div class="section-header">
                    <h2>Input</h2>
                    <div class="section-actions">
                        <button class="btn-icon" onclick="loadSample()" title="Load Sample">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                            </svg>
                            Sample
                        </button>
                        <button class="btn-icon" onclick="clearInput()" title="Clear">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="3 6 5 6 21 6"></polyline>
                                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Clear
                        </button>
                    </div>
                </div>
                <textarea id="regexInput" placeholder="Enter your regular expression here...&#10;&#10;Example: \\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"></textarea>
            </div>

            <div class="output-section">
                <div class="section-header">
                    <h2>Options</h2>
                </div>
                <div class="flags-container">
                    <label class="flag-option">
                        <input type="checkbox" id="flagGlobal" checked>
                        <span class="flag-label">Global (g)</span>
                    </label>
                    <label class="flag-option">
                        <input type="checkbox" id="flagCaseInsensitive">
                        <span class="flag-label">Case Insensitive (i)</span>
                    </label>
                    <label class="flag-option">
                        <input type="checkbox" id="flagMultiline">
                        <span class="flag-label">Multiline (m)</span>
                    </label>
                </div>
                <div class="section-header" style="margin-top: 1.5rem;">
                    <h2>Test String</h2>
                </div>
                <textarea id="testInput" placeholder="Enter text to test against...&#10;&#10;Example: Contact us at support@example.com or sales@company.org"></textarea>
            </div>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Results</h2>
                <div class="match-count" id="matchCount">0 matches found</div>
            </div>
            <div class="results-content" id="resultsContent">
                <div class="no-results">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <p>Enter a regular expression and test string to see matches</p>
                </div>
            </div>
        </div>

        <section class="quick-reference">
            <h2>Quick Reference</h2>
            <div class="reference-grid">
                <div class="reference-card">
                    <h3>Character Classes</h3>
                    <ul>
                        <li><code>.</code> - Any character</li>
                        <li><code>\\d</code> - Digit (0-9)</li>
                        <li><code>\\w</code> - Word character</li>
                        <li><code>\\s</code> - Whitespace</li>
                        <li><code>[abc]</code> - Any of a, b, or c</li>
                        <li><code>[^abc]</code> - Not a, b, or c</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Anchors</h3>
                    <ul>
                        <li><code>^</code> - Start of string</li>
                        <li><code>$</code> - End of string</li>
                        <li><code>\\b</code> - Word boundary</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Quantifiers</h3>
                    <ul>
                        <li><code>*</code> - 0 or more</li>
                        <li><code>+</code> - 1 or more</li>
                        <li><code>?</code> - 0 or 1</li>
                        <li><code>{n}</code> - Exactly n</li>
                        <li><code>{n,}</code> - n or more</li>
                        <li><code>{n,m}</code> - Between n and m</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Groups</h3>
                    <ul>
                        <li><code>(abc)</code> - Capture group</li>
                        <li><code>(?:abc)</code> - Non-capture group</li>
                        <li><code>x|y</code> - Alternation</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="common-patterns">
            <h2>Common Patterns</h2>
            <div class="patterns-grid">''',
        '''        <div class="tool-container">
            <div class="input-section">
                <div class="section-header">
                    <h2>Input</h2>
                    <div class="section-actions">
                        <button class="btn-icon" onclick="loadSample()" title="Load Sample">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                            </svg>
                            Sample
                        </button>
                        <button class="btn-icon" onclick="clearInput()" title="Clear">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="3 6 5 6 21 6"></polyline>
                                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Clear
                        </button>
                    </div>
                </div>
                <textarea id="hashInput" placeholder="Enter text to hash...&#10;&#10;Example: Hello, World!"></textarea>
            </div>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Hash Output</h2>
                <div class="hash-length" id="hashLength">Enter text to generate hashes</div>
            </div>
            <div class="results-content" id="resultsContent">
                <div class="no-results">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="4" y1="9" x2="20" y2="9"></line>
                        <line x1="4" y1="15" x2="20" y2="15"></line>
                        <line x1="10" y1="3" x2="8" y2="21"></line>
                        <line x1="16" y1="3" x2="14" y2="21"></line>
                    </svg>
                    <p>Enter text to generate cryptographic hashes</p>
                </div>
            </div>
        </div>

        <section class="hash-info">
            <h2>Hash Algorithms Explained</h2>
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>
                    </div>
                    <h3>MD5</h3>
                    <p>128-bit hash. Fast but insecure for security purposes. Good for checksums but not passwords.</p>
                    <span class="info-badge warning">Not Recommended for Security</span>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        </svg>
                    </div>
                    <h3>SHA-1</h3>
                    <p>160-bit hash. Deprecated for security use. Still used in some legacy systems and git.</p>
                    <span class="info-badge warning">Deprecated</span>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        </svg>
                    </div>
                    <h3>SHA-256</h3>
                    <p>256-bit hash. Industry standard for secure applications. Used in TLS, cryptocurrencies, and more.</p>
                    <span class="info-badge success">Recommended</span>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        </svg>
                    </div>
                    <h3>SHA-512</h3>
                    <p>512-bit hash. Stronger than SHA-256 with larger output. Good for sensitive applications.</p>
                    <span class="info-badge success">Recommended</span>
                </div>
            </div>
        </section>

        <section class="quick-reference">
            <h2>Use Cases</h2>
            <div class="reference-grid">
                <div class="reference-card">
                    <h3>Password Storage</h3>
                    <p>Never store plain text passwords. Hash them with bcrypt, scrypt, or Argon2 before storing.</p>
                    <span class="use-case-badge">Security</span>
                </div>
                <div class="reference-card">
                    <h3>File Integrity</h3>
                    <p>Verify downloads by comparing hash values. Many software sites publish MD5/SHA-256 checksums.</p>
                    <span class="use-case-badge">Checksums</span>
                </div>
                <div class="reference-card">
                    <h3>Digital Signatures</h3>
                    <p>Hash functions are fundamental to digital signatures and certificate verification.</p>
                    <span class="use-case-badge">Cryptography</span>
                </div>
                <div class="reference-card">
                    <h3>Blockchain</h3>
                    <p>Cryptocurrencies like Bitcoin use SHA-256 for transaction verification and mining.</p>
                    <span class="use-case-badge">Blockchain</span>
                </div>
            </div>
        </section>'''
    ).replace(
        'common-patterns',
        'hash-info'
    ).replace(
        '''    <div class="patterns-grid">
                <button class="pattern-btn" data-pattern="\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b" data-desc="Email address">
                    Email
                </button>
                <button class="pattern-btn" data-pattern="https?:\\/\\/[\\w\\-._~:/?#[\\]@!$&'()*+,;=%]+" data-desc="URL">
                    URL
                </button>
                <button class="pattern-btn" data-pattern="\\d{4}[-/]\\d{2}[-/]\\d{2}" data-desc="Date (YYYY-MM-DD or YYYY/MM/DD)">
                    Date
                </button>
                <button class="pattern-btn" data-pattern="\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}" data-desc="IPv4 address">
                    IPv4
                </button>
                <button class="pattern-btn" data-pattern="#[A-Fa-f0-9]{6}" data-desc="Hex color code">
                    Hex Color
                </button>
                <button class="pattern-btn" data-pattern="\\+?[1-9]\\d{1,14}" data-desc="Phone number (E.164)">
                    Phone
                </button>
                <button class="pattern-btn" data-pattern="\\$[\\d,]+\\.\\d{2}" data-desc="USD currency">
                    USD
                </button>
                <button class="pattern-btn" data-pattern="[A-Z]{2}[0-9]{2}[A-Z0-9]{4,30}" data-desc="IBAN">
                    IBAN
                </button>
            </div>
        </section>''',
        '''    <div class="patterns-grid">
                <button class="pattern-btn" data-pattern="Hello, World!" data-desc="Classic example">
                    Hello World
                </button>
                <button class="pattern-btn" data-pattern="The quick brown fox jumps over the lazy dog" data-desc="Standard test phrase">
                    Quick Brown Fox
                </button>
                <button class="pattern-btn" data-pattern="password123" data-desc="Example password">
                    Password
                </button>
                <button class="pattern-btn" data-pattern="admin@aijsons.com" data-desc="Email example">
                    Email
                </button>
            </div>
        </section>'''
    ).replace(
        '''function loadSample() {
    document.getElementById('regexInput').value = '\\\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\\\.[A-Z|a-z]{2,}\\\\b';
    document.getElementById('testInput').value = 'Contact us at support@example.com or sales@company.org or test@sub.domain.co.uk';
    testRegex();
}''',
        '''function loadSample() {
    document.getElementById('hashInput').value = 'Hello, World!';
    generateHashes();
}'''
    ).replace(
        '''function testRegex() {
    const pattern = document.getElementById('regexInput').value;
    const testStr = document.getElementById('testInput').value;
    const resultsContent = document.getElementById('resultsContent');
    const matchCount = document.getElementById('matchCount');
    
    if (!pattern || !testStr) {
        resultsContent.innerHTML = '<div class="no-results"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg><p>Enter a regular expression and test string to see matches</p></div>';
        matchCount.textContent = '0 matches found';
        return;
    }
    
    let flags = '';
    if (document.getElementById('flagGlobal').checked) flags += 'g';
    if (document.getElementById('flagCaseInsensitive').checked) flags += 'i';
    if (document.getElementById('flagMultiline').checked) flags += 'm';
    
    try {
        const regex = new RegExp(pattern, flags);
        const matches = testStr.match(regex) || [];
        
        matchCount.textContent = matches.length + ' match' + (matches.length !== 1 ? 'es' : '') + ' found';
        
        if (matches.length === 0) {
            resultsContent.innerHTML = '<div class="no-results"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg><p>No matches found</p></div>';
            return;
        }
        
        let html = '<div class="match-list">';
        matches.forEach((match, index) => {
            const highlighted = testStr.replace(regex, (m) => `<mark class="match-highlight">${m}</mark>`);
            html += '<div class="match-item">';
            html += '<div class="match-number">Match ' + (index + 1) + '</div>';
            html += '<div class="match-value">' + escapeHtml(match) + '</div>';
            html += '<div class="match-position">Position: ' + testStr.indexOf(match) + '-' + (testStr.indexOf(match) + match.length) + '</div>';
            html += '</div>';
        });
        html += '</div>';
        
        html += '<div class="highlighted-preview">';
        html += '<h3>Highlighted Preview</h3>';
        html += '<div class="preview-text">' + highlighted.replace(/\\n/g, '<br>') + '</div>';
        html += '</div>';
        
        resultsContent.innerHTML = html;
    } catch (e) {
        resultsContent.innerHTML = '<div class="error-message"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg><p>Invalid regular expression: ' + escapeHtml(e.message) + '</p></div>';
        matchCount.textContent = 'Error';
    }
}''',
        '''async function generateHashes() {
    const input = document.getElementById('hashInput').value;
    const resultsContent = document.getElementById('resultsContent');
    const hashLength = document.getElementById('hashLength');
    
    if (!input) {
        resultsContent.innerHTML = '<div class="no-results"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg><p>Enter text to generate cryptographic hashes</p></div>';
        hashLength.textContent = 'Enter text to generate hashes';
        return;
    }
    
    const encoder = new TextEncoder();
    const data = encoder.encode(input);
    
    // Generate all hashes
    const [md5, sha1, sha256, sha512] = await Promise.all([
        generateMD5(input),
        crypto.subtle.digest('SHA-1', data),
        crypto.subtle.digest('SHA-256', data),
        crypto.subtle.digest('SHA-512', data)
    ]);
    
    const sha1Hex = Array.from(new Uint8Array(sha1)).map(b => b.toString(16).padStart(2, '0')).join('');
    const sha256Hex = Array.from(new Uint8Array(sha256)).map(b => b.toString(16).padStart(2, '0')).join('');
    const sha512Hex = Array.from(new Uint8Array(sha512)).map(b => b.toString(16).padStart(2, '0')).join('');
    
    hashLength.textContent = '4 algorithms generated';
    
    let html = '<div class="hash-list">';
    
    // MD5
    html += '<div class="hash-item">';
    html += '<div class="hash-header">';
    html += '<span class="hash-name">MD5</span>';
    html += '<span class="hash-bits">128-bit</span>';
    html += '</div>';
    html += '<div class="hash-value" id="md5Hash">' + md5 + '</div>';
    html += '<button class="copy-btn" onclick="copyHash(\\'md5Hash\\')">Copy</button>';
    html += '</div>';
    
    // SHA-1
    html += '<div class="hash-item">';
    html += '<div class="hash-header">';
    html += '<span class="hash-name">SHA-1</span>';
    html += '<span class="hash-bits">160-bit</span>';
    html += '</div>';
    html += '<div class="hash-value" id="sha1Hash">' + sha1Hex + '</div>';
    html += '<button class="copy-btn" onclick="copyHash(\\'sha1Hash\\')">Copy</button>';
    html += '</div>';
    
    // SHA-256
    html += '<div class="hash-item highlight">';
    html += '<div class="hash-header">';
    html += '<span class="hash-name">SHA-256</span>';
    html += '<span class="hash-bits recommended">Recommended</span>';
    html += '</div>';
    html += '<div class="hash-value" id="sha256Hash">' + sha256Hex + '</div>';
    html += '<button class="copy-btn" onclick="copyHash(\\'sha256Hash\\')">Copy</button>';
    html += '</div>';
    
    // SHA-512
    html += '<div class="hash-item">';
    html += '<div class="hash-header">';
    html += '<span class="hash-name">SHA-512</span>';
    html += '<span class="hash-bits">512-bit</span>';
    html += '</div>';
    html += '<div class="hash-value" id="sha512Hash">' + sha512Hex + '</div>';
    html += '<button class="copy-btn" onclick="copyHash(\\'sha512Hash\\')">Copy</button>';
    html += '</div>';
    
    html += '</div>';
    
    // Input info
    html += '<div class="hash-info-panel">';
    html += '<h3>Input Summary</h3>';
    html += '<div class="info-row"><span>Characters:</span><span>' + input.length + '</span></div>';
    html += '<div class="info-row"><span>Bytes:</span><span>' + data.byteLength + '</span></div>';
    html += '<div class="info-row"><span>Type:</span><span>Text</span></div>';
    html += '</div>';
    
    resultsContent.innerHTML = html;
}

async function generateMD5(input) {
    // MD5 implementation using Web Crypto API workaround
    // Using a simple MD5 implementation since Web Crypto doesn't support it
    return md5String(input);
}

function md5String(str) {
    function md5cycle(x, k) {
        let a = x[0], b = x[1], c = x[2], d = x[3];
        a = ff(a, b, c, d, k[0], 7, -680876936);
        d = ff(d, a, b, c, k[1], 12, -389564586);
        c = ff(c, d, a, b, k[2], 17, 606105819);
        b = ff(b, c, d, a, k[3], 22, -1044525330);
        a = ff(a, b, c, d, k[4], 7, -176418897);
        d = ff(d, a, b, c, k[5], 12, 1200080426);
        c = ff(c, d, a, b, k[6], 17, -1473231341);
        b = ff(b, c, d, a, k[7], 22, -45705983);
        a = ff(a, b, c, d, k[8], 7, 1770035416);
        d = ff(d, a, b, c, k[9], 12, -1958414417);
        c = ff(c, d, a, b, k[10], 17, -42063);
        b = ff(b, c, d, a, k[11], 22, -1990404162);
        a = ff(a, b, c, d, k[12], 7, 1804603682);
        d = ff(d, a, b, c, k[13], 12, -40341101);
        c = ff(c, d, a, b, k[14], 17, -1502002290);
        b = ff(b, c, d, a, k[15], 22, 1236535329);
        a = gg(a, b, c, d, k[1], 5, -165796510);
        d = gg(d, a, b, c, k[6], 9, -1069501632);
        c = gg(c, d, a, b, k[11], 14, 643717713);
        b = gg(b, c, d, a, k[0], 20, -373897302);
        a = gg(a, b, c, d, k[5], 5, -701558691);
        d = gg(d, a, b, c, k[10], 9, 38016083);
        c = gg(c, d, a, b, k[15], 14, -660478335);
        b = gg(b, c, d, a, k[4], 20, -405537848);
        a = gg(a, b, c, d, k[9], 5, 568446438);
        d = gg(d, a, b, c, k[14], 9, -1019803690);
        c = gg(c, d, a, b, k[3], 14, -187363961);
        b = gg(b, c, d, a, k[8], 20, 1163531501);
        a = gg(a, b, c, d, k[13], 5, -1444681467);
        d = gg(d, a, b, c, k[2], 9, -51403784);
        c = gg(c, d, a, b, k[7], 14, 1735328473);
        b = gg(b, c, d, a, k[12], 20, -1926607734);
        a = hh(a, b, c, d, k[5], 4, -378558);
        d = hh(d, a, b, c, k[8], 11, -2022574463);
        c = hh(c, d, a, b, k[11], 16, 1839030562);
        b = hh(b, c, d, a, k[14], 23, -35309556);
        a = hh(a, b, c, d, k[1], 4, -1530992060);
        d = hh(d, a, b, c, k[4], 11, 1272893353);
        c = hh(c, d, a, b, k[7], 16, -155497632);
        b = hh(b, c, d, a, k[10], 23, -1094730640);
        a = hh(a, b, c, d, k[13], 4, 681279174);
        d = hh(d, a, b, c, k[0], 11, -358537222);
        c = hh(c, d, a, b, k[3], 16, -722521979);
        b = hh(b, c, d, a, k[6], 23, 76029189);
        a = hh(a, b, c, d, k[9], 4, -640364487);
        d = hh(d, a, b, c, k[12], 11, -421815835);
        c = hh(c, d, a, b, k[15], 16, 530742520);
        b = hh(b, c, d, a, k[2], 23, -995338651);
        a = ii(a, b, c, d, k[0], 6, -198630844);
        d = ii(d, a, b, c, k[7], 10, 1126891415);
        c = ii(c, d, a, b, k[14], 15, -1416354905);
        b = ii(b, c, d, a, k[5], 21, -57434055);
        a = ii(a, b, c, d, k[12], 6, 1700485571);
        d = ii(d, a, b, c, k[3], 10, -1894986606);
        c = ii(c, d, a, b, k[10], 15, -1051523);
        b = ii(b, c, d, a, k[1], 21, -2054922799);
        a = ii(a, b, c, d, k[8], 6, 1873313359);
        d = ii(d, a, b, c, k[15], 10, -30611744);
        c = ii(c, d, a, b, k[6], 15, -1560198380);
        b = ii(b, c, d, a, k[13], 21, 1309151649);
        a = ii(a, b, c, d, k[4], 6, -145523070);
        d = ii(d, a, b, c, k[11], 10, -1120210379);
        c = ii(c, d, a, b, k[2], 15, 718787259);
        b = ii(b, c, d, a, k[9], 21, -343485551);
        x[0] = add32(a, x[0]);
        x[1] = add32(b, x[1]);
        x[2] = add32(c, x[2]);
        x[3] = add32(d, x[3]);
    }
    
    function cmn(q, a, b, x, s, t) {
        a = add32(add32(a, q), add32(x, t));
        return add32((a << s) | (a >>> (32 - s)), b);
    }
    
    function ff(a, b, c, d, x, s, t) {
        return cmn((b & c) | ((~b) & d), a, b, x, s, t);
    }
    
    function gg(a, b, c, d, x, s, t) {
        return cmn((b & d) | (c & (~d)), a, b, x, s, t);
    }
    
    function hh(a, b, c, d, x, s, t) {
        return cmn(b ^ c ^ d, a, b, x, s, t);
    }
    
    function ii(a, b, c, d, x, s, t) {
        return cmn(c ^ (b | (~d)), a, b, x, s, t);
    }
    
    function md51(s) {
        let n = s.length, state = [1732584193, -271733879, -1732584194, 271733878], i;
        for (i = 64; i <= n; i += 64) {
            md5cycle(state, md5blk(s.substring(i - 64, i)));
        }
        s = s.substring(i - 64);
        let tail = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
        for (i = 0; i < s.length; i++)
            tail[i >> 2] |= s.charCodeAt(i) << ((i % 4) << 3);
        tail[i >> 2] |= 0x80 << ((i % 4) << 3);
        if (i > 55) {
            md5cycle(state, tail);
            for (i = 0; i < 16; i++) tail[i] = 0;
        }
        tail[14] = n * 8;
        md5cycle(state, tail);
        return state;
    }
    
    function md5blk(s) {
        let md5blks = [], i;
        for (i = 0; i < 64; i += 4) {
            md5blks[i >> 2] = s.charCodeAt(i) + (s.charCodeAt(i + 1) << 8) + (s.charCodeAt(i + 2) << 16) + (s.charCodeAt(i + 3) << 24);
        }
        return md5blks;
    }
    
    let hex_chr = '0123456789abcdef'.split('');
    function rhex(n) {
        let s = '', j = 0;
        for (; j < 4; j++)
            s += hex_chr[(n >> (j * 8 + 4)) & 0x0F] + hex_chr[(n >> (j * 8)) & 0x0F];
        return s;
    }
    
    function hex(x) {
        for (let i = 0; i < x.length; i++)
            x[i] = rhex(x[i]);
        return x.join('');
    }
    
    function add32(a, b) {
        return (a + b) & 0xFFFFFFFF;
    }
    
    return hex(md51(str));
}

function copyHash(hashId) {
    const hashValue = document.getElementById(hashId).textContent;
    navigator.clipboard.writeText(hashValue).then(() => {
        const btn = document.querySelector(`#${hashId}`).nextElementSibling;
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => {
            btn.textContent = originalText;
            btn.classList.remove('copied');
        }, 1500);
    });
}'''
    ).replace(
        '''document.getElementById('regexInput').addEventListener('input', testRegex);
document.getElementById('testInput').addEventListener('input', testRegex);
document.getElementById('flagGlobal').addEventListener('change', testRegex);
document.getElementById('flagCaseInsensitive').addEventListener('change', testRegex);
document.getElementById('flagMultiline').addEventListener('change', testRegex);

document.querySelectorAll(\\.pattern-btn\\).forEach(btn => {
    btn.addEventListener(\\'click\\', () => {
        document.getElementById(\\'regexInput\\').value = btn.dataset.pattern;
        testRegex();
    });
});''',
        '''document.getElementById('hashInput').addEventListener('input', generateHashes);

document.querySelectorAll('.pattern-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.getElementById('hashInput').value = btn.dataset.pattern;
        generateHashes();
    });
});'''
    ).replace(
        '''document.getElementById('regexInput').addEventListener('input', testRegex);
document.getElementById('testInput').addEventListener('input', testRegex);
document.getElementById('flagGlobal').addEventListener('change', testRegex);
document.getElementById('flagCaseInsensitive').addEventListener('change', testRegex);
document.getElementById('flagMultiline').addEventListener('change', testRegex);''',
        '''document.getElementById('hashInput').addEventListener('input', generateHashes);'''
    )
    
    # 修改CSS
    content = content.replace(
        '''.tool-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
}''',
        '''.tool-container {
    margin-bottom: 2rem;
}'''
    ).replace(
        '''.flags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.flag-option {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--bg-secondary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
}

.flag-option:hover {
    background: var(--bg-tertiary);
}

.flag-option input {
    width: 18px;
    height: 18px;
    cursor: pointer;
}

.flag-label {
    font-family: var(--font-mono);
    font-size: 0.9rem;
}''',
        '''.hash-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.hash-item {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.25rem;
    border: 1px solid var(--border-color);
    transition: all 0.2s;
}

.hash-item:hover {
    border-color: var(--primary);
}

.hash-item.highlight {
    border-color: var(--primary);
    background: rgba(99, 102, 241, 0.05);
}

.hash-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
}

.hash-name {
    font-weight: 600;
    font-size: 1rem;
}

.hash-bits {
    font-size: 0.8rem;
    color: var(--text-muted);
    background: var(--bg-tertiary);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
}

.hash-bits.recommended {
    background: rgba(34, 197, 94, 0.15);
    color: #22c55e;
}

.hash-value {
    font-family: var(--font-mono);
    font-size: 0.85rem;
    word-break: break-all;
    line-height: 1.6;
    padding: 0.75rem;
    background: var(--bg-tertiary);
    border-radius: 6px;
    margin-bottom: 0.75rem;
}

.copy-btn {
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.85rem;
    transition: all 0.2s;
}

.copy-btn:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}

.copy-btn.copied {
    background: #22c55e;
    color: white;
    border-color: #22c55e;
}

.hash-info-panel {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.25rem;
    margin-top: 1.5rem;
}

.hash-info-panel h3 {
    margin: 0 0 1rem 0;
    font-size: 1rem;
}

.info-row {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--border-color);
    font-size: 0.9rem;
}

.info-row:last-child {
    border-bottom: none;
}

.info-row span:first-child {
    color: var(--text-muted);
}

.info-row span:last-child {
    font-family: var(--font-mono);
}

.info-badge {
    display: inline-block;
    font-size: 0.75rem;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    margin-top: 0.5rem;
}

.info-badge.success {
    background: rgba(34, 197, 94, 0.15);
    color: #22c55e;
}

.info-badge.warning {
    background: rgba(234, 179, 8, 0.15);
    color: #eab308;
}

.use-case-badge {
    display: inline-block;
    font-size: 0.75rem;
    background: var(--bg-tertiary);
    color: var(--text-muted);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    margin-top: 0.5rem;
}'''
    ).replace(
        '''.results-content .no-results {
    text-align: center;
    padding: 4rem 2rem;
}

.results-content .no-results svg {
    width: 64px;
    height: 64px;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.results-content .no-results p {
    color: var(--text-muted);
    font-size: 1rem;
}''',
        '''.results-content .no-results {
    text-align: center;
    padding: 4rem 2rem;
}

.results-content .no-results svg {
    width: 64px;
    height: 64px;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.results-content .no-results p {
    color: var(--text-muted);
    font-size: 1rem;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.info-card {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.5rem;
}

.info-icon {
    width: 48px;
    height: 48px;
    background: var(--primary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
}

.info-icon svg {
    width: 24px;
    height: 24px;
    color: white;
}

.info-card h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}

.info-card p {
    margin: 0;
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
}'''
    )
    
    output_path = os.path.join(BASE_DIR, 'hash-generator.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[OK] hash-generator.html created')
    return True

def create_uuid_generator():
    """创建 UUID Generator 页面"""
    template = get_template()
    
    content = template.replace(
        'Regex Tester',
        'UUID Generator'
    ).replace(
        'regex-tester',
        'uuid-generator'
    ).replace(
        'Regular Expression Tester',
        'UUID Generator'
    ).replace(
        'Test and debug regular expressions with real-time matching',
        'Generate UUIDs (GUIDs) with one click'
    ).replace(
        'JSON Web Token decoder and validator for developers',
        'Universal Unique Identifier generator for developers'
    ).replace(
        '<meta name="keywords" content="regex tester online, regular expression tool',
        '<meta name="keywords" content="uuid generator online, guid generator, unique id'
    ).replace(
        '''        <div class="tool-container">
            <div class="input-section">
                <div class="section-header">
                    <h2>Input</h2>
                    <div class="section-actions">
                        <button class="btn-icon" onclick="loadSample()" title="Load Sample">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                            </svg>
                            Sample
                        </button>
                        <button class="btn-icon" onclick="clearInput()" title="Clear">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="3 6 5 6 21 6"></polyline>
                                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Clear
                        </button>
                    </div>
                </div>
                <textarea id="regexInput" placeholder="Enter your regular expression here...&#10;&#10;Example: \\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"></textarea>
            </div>

            <div class="output-section">
                <div class="section-header">
                    <h2>Options</h2>
                </div>
                <div class="flags-container">
                    <label class="flag-option">
                        <input type="checkbox" id="flagGlobal" checked>
                        <span class="flag-label">Global (g)</span>
                    </label>
                    <label class="flag-option">
                        <input type="checkbox" id="flagCaseInsensitive">
                        <span class="flag-label">Case Insensitive (i)</span>
                    </label>
                    <label class="flag-option">
                        <input type="checkbox" id="flagMultiline">
                        <span class="flag-label">Multiline (m)</span>
                    </label>
                </div>
                <div class="section-header" style="margin-top: 1.5rem;">
                    <h2>Test String</h2>
                </div>
                <textarea id="testInput" placeholder="Enter text to test against...&#10;&#10;Example: Contact us at support@example.com or sales@company.org"></textarea>
            </div>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Results</h2>
                <div class="match-count" id="matchCount">0 matches found</div>
            </div>
            <div class="results-content" id="resultsContent">
                <div class="no-results">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <p>Enter a regular expression and test string to see matches</p>
                </div>
            </div>
        </div>

        <section class="quick-reference">
            <h2>Quick Reference</h2>
            <div class="reference-grid">
                <div class="reference-card">
                    <h3>Character Classes</h3>
                    <ul>
                        <li><code>.</code> - Any character</li>
                        <li><code>\\d</code> - Digit (0-9)</li>
                        <li><code>\\w</code> - Word character</li>
                        <li><code>\\s</code> - Whitespace</li>
                        <li><code>[abc]</code> - Any of a, b, or c</li>
                        <li><code>[^abc]</code> - Not a, b, or c</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Anchors</h3>
                    <ul>
                        <li><code>^</code> - Start of string</li>
                        <li><code>$</code> - End of string</li>
                        <li><code>\\b</code> - Word boundary</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Quantifiers</h3>
                    <ul>
                        <li><code>*</code> - 0 or more</li>
                        <li><code>+</code> - 1 or more</li>
                        <li><code>?</code> - 0 or 1</li>
                        <li><code>{n}</code> - Exactly n</li>
                        <li><code>{n,}</code> - n or more</li>
                        <li><code>{n,m}</code> - Between n and m</li>
                    </ul>
                </div>
                <div class="reference-card">
                    <h3>Groups</h3>
                    <ul>
                        <li><code>(abc)</code> - Capture group</li>
                        <li><code>(?:abc)</code> - Non-capture group</li>
                        <li><code>x|y</code> - Alternation</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="common-patterns">
            <h2>Common Patterns</h2>
            <div class="patterns-grid">''',
        '''        <div class="tool-container">
            <div class="options-panel">
                <div class="option-group">
                    <label>UUID Version</label>
                    <div class="radio-group">
                        <label class="radio-option">
                            <input type="radio" name="uuidVersion" value="v4" checked>
                            <span>UUID v4 (Random)</span>
                        </label>
                        <label class="radio-option">
                            <input type="radio" name="uuidVersion" value="v1">
                            <span>UUID v1 (Timestamp)</span>
                        </label>
                        <label class="radio-option">
                            <input type="radio" name="uuidVersion" value="v7">
                            <span>UUID v7 (Unix Epoch)</span>
                        </label>
                    </div>
                </div>
                <div class="option-group">
                    <label>Output Format</label>
                    <div class="checkbox-group">
                        <label class="checkbox-option">
                            <input type="checkbox" id="uppercase" checked>
                            <span>Uppercase</span>
                        </label>
                        <label class="checkbox-option">
                            <input type="checkbox" id="braces" checked>
                            <span>With Braces</span>
                        </label>
                        <label class="checkbox-option">
                            <input type="checkbox" id="hyphens" checked>
                            <span>With Hyphens</span>
                        </label>
                    </div>
                </div>
                <div class="option-group">
                    <label>Quantity</label>
                    <div class="quantity-selector">
                        <button class="qty-btn" onclick="changeQty(-1)">-</button>
                        <input type="number" id="quantity" value="1" min="1" max="100">
                        <button class="qty-btn" onclick="changeQty(1)">+</button>
                    </div>
                </div>
            </div>
            <div class="action-panel">
                <button class="generate-btn" onclick="generateUUIDs()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"></path>
                    </svg>
                    Generate UUIDs
                </button>
            </div>
        </div>

        <div class="results-section">
            <div class="results-header">
                <h2>Generated UUIDs</h2>
                <div class="uuid-count" id="uuidCount">0 UUIDs generated</div>
            </div>
            <div class="results-content" id="resultsContent">
                <div class="no-results">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="3" y1="9" x2="21" y2="9"></line>
                        <line x1="9" y1="21" x2="9" y2="9"></line>
                    </svg>
                    <p>Click "Generate UUIDs" to create new identifiers</p>
                </div>
            </div>
        </div>

        <section class="uuid-info">
            <h2>UUID Versions Explained</h2>
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path>
                            <line x1="7" y1="7" x2="7.01" y2="7"></line>
                        </svg>
                    </div>
                    <h3>UUID v4 (Random)</h3>
                    <p>Most common version. 122 random bits create unique identifiers with virtually zero collision probability.</p>
                    <span class="uuid-example">550e8400-e29b-41d4-a716-446655440000</span>
                    <span class="info-badge success">Recommended</span>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                    </div>
                    <h3>UUID v1 (Timestamp)</h3>
                    <p>Contains timestamp and MAC address. Sortable but exposes machine identity and generation time.</p>
                    <span class="uuid-example">6ba7b810-9dad-11d1-80b4-00c04fd430c8</span>
                    <span class="info-badge warning">Privacy Concern</span>
                </div>
                <div class="info-card">
                    <div class="info-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="1" x2="12" y2="23"></line>
                            <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                        </svg>
                    </div>
                    <h3>UUID v7 (Unix Epoch)</h3>
                    <p>Newer version with embedded Unix timestamp. Sortable and time-ordered while maintaining randomness.</p>
                    <span class="uuid-example">0192a3e7-5f8c-7f9a-b3d4-e1f2a3c4d5e6</span>
                    <span class="info-badge success">Recommended</span>
                </div>
            </div>
        </section>

        <section class="quick-reference">
            <h2>Use Cases</h2>
            <div class="reference-grid">
                <div class="reference-card">
                    <h3>Database Keys</h3>
                    <p>Distributed systems can generate IDs without coordination, preventing hot spots and enabling parallel processing.</p>
                </div>
                <div class="reference-card">
                    <h3>Session IDs</h3>
                    <p>Secure, unpredictable identifiers for user sessions, tokens, and authentication cookies.</p>
                </div>
                <div class="reference-card">
                    <h3>URL Shorteners</h3>
                    <p>Generate unique short codes for redirecting URLs and tracking links.</p>
                </div>
                <div class="reference-card">
                    <h3>File Names</h3>
                    <p>Create unique identifiers for uploaded files, preventing name collisions and enabling deduplication.</p>
                </div>
            </div>
        </section>'''
    ).replace(
        'common-patterns',
        'uuid-info'
    ).replace(
        '''    <div class="patterns-grid">
                <button class="pattern-btn" data-pattern="\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b" data-desc="Email address">
                    Email
                </button>
                <button class="pattern-btn" data-pattern="https?:\\/\\/[\\w\\-._~:/?#[\\]@!$&'()*+,;=%]+" data-desc="URL">
                    URL
                </button>
                <button class="pattern-btn" data-pattern="\\d{4}[-/]\\d{2}[-/]\\d{2}" data-desc="Date (YYYY-MM-DD or YYYY/MM/DD)">
                    Date
                </button>
                <button class="pattern-btn" data-pattern="\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}" data-desc="IPv4 address">
                    IPv4
                </button>
                <button class="pattern-btn" data-pattern="#[A-Fa-f0-9]{6}" data-desc="Hex color code">
                    Hex Color
                </button>
                <button class="pattern-btn" data-pattern="\\+?[1-9]\\d{1,14}" data-desc="Phone number (E.164)">
                    Phone
                </button>
                <button class="pattern-btn" data-pattern="\\$[\\d,]+\\.\\d{2}" data-desc="USD currency">
                    USD
                </button>
                <button class="pattern-btn" data-pattern="[A-Z]{2}[0-9]{2}[A-Z0-9]{4,30}" data-desc="IBAN">
                    IBAN
                </button>
            </div>
        </section>''',
        '''    <div class="patterns-grid">
                <button class="pattern-btn" onclick="generateBatch(5)">Generate 5</button>
                <button class="pattern-btn" onclick="generateBatch(10)">Generate 10</button>
                <button class="pattern-btn" onclick="generateBatch(25)">Generate 25</button>
                <button class="pattern-btn" onclick="generateBatch(50)">Generate 50</button>
            </div>
        </section>'''
    ).replace(
        '''function loadSample() {
    document.getElementById('regexInput').value = '\\\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\\\.[A-Z|a-z]{2,}\\\\b';
    document.getElementById('testInput').value = 'Contact us at support@example.com or sales@company.org or test@sub.domain.co.uk';
    testRegex();
}''',
        '''function generateUUIDs() {
    const version = document.querySelector('input[name="uuidVersion"]:checked').value;
    const uppercase = document.getElementById('uppercase').checked;
    const braces = document.getElementById('braces').checked;
    const hyphens = document.getElementById('hyphens').checked;
    const quantity = parseInt(document.getElementById('quantity').value) || 1;
    
    let uuids = [];
    for (let i = 0; i < quantity; i++) {
        let uuid;
        if (version === 'v4') {
            uuid = generateUUIDv4();
        } else if (version === 'v1') {
            uuid = generateUUIDv1();
        } else if (version === 'v7') {
            uuid = generateUUIDv7();
        }
        
        if (!uppercase) uuid = uuid.toLowerCase();
        if (!hyphens) uuid = uuid.replace(/-/g, '');
        if (!braces) uuid = uuid.replace(/\\{/g, '').replace(/\\}/g, '');
        
        uuids.push(uuid);
    }
    
    displayUUIDs(uuids);
}

function generateUUIDv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0;
        const v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function generateUUIDv1() {
    const now = new Date();
    const clock = Math.floor(Math.random() * 0x3fff);
    const node = Array.from({length: 6}, () => Math.floor(Math.random() * 256));
    
    const time_low = (now.getTime() * 10000 + 0x80000000) & 0xffffffff;
    const time_mid = (now.getTime() / 0x100000000 * 10000) & 0xffff;
    const time_hi_and_version = (now.getTime() / 0x100000000 * 10000) >> 16 | 0x1000;
    const clock_seq_hi_and_reserved = clock >> 8 | 0x80;
    const clock_seq_low = clock & 0xff;
    
    return [
        (time_low >> 24) & 0xff, (time_low >> 16) & 0xff, (time_low >> 8) & 0xff, time_low & 0xff,
        (time_mid >> 8) & 0xff, time_mid & 0xff,
        (time_hi_and_version >> 8) & 0xff, time_hi_and_version & 0xff,
        (clock_seq_hi_and_reserved >> 8) & 0xff, clock_seq_low & 0xff,
        ...node
    ].map(b => b.toString(16).padStart(2, '0')).join('');
}

function generateUUIDv7() {
    const now = new Date();
    const timestamp = now.getTime();
    
    const time_high = ((timestamp & 0x1fffffff) << 22) | ((timestamp >> 13) & 0x3fffff);
    const time_low = (timestamp >> 37) & 0xffffff;
    
    const random_high = Math.floor(Math.random() * 0xfffff);
    const random_low = Array.from({length: 8}, () => Math.floor(Math.random() * 256)).join('').slice(0, 12);
    
    const hex = time_low.toString(16).padStart(6, '0') + 
                (0x70 | (Math.random() * 0xf)).toString(16) + 
                random_high.toString(16).padStart(5, '0') + 
                (0x80 | (Math.random() * 0x3f)).toString(16) + 
                random_low;
    
    return hex.slice(0, 8) + '-' + hex.slice(8, 12) + '-7' + hex.slice(13, 16) + '-89' + hex.slice(18);
}

function displayUUIDs(uuids) {
    const resultsContent = document.getElementById('resultsContent');
    const uuidCount = document.getElementById('uuidCount');
    
    uuidCount.textContent = uuids.length + ' UUID' + (uuids.length !== 1 ? 's' : '') + ' generated';
    
    let html = '<div class="uuid-list">';
    uuids.forEach((uuid, index) => {
        html += '<div class="uuid-item">';
        html += '<div class="uuid-value" id="uuid-' + index + '">' + uuid + '</div>';
        html += '<button class="copy-btn" onclick="copyUUID(\\'uuid-' + index + '\\')">Copy</button>';
        html += '</div>';
    });
    html += '</div>';
    
    // Add bulk actions
    html += '<div class="bulk-actions">';
    html += '<button class="bulk-btn" onclick="copyAllUUIDs()">Copy All</button>';
    html += '<button class="bulk-btn" onclick="downloadUUIDs()">Download as TXT</button>';
    html += '</div>';
    
    resultsContent.innerHTML = html;
}

function copyUUID(id) {
    const uuid = document.getElementById(id).textContent;
    navigator.clipboard.writeText(uuid).then(() => {
        const btn = document.getElementById(id).nextElementSibling;
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => {
            btn.textContent = originalText;
            btn.classList.remove('copied');
        }, 1500);
    });
}

function copyAllUUIDs() {
    const uuids = Array.from(document.querySelectorAll('.uuid-value')).map(el => el.textContent);
    navigator.clipboard.writeText(uuids.join('\\n')).then(() => {
        alert('All UUIDs copied to clipboard!');
    });
}

function downloadUUIDs() {
    const uuids = Array.from(document.querySelectorAll('.uuid-value')).map(el => el.textContent);
    const blob = new Blob([uuids.join('\\n')], {type: 'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'uuids-' + new Date().toISOString().slice(0,10) + '.txt';
    a.click();
    URL.revokeObjectURL(url);
}

function changeQty(delta) {
    const input = document.getElementById(\\'quantity\\');
    let value = parseInt(input.value) + delta;
    value = Math.max(1, Math.min(100, value));
    input.value = value;
}

function generateBatch(count) {
    document.getElementById(\\'quantity\\').value = count;
    generateUUIDs();
}'''
    ).replace(
        '''document.getElementById('regexInput').addEventListener('input', testRegex);
document.getElementById('testInput').addEventListener('input', testRegex);
document.getElementById('flagGlobal').addEventListener('change', testRegex);
document.getElementById('flagCaseInsensitive').addEventListener('change', testRegex);
document.getElementById('flagMultiline').addEventListener('change', testRegex);

document.querySelectorAll(\\.pattern-btn\\).forEach(btn => {
    btn.addEventListener(\\'click\\', () => {
        document.getElementById(\\'regexInput\\').value = btn.dataset.pattern;
        testRegex();
    });
});''',
        '''document.querySelectorAll('input[name="uuidVersion"]').forEach(radio => {
    radio.addEventListener('change', generateUUIDs);
});

document.getElementById('uppercase').addEventListener('change', generateUUIDs);
document.getElementById('braces').addEventListener('change', generateUUIDs);
document.getElementById('hyphens').addEventListener('change', generateUUIDs);
document.getElementById('quantity').addEventListener('change', generateUUIDs);'''
    ).replace(
        '''document.getElementById('regexInput').addEventListener('input', testRegex);
document.getElementById('testInput').addEventListener('input', testRegex);
document.getElementById('flagGlobal').addEventListener('change', testRegex);
document.getElementById('flagCaseInsensitive').addEventListener('change', testRegex);
document.getElementById('flagMultiline').addEventListener('change', testRegex);''',
        '''document.querySelectorAll('input[name="uuidVersion"]').forEach(radio => {
    radio.addEventListener('change', generateUUIDs);
});

document.getElementById('uppercase').addEventListener('change', generateUUIDs);
document.getElementById('braces').addEventListener('change', generateUUIDs);
document.getElementById('hyphens').addEventListener('change', generateUUIDs);
document.getElementById('quantity').addEventListener('change', generateUUIDs);'''
    )
    
    # 修改CSS
    content = content.replace(
        '''.tool-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
}''',
        '''.tool-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-bottom: 2rem;
}'''
    ).replace(
        '''.flags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.flag-option {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--bg-secondary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
}

.flag-option:hover {
    background: var(--bg-tertiary);
}

.flag-option input {
    width: 18px;
    height: 18px;
    cursor: pointer;
}

.flag-label {
    font-family: var(--font-mono);
    font-size: 0.9rem;
}''',
        '''.options-panel {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    background: var(--bg-secondary);
    padding: 1.5rem;
    border-radius: 12px;
}

.option-group {
    flex: 1;
    min-width: 200px;
}

.option-group label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.75rem;
    color: var(--text-secondary);
    font-size: 0.9rem;
}

.radio-group, .checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.radio-option, .checkbox-option {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem;
    background: var(--bg-tertiary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.9rem;
}

.radio-option:hover, .checkbox-option:hover {
    background: var(--bg-primary);
}

.radio-option input, .checkbox-option input {
    width: 16px;
    height: 16px;
    cursor: pointer;
}

.quantity-selector {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.qty-btn {
    width: 36px;
    height: 36px;
    border: 1px solid var(--border-color);
    background: var(--bg-tertiary);
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.2rem;
    transition: all 0.2s;
}

.qty-btn:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}

.quantity-selector input {
    width: 60px;
    text-align: center;
    padding: 0.5rem;
    border: 1px solid var(--border-color);
    background: var(--bg-tertiary);
    border-radius: 6px;
    font-size: 1rem;
}

.action-panel {
    display: flex;
    justify-content: center;
}

.generate-btn {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 2rem;
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}

.generate-btn:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.generate-btn svg {
    width: 24px;
    height: 24px;
}'''
    ).replace(
        '''.results-content .no-results {
    text-align: center;
    padding: 4rem 2rem;
}

.results-content .no-results svg {
    width: 64px;
    height: 64px;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.results-content .no-results p {
    color: var(--text-muted);
    font-size: 1rem;
}''',
        '''.results-content .no-results {
    text-align: center;
    padding: 4rem 2rem;
}

.results-content .no-results svg {
    width: 64px;
    height: 64px;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.results-content .no-results p {
    color: var(--text-muted);
    font-size: 1rem;
}

.uuid-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.uuid-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: var(--bg-secondary);
    padding: 1rem 1.25rem;
    border-radius: 8px;
    border: 1px solid var(--border-color);
}

.uuid-value {
    flex: 1;
    font-family: var(--font-mono);
    font-size: 1rem;
    letter-spacing: 0.5px;
}

.copy-btn {
    padding: 0.5rem 1rem;
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.85rem;
    transition: all 0.2s;
}

.copy-btn:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}

.copy-btn.copied {
    background: #22c55e;
    color: white;
    border-color: #22c55e;
}

.bulk-actions {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-color);
}

.bulk-btn {
    flex: 1;
    padding: 0.75rem 1.5rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: all 0.2s;
}

.bulk-btn:hover {
    background: var(--bg-tertiary);
    border-color: var(--primary);
}

.uuid-count {
    font-size: 0.9rem;
    color: var(--text-muted);
}

.uuid-example {
    display: block;
    font-family: var(--font-mono);
    font-size: 0.8rem;
    background: var(--bg-tertiary);
    padding: 0.5rem;
    border-radius: 4px;
    margin-top: 0.75rem;
    word-break: break-all;
}

.info-badge {
    display: inline-block;
    font-size: 0.75rem;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    margin-top: 0.5rem;
}

.info-badge.success {
    background: rgba(34, 197, 94, 0.15);
    color: #22c55e;
}

.info-badge.warning {
    background: rgba(234, 179, 8, 0.15);
    color: #eab308;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}

.info-card {
    background: var(--bg-secondary);
    border-radius: 12px;
    padding: 1.5rem;
}

.info-icon {
    width: 48px;
    height: 48px;
    background: var(--primary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
}

.info-icon svg {
    width: 24px;
    height: 24px;
    color: white;
}

.info-card h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}

.info-card p {
    margin: 0;
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
}'''
    )
    
    output_path = os.path.join(BASE_DIR, 'uuid-generator.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[OK] uuid-generator.html created')
    return True

def main():
    print('=' * 50)
    print('Creating P1 Tool Pages')
    print('=' * 50)
    
    create_jwt_decoder()
    create_hash_generator()
    create_uuid_generator()
    
    print('=' * 50)
    print('All P1 tools created successfully!')
    print('=' * 50)

if __name__ == '__main__':
    main()
