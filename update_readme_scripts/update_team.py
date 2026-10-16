from github import Github
import os

# Excluded users and core team configuration
EXCLUDED_USERS = ['cocopuff2u', 'github-actions[bot]']  # Users to exclude from contributors list

CORE_MEMBERS = [
    {
        'login': 'cocopuff2u',   # used to look up the commit count; not rendered
        'avatar': 'https://avatars.githubusercontent.com/u/95243190?s=96&v=4',
        'name': 'Cody Keats',
        'title': 'Lead Developer',
        'desc': 'Started MOFA and keeps the feeds, site and tooling running.',
        'links': [
            {'icon': 'github', 'link': 'https://github.com/cocopuff2u'},
            {'icon': 'linkedin', 'link': 'https://linkedin.com/in/cody-keats'},
            {'icon': 'slack', 'link': 'https://macadmins.org/slack'}
        ]
    }
]

def get_contributors():
    # Initialize Github with access token if available, otherwise use public access
    token = os.getenv('GITHUB_TOKEN')
    g = Github(token) if token else Github()
    
    # Get repository
    repo = g.get_repo("cocopuff2u/MOFA")
    
    # Get contributors
    contributors = repo.get_contributors()
    return contributors

def generate_team_markdown():
    contributors = list(get_contributors())
    
    markdown = """---
title: Our Team
editLink: false
lastUpdated: true
---
<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = ${core_members}

const members2 = ${contributors_list}
</script>

<div class="team-page">

<div class="team-head">
  <MofaMark :size="84" />
  <h1>Meet the <span class="gradient-title">MOFA</span> team</h1>
  <p>MOFA is built and maintained in the open by Mac admins, for Mac admins. Everyone below has shipped something that made the project better.</p>
</div>

## Core team {.team-h2}

<VPTeamMembers size="medium" :members="members" />

## Contributors <Badge type="tip" text="${contributor_count}" /> {.team-h2}
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
"""
    
    # Core members: add their commit count to the title, drop the lookup key
    counts = {c.login: c.contributions for c in contributors}
    core = []
    for m in CORE_MEMBERS:
        m = dict(m)
        n = counts.get(m.pop('login', None))
        if n:
            m['title'] = f"{m['title']} · {n:,} commit{'' if n == 1 else 's'}"
        core.append(m)
    core_members_str = str(core).replace("'", '"')
    
    # Format contributors
    contributors_list = []
    for contributor in contributors:
        if contributor.login not in EXCLUDED_USERS:
            n = contributor.contributions
            contributor_data = {
                'avatar': contributor.avatar_url,
                'name': contributor.login,
                'title': f"{n:,} commit{'' if n == 1 else 's'}",
                'links': [
                    {'icon': 'github', 'link': contributor.html_url}
                ]
            }
            contributors_list.append(contributor_data)
    
    contributors_str = str(contributors_list).replace("'", '"')
    
    # Replace placeholders
    markdown = markdown.replace("${core_members}", core_members_str)
    markdown = markdown.replace("${contributors_list}", contributors_str)
    markdown = markdown.replace("${contributor_count}", str(len(contributors_list)))
    
    # Save to file
    output_path = "docs/about_support/team.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(markdown)
    print(f"Team page generated at: {output_path}")

if __name__ == "__main__":
    generate_team_markdown()
