<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/95243190?s=96&v=4',
    name: 'Cody Keats',
    title: 'Lead Developer',
    links: [
      { icon: 'github', link: 'https://github.com/cocopuff2u' },
      { icon: 'linkedin', link: 'https://linkedin.com/in/cody-keats' },
      { icon: 'slack', link: 'https://macadmins.slack.com/' }
    ]
  },
  {
    avatar: 'https://www.example.com/another-avatar.png',
    name: 'Jane Doe',
    title: 'Senior Developer',
    links: [
      { icon: 'github', link: 'https://github.com/janedoe' },
      { icon: 'twitter', link: 'https://twitter.com/janedoe' }
    ]
  },
  {
    avatar: 'https://www.example.com/team-member-avatar.png',
    name: 'John Smith',
    title: 'Product Manager',
    links: [
      { icon: 'github', link: 'https://github.com/johnsmith' },
      { icon: 'twitter', link: 'https://twitter.com/johnsmith' }
    ]
  }
]

const members2 = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/95243190?s=96&v=4',
    name: 'Cody Keats',
    title: 'Lead Developer',
    links: [
      { icon: 'github', link: 'https://github.com/cocopuff2u' },
      { icon: 'linkedin', link: 'https://linkedin.com/in/cody-keats' },
      { icon: 'slack', link: 'https://macadmins.slack.com/' }
    ]
  },
  {
    avatar: 'https://www.example.com/another-avatar.png',
    name: 'Jane Doe',
    title: 'Senior Developer',
    links: [
      { icon: 'github', link: 'https://github.com/janedoe' },
      { icon: 'twitter', link: 'https://twitter.com/janedoe' }
    ]
  },
  {
    avatar: 'https://www.example.com/team-member-avatar.png',
    name: 'John Smith',
    title: 'Product Manager',
    links: [
      { icon: 'github', link: 'https://github.com/johnsmith' },
      { icon: 'twitter', link: 'https://twitter.com/johnsmith' }
    ]
  }
]
</script>

# Our Team

## Core

<VPTeamMembers size="small" :members="members" />

## Contributors
<VPTeamMembers size="small" :members="members2" />
## We Are Looking for More Contributors!

We're always looking for passionate people to contribute to the project. Whether you're a developer, designer, or just someone who loves working on open-source projects, we'd love to have you! Check out the [contributing guidelines](CONTRIBUTING.md) to get started.

If you're interested in contributing, feel free to open an issue or submit a pull request. Let's make something great together! 🚀
