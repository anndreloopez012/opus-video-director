---
name: opus-video-director
description: Use when creating AI-coded videos, viral motion design, SaaS product launch films, 3D flythroughs, kinetic typography, audio-reactive music videos, shaders, or canvas animations based on the Opus 5.5 / Skillry 400+ video catalog
---

# Opus Video Director

## Overview
Comprehensive system for producing viral, high-craft, code-based videos across all 14 archetypes and 475 reference implementations from the Opus 5.5 / Skillry collection. Rather than generating hallucinations, it treats video as a **deterministic software composition** (HyperFrames, Remotion, Canvas/Playwright, Three.js) driven by pure functions of time, closed-form physics, and object-driven transitions.

---

## When to Use

### Trigger Conditions
- When asked to create or direct an AI-coded motion graphic, SaaS product film, or launch trailer.
- When asked to make a video resembling viral Claude Opus 5.5 / Skillry creations (Taxtello, IK Builds, NotchBrowser, Liquid Glass Keynote, 3D Flythroughs).
- When asked to produce animated product demos, kinetic typography speeches, audio-reactive music videos, or GLSL fluid/shader films.
- When the user asks to browse, search, or clone any of the 405+ / 475 video prompts from `skillry.dev/ai-videos/opus-5-5`.

### When NOT to Use
- When the user wants raw text-to-video AI diffusion models (Sora, Kling, Runway, Pika, Higgsfield) with zero code or deterministic UI control.
- When the user only needs static image editing or basic screenshot cropping.
- When the user only wants plain audio transcription without visual motion design.

---

## Archetype Routing Matrix

Map incoming requests to one of the 14 verified archetypes:

| User Goal / Deliverable | Archetype ID | Recommended Engine | Duration | Aspect |
|---|---|---|---|---|
| B2B SaaS launch, luxury fintech reveal, Apple-tier product film | `saas-launch` | Remotion / HyperFrames / Canvas | 14s–30s | 16:9 |
| Adrenaline motion designer reel, kinetic resume, agency showreel | `motion-showreel` | HyperFrames + GSAP / Canvas | 15s–30s | 16:9 / 9:16 |
| Monumental spoken word, speech manifesto, structural typography | `kinetic-typography` | Canvas (SVG Paths) / Remotion | 15s–25s | 1:1 / 16:9 |
| iOS simulator tour, Dynamic Island morph, app interaction | `app-mobile-ui` | Canvas / HyperFrames | 15s–60s | 9:16 / 16:9 |
| Architecture diagram, developer workflow, technical explainer | `concept-explainer` | HyperFrames / Canvas | 20s–60s | 16:9 |
| Live line drawing charts, financial cockpit, trading sweeps | `data-viz-charts` | Canvas / Remotion | 15s–30s | 16:9 |
| Orbital zoom to city, satellite tracking, flight paths | `map-geo-spatial` | Three.js / Canvas | 15s–35s | 16:9 |
| Seamless portal descent, vintage collage zoom, 3D house tour | `3d-world-flythrough` | Three.js / Canvas (Parallax) | 20s–45s | 16:9 |
| GPU fluid simulation, procedural fire/smoke, blackbody physics | `shader-generative` | Three.js (WebGL GLSL) | 15s–40s | 16:9 |
| Rigid body collisions, Verlet springs, cloth/gravity sim | `particles-physics` | Canvas (Physics engine-free) | 15s–30s | 1:1 / 16:9 |
| Beat-synced cuts, kaleidoscope mirror, RGB split glitch | `audio-reactive-mv` | Canvas + Playwright | 30s–90s | 16:9 / 9:16 |
| Playable 90s arcade, low-poly racer, browser Minecraft | `playable-game-arcade` | Three.js + TypeScript | 20s–60s | 16:9 |
| Dramatic multi-shot cinematic narrative, space drama | `brand-commercial-ad` | Multi-scene Canvas / Playwright | 20s–45s | 9:16 / 16:9 |
| Vector mascot loops, 8-bit/16-bit retro pixel animations | `character-retro-pixel` | Pixel Canvas / Sprite engine | 10s–30s | 16:9 / 1:1 |

---

## Catalog CLI Tool (`opus_videos.py`)

The skill includes a dedicated command-line engine located at `scripts/opus_videos.py`. Use it to search, inspect, and scaffold:

```bash
# View global stats across all 475 scraped videos
python3 scripts/opus_videos.py stats

# List all 14 archetypes with descriptions and counts
python3 scripts/opus_videos.py archetypes

# Search videos by keyword (e.g. apple, taxtello, game, fire, canvas)
python3 scripts/opus_videos.py search "taxtello"

# Filter videos by archetype, aspect ratio, or tech tag
python3 scripts/opus_videos.py list --archetype saas-launch --aspect 16:9 -n 10

# Inspect complete metadata and prompt of a specific video
python3 scripts/opus_videos.py inspect "daniel-haida-636937"

# Print only the clean prompt ready for execution
python3 scripts/opus_videos.py prompt "ik-builds-585923"

# Scaffold a production project boilerplate ready to preview and render
python3 scripts/opus_videos.py scaffold saas-launch --target-dir ./my-launch-video --stack canvas
```

