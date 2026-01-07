# jf init

Initialize jflow in a Jujutsu repository.

## Usage

```bash
jf init              # Interactive setup
jf init --defaults   # Use auto-detected defaults
jf init --github     # Create GitHub repo and initialize
```

## Options

| Option | Description |
|--------|-------------|
| `-d, --defaults` | Skip prompts, use detected/default values |
| `--github` | Create a GitHub repository (uses `gh` CLI) |

## What It Does

1. Detects your main branch (main/master) and remote (origin)
2. Prompts for configuration (or uses defaults with `-d`)
3. Creates `.jflow.toml` config file
4. Optionally creates a GitHub repository with `--github`

## Examples

### Basic initialization

```bash
cd my-jj-project
jf init
```

You'll be prompted for:
- Main branch name (detected: main)
- Remote name (detected: origin)
- Push style (squash or append)
- Bookmark prefix (optional)

### Quick setup with defaults

```bash
jf init --defaults
```

Uses auto-detected values without prompting.

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
trunk = "main"

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
