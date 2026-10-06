# Render Pipelines for Code-Based Video Creation

This guide details the 4 major execution and rendering engines used in the Opus 5.5 video corpus, including deterministic frame capture, subframe temporal anti-aliasing, and FFmpeg master encoding.

---

## 1. Engine A: HyperFrames (HTML / CSS / Web Component Video)

HyperFrames is the specialized declarative framework for code video, natively supported in this environment (`/Users/macbookpro/.nvm/versions/node/v22.21.1/bin/hyperframes`).

### Project Setup
```bash
# Scaffold a new HyperFrames project
npx hyperframes init my-video
cd my-video

# Check project health
npx hyperframes check

# Preview in live interactive studio
npx hyperframes preview

# Render to MP4
npx hyperframes render --output master.mp4
```

### Composition Contract (`index.html`)
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body class="hyperframes-composition" data-duration="15s" data-fps="60" data-width="1920" data-height="1080">
  <div class="track" data-track="main">
    <!-- Clip 1: 0s to 4s -->
    <div class="clip hero" data-start="0s" data-duration="4s" data-in="fade" data-out="zoom">
      <h1 class="kinetic-text">Precision Redefined</h1>
    </div>
    <!-- Clip 2: 4s to 10s -->
    <div class="clip product" data-start="4s" data-duration="6s">
      <div class="ui-surface">...</div>
    </div>
    <!-- Clip 3: 10s to 15s -->
    <div class="clip payoff" data-start="10s" data-duration="5s">
      <div class="brand-resolve">...</div>
    </div>
  </div>
</body>
</html>
```

---

## 2. Engine B: Pure Canvas + Headless Chrome + FFmpeg (Zero-Dependency)

This is the most portable and resilient pipeline. It requires zero video framework dependencies—just a browser canvas and an FFmpeg command.

### Deterministic Architecture (`index.html`)
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { margin: 0; background: #0c0f1a; overflow: hidden; }
    canvas { width: 100vw; height: 100vh; object-fit: contain; }
  </style>
</head>
<body>
  <canvas id="c" width="1920" height="1080"></canvas>
  <script>
    const canvas = document.getElementById('c');
    const ctx = canvas.getContext('2d');
    
    // Closed-form critically damped spring: f(t) in [0, 1]
    function spring(t, delay = 0, omega = 10.0) {
      if (t < delay) return 0;
      const tau = t - delay;
      return 1 - (1 + omega * tau) * Math.exp(-omega * tau);
    }
    
    // PURE FUNCTION OF TIME: window.seek(t)
    // No timers, no RAF, no state saved between frames.
    window.seek = function(t) {
      const W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);
      
      // Draw everything purely based on t
      const progress = spring(t, 0.5, 8.0);
      ctx.save();
      ctx.translate(W/2, H/2);
      ctx.scale(progress, progress);
      ctx.fillStyle = '#e8b84b';
      ctx.font = 'bold 72px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Autonomous Video', 0, 0);
      ctx.restore();
    };
    
    // Live loop for browser inspection
    let start = performance.now();
    function loop(now) {
      window.seek(((now - start) / 1000) % 15.0);
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
  </script>
</body>
</html>
```

### Deterministic Playwright Capture Script (`render.js`)
```javascript
const { chromium } = require('playwright');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.resolve(__dirname, 'index.html'));
  
  const framesDir = path.join(__dirname, 'frames');
  fs.mkdirSync(framesDir, { recursive: true });
  
  const FPS = 60;
  const DURATION = 15;
  const TOTAL_FRAMES = FPS * DURATION;
  
  console.log(`Rendering ${TOTAL_FRAMES} frames at 60fps...`);
  for (let i = 0; i < TOTAL_FRAMES; i++) {
    const t = i / FPS;
    await page.evaluate((time) => window.seek(time), t);
    const frameFile = path.join(framesDir, `frame_${String(i).padStart(5, '0')}.png`);
    await page.screenshot({ path: frameFile, type: 'png' });
    if (i % 60 === 0) console.log(`Progress: ${(i / TOTAL_FRAMES * 100).toFixed(1)}%`);
  }
  await browser.close();
  
  console.log("Encoding with FFmpeg...");
  execSync(`ffmpeg -y -framerate 60 -i "${framesDir}/frame_%05d.png" -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 18 -movflags +faststart output.mp4`, { stdio: 'inherit' });
  console.log("Done: output.mp4");
})();
```

---

## 3. Engine C: Remotion (React-Based Video)

Used heavily for React-first workflows where UI components are already built in React/Tailwind.

### Composition Setup
```bash
npx create-video --template blank
npm install @remotion/cli
```

### Spring Easing in Remotion
```tsx
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const MyScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame: frame - 15, // start at frame 15
    fps,
    config: {
      damping: 15,
      mass: 0.8,
      stiffness: 100,
      overshootClamping: false,
    },
  });

  return (
    <div style={{ transform: `scale(${scale})` }}>
      <FinanzCockpit />
    </div>
  );
};
```

### Rendering Remotion Headless
```bash
npx remotion render src/index.ts MainComposition out/video.mp4 --codec=h264 --crf=18
```

---

## 4. Engine D: Three.js & WebGL Shaders

For 3D worlds, procedural terrain, and GLSL fluid/fire shaders.

### Offscreen Canvas Rendering Pattern
```javascript
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, 1920 / 1080, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('c'), antialias: true });
renderer.setSize(1920, 1080);

window.seek = function(t) {
  // Update uniforms or camera trajectory mathematically:
  camera.position.x = Math.sin(t * 0.5) * 15;
  camera.position.z = Math.cos(t * 0.5) * 15;
  camera.lookAt(0, 0, 0);
  
  // Pass time to custom shader material:
  customShaderMaterial.uniforms.u_time.value = t;
  
  renderer.render(scene, camera);
};
```

---

## 5. Master FFmpeg Assembly & Audio Muxing

### Standard Clean Video Master
```bash
ffmpeg -y -framerate 60 -i frames/frame_%05d.png \
  -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 18 \
  -movflags +faststart master.mp4
```

### Muxing Audio with Loudness Normalization (-14 LUFS)
```bash
ffmpeg -y -i master.mp4 -i soundtrack.wav \
  -c:v copy -c:a aac -b:a 320k \
  -filter:a "loudnorm=I=-14:TP=-1.5:LRA=11" \
  final_with_sound.mp4
```

### Contact Sheet Generator for Visual Inspection
Generate 1 still per second to visually inspect before full render:
```bash
ffmpeg -i output.mp4 -vf "fps=1,scale=480:-1,tile=5x3" contact_sheet.png
```
