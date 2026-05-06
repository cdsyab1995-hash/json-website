export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/$/, '');

    // ========== 已知工具映射 (SEO友好的目标路径) ==========
    // 已知的短名称/别名 → 正确的工具路径
    const knownTools = {
      'format': 'json-formatter',
      'escape': 'json-escape',
      'extract': 'json-extract',
      'validate': 'json-formatter',
      'minify': 'json-formatter',
      'sort': 'json-sort',
      'clean': 'json-clean',
      'toxml': 'json-to-xml',
      'toyaml': 'json-to-yaml',
      'yaml': 'json-to-yaml',
      'view': 'json-viewer',
      'toxlsx': 'json-to-csv',
      'toxls': 'json-to-csv',
      'compare': 'json-compare',
      'csvtoexcel': 'csv-to-excel',
      'mergecsv': 'merge-csv',
      'excelremoveduplicates': 'excel-remove-duplicates',
      'base64': 'base64',
      'hash': 'hash-generator',
      'urlencode': 'url-encoder',
      'htmlencode': 'html-encoder',
      'jwt': 'jwt-decoder',
      'regex': 'regex-tester',
      'timestamp': 'timestamp-converter',
      'uuid': 'uuid-generator',
      'cssminifier': 'css-minifier',
      'pdfsplit': 'pdf-split',
      'batchrenamer': 'batch-renamer',
      // 完整名称（与 tools/ 目录一致）
      'json-formatter': 'json-formatter',
      'json-escape': 'json-escape',
      'json-extract': 'json-extract',
      'json-sort': 'json-sort',
      'json-clean': 'json-clean',
      'json-to-xml': 'json-to-xml',
      'json-to-yaml': 'json-to-yaml',
      'json-viewer': 'json-viewer',
      'json-to-csv': 'json-to-csv',
      'json-compare': 'json-compare',
      'csv-to-excel': 'csv-to-excel',
      'merge-csv': 'merge-csv',
      'excel-remove-duplicates': 'excel-remove-duplicates',
      'hash-generator': 'hash-generator',
      'url-encoder': 'url-encoder',
      'html-encoder': 'html-encoder',
      'jwt-decoder': 'jwt-decoder',
      'regex-tester': 'regex-tester',
      'timestamp-converter': 'timestamp-converter',
      'uuid-generator': 'uuid-generator',
      'css-minifier': 'css-minifier',
      'pdf-split': 'pdf-split',
      'batch-renamer': 'batch-renamer'
    };

    // ========== 通用正则模式 (无需维护slug列表) ==========

    // /pages/xxx.html → /tools/xxx (未知slug也生效)
    // 匹配 /pages/format.html, /pages/uuid-generator.html, /pages/yaml.html 等
    const toolPageMatch = path.match(/^\/pages\/([^/]+)\.html$/);
    if (toolPageMatch) {
      const slug = toolPageMatch[1];
      const target = knownTools[slug] || slug; // 有映射用映射，没有直接用slug
      return Response.redirect(url.origin + '/tools/' + target, 301);
    }

    // /pages/xxx (无扩展名) → /tools/xxx
    // 匹配 /pages/uuid, /pages/format, /pages/json-formatter 等
    const toolShortMatch = path.match(/^\/pages\/([^\/]+)$/);
    if (toolShortMatch) {
      const slug = toolShortMatch[1];
      // 排除已知的目录页
      if (slug === 'news' || slug === 'blog') {
        return Response.redirect(url.origin + '/' + slug, 301);
      }
      const target = knownTools[slug] || slug;
      return Response.redirect(url.origin + '/tools/' + target, 301);
    }

    // /pages/news/xxx.html → /news/xxx (通用：匹配任意文章slug)
    const newsArticleMatch = path.match(/^\/pages\/news\/(.+)\.html$/);
    if (newsArticleMatch) {
      return Response.redirect(url.origin + '/news/' + newsArticleMatch[1], 301);
    }

    // /pages/blog/xxx.html → /blog/xxx (通用：匹配任意文章slug)
    const blogArticleMatch = path.match(/^\/pages\/blog\/(.+)\.html$/);
    if (blogArticleMatch) {
      return Response.redirect(url.origin + '/blog/' + blogArticleMatch[1], 301);
    }

    // /pages/news/ → /news
    if (path === '/pages/news') {
      return Response.redirect(url.origin + '/news', 301);
    }

    // /pages/blog/ → /blog
    if (path === '/pages/blog') {
      return Response.redirect(url.origin + '/blog', 301);
    }

    // /pages/blog.html → /blog
    if (path === '/pages/blog.html') {
      return Response.redirect(url.origin + '/blog', 301);
    }

    // /pages/ → /tools
    if (path === '/pages') {
      return Response.redirect(url.origin + '/tools', 301);
    }

    // ========== 尾斜杠清理 (通用) ==========
    if ((path === '/tools' || path === '/blog' || path === '/news') &&
        url.pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/' + path.split('/').pop(), 301);
    }

    // ========== 静态页旧 .html 路径 (通用) ==========
    // 匹配 /xxx.html → /xxx (任意单层路径.html)
    const staticPageMatch = path.match(/^\/([a-z0-9-]+)\.html$/i);
    if (staticPageMatch) {
      return Response.redirect(url.origin + '/' + staticPageMatch[1], 301);
    }

    // 非匹配路径，放行
    return fetch(request);
  }
};
