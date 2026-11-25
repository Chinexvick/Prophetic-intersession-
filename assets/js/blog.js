/* =====================================================================
   BLOG POSTS — add a new post by copying one block below.
   - slug: short web-friendly id (letters, numbers, dashes) — used in the link
   - cover: image path (put images in assets/img/blog/) or any https image
   - body: written in simple "Markdown":
       ## Heading            ### Smaller heading
       **bold**   *italic*   [link text](https://...)
       > A quote or scripture
       - list item
       ![Image description](assets/img/blog/photo.jpg "Optional caption")
       A YouTube link on its own line becomes a playable video.
       Any other link on its own line becomes a link card.
   ===================================================================== */
var PI_POSTS = [
  {
    slug: "24-hours-prayer-stretch",
    title: "24 Hours Prayer Stretch: “Revive Us Again”",
    date: "2026-11-13",
    author: "Prophetic Intercession",
    category: "Events",
    cover: "assets/img/gallery/g08.jpg",
    coverPosition: "center 25%",
    excerpt: "For twenty-four hours on Zoom, intercessors across the nations stood together on the watch, crying out with the Psalmist for revival.",
    body: [
      "From Friday, November 13th to Saturday, November 14th, 2026, Prophetic Intercession held a **24 Hours Prayer Stretch** on Zoom, hosted by our convener, the Prophetic Intercessor.",
      "> Wilt thou not revive us again: that thy people may rejoice in thee? — Psalm 85:6",
      "## One altar, many time zones",
      "The stretch kicked off at **6PM WAT** (11AM CST · 12 noon EST), so intercessors from Africa, North America and around the world could take their place on the altar.",
      "![Prophetic Intercessor in fervent prayer](assets/img/gallery/g03.jpg \"Standing on the watch in prayer\")",
      "## Don’t miss the next one",
      "Prayer stretches are announced first in our WhatsApp prayer group. Join the family so you receive the next flier and the Zoom link as soon as they are released.",
      "https://chat.whatsapp.com/Fed6pLcGBTfJ7N0FmaZfYB"
    ]
  },
  {
    slug: "prison-outreach-douala",
    title: "Prison Outreach in Douala, Cameroon",
    date: "2026-07-23",
    author: "Prophetic Intercession",
    category: "Outreach",
    cover: "https://i.ytimg.com/vi/W36f2nty25o/hqdefault.jpg",
    excerpt: "“I was in prison, and ye came unto me.” Prophetic Intercession carried prayer and the Gospel behind prison walls in Douala.",
    body: [
      "> I was in prison, and ye came unto me. — Matthew 25:36",
      "Prophetic Intercession took the love of Christ behind prison walls in **Douala, Cameroon** — praying with inmates, sharing the Word of God and reminding men and women that they are not forgotten by Him.",
      "## Watch the outreach",
      "https://www.youtube.com/watch?v=W36f2nty25o",
      "## Why we go",
      "Our seventh mandate is *manifesting the compassion of Christ through social impact*: to translate spiritual convictions into tangible expressions of Christ’s love by reaching the vulnerable, helping the helpless and supporting disadvantaged communities.",
      "> Isaiah 58:6–12 · James 1:27 · Matthew 25:35–40 · Acts 10:38",
      "If you would like to stand with us in outreaches like this, you can [sow into the ministry](give.html)."
    ]
  },
  {
    slug: "how-prophetic-intercession-began",
    title: "How Prophetic Intercession Began",
    date: "2026-11-01",
    author: "Prophetic Intercession",
    category: "Our Story",
    cover: "assets/img/gallery/g01.jpg",
    coverPosition: "center 30%",
    excerpt: "Birthed in the wake of 2020 out of a burden for prayer and revival — and growing into a mandate to raise a global prophetic and intercessory tribe.",
    body: [
      "The vision of Prophetic Intercession was birthed in the wake of 2020, out of a deep spiritual burden for prayer, revival and the emergence of a generation of prophetic intercessors.",
      "## From YouTube to the nations",
      "The vision began to find full expression in **2023 through YouTube**, where people gathered for extended hours of prayer and intercession, standing in the gap for individuals, families and nations.",
      "What began as a burden to pray for people has grown into a greater mandate: raising a global prophetic and intercessory tribe equipped to discern the heart of God, birth His purposes through prayer and become instruments of divine intervention in their generation.",
      "> I will stand upon my watch, and set me upon the tower, and will watch to see what he will say unto me. — Habakkuk 2:1",
      "## Our vision",
      "To raise a generation of prophetic intercessors who will discern the heart of God, birth His purposes and manifest His glory across the nations.",
      "![Prophetic Intercessor in prayer](assets/img/gallery/g11.jpg \"A people upon the watch, a people consecrated to the altar\")",
      "## Our philosophy",
      "*“We are not raising people who merely know how to pray. We are raising people who know the God to whom they pray, discern the purposes of His heart, carry the burdens of His kingdom and become answers to the prayers they offer.”*",
      "Read more about [our sevenfold mandate](about.html#mandate)."
    ]
  }
];

