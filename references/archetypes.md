# 14 Video Archetypes of the Opus 5.5 Collection

This reference defines the 14 distinct video archetypes extracted from the 475 viral Opus 5.5 videos on Skillry. Each archetype represents a proven structural formula with specific motion rules, timing constraints, and visual language.

---

## 1. SaaS & Product Launch Film (`saas-launch`)
- **Core Principle**: "Apple keynote meets premium European fintech". The software is treated like a physical piece of luxury hardware.
- **Duration**: 14.0s - 30.0s (15.0s sweet spot).
- **Aspect Ratio**: 16:9 (Desktop master), optional 9:16 social recut.
- **Pacing**: 115–120 BPM grid. First product moment by 1.5–2.0s. No 5-second logo intro.
- **Palette**: Dark metal (`#0c0f1a`), elevated dark cards (`#111525`, `#1a2032`), precious accent gold (`#e8b84b`), semantic green/red only.
- **Transitions**: 100% object-driven:
  - Chart vertex → document corner
  - Metric pill → modal action button
  - Receipt card → ledger entry
  - Macro camera push through glass
- **Banned**: Cheesy scanner lasers, floating paper tornados, particle bursts, spinning 3D cards, generic SaaS slide-lefts.
- **Flagship Reference**: `daniel-haida-636937` (Taxtello), `twoclipping-496100` (Liquid Glass Keynote), `aschapmann-724497` (RedShip).

---

## 2. Kinetic Motion Designer Showreel (`motion-showreel`)
- **Core Principle**: "Dynamic 15-second resume showreel proving peak motion design taste".
- **Duration**: 15.0s - 60.0s.
- **Aspect Ratio**: 16:9 or 9:16.
- **Pacing**: Rapid-fire rhythm (new idea every 1.5–2.0s), hard dark/light switches.
- **Techniques**: Staggered text reveals, squash & stretch, paper-light canvas, marker annotations (`stroke-dashoffset`), dynamic camera tilts.
- **Audio**: Sound on every hit (pops, clicks, swooshes, sub-bass logo drops).
- **Flagship Reference**: `ik-builds-585923` (IK Builds), `gabrielbuzziv-057430` (Gabriel Buzzi), `thayto-dev-739735` (Thayto Dev).

---

## 3. Architectural Kinetic Typography & Spoken Word (`kinetic-typography`)
- **Core Principle**: "Words as physical structural objects". The letterforms construct the world that the final sentence stands on.
- **Visual Assignment**:
  - Word A = Lintel (ceiling load)
  - Word B = Suspended weight
  - Word C = Vertical pillar / support
  - Word D = Aperture / camera opening
  - Word E = Load-bearing platform
- **Timing**: Cue sheet based on speech phrasing, not a dance beat. At least one 400ms moment of complete silence/stillness.
- **Deformation**: Vector glyph path deformation, preserved counters and baseline tension.
- **Flagship Reference**: `gdgtify-929495` ("BUILD THE FLOOR"), `bs-creatormotion-type-title-takeover`.

---

## 4. Mobile App UI Tour & Micro-Interactions (`app-mobile-ui`)
- **Core Principle**: Real iOS simulator captures or recreated SwiftUI components inside photorealistic phone hardware.
- **Key Features**: Dynamic Island morphing, notch expansion, haptic feedback ripples, tab stretching via asymmetric springs.
- **Interaction**: Cursor or translucent touch pointer driving real taps, swipes, and long-presses.
- **Flagship Reference**: `jake11moran-414633` (NotchBrowser), `jesscaroline7-955094` (Ondefica App).

---

## 5. Technical & Scientific Explainer (`concept-explainer`)
- **Core Principle**: Clear visual dissection of complex technical architectures, developer workflows, or scientific systems.
- **Visuals**: Animated node diagrams, data packets flowing along glowing splines, terminal code execution overlays.
- **Tone**: Clean Swiss editorial, restrained typography, zero gimmicks.
- **Flagship Reference**: `timguignard-623571`, `mattworkman-309357`, `devarshukani-341827`.

---

