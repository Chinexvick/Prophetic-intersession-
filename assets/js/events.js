/* =====================================================================
   EVENTS LIST — the only place you need to edit to add an event.
   Copy one block, change the details, and drop the flier image into
   assets/img/. Events sort themselves into "Upcoming" and "Past"
   automatically based on the end date.
   Times: use ISO format with the WAT offset, e.g. 2026-11-13T18:00:00+01:00
   ===================================================================== */
var PI_EVENTS = [
  {
    title: "24 Hours Prayer Stretch",
    start: "2026-11-13T18:00:00+01:00",
    end: "2026-11-14T18:00:00+01:00",
    dateText: "Fri. Nov 13th – Sat. Nov 14th, 2026",
    timeText: "Kick off 6PM WAT · 11AM CST · 12 Noon EST",
    venue: "Zoom",
    host: "Prophetic Intercessor",
    scripture: "Psalm 85:6",
    flyer: "assets/img/flyer-24hr-prayer-stretch.jpg",
    description:
      "Twenty-four unbroken hours of worship, travail and prophetic intercession, crying out with the Psalmist: “Wilt thou not revive us again: that thy people may rejoice in thee?” Intercessors from Africa, North America and around the world joined on Zoom to stand in the gap for families, nations and the next move of God.",
    link: ""
  }
  // , {
  //   title: "New Event Title",
  //   start: "2026-12-04T18:00:00+01:00",
  //   end:   "2026-12-04T21:00:00+01:00",
  //   dateText: "Fri. Dec 4th, 2026",
  //   timeText: "6PM WAT · 11AM CST · 12 Noon EST",
  //   venue: "Zoom",
  //   host: "Prophetic Intercessor",
  //   scripture: "",
  //   flyer: "assets/img/flyer-new-event.jpg",
  //   description: "Short description of the event.",
  //   link: "" // Zoom / WhatsApp / registration link
  // }
];

(function () {
  "use strict";
  var upEl = document.getElementById("upcoming-events");
  var pastEl = document.getElementById("past-events");
  if (!upEl && !pastEl) return;

  var now = Date.now();
  var upcoming = PI_EVENTS.filter(function (e) { return new Date(e.end).getTime() >= now; })
    .sort(function (a, b) { return new Date(a.start) - new Date(b.start); });
  var past = PI_EVENTS.filter(function (e) { return new Date(e.end).getTime() < now; })
    .sort(function (a, b) { return new Date(b.start) - new Date(a.start); });

  function esc(s) {
    return String(s || "").replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function card(e, isPast) {
    var facts = [
      ["Date", e.dateText], ["Time", e.timeText], ["Venue", e.venue], ["Host", e.host]
    ].filter(function (f) { return f[1]; }).map(function (f) {
      return '<div><span>' + f[0] + '</span><strong>' + esc(f[1]) + '</strong></div>';
    }).join("");
    var action = "";
    if (!isPast && e.link) {
      action = '<a class="btn btn-pink" href="' + esc(e.link) + '" target="_blank" rel="noopener">Join this event</a>';
    } else if (!isPast) {
      action = '<a class="btn btn-pink" href="connect.html">Get the joining details</a>';
    } else {
      action = '<a class="btn btn-outline-dark" href="' + esc(e.flyer) + '" target="_blank" rel="noopener">View flier</a>';
    }
    return '<article class="event-card reveal in">' +
      '<div class="flyer"><img src="' + esc(e.flyer) + '" alt="' + esc(e.title) + ' flier" loading="lazy"></div>' +
      '<div class="info">' +
        '<span class="badge ' + (isPast ? "past" : "upcoming") + '">' + (isPast ? "Recent gathering" : "Upcoming") + '</span>' +
        '<h3>' + esc(e.title) + '</h3>' +
        (e.scripture ? '<div class="event-date">' + esc(e.scripture) + '</div>' : "") +
        '<p class="muted">' + esc(e.description) + '</p>' +
        '<div class="event-facts">' + facts + '</div>' +
        action +
      '</div></article>';
  }

  if (upEl) {
    upEl.innerHTML = upcoming.length
      ? upcoming.map(function (e) { return card(e, false); }).join("")
      : '<div class="event-placeholder">' +
          '<div class="icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></div>' +
          '<span class="eyebrow pink">Coming soon</span>' +
          '<h3>A new gathering is being announced</h3>' +
          '<p class="muted" style="max-width:520px;margin-inline:auto">The next prayer gathering flier is on its way. Check back shortly, or reach out and we will send you the details as soon as they are released.</p>' +
          '<a class="btn btn-outline-dark" href="connect.html">Notify me</a>' +
        '</div>';
  }
  if (pastEl) {
    pastEl.innerHTML = past.length
      ? past.map(function (e) { return card(e, true); }).join("")
      : '<p class="muted">Past gatherings will appear here.</p>';
  }
})();
