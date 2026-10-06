# CLAUDE.md - Multi-Agent Operating Contract (Claude Code)

This repository contains the **Opus Video Director** suite.

## Commands
- Global Catalog Stats: `python3 scripts/opus_videos.py stats`
- Search Video Recipes: `python3 scripts/opus_videos.py search "<query>"`
- Inspect Video Details: `python3 scripts/opus_videos.py inspect "<slug_or_id>"`
- Copy Clean Prompt: `python3 scripts/opus_videos.py prompt "<slug_or_id>"`
- Scaffold New Video Project: `python3 scripts/opus_videos.py scaffold <archetype> --target-dir <path> --stack <canvas|hyperframes|remotion>`

## Design Rules
- All animations must be closed-form functions of time (seek-safe, no frame-to-frame mutable state).
- Use 118-120 BPM tempo grid for kinetic motion.
- Object-driven transitions only: elements transform into the next scene's elements.
