# jf status

View your beautiful stack visualization with sync state.

## Usage

```bash
jf              # shorthand (runs status by default)
jf status       # explicit
```

## Example Output

```
╭───────────────── Your Stack (3 commits) ─────────────────╮

  3/3 ●  abc12345  Add login screen
         jf/login-screen ✓
  │
  2/3 ○  def67890  Add API layer
         jf/api-layer ↑2 ahead
  │
  1/3 ○  ghi11111  Add REST library
        💡 ready to create PR
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯

💡 Quick commands:
  💡 Push to GitHub: jf push
  ℹ Update from remote: jf pull
```

## Understanding the Output

### Position Markers

Each change shows its position in the stack:

| Marker | Meaning |
|--------|---------|
| `3/3` | Third change out of 3 total (closest to you) |
| `1/3` | First change (closest to main) |

### Icons

| Icon | Meaning |
|------|---------|
| `●` | Current working copy |
| `○` | Other change in stack |
| `◆` | Main branch |
| `→` | Bookmark indicator |
| `💡` | Ready to create PR |
| `✓` | Synced with remote |

### Sync State Indicators

When a change has a bookmark, the sync state with remote is shown:

| Indicator | Meaning |
|-----------|---------|
| `✓` | Synced with remote (same commit) |
| `(local only)` | Bookmark exists only locally, not pushed |
| `↑N ahead` | Local is N commits ahead of remote |
| `↓N behind` | Local is N commits behind remote |
| Fork diagram | Local and remote have diverged |

### Diverged State

When local and remote have diverged, a visual fork is shown:

```
                 ╭──●──●──●    local (+2)
        hotfix ──○ abc123
                 ╰──○──○──○    origin (+3) ⚠ diverged
```

This shows:
- Local has 2 new commits (green, filled dots)
- Origin has 3 new commits (red, hollow dots)
- They share a common ancestor at `abc123`

## Configuration

### Theme

Set in `.jflow.toml`:

```toml
[display]
theme = "catppuccin"  # or "nord", "dracula"
icons = "unicode"     # or "ascii"
```

### Icon Sets

| Set | Description |
|-----|-------------|
| `unicode` | Default, works in most terminals |
| `ascii` | Safe fallback for basic terminals |

## See Also

- [jf push](./push.md) - Push changes to GitHub
- [Working with Themes](../guides/themes.md) - Customize appearance
