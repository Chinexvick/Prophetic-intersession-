// usage: node render.js out.mp4 [vertical] [fps] [from] [to]  |  node render.js --stills dir [vertical]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const args = process.argv.slice(2);
  const stills = args[0] === '--stills';
  const vertical = args.includes('vertical');
  const W = vertical ? 1080 : 1920, H = vertical ? 1920 : 1080;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: W, height: H } });
  await p.goto('file://' + path.resolve(__dirname, 'stage.html') + (vertical ? '?v=1' : ''), { waitUntil: 'networkidle' });
  await p.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(i => i.decode().catch(() => {}))); });
  const dur = await p.evaluate(() => window.DURATION);
  if (stills) {
    const times = [2.5, 7.5, 12.5, 16, 19.5, 23.5, 28.5, 33.5, 38.5, 43.8, 48.5, 54.5];
    for (const t of times) { await p.evaluate(t => renderAt(t), t); await p.screenshot({ path: `${args[1]}/t${String(t).padStart(4, '0')}${vertical ? 'v' : ''}.jpg`, type: 'jpeg', quality: 70 }); }
    await b.close(); return;
  }
  const out = args[0], fps = 30;
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const frames = Math.round(dur * fps);
  const t0 = Date.now();
  for (let f = 0; f < frames; f++) {
    await p.evaluate(t => renderAt(t), f / fps);
    const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 300 === 0) console.log(`frame ${f}/${frames}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await b.close();
  console.log('done', out);
})();
