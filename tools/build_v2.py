"""Generates Version B (ultra-modern) of the Prophetic Intercession site into v2/.
Same content and data files as Version A; new layouts, CSS (v2.css) and motion (app.js)."""
import os, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent / "v2"

WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.05 21.5a9.43 9.43 0 0 1-4.8-1.32l-.35-.2-3.57.93.96-3.48-.23-.36a9.4 9.4 0 0 1-1.44-5.02c0-5.2 4.24-9.44 9.45-9.44 2.52 0 4.89.99 6.67 2.77a9.37 9.37 0 0 1 2.76 6.68c0 5.21-4.24 9.44-9.44 9.44m8.04-17.48A11.3 11.3 0 0 0 12.05.7C5.78.7.68 5.8.68 12.06c0 2 .52 3.96 1.52 5.68L.58 23.7l6.1-1.6a11.36 11.36 0 0 0 5.37 1.37c6.26 0 11.36-5.1 11.36-11.37 0-3.03-1.18-5.89-3.33-8.03"/></svg>'
YT = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6z"/></svg>'
TT = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19.6 6.7a4.8 4.8 0 0 1-3.8-4.2V2h-3.4v13.7a2.9 2.9 0 1 1-2-2.7V9.5a6.3 6.3 0 1 0 5.4 6.2V8.8a8.2 8.2 0 0 0 4.8 1.5V6.9a4.8 4.8 0 0 1-1-.2z"/></svg>'
ZOOM = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M2 7.5A2.5 2.5 0 0 1 4.5 5h9A2.5 2.5 0 0 1 16 7.5v9a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 2 16.5zm15 2.3 4.2-2.9c.36-.25.8 0 .8.43v9.34c0 .43-.44.68-.8.43L17 14.2z"/></svg>'
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
I = {
 "flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
 "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
 "ear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>',
 "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 17.5 3 6V3h3l11.5 11.5M13 19l6-6M16 16l4 4M19 21l2-2"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
 "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg>',
}

NAV = [("index.html", "Home"), ("about.html", "About"), ("prophetic.html", "Prophetic Watch"), ("blog.html", "Blog"), ("media.html", "Media")]
MENU = [("index.html", "Home"), ("about.html", "About <span class='serif'>us</span>"), ("convener.html", "Our convener"),
        ("prayer.html", "Prayer"), ("prophetic.html", "Prophetic <span class='serif'>watch</span>"), ("blog.html", "Blog"),
        ("media.html", "Media"), ("gallery.html", "Gallery"), ("events.html", "Events"), ("outreach.html", "Outreach"),
        ("channels.html", "Channels"), ("testimonies.html", "Testimonies"), ("give.html", "Give <span class='serif'>a seed</span>")]


def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#fbf7f4">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/img/gallery/g14.jpg">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800&family=Inter+Tight:wght@400;500;600&family=Instrument+Serif:ital@1&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/v2.css">
</head>'''


def chrome_top(active):
    links = "".join(f'<li><a href="{h}"{" aria-current=page" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    menu = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in MENU)
    return f'''<div class="pt" aria-hidden="true"></div>
<header class="nav">
  <a class="nav-brand" href="index.html"><img src="assets/img/logo.png" alt="Prophetic Intercession logo" width="40" height="40"><span>Prophetic Intercession</span></a>
  <ul class="nav-links">{links}</ul>
  <div class="nav-right">
    <a class="btn btn-rose btn-give" href="give.html">Give</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu"><i></i><span>Menu</span></button>
  </div>
</header>
<nav class="menu" id="menu" aria-hidden="true" aria-label="Site">
  <ol>{menu}</ol>
  <div class="menu-side">
    <div class="card"><img src="assets/img/gallery/g14-sm.jpg" alt=""><span class="label">Join the prayer family</span><p style="margin:.6em 0 1em;color:rgba(255,255,255,.7)">Prayer alerts, fliers and Zoom links are shared first in our WhatsApp group.</p><a class="btn btn-whatsapp" data-link="whatsapp" href="channels.html">{WA} Join on WhatsApp</a></div>
    <div><span class="label">Follow</span><div class="socials" style="margin-top:12px"><a data-link="whatsapp" href="channels.html" aria-label="WhatsApp">{WA}</a><a data-link="youtube" href="channels.html" aria-label="YouTube">{YT}</a><a data-link="tiktok" href="channels.html" aria-label="TikTok">{TT}</a></div></div>
  </div>
</nav>'''


FOOT = f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div><img src="assets/img/logo.png" alt="" width="64" height="64" style="border-radius:50%;box-shadow:0 0 0 1.5px var(--gold)"><p style="margin:18px 0 0;color:rgba(255,255,255,.7);max-width:34ch">A global interdenominational ministry — a people upon the watch, a people consecrated to the altar.</p>
        <div class="socials"><a data-link="whatsapp" href="channels.html" aria-label="WhatsApp">{WA}</a><a data-link="youtube" href="channels.html" aria-label="YouTube">{YT}</a><a data-link="tiktok" href="channels.html" aria-label="TikTok">{TT}</a></div></div>
      <div><h4>Ministry</h4><ul><li><a href="about.html">About</a></li><li><a href="convener.html">Our Convener</a></li><li><a href="outreach.html">Outreach</a></li><li><a href="testimonies.html">Testimonies</a></li></ul></div>
      <div><h4>Grow</h4><ul><li><a href="prophetic.html">Prophetic Watch</a></li><li><a href="blog.html">Blog</a></li><li><a href="media.html">Media</a></li><li><a href="gallery.html">Gallery</a></li></ul></div>
      <div><h4>Join</h4><ul><li><a href="prayer.html">Prayer</a></li><li><a href="events.html">Events</a></li><li><a href="channels.html">Channels</a></li><li><a href="give.html">Give</a></li></ul></div>
    </div>
    <div class="foot-word" aria-hidden="true">Raising a Tribe.</div>
    <div class="foot-bottom"><span>© <span data-year>2026</span> Prophetic Intercession</span><span>“I will stand upon my watch” — Habakkuk 2:1</span><span>propheticintercession.org</span></div>
  </div>
</footer>'''

