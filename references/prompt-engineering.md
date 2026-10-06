# Prompt Engineering for AI-Coded Motion & Video

The viral Opus 5.5 videos achieved their visual quality because their creators stopped using vague requests ("make a cool video") and transitioned to **deterministic director contracts**.

Below is the exact anatomy, structure, and rule system distilled from the top 50 viral prompts in the collection.

---

## 1. The 6-Block Structural Contract

Top creators (e.g. Taxtello, Verbove, TwoClipping, IK Builds) enclose their instructions in modular XML tags or clearly delimited markdown sections:

```markdown
<inputs>
Specify exact data sources, brand tokens, product URLs, or local files.
Do not allow the model to invent dummy data if real data exists.
</inputs>

<direction>
The conceptual aesthetic anchor:
"Apple product launch film x premium fintech x editorial Swiss motion design"
"Literary monument in stone and ink, high-contrast serif with structural grotesques"
"Vintage collage realistic photo landscapes + halftone newspaper cutouts"
</direction>

<rules>
Hard physical and programmatic constraints:
- One HTML file, square 1440x1440 (or 1920x1080).
- Pure seek(t) function: No CSS transitions, no setTimeout, no state between frames.
- Every animation value must be a pure closed-form function of time.
- All-intra video loading (ffmpeg -g 1) if using video textures.
- Negative constraints: Banned effects, banned words, banned transitions.
</rules>

<structure>
Beat-mapped chronological storyboard:
- Pacing: 120 BPM grid (54 beats = 27 seconds, 1 action per beat).
- Timestamps: [0.00-1.50], [1.50-4.00], [4.00-7.50], [7.50-11.00], [11.00-14.00], [14.00-15.00].
- One clear idea per shot. Never rush.
</structure>

<motion>
Specific mathematical behaviors:
- Closed-form step responses for springs:
  f(t) = 1 - (1 + omega * t) * exp(-omega * t)
- Summed target springs for multi-step movements.
- Object-driven transitions (Object A transforms into Object B).
- Motion blur via subframe temporal supersampling.
</motion>

<export>
Verification and rendering protocol:
- First render 1 frame per beat as a contact sheet (visual QA).
- Inspect frames for overlaps, clipping, or visual clutter.
- Render full sequence in headless Chromium at 60fps.
- Pipe frames into FFmpeg with libx264, yuv420p, crf 18.
</export>
```

---

## 2. The Golden Rules of Visual Taste

### Rule 1: ONE SHOT = ONE IDEA
Never crowd multiple competing elements into a single scene. If you show a financial cockpit, animate the balance first, then let the chart draw. Give each visual element 800ms–1500ms to register before changing the subject.

### Rule 2: Object-Driven Transitions
Reject generic transitions:
| Bad Transitions | Good Object-Driven Transitions |
|---|---|
| Crossfade / Fade to black | Chart point expands into receipt corner |
| Slide left / Carousel wipe | Notch expands into browser window |
| Random 3D spin / Glitch spam | Number counter zooms into camera iris |
| Zoom blur spam | Wordmark collapses into period; period becomes circular portal |

### Rule 3: Restrained Palette & True Hierarchy
- Dark metal backgrounds (`#0c0f1a` / `#111525`) provide infinite contrast without harsh `#000000`.
- Single precious accent (e.g. machined gold `#e8b84b` or electric cyan `#00e5ff`).
- Muted secondary typography (`#8b93b5`).
- Never flood the screen with accent color. Accent is for active state and precision highlights.

### Rule 4: Ban the AI Slop Clichés
Explicitly include these negative constraints in your prompt:
- **NO particle spam** (floating dust or sparkles).
- **NO generic purple/cyan neon cyber aesthetics**.
- **NO 3D rotating cards** that serve no purpose.
- **NO fake glassmorphism** that degrades text contrast.
- **NO bouncing cartoon springs**; use critically damped or 1.5% overshoot curves.
- **NO marketing fluff copy**; use max 3–5 word punchlines ("Alles im Blick", "Build the Floor").

---

## 3. The 3 Master Prompt Archetype Templates

### Template A: The Apple-Tier SaaS Launch (Taxtello Style)
```markdown
You are the senior motion designer and creative technologist for {{PRODUCT_NAME}}.
Create a 15-second, 60fps, 1080p product launch film entirely in code.
Aesthetic: Apple product reveal x Stripe financial precision x quiet luxury.

REPO / BRAND TRUTH:
- Inspect {{REPO_PATH}} or {{URL}}. Use real CSS tokens, fonts, and screenshots.
- Palette: Background #0c0f1a, Card #131722, Accent Gold #e8b84b, Text #e8eaf2.
- Fonts: Plus Jakarta Sans / JetBrains Mono for figures.

RULES:
- One shot = one idea. The product UI is the hero.
- No crossfades. Object-driven transitions only:
  0.0-1.5s: Machined glint resolves into wordmark.
  1.5-5.0s: Financial cockpit emerges; hero metric counts up; chart draws smoothly.
  5.0-8.5s: Data point morphs into document card; magnetic alignment into booking table.
  8.5-12.0s: Status pill transitions to active invoice view; tactile currency updates.
  12.0-15.0s: UI folds outward into single dark luxury canvas with final brand payoff.
- Music cut to 118 BPM. Subtle tactile mechanical clicks on UI state changes.
- Output: Render contact sheet at 0s, 2s, 5s, 8s, 11s, 14s. Verify frames before full render.
```

### Template B: The Adrenaline Motion Showreel (IK Builds Style)
```markdown
Create a 15s kinetic motion graphics film for {{PRODUCT}}.
Stack: HyperFrames + GSAP (or deterministic Canvas), no footage, no voiceover.
Style: Paper-light canvas, marker annotations via stroke-dashoffset, huge kinetic type (Anton), hard dark/light switches.
Pacing: A new idea every 1.5s. Sound effect on every single visual hit.
Copy: Read {{DOCS}}. Short phrases only. Speak directly to the technical buyer.
Motion: Heavy easing, squash/stretch, staggered reveals, seek-safe t=0 states.
Audio: 120 BPM drum drops, whooshes, pen scribbles, sub-bass hit on logo resolve.
```

### Template C: The Liquid Glass & Canvas Morph (Verbove / TwoClipping Style)
```markdown
Single HTML file. Square 1440x1440. One canvas, one window.seek(t) function.
No CSS transitions, no timers, zero frame-to-frame mutable state.
One central shape that morphs size, corner radius, and content across 12 UI states.
A virtual cursor drives clicks, drags, and long-presses.
Motion: Closed-form critically damped springs.
Audio: 54 beats at 120 BPM, something happens on every single beat.
Render: Playwright headless capture, 60fps, 4 subframes averaged for motion blur, encoded via FFmpeg.
```
