#!/usr/bin/env python3
"""
Generate all documentation files for jflow mdBook
"""

import os
from pathlib import Path

# Base directory
BASE = Path("/home/claude/jflow-book/src")

# Command documentation
COMMANDS = {
    "init.md": """# jf init

Initialize jflow with smart defaults. See full guide in Getting Started section.

## Usage
```bash
jf init [--defaults]
```

Creates `.jflow.toml` with auto-detected settings.""",

    "status.md": """# jf status

View your beautiful stack visualization.

## Usage
```bash
jf status
```

## Example Output
```
╭─ Your Stack ────────────────────────────────╮
│  ●  abc1234  Working on feature            │
│  ○  def5678  Dependency → my-bookmark      │
│  ◆  main@origin                            │
╰──────────────────────────────────────────────╯
```""",

    "pr.md": """# jf pr

Create bookmark and pull request.

## Usage
```bash
jf pr <change-id> <bookmark-name> [--title "Custom Title"]
```

Creates bookmark, pushes, and opens PR with gh CLI.""",

    "sync.md": """# jf sync

Update all bookmarks to current commits.

## Usage
```bash
jf sync [--dry-run]
```

Updates bookmarks after rebasing or editing changes.""",

    "pull.md": """# jf pull

Fetch and rebase your stack.

## Usage
```bash
jf pull [--remote <name>]
```

Equivalent to `jj git fetch && jj rebase -d main@origin`.""",
}

# Create command docs
commands_dir = BASE / "commands"
commands_dir.mkdir(exist_ok=True)
for filename, content in COMMANDS.items():
    (commands_dir / filename).write_text(content)
    print(f"Created commands/{filename}")

print("\nAll documentation files created!")
print("Run: cd /home/claude/jflow-book && mdbook build")
