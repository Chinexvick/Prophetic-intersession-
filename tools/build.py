import os
import pathlib
R = str(pathlib.Path(__file__).resolve().parent.parent)

NAV = [("index.html", "Home"), ("about.html", "About"), ("prayer.html", "Prayer"),
       ("prophetic.html", "Prophetic"), ("channels.html", "Channels"), ("events.html", "Events"),
       ("media.html", "Media"), ("testimonies.html", "Testimonies")]

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.05 21.5h-.01a9.43 9.43 0 0 1-4.8-1.32l-.35-.2-3.57.93.96-3.48-.23-.36a9.4 9.4 0 0 1-1.44-5.02c0-5.2 4.24-9.44 9.45-9.44 2.52 0 4.89.99 6.67 2.77a9.37 9.37 0 0 1 2.76 6.68c0 5.21-4.24 9.44-9.44 9.44m8.04-17.48A11.3 11.3 0 0 0 12.05.7C5.78.7.68 5.8.68 12.06c0 2 .52 3.96 1.52 5.68L.58 23.7l6.1-1.6a11.36 11.36 0 0 0 5.37 1.37h.01c6.26 0 11.36-5.1 11.36-11.37 0-3.03-1.18-5.89-3.33-8.03"/></svg>'
YT_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6z"/></svg>'
TT_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M19.6 6.7a4.8 4.8 0 0 1-3.8-4.2V2h-3.4v13.7a2.9 2.9 0 1 1-2-2.7V9.5a6.3 6.3 0 1 0 5.4 6.2V8.8a8.2 8.2 0 0 0 4.8 1.5V6.9a4.8 4.8 0 0 1-1-.2z"/></svg>'
ZOOM_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M2 7.5A2.5 2.5 0 0 1 4.5 5h9A2.5 2.5 0 0 1 16 7.5v9a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 2 16.5zm15 2.3 4.2-2.9c.36-.25.8 0 .8.43v9.34c0 .43-.44.68-.8.43L17 14.2z"/></svg>'


ARROW_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>'
ARROW_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>'

ICON = {
 "flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
 "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
 "ear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06z"/><path d="M10 2c1 .5 2 2 2 5"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>',
 "key": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="5.5"/><path d="M21 2l-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
}


def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0b0c">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/hero-worship.jpg">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500;1,600;1,700&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>'''


CUR = ' aria-current="page"'

def header(active):
    links = "\n".join(
        f'        <li><a href="{h}"{CUR if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Prophetic Intercession home">
      <img src="assets/img/logo.png" alt="Prophetic Intercession logo" width="46" height="46">
      <span class="brand-text"><strong>Prophetic Intercession</strong><span>Praying · Reaching · Transforming</span></span>
    </a>
    <nav aria-label="Main">
      <ul class="nav-links">
{links}
        <li><a class="btn btn-gold" href="give.html">Give</a></li>
      </ul>
    </nav>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>'''


FOOTER = '''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo.png" alt="Prophetic Intercession logo" width="72" height="72">
        <p class="tag">Raising a Tribe. Birthing Revival. Transforming Nations.</p>
        <p>A global interdenominational ministry — a people upon the watch, a people consecrated to the altar.</p>
      </div>
      <div>
        <h4>Ministry</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="founder.html">Our Founder</a></li>
          <li><a href="about.html#beliefs">What We Believe</a></li>
          <li><a href="outreach.html">Our Outreach</a></li>
          <li><a href="testimonies.html">Testimonies</a></li>
        </ul>
      </div>
      <div>
        <h4>Get Involved</h4>
        <ul>
          <li><a href="events.html">Upcoming Events</a></li>
          <li><a href="prayer.html">Prayer Requests</a></li>
          <li><a href="channels.html">Our Channels</a></li>
          <li><a href="media.html">Media &amp; Flyers</a></li>
          <li><a href="give.html">Partner &amp; Give</a></li>
        </ul>
      </div>
      <div>
        <h4>Outreach</h4>
        <ul>
          <li><a href="outreach.html#prison">Prison Outreach</a></li>
          <li><a href="outreach.html#rural">Rural Missions</a></li>
          <li><a href="outreach.html#orphanage">Orphanage</a></li>
          <li><a href="outreach.html#future">Hospitals &amp; Schools</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Prophetic Intercession. All rights reserved.</span>
      <span>“I will stand upon my watch…” — Habakkuk 2:1</span>
    </div>
  </div>
</footer>'''


def page(fname, title, desc, body, extra_js=""):
    html = (head(title, desc) + "\n<body>\n" + header(fname) + "\n<main>\n" + body.strip() + "\n</main>\n" + FOOTER +
            "\n" + extra_js + '<script src="assets/js/content.js"></script>\n<script src="assets/js/main.js"></script>\n</body>\n</html>\n')
    with open(os.path.join(R, fname), "w") as f:
        f.write(html)


def page_hero(img, eyebrow, title, text, pos="center"):
    return f'''<section class="page-hero">
  <img src="assets/img/{img}" alt="" style="object-position:{pos}">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>'''


CTA = '''<section class="cta-band">
  <div class="container">
    <div>
      <span class="eyebrow pink">Partner with us</span>
      <h2>Your seed keeps the altar burning.</h2>
    </div>
    <div class="hero-row">
      <a class="btn btn-gold" href="give.html">Give Now</a>
      <a class="btn btn-outline-dark" href="prayer.html">Send a Prayer Request</a>
    </div>
  </div>
</section>'''