GIVE_CTA = f'''<section class="sec dark">
  <div class="wrap cta-big rv">
    <span class="label">Partner with us</span>
    <h2 style="margin:.3em 0 .4em">Keep the <span class="serif">altar</span> burning.</h2>
    <p class="muted" style="max-width:46ch;margin:0 auto 30px">Every seed fuels prayer, prison outreach, rural missions and the orphanage we are building.</p>
    <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap"><a class="btn btn-rose" href="give.html">Give a seed <span class="arr">{ARR}</span></a><a class="btn btn-ghost" href="prayer.html">Send a prayer request</a></div>
  </div>
</section>'''


def page(fname, title, desc, body, scripts=""):
    html = (head(title, desc) + "\n<body>\n" + chrome_top(fname) + "\n<main>\n" + body.strip() + "\n</main>\n" + FOOT +
            "\n" + scripts + '<script src="assets/js/content.js"></script>\n<script src="assets/js/engine.js"></script>\n<script src="assets/js/app.js"></script>\n</body>\n</html>\n')
    (ROOT / fname).write_text(html)


def phero(label, title_html, lede, img=None, pos="center 30%"):
    im = f'<div class="phero-img rv grain"><img src="assets/img/{img}" alt="" style="object-position:{pos}"></div>' if img else ""
    return f'''<section class="phero"><div class="wrap">
  <span class="label rv">{label}</span>
  <h1 class="split"><span class="split-line"><span>{title_html}</span></span></h1>
  <p class="lede rv" style="--d:.15s">{lede}</p>
  {im}
</div></section>'''


def feat(icon, h, p, small=""):
    return f'<div class="feat rv"><div class="ic">{I[icon]}</div><h3>{h}</h3><p>{p}</p>{f"<small>{small}</small>" if small else ""}</div>'


MANDATE = [
 ("Raising a Prophetic and Intercessory Generation", "To raise, disciple and equip a consecrated people who understand the ministry of prayer, develop intimacy with God, discern His voice and faithfully stand in the gap for individuals, families, communities and nations.", "Ezekiel 22:30 · 1 Timothy 2:1–4 · Isaiah 62:6–7"),
 ("Birthing and Sustaining Genuine Revival", "To become a spiritual catalyst for revival through persistent intercession, consecration, repentance and the stirring of spiritual hunger, raising people who will contend for a fresh move of God in the Church and across the nations.", "Habakkuk 3:2 · Acts 2:1–4 · Joel 2:28–29 · 2 Chronicles 7:14"),
 ("Awakening Gifts, Callings and Spiritual Destinies", "To create an atmosphere of spiritual growth, impartation, discipleship and prophetic activation where believers discover, develop and deploy their God-given gifts, callings and assignments for kingdom advancement.", "2 Timothy 1:6 · 1 Timothy 4:14 · Ephesians 4:11–13 · Romans 12:6–8"),
 ("Demonstrating the Supernatural Reality of the Risen Christ", "To cultivate a community that believes, pursues and demonstrates the supernatural ministry of the Holy Spirit through the gifts of the Spirit, divine healing, miracles, signs and wonders, bringing glory to Jesus Christ.", "Mark 16:17–20 · Acts 4:29–33 · Hebrews 2:3–4 · 1 Corinthians 2:4–5"),
 ("Evangelism", "To labour in intercession for the salvation of the lost and translate this burden into intentional evangelism that brings people into the knowledge of Jesus Christ.", "Romans 10:1 · 2 Corinthians 5:18–20 · 2 Corinthians 4:3 · Matthew 28:19–20"),
 ("A Global Network of Prayer and Spiritual Collaboration", "To unite believers, prayer movements, churches and ministries across denominations, cultures and nations into a global fellowship of intercessors, fostering corporate prayer, prophetic accountability and kingdom partnerships.", "John 17:20–23 · Acts 1:14 · Matthew 18:19–20 · Ephesians 4:3–6"),
 ("The Compassion of Christ Through Social Impact", "To translate spiritual convictions into tangible expressions of Christ’s love by reaching the vulnerable, helping the helpless, supporting disadvantaged communities and initiating humanitarian projects that restore dignity.", "Isaiah 58:6–12 · James 1:27 · Matthew 25:35–40 · Acts 10:38"),
]
PILLARS = [("flame", "Prayer & Intercession", "“We will give ourselves continually to prayer, and to the ministry of the word.”", "Acts 6:4 · Isaiah 62:6–7"),
 ("shield", "Consecration", "Living a life worthy and pleasing unto God.", "John 17:19 · Romans 12:1 · Galatians 2:20"),
 ("book", "The Word of God", "We labour in the word of God and doctrine.", "John 8:32 · Psalm 107:20"),
 ("ear", "Prophetic Awakening", "Fulfilling God’s mandate on our prophetic destinies.", "1 Samuel 3:8–11 · Joel 2:28–29"),
 ("key", "Warfare", "Advancing the kingdom across lives and territories through warfare.", "Ephesians 6:12 · 2 Corinthians 10:3–5"),
 ("globe", "Evangelism & Kingdom Service", "Taking the gospel to the ends of the earth.", "Romans 10:14 · 2 Timothy 4:5"),
 ("spark", "Miracles & the Supernatural", "He confirmed His word with signs following.", "Mark 16:20 · 1 Corinthians 12:10 · Acts 19:11")]

