# jflow Documentation (mdBook)

This is the source for the jflow documentation, built with [mdBook](https://rust-lang.github.io/mdBook/).

## Building the Book

### Install mdBook

```bash
cargo install mdbook
```

### Build

```bash
mdbook build
```

Output will be in `book/` directory.

### Serve Locally

```bash
mdbook serve
```

Opens browser at `http://localhost:3000`

### Watch for Changes

```bash
mdbook watch
```

## Structure

- `book.toml` - Configuration
- `src/` - Documentation source (Markdown)
  - `SUMMARY.md` - Table of contents
  - `introduction.md` - Introduction
  - `getting-started/` - Installation, quick start, first workflow
  - `commands/` - Command reference
  - `guides/` - Usage guides
  - `reference/` - Technical reference
  - `advanced/` - Architecture and contributing
  - `appendix/` - Changelog, FAQ, comparisons

## Editing

1. Edit Markdown files in `src/`
2. Run `mdbook serve` to preview
3. Build with `mdbook build`

## Publishing

The built book in `book/` can be:
- Served with any static site host
- Deployed to GitHub Pages
- Hosted on Netlify/Vercel
- Served locally

## Customization

Edit `book.toml` to customize:
- Theme
- Title
- Repository links
- Search settings

## Documentation Content

The book includes:
- Complete command reference
- Step-by-step guides
- Configuration options
- Troubleshooting
- Best practices
- Architecture details
