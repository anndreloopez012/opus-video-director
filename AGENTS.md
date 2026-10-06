# AGENTS.md - Multi-Agent Operating Contract (Antigravity & Codex)

This repository houses the **Opus Video Director** suite: a production-grade catalog and scaffolding system for creating 475 code-based video archetypes pioneered by Claude Opus 5.5.

## Protocol for Codex & Antigravity
1. **Always use deterministic code**: Videos must be built using pure functions of time (`window.seek(t)` in Canvas, Remotion frame interpolation, or HyperFrames `data-*` timing attributes).
2. **Consult Catalog**: Use `python3 scripts/opus_videos.py search "<keyword>"` or `inspect "<slug>"` before designing a video to locate the exact reference prompt and architecture.
3. **Continuous Memory Synchronization**:
   - Keep git status clean before editing.
   - When updating the codebase, update Graphify: `graphify .`
   - Synchronize with Obsidian: `memoria refresh`
