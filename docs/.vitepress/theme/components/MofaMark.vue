<script setup lang="ts">
// Inline MOFA mark for content pages: themed colours, a quiet leaf nod, and a lift on hover.
withDefaults(defineProps<{ size?: number }>(), { size: 150 })
</script>

<template>
  <span class="mofa-mark" :style="{ width: size + 'px', height: size + 'px' }">
    <svg viewBox="0 0 256 256" role="img" aria-label="MOFA">
      <rect class="tile a" x="136" y="28" width="92" height="92" rx="18" />
      <rect class="tile b" x="28" y="136" width="92" height="92" rx="18" />
      <rect class="tile c" x="136" y="136" width="92" height="92" rx="18" />
      <g transform="translate(0 -8)"><g class="apple">
        <path class="body" d="M74 52C66 40 42 38 32 60C22 82 28 108 44 120C56 129 66 122 74 122C82 122 92 129 104 120C120 108 126 82 116 60C106 38 82 40 74 52Z" />
        <path class="dimple" d="M62 52Q74 60 86 52" fill="none" stroke-width="4" stroke-linecap="round" />
        <path class="stem" d="M74 54Q72 42 80 32" fill="none" stroke-width="5" stroke-linecap="round" />
        <path class="leaf" d="M78 44C80 30 94 22 110 26C106 42 92 50 78 44Z" />
      </g></g>
    </svg>
  </span>
</template>

<style>
.mofa-mark {
  display: inline-block;
  position: relative;
  opacity: 0;
  animation: mofa-mark-in 0.5s 0.05s cubic-bezier(0.2, 0.7, 0.2, 1) forwards;
  transition: transform 0.35s cubic-bezier(0.2, 0.7, 0.2, 1), filter 0.35s;
  filter: drop-shadow(0 10px 22px rgba(4, 102, 114, 0.18));
}
.mofa-mark:hover { transform: translateY(-6px) rotate(-2deg); filter: drop-shadow(0 18px 30px rgba(4, 102, 114, 0.26)); }
.dark .mofa-mark { filter: drop-shadow(0 10px 22px rgba(95, 196, 207, 0.14)); }
.dark .mofa-mark:hover { filter: drop-shadow(0 18px 30px rgba(95, 196, 207, 0.22)); }
.mofa-mark svg { width: 100%; height: 100%; overflow: visible; display: block; }
.mofa-mark .tile { fill: var(--mofa-t2); }
.mofa-mark .tile.a { fill: var(--mofa-t1); }
.mofa-mark .tile.c { fill: var(--mofa-t3); }
.mofa-mark .body { fill: var(--mofa-apple); }
.mofa-mark .dimple { stroke: var(--mofa-apple-dark); }
.mofa-mark .stem { stroke: var(--mofa-stem); }
.mofa-mark .leaf {
  fill: var(--mofa-leaf);
  transform-box: fill-box;
  transform-origin: left bottom;
  animation: mofa-nod 4s 1s ease-in-out infinite;
}
@keyframes mofa-mark-in { from { opacity: 0; transform: translateY(10px) scale(0.96); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) {
  .mofa-mark, .mofa-mark .leaf { animation: none; opacity: 1; transform: none; }
}
</style>
