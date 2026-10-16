<script setup lang="ts">
// "Live from the feed": the newest versions from each source, read from the raw data the
// hourly workflow pulls. Rebuilt on every deploy, so it is always current. The three lists
// are computed at build time; only the selected tab is client state.
import { ref } from 'vue'
import standalone from '../../../../repo_raw_data/macos_standalone_latest.json'
import macAppStore from '../../../../repo_raw_data/macos_appstore_latest.json'
import iosAppStore from '../../../../repo_raw_data/ios_appstore_latest.json'

type StandalonePkg = { name: string; short_version: string; last_updated: string; min_os: string }
type StorePkg = {
  application_name: string; bundleId: string; version: string
  currentVersionReleaseDate: string; minimumOsVersion: string; icon_image: string
}
type Item = { key: string; name: string; version: string; date: string; os: string; icon: string }
type Source = { id: string; tab: string; os: string; meta: string; allHref: string; items: Item[] }

const standaloneIcons: Record<string, string> = {
  'Word': 'MSWD_512x512x32.png',
  'Excel': 'XCEL_512x512x32.png',
  'PowerPoint': 'PPT3_512x512x32.png',
  'Outlook': 'Outlook_512x512x32.png',
  'OneNote': 'OneNote_512x512x32.png',
  'Teams': 'teams_512x512x32.png',
  'Defender For Endpoint': 'defender_512x512x32.png',
  'Windows App': 'windowsapp.png',
  'Intune': 'companyportal.png',
  'Copilot': 'Copilot.png',
  'MAU': 'autoupdate.png',
  'Microsoft Office Suite': 'Office_Suite.webp'
}

// Local icons for App Store apps, keyed by display label. Anything not listed falls back to
// the icon Apple serves in the feed.
const storeIcons: Record<string, string> = {
  'Word': 'MSWD_512x512x32.png',
  'Excel': 'XCEL_512x512x32.png',
  'PowerPoint': 'PPT3_512x512x32.png',
  'Outlook': 'Outlook_512x512x32.png',
  'OneNote': 'OneNote_512x512x32.png',
  'OneDrive': 'OneDrive_512x512x32.png',
  'Teams': 'teams_512x512x32.png',
  'Defender': 'defender_512x512x32.png',
  'Windows App': 'windowsapp.png',
  'Company Portal': 'companyportal.png',
  'Copilot': 'Copilot.png',
  'Edge': 'edge_app.png',
  'Azure': 'azure.png',
  'Skype for Business': 'skype_for_business.png'
}

// Newest first. The feeds only carry a date, so same-day releases tie; ties are broken by
// this fixed order (the core apps first), then alphabetically, so the strip is predictable.
const priority = ['Office Suite', 'Word', 'Excel', 'PowerPoint', 'Outlook', 'OneNote', 'Teams']
const rank = (n: string) => { const i = priority.indexOf(n); return i === -1 ? priority.length : i }
const newest = (items: Item[]) => items
  .sort((a, b) => Date.parse(b.date) - Date.parse(a.date) || rank(a.name) - rank(b.name) || a.name.localeCompare(b.name))
  .slice(0, 6)

