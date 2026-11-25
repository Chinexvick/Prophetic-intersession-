/* =====================================================================
   SITE CONTENT — edit this file to update links, prophetic words,
   media posts (flyers, videos, messages) and testimonies.
   Leave a link as "" and the site shows "coming soon" instead.
   ===================================================================== */

var PI_SITE = {
  whatsapp: "https://chat.whatsapp.com/Fed6pLcGBTfJ7N0FmaZfYB",
  youtube: "https://www.youtube.com/@PropheticAndIntercession",
  tiktok: "https://www.tiktok.com/@propheticandintercession",
  zoom: "",         // standing Zoom link, if there is one
  contactEmail: ""  // where prayer requests, testimonies and watch sign-ups are emailed
};

/* Current prayer focus (shown on Home and the Prayer page) */
var PI_FOCUS = {
  label: "Prayer focus",
  title: "Revival",
  scripture: "Psalm 85:6",
  text: "“Wilt thou not revive us again: that thy people may rejoice in thee?”"
};

/* PROPHETIC WATCH — words and warnings, published and watched over.
   kind:   "word" or "warning"
   status: "watching"  (released, we are watching and praying over it)
           "unfolding" (we are seeing it begin to come to pass)
           "fulfilled" (it has come to pass — add the testimony in updates)
   updates: the watch log — add a dated line whenever something unfolds.
   youtube: video ID if the word was released on YouTube (optional)
   image:   flier image (optional)                                      */
var PI_WORDS = [
  { kind: "word", status: "watching", title: "I Break Camp and I Break Out", date: "2026-10-20", youtube: "F0afF5TdyZc",
    text: "A prophetic word and prayer released on our YouTube channel. Watch the full word below and pray into it.",
    updates: [{ date: "2026-10-20", text: "Word released on YouTube." }] },
  { kind: "word", status: "watching", title: "Prophecy Concerning You: This Is Why Things Are Not Working", date: "2026-01", youtube: "OUEhG2ll5DE",
    text: "A prophetic word released on our YouTube channel. Watch the full word below.",
    updates: [{ date: "2026-01", text: "Word released on YouTube." }] },
  { kind: "word", status: "watching", title: "Urgent Prophetic Word Before You Cross Over to 2026", date: "2025-12", youtube: "Dd-YtdZK7VM",
    text: "An urgent word and decree released before the crossover into 2026.",
    updates: [{ date: "2025-12", text: "Word released on YouTube." }] },
  { kind: "word", status: "watching", title: "Documentation Approval & Relocation", date: "2025-12", youtube: "3ju54pA0VYo",
    text: "A prophetic word concerning documentation approval and relocation. Watch the full word below.",
    updates: [{ date: "2025-12", text: "Word released on YouTube." }] },
  { kind: "warning", status: "watching", title: "Are You Conscious of Heaven and Hell?", date: "2024", youtube: "jQWX2ujmTlw",
    text: "“God said: Are you conscious of Heaven and Hell?” A sober call to the Church to live with eternity in view.",
    updates: [{ date: "2024", text: "Word released on YouTube." }] },
  { kind: "word", status: "watching", title: "There’s a Selection in the Realm of the Spirit", date: "2024", youtube: "0ZPy48qGnEM",
    text: "A prophetic word released on our YouTube channel. Watch the full word below.",
    updates: [{ date: "2024", text: "Word released on YouTube." }] },
  { kind: "word", status: "watching", title: "A Word for Upcoming Ministers of the Gospel", date: "2024", youtube: "YRGKfz8HxWs",
    text: "A prophetic word for those being raised into ministry.",
    updates: [{ date: "2024", text: "Word released on YouTube." }] },
  { kind: "warning", status: "watching", title: "Urgent Prophetic Word and Prayers for Now", date: "2024", youtube: "6bGHeS9JD5k",
    text: "An urgent word with prayers for this season.",
    updates: [{ date: "2024", text: "Word released on YouTube." }] }
  // , { kind: "warning", status: "watching", title: "Title", date: "2026-12-01", scripture: "Ezekiel 33:6",
  //     image: "assets/img/word-dec.jpg", text: "Full text of the word or warning…",
  //     updates: [{ date: "2026-12-01", text: "Released." }, { date: "2027-01-15", text: "We are seeing this begin to unfold…" }] }
];

