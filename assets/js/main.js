/* Prophetic Intercession — site interactions */
(function () {
  "use strict";

  // ------------------------------------------------------------------
  // SITE SETTINGS — fill these in when the ministry confirms them.
  // contactEmail: where prayer requests / contact messages are sent.
  // ------------------------------------------------------------------
  var CONFIG = {
    contactEmail: "" // e.g. "hello@propheticintercession.org"
  };

  var body = document.body;
  var header = document.querySelector(".site-header");

  // Header background on scroll
  function onScroll() {
    if (!header) return;
    header.classList.toggle("scrolled", window.scrollY > 40);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () {
        body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") body.classList.remove("nav-open");
    });
  }

  // Carousels
  document.querySelectorAll(".carousel").forEach(function (c) {
    var track = c.querySelector(".track");
    var prev = c.querySelector("[data-prev]");
    var next = c.querySelector("[data-next]");
    function step() {
      var card = track.firstElementChild;
      return card ? card.getBoundingClientRect().width + 20 : 300;
    }
    if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
    if (next) next.addEventListener("click", function () { track.scrollBy({ left: step(), behavior: "smooth" }); });
  });

  // Reveal on scroll
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // Toast helper
  var toastEl;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "toast";
      toastEl.setAttribute("role", "status");
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }
  window.PI_toast = toast;

  // Copy-to-clipboard buttons (giving details)
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () {
        btn.classList.add("copied");
        var old = btn.textContent;
        btn.textContent = "Copied ✓";
        toast("Copied: " + text);
        setTimeout(function () { btn.classList.remove("copied"); btn.textContent = old; }, 2000);
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(done, fallback);
      } else { fallback(); }
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); done(); } catch (e) { toast("Please copy manually: " + text); }
        document.body.removeChild(ta);
      }
    });
  });

  // Prayer request / contact forms -> opens the visitor's email app
  document.querySelectorAll("form[data-mail-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form);
      var subject = (form.getAttribute("data-subject") || "Message") + " — " + (data.get("name") || "Website visitor");
      var lines = [];
      data.forEach(function (v, k) { if (String(v).trim()) lines.push(k.charAt(0).toUpperCase() + k.slice(1) + ": " + v); });
      if (!CONFIG.contactEmail) {
        toast("Our prayer line email is being set up — please check back soon.");
        return;
      }
      window.location.href = "mailto:" + CONFIG.contactEmail +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(lines.join("\n"));
      toast("Opening your email app…");
    });
  });

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
