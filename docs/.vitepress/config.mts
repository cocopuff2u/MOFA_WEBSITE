import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "MOFA",
  description: "Microsoft Overview For Apple",
  themeConfig: {
    lastUpdated: true,
    logo: '/images/logo_Mofa_NoBackground.png', 
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Standalone Apps', link: '/readme_standalone_main' },
      { text: 'MacOS AppStore', link: '/readme_macos_appstore_latest' },
      { text: 'iOS AppStore', link: '/api-test' }
    ],
    sidebar: [
      {
        text: '📦 Standalone Apps',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/readme_standalone_main' },
          { text: 'Update History', link: '/readme_standalone_update_history' },
          { text: 'CVE (Vulnerabilities)', link: '/api-test' },
          { text: 'SHA1 & SHA256 Hashes', link: '/api-test' },
          { text: 'Tools & Scripts  ', link: '/api-test' },
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