const trimVersion = (v: string) => v.replace(/\s*\(.*\)$/, '')
const trimOs = (v: string) => v.replace(/\.0$/, '')
const shortDate = (d: string) => {
  const t = Date.parse(d)
  return isNaN(t) ? d : new Date(t).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

const standaloneLabel = (n: string) =>
  n === 'Microsoft Office Suite' ? 'Office Suite' : n === 'Defender For Endpoint' ? 'Defender' : n === 'MAU' ? 'AutoUpdate' : n

const storeLabel = (n: string) => {
  const special: Record<string, string> = {
    'Microsoft Defender: Security': 'Defender',
    'Windows App Mobile': 'Windows App',
    'Intune Company Portal': 'Company Portal'
  }
  return special[n] ?? n.replace(/^Microsoft\s+/, '')
}

// The App Store feeds include a few third-party apps and the iOS feed repeats some entries,
// so keep Microsoft bundle IDs (plus Viva Engage, whose bundle ID is not namespaced) and
// dedupe on bundle ID.
const storeItems = (pkgs: StorePkg[]): Item[] => {
  const seen = new Set<string>()
  const out: Item[] = []
  for (const p of pkgs) {
    const isMicrosoft = p.bundleId.startsWith('com.microsoft') || p.application_name === 'Viva Engage'
    if (!isMicrosoft || seen.has(p.bundleId)) continue
    seen.add(p.bundleId)
    const name = storeLabel(p.application_name)
    out.push({
      key: p.bundleId, name, version: p.version, date: p.currentVersionReleaseDate,
      os: trimOs(p.minimumOsVersion),
      icon: storeIcons[name] ? '/images/' + storeIcons[name] : p.icon_image
    })
  }
  return out
}

const sources: Source[] = [
  {
    id: 'standalone', tab: 'Standalone', os: 'macOS',
    meta: 'Pulled from Microsoft ' + standalone.last_updated,
    allHref: '/standalone_apps/standalone_current_version_en',
    items: newest((standalone.packages as StandalonePkg[])
      .filter(p => standaloneIcons[p.name])
      .map(p => ({
        key: p.name, name: standaloneLabel(p.name), version: trimVersion(p.short_version),
        date: p.last_updated, os: trimOs(p.min_os), icon: '/images/' + standaloneIcons[p.name]
      })))
  },
  {
    id: 'macos', tab: 'Mac App Store', os: 'macOS',
    meta: 'Pulled from the App Store ' + macAppStore.last_updated,
    allHref: '/macos_appstore/macos_appstore_current_version',
    items: newest(storeItems(macAppStore.packages as StorePkg[]))
  },
  {
    id: 'ios', tab: 'iOS App Store', os: 'iOS',
    meta: 'Pulled from the App Store ' + iosAppStore.last_updated,
    allHref: '/ios_appstore/ios_appstore_current_version',
    items: newest(storeItems(iosAppStore.packages as StorePkg[]))
  }
]

const active = ref(sources[0])
// The first paint waits for the hero animation; later tab switches should feel instant.
const switched = ref(false)
const select = (s: Source) => { active.value = s; switched.value = true }
const delay = (i: number) => ((switched.value ? 0 : 0.55) + i * 0.05) + 's'
</script>

<template>
  <section class="mofa-live">
    <div class="mofa-live-head">
      <span class="mofa-live-dot"></span>
      <span class="mofa-live-title">Recently updated</span>
      <div class="mofa-live-tabs" role="tablist" aria-label="Version source">
        <button
          v-for="s in sources"
          :key="s.id"
          type="button"
          role="tab"
          :aria-selected="s.id === active.id"
          :class="{ on: s.id === active.id }"
          @click="select(s)"
        >{{ s.tab }}</button>
      </div>
      <span class="mofa-live-meta">{{ active.meta }}</span>
      <a class="mofa-live-all" :href="active.allHref">All versions →</a>
    </div>
    <div class="mofa-live-grid">
      <a
        v-for="(p, i) in active.items"
        :key="active.id + ':' + p.key"
        class="mofa-live-item"
        :style="{ animationDelay: delay(i) }"
        :href="active.allHref"
      >
        <img :src="p.icon" :alt="p.name" loading="lazy" width="36" height="36" />
        <div class="mofa-live-text">
          <b>{{ p.name }}</b>
          <span class="v">{{ p.version }}</span>
          <span class="d">{{ shortDate(p.date) }} · {{ active.os }} {{ p.os }}+</span>
        </div>
      </a>
    </div>
  </section>
</template>

<style>
.mofa-live { max-width: 1152px; margin: 0 auto; padding: 0 24px; }
.mofa-live-head {
  display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
  padding: 0 6px 12px; border-bottom: 1px solid var(--vp-c-divider);
  font-size: 13px; color: var(--vp-c-text-2);
}
.mofa-live-dot {
  width: 8px; height: 8px; border-radius: 50%; background: var(--mofa-leaf);
  box-shadow: 0 0 0 0 rgba(111, 137, 11, 0.5); animation: mofa-pulse 2.4s ease-out infinite;
}
.mofa-live-title { font-family: var(--mofa-display-font); font-weight: 700; font-size: 16px; color: var(--vp-c-text-1); letter-spacing: 0.01em; }
.mofa-live-tabs {
  display: inline-flex; gap: 2px; padding: 2px; border-radius: 999px;
  background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider);
}
.mofa-live-tabs button {
  appearance: none; border: 0; background: transparent; cursor: pointer;
  padding: 3px 10px; border-radius: 999px; font: inherit; font-size: 12px; font-weight: 500;
  color: var(--vp-c-text-2); line-height: 1.4; transition: background 0.2s, color 0.2s;
}
.mofa-live-tabs button:hover { color: var(--vp-c-text-1); }
.mofa-live-tabs button.on { background: var(--vp-c-bg); color: var(--vp-c-brand-1); box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08); }
.mofa-live-all { margin-left: auto; color: var(--vp-c-brand-1); font-weight: 500; text-decoration: none !important; }
.mofa-live-grid {
  display: grid; grid-template-columns: repeat(6, 1fr); gap: 4px 8px; padding: 10px 0 12px;
  border-bottom: 1px solid var(--vp-c-divider);
}
.mofa-live-item {
  display: flex; gap: 10px; align-items: center; padding: 10px 6px; border-radius: 12px;
  color: var(--vp-c-text-1); text-decoration: none !important; min-width: 0;
  opacity: 0; transform: translateY(10px); animation: mofa-rise 0.5s ease forwards;
  transition: background 0.2s, transform 0.2s;
}
.mofa-live-item:hover { background: var(--vp-c-bg-soft); }
.mofa-live-item img { width: 40px; height: 40px; flex: none; border-radius: 9px; }
.mofa-live-text { display: flex; flex-direction: column; min-width: 0; line-height: 1.25; }
.mofa-live-text b { font-size: 13px; font-weight: 600; }
.mofa-live-text .v { font-family: var(--vp-font-family-mono); font-size: 11.5px; color: var(--vp-c-brand-1); word-break: break-all; }
.mofa-live-text .d { font-size: 11.5px; color: var(--vp-c-text-2); }
@keyframes mofa-pulse { 0% { box-shadow: 0 0 0 0 rgba(111, 137, 11, 0.5); } 100% { box-shadow: 0 0 0 10px rgba(111, 137, 11, 0); } }
@media (max-width: 1100px) { .mofa-live-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 720px) {
  .mofa-live-grid { grid-template-columns: repeat(2, 1fr); gap: 2px 4px; }
  .mofa-live { padding: 0 16px; }
  .mofa-live-head { font-size: 12px; gap: 8px; }
  .mofa-live-tabs { order: 2; flex-basis: 100%; }
  .mofa-live-tabs button { flex: 1; text-align: center; white-space: nowrap; padding: 3px 6px; }
  .mofa-live-meta { flex-basis: 100%; order: 3; }
  .mofa-live-all { order: 1; }
  .mofa-live-item { padding: 8px 4px; }
}
@media (prefers-reduced-motion: reduce) { .mofa-live-item, .mofa-live-dot { animation: none; opacity: 1; transform: none; } }
</style>
