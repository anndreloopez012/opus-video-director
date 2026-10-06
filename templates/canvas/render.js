const { chromium } = require('playwright');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  console.log("Launching Headless Chrome for deterministic 60fps frame capture...");
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  
  const fileUrl = 'file://' + path.resolve(__dirname, 'index.html');
  await page.goto(fileUrl);
  
  const framesDir = path.join(__dirname, 'frames');
  fs.mkdirSync(framesDir, { recursive: true });
  
  const FPS = 60;
  const DURATION = 15;
  const TOTAL_FRAMES = FPS * DURATION;
  
  console.log(`Rendering ${TOTAL_FRAMES} frames at 1920x1080 60fps...`);
  for (let i = 0; i < TOTAL_FRAMES; i++) {
    const t = i / FPS;
    await page.evaluate((time) => window.seek(time), t);
    const framePath = path.join(framesDir, `frame_${String(i).padStart(5, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });
    if (i % 60 === 0) console.log(`  Frame ${i}/${TOTAL_FRAMES} (${(i/TOTAL_FRAMES*100).toFixed(1)}%)`);
  }
  await browser.close();
  
  console.log("Encoding video with FFmpeg...");
  const outMp4 = path.join(__dirname, 'output.mp4');
  execSync(`ffmpeg -y -framerate ${FPS} -i "${framesDir}/frame_%05d.png" -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 18 -movflags +faststart "${outMp4}"`, { stdio: 'inherit' });
  console.log(`Video generated successfully: ${outMp4}`);
})();
