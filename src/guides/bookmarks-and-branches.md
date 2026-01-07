# Understanding Bookmarks and Branches

If you're coming from Git, the relationship between jj changes, bookmarks, and GitHub PRs can be confusing. This guide explains how they all fit together.

## The Mental Model

In jflow, you work on `main` and create small, focused changes. Each change can become a PR. Branches are **ephemeral** - they exist only to integrate with GitHub's PR model.

| Concept | Git | Jujutsu | GitHub |
|---------|-----|---------|--------|
| Main line | `main` branch | `main@origin` | Default branch |
| Your work | Feature branch | **Change** | PR |
| Integration | Merge/rebase | Rebase | Merge PR |

## What's `main@origin`?

In jj, bookmarks can be local or remote-tracking:

- `main` - a local bookmark (may or may not exist)
- `main@origin` - the remote-tracking bookmark (what's on GitHub)

When you `jj git fetch`, jj updates `main@origin` to match what's on GitHub. This is similar to git's `origin/main`.

jflow uses `main@origin` as the base for your stack because it represents "what's actually on GitHub" - the source of truth.

## Changes, Not Branches

In Git, you create a branch, switch to it, make commits, then merge.

In jj (and jflow), you work differently:

1. **You stay on main** - no branch switching
2. **You create changes** - each change is like a commit with a unique ID
3. **Changes stack naturally** - child changes sit on top of parent changes
4. **Bookmarks are just names** - attached only when pushing to GitHub

Think of it this way: in jflow, you work with **changes**. Bookmarks are an implementation detail for GitHub.

## The jflow Workflow

```
Your local state (jj log):

@  qvmlopxt  Add login button      <- you are here
│
○  rnxpwmkl  Add auth API          <- ready to push
│
○  ktspomvn  Add user model        <- already has PR
│
◆  main@origin                     <- what's on GitHub
```

When you run `jf push`:

1. For each change without a bookmark, jflow generates one from the description
   - "Add auth API" → `add-auth-api`
2. Pushes the bookmark to GitHub (creating a branch)
3. Creates a PR from that branch

After push, GitHub has:
- Branch `add-user-model` → PR targeting `main`
- Branch `add-auth-api` → PR targeting `add-user-model`

## Why This Works

- **No context switching** - you stay on main, jj handles the graph
- **Small PRs** - each change = one PR, easy to review
- **Clean history** - PRs merge to main, bookmarks disappear
- **No manual naming** - jflow generates bookmark names automatically

## Bookmarks Are Temporary

This is the key insight: **bookmarks exist for GitHub, not for you**.

You work with changes. When you need to push to GitHub, jflow creates a bookmark (branch name) automatically. After the PR merges, `jf land` cleans up the bookmark.

You never need to think about branch names unless you want to override the auto-generated one:

```bash
# Auto-generated: "add-user-authentication"
jf push

# Custom name if needed
jf push -b auth-v2
```

## Common Questions

### Do I need to create bookmarks manually?

No. `jf push` creates them automatically from your change descriptions.

### What if I want to work on something unrelated?

Create a new change from main:

```bash
jj new main@origin  # Start fresh from remote main
```

Your other changes are still there - jj tracks everything in the graph.

### How do I see what bookmarks exist?

```bash
jj bookmark list
```

But you rarely need to - jflow manages them for you.

### What happens when a PR merges?

Run `jf land` to:
1. Fetch the merged changes
2. Rebase your remaining stack
3. Delete the merged bookmark
4. Update downstream PRs to target `main`