/* MEDIA — flyers, videos and messages (the ministry's blog).
   type: "flyer" | "video" | "message"
   video: youtube = the ID after watch?v=   (or use url for TikTok etc.) */
var PI_MEDIA = [
  // Videos from the ministry's YouTube channel (@PropheticAndIntercession)
  { type: "video", title: "Understanding the Power of Priesthood", date: "2026-11-13", youtube: "tucTp7GnCZg", text: "Teaching on the ministry’s foundational conviction: everything by priesthood." },
  { type: "video", title: "Death Has Been Swallowed Up", date: "2026-10-27", youtube: "xNMD8HumRPI" },
  { type: "video", title: "Resurrection Power of God", date: "2026-10-25", youtube: "jBwouPXQB9E" },
  { type: "video", title: "I Break Camp and I Break Out", date: "2026-10-20", youtube: "F0afF5TdyZc", text: "Prophetic word and prayer." },
  { type: "video", title: "Flowing in the Prophetic", date: "2026-10-17", youtube: "TbLa9aiIARA" },
  { type: "video", title: "When the Word Dwells in You", date: "2026-10-01", youtube: "KbVQfWFZxCU", text: "Powerful prophetic teaching." },
  { type: "video", title: "Prison Outreach Douala-Cameroon", date: "2026-07-23", youtube: "W36f2nty25o", text: "Prophetic Intercession takes the love of Christ behind prison walls in Douala, Cameroon." },
  { type: "video", title: "Oh Lord, Set My Life in Order for You", date: "2026-07-12", youtube: "Wnt3I8jTosg", text: "Prophetic prayers — live prayer session." },
  { type: "video", title: "Don’t Be Moved by Giftings", date: "2026-06", youtube: "fC-RCzdncvk" },
  { type: "video", title: "My Glory Must Manifest — Day 1: Stop the Hiding!", date: "2026-04", youtube: "twKSkp44n1Q", text: "First night of the five-day “My Glory Must Manifest” prayer series." },
  { type: "video", title: "My Glory Must Manifest — Day 5: Grand Finale Breakthrough", date: "2026-04", youtube: "FY3Egdh5RiY" },
  { type: "video", title: "Urgent Prophetic Word Before You Cross Over to 2026", date: "2025-12", youtube: "Dd-YtdZK7VM" },
  { type: "video", title: "1 Hour of Prophetic Intercession and Groanings", date: "2024", youtube: "hGukZ_Xq2uo", text: "An hour of travail and intercession." },
  {
    type: "flyer",
    title: "24 Hours Prayer Stretch",
    date: "2026-11-06",
    image: "assets/img/flyer-24hr-prayer-stretch.jpg",
    text: "Fri. Nov 13th – Sat. Nov 14th, 2026 on Zoom · Psalm 85:6"
  }
  // , { type: "video", title: "Message title", date: "2026-12-01", youtube: "VIDEO_ID", text: "Short description" }
  // , { type: "video", title: "TikTok live replay", date: "2026-12-01", url: "https://www.tiktok.com/@.../video/...", image: "assets/img/thumb.jpg" }
  // , { type: "message", title: "Message title", date: "2026-12-01", text: "Full message text…" }
];

/* GALLERY — photos live in assets/img/gallery/ (gNN.jpg large, gNN-sm.jpg small) */
var PI_GALLERY = [
  { n: "01", caption: "In intercession" },
  { n: "02", caption: "Releasing the Word" },
  { n: "03", caption: "Open-armed worship" },
  { n: "04", caption: "Leading in worship" },
  { n: "05", caption: "Preaching the Word" },
  { n: "06", caption: "Praying over the Scriptures" },
  { n: "07", caption: "Ministering" },
  { n: "08", caption: "Fervent prayer" },
  { n: "09", caption: "Teaching" },
  { n: "10", caption: "Prophetic teaching" },
  { n: "11", caption: "Lost in worship" },
  { n: "12", caption: "Declaring the Word" },
  { n: "13", caption: "In the place of prayer" },
  { n: "14", caption: "Prophetic Intercessor — convener & host" }
];

