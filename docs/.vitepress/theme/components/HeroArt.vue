<script setup lang="ts">
// Landing-page hero art: the MOFA mark with one API source feeding into it.
// Pure SVG + CSS; honours prefers-reduced-motion via the global stylesheet.
const routes = [
  'M20 160H40L62 138V117H77',              // into the apple, from the left
  'M20 160H40L62 182V207H73',              // into the lower-left tile, from the left
  'M20 160H30V62L50 42H187L207 62V73',     // over the top, into the upper-right tile
  'M20 160H30V258L50 278H187L207 258V247'  // under the bottom, into the lower-right tile
]
const speeds = ['', 'fast', 'slow', 'slow']
const delays = [0, 0.6, 1.1, 1.7]
</script>

<template>
  <div class="mofa-hero-art" aria-hidden="true">
    <svg class="mofa-net" viewBox="0 0 320 320">
      <path v-for="(d, i) in routes" :key="'t' + i" class="trace" :d="d" />
      <path
        v-for="(d, i) in routes"
        :key="'l' + i"
        class="lane"
        :class="speeds[i]"
        :d="d"
        :style="{ animationDelay: delays[i] + 's' }"
      />
      <circle class="srcring" cx="20" cy="160" r="7" />
      <circle class="srcdot" cx="20" cy="160" r="3" />
      <circle class="via" cx="40" cy="160" r="2.4" />
      <circle class="via" cx="62" cy="138" r="2.4" />
      <circle class="via" cx="62" cy="182" r="2.4" />
      <circle class="via" cx="30" cy="62" r="2.4" />
      <circle class="via" cx="30" cy="258" r="2.4" />
      <circle class="pad" cx="77" cy="117" r="4" />
      <circle class="pad" cx="73" cy="207" r="4" />
      <circle class="pad" cx="207" cy="73" r="4" />
      <circle class="pad" cx="207" cy="247" r="4" />
    </svg>

    <svg class="mofa-logo" viewBox="0 0 256 256" role="img" aria-label="MOFA">
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
  </div>
</template>

<style>
.mofa-hero-art {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  /* routes reach further left than right, so nudge the piece right to centre its visual mass */
  transform: translateX(6%);
}
.mofa-hero-art svg {
  position: absolute;
  overflow: visible;
}
.mofa-hero-art .mofa-net {
  /* 1.44x the logo so the routes have room around it */
  inset: -22%;
  width: 144%;
  height: 144%;
}
.mofa-hero-art .mofa-logo {
  width: 100%;
  height: 100%;
}

/* colours come from the theme so light/dark just work */
.mofa-logo .tile { fill: var(--mofa-t2); }
.mofa-logo .tile.a { fill: var(--mofa-t1); }
.mofa-logo .tile.c { fill: var(--mofa-t3); }
.mofa-logo .body { fill: var(--mofa-apple); }
.mofa-logo .dimple { stroke: var(--mofa-apple-dark); }
.mofa-logo .stem { stroke: var(--mofa-stem); }
.mofa-logo .leaf { fill: var(--mofa-leaf); }

.mofa-net .trace { fill: none; stroke: var(--mofa-trace); stroke-width: 1.8; }
.mofa-net .lane {
  fill: none;
  stroke: var(--mofa-t1);
  stroke-width: 3;
  stroke-linecap: round;
  stroke-dasharray: 12 120;
  animation: mofa-travel 3.2s linear infinite;
}
.mofa-net .lane.slow { stroke-dasharray: 8 150; animation: mofa-travel-slow 4.6s linear infinite; }
.mofa-net .lane.fast { stroke-dasharray: 16 100; animation: mofa-travel-fast 2.4s linear infinite; }
.mofa-net .srcring { fill: none; stroke: var(--mofa-t1); stroke-width: 2.4; }
.mofa-net .srcdot { fill: var(--mofa-apple); }
.mofa-net .via { fill: var(--mofa-trace); }
.mofa-net .pad { fill: var(--vp-c-bg); stroke: var(--mofa-trace-strong); stroke-width: 2; }

/* entrance: tiles slide into the grid, apple drops in, leaf nods now and then */
.mofa-logo .tile {
  opacity: 0;
  transform-box: fill-box;
  transform-origin: center;
  animation: mofa-slidein 0.4s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
}
.mofa-logo .tile.a { --dx: 40px; --dy: -40px; animation-delay: 0s; }
.mofa-logo .tile.b { --dx: -40px; --dy: 40px; animation-delay: 0.07s; }
.mofa-logo .tile.c { --dx: 40px; --dy: 40px; animation-delay: 0.14s; }
.mofa-logo .apple {
  opacity: 0;
  transform-box: fill-box;
  transform-origin: center;
  animation: mofa-drop 0.45s 0.25s cubic-bezier(0.3, 1.4, 0.4, 1) forwards;
}
.mofa-logo .leaf {
  transform-box: fill-box;
  transform-origin: left bottom;
  animation: mofa-nod 4s 0.9s ease-in-out infinite;
}
.mofa-net { opacity: 0; animation: mofa-fadein 0.5s 0.4s ease forwards; }

@keyframes mofa-slidein { from { opacity: 0; transform: translate(var(--dx), var(--dy)); } to { opacity: 1; transform: none; } }
@keyframes mofa-drop { from { opacity: 0; transform: translateY(-70px) scale(0.9); } to { opacity: 1; transform: none; } }
@keyframes mofa-nod { 0%, 80%, 100% { transform: rotate(0); } 88% { transform: rotate(-10deg); } 94% { transform: rotate(6deg); } }
@keyframes mofa-fadein { to { opacity: 1; } }
@keyframes mofa-travel { from { stroke-dashoffset: 0; } to { stroke-dashoffset: -132; } }
@keyframes mofa-travel-slow { from { stroke-dashoffset: 0; } to { stroke-dashoffset: -158; } }
@keyframes mofa-travel-fast { from { stroke-dashoffset: 0; } to { stroke-dashoffset: -116; } }

/* Narrow screens: VitePress stacks the art above the text, so keep the whole piece inside its
   box. Logo at 69.4% with the trace layer at 100% keeps the same 1.44 ratio, so the pins still land. */
@media (max-width: 959px) {
  .mofa-hero-art { transform: none; }
  .mofa-hero-art .mofa-net { inset: 0; width: 100%; height: 100%; }
  .mofa-hero-art .mofa-logo { width: 69.4%; height: 69.4%; }
}

@media (prefers-reduced-motion: reduce) {
  .mofa-hero-art * { animation: none !important; opacity: 1 !important; transform: none !important; }
}
</style>