# ======================= HOME =======================
home = f'''
<section class="hero">
  <div class="hero-media"><img src="assets/img/hero-worship.jpg" alt="Worshippers lifting their hands in prayer" fetchpriority="high"></div>
  <div class="container hero-content">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">A global interdenominational ministry</span>
        <h1>Prophetic Intercession</h1>
        <p class="tagline">Raising a Tribe. Birthing Revival. Transforming Nations.</p>
        <div class="hero-actions">
          <a class="btn btn-whatsapp" data-link="whatsapp" href="channels.html">{WA_ICON} Join the Prayer Group</a>
          <a class="btn btn-gold" href="prayer.html">Send a Prayer Request</a>
        </div>
        <div class="hero-meta"><strong>We gather online</strong>A global prayer community connecting people through powerful online prayer gatherings on Zoom, TikTok &amp; YouTube.</div>
      </div>
      <div class="session-card reveal" data-next-session></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <h2>Around Prophetic Intercession</h2>
      <a class="btn btn-outline-dark" href="events.html">All events</a>
    </div>
    <div class="carousel reveal">
      <div class="track">
        <a class="feature-card" href="events.html">
          <img src="assets/img/prayer-hands.jpg" alt="" loading="lazy">
          <div><span class="label">Nov 13 – 14 · Recent</span><h3>24 Hours Prayer Stretch</h3></div>
          <span class="more">Learn more</span>
        </a>
        <a class="feature-card" href="events.html">
          <img src="assets/img/worship-night.jpg" alt="" loading="lazy">
          <div><span class="label">Coming soon</span><h3>Next Prayer Gathering</h3></div>
          <span class="more">See upcoming</span>
        </a>
        <a class="feature-card" href="outreach.html#prison">
          <img src="assets/img/prison-outreach.jpg" alt="" loading="lazy">
          <div><span class="label">Outreach</span><h3>Prison Outreach</h3></div>
          <span class="more">Learn more</span>
        </a>
        <a class="feature-card" href="outreach.html#rural">
          <img src="assets/img/rural-missions.jpg" alt="" loading="lazy">
          <div><span class="label">Missions</span><h3>Rural Missions</h3></div>
          <span class="more">Learn more</span>
        </a>
        <a class="feature-card" href="prophetic.html">
          <img src="assets/img/bible.jpg" alt="" loading="lazy">
          <div><span class="label">Prophetic</span><h3>Word for the Week</h3></div>
          <span class="more">Read the word</span>
        </a>
        <a class="feature-card" href="media.html">
          <img src="assets/img/flyer-24hr-prayer-stretch.jpg" alt="" loading="lazy" style="object-position:center 85%">
          <div><span class="label">Media</span><h3>Flyers &amp; Videos</h3></div>
          <span class="more">Browse media</span>
        </a>
        <a class="feature-card" href="give.html">
          <img src="assets/img/giving.jpg" alt="" loading="lazy">
          <div><span class="label">Partner</span><h3>Sow Into the Ministry</h3></div>
          <span class="more">Give now</span>
        </a>
      </div>
      <div class="carousel-controls">
        <button class="carousel-btn" data-prev aria-label="Previous">{ARROW_L}</button>
        <button class="carousel-btn" data-next aria-label="Next">{ARROW_R}</button>
      </div>
    </div>
  </div>
</section>

<section class="about-band">
  <img src="assets/img/vision-sunrise.jpg" alt="" loading="lazy" style="object-position:70% center">
  <div class="container">
    <div class="about-box reveal">
      <span class="eyebrow">Who we are</span>
      <h2>About Us</h2>
      <p>Welcome to Prophetic Intercession — a house of prayer without walls. We are a community of intercessors who believe that prayer moves heaven and changes earth. Online — on Zoom, TikTok and YouTube — believers from Africa, North America and around the world gather to seek the face of God, hear His voice and stand in the gap for families, cities and nations.</p>
      <p>But we don’t stop at prayer. What we receive on our knees, we carry out with our hands — into prisons, rural villages and the lives of children who need a family.</p>
      <a class="btn btn-outline" href="about.html">Learn more</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container focus-strip">
    <div class="reveal">
      <span class="eyebrow">Our vision</span>
      <h2>Raising a prophetic and intercessory tribe</h2>
      <p class="muted">To raise a generation of prophetic intercessors who will discern the heart of God, birth His purposes and manifest His glory across the nations.</p>
      <p class="muted"><strong style="color:var(--ink)">Foundational conviction:</strong> Everything by priesthood.</p>
      <div class="focus-box mt-2" data-focus></div>
    </div>
    <div class="pillars">
      <div class="pillar reveal"><span class="num">1</span><div><h3>Raising a Prophetic &amp; Intercessory Generation</h3><p>A consecrated people who discern His voice and stand in the gap.</p></div></div>
      <div class="pillar reveal"><span class="num">2</span><div><h3>Birthing &amp; Sustaining Genuine Revival</h3><p>Contending for a fresh move of God in the Church and the nations.</p></div></div>
      <div class="pillar reveal"><span class="num">3</span><div><h3>Awakening Gifts, Callings &amp; Destinies</h3><p>Discovering, developing and deploying God-given gifts.</p></div></div>
      <div class="pillar reveal"><span class="num">4</span><div><h3>Demonstrating the Risen Christ</h3><p>Healing, miracles, signs and wonders that glorify Jesus.</p></div></div>
      <div class="pillar reveal"><span class="num">5</span><div><h3>Evangelism</h3><p>Interceding for the lost and bringing them to Jesus Christ.</p></div></div>
      <div class="pillar reveal"><span class="num">6</span><div><h3>A Global Network of Prayer</h3><p>Uniting believers across denominations, cultures and nations.</p></div></div>
      <div class="pillar reveal"><span class="num">7</span><div><h3>Compassion Through Social Impact</h3><p>Reaching the vulnerable and restoring dignity.</p></div></div>
      <a class="btn btn-outline-dark reveal" href="about.html#mandate" style="justify-self:start">Our sevenfold mandate</a>
    </div>
  </div>
</section>

<section class="section-sm bg-dark">
  <div class="container">
    <div class="section-head reveal"><h2>Pray with us online</h2><a class="btn btn-outline" href="channels.html">All channels</a></div>
    <div class="grid-4">
      <a class="tile reveal" data-link="whatsapp" href="channels.html"><div class="icon" style="color:#25d366">{WA_ICON}</div><h3>WhatsApp</h3><p>Our prayer group — fliers, alerts and joining links.</p></a>
      <a class="tile reveal" href="channels.html#zoom"><div class="icon" style="color:#2d8cff">{ZOOM_ICON}</div><h3>Zoom</h3><p>Where our prayer stretches happen.</p></a>
      <a class="tile reveal" data-link="tiktok" href="channels.html"><div class="icon">{TT_ICON}</div><h3>TikTok</h3><p>Live prayer and short prophetic words.</p></a>
      <a class="tile reveal" data-link="youtube" href="channels.html"><div class="icon" style="color:#ff0033">{YT_ICON}</div><h3>YouTube</h3><p>Prayer sessions and messages to watch again.</p></a>
    </div>
  </div>
</section>

<section class="section bg-blush">
  <div class="container">
    <div class="section-head reveal">
      <h2>Our Outreach</h2>
      <a class="btn btn-outline-dark" href="outreach.html">See all</a>
    </div>
    <div class="carousel reveal">
      <div class="track">
        <article class="ministry-card">
          <div class="media"><img src="assets/img/prison-outreach.jpg" alt="Hands reaching out to one another" loading="lazy"><span class="status done">Completed</span></div>
          <div class="body">
            <h3>Prison Outreach</h3>
            <p class="sub">Bringing hope, the Word and practical care to men and women behind bars.</p>
            <div class="meta-title">Focus</div>
            <div class="meta">Prayer · The Gospel · Care packs</div>
            <a class="btn btn-outline-dark" href="outreach.html#prison">Learn more</a>
          </div>
        </article>
        <article class="ministry-card">
          <div class="media"><img src="assets/img/rural-missions.jpg" alt="Wide rural landscape" loading="lazy"><span class="status done">Supported</span></div>
          <div class="body">
            <h3>Rural Missions</h3>
            <p class="sub">Standing with missionaries who carry the Gospel to remote, overlooked communities.</p>
            <div class="meta-title">Focus</div>
            <div class="meta">Evangelism · Mission support</div>
            <a class="btn btn-outline-dark" href="outreach.html#rural">Learn more</a>
          </div>
        </article>
        <article class="ministry-card">
          <div class="media"><img src="assets/img/orphanage.jpg" alt="Smiling children" loading="lazy"><span class="status progress">In progress</span></div>
          <div class="body">
            <h3>Orphanage</h3>
            <p class="sub">Building a loving, Christ-centred home where orphaned children can grow and thrive.</p>
            <div class="meta-title">Focus</div>
            <div class="meta">Shelter · Education · Family</div>
            <a class="btn btn-outline-dark" href="outreach.html#orphanage">Learn more</a>
          </div>
        </article>
        <article class="ministry-card">
          <div class="media"><img src="assets/img/schools.jpg" alt="Children in a classroom" loading="lazy"><span class="status future">Future vision</span></div>
          <div class="body">
            <h3>Hospitals &amp; Schools</h3>
            <p class="sub">Our next horizon: bringing healing and education to communities that need it most.</p>
            <div class="meta-title">Focus</div>
            <div class="meta">Health · Learning · Dignity</div>
            <a class="btn btn-outline-dark" href="outreach.html#future">Learn more</a>
          </div>
        </article>
      </div>
      <div class="carousel-controls">
        <button class="carousel-btn" data-prev aria-label="Previous">{ARROW_L}</button>
        <button class="carousel-btn" data-next aria-label="Next">{ARROW_R}</button>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2>Latest on YouTube</h2><a class="btn btn-outline-dark" data-link="youtube" href="media.html">Visit channel</a></div>
    <div class="media-grid" id="latest-videos"></div>
    <div class="center mt-2 reveal"><a class="btn btn-gold" href="media.html">More videos &amp; flyers</a></div>
  </div>
</section>

<section class="founder-band">
  <div class="container grid">
    <div class="founder-photo reveal"><img src="assets/img/founder.jpg" alt="The founder of Prophetic Intercession" loading="lazy"><span class="pin">Host · Prophetic Intercessor</span></div>
    <div class="founder-copy">
      <div class="founder-card reveal">
        <span class="eyebrow">Ministry leadership</span>
        <h2><span class="serif">Founder &amp; Host</span>Prophetic Intercessor</h2>
        <p>Called to the place of prayer, our founder carries a burden for revival and for raising a generation of prophetic intercessors. Through Prophetic Intercession she gathers believers across nations to pray, then leads them out to reach prisoners, rural communities and orphaned children with the love of Christ.</p>
        <a class="btn btn-gold" href="founder.html">Learn more</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="scripture reveal">
      <span class="eyebrow pink">Upon the watch</span>
      <blockquote>“I will stand upon my watch, and set me upon the tower, and will watch to see what he will say unto me…”</blockquote>
      <cite>Habakkuk 2:1</cite>
    </div>
  </div>
</section>

<section class="section-sm" style="padding-top:0">
  <div class="container">
    <div class="promo reveal">
      <div class="copy">
        <span class="eyebrow">Support the ministry</span>
        <h2>Partner with Prophetic Intercession</h2>
        <p>Every seed you sow fuels prayer, outreach to prisons and rural communities, and the orphanage we are building. Give from anywhere in the world.</p>
        <div class="chips"><span class="chip">MTN MoMo</span><span class="chip">Zelle</span><span class="chip">BNB / USDT (BEP-20)</span></div>
        <a class="btn btn-gold" href="give.html">Give now</a>
      </div>
      <div class="visual"><img src="assets/img/flyer-partner.jpg" alt="Partner with Prophetic Intercession flier"></div>
    </div>
  </div>
</section>
'''
page("index.html", "Prophetic Intercession — Praying, Reaching, Transforming Lives",
     "Prophetic Intercession is a global prayer community gathering online on Zoom, TikTok and YouTube, and reaching prisons, rural communities and orphans with the love of Jesus.",
     home, '<script src="assets/js/events.js"></script>\n')