def stack_cards():
    return "".join(f'''<article class="stack-card" style="--i:{i}"><div class="n">0{i+1}</div><h3>{t}</h3><div><p>{d}</p><small>{s}</small></div></article>''' for i, (t, d, s) in enumerate(MANDATE))

MARQUEE = '<div class="marquee rose"><div class="marquee-track">' + ("<span>Raising a <em>Tribe</em></span><span>Birthing <em>Revival</em></span><span>Transforming <em>Nations</em></span>" * 4) + '</div></div>'

# ============================== HOME ==============================
home = f'''
<section class="hero">
  <div class="hero-top">
    <h1 class="split"><span class="split-line"><span>Prophetic</span></span><span class="split-line"><span style="--d:.12s"><span class="serif">intercession</span></span></span></h1>
    <div class="hero-meta rv" style="--d:.3s">
      <span class="label">A global interdenominational ministry</span>
      <p>A global prayer community connecting people through powerful online prayer gatherings on Zoom, TikTok &amp; YouTube.</p>
      <div class="hero-actions"><a class="btn btn-whatsapp" data-link="whatsapp" href="channels.html">{WA} Join the prayer group</a><a class="btn btn-ghost" href="prayer.html">Prayer request</a></div>
    </div>
  </div>
  <div class="hero-stage grain">
    <img src="assets/img/hero-worship.jpg" alt="Worshippers lifting their hands in prayer" fetchpriority="high">
    <div class="hero-float hero-session session-card" data-next-session></div>
    <a class="hero-float hero-convener" href="convener.html"><img src="assets/img/gallery/g14-sm.jpg" alt=""><span><strong>Prophetic Intercessor</strong><small>Convener &amp; host</small></span></a>
    <div class="hero-scroll"><i>↓</i>Scroll</div>
  </div>
</section>

{MARQUEE}

<section class="sec statement">
  <div class="wrap">
    <span class="label rv">Who we are</span>
    <p style="margin-top:26px">We are not raising people who merely know how to pray. We are raising people who <span class="serif">know the God</span> to whom they pray, discern the purposes of His heart and become answers to the prayers they offer.</p>
    <div class="statement-foot rv"><a class="btn btn-ink" href="about.html">Our story <span class="arr">{ARR}</span></a><span class="mono muted">Habakkuk 2:1 · Isaiah 62:6–7 · Ezekiel 22:30</span></div>
  </div>
</section>

<section class="sec-sm" style="padding-top:0">
  <div class="wrap">
    <div class="head"><div><span class="label rv">Explore</span><h2 class="rv">Everything in <span class="serif">one place</span></h2></div><p class="rv">Prophetic words, teachings, prayer, giving and the stories of what God is doing — all in one home.</p></div>
    <div class="bento">
      <a class="tile photo t-a rv" href="prophetic.html"><img src="assets/img/gallery/g05.jpg" alt="" style="object-position:center 25%"><span class="go">{ARR}</span><span class="label" style="color:#fff">New · Prophetic Watch</span><div><h3>Words &amp; warnings, <span class="serif">watched over</span></h3><p>Every word is published, prayed over and tracked until it comes to pass.</p></div></a>
      <a class="tile ink t-b rv" href="blog.html" style="--d:.05s"><span class="go">{ARR}</span><span class="label">Blog</span><div><h3>Stories &amp; <span class="serif">teachings</span></h3><p>Outreach reports, event recaps and the Word.</p></div></a>
      <a class="tile rose t-c rv" href="give.html" style="--d:.1s"><span class="go">{ARR}</span><span class="label" style="color:#fff">Give</span><div><h3>Sow in <span class="serif">seconds</span></h3><p>MTN MoMo · Zelle · BNB / USDT</p></div></a>
      <a class="tile blush t-d rv" href="prayer.html"><span class="go">{ARR}</span><span class="label">Prayer</span><div><div class="big-num">24/7</div><p>Send a request, take a watch on the altar, track your Bible reading.</p></div></a>
      <a class="tile photo t-e rv" href="gallery.html" style="--d:.05s"><img src="assets/img/gallery/g03-sm.jpg" alt="" style="object-position:center 25%"><span class="go">{ARR}</span><span class="label" style="color:#fff">Gallery</span><div><h3>Moments in <span class="serif">ministry</span></h3></div></a>
      <a class="tile gold t-f rv" href="channels.html" style="--d:.1s"><span class="go">{ARR}</span><span class="label" style="color:var(--ink)">Pray online</span><div><div class="icons"><span style="background:#25d366;color:#fff">{WA}</span><span style="background:#2d8cff;color:#fff">{ZOOM}</span><span style="background:#111;color:#fff">{TT}</span><span style="background:#ff0033;color:#fff">{YT}</span></div><p style="color:var(--ink)">WhatsApp · Zoom · TikTok · YouTube</p></div></a>
    </div>
  </div>
</section>

<section class="sec dark card-sec" style="background:var(--ink)">
  <div class="wrap">
    <div class="head"><div><span class="label rv">Our sevenfold mandate</span><h2 class="rv" style="color:#fff">Raising a prophetic &amp; intercessory <span class="serif" style="color:var(--rose)">tribe</span></h2></div><p class="rv">Seven assignments that shape everything we pray for and every place we go.</p></div>
    <div class="stack">{stack_cards()}</div>
  </div>
</section>

<section class="hscroll" style="background:var(--paper)">
  <div class="hscroll-pin">
    <div class="hscroll-track">
      <div class="h-intro"><span class="label">Outreach</span><h2>Prayer with <span class="serif">hands &amp; feet</span></h2><p class="muted">What we receive on our knees, we carry into the world.</p><a class="btn btn-ink" href="outreach.html" style="align-self:flex-start">All outreach <span class="arr">{ARR}</span></a></div>
      <a class="h-card" href="outreach.html#prison"><img src="https://i.ytimg.com/vi/W36f2nty25o/hqdefault.jpg" alt=""><span class="status done">Completed · Douala</span><h3>Prison outreach</h3><p>Prayer and the Gospel behind prison walls in Douala, Cameroon.</p></a>
      <a class="h-card" href="outreach.html#rural"><img src="assets/img/rural-missions.jpg" alt=""><span class="status done">Supported</span><h3>Rural missions</h3><p>Standing with the Gospel in remote, overlooked communities.</p></a>
      <a class="h-card" href="outreach.html#orphanage"><img src="assets/img/orphanage.jpg" alt=""><span class="status prog">In progress</span><h3>The orphanage</h3><p>A loving, Christ-centred home for children who need a family.</p></a>
      <a class="h-card" href="outreach.html#future"><img src="assets/img/schools.jpg" alt=""><span class="status">Future vision</span><h3>Hospitals &amp; schools</h3><p>Healing and education for the communities we serve.</p></a>
    </div>
  </div>
</section>

<section class="sec dark" style="border-radius:var(--r-xl) var(--r-xl) 0 0">
  <div class="wrap">
    <div class="head"><div><span class="label rv">Latest on YouTube · updates automatically</span><h2 class="rv" style="color:#fff">Watch &amp; <span class="serif" style="color:var(--rose)">pray</span></h2></div><a class="btn btn-ghost rv" data-link="youtube" href="media.html">Subscribe {YT}</a></div>
    <div class="media-grid" id="latest-videos"></div>
  </div>
</section>

<section class="sec" style="background:var(--paper);border-radius:var(--r-xl) var(--r-xl) 0 0;margin-top:-48px;position:relative">
  <div class="wrap">
    <div class="head"><div><span class="label rv">From the blog</span><h2 class="rv">Stories of <span class="serif">grace</span></h2></div><a class="btn btn-ghost rv" href="blog.html">All articles</a></div>
    <div class="post-grid" id="latest-posts"></div>
  </div>
</section>

<section class="sec-sm" style="padding-top:0">
  <div class="wrap"><div class="head" style="margin-bottom:28px"><div><span class="label rv">Gallery</span><h2 class="rv">Moments in <span class="serif">ministry</span></h2></div><a class="btn btn-ghost rv" href="gallery.html">View gallery</a></div></div>
  <div class="marquee-photos" data-marquee></div>
</section>

<section class="sec">
  <div class="wrap convener">
    <div class="convener-photo rv"><img src="assets/img/gallery/g14.jpg" alt="Prophetic Intercessor ministering"><span class="tag">Convener &amp; host</span></div>
    <div class="rv" style="--d:.1s">
      <span class="label">Meet our convener</span>
      <p class="quote">“Prayer is not an event — it is a <b>lifestyle</b>. Everything by priesthood.”</p>
      <p class="muted" style="max-width:48ch">In the wake of 2020, God birthed in her the vision of Prophetic Intercession. From 2023 she began gathering people on YouTube for extended hours of prayer — today a global prophetic and intercessory tribe.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:24px"><a class="btn btn-ink" href="convener.html">Her story <span class="arr">{ARR}</span></a><a class="btn btn-yt" data-link="youtube" href="media.html">{YT} Watch on YouTube</a></div>
    </div>
  </div>
</section>

<section class="sec-sm" style="padding-top:0"><div class="wrap"><div class="panel blush rv" style="display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center"><div class="focus-box" data-focus></div><a class="btn btn-ink" href="prayer.html">Pray with us <span class="arr">{ARR}</span></a></div></div></section>
''' + GIVE_CTA
page("index.html", "Prophetic Intercession — Raising a Tribe. Birthing Revival. Transforming Nations.",
     "A global interdenominational ministry raising a prophetic and intercessory tribe. Pray with us online on Zoom, TikTok and YouTube.",
     home, '<script src="assets/js/events.js"></script>\n<script src="assets/js/blog.js"></script>\n')

