// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import HeroArt from './components/HeroArt.vue'
import LatestVersions from './components/LatestVersions.vue'
import MofaMark from './components/MofaMark.vue'
import PackageJump from './components/PackageJump.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
      'home-hero-image': () => h(HeroArt),
      'aside-outline-before': () => h(PackageJump)
    })
  },
  enhanceApp({ app }) {
    app.component('LatestVersions', LatestVersions)
    app.component('MofaMark', MofaMark)
  }
} satisfies Theme