# ======================= ABOUT =======================
def tile(icon, h, p):
    return f'<div class="tile reveal"><div class="icon">{ICON[icon]}</div><h3>{h}</h3><p>{p}</p></div>'

about = page_hero("vision-sunrise.jpg", "A global interdenominational ministry", "Raising a prophetic and intercessory tribe",
                  "Prophetic Intercession is a global prophetic and intercessory movement — interdenominational, Christ-centred and led by the Spirit of God.", "70% center") + f'''
<section class="section">
  <div class="container grid-2">
    <div class="reveal">
      <span class="eyebrow">The birth of the vision</span>
      <h2>From a burden to a global mandate</h2>
      <p>The vision of Prophetic Intercession was birthed in the wake of 2020, out of a deep spiritual burden for prayer, revival and the emergence of a generation of prophetic intercessors.</p>
      <p>The vision began to find full expression in 2023 through YouTube, where people gathered for extended hours of prayer and intercession, standing in the gap for individuals, families and nations.</p>
      <p>What began as a burden to pray for people has grown into a greater mandate: raising a global prophetic and intercessory tribe equipped to discern the heart of God, birth His purposes through prayer and become instruments of divine intervention in their generation.</p>
      <div class="hero-row mt-2"><a class="btn btn-gold" href="founder.html">Meet our founder</a><a class="btn btn-outline-dark" href="outreach.html">Our outreach</a></div>
    </div>
    <div class="img-accent reveal"><div class="img-frame tall"><img src="assets/img/prayer-hands.jpg" alt="Hands raised in worship" loading="lazy"></div></div>
  </div>
</section>

<section class="section bg-dark" id="vision">
  <div class="container">
    <div class="grid-2" style="align-items:stretch">
      <div class="vm-card reveal">
        <span class="eyebrow">Our vision</span>
        <p class="vm-text">To raise a generation of prophetic intercessors who will discern the heart of God, birth His purposes and manifest His glory across the nations.</p>
        <small>Habakkuk 2:1 · Isaiah 62:6–7 · Ezekiel 22:30 · Acts 2:17–18</small>
      </div>
      <div class="vm-card reveal">
        <span class="eyebrow">Our mission</span>
        <p class="vm-text">To cultivate a global community of prayer, prophetic expression, spiritual awakening and kingdom intervention, equipping believers across denominational boundaries to fulfil their spiritual callings, advance the purposes of God and demonstrate the love and power of Christ to humanity.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-blush" id="mandate">
  <div class="container">
    <div class="section-head reveal"><h2>Our sevenfold mandate</h2></div>
    <div class="mandates">
      <div class="mandate reveal"><span class="num">1</span><div><h3>Raising a Prophetic and Intercessory Generation</h3><p>To raise, disciple and equip a consecrated people who understand the ministry of prayer, develop intimacy with God, discern His voice and faithfully stand in the gap for individuals, families, communities and nations.</p><small>Ezekiel 22:30 · 1 Timothy 2:1–4 · Isaiah 62:6–7</small></div></div>
      <div class="mandate reveal"><span class="num">2</span><div><h3>Birthing and Sustaining Genuine Revival</h3><p>To become a spiritual catalyst for revival through persistent intercession, consecration, repentance and the stirring of spiritual hunger, raising people who will contend for a fresh move of God in the Church and across the nations.</p><small>Habakkuk 3:2 · Acts 2:1–4 · Joel 2:28–29 · 2 Chronicles 7:14</small></div></div>
      <div class="mandate reveal"><span class="num">3</span><div><h3>Awakening Gifts, Callings and Spiritual Destinies</h3><p>To create an atmosphere of spiritual growth, impartation, discipleship and prophetic activation where believers discover, develop and deploy their God-given gifts, callings and assignments for kingdom advancement.</p><small>2 Timothy 1:6 · 1 Timothy 4:14 · Ephesians 4:11–13 · Romans 12:6–8</small></div></div>
      <div class="mandate reveal"><span class="num">4</span><div><h3>Demonstrating the Supernatural Reality of the Risen Christ</h3><p>To cultivate a community that believes, pursues and demonstrates the supernatural ministry of the Holy Spirit through the gifts of the Spirit, divine healing, miracles, signs and wonders, bringing glory to Jesus Christ and bearing witness to His resurrection.</p><small>Mark 16:17–20 · Acts 4:29–33 · Hebrews 2:3–4 · 1 Corinthians 2:4–5</small></div></div>
      <div class="mandate reveal"><span class="num">5</span><div><h3>Evangelism</h3><p>To labour in intercession for the salvation of the lost and translate this burden into intentional evangelism that brings people into the knowledge of Jesus Christ.</p><small>Romans 10:1 · 2 Corinthians 5:18–20 · 2 Corinthians 4:3 · Matthew 28:19–20</small></div></div>
      <div class="mandate reveal"><span class="num">6</span><div><h3>Establishing a Global Network of Prayer and Spiritual Collaboration</h3><p>To unite believers, prayer movements, churches and ministries across denominations, cultures and nations into a global fellowship of intercessors, fostering spiritual collaboration, corporate prayer, prophetic accountability and kingdom partnerships.</p><small>John 17:20–23 · Acts 1:14 · Matthew 18:19–20 · Ephesians 4:3–6</small></div></div>
      <div class="mandate reveal"><span class="num">7</span><div><h3>Manifesting the Compassion of Christ Through Social Impact</h3><p>To translate spiritual convictions into tangible expressions of Christ’s love by reaching the vulnerable, helping the helpless, supporting disadvantaged communities and initiating humanitarian and social transformation projects that restore dignity and demonstrate the compassion of the Gospel.</p><small>Isaiah 58:6–12 · James 1:27 · Matthew 25:35–40 · Acts 10:38</small></div></div>
    </div>
  </div>
</section>

<section class="section" id="beliefs">
  <div class="container">
    <div class="section-head reveal"><h2>Our prophetic pillars</h2></div>
    <p class="lead reveal">Prophetic Intercession is upheld and driven by seven pillars.</p>
    <div class="grid-4 mt-2">
      <div class="tile reveal"><div class="icon">{ICON["flame"]}</div><h3>Prayer and Intercession</h3><p>“But we will give ourselves continually to prayer, and to the ministry of the word.”</p><small class="ref">Acts 6:4 · Isaiah 62:6–7</small></div>
      <div class="tile reveal"><div class="icon">{ICON["shield"]}</div><h3>Consecration</h3><p>Living a life worthy and pleasing unto God.</p><small class="ref">John 17:19 · Romans 12:1 · Galatians 2:20</small></div>
      <div class="tile reveal"><div class="icon">{ICON["book"]}</div><h3>The Word of God</h3><p>We labour in the word of God and doctrine.</p><small class="ref">John 8:32 · Psalm 107:20</small></div>
      <div class="tile reveal"><div class="icon">{ICON["ear"]}</div><h3>Prophetic Awakening</h3><p>Fulfilling God’s mandate on our prophetic destinies.</p><small class="ref">1 Samuel 3:8–11 · Joel 2:28–29</small></div>
      <div class="tile reveal"><div class="icon">{ICON["key"]}</div><h3>Warfare</h3><p>Advancing the kingdom of God across lives and territories through warfare.</p><small class="ref">Ephesians 6:12 · 2 Corinthians 10:3–5</small></div>
      <div class="tile reveal"><div class="icon">{ICON["globe"]}</div><h3>Evangelism and Kingdom Service</h3><p>Taking the gospel to the ends of the earth.</p><small class="ref">Romans 10:14 · 2 Timothy 4:5</small></div>
      <div class="tile reveal"><div class="icon">{ICON["heart"]}</div><h3>Miracles and the Supernatural</h3><p>He confirmed His word with signs following.</p><small class="ref">Mark 16:20 · 1 Corinthians 12:10 · Acts 19:11</small></div>
      <div class="tile reveal" style="background:var(--black);color:#fff;border-color:var(--black)"><span class="eyebrow">Foundational conviction</span><h3 style="font-size:1.6rem;color:var(--gold-soft)">Everything by priesthood</h3><p style="color:rgba(255,255,255,.75)">Interdenominational, Christ-centred and led by the Spirit of God.</p></div>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container grid-2" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Our philosophy</span>
      <blockquote class="big-quote">“We are not raising people who merely know how to pray. We are raising people who know the God to whom they pray, discern the purposes of His heart, carry the burdens of His kingdom and become answers to the prayers they offer.”</blockquote>
      <p class="gold" style="font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:.8rem">A people upon the watch, a people consecrated to the altar.</p>
      <div class="slogan mt-2"><span>Raising a Tribe.</span><span>Birthing Revival.</span><span>Transforming Nations.</span></div>
    </div>
    <div class="anthem reveal">
      <span class="eyebrow">Our anthem</span>
      <p>We are prophetic intercessors<br>We walk in the supernatural<br>We are rising with power<br>We are rising with fire<br>We’ll cover all the earth</p>
      <p>So we rise above every fear and limitations<br>We rise in battle<br>We rise in strength<br>We’ll take dominion</p>
      <p>We are prophetic intercessors<br>We walk in the supernatural<br>Like the waters we are unstoppable<br>To dispense the Lord’s glory</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2>How we gather</h2></div>
    <div class="grid-3">
      {tile("video", "Online prayer altar", "Our prayers are online — on Zoom, TikTok and YouTube — so intercessors anywhere in the world can join, from Africa to North America and beyond.")}
      {tile("flame", "Prayer stretches on Zoom", "Extended seasons of prayer like our 24 Hours Prayer Stretch, held on Zoom, where intercessors take turns keeping the fire burning.")}
      {tile("key", "Outreach missions", "Prayer-led outreaches into prisons and rural communities, and the ongoing work of building an orphanage.")}
    </div>
  </div>
</section>
''' + CTA
page("about.html", "About Us — Prophetic Intercession",
     "Prophetic Intercession is a global interdenominational ministry raising a prophetic and intercessory tribe: our vision, mission, sevenfold mandate, pillars and anthem.", about)