/* GIVING — the methods shown in the giving engine on give.html */
var PI_GIVING = [
  {
    id: "momo", label: "MTN MoMo", sub: "Mobile Money · Cameroon", theme: "momo",
    fieldLabel: "MoMo number", value: "+237 682 933 824", copy: "+237682933824",
    name: "Ndi Richard", currency: "XAF", amounts: [5000, 10000, 25000, 50000],
    steps: ["Open your MTN MoMo app or the MoMo menu on your phone.", "Choose Transfer → to a MoMo user.", "Enter the number above and confirm the name shows Ndi Richard.", "Enter your amount, confirm with your PIN and send."]
  },
  {
    id: "zelle", label: "Zelle", sub: "Bank transfer · USA", theme: "zelle",
    fieldLabel: "Zelle phone number", value: "+1 (202) 509-6004", copy: "+12025096004",
    name: "Alambeh", currency: "USD", amounts: [20, 50, 100, 250],
    steps: ["Open your banking app and go to Zelle.", "Send money to the phone number above.", "Check that the recipient name shows Alambeh.", "Enter your amount and send."]
  },
  {
    id: "crypto", label: "BNB / USDT", sub: "Crypto · BEP-20 (BNB Smart Chain)", theme: "crypto",
    fieldLabel: "Wallet address (BEP-20)", value: "0xDa8Eb0767eAA65009fc13db0e2027baf2353f94A", copy: "0xDa8Eb0767eAA65009fc13db0e2027baf2353f94A",
    name: "", currency: "USDT", amounts: [10, 25, 50, 100], qr: true,
    warning: "Send only BNB or USDT on the BEP-20 (BNB Smart Chain) network. Funds sent on another network cannot be recovered.",
    steps: ["Open your wallet app (Binance, Trust Wallet, MetaMask…).", "Choose BNB or USDT and select the BEP-20 / BNB Smart Chain network.", "Paste the address above, then check the first and last characters match.", "Send and keep your transaction hash for your records."]
  }
];

/* TESTIMONIES — only add testimonies shared with permission. */
var PI_TESTIMONIES = [
  // { text: "What God did…", name: "First name or Anonymous", place: "City, Country" }
];

