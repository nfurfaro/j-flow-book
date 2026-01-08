# jf init

Initialize jflow in a Jujutsu repository.

## Usage

```bash
jf init              # Interactive setup (skips if global config exists)
jf init --defaults   # Use auto-detected defaults
jf init --local      # Force create local config
jf init --github     # Create GitHub repo and initialize
```

## Options

| Option | Description |
|--------|-------------|
| `-d, --defaults` | Skip prompts, use detected/default values |
| `-l, --local` | Force creating local `.jflow.toml` even if global config exists |
| `--github` | Create a GitHub repository (uses `gh` CLI) |

## What It Does

1. Checks for global config (`~/.jflow.toml`) - if found, jflow is ready to use
2. Detects your primary branch (main/master) and remote (origin)
3. Prompts for configuration (or uses defaults with `-d`)
4. Creates `.jflow.toml` config file
5. Optionally creates a GitHub repository with `--github`

## Examples

### Basic initialization

```bash
cd my-jj-project
jf init
```

If you have a global `~/.jflow.toml`, jflow will use that and skip creating a local config.

You'll be prompted for:
- Primary branch name (detected: main)
- Remote name (detected: origin)
- Push style (squash or append)
- Bookmark prefix (optional)

### Quick setup with defaults

```bash
jf init --defaults
```

Uses auto-detected values without prompting.

### Force local config

```bash
jf init --local
```

Creates a local `.jflow.toml` even if global config exists. Local config values override global settings.

### New project with GitHub

```bash
mkdir my-project
cd my-project
jj git init
jf init --github
```

This will:
1. Create a private GitHub repository named `my-project`
2. Set up `origin` remote pointing to it
3. Push your initial commit as `main`
4. Create `.jflow.toml`

## Generated Config

`jf init` creates `.jflow.toml`:

```toml
# jflow configuration

[remote]
name = "origin"
primary = "main"

[github]
push_style = "squash"
merge_style = "squash"
stack_context = true

[bookmarks]
prefix = ""
```

## Prerequisites

- Must be in a jj repository (`jj git init` first)
- For `--github`: requires [GitHub CLI](https://cli.github.com/) (`gh`) installed and authenticated

## See Also

- [Quick Start](../getting-started/quick-start.md) - Full getting started guide
- [Configuration](../guides/configuration.md) - Config file reference