/* ===================================================================== */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function safeUrl(u) {
    u = String(u || "").trim();
    return /^(https?:\/\/|mailto:|[a-z0-9_\-\/.#?=&]+$)/i.test(u) && !/^javascript:/i.test(u) ? u : "#";
  }
  function fmtDate(d) {
    var dt = new Date(String(d) + "T12:00:00");
    return isNaN(dt) ? "" : dt.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
  }
  function ytId(u) {
    var m = String(u).match(/(?:youtube\.com\/(?:watch\?v=|shorts\/|live\/)|youtu\.be\/)([\w-]{11})/);
    return m ? m[1] : null;
  }
  // inline formatting on already-escaped text
  function inline(t) {
    return t
      .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (_, txt, url) {
        var href = safeUrl(url.replace(/&amp;/g, "&"));
        var ext = /^https?:/i.test(href);
        return '<a href="' + esc(href) + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + ">" + txt + "</a>";
      })
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/\*([^*]+)\*/g, "<em>$1</em>");
  }
  function videoBlock(id) {
    return '<div class="post-video"><button class="media-thumb video" data-yt="' + esc(id) + '" aria-label="Play video">' +
      '<img src="https://i.ytimg.com/vi/' + esc(id) + '/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></button></div>';
  }
  function linkCard(url) {
    var host = url.replace(/^https?:\/\//, "").split("/")[0].replace(/^www\./, "");
    var label = /whatsapp/.test(host) ? "Join our WhatsApp prayer group" : /tiktok/.test(host) ? "Watch on TikTok" : /youtube|youtu\.be/.test(host) ? "Watch on YouTube" : "Open link";
    return '<a class="link-card" href="' + esc(safeUrl(url)) + '" target="_blank" rel="noopener"><span><strong>' + label + '</strong><small>' + esc(host) + '</small></span><span class="arrow">→</span></a>';
  }
  function render(lines) {
    var out = [], list = null;
    function closeList() { if (list) { out.push("<ul>" + list.join("") + "</ul>"); list = null; } }
    (lines || []).forEach(function (raw) {
      String(raw).split(/\n/).forEach(function (line) {
        var l = line.trim();
        if (!l) { closeList(); return; }
        if (/^- /.test(l)) { (list = list || []).push("<li>" + inline(esc(l.slice(2))) + "</li>"); return; }
        closeList();
        var m;
        if ((m = l.match(/^!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)$/))) {
          out.push('<figure class="post-figure"><img src="' + esc(safeUrl(m[2])) + '" alt="' + esc(m[1]) + '" loading="lazy">' +
            (m[3] ? "<figcaption>" + esc(m[3]) + "</figcaption>" : "") + "</figure>");
        } else if (/^https?:\/\/\S+$/.test(l)) {
          var id = ytId(l);
          out.push(id ? videoBlock(id) : linkCard(l));
        } else if (/^### /.test(l)) out.push("<h3>" + inline(esc(l.slice(4))) + "</h3>");
        else if (/^## /.test(l)) out.push("<h2>" + inline(esc(l.slice(3))) + "</h2>");
        else if (/^> /.test(l)) out.push("<blockquote>" + inline(esc(l.slice(2))) + "</blockquote>");
        else out.push("<p>" + inline(esc(l)) + "</p>");
      });
    });
    closeList();
    return out.join("\n");
  }
  function readMins(p) {
    var words = (p.body || []).join(" ").split(/\s+/).length;
    return Math.max(1, Math.round(words / 200));
  }
  var posts = PI_POSTS.slice().sort(function (a, b) { return String(b.date).localeCompare(String(a.date)); });
  function card(p, featured) {
    return '<a class="post-card' + (featured ? " featured" : "") + ' reveal in" href="blog-post.html?p=' + encodeURIComponent(p.slug) + '">' +
      '<div class="post-cover"><img src="' + esc(p.cover) + '" alt="" loading="lazy" style="object-position:' + esc(p.coverPosition || "center") + '"><span class="post-cat">' + esc(p.category) + '</span></div>' +
      '<div class="post-body"><span class="post-meta">' + fmtDate(p.date) + ' · ' + readMins(p) + ' min read</span>' +
      '<h3>' + esc(p.title) + '</h3><p>' + esc(p.excerpt) + '</p><span class="more-link">Read article →</span></div></a>';
  }

  /* ---------- Blog list ---------- */
  var list = $("#blog-list");
  if (list) {
    var cats = ["All"].concat(posts.map(function (p) { return p.category; }).filter(function (c, i, a) { return a.indexOf(c) === i; }));
    var filt = $("#blog-filters");
    var state = { cat: "All", q: "" };
    filt.innerHTML = cats.map(function (c, i) { return '<button class="filter' + (i ? "" : " active") + '" data-cat="' + esc(c) + '">' + esc(c) + "</button>"; }).join("");
    var draw = function () {
      var q = state.q.toLowerCase();
      var shown = posts.filter(function (p) {
        return (state.cat === "All" || p.category === state.cat) &&
          (!q || (p.title + " " + p.excerpt + " " + (p.body || []).join(" ")).toLowerCase().indexOf(q) > -1);
      });
      list.innerHTML = shown.length
        ? shown.map(function (p, i) { return card(p, i === 0 && state.cat === "All" && !q); }).join("")
        : '<div class="event-placeholder" style="grid-column:1/-1"><h3>No articles found</h3><p class="muted">Try another word or category.</p></div>';
    };
    filt.addEventListener("click", function (e) {
      var b = e.target.closest("[data-cat]"); if (!b) return;
      state.cat = b.getAttribute("data-cat");
      filt.querySelectorAll(".filter").forEach(function (x) { x.classList.toggle("active", x === b); });
      draw();
    });
    var search = $("#blog-search");
    if (search) search.addEventListener("input", function () { state.q = search.value.trim(); draw(); });
    draw();
  }

  /* ---------- Latest posts (home) ---------- */
  var latest = $("#latest-posts");
  if (latest) latest.innerHTML = posts.slice(0, 3).map(function (p) { return card(p, false); }).join("");

  /* ---------- Single post ---------- */
  var art = $("#post");
  if (art) {
    var slug = new URLSearchParams(location.search).get("p");
    var i = posts.map(function (p) { return p.slug; }).indexOf(slug);
    if (i < 0) {
      art.innerHTML = '<div class="container post-wrap" style="padding:160px 0 80px"><h1>Article not found</h1><p><a class="btn btn-gold" href="blog.html">Back to the blog</a></p></div>';
      return;
    }
    var p = posts[i];
    document.title = p.title + " — Prophetic Intercession";
    var md = document.querySelector('meta[name="description"]'); if (md) md.setAttribute("content", p.excerpt);
    var share = location.href;
    var prev = posts[i + 1], next = posts[i - 1];
    art.innerHTML =
      '<header class="post-hero"><img src="' + esc(p.cover) + '" alt="" style="object-position:' + esc(p.coverPosition || "center") + '">' +
      '<div class="container post-wrap"><a class="back-link" href="blog.html">← All articles</a><span class="post-cat">' + esc(p.category) + '</span>' +
      '<h1>' + esc(p.title) + '</h1><p class="post-meta">' + esc(p.author || "Prophetic Intercession") + ' · ' + fmtDate(p.date) + ' · ' + readMins(p) + ' min read</p></div></header>' +
      '<div class="container post-wrap"><div class="post-content">' + render(p.body) + '</div>' +
      '<div class="post-share"><span>Share this article</span>' +
        '<a class="btn btn-whatsapp" href="https://wa.me/?text=' + encodeURIComponent(p.title + " — " + share) + '" target="_blank" rel="noopener">WhatsApp</a>' +
        '<button class="btn btn-outline-dark" data-copy="' + esc(share) + '">Copy link</button></div>' +
      '<nav class="post-nav">' +
        (prev ? '<a href="blog-post.html?p=' + encodeURIComponent(prev.slug) + '"><small>← Older</small><strong>' + esc(prev.title) + '</strong></a>' : "<span></span>") +
        (next ? '<a class="next" href="blog-post.html?p=' + encodeURIComponent(next.slug) + '"><small>Newer →</small><strong>' + esc(next.title) + '</strong></a>' : "<span></span>") +
      '</nav></div>';
  }
})();
