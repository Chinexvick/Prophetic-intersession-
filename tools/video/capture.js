const { chromium, devices } = require('playwright');
(async () => {
  const out = process.argv[2], U = 'https://prophetic-intercession-vick22.vercel.app/';
  const b = await chromium.launch();
  async function prep(p) {
    await p.evaluate(async () => {
      document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager');
      document.querySelectorAll('.reveal').forEach(e => e.classList.add('in'));
      for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 100)); }
      window.scrollTo(0, 0);
    });
    await p.waitForTimeout(1500);
  }
  // desktop full home for laptop scroll
  const d = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await d.goto(U, { waitUntil: 'networkidle' }); await prep(d);
  await d.screenshot({ path: out + '/home-desk-full.jpg', fullPage: true, type: 'jpeg', quality: 85 });
  // viewport shots of features (scroll element to near top)
  async function shot(path, sel, name, offset = 90) {
    await d.goto(U + path, { waitUntil: 'networkidle' }); await prep(d);
    if (sel) await d.evaluate(([s, o]) => { const e = document.querySelector(s); window.scrollTo(0, e.getBoundingClientRect().top + scrollY - o); }, [sel, offset]);
    await d.waitForTimeout(900);
    await d.screenshot({ path: `${out}/${name}.jpg`, type: 'jpeg', quality: 88 });
  }
  await shot('prophetic.html', '#watch-filters', 'watch', 150);
  await shot('blog-post.html?p=how-prophetic-intercession-began', null, 'blog-post');
  await shot('blog.html', '.blog-tools', 'blog-list', 120);
  await d.goto(U + 'give.html#crypto', { waitUntil: 'networkidle' }); await prep(d);
  await d.evaluate(() => { const e = document.querySelector('#give-engine'); window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 110); });
  await d.waitForTimeout(1500); await d.click('.ge-qr-toggle'); await d.waitForTimeout(800);
  await d.screenshot({ path: out + '/give.jpg', type: 'jpeg', quality: 88 });
  // mobile full home for phone
  const ctx = await b.newContext({ ...devices['iPhone 13'] });
  const m = await ctx.newPage(); await m.goto(U, { waitUntil: 'networkidle' }); await prep(m);
  await m.screenshot({ path: out + '/home-mob-full.jpg', fullPage: true, type: 'jpeg', quality: 85 });
  await m.goto(U + 'give.html', { waitUntil: 'networkidle' }); await prep(m);
  await m.evaluate(() => { const e = document.querySelector('#give-engine'); window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 70); });
  await m.waitForTimeout(1500);
  await m.screenshot({ path: out + '/give-mob.jpg', type: 'jpeg', quality: 88 });
  await b.close();
})();
