/* Prophetic Intercession — gallery marquee, lightbox and giving engine */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  var G = (typeof PI_GALLERY !== "undefined") ? PI_GALLERY : [];
  var big = function (g) { return "assets/img/gallery/g" + g.n + ".jpg"; };
  var small = function (g) { return "assets/img/gallery/g" + g.n + "-sm.jpg"; };

  /* ---------- Two-row marquee (home) ---------- */
  $$("[data-marquee]").forEach(function (wrap) {
    var half = Math.ceil(G.length / 2);
    var rows = [G.slice(0, half), G.slice(half)];
    wrap.innerHTML = rows.map(function (row, r) {
      var items = row.map(function (g) {
        return '<button class="mq-item" data-lightbox="' + G.indexOf(g) + '" aria-label="View photo: ' + esc(g.caption) + '">' +
          '<img src="' + small(g) + '" alt="' + esc(g.caption) + '" loading="lazy" decoding="async"></button>';
      }).join("");
      // duplicated once so the loop is seamless; the copy is hidden from screen readers
      return '<div class="mq-row ' + (r ? "mq-ltr" : "mq-rtl") + '"><div class="mq-track">' + items +
        '<div class="mq-dup" aria-hidden="true">' + items.replace(/<button /g, '<button tabindex="-1" ') + '</div></div></div>';
    }).join("");
  });

  /* ---------- Gallery grid (gallery page) ---------- */
  var grid = $("#gallery-grid");
  if (grid) {
    grid.innerHTML = G.map(function (g, i) {
      return '<figure class="g-item reveal in" style="--d:' + (i % 6) * 60 + 'ms"><button data-lightbox="' + i + '" aria-label="View photo: ' + esc(g.caption) + '">' +
        '<img src="' + small(g) + '" srcset="' + small(g) + ' 420w, ' + big(g) + ' 1000w" sizes="(max-width:600px) 50vw, 25vw" alt="' + esc(g.caption) + '" loading="lazy" decoding="async">' +
        '</button><figcaption>' + esc(g.caption) + '</figcaption></figure>';
    }).join("");
  }

  /* ---------- Lightbox ---------- */
  var lb, cur = 0, lastFocus;
  function buildLb() {
    lb = document.createElement("div");
    lb.className = "lightbox";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.setAttribute("aria-label", "Photo viewer");
    lb.innerHTML = '<button class="lb-close" aria-label="Close">&times;</button>' +
      '<button class="lb-nav lb-prev" aria-label="Previous photo">&#8249;</button>' +
      '<figure><img alt=""><figcaption></figcaption></figure>' +
      '<button class="lb-nav lb-next" aria-label="Next photo">&#8250;</button>';
    document.body.appendChild(lb);
    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.closest(".lb-close")) close();
      else if (e.target.closest(".lb-prev")) show(cur - 1);
      else if (e.target.closest(".lb-next")) show(cur + 1);
    });
    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) show(cur + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }
  function show(i) {
    cur = (i + G.length) % G.length;
    var img = $("img", lb);
    img.classList.remove("in");
    img.onload = function () { img.classList.add("in"); };
    img.src = big(G[cur]);
    img.alt = G[cur].caption;
    $("figcaption", lb).textContent = G[cur].caption + "  ·  " + (cur + 1) + " / " + G.length;
  }
  function open(i) {
    if (!lb) buildLb();
    lastFocus = document.activeElement;
    show(i);
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
    $(".lb-close", lb).focus();
  }
  function close() {
    lb.classList.remove("open");
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-lightbox]");
    if (t && G.length) open(+t.getAttribute("data-lightbox"));
  });
  document.addEventListener("keydown", function (e) {
    if (!lb || !lb.classList.contains("open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowRight") show(cur + 1);
    if (e.key === "ArrowLeft") show(cur - 1);
  });

  /* ---------- Giving engine ---------- */
  var engine = $("#give-engine");
  if (engine && typeof PI_GIVING !== "undefined") {
    var methodsEl = $(".ge-methods", engine);
    var panel = $(".ge-panel", engine);
    var state = { id: null, amount: null };

    methodsEl.innerHTML = PI_GIVING.map(function (m, i) {
      return '<button class="ge-method theme-' + m.theme + '" role="tab" aria-selected="false" data-method="' + m.id + '" style="--i:' + i + '">' +
        '<span class="ge-logo">' + logo(m.theme) + '</span>' +
        '<span class="ge-mtext"><strong>' + esc(m.label) + '</strong><small>' + esc(m.sub) + '</small></span>' +
        '<span class="ge-check" aria-hidden="true"></span></button>';
    }).join("");

    methodsEl.addEventListener("click", function (e) {
      var b = e.target.closest("[data-method]");
      if (b) select(b.getAttribute("data-method"), true);
    });

    function fmt(n, cur) {
      return Number(n).toLocaleString("en-US") + " " + cur;
    }

    function select(id, user) {
      var m = PI_GIVING.filter(function (x) { return x.id === id; })[0];
      if (!m) return;
      state.id = id; state.amount = null;
      $$(".ge-method", methodsEl).forEach(function (b) {
        var on = b.getAttribute("data-method") === id;
        b.classList.toggle("active", on);
        b.setAttribute("aria-selected", on);
      });
      engine.setAttribute("data-theme", m.theme);
      if (user && history.replaceState) history.replaceState(null, "", "#" + id);

      panel.classList.remove("show");
      void panel.offsetWidth; // restart the animation
      panel.innerHTML =
        '<div class="ge-sweep" aria-hidden="true"></div>' +
        '<div class="ge-head"><span class="ge-logo big">' + logo(m.theme) + '</span><div><span class="eyebrow">Give with ' + esc(m.label) + '</span><h3>' + esc(m.sub) + '</h3></div></div>' +
        '<div class="ge-amount"><span class="ge-label">Choose a seed (optional)</span><div class="ge-chips">' +
          m.amounts.map(function (a) { return '<button type="button" class="ge-chip" data-amount="' + a + '">' + fmt(a, m.currency) + '</button>'; }).join("") +
          '<label class="ge-custom"><span class="sr-only">Other amount</span><input type="number" min="1" inputmode="decimal" placeholder="Other"><em>' + esc(m.currency) + '</em></label>' +
        '</div></div>' +
        '<div class="ge-detail">' +
          '<span class="ge-label">' + esc(m.fieldLabel) + '</span>' +
          '<div class="ge-value' + (m.qr ? " mono" : "") + '">' + esc(m.value) + '</div>' +
          (m.name ? '<div class="ge-name">Account name: <strong>' + esc(m.name) + '</strong></div>' : "") +
          '<div class="ge-actions"><button type="button" class="btn btn-dark ge-copy" data-copy="' + esc(m.copy) + '">Copy ' + (m.qr ? "address" : "number") + '</button>' +
          (m.qr ? '<button type="button" class="btn btn-outline-dark ge-qr-toggle">Show QR code</button>' : "") + '</div>' +
          (m.qr ? '<div class="ge-qr" hidden></div>' : "") +
          (m.warning ? '<p class="ge-warn">' + esc(m.warning) + '</p>' : "") +
        '</div>' +
        '<ol class="ge-steps">' + m.steps.map(function (s, i) { return '<li style="--i:' + i + '">' + esc(s) + '</li>'; }).join("") + '</ol>' +
        '<div class="ge-summary" aria-live="polite"></div>' +
        '<button type="button" class="btn btn-gold ge-done">I have sent my seed</button>';
      panel.classList.add("show");
      wirePanel(m);
      if (user && window.innerWidth < 900) panel.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    function setAmount(a) {
      var m = state.m;
      state.amount = a;
      $$(".ge-chip", panel).forEach(function (c) { c.classList.toggle("active", +c.getAttribute("data-amount") === a); });
      var summary = $(".ge-summary", panel);
      if (summary) summary.innerHTML = a ? 'Your seed: <strong>' + esc(fmt(a, m.currency)) + '</strong> via ' + esc(m.label) : "";
    }
    // one delegated listener for everything inside the panel
    panel.addEventListener("click", function (e) {
      var m = state.m;
      var chip = e.target.closest(".ge-chip");
      if (chip) { $(".ge-custom input", panel).value = ""; setAmount(+chip.getAttribute("data-amount")); }
      var cp = e.target.closest(".ge-copy");
      if (cp) copy(cp);
      var q = e.target.closest(".ge-qr-toggle");
      if (q) toggleQr(q, m);
      if (e.target.closest(".ge-done")) thanks(m);
      if (e.target.closest(".ge-again")) select(m.id, true);
    });
    panel.addEventListener("input", function (e) {
      if (!e.target.closest(".ge-custom")) return;
      var v = parseFloat(e.target.value);
      setAmount(v > 0 ? v : null);
    });
    function wirePanel(m) { state.m = m; }

    function copy(btn) {
      var text = btn.getAttribute("data-copy");
      var ok = function () {
        btn.classList.add("copied");
        var old = btn.textContent; btn.textContent = "Copied ✓";
        if (window.PI_toast) window.PI_toast("Copied: " + text);
        setTimeout(function () { btn.classList.remove("copied"); btn.textContent = old; }, 1800);
      };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(ok, fb); else fb();
      function fb() {
        var ta = document.createElement("textarea"); ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); ok(); } catch (e) { if (window.PI_toast) window.PI_toast("Please copy manually: " + text); }
        document.body.removeChild(ta);
      }
    }

    function toggleQr(btn, m) {
      var box = $(".ge-qr", panel);
      if (!box.hidden) { box.hidden = true; btn.textContent = "Show QR code"; return; }
      if (!box.innerHTML && typeof qrcode === "function") {
        var qr = qrcode(0, "M"); qr.addData(m.copy); qr.make();
        box.innerHTML = qr.createSvgTag({ cellSize: 5, margin: 3, scalable: true }) + '<small>Scan with your wallet app · BEP-20 only</small>';
      }
      box.hidden = false; btn.textContent = "Hide QR code";
    }

    function thanks(m) {
      var amt = state.amount ? esc(fmt(state.amount, m.currency)) + " " : "";
      panel.classList.remove("show"); void panel.offsetWidth;
      panel.innerHTML = '<div class="ge-thanks">' + burst() +
        '<div class="ge-heart" aria-hidden="true">♥</div>' +
        '<span class="eyebrow">Thank you for partnering with us!</span>' +
        '<h3>Your ' + amt + 'seed keeps the altar burning.</h3>' +
        '<p class="ge-bless">May God richly reward you and enlarge your territory!</p>' +
        '<div class="ge-actions" style="justify-content:center">' +
        (PI_SITE && PI_SITE.whatsapp ? '<a class="btn btn-whatsapp" href="' + esc(PI_SITE.whatsapp) + '" target="_blank" rel="noopener">Join our WhatsApp family</a>' : "") +
        '<button type="button" class="btn btn-outline-dark ge-again">Give again</button></div></div>';
      panel.classList.add("show");
    }

    function burst() {
      var out = '<div class="ge-burst" aria-hidden="true">';
      for (var i = 0; i < 18; i++) {
        out += '<i style="--a:' + (i * 20) + 'deg;--d:' + (60 + (i % 3) * 30) + 'px;--c:' + ["var(--gold)", "var(--pink)", "#fff"][i % 3] + '"></i>';
      }
      return out + "</div>";
    }

    function logo(theme) {
      if (theme === "momo") return '<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#ffcb05"/><ellipse cx="24" cy="24" rx="17" ry="10.5" fill="none" stroke="#00487a" stroke-width="2.6"/><text x="24" y="28.5" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="11.5" fill="#00487a">MTN</text></svg>';
      if (theme === "zelle") return '<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#6d1ed4"/><path d="M16 15h16v4.2L21.6 30H32v4H16v-4.2L26.4 19H16z" fill="#fff"/><rect x="22.6" y="10.5" width="2.8" height="5.5" fill="#fff"/><rect x="22.6" y="32" width="2.8" height="5.5" fill="#fff"/></svg>';
      return '<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#111"/><g fill="#f0b90b"><path d="M24 11l4.2 4.2-4.2 4.2-4.2-4.2z"/><path d="M24 28.6l4.2 4.2L24 37l-4.2-4.2z"/><path d="M15.2 19.8l4.2 4.2-4.2 4.2L11 24z"/><path d="M32.8 19.8L37 24l-4.2 4.2-4.2-4.2z"/><path d="M24 19.8l4.2 4.2-4.2 4.2-4.2-4.2z"/></g></svg>';
    }

    var hashMethod = function () {
      var h = (location.hash || "").slice(1);
      return PI_GIVING.some(function (m) { return m.id === h; }) ? h : null;
    };
    select(hashMethod() || PI_GIVING[0].id, false);
    window.addEventListener("hashchange", function () {
      var h = hashMethod();
      if (h && h !== state.id) select(h, false);
    });
  }
})();
