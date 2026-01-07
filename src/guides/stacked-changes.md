# Stacked Changes

A workflow methodology for building features as small, focused, reviewable changes.

## The Core Idea

Instead of building a feature in one large commit (or messy branch), break it into a **stack of small, focused changes**. Each change:

- Does one thing well
- Builds on the previous change
- Is independently reviewable
- Can be merged incrementally

## Outside-In Development, Inside-Out Review

This methodology was popularized by Drew Deponte in his article [How We Should Be Using Git](https://drewdeponte.com/blog/how-we-should-be-using-git/).

### Outside-In Development

When building a feature, start from the **outside** (what the user sees) and work **inward** (to the implementation details):

1. **UI layer** - The user-facing component
2. **API layer** - The interface the UI needs
3. **Core layer** - The underlying implementation

This is natural because you think about what you need as you go.

### Inside-Out Review

When reviewing and merging, go in the **opposite direction**:

1. **Core layer first** - Merge the foundation
2. **API layer next** - Merge the interface
3. **UI layer last** - Merge what depends on everything else

This ensures each PR has its dependencies already merged.

### Example

Building user authentication:

```
Development order (outside-in):
1. Add login screen UI
2. Add authentication API
3. Add REST client library

Review/merge order (inside-out):
1. Add REST client library  <- merge first
2. Add authentication API   <- merge second
3. Add login screen UI      <- merge last
```

After creating these changes, use `jf reorder --invert` to flip the stack for proper merge order.

## Why Stacked Changes?

### Smaller PRs

- Easier to review (< 200 lines ideal)
- Faster feedback cycles
- Less context switching for reviewers

### Better History

- Each change tells a clear story
- Easy to bisect and debug
- Clean, linear history

### Parallel Work

- Team members can review different parts of the stack
- Changes can be merged as soon as they're approved
- No waiting for one massive PR

## jflow's Role

jflow makes this workflow effortless:

| Task | Command |
|------|---------|
| See your stack | `jf` |
| Reorder for review | `jf reorder --invert` |
| Push all changes | `jf push` |
| Clean up after merge | `jf land` |

## Inspiration

jflow's stacked workflow is inspired by:

- **[git-ps-rs](https://github.com/uptech/git-ps-rs)** - Patch stack tooling for Git
- **Drew Deponte's [article](https://drewdeponte.com/blog/how-we-should-be-using-git/)** on Git workflows
- **Jujutsu's** native support for working with stacked changes

The key insight: Git (and GitHub) weren't designed for this workflow, but Jujutsu was. jflow bridges jj's powerful change model with GitHub's PR-based review process.
