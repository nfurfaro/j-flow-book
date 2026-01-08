# Configuration Reference

All `.jflow.toml` options explained.

## Config Hierarchy

jflow loads configuration in this order (later values override earlier):

1. **Built-in defaults** - sensible starting values
2. **Global config** (`~/.jflow.toml`) - your personal defaults
3. **Local config** (`.jflow.toml` in repo) - project-specific overrides

This means you can set your preferred theme and push style globally, then override just the primary branch for specific projects.

## Full Example

```toml
[remote]
name = "origin"
primary = "main"

[github]
push_style = "squash"
merge_style = "squash"
stack_context = true

[display]
theme = "catppuccin"
icons = "unicode"
show_commit_ids = false

[bookmarks]
prefix = ""
```

## Sections

### [remote]

Remote repository settings.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | string | `"origin"` | Name of the Git remote |
| `primary` | string | `"main"` | Primary branch name (also accepts `trunk` as alias) |

**Branch resolution:**

jflow resolves the primary branch reference in this order:
1. `primary@remote` (e.g., `main@origin`) - the remote tracking branch
2. `primary` (local) - if remote doesn't exist
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

### [display]

Display and theming settings.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `theme` | string | `"catppuccin"` | Color theme |
| `icons` | string | `"unicode"` | Icon set |
| `show_commit_ids` | bool | `false` | Show git commit hashes |

**Available themes:** `catppuccin`, `nord`, `dracula`, `default`

**Available icon sets:** `unicode`, `ascii`, `nerdfont`

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

## File Locations

### Global Config

Location: `~/.jflow.toml`

Set your personal defaults here. These apply to all repositories unless overridden.

### Local Config

jflow looks for `.jflow.toml` in:
1. Current directory
2. Parent directories (up to repository root)

Local config values override global config.

## Creating a Config

### Interactive Setup

```bash
jf init
```

Guides you through configuration with prompts. Skips if global config already exists.

### Quick Setup

```bash
jf init --defaults
```

Creates config with sensible defaults.

### Force Local Config

```bash
jf init --local
```

Creates local `.jflow.toml` even if global config exists.

### Manual

Create `.jflow.toml` manually with your preferred settings.

## Backward Compatibility

The `trunk` field name is accepted as an alias for `primary`:

```toml
[remote]
trunk = "main"  # Works, but 'primary' is preferred
```