/* ===================================================================== */
(function () {
  "use strict";
  function $(s, r) { return (r || document).querySelector(s); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function fmtDate(d) {
    d = String(d || "");
    if (/^\d{4}$/.test(d)) return d;
    if (/^\d{4}-\d{2}$/.test(d)) return new Date(d + "-15T12:00:00").toLocaleDateString("en-GB", { month: "short", year: "numeric" });
    var dt = new Date(d + (String(d).length === 10 ? "T12:00:00" : ""));
    return isNaN(dt) ? "" : dt.toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });
  }
  function byDateDesc(a, b) { return String(b.date).localeCompare(String(a.date)); }

  // ---- Social links: <a data-link="whatsapp|youtube|tiktok|zoom"> ----
  document.querySelectorAll("[data-link]").forEach(function (a) {
    var url = PI_SITE[a.getAttribute("data-link")];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; }
    else {
      a.removeAttribute("href");
      a.classList.add("is-soon");
      a.setAttribute("aria-disabled", "true");
      var soon = a.getAttribute("data-soon");
      if (soon) a.textContent = soon;
    }
  });

  // ---- Prayer focus ----
  document.querySelectorAll("[data-focus]").forEach(function (el) {
    el.innerHTML = '<span class="eyebrow">' + esc(PI_FOCUS.label) + '</span>' +
      '<h3>' + esc(PI_FOCUS.title) + '</h3>' +
      '<blockquote>' + esc(PI_FOCUS.text) + '</blockquote>' +
      '<cite>' + esc(PI_FOCUS.scripture) + '</cite>';
  });

  // ---- Next prayer session card (needs events.js loaded first) ----
  var next = $("[data-next-session]");
  if (next && typeof PI_EVENTS !== "undefined") {
    var now = Date.now();
    var up = PI_EVENTS.filter(function (e) { return new Date(e.end).getTime() >= now; })
      .sort(function (a, b) { return new Date(a.start) - new Date(b.start); })[0];
    if (up) {
      next.innerHTML = '<span class="eyebrow">Next prayer session</span>' +
        '<h3>' + esc(up.title) + '</h3><div class="countdown" aria-live="polite"></div>' +
        '<p class="small">' + esc(up.dateText) + '<br>' + esc(up.timeText) + '</p>' +
        '<a class="btn btn-gold" href="events.html">Event details</a>';
      var cd = $(".countdown", next);
      var tick = function () {
        var ms = new Date(up.start).getTime() - Date.now();
        if (ms <= 0) { cd.innerHTML = '<span class="live">● Live now</span>'; return; }
        var d = Math.floor(ms / 864e5), h = Math.floor(ms / 36e5) % 24, m = Math.floor(ms / 6e4) % 60, s = Math.floor(ms / 1e3) % 60;
        var p = function (n) { return (n < 10 ? "0" : "") + n; };
        cd.innerHTML = [[d, "days"], [h, "hrs"], [m, "min"], [s, "sec"]].map(function (x) {
          return '<div><strong>' + p(x[0]) + '</strong><span>' + x[1] + '</span></div>';
        }).join("");
      };
      tick(); setInterval(tick, 1000);
    } else {
      next.innerHTML = '<span class="eyebrow">Next prayer session</span>' +
        '<h3>Announcing soon</h3>' +
        '<p class="small">Join our WhatsApp prayer group to be the first to receive the next flier and joining link.</p>' +
        (PI_SITE.whatsapp ? '<a class="btn btn-whatsapp" href="' + esc(PI_SITE.whatsapp) + '" target="_blank" rel="noopener">Join on WhatsApp</a>' : '');
    }
  }

  // ---- Prophetic watch ----
  var wordsEl = $("#prophetic-words");
  if (wordsEl) {
    var STATUS = { watching: "Watching", unfolding: "Unfolding", fulfilled: "Fulfilled" };
    var words = PI_WORDS.slice().sort(byDateDesc);
    var counts = { all: words.length, word: 0, warning: 0, fulfilled: 0 };
    words.forEach(function (w) { counts[w.kind] = (counts[w.kind] || 0) + 1; if (w.status === "fulfilled") counts.fulfilled++; });
    var filters = $("#watch-filters");
    if (filters) {
      filters.innerHTML = [["all", "All"], ["word", "Words"], ["warning", "Warnings"], ["fulfilled", "Fulfilled"]].map(function (f, i) {
        return '<button class="filter' + (i ? "" : " active") + '" data-watch="' + f[0] + '">' + f[1] + ' <span class="count">' + (counts[f[0]] || 0) + "</span></button>";
      }).join("");
    }
    var drawWords = function (f) {
      var list = words.filter(function (w) { return f === "all" || (f === "fulfilled" ? w.status === "fulfilled" : w.kind === f); });
      if (!list.length) {
        wordsEl.innerHTML = emptyState(f === "fulfilled" ? "Watching and praying" : "A fresh word is coming",
          f === "fulfilled" ? "As words come to pass, they will be marked fulfilled here with the testimony." :
          "Words and warnings will be posted here as they are released. Join our WhatsApp prayer group to receive them first.", f !== "fulfilled");
        return;
      }
      wordsEl.innerHTML = list.map(function (w) {
        var st = w.status || "watching";
        var media = w.youtube
          ? '<div class="watch-media"><button class="media-thumb video" data-yt="' + esc(w.youtube) + '" aria-label="Play ' + esc(w.title) + '"><img src="https://i.ytimg.com/vi/' + esc(w.youtube) + '/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></button></div>'
          : (w.image ? '<a class="watch-media" href="' + esc(w.image) + '" target="_blank" rel="noopener"><img src="' + esc(w.image) + '" alt="' + esc(w.title) + '" loading="lazy"></a>' : "");
        var log = (w.updates || []).slice().sort(function (a, b) { return String(b.date).localeCompare(String(a.date)); });
        var share = location.origin + location.pathname + "#" + encodeURIComponent(w.title);
        return '<article class="watch-card kind-' + esc(w.kind) + ' st-' + esc(st) + ' reveal in">' + media +
          '<div class="watch-body">' +
            '<div class="watch-tags"><span class="tag kind">' + (w.kind === "warning" ? "⚠ Warning" : "Prophetic word") + '</span>' +
            '<span class="tag status">' + esc(STATUS[st] || st) + '</span></div>' +
            '<h3>' + esc(w.title) + '</h3>' +
            '<div class="post-meta">Released ' + fmtDate(w.date) + (w.scripture ? " · " + esc(w.scripture) : "") + '</div>' +
            (w.text ? '<p>' + esc(w.text).replace(/\n/g, "<br>") + '</p>' : "") +
            (log.length ? '<details class="watch-log"><summary>Watch log (' + log.length + ')</summary><ol>' +
              log.map(function (u) { return '<li><time>' + fmtDate(u.date) + '</time>' + esc(u.text) + '</li>'; }).join("") + '</ol></details>' : "") +
            '<div class="watch-actions"><a class="btn btn-outline-dark" href="https://wa.me/?text=' + encodeURIComponent(w.title + " — Prophetic Intercession " + share) + '" target="_blank" rel="noopener">Share</a>' +
            '<a class="btn btn-gold" href="prayer.html">Pray with us</a></div>' +
          '</div></article>';
      }).join("");
    };
    if (filters) filters.addEventListener("click", function (e) {
      var b = e.target.closest("[data-watch]"); if (!b) return;
      filters.querySelectorAll(".filter").forEach(function (x) { x.classList.toggle("active", x === b); });
      drawWords(b.getAttribute("data-watch"));
    });
    drawWords("all");
  }

  // ---- Media (blog) ----
  var mediaEl = $("#media-grid");
  if (mediaEl) {
    var items = PI_MEDIA.slice().sort(byDateDesc);
    var render = function (filter) {
      var list = items.filter(function (m) { return filter === "all" || m.type === filter; });
      if (!list.length) {
        var label = { video: "Videos", flyer: "Flyers", message: "Messages" }[filter] || "Posts";
        mediaEl.innerHTML = '<div class="media-empty">' + emptyState(label + " coming soon",
          filter === "video" ? "Recorded prayer sessions and messages will appear here. Meanwhile, follow us on YouTube and TikTok." :
          "New posts will appear here soon.", filter !== "video") +
          (filter === "video" ? socialButtons() : "") + '</div>';
        return;
      }
      mediaEl.innerHTML = list.map(mediaCard).join("");
    };
    document.querySelectorAll("[data-filter]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        document.querySelectorAll("[data-filter]").forEach(function (b) { b.classList.toggle("active", b === btn); b.setAttribute("aria-pressed", b === btn); });
        render(btn.getAttribute("data-filter"));
      });
    });
    render("all");
  }

  // Latest videos on the home page
  var latest = $("#latest-videos");
  if (latest) {
    var vids = PI_MEDIA.filter(function (m) { return m.type === "video"; }).sort(byDateDesc).slice(0, 3);
    latest.innerHTML = vids.length ? vids.map(mediaCard).join("") : "";
  }

  // Click-to-play YouTube anywhere on the site (loads the player only when clicked)
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-yt]");
    if (!b) return;
    var f = document.createElement("iframe");
    f.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(b.getAttribute("data-yt")) + "?autoplay=1&rel=0";
    f.title = b.getAttribute("aria-label") || "Video";
    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
    f.allowFullscreen = true;
    b.replaceWith(f);
  });

  function mediaCard(m) {
    var media = "";
    if (m.type === "video" && m.youtube) {
      media = '<button class="media-thumb video" data-yt="' + esc(m.youtube) + '" aria-label="Play ' + esc(m.title) + '">' +
        '<img src="https://i.ytimg.com/vi/' + esc(m.youtube) + '/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></button>';
    } else if (m.type === "video") {
      media = '<a class="media-thumb video" href="' + esc(m.url) + '" target="_blank" rel="noopener">' +
        (m.image ? '<img src="' + esc(m.image) + '" alt="" loading="lazy">' : '<div class="thumb-fallback"></div>') + '<span class="play"></span></a>';
    } else if (m.type === "flyer") {
      media = '<a class="media-thumb flyer" href="' + esc(m.image) + '" target="_blank" rel="noopener"><img src="' + esc(m.image) + '" alt="' + esc(m.title) + ' flier" loading="lazy"></a>';
    }
    var label = { video: "Video", flyer: "Flyer", message: "Message" }[m.type] || "Post";
    return '<article class="media-card type-' + esc(m.type) + '">' + media +
      '<div class="body"><span class="label">' + label + ' · ' + fmtDate(m.date) + '</span>' +
      '<h3>' + esc(m.title) + '</h3>' +
      (m.text ? '<p class="' + (m.type === "message" ? "message-text" : "sub") + '">' + esc(m.text).replace(/\n/g, "<br>") + '</p>' : "") +
      '</div></article>';
  }

  // ---- Testimonies ----
  var tEl = $("#testimonies");
  if (tEl) {
    tEl.innerHTML = PI_TESTIMONIES.length
      ? PI_TESTIMONIES.map(function (t) {
          return '<figure class="testimony reveal in"><blockquote>' + esc(t.text) + '</blockquote>' +
            '<figcaption>— ' + esc(t.name || "Shared with permission") + (t.place ? ', ' + esc(t.place) : "") + '</figcaption></figure>';
        }).join("")
      : emptyState("Testimonies are being gathered",
          "Has God answered prayer for you through this ministry? Share your testimony below, and with your permission it will be published here to encourage others.", false);
  }

  function emptyState(title, text, withWa) {
    return '<div class="event-placeholder"><div class="icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg></div>' +
      '<span class="eyebrow pink">Coming soon</span><h3>' + esc(title) + '</h3>' +
      '<p class="muted" style="max-width:540px;margin-inline:auto">' + esc(text) + '</p>' +
      (withWa && PI_SITE.whatsapp ? '<a class="btn btn-whatsapp" href="' + esc(PI_SITE.whatsapp) + '" target="_blank" rel="noopener">Join our WhatsApp</a>' : "") +
      '</div>';
  }
  function socialButtons() {
    var out = [["youtube", "YouTube"], ["tiktok", "TikTok"]].filter(function (s) { return PI_SITE[s[0]]; })
      .map(function (s) { return '<a class="btn btn-outline-dark" href="' + esc(PI_SITE[s[0]]) + '" target="_blank" rel="noopener">' + s[1] + '</a>'; });
    return out.length ? '<div class="hero-row" style="justify-content:center;margin-top:1rem">' + out.join("") + '</div>' : "";
  }

  // ---- Bible reading tracker (saved on this device) ----
  var tracker = $("#bible-tracker");
  if (tracker) {
    var KEY = "pi-bible-tracker";
    var state;
    try { state = JSON.parse(localStorage.getItem(KEY)) || null; } catch (e) { state = null; }
    if (!state) state = { plan: 21, done: [] };
    var save = function () { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} };
    var draw = function () {
      var n = state.plan, done = state.done.filter(function (d) { return d <= n; });
      var pct = Math.round(done.length / n * 100);
      var days = "";
      for (var i = 1; i <= n; i++) {
        var on = done.indexOf(i) > -1;
        days += '<button type="button" class="day' + (on ? " on" : "") + '" data-day="' + i + '" aria-pressed="' + on + '">' + i + '</button>';
      }
      tracker.querySelector(".days").innerHTML = days;
      tracker.querySelector(".bar span").style.width = pct + "%";
      tracker.querySelector(".pct-text").textContent = done.length + " of " + n + " days · " + pct + "%";
      tracker.querySelectorAll("[data-plan]").forEach(function (b) { b.classList.toggle("active", +b.getAttribute("data-plan") === n); });
    };
    tracker.addEventListener("click", function (e) {
      var d = e.target.closest("[data-day]"), p = e.target.closest("[data-plan]"), r = e.target.closest("[data-reset]");
      if (d) {
        var k = +d.getAttribute("data-day"), i = state.done.indexOf(k);
        if (i > -1) state.done.splice(i, 1); else state.done.push(k);
      } else if (p) { state.plan = +p.getAttribute("data-plan"); }
      else if (r) { state.done = []; }
      else return;
      save(); draw();
    });
    draw();
  }
})();