# ======================= FOUNDER =======================
founder = '''
<section class="founder-band" style="padding-top:76px">
  <div class="container grid">
    <div class="founder-photo reveal"><img src="assets/img/founder.jpg" alt="The founder of Prophetic Intercession"><span class="pin">Host · Prophetic Intercessor</span></div>
    <div class="founder-copy">
      <div class="founder-card reveal">
        <span class="eyebrow">Our founder</span>
        <h2><span class="serif">Founder &amp; Host</span>Prophetic Intercessor</h2>
        <p>Our founder is a woman of prayer with a prophetic burden for revival. In the wake of 2020, God birthed in her the vision of Prophetic Intercession — and from 2023 she began gathering people on YouTube for extended hours of prayer, standing in the gap for individuals, families and nations.</p>
        <p>Her heart beats for people the world often overlooks. Under her leadership the ministry has reached into prisons, supported rural missions, and begun the work of building an orphanage.</p>
        <div class="hero-row" style="margin-top:1.2rem">
          <a class="btn btn-gold" href="events.html">Pray with her</a>
          <a class="btn btn-outline" href="prayer.html">Send a message</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2">
    <div class="reveal">
      <span class="eyebrow">Her heart</span>
      <h2>“We are raising people who know the God to whom they pray.”</h2>
      <p>“We are not raising people who merely know how to pray. We are raising people who know the God to whom they pray, discern the purposes of His heart, carry the burdens of His kingdom and become answers to the prayers they offer.”</p>
      <p>Her foundational conviction is simple: <strong>everything by priesthood</strong>. The ministry seeks God first, listens for His voice, and then goes — carrying hope to prisoners, rural communities and children in need of a home.</p>
      <a class="btn btn-yt" data-link="youtube" href="media.html">Watch on YouTube</a>
    </div>
    <div class="img-accent reveal"><div class="img-frame"><img src="assets/img/bible.jpg" alt="An open Bible" loading="lazy"></div></div>
  </div>
</section>

<section class="section bg-blush">
  <div class="container">
    <div class="section-head reveal"><h2>The journey so far</h2></div>
    <div class="grid-2" style="align-items:start">
      <div class="timeline reveal">
        <div class="tl-item"><h3>2020 · The vision is birthed</h3><p>A deep spiritual burden for prayer, revival and a generation of prophetic intercessors.</p></div>
        <div class="tl-item"><h3>2023 · Prayer on YouTube</h3><p>People gather online for extended hours of prayer and intercession.</p></div>
        <div class="tl-item"><h3>2026 · Prison outreach, Douala</h3><p>The ministry takes prayer and the Gospel into prison in Douala, Cameroon.</p></div>
        <div class="tl-item"><h3>Rural missions supported</h3><p>Prophetic Intercession stands behind mission work in remote communities.</p></div>
        <div class="tl-item"><h3>24 Hours Prayer Stretch · Nov 2026</h3><p>A full day and night of prayer on Zoom, hosted by our founder — Psalm 85:6.</p></div>
        <div class="tl-item progress"><h3>Orphanage — in progress</h3><p>We are working toward a loving home for orphaned children.</p></div>
        <div class="tl-item future"><h3>Hospitals &amp; schools — the future</h3><p>A vision for healing and education in the communities we serve.</p></div>
      </div>
      <div class="img-frame tall reveal"><img src="assets/img/orphanage.jpg" alt="Children smiling together" loading="lazy"></div>
    </div>
  </div>
</section>
''' + CTA
page("founder.html", "Our Founder — Prophetic Intercession",
     "Meet the founder and host of Prophetic Intercession.", founder)

