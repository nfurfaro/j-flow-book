# Configuration

This guide covers how to configure jflow for your workflow.

## Quick Start

Run `jf init` in your repository:

```bash
jf init           # Interactive setup
jf init -d        # Use defaults
```

If you have a global `~/.jflow.toml`, jflow will use it automatically. Use `jf init --local` to create a project-specific config.

## Global vs Local Config

jflow supports a two-level configuration hierarchy:

### Global Config (`~/.jflow.toml`)

Your personal defaults that apply to all repositories:

```toml
[display]
theme = "nord"
icons = "nerdfont"

[github]
push_style = "append"
```

### Local Config (`.jflow.toml`)

Project-specific settings that override global config:

```toml
[remote]
primary = "develop"  # This project uses 'develop' instead of 'main'
```

## Common Configurations

### Simple Setup

Most users just need:

```toml
[remote]
name = "origin"
primary = "main"
```

### Custom Theme

```toml
[display]
theme = "dracula"      # Options: catppuccin, nord, dracula, default
icons = "nerdfont"     # Options: unicode, ascii, nerdfont
```

### Append-Style Pushes

Preserve review comments by appending commits instead of force-pushing:

```toml
[github]
push_style = "append"
```

### Bookmark Prefix

Namespace your bookmarks:

```toml
[bookmarks]
prefix = "nick/"  # Creates bookmarks like "nick/add-feature"
```

## Full Reference

See [Configuration Reference](../reference/config-reference.md) for all options.