---

## 5-Step Production Workflow

### Step 1: Ingest Brand Truth & Real Data
Never invent placeholder UI or fake company names if a project exists.
- Inspect the repository or landing page for real CSS tokens (`--color-bg`, `--color-accent`), real typography, SVG wordmarks, and genuine screenshots.
- Pull real product states (e.g. Dashboard $\to$ Invoices $\to$ Settings).

### Step 2: Select Archetype & Engine
- Use the Archetype Routing Matrix above.
- Default to **Canvas (Single File `seek(t)` + Playwright)** for zero external dependencies and guaranteed 60fps determinism.
- Use **HyperFrames** when working within a project that has `@hyperframes/cli` installed.
- Use **Remotion** when animating existing React component libraries.
- Use **Three.js** for 3D camera moves, meshes, or custom GLSL fragment shaders.

### Step 3: Design the Beat-Mapped Storyboard
- Establish a strict musical tempo (typically **118–120 BPM**, where 1 beat = 0.5s).
- Enforce **ONE SHOT = ONE IDEA**. Never animate multiple disparate UI widgets simultaneously.
- Map out **Object-Driven Transitions**:
  - Example: A gold chart point grows into a document card; the card snaps into an invoice table; the table folds into the final brand wordmark.
  - Ban generic crossfades, wipes, and spinning cards.

### Step 4: Author Deterministic Code
Every visual attribute must be computed from time inside a pure seek function:
```javascript
// Closed-form critically damped spring: f(t) in [0, 1]
function spring(t, delay = 0, omega = 10.0) {
  if (t < delay) return 0;
  const tau = t - delay;
  return 1 - (1 + omega * tau) * Math.exp(-omega * tau);
}

window.seek = function(t) {
  // Pure function of t. NO setTimeout, NO CSS transitions, NO frame state.
};
```

### Step 5: Contact Sheet Verification & Render
Before delivering or claiming success:
1. Render a contact sheet of key frames (e.g. at 0s, 2s, 5s, 8s, 11s, 14s).
2. Visually inspect the still images for text clipping, contrast degradation, or rushed pacing.
3. Render the full sequence at 60fps and compile with FFmpeg:
```bash
ffmpeg -y -framerate 60 -i frames/frame_%05d.png \
  -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 18 -movflags +faststart output.mp4
```

---

## Common Mistakes & Quality Counters

| Bad Impulse | Why It Fails | Opus 5.5 Proven Standard |
|---|---|---|
| "Let me add floating particles & purple glow" | Looks like cheap AI template slop | Use dark metal (`#0c0f1a`) and machined gold (`#e8b84b`) accents |
| "I'll use CSS transitions with `setTimeout`" | Non-deterministic; drops frames during headless capture | Pure mathematical $f(t)$ step functions inside `seek(t)` |
| "Let's put 5 features in a 15-second video" | Viewer cognitive overload; nothing registers | Exactly 3–4 visual moments; give each 1.5s–3.0s to breathe |
| "Crossfade between scene A and scene B" | Feels like a PowerPoint slideshow | Object-driven transitions (the object in A becomes the surface in B) |
| "Declare done because code compiled" | Visual bugs, bad kerning, overlapping cards | Generate contact sheet frames and inspect before final export |

---

## Supporting References
- [14 Video Archetypes In-Depth](references/archetypes.md)
- [Prompt Engineering & Structural Contracts](references/prompt-engineering.md)
- [Deterministic Render Pipelines (HyperFrames, Remotion, Canvas, ThreeJS)](references/render-pipelines.md)
- [Full 475-Video Database (`catalog.json`)](references/catalog.json)

---

## Specialized Subagent: `video-director-cinematographer`

For autonomous, end-to-end directorial supervision, invoke or collaborate with the specialized subagent `video-director-cinematographer`:
- **Role**: Director Cinematográfico & Diseñador Visual de Videos (The AI Filmmaker & Motion Designer).
- **Core Workflow**:
  1. **Briefing Refinement**: Organizes disorganized ideas into an exact beat-by-beat storyboard.
  2. **Style Matching**: Uses `python3 scripts/opus_videos.py search "<tema>"` to pick the optimal archetype among the 475 Opus 5.5 styles.
  3. **Missing Inputs Audit**: Stops before generating to ask the user what assets need to be uploaded (SVG logos, brand HEX, UI mockups, voiceover timing).
  4. **7-Layer Master Prompt**: Writes production-ready cinematic prompts in technical English with camera lenses, physical lighting, and closed-form eases.