# ======================= OUTREACH =======================
outreach = page_hero("unity-hands.jpg", "Outreach", "Prayer with hands and feet",
                     "What we receive on our knees, we carry into the world. Here is what God has allowed us to do so far — and where He is leading us next.") + f'''
<section class="section-sm bg-dark">
  <div class="container">
    <div class="stats reveal">
      <div class="stat"><strong>Prison Outreach</strong><span>Completed</span></div>
      <div class="stat"><strong>Rural Missions</strong><span>Supported</span></div>
      <div class="stat"><strong>Orphanage</strong><span>In progress</span></div>
      <div class="stat"><strong>Hospitals &amp; Schools</strong><span>Future vision</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="outreach-row reveal" id="prison">
      <div class="video-frame"><button class="media-thumb video" data-yt="W36f2nty25o" aria-label="Play Prison Outreach Douala-Cameroon video"><img src="https://i.ytimg.com/vi/W36f2nty25o/hqdefault.jpg" alt="Prison Outreach Douala-Cameroon" loading="lazy"><span class="play"></span></button></div>
      <div>
        <span class="eyebrow">Completed outreach · Douala, Cameroon</span>
        <h2>Prison Outreach</h2>
        <p>Jesus said, “I was in prison, and ye came unto me” (Matthew 25:36). In Douala, Cameroon, we have taken the love of Christ behind prison walls — praying with inmates, sharing the Gospel and reminding men and women that they are not forgotten by God.</p>
        <ul>
          <li>Prayer and ministry of the Word with inmates</li>
          <li>Encouragement and hope for those who feel forgotten</li>
          <li>Practical care to meet everyday needs</li>
        </ul>
      </div>
    </div>

    <div class="outreach-row reveal" id="rural">
      <div class="img-frame"><img src="assets/img/rural-missions.jpg" alt="Rural landscape at dawn" loading="lazy"></div>
      <div>
        <span class="eyebrow">Supported mission</span>
        <h2>Rural Missions</h2>
        <p>Some of the most faithful Gospel work happens far from the city lights. We have supported rural missions so that remote communities can hear the Good News and experience the practical love of God.</p>
        <ul>
          <li>Support for missionaries serving remote communities</li>
          <li>Prayer covering for the mission field</li>
          <li>Helping the Gospel reach places that are often overlooked</li>
        </ul>
      </div>
    </div>

    <div class="outreach-row reveal" id="orphanage">
      <div class="img-frame"><img src="assets/img/orphanage.jpg" alt="Children laughing together" loading="lazy"></div>
      <div>
        <span class="eyebrow pink">In progress</span>
        <h2>Our Orphanage</h2>
        <p>“A father of the fatherless… is God in his holy habitation. God setteth the solitary in families” (Psalm 68:5–6). We are working toward an orphanage — a safe, loving, Christ-centred home where children can be cared for, educated and raised to know they are loved.</p>
        <ul>
          <li>A safe home and daily care for orphaned children</li>
          <li>Education, mentoring and discipleship</li>
          <li>A family built on the love of Christ</li>
        </ul>
        <a class="btn btn-pink mt-2" href="give.html">Help build the orphanage</a>
      </div>
    </div>
  </div>
</section>

<section class="section bg-blush" id="future">
  <div class="container">
    <div class="section-head reveal"><h2>The road ahead</h2><span class="eyebrow mb-0">Future vision</span></div>
    <p class="lead reveal">As God provides, we believe He is leading us to bring healing and education to the communities we serve.</p>
    <div class="grid-2 mt-2" style="align-items:stretch">
      <article class="ministry-card reveal">
        <div class="media"><img src="assets/img/hospitals.jpg" alt="Clean hospital ward" loading="lazy"><span class="status future">Future</span></div>
        <div class="body"><h3>Hospitals</h3><p class="sub">Bringing care and healing to communities with little access to medical help — ministering to body and soul.</p></div>
      </article>
      <article class="ministry-card reveal">
        <div class="media"><img src="assets/img/schools.jpg" alt="Children learning in a classroom" loading="lazy"><span class="status future">Future</span></div>
        <div class="body"><h3>Schools</h3><p class="sub">Opening doors of learning so children can grow in knowledge, character and faith.</p></div>
      </article>
    </div>
  </div>
</section>
''' + CTA
page("outreach.html", "Outreach — Prophetic Intercession",
     "Prison outreach, rural missions, our orphanage in progress and the future vision for hospitals and schools.", outreach)

