# Introduction

Welcome to **jflow** - a beautiful, radically simple workflow tool for [Jujutsu](https://github.com/martinvonz/jj) version control.

## What is jflow?

jflow is a command-line tool that makes working with stacked changes in Jujutsu and GitHub effortless. It provides:

- **Beautiful visualization** of your commit stack with sync state
- **Simple commands** for common workflows
- **Automatic bookmark management**
- **Smart defaults** that just work
- **GitHub integration** via gh CLI

## Why jflow?

### The Problem

Working with Jujutsu and GitHub PRs involves managing bookmarks (branches), keeping them in sync after rebases, and maintaining clean stacks of changes. This requires multiple manual steps:

```bash
# Without jflow
jj edit <change-id>
# make changes...
jj bookmark set my-feature
jj git push --bookmark my-feature --force
# Repeat for each bookmark...
```

### The Solution

jflow automates this workflow:

```bash
# With jflow
jj edit <change-id>
# make changes...
jf push  # Updates ALL bookmarks and PRs automatically!
```

## Core Philosophy

**Query, don't track.** jflow has zero state files—it queries jj directly using powerful revsets. Your stack is always `::@ ~ ::main@origin`. Simple.

**Four commands. That's it.**
- `jf` - See your beautiful stack with sync state (same as `jf status`)
- `jf push` - Push and create/update PRs
- `jf land` - Clean up after PRs merge
- `jf pull` - Fetch + rebase

Plus one more for setup:
- `jf init` - Initialize with smart defaults

## Key Features

### Beautiful Output with Sync State

```
╭───────────────── Your Stack (3 commits) ─────────────────╮

  3/3 ●  qwer5678  Add login screen
         jf/login-screen ✓
  │
  2/3 ○  tyui9012  Add backend API
         jf/add-backend-api ↑2 ahead
  │
  1/3 ○  asdf1234  Add REST library
        💡 ready to create PR
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯
```

### Smart Stack Management

- **Position markers** - See where each change is in the stack (1/3, 2/3, 3/3)
- **Sync indicators** - Know if you're ahead, behind, or synced with remote
- **Change IDs** - Stable identifiers that survive rebases
- **Automatic rebasing** - jj handles dependencies automatically

### GitHub Integration

- **Stack context in PRs** - Shows dependencies automatically
- **gh CLI integration** - Create PRs from the command line
- **Push styles** - Squash or append commits based on your preference

## Who Should Use jflow?

jflow is perfect for:

- **Jujutsu users** who work with GitHub
- **Teams** practicing stacked development
- **Developers** who want beautiful tooling
- **Anyone** tired of manual bookmark management

## What's Next?

- Read the [Quick Start](./getting-started/quick-start.md) to get up and running
- Learn about [Commands](./commands/init.md) in detail
- Explore the [Complete Workflow](./guides/complete-workflow.md) guide

Let's make version control beautiful!
