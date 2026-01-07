# Configuration Reference

All `.jflow.toml` options explained.

## Full Example

```toml
[remote]
name = "origin"
main_branch = "main"

[github]
push_style = "squash"
merge_style = "squash"
stack_context = true

[bookmarks]
prefix = ""
```

## Sections

### [remote]

Remote repository settings.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | string | `"origin"` | Name of the Git remote |
| `main_branch` | string | `"main"` | Main branch name |

**Branch resolution:**

jflow resolves the main branch reference in this order:
1. `main_branch@remote` (e.g., `main@origin`) - the remote tracking branch
2. `main_branch` (local) - if remote doesn't exist
3. `root()` - fallback for brand new repos

### [github]

GitHub integration settings.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `push_style` | string | `"squash"` | How to push updates |
| `merge_style` | string | `"squash"` | How PRs should be merged |
| `stack_context` | bool | `true` | Include stack info in PR descriptions |

**Push styles:**

| Style | Description |
|-------|-------------|
| `squash` | Force-push updates. Simple and clean. |
| `append` | Add incremental commits. Preserves review context. |

**Merge styles:**

| Style | Description |
|-------|-------------|
| `squash` | Squash all commits into one |
| `merge` | Create a merge commit |
| `rebase` | Rebase and merge |

### [bookmarks]

Bookmark naming settings.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `prefix` | string | `""` | Prefix for auto-generated bookmark names |

**Example:** If `prefix = "jf/"` and you push a change with description "Add user auth", the bookmark will be `jf/add-user-auth`.

## Environment Variables

jflow respects standard environment variables:

| Variable | Description |
|----------|-------------|
| `NO_COLOR` | Disable color output |
| `CLICOLOR_FORCE` | Force color output |

## File Location

jflow looks for `.jflow.toml` in:
1. Current directory
2. Parent directories (up to repository root)

If not found, default values are used.

## Creating a Config

### Interactive Setup

```bash
jf init
```

Guides you through configuration with prompts.

### Quick Setup

```bash
jf init --defaults
```

Creates config with sensible defaults.

### Manual

Create `.jflow.toml` manually with your preferred settings.