# ======================= EVENTS =======================
events = page_hero("worship-night.jpg", "Events", "Gather with us",
                   "Prayer meetings, prayer stretches and special gatherings — most held online on Zoom so you can join from anywhere.") + '''
<section class="section bg-blush">
  <div class="container">
    <div class="section-head reveal"><h2>Upcoming events</h2></div>
    <div id="upcoming-events"></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2>Recent gatherings</h2></div>
    <div id="past-events"></div>
  </div>
</section>

<section class="section-sm bg-dark">
  <div class="container grid-2">
    <div class="reveal">
      <span class="eyebrow">Joining from anywhere</span>
      <h2>One altar, many time zones</h2>
      <p style="color:rgba(255,255,255,.78)">Our gatherings are announced in West Africa Time (WAT) with US times alongside. 6PM WAT is 11AM CST and 12 noon EST.</p>
    </div>
    <div class="reveal" style="text-align:right">
      <a class="btn btn-gold" href="prayer.html">Get event updates</a>
    </div>
  </div>
</section>
'''
page("events.html", "Events — Prophetic Intercession",
     "Upcoming prayer gatherings and recent events from Prophetic Intercession.", events,
     '<script src="assets/js/events.js"></script>\n')

# ======================= GIVE =======================
give = page_hero("giving.jpg", "Partner with us", "Support the ministry",
                 "If you would like to give to support the ministry, please use any of the giving options below. Thank you for partnering with us!") + '''
<section class="section bg-blush">
  <div class="container grid-2" style="align-items:start">
    <div>
      <div class="give-card reveal">
        <div class="give-logo momo">MTN<small>MoMo</small></div>
        <div class="give-body">
          <div class="label">MTN MoMo Transfer</div>
          <div class="give-value">+237 682 933 824</div>
          <div class="give-name">Name: Ndi Richard</div>
          <button class="copy-btn" data-copy="+237682933824">Copy number</button>
        </div>
      </div>
      <div class="give-card reveal">
        <div class="give-logo zelle">Zelle</div>
        <div class="give-body">
          <div class="label">Zelle</div>
          <div class="give-value">+1 (202) 509-6004</div>
          <div class="give-name">Name: Alambeh</div>
          <button class="copy-btn" data-copy="+12025096004">Copy number</button>
        </div>
      </div>
      <div class="give-card reveal">
        <div class="give-logo binance">BINANCE<small>BNB · USDT</small></div>
        <div class="give-body">
          <div class="label">BNB or USDT · BEP-20 (BNB Smart Chain)</div>
          <div class="give-value mono">0xDa8Eb0767eAA65009fc13db0e2027baf2353f94A</div>
          <div class="give-name">Send only on the BEP-20 network.</div>
          <button class="copy-btn" data-copy="0xDa8Eb0767eAA65009fc13db0e2027baf2353f94A">Copy address</button>
        </div>
      </div>
      <p class="note mt-2 reveal">Please double-check the number or wallet address before sending. Crypto sent on the wrong network cannot be recovered.</p>
    </div>
    <div class="reveal">
      <div class="img-frame"><img src="assets/img/flyer-partner.jpg" alt="Partner with Prophetic Intercession flier with giving details" loading="lazy" style="aspect-ratio:3/4"></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2>Where your seed goes</h2></div>
    <div class="grid-4">
      <article class="ministry-card reveal"><div class="media"><img src="assets/img/prayer-hands.jpg" alt="" loading="lazy"></div><div class="body"><h3>Prayer gatherings</h3><p class="sub">Hosting prayer meetings and prayer stretches for intercessors worldwide.</p></div></article>
      <article class="ministry-card reveal"><div class="media"><img src="assets/img/prison-outreach.jpg" alt="" loading="lazy"></div><div class="body"><h3>Prison outreach</h3><p class="sub">Taking hope and practical care to those behind bars.</p></div></article>
      <article class="ministry-card reveal"><div class="media"><img src="assets/img/rural-missions.jpg" alt="" loading="lazy"></div><div class="body"><h3>Rural missions</h3><p class="sub">Supporting the Gospel in remote communities.</p></div></article>
      <article class="ministry-card reveal"><div class="media"><img src="assets/img/orphanage.jpg" alt="" loading="lazy"></div><div class="body"><h3>The orphanage</h3><p class="sub">Building a home for children who need a family.</p></div></article>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container scripture reveal">
    <span class="eyebrow">Thank you for partnering with us!</span>
    <blockquote>May God richly reward you and enlarge your territory!</blockquote>
    <cite>1 Chronicles 4:10</cite>
  </div>
</section>
'''
page("give.html", "Give — Prophetic Intercession",
     "Partner with Prophetic Intercession through MTN MoMo, Zelle or BNB/USDT (BEP-20).", give)