# ============================== ABOUT ==============================
pillars = "".join(feat(ic, t, d, s) for ic, t, d, s in PILLARS)
about = phero("About us", "A <span class='serif'>tribe</span> upon the watch",
              "Prophetic Intercession is a global prophetic and intercessory movement — interdenominational, Christ-centred and led by the Spirit of God.",
              "gallery/g01.jpg", "center 28%") + f'''
<section class="sec"><div class="wrap g2">
  <div class="rv"><span class="label">The birth of the vision</span><h2 style="font-size:clamp(2.4rem,5vw,4.2rem);margin-top:.4em">From a burden to a <span class="serif">global mandate</span></h2></div>
  <div class="rv" style="--d:.1s"><p>The vision of Prophetic Intercession was birthed in the wake of 2020, out of a deep spiritual burden for prayer, revival and the emergence of a generation of prophetic intercessors.</p><p>It found full expression in <strong>2023 through YouTube</strong>, where people gathered for extended hours of prayer, standing in the gap for individuals, families and nations.</p><p class="muted">What began as a burden to pray for people has grown into a greater mandate: raising a global prophetic and intercessory tribe equipped to discern the heart of God, birth His purposes through prayer and become instruments of divine intervention in their generation.</p></div>
</div></section>
{MARQUEE}
<section class="sec dark"><div class="wrap g2" style="align-items:stretch">
  <div class="panel rv"><span class="label">Our vision</span><p class="quote" style="font-size:clamp(1.8rem,3vw,2.6rem)">To raise a generation of prophetic intercessors who will discern the heart of God, birth His purposes and manifest His glory across the nations.</p><span class="mono" style="color:var(--gold-soft)">Habakkuk 2:1 · Isaiah 62:6–7 · Ezekiel 22:30 · Acts 2:17–18</span></div>
  <div class="panel rv" style="--d:.1s"><span class="label">Our mission</span><p class="quote" style="font-size:clamp(1.8rem,3vw,2.6rem)">To cultivate a global community of prayer, prophetic expression, spiritual awakening and kingdom intervention — equipping believers across denominations to fulfil their callings.</p></div>
</div></section>
<section class="sec dark" id="mandate" style="padding-top:0"><div class="wrap"><div class="head"><div><span class="label rv">Sevenfold mandate</span><h2 class="rv" style="color:#fff">Seven <span class="serif" style="color:var(--rose)">assignments</span></h2></div></div><div class="stack">{stack_cards()}</div></div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="label rv">Prophetic pillars</span><h2 class="rv">Upheld by <span class="serif">seven pillars</span></h2></div><div class="rv panel" style="background:var(--ink);color:#fff;padding:24px 28px"><span class="label">Foundational conviction</span><div style="font-family:var(--display);font-weight:700;font-size:2rem;letter-spacing:-.03em;color:var(--gold-soft)">Everything by priesthood</div></div></div><div class="g4">{pillars}</div></div></section>
<section class="sec dark"><div class="wrap g2" style="align-items:start">
  <div class="rv"><span class="label">Our philosophy</span><p class="quote">“We are raising people who know the God to whom they pray, discern the purposes of His heart, carry the burdens of His kingdom and become <b>answers to the prayers</b> they offer.”</p><span class="mono" style="color:var(--gold-soft)">A people upon the watch · a people consecrated to the altar</span></div>
  <div class="panel rv" style="--d:.1s"><span class="label">Our anthem</span><p class="serif" style="font-size:1.6rem;line-height:1.45;margin-top:14px">We are prophetic intercessors<br>We walk in the supernatural<br>We are rising with power<br>We are rising with fire<br>We’ll cover all the earth<br><br>So we rise above every fear and limitations<br>We rise in battle · We rise in strength<br>We’ll take dominion<br><br>Like the waters we are unstoppable<br>To dispense the Lord’s glory</p></div>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="label rv">How we gather</span><h2 class="rv">One altar, <span class="serif">many nations</span></h2></div></div><div class="g3">
{feat("video", "Online prayer altar", "On Zoom, TikTok and YouTube — so intercessors join from Africa, North America and beyond.")}
{feat("flame", "Prayer stretches on Zoom", "Extended seasons of prayer like our 24 Hours Prayer Stretch, keeping the fire burning.")}
{feat("heart", "Outreach missions", "Prison outreach in Douala, rural missions and the orphanage we are building.")}
</div></div></section>''' + GIVE_CTA
page("about.html", "About — Prophetic Intercession", "Our vision, mission, sevenfold mandate, prophetic pillars, philosophy and anthem.", about)

