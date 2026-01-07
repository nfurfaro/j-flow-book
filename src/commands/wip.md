# jf wip

Sync work-in-progress between machines.

## Usage

```bash
jf wip              # show wip status
jf wip push         # push stack to wip branch
jf wip push --force # overwrite existing wip branch
jf wip pull         # pull wip branch and rebase onto main
jf wip clean        # delete wip branch (if changes have PRs)
jf wip clean --force # delete wip branch regardless
```

## Options

| Option | Description |
|--------|-------------|
| `-f, --force` | Force overwrite (push) or delete without PR check (clean) |

## What It Does

The `wip` command helps you sync uncommitted work between machines without creating PRs.

### The Problem

With jj/jflow, you work directly on main and your changes aren't on a feature branch. When you need to switch machines, you need a way to transfer your stack.

### The Solution

`jf wip` creates a temporary `wip/<username>` bookmark that holds your entire stack. Push it from one machine, pull it on another.

## Subcommands

### `jf wip` (status)

Show the current state of your wip branch:

```
$ jf wip
ℹ wip/nick on origin:
  ○ abc12345  Add login UI
  ○ def67890  Add auth API
  ○ ghi11111  Add REST client
```

Or if no wip exists:

```
$ jf wip
ℹ No wip branch found (wip/nick)
  Use `jf wip push` to push your stack
```

### `jf wip push`

Push your entire stack to the wip branch:

```
$ jf wip push
ℹ Pushing 3 changes to wip/nick...
✓ Done!
```

If a wip branch already exists (maybe you pushed from another machine), it fails:

```
$ jf wip push
✗ wip/nick already exists on origin
  ○ xyz98765  Some other work

  Use `--force` to overwrite, or `jf wip pull` to fetch it first.
```

Use `--force` to overwrite:

```
$ jf wip push --force
ℹ Overwriting wip/nick (3 changes)...
✓ Done!
```

### `jf wip pull`

Fetch the wip branch and rebase onto your local main:

```
$ jf wip pull
ℹ Fetching from origin...
ℹ Found 3 changes in wip/nick
ℹ Rebasing onto main@origin...
✓ Done!
```

This command:
1. Fetches from remote (updates both wip and main@origin)
2. Checks for local changes (aborts if any exist)
3. Rebases the wip changes onto main@origin

If you have local changes, it aborts:

```
$ jf wip pull
ℹ Fetching from origin...
✗ You have local changes:
  ○ abc12345  Some local work

  Clean up your local stack first, then try again.
```

### `jf wip clean`

Delete the wip bookmark (local and remote) when you're done:

```
$ jf wip clean
ℹ wip/nick contains 3 changes:
  ○ abc12345  Add login UI ✓
  ○ def67890  Add auth API ✓
  ○ ghi11111  Add REST client ✓

✓ All changes have PRs
✓ Deleted bookmark wip/nick (local and remote)
```

If changes don't have PRs yet, it refuses (to prevent data loss):

```
$ jf wip clean
ℹ wip/nick contains 3 changes:
  ○ abc12345  Add login UI
  ○ def67890  Add auth API
  ○ ghi11111  Add REST client

✗ Cannot clean: some changes not in any PR
  Hint: push PRs with `jf push`, or use `--force` to delete anyway
```

Use `--force` to delete anyway:

```
$ jf wip clean --force
✓ Deleted bookmark wip/nick (local and remote)
```

## Typical Workflow

### Switching from desktop to laptop

```bash
# On desktop - done for the day
jf wip push

# On laptop - starting work
jf wip pull
# ... continue working ...

# When done, push PRs
jf push
jf wip clean
```

### Resuming on original machine

```bash
# On desktop next day
jf wip pull   # get any changes made on laptop

# Or if you already have the changes locally
jf wip clean  # just clean up the wip branch
```

## Notes

- The wip branch is named `wip/<username>` (e.g., `wip/nick`)
- Only one wip branch per user - it represents "my current work"
- Changes in wip are rebased onto the latest main@origin when pulled
- The `clean` command checks that changes have PRs before deleting (safety net)

## See Also

- [jf push](./push.md) - Push changes as PRs
- [jf pull](./pull.md) - Pull and rebase main
