#!/usr/bin/env bash
# Reels agent — Hetzner (Ubuntu 24.04) server setup. Run as a normal user with sudo.
set -e
echo "== 1/6 Tizim paketlari"
sudo apt-get update -y
sudo apt-get install -y git curl unzip ffmpeg tmux fonts-noto-color-emoji
echo "== 2/6 Node.js 22"
if ! command -v node >/dev/null; then curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt-get install -y nodejs; fi
echo "== 3/6 Bun (Telegram plugin uchun)"
command -v bun >/dev/null || curl -fsSL https://bun.sh/install | bash
echo "== 4/6 Claude Code"
command -v claude >/dev/null || curl -fsSL https://claude.ai/install.sh | bash
echo "== 5/6 Ombor va montaj vositalari"
cd ~
[ -d kontent-agent-fikr-va-hikmaty- ] || git clone https://github.com/diyorbakhromoff-droid/kontent-agent-fikr-va-hikmaty-.git
cd kontent-agent-fikr-va-hikmaty-
[ -f package.json ] || npm init -y >/dev/null
npm i playwright@1.49.1 >/dev/null
npx playwright install --with-deps chromium
echo "== 6/6 Tayyor"
echo "Endi: cd ~/kontent-agent-fikr-va-hikmaty- && claude"
