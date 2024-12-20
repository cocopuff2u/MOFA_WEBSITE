import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "MOFA",
  description: "Microsoft Overview For Apple",
  themeConfig: {
    lastUpdated: true,
    cleanUrls: true,
    search: {
      provider: 'local'
    },
    editLink: {
      pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    logo: '/images/logo_Mofa_NoBackground.png', 
    nav: [ 
      { text: 'Home', link: '/' },
      { text: 'Standalone Apps', link: '/readme_standalone_main' },
      { text: 'MacOS AppStore', link: '/readme_macos_appstore_latest' },
      { text: 'iOS AppStore', link: '/api-test' }
    ],
    sidebar: [
      {
      items: [
        { text: 'Home', link: '/readme_home' }
      ]
      },
      {
        text: '📦 Standalone Apps',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/readme_standalone_main' },
          {
            text: 'SHA Hashes',
            collapsed: true,
            items: [
              { text: 'SHA1 Hash', link: '/readme_standalone_sha1' },
              { text: 'SHA256 Hash', link: '/readme_standalone_sha256' }
            ]
          },
          { text: 'Update History', link: '/readme_standalone_update_history' },
          { text: 'CVE (Vulnerabilities)', link: '/readme_standalone_cve_history' },
          { text: 'Tools & Scripts', link: '/readme_standalone_tools' }
        ]
      },
      {
        text: '📦 Standalone Guides',
        collapsed: true,
        items: [
          {
            text: 'Mobile Device Management',
            collapsed: true,
            items: [
              { text: 'MDM Overview', link: '/readme_placeholder' },
              { text: 'Configuration Guide', link: '/readme_placeholder' }
            ]
          },
          {
            text: 'Installation Guides',
            collapsed: true,
            items: [
              { text: 'Windows Install', link: '/readme_placeholder' },
              { text: 'MacOS Install', link: '/readme_placeholder' }
            ]
          }
        ]
      },
      {
        text: '💻 MacOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/markdown-examples' },
          { text: 'Update History', link: '/api-examples' },
          { text: 'TEST', link: '/api-test' }
        ]
      },
      {
        text: '📱 iOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/markdown-examples' },
          { text: 'Update History', link: '/api-examples' },
          { text: 'TEST', link: '/api-test' }
        ]
      },
      {
        text: 'ℹ️ About & Support',
        collapsed: true,
        items: [
          { text: '📖 About', link: '/readme_about' },
          { text: '📝 Feedback', link: '/readme_feedback' },
          { text: '👥 Meet The Team', link: '/readme_team' },
          { text: '🐞 Report Issues', link: '/readme_report_issue' },
          { text: '🆕 Changelog', link: '/readme_changelog' },
        ]
      }
    ],
    search: {
      provider: 'local'
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/cocopuff2u/MOFA' }
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