# ============================== CONVENER ==============================
convener = f'''
<section class="phero"><div class="wrap convener" style="padding-bottom:60px">
  <div class="convener-photo rv"><img src="assets/img/gallery/g14.jpg" alt="Prophetic Intercessor ministering in prayer"><span class="tag">Prophetic Intercessor</span></div>
  <div>
    <span class="label rv">Our convener</span>
    <h1 class="split" style="font-size:clamp(3rem,7vw,6.4rem);line-height:.9;letter-spacing:-.05em;margin:.3em 0 .4em"><span class="split-line"><span>Prophetic</span></span><span class="split-line"><span class="serif" style="color:var(--rose-deep)">Intercessor</span></span></h1>
    <p class="rv">Our convener is a woman of prayer with a prophetic burden for revival. In the wake of 2020, God birthed in her the vision of Prophetic Intercession — and from 2023 she began gathering people on YouTube for extended hours of prayer, standing in the gap for individuals, families and nations.</p>
    <p class="muted rv">Under her leadership the ministry has reached into prison in Douala, supported rural missions and begun the work of building an orphanage.</p>
    <div class="rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:24px"><a class="btn btn-yt" data-link="youtube" href="media.html">{YT} Watch on YouTube</a><a class="btn btn-ghost" href="events.html">Pray with her</a></div>
  </div>
</div></section>
<section class="sec dark"><div class="wrap g2">
  <div class="rv"><span class="label">Her heart</span><p class="quote">“We are not raising people who merely know how to pray. We are raising people who <b>know the God</b> to whom they pray.”</p><p class="muted">Her foundational conviction is simple: everything by priesthood.</p></div>
  <div class="frame rv"><img src="assets/img/gallery/g06.jpg" alt="Praying over the open Scriptures"></div>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="label rv">The journey</span><h2 class="rv">So <span class="serif">far</span></h2></div></div>
<div class="g4">
{feat("spark", "2020", "The vision is birthed — a burden for prayer, revival and a generation of prophetic intercessors.")}
{feat("video", "2023", "Prayer on YouTube: people gather online for extended hours of intercession.")}
{feat("key", "2026", "Prison outreach in Douala, Cameroon, and the 24 Hours Prayer Stretch on Zoom.")}
{feat("heart", "Next", "The orphanage — and a vision for hospitals and schools.")}
</div></div></section>''' + GIVE_CTA
page("convener.html", "Our Convener — Prophetic Intercession", "Meet the convener and host of Prophetic Intercession.", convener)

