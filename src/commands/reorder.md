# jf reorder

Reorder changes in your stack.

## Usage

```bash
jf reorder <change1> <change2> ...      # put changes in specified order
jf reorder -f <c1> <c2> <c3> ...        # reorder starting from c1 (inclusive)
jf reorder --invert                      # reverse the entire stack
jf reorder --invert -f <change>          # reverse from change to @ (inclusive)
```

## Options

| Option | Description |
|--------|-------------|
| `<changes>...` | Changes to reorder (short IDs like `abc` work) |
| `-i, --invert` | Reverse the stack order |
| `-f, --from <change>` | Starting change (inclusive) for both explicit and invert modes |

## What It Does

### Explicit Reorder

Put changes in exactly the order you specify:

```bash
jf reorder abc def ghi
```

Results in: `main` → `abc` → `def` → `ghi`

This is useful when you realize your changes are in the wrong dependency order.

### Reorder with Starting Point

Specify the first change to include in the reorder:

```bash
jf reorder -f abc def ghi
```

Results in: `parent(abc)` → `abc` → `def` → `ghi`

The `-f` flag is inclusive - `abc` becomes the first change in the new order.

### Invert Stack

Reverse the order of your entire stack:

```bash
jf reorder --invert
```

Before:
```
@  ghi  Third change
○  def  Second change
○  abc  First change
◆  main@origin
```

After:
```
@  abc  First change
○  def  Second change
○  ghi  Third change
◆  main@origin
```

### Partial Invert

Reverse only part of the stack:

```bash
jf reorder --invert -f def
```

This reverses from `def` to `@`, leaving earlier changes alone.

## Examples

### Fix dependency order

You created changes in the wrong order - the UI change came before the API it depends on:

```bash
# Current (wrong):
# @  ui-change
# ○  api-change
# ◆  main

# Fix it:
jf reorder api-change ui-change

# Result (correct):
# @  api-change
# ○  ui-change
# ◆  main
```

### Quick stack reversal

You built a feature bottom-up but want to submit PRs top-down:

```bash
jf reorder --invert
```

## Notes

- Uses short change IDs (first few unique characters)
- Shows the updated stack after reordering
- Under the hood, uses `jj rebase` to move changes

## See Also

- [jf status](./status.md) - View your stack
- [jf push](./push.md) - Push after reordering
