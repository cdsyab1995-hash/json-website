export default {
  async fetch(request) {
    const url = new URL(request.url);
    let path = url.pathname.replace(/\/$/, '');

    // ========== 工具路径映射 ==========
    // 格式: 旧路径slug → 新工具名称
    const toolMap = {
      // 短名称映射
      'format': 'json-formatter',
      'escape': 'json-escape',
      'extract': 'json-extract',
      'validate': 'json-formatter',
      'minify': 'json-formatter',
      'sort': 'json-sort',
      'clean': 'json-clean',
      'toxml': 'json-to-xml',
      'toyaml': 'json-to-yaml',
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
      
      // 完整名称映射（兼容 /pages/tool-name 格式）
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
      'base64': 'base64',
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

    // ========== 处理 /pages/xxx 或 /pages/xxx.html ==========
    const match = path.match(/^\/pages\/([^/.]+)(?:\.html)?$/);
    if (match) {
      const slug = match[1];
      const tool = toolMap[slug];
      
      if (tool) {
        return Response.redirect(url.origin + '/tools/' + tool, 301);
      }
    }

    // ========== 处理 /pages/news/xxx.html ==========
    const newsMatch = path.match(/^\/pages\/news\/(.+)\.html$/);
    if (newsMatch) {
      const slug = newsMatch[1];
      return Response.redirect(url.origin + '/news/' + slug, 301);
    }

    // ========== 处理 /pages/blog/xxx.html ==========
    const blogMatch = path.match(/^\/pages\/blog\/(.+)\.html$/);
    if (blogMatch) {
      const slug = blogMatch[1];
      return Response.redirect(url.origin + '/blog/' + slug, 301);
    }

    // ========== 处理尾斜杠通用规则 ==========
    // /tools/ → /tools (避免目录不存在导致 404)
    if (path === '/tools' && new URL(request.url).pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/tools', 301);
    }
    // /blog/ → /blog
    if (path === '/blog' && new URL(request.url).pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/blog', 301);
    }
    // /news/ → /news
    if (path === '/news' && new URL(request.url).pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/news', 301);
    }

    // 非 pages 路径，放行
    return fetch(request);
  }
};