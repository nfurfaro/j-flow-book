# jf push

Push changes to GitHub, creating or updating PRs.

## Usage

```bash
jf push                           # Push all changes in current stack
jf push -r <revset>               # Push specific changes
jf push -b <name> -r @            # Override auto-generated bookmark name
jf push --dry-run                 # Preview what would be done
```

## Options

| Option | Description |
|--------|-------------|
| `-r, --revision <revset>` | Revset of changes to push (default: entire stack) |
| `-b, --bookmark <name>` | Override the auto-generated bookmark name |
| `--squash` | Force squash-style push (override config) |
| `--append` | Force append-style push (override config) |
| `-n, --dry-run` | Show what would be done without doing it |

## What It Does

1. **Ensures main branch exists** - Automatically creates `main` on remote if missing
2. **Finds changes to push** - Uses the provided revset or the entire stack
3. **Auto-generates bookmark names** - From the change description (e.g., "Add login" → `add-login`)
4. **Sets PR base branch** - Parent's bookmark or main for root changes
5. **Pushes to remote** - Uses configured push style (squash or append)
6. **Creates/updates PRs** - Via `gh` CLI if available

## Bookmark Generation

jflow automatically creates bookmark names from your change descriptions:

| Description | Generated Bookmark |
|-------------|-------------------|
| Add user authentication | `add-user-authentication` |
| Fix bug in login form | `fix-bug-in-login-form` |
| Update README with examples | `update-readme-with-examples` |

The bookmark name is:
- Lowercase
- Words joined with hyphens
- Limited to first 5 words
- Only alphanumeric characters and hyphens

Use `-b` to override when the auto-generated name isn't suitable:

```bash
jf push -b auth-v2 -r @
```

## Push Styles

### Squash (default)

Force-pushes updates to the branch. Simple and clean.

```bash
jf push --squash
```

### Append

Adds incremental commits on top. Preserves review context.

```bash
jf push --append
```

Configure default in `.jflow.toml`:

```toml
[github]
push_style = "squash"  # or "append"
```

## Examples

### Push entire stack

```bash
jf push
```

### Push single change with custom bookmark

```bash
jf push -r @ -b my-feature
```

### Preview changes

```bash
jf push --dry-run
```

Output:
```
ℹ Found 2 change(s) to push (style: squash)

Dry run - would push:
  abc12345 Add authentication [needs bookmark]
  def67890 Add login screen [add-login-screen]
```

## Stack Context in PRs

When `stack_context = true` in config, PR descriptions include:

```markdown
## Part of stack:

- ✓ Add REST library (bookmark: `add-rest-library`)
- **This PR** (Add API layer)
- ⏳ Add UI component (bookmark: `add-ui-component`)
```

## See Also

- [Bookmarks and Branches](../guides/bookmarks-and-branches.md) - Understanding the relationship
- [jf land](./land.md) - Clean up after PRs are merged
- [jf status](./status.md) - View your stack