# ============================== PRAYER ==============================
HOURS = "".join(f'<option>{h:02d}:00 – {(h + 1) % 24:02d}:00 WAT</option>' for h in range(24))
prayer = phero("Prayer", "Let us <span class='serif'>stand</span> with you", "Share your request, take a watch on the altar and pray with intercessors across the nations — day and night.", "gallery/g13.jpg") + f'''
<section class="sec"><div class="wrap g2" style="align-items:start">
  <div class="rv"><span class="label">Prayer request</span><h2 style="font-size:clamp(2.4rem,5vw,4rem);margin-top:.4em">Every request is <span class="serif">carried</span> to God.</h2><p class="muted">“The effectual fervent prayer of a righteous man availeth much.” — James 5:16. Your request is only shared with our prayer team.</p></div>
  <div class="panel rv" style="--d:.1s"><form class="form" data-mail-form data-subject="Prayer Request">
    <div class="row"><div><label for="n">Name</label><input id="n" name="name" required autocomplete="name"></div><div><label for="c">Email or WhatsApp</label><input id="c" name="contact" required></div></div>
    <div><label for="co">Country</label><input id="co" name="country"></div>
    <div><label for="r">Your prayer request</label><textarea id="r" name="request" required></textarea></div>
    <label class="check"><input type="checkbox" name="private" value="Only intercessors may see this"> Only intercessors can see this.</label>
    <button class="btn btn-rose" type="submit">Send request <span class="arr">{ARR}</span></button>
  </form></div>
</div></section>
<section class="sec dark"><div class="wrap">
  <div class="head"><div><span class="label rv">Prayer features</span><h2 class="rv" style="color:#fff">Keep the <span class="serif" style="color:var(--rose)">fire</span> burning</h2></div></div>
  <div class="g2" style="align-items:stretch">
    <div class="panel rv"><div class="focus-box" data-focus></div><p class="muted" style="margin-top:14px">Our current theme of prayer — pray into it daily with the family.</p></div>
    <div class="panel rv" id="watch" style="--d:.05s"><span class="label">24/7 watch sign-up</span><h3 style="font-size:2rem;margin:.4em 0">Take a watch on the altar</h3>
      <form class="form" data-mail-form data-subject="Watch Sign-up"><div class="row"><div><label for="wn">Name</label><input id="wn" name="name" required></div><div><label for="wc">Email or WhatsApp</label><input id="wc" name="contact" required></div></div><div><label for="wh">Preferred hour</label><select id="wh" name="hour">{HOURS}</select></div><button class="btn btn-gold" type="submit">Sign me up</button></form></div>
    <div class="panel rv" id="bible-tracker" style="background:var(--paper);color:var(--ink)"><span class="label">Bible reading tracker</span><h3 style="font-size:2rem;margin:.4em 0">Read through with us</h3><p class="muted">21 or 40 days — tap a day when you’ve read it. Saved on this device.</p>
      <div class="plan-toggle"><button type="button" class="filter" data-plan="21">21 days</button><button type="button" class="filter" data-plan="40">40 days</button></div>
      <div class="bar"><span></span></div><div class="pct"><span class="pct-text"></span><button type="button" class="link-btn" data-reset>Reset</button></div><div class="days"></div></div>
    <div class="panel rv" style="--d:.05s;background:#25d366;color:#052b14;border:0"><span class="label" style="color:#052b14">Join the intercessors</span><h3 style="font-size:2.4rem;margin:.4em 0">Pray with us on WhatsApp</h3><p>Fliers, prayer alerts, prophetic words and joining links — shared here first.</p><a class="btn btn-ink" data-link="whatsapp" href="channels.html">{WA} Join the group</a><p style="margin-top:24px;opacity:.8">Prayer wall <span class="soon-tag">Coming soon</span></p></div>
  </div>
</div></section>''' + GIVE_CTA
page("prayer.html", "Prayer — Prophetic Intercession", "Send a prayer request, sign up for a watch, track your Bible reading and join our WhatsApp prayer group.", prayer)

# ============================== PROPHETIC WATCH ==============================
prophetic = phero("Prophetic Watch", "Words &amp; warnings, <span class='serif'>watched over</span>", "Prophetic words and warnings — published, prayed over and watched until they come to pass.") + '''
<section class="sec-sm"><div class="wrap"><div class="g2 dark rv" style="border-radius:var(--r-xl);padding:clamp(26px,4vw,50px);align-items:center">
  <div><span class="label">The watchman’s charge</span><p class="quote">“Write the vision, and make it plain… though it <b>tarry</b>, wait for it.”</p><span class="mono" style="color:var(--gold-soft)">Habakkuk 2:2–3</span></div>
  <div class="status-legend"><div><span class="tag status st-watching">Watching</span><p>Released — we are praying over it and watching for it.</p></div><div><span class="tag status st-unfolding">Unfolding</span><p>We are seeing it begin to come to pass.</p></div><div><span class="tag status st-fulfilled">Fulfilled</span><p>It has come to pass — the testimony is in the watch log.</p></div></div>
</div></div></section>
<section class="sec" style="padding-top:20px"><div class="wrap"><div class="filters" id="watch-filters" role="group" aria-label="Filter words"></div><div class="watch-list" id="prophetic-words"></div></div></section>''' + GIVE_CTA
page("prophetic.html", "Prophetic Watch — Prophetic Intercession", "Prophetic words and warnings, published and watched over until they come to pass.", prophetic)

# ============================== BLOG ==============================
blog = phero("Blog", "Stories &amp; <span class='serif'>teachings</span>", "Outreach stories, event recaps, teachings and updates from the Prophetic Intercession family.") + '''
<section class="sec" style="padding-top:50px"><div class="wrap"><div class="blog-tools rv"><div class="filters" id="blog-filters" role="group" aria-label="Filter by category"></div><label class="blog-search"><span class="sr-only">Search articles</span><input id="blog-search" type="search" placeholder="Search articles…"></label></div><div class="post-grid" id="blog-list"></div></div></section>''' + GIVE_CTA
page("blog.html", "Blog — Prophetic Intercession", "Articles, teachings and stories from Prophetic Intercession.", blog, '<script src="assets/js/blog.js"></script>\n')
blog_post = '''<article id="post" class="post"></article>
<section class="sec-sm" style="background:var(--paper-2)"><div class="wrap"><div class="head"><div><span class="label">Keep reading</span><h2>More <span class="serif">stories</span></h2></div><a class="btn btn-ghost" href="blog.html">All articles</a></div><div class="post-grid" id="latest-posts"></div></div></section>''' + GIVE_CTA
page("blog-post.html", "Blog — Prophetic Intercession", "An article from the Prophetic Intercession blog.", blog_post, '<script src="assets/js/blog.js"></script>\n')

