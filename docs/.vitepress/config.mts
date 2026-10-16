import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "MOFA",
  description: "Microsoft Overview Feed For Apple",
  lastUpdated: true,
  cleanUrls: true,
  sitemap: {
    hostname: 'https://mofa.cocolabs.dev'
  },
  vite: {
    server: {
      // the landing page imports repo_raw_data/*.json, which lives outside docs/
      fs: { allow: ['..'] }
    }
  },
  markdown: {
    // Ensure HTML is enabled in markdown options
    html: true,
  },
  head: [
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&display=swap' }],
    ['link', { rel: 'icon', href: '/favicon.ico', sizes: '32x32' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' }],
    // Social preview (Open Graph + Twitter Card)
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'MOFA' }],
    ['meta', { property: 'og:title', content: 'MOFA - Microsoft Overview Feed For Apple' }],
    ['meta', { property: 'og:description', content: 'Empowering Apple Devices with Microsoft Solutions' }],
    ['meta', { property: 'og:url', content: 'https://mofa.cocolabs.dev/' }],
    ['meta', { property: 'og:image', content: 'https://mofa.cocolabs.dev/social-preview.png' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { property: 'og:image:alt', content: 'MOFA - Microsoft Overview Feed For Apple' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'MOFA - Microsoft Overview Feed For Apple' }],
    ['meta', { name: 'twitter:description', content: 'Empowering Apple Devices with Microsoft Solutions' }],
    ['meta', { name: 'twitter:image', content: 'https://mofa.cocolabs.dev/social-preview.png' }],
    ['script', { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-P45L4Y5WFQ' }],
    ['script', {}, `
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-P45L4Y5WFQ');
    `],
    // Early theme apply to avoid flash (browser only)
    ['script', { id: 'mofa-theme-early' }, `
      (function() {
        if (typeof window === 'undefined' || typeof document === 'undefined') return;
        try {
          var KEY = 'vitepress-theme-appearance';
          var saved = localStorage.getItem(KEY);
          var sysDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
          var mode = (saved === 'dark' || saved === 'light') ? saved : (sysDark ? 'dark' : 'light');
          var el = document.documentElement;
          el.classList.toggle('dark', mode === 'dark');
          el.setAttribute('data-theme', mode);
          el.style.colorScheme = mode;
        } catch (_) {}
      })();
    `],
    // Robust SPA-safe toggle and sync (browser only)
    ['script', { id: 'mofa-theme-toggle', defer: '' }, `
      (function() {
        if (typeof window === 'undefined' || typeof document === 'undefined') return;
        if (window.__mofaThemeInit) return;
        window.__mofaThemeInit = true;

        var KEY = 'vitepress-theme-appearance';

        function getStored() {
          try {
            var v = localStorage.getItem(KEY);
            if (v === 'dark' || v === 'light') return v;
          } catch (_) {}
          return null;
        }
        function setStored(mode) {
          try { localStorage.setItem(KEY, mode); } catch (_) {}
        }
        function isDark() {
          var el = document.documentElement;
          return el.classList.contains('dark') || el.getAttribute('data-theme') === 'dark';
        }
        function apply(mode) {
          var dark = mode === 'dark';
          var el = document.documentElement;
          el.classList.toggle('dark', dark);
          el.setAttribute('data-theme', dark ? 'dark' : 'light');
          el.style.colorScheme = dark ? 'dark' : 'light';
          setStored(dark ? 'dark' : 'light');
          updateButton(dark);
        }
        function updateButton(dark) {
          var btn = document.getElementById('appearance-toggle');
          if (!btn) return;
          btn.setAttribute('aria-checked', String(!!dark));
          btn.title = dark ? 'Switch to light theme' : 'Switch to dark theme';
        }

        apply(getStored() || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));

        document.addEventListener('click', function(e) {
          var btn = e.target && e.target.closest && e.target.closest('#appearance-toggle');
          if (!btn) return;
          e.preventDefault();
          apply(isDark() ? 'light' : 'dark');
        }, true);

        window.addEventListener('storage', function(e) {
          if (!e || e.key !== KEY) return;
          if (e.newValue === 'dark' || e.newValue === 'light') apply(e.newValue);
        });

        var mo = new MutationObserver(function() { updateButton(isDark()); });
        mo.observe(document.documentElement, { subtree: true, childList: true });

        if (document.readyState === 'complete' || document.readyState === 'interactive') {
          updateButton(isDark());
        } else {
          document.addEventListener('DOMContentLoaded', function() { updateButton(isDark()); });
        }
      })();
    `]
  ],
  themeConfig: {
    search: {
      provider: 'local'
    },
    editLink: {
      pattern: 'https://github.com/cocopuff2u/mofa_website/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    logo: { light: '/images/mofa-icon-light.svg', dark: '/images/mofa-icon-dark.svg', alt: 'MOFA' },
    nav: [
      { text: 'Get Started', link: '/home' },
      { text: 'Standalone Apps', link: '/standalone_apps/standalone_current_version_en' },
      { text: 'MacOS AppStore', link: '/macos_appstore/macos_appstore_current_version' },
      { text: 'iOS AppStore', link: '/ios_appstore/ios_appstore_current_version' }
    ],
    sidebar: [
      {
      items: [
        { text: 'Get Started', link: '/home' }
      ]
      },
      {
        text: '📦 Standalone Apps',
        collapsed: true,
        items: [
          { text: 'Current Versions', link: '/standalone_apps/standalone_current_version_en',
            collapsed: true,
            items: [
              { text: 'Simple View', link: '/simple' },
              { text: 'Minimal View', link: '/minimal' },
              { text: 'SHA1 Hashes', link: '/standalone_apps/standalone_sha1_hashes_en' },
              { text: 'SHA256 Hashes', link: '/standalone_apps/standalone_sha256_hashes_en' }
            ]
          },
          { text: 'Preview Versions', link: '/standalone_apps/standalone_preview_version_en',
            collapsed: true,
            items: [
              { text: 'SHA1 Hashes', link: '/standalone_apps/standalone_preview_sha1_hashes_en' },
              { text: 'SHA256 Hashes', link: '/standalone_apps/standalone_preview_sha256_hashes_en' }
            ]
          },
          { text: 'Beta Versions', link: '/standalone_apps/standalone_beta_version_en',
            collapsed: true,
            items: [
              { text: 'SHA1 Hashes', link: '/standalone_apps/standalone_beta_sha1_hashes_en' },
              { text: 'SHA256 Hashes', link: '/standalone_apps/standalone_beta_sha256_hashes_en' }
            ]
          },
          { text: 'Other Microsoft Apps', link: '/standalone_apps/macos_standalone_other_readme',
            collapsed: true,
            items: [
              { text: 'SHA256 Hashes', link: '/standalone_apps/macos_standalone_other_sha256' }
            ]
          },
          { text: 'Last Supported Versions', link: '/standalone_apps/standalone_last_supported_versions_en' },
          { text: 'OneDrive Versions', link: '/standalone_apps/macos_standalone_onedrive_readme' },
          { text: 'Office Update History', link: '/standalone_apps/standalone_update_history_en' },
          { text: 'Teams Update History', link: '/standalone_apps/teams_update_history_en' },
          { text: 'Office CVE History', link: '/standalone_apps/standalone_cve_history_en' },
          { text: 'Raw Feeds', link: '/standalone_apps/standalone_raw_feeds_en' }
        ]
      },
      {
        text: '📚 MacOS Guides',
        collapsed: true,
        items: [
          // Hidden until the MDM guide has content
          // {
          //   text: 'Mobile Device Management',
          //   collapsed: true,
          //   items: [
          //     { text: 'MDM Overview', link: '/placeholder' }
          //   ]
          // },
          { text: 'How To SHA1', link: '/guides/how_to_sha1' },
          { text: 'How To SHA256', link: '/guides/how_to_sha256' },
          { text: 'How To Plist', link: '/guides/how_to_plist' }
        ]
      },
      {
                text: '🛠️ MacOS Tools',
        collapsed: true,
        items: [
          { text: 'Microsoft Office Repair Tools', link: '/macos_tools/microsoft_office_repair_tools' },
          { text: 'App Icons', link: '/macos_tools/app_icons' },
          { text: 'Community Scripts', link: '/macos_tools/community_scripts' },
          { text: 'Preconfigured Profiles', link: '/macos_tools/preconfigured_profiles',
            collapsed: true,
            items: [
              { text: 'Profile Breakdown', link: '/macos_tools/profile_breakdown' }
            ]
           }
        ]
      },
      {
        text: '💻 MacOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/macos_appstore/macos_appstore_current_version' },
          { text: 'Minimal View', link: '/minimal_macos_appstore' },
          { text: 'Raw Feeds', link: '/macos_appstore/macos_raw_feeds' }
        ]
      },
      {
        text: '📱 iOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/ios_appstore/ios_appstore_current_version' },
          { text: 'Minimal View', link: '/minimal_ios_appstore' },
          { text: 'Raw Feeds', link: '/ios_appstore/ios_raw_feeds' }
        ]
      },
      {
        text: 'ℹ️ About & Support',
        collapsed: true,
        items: [
          { text: '📖 About', link: '/about_support/about' },
          { text: '📝 Feedback', link: '/about_support/feedback' },
          { text: '👥 Meet The Team', link: '/about_support/team' },
          { text: '🐞 Report Issues', link: '/about_support/report_issue' },
          // Hidden: the changelog is no longer maintained
          // { text: '🆕 Changelog', link: '/about_support/changelog' },
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/cocopuff2u/MOFA' },
      { icon: 'rss', link: 'https://mofa.cocolabs.dev/standalone_apps/standalone_raw_feeds_en#rss-feeds' },
      { icon: 'buymeacoffee', link: 'https://buymeacoffee.com/cocopuff2u' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: `Copyright © ${new Date().getFullYear()} MOFA All rights reserved.`
    }
  }
})
