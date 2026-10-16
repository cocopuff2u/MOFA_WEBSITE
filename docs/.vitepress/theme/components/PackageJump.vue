<script setup lang="ts">
// "On this page" for the generated package pages: the page's sections with each package
// (an <a class="pkg-anchor"> emitted by the Python generators) nested under the section it
// sits in. Highlights the item currently in view. Other pages keep the stock outline.
import { ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { useRoute, useData } from 'vitepress'

type Item = { id: string; label: string; level: number; pkg: boolean }
const route = useRoute()
const { frontmatter } = useData()

// Only pages that set `packageOutline: true` (the generated package pages, which also set
// `outline: false` to drop the stock outline) get this list. Everything else keeps VitePress's own.
function levels(): [number, number] | null {
  return frontmatter.value.packageOutline ? [2, 3] : null
}
const items = ref<Item[]>([])
const active = ref('')
let targets: HTMLElement[] = []
let raf = 0

function headingText(h: HTMLElement) {
  return (h.textContent || '').replace(/[#​]/g, '').replace(/\s+/g, ' ').trim()
}
function collect() {
  const lv = levels()
  if (!lv) { items.value = []; targets = []; return }
  const hs = Array.from({ length: lv[1] - lv[0] + 1 }, (_, i) => `.vp-doc h${lv[0] + i}[id]`)
  const nodes = Array.from(document.querySelectorAll<HTMLElement>([...hs, '.vp-doc a.pkg-anchor[id]'].join(', ')))
  targets = nodes
  let last = lv[0]
  items.value = nodes.map(n => {
    if (n.tagName.startsWith('H')) {
      last = Number(n.tagName[1])
      return { id: n.id, label: headingText(n), level: last - lv[0], pkg: false }
    }
    return { id: n.id, label: n.dataset.label || n.id, level: last - lv[0] + 1, pkg: true }
  })
  update()
}
function update() {
  if (!targets.length) return
  const line = 150
  let cur = targets[0].id
  for (const t of targets) { if (t.getBoundingClientRect().top <= line) cur = t.id; else break }
  active.value = cur
}
function onScroll() { cancelAnimationFrame(raf); raf = requestAnimationFrame(update) }

onMounted(() => { collect(); window.addEventListener('scroll', onScroll, { passive: true }) })
onBeforeUnmount(() => { window.removeEventListener('scroll', onScroll); cancelAnimationFrame(raf) })
watch(() => route.path, () => { nextTick(collect); setTimeout(collect, 300) })
</script>

<template>
  <nav v-if="items.length" class="mofa-outline" aria-label="On this page">
    <p class="mofa-outline-title">On this page</p>
    <ul>
      <li v-for="i in items" :key="i.id" :class="[i.pkg ? 'pkg' : 'section', 'lv' + Math.min(i.level, 3)]">
        <a :href="'#' + i.id" :class="{ active: i.id === active }" :title="i.label">{{ i.label }}</a>
      </li>
    </ul>
  </nav>
</template>

<style>
.mofa-outline { position: relative; }
.mofa-outline-title {
  font-family: var(--mofa-display-font); font-weight: 700; font-size: 14px; line-height: 1.4;
  letter-spacing: 0.01em; color: var(--vp-c-text-1); margin: 0 0 6px;
}
.mofa-outline ul { list-style: none; margin: 0; padding: 0; border-left: 1px solid var(--vp-c-divider); }
.mofa-outline li { margin: 0; padding: 0; }
.mofa-outline a {
  display: block; padding: 4px 0 4px 12px; margin-left: -1px;
  font-size: 13px; line-height: 1.5; color: var(--vp-c-text-2);
  border-left: 2px solid transparent; text-decoration: none !important;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  transition: color 0.2s, border-color 0.2s;
}
.mofa-outline li.lv0 + li.lv0 a { margin-top: 2px; }
.mofa-outline li.lv1 a { padding-left: 24px; font-size: 12.5px; line-height: 1.45; padding-top: 2.5px; padding-bottom: 2.5px; }
.mofa-outline li.lv2 a { padding-left: 36px; font-size: 12px; line-height: 1.4; padding-top: 2px; padding-bottom: 2px; }
.mofa-outline li.lv3 a { padding-left: 48px; font-size: 12px; line-height: 1.4; padding-top: 2px; padding-bottom: 2px; }
.mofa-outline a:hover { color: var(--vp-c-text-1); }
.mofa-outline a.active { color: var(--vp-c-brand-1); border-left-color: var(--vp-c-brand-1); font-weight: 500; }
/* package anchors: zero-size, but land below the sticky nav when jumped to */
.vp-doc a.pkg-anchor { display: block; height: 0; scroll-margin-top: 96px; }
</style>