# ============================== MEDIA ==============================
media = phero("Media", "Watch, listen &amp; <span class='serif'>pray</span>", "Prayer sessions, prophetic words and teachings — new YouTube uploads appear here automatically.") + f'''
<section class="sec" style="padding-top:50px"><div class="wrap">
  <div class="panel rv" style="background:var(--ink);color:#fff;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-bottom:30px;padding:24px 28px"><div><strong style="font-family:var(--display);font-size:1.5rem;letter-spacing:-.02em">Prophetic Intercession on YouTube</strong><div class="mono" style="color:rgba(255,255,255,.6);margin-top:4px">@PropheticAndIntercession · 7K+ subscribers</div></div><a class="btn btn-yt" data-link="youtube" href="#">{YT} Subscribe</a></div>
  <div class="filters rv" role="group" aria-label="Filter media"><button class="filter active" data-filter="all" aria-pressed="true">All</button><button class="filter" data-filter="video" aria-pressed="false">Videos</button><button class="filter" data-filter="flyer" aria-pressed="false">Flyers</button><button class="filter" data-filter="message" aria-pressed="false">Messages</button></div>
  <div class="media-grid" id="media-grid"></div>
</div></section>''' + GIVE_CTA
page("media.html", "Media — Prophetic Intercession", "Videos, flyers and messages from Prophetic Intercession.", media)

# ============================== GALLERY ==============================
gallery = phero("Gallery", "Moments in <span class='serif'>ministry</span>", "Prayer, worship and the preaching of the Word.") + '''
<section class="sec" style="padding-top:50px"><div class="wrap"><div class="gallery-grid" id="gallery-grid"></div></div></section>''' + GIVE_CTA
page("gallery.html", "Gallery — Prophetic Intercession", "Photos from the ministry of Prophetic Intercession.", gallery)

# ============================== EVENTS ==============================
events = phero("Events", "Gather <span class='serif'>with us</span>", "Prayer stretches on Zoom and special gatherings. Announced in WAT — 6PM WAT is 11AM CST and 12 noon EST.") + '''
<section class="sec" style="padding-top:50px"><div class="wrap"><span class="label rv">Upcoming</span><div id="upcoming-events" style="margin-top:18px"></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="label rv">Recent gatherings</span><div id="past-events" style="margin-top:18px"></div></div></section>''' + GIVE_CTA
page("events.html", "Events — Prophetic Intercession", "Upcoming prayer gatherings and recent events.", events, '<script src="assets/js/events.js"></script>\n')

# ============================== OUTREACH ==============================
def orow(id_, img, label, title, text, items, rev=False, extra=""):
    lis = "".join(f"<li>{x}</li>" for x in items)
    media_ = img if img.startswith("<") else f'<div class="frame wide rv"><img src="assets/img/{img}" alt=""></div>'
    copy = f'<div class="rv" style="--d:.1s"><span class="label">{label}</span><h2 style="font-size:clamp(2.4rem,4.6vw,4rem);margin-top:.4em">{title}</h2><p>{text}</p><ul class="muted" style="padding-left:1.1em">{lis}</ul>{extra}</div>'
    return f'<div class="g2" id="{id_}" style="padding:50px 0">' + (copy + media_ if rev else media_ + copy) + '</div>'
outreach = phero("Outreach", "Prayer with <span class='serif'>hands &amp; feet</span>", "What we receive on our knees, we carry into the world — here is what God has allowed us to do so far.", "unity-hands.jpg") + f'''
<section class="sec"><div class="wrap">
{orow("prison", '<div class="frame wide rv" style="background:var(--ink)"><button class="media-thumb video" data-yt="W36f2nty25o" aria-label="Play Prison Outreach Douala-Cameroon video" style="height:100%"><img src="https://i.ytimg.com/vi/W36f2nty25o/hqdefault.jpg" alt=""><span class="play"></span></button></div>', "Completed · Douala, Cameroon", "Prison <span class='serif'>outreach</span>", "“I was in prison, and ye came unto me” (Matthew 25:36). In Douala we took the love of Christ behind prison walls.", ["Prayer and ministry of the Word with inmates", "Hope for those who feel forgotten", "Practical care for everyday needs"])}
{orow("rural", "rural-missions.jpg", "Supported", "Rural <span class='serif'>missions</span>", "Standing with missionaries who carry the Gospel to remote, overlooked communities.", ["Support for missionaries", "Prayer covering for the mission field", "The Gospel where it’s rarely heard"], True)}
{orow("orphanage", "orphanage.jpg", "In progress", "The <span class='serif'>orphanage</span>", "“A father of the fatherless… God setteth the solitary in families” (Psalm 68:5–6).", ["A safe home and daily care", "Education, mentoring and discipleship", "A family built on Christ’s love"], False, f'<a class="btn btn-rose" href="give.html">Help build it <span class="arr">{ARR}</span></a>')}
</div></section>
<section class="sec dark" id="future"><div class="wrap"><div class="head"><div><span class="label rv">Future vision</span><h2 class="rv" style="color:#fff">The road <span class="serif" style="color:var(--rose)">ahead</span></h2></div><p class="rv">As God provides, we will bring healing and education to the communities we serve.</p></div>
<div class="g2" style="align-items:stretch"><div class="h-card rv" style="width:auto"><img src="assets/img/hospitals.jpg" alt=""><span class="status">Future</span><h3>Hospitals</h3><p>Care and healing for body and soul.</p></div><div class="h-card rv" style="width:auto;--d:.1s"><img src="assets/img/schools.jpg" alt=""><span class="status">Future</span><h3>Schools</h3><p>Doors of learning for children to grow in knowledge and faith.</p></div></div></div></section>''' + GIVE_CTA
page("outreach.html", "Outreach — Prophetic Intercession", "Prison outreach in Douala, rural missions, the orphanage and the vision for hospitals and schools.", outreach)

