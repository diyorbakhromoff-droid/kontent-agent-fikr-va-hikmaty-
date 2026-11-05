#!/usr/bin/env bash
# Agentni tmux ichida doimiy ishga tushiradi (SSH yopilsa ham ishlayveradi)
cd ~/kontent-agent-fikr-va-hikmaty-
export PATH="$HOME/.bun/bin:$HOME/.local/bin:$PATH"
tmux has-session -t reels 2>/dev/null && { echo "Agent allaqachon ishlayapti: tmux attach -t reels"; exit 0; }
tmux new-session -d -s reels "claude --channels plugin:telegram@claude-plugins-official"
echo "Agent ishga tushdi. Ko'rish: tmux attach -t reels  (chiqish: Ctrl+B, keyin D)"
