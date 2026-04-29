/**
 * Shared Navbar Component for aijsons.com
 * Usage: <div id="navbar-placeholder"></div>
 *        <script src="/js/navbar.js"></script>
 */
(function () {
  // Tool list config: [slug, label, svg_path_d]
  const TOOLS = [
    {
      slug: 'json-formatter',
      label: 'Format',
      icon: '<polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line>',
    },
    {
      slug: 'json-escape',
      label: 'Escape',
      icon: '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>',
    },
    {
      slug: 'json-extract',
      label: 'Extract',
      icon: '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>',
    },
    {
      slug: 'json-sort',
      label: 'Sort',
      icon: '<line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline>',
    },
    {
      slug: 'json-clean',
      label: 'Clean',
      icon: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>',
    },
    {
      slug: 'json-to-xml',
      label: 'XML',
      icon: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline>',
    },
    {
      slug: 'json-to-yaml',
      label: 'YAML',
      icon: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline>',
    },
    {
      slug: 'json-viewer',
      label: 'Viewer',
      icon: '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>',
    },
    {
      slug: 'json-to-csv',
      label: 'CSV',
      icon: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="8" y1="13" x2="16" y2="13"></line><line x1="8" y1="17" x2="16" y2="17"></line>',
    },
    {
      slug: 'json-compare',
      label: 'Compare',
      icon: '<path d="M18 20V10"></path><path d="M12 20V4"></path><path d="M6 20v-6"></path>',
    },
    {
      slug: 'regex-tester',
      label: 'Regex',
      icon: '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>',
    },
    {
      slug: 'base64',
      label: 'Base64',
      icon: '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>',
    },
    {
      slug: 'url-encoder',
      label: 'URL Encoder',
      icon: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>',
    },
    {
      slug: 'csv-to-excel',
      label: 'Excel',
      icon: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline>',
    },
    {
      slug: 'excel-remove-duplicates',
      label: 'Remove Duplicates',
      icon: '<polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>',
    },
    {
      slug: 'merge-csv',
      label: 'Merge CSV',
      icon: '<path d="M16 16v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h2"></path><rect x="8" y="8" width="12" height="12" rx="2"></rect>',
    },
    {
      slug: 'batch-renamer',
      label: 'Batch Rename',
      icon: '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>',
    },
    {
      slug: 'pdf-split',
      label: 'PDF Split',
      icon: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline>',
    },
    {
      slug: 'timestamp-converter',
      label: 'Timestamp',
      icon: '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
    },
    {
      slug: 'css-minifier',
      label: 'CSS Minifier',
      icon: '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>',
    },
    {
      slug: 'html-encoder',
      label: 'HTML Encoder',
      icon: '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>',
    },
    {
      slug: 'jwt-decoder',
      label: 'JWT',
      icon: '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>',
    },
    {
      slug: 'hash-generator',
      label: 'Hash',
      icon: '<line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line>',
    },
    {
      slug: 'uuid-generator',
      label: 'UUID',
      icon: '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line>',
    },
  ];

  function svg(d) {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">${d}</svg>`;
  }

  function buildNavbar() {
    const currentPath = window.location.pathname.replace(/\/$/, '');

    // Detect active tool slug
    const activeSlug = currentPath.startsWith('/tools/')
      ? currentPath.replace('/tools/', '')
      : null;

    // Build tool dropdown items
    const toolItems = TOOLS.map((t) => {
      const isActive = t.slug === activeSlug ? ' active' : '';
      return `<a href="/tools/${t.slug}" class="nav-link${isActive}">${svg(t.icon)}${t.label}</a>`;
    }).join('\n');

    // Build nav links with active state helper
    function navLink(href, iconD, label) {
      const isActive = currentPath === href || currentPath.startsWith(href + '/') ? ' active' : '';
      return `<a href="${href}" class="nav-link${isActive}">${svg(iconD)}${label}</a>`;
    }

    const html = `
<nav class="navbar">
  <a href="/" class="navbar-brand">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
      <polyline points="14 2 14 8 20 8"></polyline>
      <line x1="16" y1="13" x2="8" y2="13"></line>
      <line x1="16" y1="17" x2="8" y2="17"></line>
    </svg>
    AI JSON
  </a>

  <button class="menu-toggle" aria-label="Menu">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <line x1="3" y1="12" x2="21" y2="12"></line>
      <line x1="3" y1="6" x2="21" y2="6"></line>
      <line x1="3" y1="18" x2="21" y2="18"></line>
    </svg>
  </button>

  <div class="navbar-links">
    ${navLink('/', '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline>', 'Home')}

    <!-- Tools Dropdown -->
    <div class="nav-dropdown">
      <a href="#" class="nav-link nav-dropdown-toggle${activeSlug ? ' active' : ''}" onclick="return false;" aria-haspopup="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="3" width="7" height="7"></rect>
          <rect x="14" y="3" width="7" height="7"></rect>
          <rect x="14" y="14" width="7" height="7"></rect>
          <rect x="3" y="14" width="7" height="7"></rect>
        </svg>
        Tools
        <svg class="chevron-down" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </a>
      <div class="nav-dropdown-menu wide">
        <div class="nav-dropdown-menu-box">
          ${toolItems}
        </div>
      </div>
    </div>

    ${navLink('/blog', '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>', 'Blog')}
    ${navLink('/best-practices', '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>', 'Practices')}
    ${navLink('/news', '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>', 'News')}
    ${navLink('/about', '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line>', 'About')}
    ${navLink('/changelog', '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>', 'Changelog')}

    <a href="/tools/json-formatter" class="nav-link cta">Try Formatter</a>
  </div>
</nav>`;

    return html;
  }

  function mount() {
    const placeholder = document.getElementById('navbar-placeholder');
    if (!placeholder) return;
    placeholder.outerHTML = buildNavbar();

    // Mobile menu toggle
    const toggle = document.querySelector('.menu-toggle');
    const links = document.querySelector('.navbar-links');
    if (toggle && links) {
      toggle.addEventListener('click', function () {
        links.classList.toggle('active');
      });
    }

    // Dropdown hover/click support
    document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
      dropdown.addEventListener('mouseenter', function () {
        this.classList.add('open');
      });
      dropdown.addEventListener('mouseleave', function () {
        this.classList.remove('open');
      });
      // Mobile tap
      const toggle = dropdown.querySelector('.nav-dropdown-toggle');
      if (toggle) {
        toggle.addEventListener('click', function (e) {
          e.preventDefault();
          dropdown.classList.toggle('open');
        });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
