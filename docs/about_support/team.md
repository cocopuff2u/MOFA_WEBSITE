---
title: Our Team
editLink: false
lastUpdated: true
---
<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [{"avatar": "https://avatars.githubusercontent.com/u/95243190?s=96&v=4", "name": "Cody Keats", "title": "Lead Developer · 35,978 commits", "desc": "Started MOFA and keeps the feeds, site and tooling running.", "links": [{"icon": "github", "link": "https://github.com/cocopuff2u"}, {"icon": "linkedin", "link": "https://linkedin.com/in/cody-keats"}, {"icon": "slack", "link": "https://macadmins.org/slack"}]}]

const members2 = [{"avatar": "https://avatars.githubusercontent.com/u/128184015?v=4", "name": "npc137", "title": "6 commits", "links": [{"icon": "github", "link": "https://github.com/npc137"}]}, {"avatar": "https://avatars.githubusercontent.com/u/3985769?v=4", "name": "Theile", "title": "5 commits", "links": [{"icon": "github", "link": "https://github.com/Theile"}]}, {"avatar": "https://avatars.githubusercontent.com/u/122827777?v=4", "name": "OasisMcFly", "title": "2 commits", "links": [{"icon": "github", "link": "https://github.com/OasisMcFly"}]}, {"avatar": "https://avatars.githubusercontent.com/u/91097104?v=4", "name": "darixn", "title": "1 commit", "links": [{"icon": "github", "link": "https://github.com/darixn"}]}, {"avatar": "https://avatars.githubusercontent.com/u/2012985?v=4", "name": "gilburns", "title": "1 commit", "links": [{"icon": "github", "link": "https://github.com/gilburns"}]}, {"avatar": "https://avatars.githubusercontent.com/u/618055?v=4", "name": "rtrouton", "title": "1 commit", "links": [{"icon": "github", "link": "https://github.com/rtrouton"}]}]
</script>

<div class="team-page">

<div class="team-head">
  <MofaMark :size="84" />
  <h1>Meet the <span class="gradient-title">MOFA</span> team</h1>
  <p>MOFA is built and maintained in the open by Mac admins, for Mac admins. Everyone below has shipped something that made the project better.</p>
</div>

## Core team {.team-h2}

<VPTeamMembers size="medium" :members="members" />

## Contributors <Badge type="tip" text="6" /> {.team-h2}
<p class="team-sub">Pulled automatically from the <a href="https://github.com/cocopuff2u/MOFA/graphs/contributors" target="_blank" rel="noopener">MOFA repository</a>, newest commits first.</p>

<VPTeamMembers size="small" :members="members2" />

## Want to join? {.team-h2}
<p class="team-sub">You don't need to be a developer. These are the areas where help makes the biggest difference right now.</p>

<div class="mofa-rows team-rows">
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA_WEBSITE" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>Guides for App Store apps</b><span>Write or improve guides for the macOS and iOS App Store sections.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><circle cx="6" cy="4" r="2"/><circle cx="18" cy="4" r="2"/><circle cx="12" cy="20" r="2"/><path d="M6 6v2a4 4 0 0 0 4 4h4a4 4 0 0 0 4-4V6M12 12v6"/></svg></i><div><b>Raw data feeds</b><span>Add new Microsoft sources or make the existing feeds more accurate.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA_WEBSITE/issues" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg></i><div><b>Website features</b><span>Suggest or build features for the site itself. Open an issue to start.</span></div></a>
</div>

<p class="team-foot">The data behind MOFA lives at <a href="https://github.com/cocopuff2u/mofa" target="_blank" rel="noopener">github.com/cocopuff2u/mofa</a> and this website at <a href="https://github.com/cocopuff2u/mofa_website" target="_blank" rel="noopener">github.com/cocopuff2u/mofa_website</a>. Fork either, open an issue, or send a pull request.</p>

<p class="team-note">This page is generated automatically from GitHub by <a href="https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts" target="_blank" rel="noopener">a script</a>. To change it, change the script.</p>

</div>
