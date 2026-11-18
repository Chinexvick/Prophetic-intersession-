# Prophetic Intercession — Website

Static multi-page site (HTML/CSS/JS, no build step). Open `index.html` or host the folder on any static host (Netlify, Vercel, GitHub Pages).

Pages: `index.html`, `about.html`, `founder.html`, `outreach.html`, `events.html`, `connect.html` (prayer requests), `give.html`.

## Common edits
- **Add an event / new flier:** put the image in `assets/img/` and add an entry to `PI_EVENTS` in `assets/js/events.js`. Events sort into Upcoming / Recent automatically by date.
- **Prayer-request email:** set `contactEmail` at the top of `assets/js/main.js`.
- **Brand colours:** CSS variables at the top of `assets/css/style.css`.
