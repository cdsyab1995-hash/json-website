export default {
  async fetch(request) {
    const url = new URL(request.url);
    let path = url.pathname.replace(/\/$/, '');

    // ========== 工具路径映射 ==========
    const toolMap = {
      // JSON 工具
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
      'toexcel': 'json-to-csv',
      'compare': 'json-compare',
      // CSV/Excel 工具
      'csvtoexcel': 'csv-to-excel',
      'mergecsv': 'merge-csv',
      'excelremoveduplicates': 'excel-remove-duplicates',
      // 编码/解码工具
      'base64': 'base64',
      'hash': 'hash-generator',
      'hash-generator': 'hash-generator',
      'urlencode': 'url-encoder',
      'htmlencode': 'html-encoder',
      // 开发工具
      'jwt': 'jwt-decoder',
      'regex': 'regex-tester',
      'timestamp': 'timestamp-converter',
      'uuid': 'uuid-generator',
      // 其他工具
      'cssminifier': 'css-minifier',
      'pdfsplit': 'pdf-split',
      'batchrenamer': 'batch-renamer'
    };

    // ========== News 文章映射 ==========
    const newsMap = {
      'api-transformations-2026': 'api-transformations-2026',
      'browser-devtools-json-schema': 'browser-devtools-json-schema',
      'bun-2-json-serialization': 'bun-2-json-serialization',
      'cursor-vscode-json-lint-ai': 'cursor-vscode-json-lint-ai',
      'json-schema-to-typescript-v6': 'json-schema-to-typescript-v6',
      'json-schema-w3c-recommendation': 'json-schema-w3c-recommendation',
      'json-streaming-api-browser': 'json-streaming-api-browser',
      'jsonata-2-ai-query': 'jsonata-2-ai-query',
      'mcp-10000-servers': 'mcp-10000-servers',
      'nextjs-16-json-streaming': 'nextjs-16-json-streaming',
      'nodejs-24-json-schema': 'nodejs-24-json-schema',
      'zod-v4-5m-downloads': 'zod-v4-5m-downloads'
    };

    // ========== Blog 文章映射 ==========
    const blogMap = {
      'compare-json-documents-find-differences': 'compare-json-documents-find-differences',
      'curl-json-api-guide': 'curl-json-api-guide',
      'json-api-error-handling-2026': 'json-api-error-handling-2026',
      'json-edge-computing-cloudflare-workers': 'json-edge-computing-cloudflare-workers',
      'json-parsing-performance-comparison': 'json-parsing-performance-comparison',
      'json-patch-vs-merge-patch': 'json-patch-vs-merge-patch',
      'json-schema-complete-guide-2026': 'json-schema-complete-guide-2026',
      'json-viewer-tree-view-why-you-need-one': 'json-viewer-tree-view-why-you-need-one',
      'jwt-security-best-practices-2026': 'jwt-security-best-practices-2026',
      'mcp-json-standardizing-ai-tools': 'mcp-json-standardizing-ai-tools',
      'model-context-protocol-json-rpc-ai-tools': 'model-context-protocol-json-rpc-ai-tools',
      'postgresql-jsonb-vs-mongodb-document-store': 'postgresql-jsonb-vs-mongodb-document-store',
      'rfc9457-problem-details-json-api-errors': 'rfc9457-problem-details-json-api-errors',
      'sort-json-arrays-objects-guide': 'sort-json-arrays-objects-guide',
      'zod-json-schema-validation-ai': 'zod-json-schema-validation-ai'
    };

    // ========== 处理 /pages/xxx 或 /pages/xxx.html ==========
    const toolMatch = path.match(/^\/pages\/([^\/]+)(?:\.html)?$/);
    if (toolMatch) {
      const slug = toolMatch[1];
      const tool = toolMap[slug];

      if (tool) {
        return Response.redirect(url.origin + '/tools/' + tool, 301);
      }
      return new Response('Tool not found: ' + slug, { status: 404 });
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

    // ========== 处理 /pages/format.html 等旧格式 ==========
    const legacyToolMatch = path.match(/^\/pages\/(.+)\.html$/);
    if (legacyToolMatch) {
      const slug = legacyToolMatch[1];
      const tool = toolMap[slug];
      if (tool) {
        return Response.redirect(url.origin + '/tools/' + tool, 301);
      }
    }

    // ========== 尾斜杠清理 ==========
    if (path === '/tools' && new URL(request.url).pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/tools', 301);
    }
    if (path === '/blog' && new URL(request.url).pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/blog', 301);
    }
    if (path === '/news' && new URL(request.url).pathname.endsWith('/')) {
      return Response.redirect(url.origin + '/news', 301);
    }

    // 非 pages 路径，放行
    return fetch(request);
  }
};