#!/usr/bin/env python3
"""
Opus Video Director CLI (opus_videos.py)
Search, inspect, analyze, and scaffold video projects across the 475 Opus 5.5 / Skillry video collection.
Compatible with Claude Code, Antigravity, and Codex.
"""

import os
import sys
import json
import argparse
import collections

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'references', 'catalog.json'))

def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        print(f"Error: Catalog not found at {CATALOG_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def cmd_stats(args, data):
    videos = data['videos']
    archetypes = data['archetypes']
    print(f"==================================================")
    print(f" OPUS 5.5 VIDEO CATALOG STATISTICS")
    print(f" Total Videos: {len(videos)}")
    print(f" Archetypes:   {len(archetypes)}")
    print(f"==================================================")
    
    arch_counts = collections.Counter(v['archetype'] for v in videos)
    print("\n[Video Distribution by Archetype]")
    for a in archetypes:
        aid = a['id']
        cnt = arch_counts.get(aid, 0)
        pct = (cnt / len(videos)) * 100
        print(f"  {aid:22} | {cnt:3} videos ({pct:4.1f}%) | {a['title']}")
        
    tag_counts = collections.Counter(t for v in videos for t in v.get('tags', []))
    print("\n[Tech Stacks & Tags]")
    for tag, cnt in tag_counts.most_common(12):
        print(f"  {tag:18} : {cnt:3} videos")
        
    aspects = collections.Counter(v.get('aspect', '16:9') for v in videos)
    print("\n[Aspect Ratios]")
    for asp, cnt in aspects.items():
        print(f"  {asp:8} : {cnt:3} videos")

def cmd_archetypes(args, data):
    archetypes = data['archetypes']
    videos = data['videos']
    arch_counts = collections.Counter(v['archetype'] for v in videos)
    print(f"Total Archetypes: {len(archetypes)}\n")
    for a in archetypes:
        cnt = arch_counts.get(a['id'], 0)
        print(f"ID:          {a['id']}")
        print(f"Title:       {a['title']} ({cnt} videos)")
        print(f"Keywords:    {', '.join(a['keywords'][:8])}")
        print(f"Description: {a['description']}")
        print("-" * 60)

def cmd_list(args, data):
    videos = data['videos']
    if args.archetype:
        videos = [v for v in videos if v['archetype'] == args.archetype]
    if args.tag:
        videos = [v for v in videos if args.tag.lower() in [t.lower() for t in v.get('tags', [])]]
    if args.aspect:
        videos = [v for v in videos if v.get('aspect') == args.aspect]
        
    total_matches = len(videos)
    limit = args.limit or 25
    videos = videos[:limit]
    
    print(f"Found {total_matches} videos (showing {len(videos)}):")
    print(f"{'ID':<4} | {'SLUG':<25} | {'ARCHETYPE':<20} | {'DUR':<5} | {'ASPECT':<6} | {'AUTHOR'}")
    print("-" * 80)
    for v in videos:
        print(f"{v['id']:<4} | {v['slug']:<25} | {v['archetype']:<20} | {v['duration']:<5.1f} | {v['aspect']:<6} | @{v['author']}")

def cmd_search(args, data):
    query = args.query.lower()
    videos = data['videos']
    matches = []
    for v in videos:
        score = 0
        prompt_lower = v.get('prompt', '').lower()
        slug_lower = v.get('slug', '').lower()
        author_lower = v.get('author', '').lower()
        tags_lower = ' '.join(v.get('tags', [])).lower()
        arch_lower = v.get('archetype', '').lower()
        
        if query in slug_lower: score += 10
        if query in arch_lower: score += 8
        if query in tags_lower: score += 6
        if query in author_lower: score += 5
        if query in prompt_lower: score += prompt_lower.count(query) * 2
        
        if score > 0:
            matches.append((score, v))
            
    matches.sort(key=lambda x: -x[0])
    limit = args.limit or 15
    print(f"Search for '{args.query}': {len(matches)} matching videos (showing top {min(limit, len(matches))})\n")
    for score, v in matches[:limit]:
        snip = v['prompt'].replace('\n', ' ')
        if len(snip) > 90: snip = snip[:87] + '...'
        print(f"[{v['id']}] {v['slug']} ({v['archetype']} | {v['duration']}s | {v['aspect']}) - @{v['author']}")
        print(f"     Prompt: {snip}")
        print(f"     Tags: {', '.join(v['tags'])} | URL: {v.get('postUrl','')}\n")

def find_video(term, videos):
    term = str(term).strip()
    if term.isdigit():
        idx = int(term)
        for v in videos:
            if v['id'] == idx:
                return v
    for v in videos:
        if v['slug'].lower() == term.lower():
            return v
    for v in videos:
        if term.lower() in v['slug'].lower():
            return v
    return None

def cmd_inspect(args, data):
    v = find_video(args.target, data['videos'])
    if not v:
        print(f"Error: Video '{args.target}' not found.", file=sys.stderr)
        sys.exit(1)
        
    print("=" * 70)
    print(f" VIDEO DETAILS: {v['slug']} (ID: {v['id']})")
    print("=" * 70)
    print(f"Archetype:        {v['archetype']}")
    print(f"Author:           @{v['author']} ({v.get('authorUrl','')})")
    print(f"Duration:         {v['duration']} seconds")
    print(f"Resolution:       {v['resolution']} ({v['aspect']})")
    print(f"Tech Tags:        {', '.join(v['tags'])}")
    print(f"Post URL:         {v.get('postUrl','')}")
    print(f"Original Video:   {v.get('originalVideoUrl','')}")
    print(f"Live Remake:      {v.get('remakeVideoUrl','')}")
    print(f"Prompt Length:    {v['promptLength']} characters")
    print("-" * 70)
    print("PROMPT RECIPE / INSTRUCTIONS:")
    print("-" * 70)
    print(v['prompt'])
    print("=" * 70)

def cmd_prompt(args, data):
    v = find_video(args.target, data['videos'])
    if not v:
        print(f"Error: Video '{args.target}' not found.", file=sys.stderr)
        sys.exit(1)
    print(v['prompt'])

def cmd_scaffold(args, data):
    archetype = args.archetype
    target_dir = args.target_dir or f"./video_{archetype.replace('-', '_')}"
    stack = (args.stack or 'canvas').lower()
    title = args.title or archetype.replace('-', ' ').title()
    
    os.makedirs(target_dir, exist_ok=True)
    
    if stack == 'canvas':
        # Generate single-file deterministic Canvas HTML + Node rendering script
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ background: #0c0f1a; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }}
    canvas {{ width: 100%; height: 100%; object-fit: contain; }}
  </style>
</head>
<body>
  <canvas id="c" width="1920" height="1080"></canvas>
  <script>
    const canvas = document.getElementById('c');
    const ctx = canvas.getContext('2d');
    const DURATION = 15.0; // seconds
    const FPS = 60;
    
    // Closed-form critically damped spring f(t)
    function spring(t, delay = 0, omega = 12.0) {{
      if (t < delay) return 0;
      const tau = t - delay;
      return 1 - (1 + omega * tau) * Math.exp(-omega * tau);
    }}
    
    // Pure function of time: seekable, deterministic
    window.seek = function(t) {{
      const W = canvas.width;
      const H = canvas.height;
      ctx.clearRect(0, 0, W, H);
      
      // Background gradient
      const bg = ctx.createRadialGradient(W/2, H/2, 100, W/2, H/2, W/1.2);
      bg.addColorStop(0, '#151928');
      bg.addColorStop(1, '#090b12');
      ctx.fillStyle = bg;
      ctx.fillRect(0, 0, W, H);
      
      // Scene progression based on t
      ctx.save();
      const p1 = spring(t, 0.2, 8.0);
      const alpha = Math.min(1, p1);
      const scale = 0.85 + 0.15 * p1;
      
      ctx.translate(W/2, H/2);
      ctx.scale(scale, scale);
      ctx.globalAlpha = alpha;
      
      // Brand Gold Hero Object
      ctx.fillStyle = '#e8b84b';
      ctx.font = 'bold 64px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('{title}', 0, -40);
      
      // Subtitle
      ctx.fillStyle = '#8b93b5';
      ctx.font = '500 28px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
      ctx.fillText('Autonomous AI Motion System', 0, 40);
      
      ctx.restore();
    }};
    
    // Local preview loop
    let startTime = performance.now();
    function loop(now) {{
      const t = ((now - startTime) / 1000) % DURATION;
      window.seek(t);
      requestAnimationFrame(loop);
    }}
    requestAnimationFrame(loop);
  </script>
</body>
</html>
"""
        with open(os.path.join(target_dir, 'index.html'), 'w') as f:
            f.write(html_content)
            
        render_script = f"""const {{ chromium }} = require('playwright');
const {{ execSync }} = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {{
  console.log("Launching Headless Chrome for deterministic 60fps frame capture...");
  const browser = await chromium.launch();
  const page = await browser.newPage({{ viewport: {{ width: 1920, height: 1080 }} }});
  
  const fileUrl = 'file://' + path.resolve(__dirname, 'index.html');
  await page.goto(fileUrl);
  
  const framesDir = path.join(__dirname, 'frames');
  fs.mkdirSync(framesDir, {{ recursive: true }});
  
  const FPS = 60;
  const DURATION = 15;
  const TOTAL_FRAMES = FPS * DURATION;
  
  console.log(`Rendering ${{TOTAL_FRAMES}} frames at 1920x1080 60fps...`);
  for (let i = 0; i < TOTAL_FRAMES; i++) {{
    const t = i / FPS;
    await page.evaluate((time) => window.seek(time), t);
    const framePath = path.join(framesDir, `frame_${{String(i).padStart(5, '0')}}.png`);
    await page.screenshot({{ path: framePath, type: 'png' }});
    if (i % 60 === 0) console.log(`  Frame ${{i}}/${{TOTAL_FRAMES}} (${{(i/TOTAL_FRAMES*100).toFixed(1)}}%)`);
  }}
  await browser.close();
  
  console.log("Encoding video with FFmpeg...");
  const outMp4 = path.join(__dirname, 'output.mp4');
  execSync(`ffmpeg -y -framerate ${{FPS}} -i "${{framesDir}}/frame_%05d.png" -c:v libx264 -pix_fmt yuv420p -profile:v high -crf 18 -movflags +faststart "${{outMp4}}"`, {{ stdio: 'inherit' }});
  console.log(`Video generated successfully: ${{outMp4}}`);
}})();
"""
        with open(os.path.join(target_dir, 'render.js'), 'w') as f:
            f.write(render_script)
            
        package_json = {
            "name": f"video-{archetype}",
            "version": "1.0.0",
            "scripts": {
                "render": "node render.js"
            },
            "dependencies": {
                "playwright": "^1.40.0"
            }
        }
        with open(os.path.join(target_dir, 'package.json'), 'w') as f:
            json.dump(package_json, f, indent=2)

    elif stack == 'hyperframes':
        hf_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body class="hyperframes-composition" data-duration="15s" data-fps="60" data-width="1920" data-height="1080">
  <div class="track" data-track="main">
    <div class="clip hero-scene" data-start="0s" data-duration="5s">
      <h1 class="kinetic-title">{title}</h1>
      <p class="subtitle">Next-Generation Code Video</p>
    </div>
    <div class="clip product-scene" data-start="5s" data-duration="6s">
      <div class="ui-cockpit-card">
        <div class="card-header">Finanzcockpit</div>
        <div class="metric-counter" data-target="148500">€0</div>
      </div>
    </div>
    <div class="clip logo-payoff" data-start="11s" data-duration="4s">
      <div class="wordmark-glint">{title}</div>
    </div>
  </div>
</body>
</html>
"""
        with open(os.path.join(target_dir, 'index.html'), 'w') as f:
            f.write(hf_html)
            
        css_content = """body {
  margin: 0;
  background: #0c0f1a;
  color: #e8eaf2;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  overflow: hidden;
}
.hero-scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.kinetic-title {
  font-size: 72px;
  color: #e8b84b;
  letter-spacing: -0.02em;
}
.subtitle {
  color: #8b93b5;
  font-size: 24px;
}
"""
        with open(os.path.join(target_dir, 'style.css'), 'w') as f:
            f.write(css_content)

    print(f"Scaffolded [{archetype}] project in: {target_dir}")
    print(f"Engine: {stack}")
    print(f"Next steps:")
    if stack == 'canvas':
        print(f"  1. cd {target_dir}")
        print(f"  2. npm install")
        print(f"  3. Open index.html in browser for live preview")
        print(f"  4. Run 'npm run render' to export MP4 via Playwright + FFmpeg")
    elif stack == 'hyperframes':
        print(f"  1. cd {target_dir}")
        print(f"  2. npx hyperframes preview")
        print(f"  3. npx hyperframes render")

