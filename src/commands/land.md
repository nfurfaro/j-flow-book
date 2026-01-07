# jf land

Clean up after PRs are merged.

## Usage

```bash
jf land                  # Auto-detect merged PRs and cleanup
jf land <bookmark>       # Land a specific PR
jf land --dry-run        # Preview what would be done
```

## Options

| Option | Description |
|--------|-------------|
| `<bookmark>` | Specific bookmark to land (optional) |
| `-n, --dry-run` | Show what would be done without doing it |

## What It Does

1. **Fetches from remote** - Gets latest state from origin
2. **Finds merged PRs** - Checks which bookmarks have merged PRs (via `gh` CLI)
3. **Deletes landed bookmarks** - Removes local bookmarks for merged PRs
4. **Rebases remaining stack** - Updates your stack onto the updated main
5. **Creates fresh commit** - Runs `jj new` so you're ready for new work
6. **Shows updated stack** - Displays what's left to work on

## Examples

### Auto-detect and cleanup merged PRs

```bash
jf land
```

Output:
```
ℹ Fetching from origin...
ℹ Found 2 merged PR(s)
ℹ Deleting bookmark 'jf/rest-library'...
ℹ Deleting bookmark 'jf/auth-api'...
ℹ Rebasing stack onto main@origin...
✓ Cleanup complete!
ℹ Creating fresh commit for new work...

╭─ Your Stack (1 commit) ──────────────────────╮
│                                               │
│  ●  xyz789  (empty) New work                 │
│  │                                            │
│  ◆  main@origin                              │
│                                               │
╰───────────────────────────────────────────────╯
```

### Land a specific bookmark

```bash
jf land jf/my-feature
```

### Preview cleanup

```bash
jf land --dry-run
```

Output:
```
ℹ Fetching from origin...
ℹ Found 1 merged PR(s)

Dry run - would clean up:
  - jf/rest-library
```

## Workflow

Typical post-merge workflow:

```bash
# After PRs are merged on GitHub
jf land          # Cleanup merged bookmarks
jf               # See remaining stack
jf push          # Update remaining PRs with new base
```

## See Also

- [jf push](./push.md) - Push changes to GitHub
- [jf pull](./pull.md) - Pull and rebase stack
- [Complete Workflow](../guides/complete-workflow.md) - Full development cycle