# ============================== CHANNELS ==============================
def chan(bg, icon, title, text, btn):
    return f'<div class="panel rv" style="display:flex;flex-direction:column;gap:14px"><span style="width:64px;height:64px;border-radius:18px;display:grid;place-items:center;background:{bg};color:#fff">{icon}</span><h3 style="font-size:2rem;margin:0">{title}</h3><p class="muted" style="margin:0">{text}</p><div style="margin-top:auto">{btn}</div></div>'
channels = phero("Channels", "One altar, <span class='serif'>every screen</span>", "Our prayers are online — on Zoom, TikTok and YouTube. Our prayer stretches happen on Zoom.") + f'''
<section class="sec" style="padding-top:50px"><div class="wrap g2" style="align-items:stretch">
{chan("#25d366", WA, "WhatsApp", "Prayer alerts, fliers, prophetic words and joining links — shared here first.", f'<a class="btn btn-whatsapp" data-link="whatsapp" href="#">{WA} Join the group</a>')}
{chan("#2d8cff", ZOOM, "Zoom", "Our prayer stretches — like the 24 Hours Prayer Stretch — happen on Zoom.", '<a class="btn btn-ghost" href="events.html">See events</a>')}
{chan("#111", TT, "TikTok", "Live prayer and short prophetic words · @propheticandintercession", f'<a class="btn btn-ink" data-link="tiktok" href="#">{TT} Follow</a>')}
{chan("#ff0033", YT, "YouTube", "Prayer sessions, prophetic words and teachings · @PropheticAndIntercession", f'<a class="btn btn-yt" data-link="youtube" href="#">{YT} Subscribe</a>')}
</div></section>''' + GIVE_CTA
page("channels.html", "Channels — Prophetic Intercession", "Join Prophetic Intercession on WhatsApp, Zoom, TikTok and YouTube.", channels)

# ============================== TESTIMONIES ==============================
testimonies = phero("Testimonies", "Answered <span class='serif'>prayers</span>", "“They overcame him by the blood of the Lamb, and by the word of their testimony.” — Revelation 12:11") + f'''
<section class="sec" style="padding-top:50px"><div class="wrap"><div class="testimony-grid" id="testimonies"></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap g2" style="align-items:start">
  <div class="rv"><span class="label">Share yours</span><h2 style="font-size:clamp(2.4rem,5vw,4rem);margin-top:.4em">What has God <span class="serif">done</span> for you?</h2><p class="muted">Published only with your permission — anonymously if you prefer.</p></div>
  <div class="panel rv"><form class="form" data-mail-form data-subject="Testimony"><div class="row"><div><label for="tn">Name</label><input id="tn" name="name" required></div><div><label for="tp">City / Country</label><input id="tp" name="place"></div></div><div><label for="tc">Email or WhatsApp</label><input id="tc" name="contact" required></div><div><label for="tt">Your testimony</label><textarea id="tt" name="testimony" required></textarea></div><label class="check"><input type="checkbox" name="permission" value="Yes"> You may publish this on the website.</label><label class="check"><input type="checkbox" name="anonymous" value="Yes"> Please publish it anonymously.</label><button class="btn btn-rose" type="submit">Share testimony <span class="arr">{ARR}</span></button></form></div>
</div></section>''' + GIVE_CTA
page("testimonies.html", "Testimonies — Prophetic Intercession", "Answered prayers from the Prophetic Intercession family.", testimonies)

# ============================== GIVE ==============================
give = phero("Give", "Sow a <span class='serif'>seed</span>", "Choose how you’d like to give — your details appear instantly with step-by-step guidance.") + f'''
<section class="sec dark" style="margin-top:60px;border-radius:var(--r-xl) var(--r-xl) 0 0"><div class="wrap">
  <div class="give-engine" id="give-engine" data-theme="momo">
    <div><p class="ge-step"><b>1</b> Choose a method</p><div class="ge-methods" role="tablist" aria-label="Giving methods"></div><p class="ge-trust">{I["shield"]}<span>Always confirm the account name before sending. We will never ask for your PIN or password.</span></p></div>
    <div><p class="ge-step"><b>2</b> Send your seed</p><div class="ge-panel" aria-live="polite"></div></div>
  </div>
</div></section>
<section class="sec"><div class="wrap"><div class="head"><div><span class="label rv">Where your seed goes</span><h2 class="rv">Fuel for the <span class="serif">mission</span></h2></div></div><div class="g4">
{feat("flame", "Prayer gatherings", "Prayer stretches on Zoom and live prayer online.")}
{feat("key", "Prison outreach", "Hope and practical care behind prison walls in Douala.")}
{feat("globe", "Rural missions", "The Gospel in remote communities.")}
{feat("heart", "The orphanage", "A home for children who need a family.")}
</div></div></section>
<section class="sec-sm dark"><div class="wrap cta-big rv"><span class="label">Thank you for partnering with us</span><p class="quote" style="margin:.5em auto 0;max-width:22ch">May God richly reward you and <b>enlarge your territory!</b></p></div></section>'''
page("give.html", "Give — Prophetic Intercession", "Partner with Prophetic Intercession through MTN MoMo, Zelle or BNB / USDT (BEP-20).", give,
     '<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js" defer></script>\n')

(ROOT / "vercel.json").write_text('{\n  "cleanUrls": false\n}\n')
print("built v2:", sorted(p.name for p in ROOT.glob("*.html")))