def main():
    parser = argparse.ArgumentParser(description="Opus 5.5 Video Director CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # stats
    subparsers.add_parser("stats", help="Show global video catalog stats")
    
    # archetypes
    subparsers.add_parser("archetypes", help="List all 14 video archetypes and descriptions")
    
    # list
    p_list = subparsers.add_parser("list", help="List videos in catalog")
    p_list.add_argument("--archetype", "-a", help="Filter by archetype ID")
    p_list.add_argument("--tag", "-t", help="Filter by technology tag")
    p_list.add_argument("--aspect", help="Filter by aspect ratio (16:9, 9:16, 1:1)")
    p_list.add_argument("--limit", "-n", type=int, default=25, help="Number of records to show")
    
    # search
    p_search = subparsers.add_parser("search", help="Full-text search across prompt recipes")
    p_search.add_argument("query", help="Search keyword")
    p_search.add_argument("--limit", "-n", type=int, default=15, help="Max results")
    
    # inspect
    p_inspect = subparsers.add_parser("inspect", help="Inspect a specific video by ID or slug")
    p_inspect.add_argument("target", help="Video ID (number) or slug")
    
    # prompt
    p_prompt = subparsers.add_parser("prompt", help="Print clean prompt for a video")
    p_prompt.add_argument("target", help="Video ID or slug")
    
    # scaffold
    p_scaffold = subparsers.add_parser("scaffold", help="Scaffold a new video project")
    p_scaffold.add_argument("archetype", help="Archetype ID (e.g. saas-launch, motion-showreel)")
    p_scaffold.add_argument("--target-dir", "-d", help="Destination directory")
    p_scaffold.add_argument("--stack", "-s", choices=["canvas", "hyperframes", "remotion", "threejs"], default="canvas", help="Engine stack")
    p_scaffold.add_argument("--title", help="Video project title")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
        
    data = load_catalog()
    
    if args.command == "stats":
        cmd_stats(args, data)
    elif args.command == "archetypes":
        cmd_archetypes(args, data)
    elif args.command == "list":
        cmd_list(args, data)
    elif args.command == "search":
        cmd_search(args, data)
    elif args.command == "inspect":
        cmd_inspect(args, data)
    elif args.command == "prompt":
        cmd_prompt(args, data)
    elif args.command == "scaffold":
        cmd_scaffold(args, data)

if __name__ == '__main__':
    main()
