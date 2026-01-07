# Your First Workflow

A hands-on tutorial for your first stack of changes with jflow.

## Scenario

You're adding user authentication to your app. This requires:
1. A REST client library
2. An API layer that uses it
3. A UI component that uses the API

Let's build this as a stack of changes!

## Step 1: Initialize

```bash
cd your-jj-project
jf init --defaults
```

## Step 2: Create the Stack (Outside-In)

Work from **outside** (UI) to **inside** (core):

```bash
# Start with UI (what user sees)
jj new -m "Add login screen UI"
# Create login screen files
touch src/components/LoginScreen.tsx
# Edit the file...

# Add API layer (what UI needs)
jj new -m "Add authentication API"
# Create API files
touch src/api/auth.ts
# Edit the file...

# Add core library (what API needs)
jj new -m "Add REST client library"
# Create library files
touch src/lib/rest-client.ts
# Edit the file...
```

## Step 3: View Your Stack

```bash
jf
```

Output:
```
╭───────────────── Your Stack (3 commits) ─────────────────╮

  3/3 ●  xyz789  Add REST client library
        💡 ready to create PR
  │
  2/3 ○  def456  Add authentication API
        💡 ready to create PR
  │
  1/3 ○  abc123  Add login screen UI
        💡 ready to create PR
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯
```

Notice: The stack is in the order we created them - but that's backwards for dependencies! The library should be at the bottom (merged first), not the top.

## Step 4: Reorder by Dependency

We want: Library → API → UI (bottom to top). Just invert the stack:

```bash
jf reorder --invert
```

That's it! Now `jf` shows the correct order:

```
╭───────────────── Your Stack (3 commits) ─────────────────╮

  3/3 ●  abc123  Add login screen UI
        💡 ready to create PR
  │
  2/3 ○  def456  Add authentication API
        💡 ready to create PR
  │
  1/3 ○  xyz789  Add REST client library
        💡 ready to create PR
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯
```

Perfect! Library at bottom, UI at top.

## Step 5: Push to GitHub

Push everything at once:

```bash
jf push
```

jflow auto-generates bookmark names from your descriptions:

```
ℹ Found 3 change(s) to push (style: squash)
ℹ Creating bookmark 'add-rest-client-library' at xyz789
ℹ Pushing add-rest-client-library...
ℹ Creating pull request...
✓ Pull request created!

ℹ Creating bookmark 'add-authentication-api' at def456
ℹ Pushing add-authentication-api...
ℹ Creating pull request...
✓ Pull request created!

ℹ Creating bookmark 'add-login-screen-ui' at abc123
ℹ Pushing add-login-screen-ui...
ℹ Creating pull request...
✓ Pull request created!

✓ Done!
```

Each PR shows its dependencies in the description!

## Step 6: Check Sync State

```bash
jf
```

```
╭───────────────── Your Stack (3 commits) ─────────────────╮

  3/3 ●  abc123  Add login screen UI
         → add-login-screen-ui ✓
  │
  2/3 ○  def456  Add authentication API
         → add-authentication-api ✓
  │
  1/3 ○  xyz789  Add REST client library
         → add-rest-client-library ✓
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯
```

All bookmarks show ✓ - they're synced with remote!

## Step 7: Respond to Review Feedback

Reviewer comments on the library PR:

> "Please add error handling"

No problem! Edit it directly:

```bash
# Edit the library commit
jj edit xyz789

# Make changes
vim src/lib/rest-client.ts
# Add error handling...

# Return to tip
jj new
```

## Step 8: Push Updates

```bash
jf push
```

Output:
```
ℹ Found 3 change(s) to push (style: squash)
ℹ Pushing rest-client-library...
ℹ Pushing auth-api...
ℹ Pushing login-screen...
✓ Done!
```

**All three PRs automatically updated!**

The API and UI commits were automatically rebased onto the updated library.

## Step 9: Library PR Gets Merged

Great! The library PR is approved and merged.

Clean up:

```bash
jf land
```

Output:
```
ℹ Fetching from origin...
ℹ Found 1 merged PR(s)
ℹ Deleting bookmark 'rest-client-library'...
ℹ Rebasing stack onto main@origin...
✓ Cleanup complete!

╭───────────────── Your Stack (2 commits) ─────────────────╮

  2/2 ●  abc123  Add login screen UI
         login-screen ✓
  │
  1/2 ○  def456  Add authentication API
         auth-api ✓
  │
  ◆  main@origin

╰────────────────────────────────────────────────────────────╯
```

Notice: Library is gone (merged into main)!

Push the remaining PRs to update their base:

```bash
jf push
```

Now API and UI PRs are based on latest main.

## Step 10: Continue Until Done

Continue the process:

```bash
# After API PR merges
jf land
jf push

# After UI PR merges
jf land
```

Final state:

```
╭───────────────── Your Stack (0 commits) ─────────────────╮

  No changes in stack
  (All work is integrated into main@origin)

╰────────────────────────────────────────────────────────────╯
```

Clean slate! Ready for next feature.

## What You Learned

### Outside-In Development
- Start with UI (what user sees)
- Work backwards to dependencies
- Natural way to think about features

### Inside-Out Review
- Review core dependencies first
- Higher-level changes wait for lower-level
- Reduces review iterations

### Automatic Rebasing
- Edit any change directly with `jj edit`
- Descendants automatically rebase
- `jf push` updates all PRs

### Stack Management
- `jf` shows clear picture with sync state
- `jf push` pushes and creates/updates PRs
- `jf land` cleans up after merges
- `jf pull` keeps you current

## Common Patterns

### Fix in Middle of Stack

```bash
jj edit <middle-change>
# fix...
jf push  # Updates all dependent PRs
```

### Add Change to Stack

```bash
jj new <parent> -m "New change"
# work...
jf push  # Creates bookmark and PR
```

### Split a Change

```bash
jj edit <change>
jj split
# Creates two changes
jf push  # Creates PRs for both
```

## Next Steps

- Read the [Complete Workflow Guide](../guides/complete-workflow.md)
- Learn about [GitHub Integration](../guides/github-integration.md)
- Explore [Configuration Options](../guides/configuration.md)