print("built")

# ======================= PRAYER =======================
HOURS = "".join(f'<option>{h:02d}:00 – {(h + 1) % 24:02d}:00 WAT</option>' for h in range(24))
prayer = page_hero("prayer-hands.jpg", "Prayer", "Request, join and watch with us",
                   "Share your prayer request, take a watch on the altar, and pray with intercessors across the nations — day and night.") + f'''
<section class="section bg-blush">
  <div class="container grid-2" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Prayer request</span>
      <h2>Let us stand with you</h2>
      <p class="muted">“Is any among you afflicted? let him pray… The effectual fervent prayer of a righteous man availeth much.” — James 5:13, 16</p>
      <div class="grid-2 mt-2" style="gap:16px">
        {tile("heart", "Confidential", "Your request is only shared with our prayer team.")}
        {tile("flame", "Prayed over", "Our intercessors lift every request before the Lord.")}
      </div>
    </div>
    <div class="form-panel reveal">
      <form class="form" data-mail-form data-subject="Prayer Request">
        <div class="row">
          <div><label for="pr-name">Name</label><input id="pr-name" name="name" required autocomplete="name"></div>
          <div><label for="pr-email">Email or WhatsApp</label><input id="pr-email" name="contact" required></div>
        </div>
        <div><label for="pr-country">Country</label><input id="pr-country" name="country" autocomplete="country-name"></div>
        <div><label for="pr-msg">Your prayer request</label><textarea id="pr-msg" name="request" required></textarea></div>
        <label class="check"><input type="checkbox" name="private" value="Only intercessors may see this"> Only intercessors can see this.</label>
        <button class="btn btn-pink" type="submit">Send request</button>
      </form>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><h2>Prayer features</h2></div>
    <div class="grid-2" style="align-items:stretch">
      <div class="feature-panel reveal">
        <div class="focus-box" data-focus></div>
        <p class="muted mt-2 mb-0">Our current theme of prayer. Pray into it daily with the family.</p>
      </div>
      <div class="feature-panel reveal" id="watch">
        <span class="eyebrow">24/7 Watch sign-up</span>
        <h3>Take a watch on the altar</h3>
        <p class="muted">Pick a one-hour slot so the altar is always covered during our prayer stretches.</p>
        <form class="form" data-mail-form data-subject="Watch Sign-up">
          <div class="row">
            <div><label for="w-name">Name</label><input id="w-name" name="name" required></div>
            <div><label for="w-contact">Email or WhatsApp</label><input id="w-contact" name="contact" required></div>
          </div>
          <div><label for="w-hour">Preferred hour</label><select id="w-hour" name="hour">{HOURS}</select></div>
          <button class="btn btn-gold" type="submit">Sign me up</button>
        </form>
      </div>
      <div class="feature-panel reveal" id="bible-tracker">
        <span class="eyebrow">Bible reading tracker</span>
        <h3>Read through with us</h3>
        <p class="muted">Follow our corporate Bible reading for 21 or 40 days. Tap a day when you have read it — your progress is saved on this device.</p>
        <div class="plan-toggle"><button type="button" class="filter" data-plan="21">21 days</button><button type="button" class="filter" data-plan="40">40 days</button></div>
        <div class="bar"><span></span></div>
        <div class="pct"><span class="pct-text"></span><button type="button" class="link-btn" data-reset>Reset</button></div>
        <div class="days"></div>
      </div>
      <div class="feature-panel reveal">
        <span class="eyebrow">Join the intercessors</span>
        <h3>Pray with us on WhatsApp</h3>
        <p class="muted">Our WhatsApp prayer group is where fliers, prayer alerts, prophetic words and joining links are shared first.</p>
        <a class="btn btn-whatsapp" data-link="whatsapp" href="channels.html">{WA_ICON} Join the WhatsApp group</a>
        <hr style="border:0;border-top:1px solid var(--line);margin:24px 0">
        <h3>Prayer wall <span class="soon-tag">Coming soon</span></h3>
        <p class="muted mb-0">A wall where requests are posted and others can tap “I prayed for this.”</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container">
    <div class="section-head reveal"><h2>Join the intercessors</h2></div>
    <div class="grid-3">
      <div class="tile reveal"><div class="icon" style="color:#25d366">{WA_ICON}</div><h3>Join us on WhatsApp</h3><p>Get prayer alerts, fliers and joining links in our WhatsApp prayer group.</p><a class="btn btn-whatsapp mt-2" data-link="whatsapp" href="channels.html">Join the group</a></div>
      {tile("users", "Become an intercessor", "Take a prayer slot during our prayer stretches on Zoom and help keep the fire burning.")}
      {tile("globe", "Serve in outreach", "Volunteer for prison outreach, rural missions and the orphanage work.")}
    </div>
  </div>
</section>
''' + CTA
page("prayer.html", "Prayer — Prophetic Intercession",
     "Send a prayer request, sign up for a watch, track your Bible reading and join our WhatsApp prayer group.", prayer)

# old URL -> new prayer page
with open(os.path.join(R, "connect.html"), "w") as f:
    f.write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Prayer — Prophetic Intercession</title>'
            '<meta http-equiv="refresh" content="0; url=prayer.html"><link rel="canonical" href="prayer.html"></head>'
            '<body><a href="prayer.html">Continue to the Prayer page</a></body></html>\n')

