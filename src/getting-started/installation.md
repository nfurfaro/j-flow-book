# Installation

## Prerequisites

Before installing jflow, you need:

1. **Rust toolchain** - For building from source
2. **Jujutsu (jj)** - The version control system
3. **gh CLI** (optional) - For automatic PR creation

## Install Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
```

Verify installation:
```bash
rustc --version
cargo --version
```

## Install Jujutsu

```bash
cargo install --git https://github.com/martinvonz/jj jj-cli
```

Verify installation:
```bash
jj --version
```

## Install jflow

### From Source (Recommended)

```bash
# Download and extract
tar -xzf jflow-v0.2.0.tar.gz
cd jflow

# Build release binary
cargo build --release

# Install to PATH
cp target/release/jf ~/.local/bin/
```

Make sure `~/.local/bin` is in your PATH:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Verify Installation

```bash
jf --version
```

You should see:
```
jf 0.2.0
```

## Install gh CLI (Optional)

For automatic PR creation:

### macOS
```bash
brew install gh
```

### Linux
```bash
# Debian/Ubuntu
sudo apt install gh

# Fedora
sudo dnf install gh

# Arch
sudo pacman -S github-cli
```

### Authenticate
```bash
gh auth login
```

## Platform-Specific Notes

### Linux

You may need build essentials:
```bash
# Debian/Ubuntu
sudo apt install build-essential libssl-dev pkg-config

# Fedora
sudo dnf install gcc openssl-devel
```

### macOS

If using Homebrew:
```bash
brew install openssl
```

### Windows

Use WSL2 or install Rust via rustup-init.exe and build natively.

## Troubleshooting

### "cargo: command not found"

Rust not installed or not in PATH. Install Rust and run:
```bash
source ~/.cargo/env
```

### "jj: command not found"

Jujutsu not installed. Follow the Jujutsu installation above.

### Compilation errors

See the [Building from Source](../advanced/building.md) guide for detailed troubleshooting.

## Next Steps

- [Quick Start Guide](./quick-start.md) - Get started with jflow
- [Initialize Your Repository](../commands/init.md) - Run `jf init`
