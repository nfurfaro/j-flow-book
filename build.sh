#!/usr/bin/env bash
# Build script for jflow documentation

set -e

echo "🔨 Building jflow documentation..."

# Check if mdbook is installed
if ! command -v mdbook &> /dev/null; then
    echo "❌ mdbook not found"
    echo "Install with: cargo install mdbook"
    exit 1
fi

# Build the book
mdbook build

echo "✅ Documentation built successfully!"
echo "📖 Output: book/index.html"
echo ""
echo "To view:"
echo "  mdbook serve"
echo "  # or"
echo "  open book/index.html"
