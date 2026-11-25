/*
 * GET /api/youtube
 * Reads the ministry's public YouTube channel feed and returns the latest
 * uploads as JSON, so new videos appear on the website automatically.
 *
 * - Cached at Vercel's edge for 5 minutes (s-maxage=300), so a new upload
 *   shows up on the site within ~5 minutes of going public.
 * - Videos whose titles match EXCLUDE (crypto / token "wealth transfer"
 *   content) are left off the church website on purpose.
 */
const CHANNEL_ID = "UCK50_Bw9RulYECpCHM3TdgQ"; // @PropheticAndIntercession
const FEED = "https://www.youtube.com/feeds/videos.xml?channel_id=" + CHANNEL_ID;
const EXCLUDE = /(\$[A-Z]{2,}|crypto|token|solana|wealth\s*transfer|market update|trading)/i;

function decode(s) {
  return String(s || "")
    .replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, "$1")
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"')
    .replace(/&#39;|&apos;/g, "'").replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n))
    .replace(/&amp;/g, "&");
}
function tag(xml, name) {
  const m = xml.match(new RegExp("<" + name + "(?:\\s[^>]*)?>([\\s\\S]*?)</" + name + ">"));
  return m ? decode(m[1]).trim() : "";
}
// "Title | Prophetic Intercession #tag #tag" -> "Title"
function cleanTitle(t) {
  return t.replace(/\s*#\S+/g, "").replace(/\s*[|·-]\s*Prophetic\s+Intercession\s*$/i, "").replace(/\s{2,}/g, " ").trim();
}
function firstLine(desc, title) {
  const t = title.toLowerCase().slice(0, 25);
  const line = desc.split(/\n+/).map((l) => l.trim()).find((l) =>
    l && !/^#/.test(l) && !/https?:|whatsapp|subscribe|join (our|us)|follow us|telegram|zelle|momo|donat/i.test(l) &&
    !l.toLowerCase().startsWith(t) && /[a-z]/i.test(l)) || "";
  return line.length > 140 ? line.slice(0, 137).trimEnd() + "…" : line;
}

module.exports = async function handler(req, res) {
  try {
    const r = await fetch(FEED, { headers: { "User-Agent": "Mozilla/5.0 (compatible; website feed reader)" } });
    if (!r.ok) throw new Error("feed status " + r.status);
    const xml = await r.text();
    const videos = (xml.match(/<entry>[\s\S]*?<\/entry>/g) || []).map((e) => {
      const rawTitle = tag(e, "title");
      return {
        type: "video",
        youtube: tag(e, "yt:videoId"),
        title: cleanTitle(rawTitle),
        rawTitle,
        date: tag(e, "published").slice(0, 10),
        text: firstLine(tag(e, "media:description"), cleanTitle(rawTitle)),
        short: /\/shorts\//.test((e.match(/<link[^>]+href="([^"]+)"/) || [])[1] || ""),
      };
    }).filter((v) => v.youtube && !EXCLUDE.test(v.rawTitle))
      .map(({ rawTitle, ...v }) => v)
      .filter((v, i, all) => all.findIndex((x) => x.title.toLowerCase() === v.title.toLowerCase()) === i); // same session uploaded twice

    res.setHeader("Content-Type", "application/json; charset=utf-8");
    res.setHeader("Cache-Control", "public, s-maxage=300, stale-while-revalidate=86400");
    res.status(200).send(JSON.stringify({ channel: "@PropheticAndIntercession", fetched: new Date().toISOString(), videos }));
  } catch (err) {
    // The site keeps showing its built-in list if the feed is unavailable.
    res.setHeader("Cache-Control", "public, s-maxage=60");
    res.status(502).json({ error: "feed unavailable", videos: [] });
  }
};
