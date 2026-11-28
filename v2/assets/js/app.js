/* Prophetic Intercession — Version B interactions */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var body = document.body;
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var CONFIG = window.PI_SITE || { contactEmail: "" };

  /* ---------- page transition ---------- */
  var pt = $(".pt");
  // back/forward cache: make sure the curtain is down when a page is shown again
  window.addEventListener("pageshow", function () { if (pt) pt.classList.remove("cover"); });
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[href]");
    if (!a || !pt || reduce || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === "_blank") return;
    var href = a.getAttribute("href");
    if (!href || href.charAt(0) === "#" || /^(https?:|mailto:|tel:)/.test(href) || a.hasAttribute("download")) return;
    e.preventDefault();
    pt.classList.add("cover");
    setTimeout(function () { location.href = href; }, 480);
  });

  /* ---------- nav: hide on scroll down, show on scroll up ---------- */
  var nav = $(".nav"), lastY = 0;
  window.addEventListener("scroll", function () {
    var y = window.scrollY;
    if (nav && !body.classList.contains("menu-open")) nav.classList.toggle("hide", y > lastY && y > 300);
    lastY = y;
  }, { passive: true });

  /* ---------- full-screen menu ---------- */
  var mb = $(".menu-btn");
  function setMenu(open) {
    body.classList.toggle("menu-open", open);
    if (mb) { mb.setAttribute("aria-expanded", String(open)); mb.querySelector("span").textContent = open ? "Close" : "Menu"; }
    var m = $(".menu"); if (m) m.setAttribute("aria-hidden", String(!open));
  }
  if (mb) mb.addEventListener("click", function () { setMenu(!body.classList.contains("menu-open")); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* ---------- reveals ---------- */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (en) {
    en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } });
  }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" }) : null;
  function watch(el) { if (io) io.observe(el); else el.classList.add("in"); }
  $$(".rv, .split-line, .split, .hero-stage").forEach(watch);
  // content rendered later by data scripts
  new MutationObserver(function () { $$(".rv:not(.in)").forEach(watch); }).observe(document.body, { childList: true, subtree: true });

  /* ---------- statement: words light up as you scroll ---------- */
  $$(".statement p").forEach(function (p) {
    var html = p.innerHTML.split(/(<span class="serif">.*?<\/span>)/).map(function (chunk) {
      if (/^<span class="serif">/.test(chunk)) return chunk.replace('class="serif"', 'class="serif w"');
      return chunk.split(/(\s+)/).map(function (w) { return /^\s+$/.test(w) || !w ? w : '<span class="w">' + w + '</span>'; }).join("");
    }).join("");
    p.innerHTML = html;
    var words = $$(".w", p);
    function upd() {
      var r = p.getBoundingClientRect(), vh = innerHeight;
      var prog = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      var n = Math.round(prog * words.length);
      words.forEach(function (w, i) { w.classList.toggle("on", i < n); });
    }
    if (reduce) words.forEach(function (w) { w.classList.add("on"); });
    else { window.addEventListener("scroll", upd, { passive: true }); upd(); }
  });

  /* ---------- horizontal scroll section ---------- */
  $$(".hscroll").forEach(function (sec) {
    var track = $(".hscroll-track", sec), pin = $(".hscroll-pin", sec);
    function size() {
      if (innerWidth <= 800) { sec.style.height = ""; track.style.transform = ""; return; }
      var dist = track.scrollWidth - innerWidth + 60;
      sec.style.height = (innerHeight + Math.max(0, dist)) + "px";
      sec.dataset.dist = Math.max(0, dist);
    }
    function move() {
      if (innerWidth <= 800) return;
      var r = sec.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, -r.top / (sec.offsetHeight - innerHeight)));
      track.style.transform = "translate3d(" + (-p * (+sec.dataset.dist || 0)) + "px,0,0)";
    }
    size(); move();
    window.addEventListener("resize", function () { size(); move(); });
    window.addEventListener("scroll", move, { passive: true });
    window.addEventListener("load", function () { size(); move(); });
  });

  /* ---------- stacking cards: earlier cards shrink as the next arrives ---------- */
  var cards = $$(".stack-card");
  if (cards.length && !reduce) {
    var onStack = function () {
      if (innerWidth <= 800) { cards.forEach(function (c) { c.style.transform = ""; c.style.filter = ""; }); return; }
      cards.forEach(function (c, i) {
        var next = cards[i + 1]; if (!next) return;
        var gap = next.getBoundingClientRect().top - c.getBoundingClientRect().top;
        var t = Math.min(1, Math.max(0, 1 - gap / c.offsetHeight));
        c.style.transform = "scale(" + (1 - t * 0.06) + ")";
        c.style.filter = "brightness(" + (1 - t * 0.35) + ")";
      });
    };
    window.addEventListener("scroll", onStack, { passive: true }); onStack();
  }

  /* ---------- toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; toastEl.setAttribute("role", "status"); body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastEl._t); toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }
  window.PI_toast = toast;

  /* ---------- copy buttons (outside the giving engine) ---------- */
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-copy]");
    if (!btn || btn.closest(".ge-panel")) return;
    var text = btn.getAttribute("data-copy");
    var done = function () { var o = btn.textContent; btn.classList.add("copied"); btn.textContent = "Copied ✓"; toast("Copied"); setTimeout(function () { btn.classList.remove("copied"); btn.textContent = o; }, 1800); };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done, function () { toast(text); });
    else toast(text);
  });

  /* ---------- forms -> email ---------- */
  $$("form[data-mail-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form), lines = [];
      data.forEach(function (v, k) { if (String(v).trim()) lines.push(k.charAt(0).toUpperCase() + k.slice(1) + ": " + v); });
      if (!CONFIG.contactEmail) { toast("Our email line is being set up. Please reach us on our WhatsApp prayer group for now."); return; }
      location.href = "mailto:" + CONFIG.contactEmail + "?subject=" + encodeURIComponent((form.getAttribute("data-subject") || "Message") + " — " + (data.get("name") || "Website visitor")) + "&body=" + encodeURIComponent(lines.join("\n"));
    });
  });

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
