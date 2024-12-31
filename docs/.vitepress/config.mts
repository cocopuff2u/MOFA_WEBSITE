the import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "MOFA",
  description: "Microsoft Overview For Apple",
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['script', { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-P45L4Y5WFQ' }],
    ['script', {}, `
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-P45L4Y5WFQ');
    `]
  ],
  themeConfig: {
    lastUpdated: true,
    cleanUrls: true,
    search: {
      provider: 'local'
    },
    editLink: {
      pattern: 'https://github.com/cocopuff2u/mofa_website/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    logo: '/images/logo_Mofa_NoBackground.png',
    nav: [
      { text: 'Get Started', link: '/home' },
      { text: 'Standalone Apps', link: '/standalone_current_version' },
      { text: 'MacOS AppStore', link: '/macos_appstore_current_version' },
      { text: 'iOS AppStore', link: '/ios_appstore_current_version' }
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
          { text: 'Current Versions', link: '/standalone_current_version',
            collapsed: true,
            items: [
              { text: 'SHA1 Hashes', link: '/standalone_sha1_hashes' },
              { text: 'SHA256 Hashes', link: '/standalone_sha256_hashes' }
            ]
          },
          { text: 'Last Supported Versions', link: '/standalone_last_supported_versions' },
          { text: 'Update History', link: '/standalone_update_history' },
          { text: 'CVE (Vulnerabilities)', link: '/standalone_cve_history' },
          { text: 'Raw Feeds', link: '/standalone_raw_feeds' }
        ]
      },
      {
        text: '📚 Standalone Guides',
        collapsed: true,
        items: [
          {
            text: 'Mobile Device Management',
            collapsed: true,
            items: [
              { text: 'MDM Overview', link: '/placeholder' }
            ]
          },
          {
            text: 'How To Guides',
            collapsed: true,
            items: [
              { text: 'How To SHA1', link: '/guides/how_to_sha1' },
              { text: 'How To SHA256', link: '/guides/how_to_sha256' },
              { text: 'How To Plist', link: '/guides/how_to_plist' }
            ]
          }
        ]
      },
      {
                text: '🛠️ Standalone Tools',
        collapsed: true,
        items: [
          { text: 'Microsoft Office Repair Tools', link: '/microsoft_office_repair_tools' },
          { text: 'Community Scripts', link: '/community_scripts' }
        ]
      },
      {
        text: '💻 MacOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/macos_appstore_current_version' },
          { text: 'Raw Feeds', link: '/macos_raw_feeds' }
        ]
      },
      {
        text: '📱 iOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/ios_appstore_current_version' },
          { text: 'Raw Feeds', link: '/ios_raw_feeds' }
        ]
      },
      {
        text: 'ℹ️ About & Support',
        collapsed: true,
        items: [
          { text: '📖 About', link: '/about' },
          { text: '📝 Feedback', link: '/feedback' },
          { text: '👥 Meet The Team', link: '/team' },
          { text: '🐞 Report Issues', link: '/report_issue' },
          { text: '🆕 Changelog', link: '/changelog' },
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/cocopuff2u/MOFA' },
      { icon: 'buymeacoffee', link: 'https://buymeacoffee.com/cocopuff2u' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024 MOFA All rights reserved.'
    },
    markdown: {
      // Ensure HTML is enabled in markdown options
      html: true,
    }
  }
})
