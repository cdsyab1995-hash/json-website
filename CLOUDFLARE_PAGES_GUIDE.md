# Cloudflare Pages Deployment Guide

## Architecture Change (2026-04-29)

**Old Architecture:**
```
DNS → GitHub Pages → 404.html JS Redirect (HTTP 404)
```

**New Architecture:**
```
DNS → Cloudflare Pages → _redirects 301 Redirect (SEO Friendly)
```

---

## Deployment Steps

### Step 1: Create Cloudflare Pages Project

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to **Workers & Pages** → **Create application**
3. Select **Pages** → **Create a Pages project**
4. Choose **Direct Upload** (upload entire site folder)

### Step 2: Upload Build Output

Upload the entire contents of `d:\网站开发-json\` directory:

```
/
├── index.html
├── 404.html
├── _redirects          ← NEW: Cloudflare Pages redirects
├── _headers
├── CNAME
├── manifest.json
├── sw.js
├── robots.txt
├── sitemap.xml
├── about/
├── blog/
├── changelog/
├── cookie/
├── css/
├── images/
├── js/
├── news/
├── privacy/
├── terms/
└── tools/
```

### Step 3: Configure Custom Domain

1. In your Pages project → **Settings** → **Custom domains**
2. Add `aijsons.com` (apex domain)
3. Add `www.aijsons.com` (www subdomain)

Cloudflare will automatically:
- Create appropriate DNS records
- Issue SSL certificates
- Configure HTTPS

### Step 4: Verify DNS Propagation

```bash
# Check if DNS points to Cloudflare Pages
nslookup aijsons.com

# Should return Cloudflare Pages IP range
# 198.41.128.0/17 or 162.159.192.0/20
```

### Step 5: Test Redirects

Test each redirect type:

```bash
# Tool pages with .html
curl -I https://aijsons.com/tools/json-formatter.html
# Should return: 301 → /tools/json-formatter

# Short paths
curl -I https://aijsons.com/pages/format
# Should return: 301 → /tools/json-formatter

# Blog articles
curl -I https://aijsons.com/blog/json-api-error-handling-2026
# Should return: 200 OK
```

---

## Cloudflare Pages Configuration

### Build Settings (if using framework)
- **Build command:** (leave empty for static site)
- **Build output directory:** (leave empty, use root)

### Redirects Configuration
The `_redirects` file handles all 301 redirects:
- 50+ redirect rules for legacy URLs
- Full SEO juice transfer
- HTTP 301 status codes

### Headers Configuration
The `_headers` file handles:
- Cache-Control for static assets
- Security headers
- CORS policies

---

## Post-Deployment Checklist

- [ ] Site loads at `https://aijsons.com`
- [ ] All tool pages work (e.g., `/tools/json-formatter`)
- [ ] `/tools/json-formatter.html` → 301 redirect
- [ ] `/pages/format` → 301 redirect
- [ ] Blog articles accessible
- [ ] News articles accessible
- [ ] GA4 tracking works
- [ ] SSL certificate valid

---

## GitHub Pages (Optional Backup)

You can keep GitHub Pages as a secondary deployment:

1. Keep GitHub repo but remove custom domain
2. Use GitHub Pages for development/preview
3. Cloudflare Pages for production

Or simply keep GitHub as-is since it won't be the primary anymore.

---

## Rollback Plan

If Cloudflare Pages causes issues:

1. Re-add `aijsons.com` to GitHub Pages custom domain
2. Update DNS A record to GitHub Pages IP
3. DNS propagates in ~5-30 minutes

---

## Monitoring

After deployment, check:
- **Cloudflare Analytics:** Traffic, redirects, errors
- **Google Search Console:** Index status, crawl errors
- **GA4:** Page views, bounce rates
