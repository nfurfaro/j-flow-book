# Quick Start

Get up and running with jflow in 5 minutes!

## 1. Verify Prerequisites

```bash
# Check jj is installed
jj --version

# Check jf is installed
jf --version
```

## 2. Initialize jflow

In your jj repository:

```bash
cd my-jj-project
jf init
```

Follow the prompts or use `jf init --defaults` for quick setup.

This creates `.jflow.toml` with your configuration.

### Starting a new project?

Create a GitHub repo and initialize in one step:

```bash
mkdir my-project && cd my-project
jj git init
jf init --github
```

This creates a private GitHub repo, sets up the remote, and initializes jflow.

## 3. View Your Stack

```bash
jf
```

Output:
```
╭───────────────── Your Stack (1 commit) ─────────────────╮

  1/1 ●  abc1234  Current work
        💡 ready to create PR
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯
```

## 4. Create Some Changes

```bash
jj new -m "Add REST library"
# ... make changes ...

jj new -m "Add API layer"
# ... make changes ...

jj new -m "Add UI component"
# ... make changes ...
```

## 5. View Your Stack Again

```bash
jf
```

Now you'll see all three changes with position markers!

## 6. Push to GitHub

```bash
jf push
```

This:
- Prompts for bookmark names (if needed)
- Creates bookmarks
- Pushes to GitHub
- Creates PRs with stack context

## 7. Edit a Change

```bash
# Edit any change in your stack
jj edit <change-id>
# ... make changes ...
```

## 8. Push Updates

After editing:

```bash
jf push
```

This updates all bookmarks and their PRs automatically.

## 9. After PRs Merge

```bash
jf land
```

This cleans up merged PRs and rebases your remaining stack.

## 10. Pull Latest Changes

```bash
jf pull
```

This fetches from origin and rebases your stack.

## Common Commands

| Command | What it does |
|---------|--------------|
| `jf init` | Initialize jflow in repo |
| `jf init --github` | Create GitHub repo and initialize |
| `jf` | View your stack with sync state |
| `jf push` | Push and create/update PRs |
| `jf land` | Clean up after PRs merge |
| `jf pull` | Fetch + rebase |

## Typical Workflow

```bash
# Morning
jf pull                          # Get latest

# Work (outside-in)
jj new -m "Add core library"
jj new -m "Add API"
jj new -m "Add UI"

# View
jf

# Push all at once
jf push                          # Creates bookmarks and PRs

# Get feedback, edit
jj edit <core-id>
# make changes...

# Push updates
jf push                          # All PRs updated!

# After PRs merge
jf land                          # Clean up

# End of day
jf pull                          # Stay current
```

## Tips

### 1. Use jf Often

```bash
jf
```

Shows what you're working on, sync state, and what has PRs.

### 2. Bookmark Naming

Use descriptive names when prompted:
```
Bookmark name for abc1234 (Add authentication) [skip]: add-user-authentication
```

### 3. Small Changes

Keep changes small and focused:
- ✅ "Add REST client"
- ✅ "Add API endpoint"
- ❌ "Add entire feature"

### 4. Inside-Out Review

Create PRs from bottom of stack up - review dependencies first.

### 5. Check Before Push

```bash
jf push --dry-run            # Preview changes
jf push                      # Actually push
```

## Next Steps

- Learn about each [command](../commands/init.md) in detail
- Read the [complete workflow guide](../guides/complete-workflow.md)
- Understand [stacked changes](../guides/stacked-changes.md)
