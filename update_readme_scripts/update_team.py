from github import Github
import os

# Excluded users and core team configuration
EXCLUDED_USERS = ['cocopuff2u', 'github-actions[bot]']  # Users to exclude from contributors list

CORE_MEMBERS = [
    {
        'avatar': 'https://avatars.githubusercontent.com/u/95243190?s=96&v=4',
        'name': 'Cody Keats',
        'title': '✨ Lead Developer ✨',
        'links': [
            {'icon': 'github', 'link': 'https://github.com/cocopuff2u'},
            {'icon': 'linkedin', 'link': 'https://linkedin.com/in/cody-keats'},
            {'icon': 'slack', 'link': 'https://macadmins.slack.com/'}
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
    contributors = get_contributors()
    
    markdown = """---
editLink: false
lastUpdated: true
---
<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = ${core_members}

const members2 = ${contributors_list}
</script>

# 👥 Our Team

## 🌟 Core Developers 🌟

<VPTeamMembers size="small" :members="members" />

## 🌈 Contributors 🌈

<VPTeamMembers size="small" :members="members2" />

## 🚀 We Need Contributors! 🛠️

We're always looking for passionate people to contribute to the project. Whether you're a developer, designer, or just someone who loves working on open-source projects, we'd love to have you! 🧑‍💻🌍

### 🧑‍💻 Areas Where We Need Help:
- Adding new guides for MacOS App Store and iOS App Store apps 📱
- Improving & Adding raw data feeds 📊
- Creating more features for the website 🌐

The data powering this project is pulled from the repository [GitHub.com/cocopuff2u/mofa](https://github.com/cocopuff2u/mofa), and the website is hosted in its own repository at [GitHub.com/cocopuff2u/mofa_website](https://github.com/cocopuff2u/mofa_website).

Feel free to fork the repositories and contribute! You can open an issue or submit a pull request once you've made your updates. Let's make something great together! 🎉🚀

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from github. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""
    
    # Format core members for template
    core_members_str = str(CORE_MEMBERS).replace("'", '"')
    
    # Format contributors
    contributors_list = []
    for contributor in contributors:
        if contributor.login not in EXCLUDED_USERS:
            contributor_data = {
                'avatar': contributor.avatar_url,
                'name': contributor.login,
                'title': '🌟 Contributor',
                'links': [
                    {'icon': 'github', 'link': contributor.html_url}
                ]
            }
            contributors_list.append(contributor_data)
    
    contributors_str = str(contributors_list).replace("'", '"')
    
    # Replace placeholders
    markdown = markdown.replace("${core_members}", core_members_str)
    markdown = markdown.replace("${contributors_list}", contributors_str)
    
    # Save to file
    output_path = "docs/about_support/team.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(markdown)
    print(f"Team page generated at: {output_path}")

if __name__ == "__main__":
    generate_team_markdown()
