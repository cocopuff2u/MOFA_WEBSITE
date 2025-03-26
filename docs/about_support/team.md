<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [{"login": "cocopuff2u", "name": "Cody Keats", "title": "✨ Lead Developer ✨", "links": [{"icon": "github", "link": "https://github.com/cocopuff2u"}, {"icon": "linkedin", "link": "https://linkedin.com/in/cody-keats"}, {"icon": "slack", "link": "https://macadmins.slack.com/"}]}]

const members2 = [{"avatar": "https://avatars.githubusercontent.com/u/3985769?v=4", "name": "Theile", "title": "🌟 Contributor", "links": [{"icon": "github", "link": "https://github.com/Theile"}]}, {"avatar": "https://avatars.githubusercontent.com/u/91097104?v=4", "name": "darixn", "title": "🌟 Contributor", "links": [{"icon": "github", "link": "https://github.com/darixn"}]}, {"avatar": "https://avatars.githubusercontent.com/u/2012985?v=4", "name": "gilburns", "title": "🌟 Contributor", "links": [{"icon": "github", "link": "https://github.com/gilburns"}]}, {"avatar": "https://avatars.githubusercontent.com/u/618055?v=4", "name": "rtrouton", "title": "🌟 Contributor", "links": [{"icon": "github", "link": "https://github.com/rtrouton"}]}]
</script>

# 👥 Our Team

## 🌟 Core Developers 🌟

<VPTeamMembers size="medium" :members="members" />

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