## 6. Data Visualization & Financial Heatmaps (`data-viz-charts`)
- **Core Principle**: Precision financial metrics brought to life through kinetic plotting and spatial depth.
- **Elements**: Bezier curve line charts drawing in real-time, glowing data points, live counter interpolations (`€0` → `€148,500`), candlestick sweeps.
- **Flagship Reference**: `petert-350098`, `teslachartz-887985`.

---

## 7. Geographic, Satellite & 3D Globe Flythroughs (`map-geo-spatial`)
- **Core Principle**: Continuous zoom from orbital planetary scale down to street-level coordinates.
- **Elements**: 3D textured globe, atmospheric limb airglow, glowing route trajectories, pin drops with spring damping.
- **Flagship Reference**: `alexalbert-274839` (1906 San Francisco), `verbove-268381`.

---

## 8. 3D Environments, Dioramas & Infinite Zooms (`3d-world-flythrough`)
- **Core Principle**: Seamless spatial exploration through portal transitions or infinite camera descent.
- **Techniques**:
  - Exponential zoom: $d(t) \propto \log(zoom)$
  - Depth-layer separation with parallax: $scale = camera^Z$ ($0.45 \le Z \le 1.22$)
  - Low-poly isometric scenes in Three.js (no external models required)
- **Flagship Reference**: `koldo2k-778767` (Vintage Infinite Zoom), `aayush4soni-644283` (3D House Walkthrough).

---

## 9. GLSL Shaders & Real-time Generative Art (`shader-generative`)
- **Core Principle**: GPU fragment shaders running at 60fps computing procedural physics, fluids, and light.
- **Techniques**: Raymarching SDFs, Navier-Stokes fluid simulations, blackbody radiation formulas for photoreal fire/smoke, domain warping.
- **Flagship Reference**: `nathanwilbanks-981110` (GPU Fluid Fire), `niegramotny-197521`.

---

## 10. Particle Systems & Verlet Physics (`particles-physics`)
- **Core Principle**: Real simulated mechanics instead of keyframed approximations.
- **Techniques**: Verlet integration, closed-form springs ($1 - (1 + \omega\tau)e^{-\omega\tau}$), mass/gravity damping, collision resolution.
- **Flagship Reference**: `twoclipping-496100`, `verbove-268381`.

---

## 11. Audio-Reactive Music Videos & Glitch MV (`audio-reactive-mv`)
- **Core Principle**: Frame-exact synchronization to music transients and frequency spectrum.
- **Techniques**:
  - Cut on every beat (120 BPM = 1 cut every 0.5s)
  - White flash on bar downbeats
  - RGB chromatic split on bass drops
  - Kaleidoscope radial mirroring
- **Flagship Reference**: `pound75423-464968` (Psychedelic Glitch MV), `aisongman-461057`.

---

## 12. Playable Web Games & Arcade Simulations (`playable-game-arcade`)
- **Core Principle**: Code-generated game world with fixed-timestep physics and scripted cinematic camera tracks.
- **Features**: Low-poly vehicle/character meshes generated programmatically (`BoxGeometry`, `CylinderGeometry`), procedural voxel terrain, HUD DOM layer.
- **Flagship Reference**: `niegramotny-197521` (Ignition 1997 Racer), `viggle-pinoc-434495` (Browser Minecraft).

---

## 13. Cinematic Storytelling & High-Concept Ads (`brand-commercial-ad`)
- **Core Principle**: Dramatic multi-scene narrative with Hollywood-level camera direction, character blocking, and lighting arcs.
- **Techniques**: Strict continuity constraints, multi-camera angle coverage, atmospheric audio bed, single-source cinematic lighting (5600K key, 2800K fill).
- **Flagship Reference**: `alexwtlf-981005` (Earth Orbit Astronaut Bolide), `washow-cfo-175311`.

---

## 14. Character Mascot Animation & Retro Pixel Worlds (`character-retro-pixel`)
- **Core Principle**: Hand-drawn canvas vector characters, 8-bit/16-bit pixel sprites, sticker outlines, and playful mascot motion loops.
- **Techniques**: Pixel-grid canvas rendering, sprite sheets, white sticker offset borders, playful squash/stretch idle cycles.
- **Flagship Reference**: `eric-khun-667455` (Taiwan Bear), `mozetech-471882`.