# ======================= PROPHETIC =======================
prophetic = page_hero("bible.jpg", "Prophetic", "What God is saying",
                      "Prophetic words for the week and for the month, released to encourage, direct and build up the body of Christ.") + '''
<section class="section bg-blush">
  <div class="container">
    <div class="section-head reveal"><h2>Prophetic words</h2></div>
    <div id="prophetic-words"></div>
  </div>
</section>

<section class="section">
  <div class="container scripture reveal">
    <span class="eyebrow pink">Test every word</span>
    <blockquote>“Despise not prophesyings. Prove all things; hold fast that which is good.”</blockquote>
    <cite>1 Thessalonians 5:20–21</cite>
  </div>
</section>
''' + CTA
page("prophetic.html", "Prophetic Words — Prophetic Intercession",
     "Prophetic words for the week and month from Prophetic Intercession.", prophetic)

# ======================= CHANNELS =======================
channels = page_hero("worship-night.jpg", "Channels", "Our channels",
                     "Our prayers are online — on Zoom, TikTok and YouTube. Join and be part of this global prayer movement.") + f'''
<section class="section bg-blush">
  <div class="container">
    <div class="channel-grid">
      <div class="channel reveal"><div class="logo wa">{WA_ICON}</div><div>
        <h3>WhatsApp prayer group</h3>
        <p>Prayer alerts, fliers, prophetic words and joining links — shared here first.</p>
        <a class="btn btn-whatsapp" data-link="whatsapp" href="#">Join on WhatsApp</a></div></div>
      <div class="channel reveal" id="zoom"><div class="logo zoom">{ZOOM_ICON}</div><div>
        <h3>Zoom — prayer stretches</h3>
        <p>Our prayer stretches, like the 24 Hours Prayer Stretch, happen on Zoom. The joining link is shared on each event flier and in the WhatsApp group.</p>
        <a class="btn btn-outline-dark" href="events.html">See upcoming events</a></div></div>
      <div class="channel reveal"><div class="logo tt">{TT_ICON}</div><div>
        <h3>TikTok</h3>
        <p>Live prayer sessions and short prophetic words.</p>
        <a class="btn btn-outline-dark" data-link="tiktok" data-soon="Link coming soon" href="#">Follow on TikTok</a></div></div>
      <div class="channel reveal"><div class="logo yt">{YT_ICON}</div><div>
        <h3>YouTube</h3>
        <p>Prayer sessions and messages you can watch again.</p>
        <a class="btn btn-yt" data-link="youtube" data-soon="Link coming soon" href="#">Subscribe on YouTube</a></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2">
    <div class="reveal">
      <span class="eyebrow">A global altar</span>
      <h2>Praying across the nations</h2>
      <p class="muted">Intercessors join us from Africa, North America and around the world. Our gatherings are announced in West Africa Time (WAT) with US times alongside — 6PM WAT is 11AM CST and 12 noon EST.</p>
    </div>
    <div class="reach-out reveal">
      <div><span class="eyebrow">Reach out</span><h3 style="font-size:1.5rem">Want to be part of what God is doing?</h3>
      <p style="color:rgba(255,255,255,.78)">Send us a message or a prayer request and our team will get back to you.</p></div>
      <a class="btn btn-pink" href="prayer.html" style="align-self:flex-start">Contact us</a>
    </div>
  </div>
</section>
''' + CTA
page("channels.html", "Channels — Prophetic Intercession",
     "Join Prophetic Intercession on WhatsApp, Zoom, TikTok and YouTube.", channels)

# ======================= MEDIA =======================
media = page_hero("study.jpg", "Media", "Flyers, messages &amp; videos",
                  "Catch up on fliers, prophetic messages and recorded prayer sessions from Prophetic Intercession.") + '''
<section class="section bg-blush">
  <div class="container">
    <div class="yt-banner reveal"><div><strong>Prophetic Intercession on YouTube</strong><small>Prayer sessions, prophetic words and teachings · @PropheticAndIntercession</small></div><a class="btn btn-yt" data-link="youtube" href="#">Subscribe on YouTube</a></div>
    <div class="filters reveal" role="group" aria-label="Filter media">
      <button class="filter active" data-filter="all" aria-pressed="true">All</button>
      <button class="filter" data-filter="flyer" aria-pressed="false">Flyers</button>
      <button class="filter" data-filter="video" aria-pressed="false">Videos</button>
      <button class="filter" data-filter="message" aria-pressed="false">Messages</button>
    </div>
    <div class="media-grid" id="media-grid"></div>
  </div>
</section>
''' + CTA
page("media.html", "Media — Prophetic Intercession",
     "Flyers, messages and videos from Prophetic Intercession.", media)

# ======================= TESTIMONIES =======================
testimonies = page_hero("vision-sunrise.jpg", "Testimonies", "Answered prayers",
                        "“They overcame him by the blood of the Lamb, and by the word of their testimony.” — Revelation 12:11", "70% center") + '''
<section class="section bg-blush">
  <div class="container">
    <div class="section-head reveal"><h2>Testimonies</h2></div>
    <div class="testimony-grid" id="testimonies"></div>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="align-items:start">
    <div class="reveal">
      <span class="eyebrow">Share your testimony</span>
      <h2>What has God done for you?</h2>
      <p class="muted">Your story could be the encouragement someone else needs. Testimonies are only published with your permission, and you can choose to stay anonymous.</p>
    </div>
    <div class="form-panel reveal">
      <form class="form" data-mail-form data-subject="Testimony">
        <div class="row">
          <div><label for="t-name">Name</label><input id="t-name" name="name" required></div>
          <div><label for="t-place">City / Country</label><input id="t-place" name="place"></div>
        </div>
        <div><label for="t-contact">Email or WhatsApp</label><input id="t-contact" name="contact" required></div>
        <div><label for="t-msg">Your testimony</label><textarea id="t-msg" name="testimony" required></textarea></div>
        <label class="check"><input type="checkbox" name="permission" value="Yes, you may publish this"> You may publish this on the website.</label>
        <label class="check"><input type="checkbox" name="anonymous" value="Publish anonymously"> Please publish it anonymously.</label>
        <button class="btn btn-pink" type="submit">Share testimony</button>
      </form>
    </div>
  </div>
</section>
''' + CTA
page("testimonies.html", "Testimonies — Prophetic Intercession",
     "Answered prayers and testimonies from the Prophetic Intercession family.", testimonies)
print("built")
