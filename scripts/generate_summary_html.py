#!/usr/bin/env python3
"""Generate beautiful HTML pages from Horizon Daily summary Markdown files."""

import re
from pathlib import Path

import markdown

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SUMMARIES_DIR = PROJECT_ROOT / "data" / "summaries"
OUTPUT_DIR = SUMMARIES_DIR / "html"

# ---------------------------------------------------------------------------
# HTML template — single-page, self-contained, dark magazine style
# ---------------------------------------------------------------------------
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
/* ===================================================================
   Horizon Daily — Base & Reset
   =================================================================== */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg-primary:    #0b0b12;
  --bg-secondary:  #12121c;
  --bg-card:       #181825;
  --bg-card-hover: #1e1e30;
  --bg-tag:        #1e1e32;
  --text-primary:  #e8e8ed;
  --text-secondary:#a0a0b8;
  --text-muted:    #6b6b80;
  --border:        #252540;
  --border-light:  #1f1f35;
  --accent:        #b0a8a0;
  --accent-glow:   rgba(176, 168, 160, 0.10);
  --gold:          #f0b90b;
  --gold-dim:      #8a6d20;
  --red:           #ff5e5e;
  --green:         #5effa0;
  --font-sans:     "Inter", "SF Pro Display", "Segoe UI", system-ui, -apple-system, sans-serif;
  --font-mono:     "JetBrains Mono", "SF Mono", "Cascadia Code", "Consolas", monospace;
  --radius-sm:     6px;
  --radius-md:     10px;
  --radius-lg:     16px;
  --shadow-card:   0 1px 3px rgba(0,0,0,.4), 0 0 0 1px var(--border);
  --shadow-glow:   0 0 28px var(--accent-glow);
  --max-width:     820px;
}}

html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--font-sans);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

/* ===================================================================
   Header
   =================================================================== */
.header {{
  position: sticky; top: 0; z-index: 100;
  background: rgba(11,11,18,.82);
  backdrop-filter: blur(18px) saturate(140%);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  border-bottom: 1px solid var(--border);
  padding: 14px 24px;
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
}}
.header-brand {{
  display: flex; align-items: center; gap: 12px;
  font-weight: 700; font-size: 1.1rem; letter-spacing: -.01em;
  color: var(--text-primary); text-decoration: none;
}}
.header-logo {{
  width: 34px; height: 34px; border-radius: var(--radius-sm);
  background: linear-gradient(135deg, #c8a880, #c0a898);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.15rem;
}}
.header-date {{
  font-size: .85rem; color: var(--text-secondary);
  font-weight: 500;
}}
.header-actions {{ display: flex; gap: 8px; }}
.btn {{
  display: inline-flex; align-items: center; gap: 6px;
  padding: 7px 14px; border-radius: var(--radius-sm);
  font-size: .82rem; font-weight: 600; cursor: pointer;
  border: 1px solid var(--border);
  background: var(--bg-secondary); color: var(--text-secondary);
  transition: all .15s;
  text-decoration: none;
  font-family: var(--font-sans);
}}
.btn:hover {{ background: var(--bg-card); color: var(--text-primary); border-color: var(--accent); }}

/* ===================================================================
   Layout
   =================================================================== */
.wrapper {{
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 32px 24px 80px;
}}

/* ===================================================================
   Hero / summary bar
   =================================================================== */
.hero {{
  text-align: center; padding: 40px 0 28px;
}}
.hero h1 {{
  font-size: 2rem; font-weight: 800; letter-spacing: -.025em;
  background: linear-gradient(135deg, var(--text-primary) 20%, var(--accent) 80%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 8px;
}}
.hero .subtitle {{
  color: var(--text-secondary); font-size: .95rem;
}}
.stats-row {{
  display: flex; justify-content: center; gap: 28px; margin-top: 18px;
}}
.stat {{
  text-align: center;
}}
.stat-value {{
  font-size: 1.6rem; font-weight: 800; color: var(--accent);
}}
.stat-label {{
  font-size: .75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: .05em;
}}

/* ===================================================================
   Table of Contents
   =================================================================== */
.toc {{
  background: var(--bg-card); border-radius: var(--radius-lg);
  border: 1px solid var(--border); padding: 20px 24px;
  margin-bottom: 36px;
}}
.toc-title {{
  font-size: .8rem; text-transform: uppercase; letter-spacing: .1em;
  color: var(--text-muted); margin-bottom: 12px; font-weight: 700;
}}
.toc-list {{ list-style: none; columns: 2; column-gap: 24px; }}
@media (max-width: 640px) {{ .toc-list {{ columns: 1; }} }}
.toc-item {{
  padding: 4px 0; font-size: .88rem; break-inside: avoid;
}}
.toc-item a {{
  color: var(--text-secondary); text-decoration: none;
  display: flex; align-items: center; gap: 8px;
  transition: color .12s;
}}
.toc-item a:hover {{ color: var(--accent); }}
.toc-star {{
  font-size: .72rem; color: var(--gold); white-space: nowrap;
  font-weight: 600;
}}

/* ===================================================================
   Item cards
   =================================================================== */
.item {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 28px 30px;
  margin-bottom: 24px;
  transition: border-color .2s, box-shadow .2s;
  scroll-margin-top: 80px;
}}
.item:hover {{
  border-color: #353560;
  box-shadow: var(--shadow-glow);
}}
.item-header {{
  display: flex; align-items: flex-start; justify-content: space-between;
  gap: 16px; margin-bottom: 12px;
}}
.item-title {{
  font-size: 1.18rem; font-weight: 700; line-height: 1.4; letter-spacing: -.01em;
  color: var(--text-primary); text-decoration: none;
}}
.item-title:hover {{ color: var(--accent); }}
.item-title a {{ color: inherit; text-decoration: none; }}
.item-title a:hover {{ color: var(--accent); }}

.rating {{
  display: inline-flex; align-items: center; gap: 4px;
  background: #1f1a0a; border: 1px solid #3d3515;
  border-radius: 20px; padding: 4px 12px;
  font-size: .8rem; font-weight: 700; white-space: nowrap;
  color: var(--gold); flex-shrink: 0;
}}
.rating.star-9 {{ background: #1f1a0a; border-color: #5c4a10; box-shadow: 0 0 12px rgba(240,185,11,.12); }}
.rating.star-8 {{ border-color: #3d3515; }}
.rating.star-7 {{ border-color: #2d2818; opacity: .85; }}

.item-body {{ color: var(--text-secondary); font-size: .92rem; line-height: 1.75; }}
.item-body p {{ margin-bottom: 12px; }}
.item-body p:last-child {{ margin-bottom: 0; }}

/* Source line */
.source-line {{
  display: flex; flex-wrap: wrap; align-items: center; gap: 8px 16px;
  margin-top: 14px; padding-top: 14px;
  border-top: 1px solid var(--border-light);
  font-size: .78rem; color: var(--text-muted);
}}
.source-line a {{ color: var(--accent); text-decoration: none; font-weight: 500; }}
.source-line a:hover {{ text-decoration: underline; }}

/* Background / Discussion sections */
.section-label {{
  display: inline-block; font-size: .72rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: .07em;
  color: var(--text-muted); margin-top: 14px; margin-bottom: 6px;
}}
.item-body strong {{ color: var(--text-primary); }}

/* Tags */
.tags {{
  display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px;
}}
.tag {{
  display: inline-block; padding: 3px 10px;
  font-size: .72rem; font-weight: 600;
  border-radius: 12px;
  background: var(--bg-tag); color: var(--text-muted);
  border: 1px solid var(--border-light);
  transition: all .12s;
}}
.tag:hover {{ color: var(--accent); border-color: var(--accent); background: #1f1f3a; }}

/* Details / References */
details {{
  margin-top: 12px; margin-bottom: 4px;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  overflow: hidden;
}}
details[open] {{ border-color: var(--border); }}
summary {{
  padding: 8px 14px; font-size: .78rem; font-weight: 600;
  color: var(--text-muted); cursor: pointer;
  user-select: none;
  background: var(--bg-secondary);
  transition: color .12s;
}}
summary:hover {{ color: var(--accent); }}
details .references {{
  padding: 8px 14px 12px; font-size: .8rem;
}}
details .references ul {{ list-style: none; padding: 0; }}
details .references li {{
  padding: 3px 0; font-size: .8rem;
}}
details .references a {{
  color: var(--accent); text-decoration: none;
}}
details .references a:hover {{ text-decoration: underline; }}

/* ===================================================================
   Footer
   =================================================================== */
.footer {{
  text-align: center; padding: 40px 0 0;
  color: var(--text-muted); font-size: .78rem;
  border-top: 1px solid var(--border); margin-top: 40px;
}}
.footer a {{ color: var(--accent); text-decoration: none; }}

/* Hide markdown horizontal rules left from separators */
.item hr {{ display: none; }}

/* ===================================================================
   Scrollbar
   =================================================================== */
::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: var(--bg-primary); }}
::-webkit-scrollbar-thumb {{ background: #2a2a40; border-radius: 4px; }}
::-webkit-scrollbar-thumb:hover {{ background: #3a3a55; }}

/* ===================================================================
   Responsive
   =================================================================== */
@media (max-width: 640px) {{
  .wrapper {{ padding: 16px 14px 60px; }}
  .item {{ padding: 18px 16px; }}
  .hero h1 {{ font-size: 1.45rem; }}
  .header {{ padding: 10px 14px; }}
  .header-date {{ display: none; }}
  .header-brand {{ font-size: .95rem; }}
  .item-header {{ flex-direction: column; gap: 8px; }}
  .rating {{ align-self: flex-start; }}
}}
</style>
</head>
<body>

<header class="header">
  <a class="header-brand" href="#">
    <span class="header-logo">🌐</span>
    Horizon Daily
  </a>
  <span class="header-date">{date_display}</span>
  <div class="header-actions">
    <a class="btn" href="#toc">📑 Index</a>
    <button class="btn" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">⬆ Top</button>
  </div>
</header>

<div class="wrapper">

  <section class="hero">
    <h1>{title}</h1>
    <p class="subtitle">{subtitle}</p>
    <div class="stats-row">
      <div class="stat"><div class="stat-value">{item_count}</div><div class="stat-label">Selected</div></div>
      <div class="stat"><div class="stat-value">{total_items}</div><div class="stat-label">Total Feed</div></div>
      <div class="stat"><div class="stat-value">{avg_score}</div><div class="stat-label">Avg Score</div></div>
    </div>
  </section>

  <nav class="toc" id="toc">
    <div class="toc-title">📑 Table of Contents</div>
    <ol class="toc-list">
      {toc_items}
    </ol>
  </nav>

  <main>
    {body}
  </main>

  <footer class="footer">
    Generated by <a href="https://github.com/strom-fung/horizon">Horizon</a>
    — AI-powered information aggregation ·
    <span id="gen-time">{gen_time}</span>
  </footer>

</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Markdown → HTML conversion
# ---------------------------------------------------------------------------
def _extract_meta(md_text: str) -> dict:
    """Pull title, subtitle, and stats from the top of the markdown."""
    lines = md_text.splitlines()
    title = ""
    subtitle = ""
    items_from = 0
    total_from = 0
    items_count = 0

    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("> "):
            subtitle = line[2:].strip()
            # Try to extract numbers
            m = re.search(r"(\d+)\s+items.*?(\d+)\s+important", subtitle, re.IGNORECASE)
            if m:
                total_from = int(m.group(1))
                items_from = int(m.group(2))
            else:
                m2 = re.search(r"(\d+)\s+条.*?(\d+)\s+条", subtitle)
                if m2:
                    total_from = int(m2.group(1))
                    items_from = int(m2.group(2))
        elif line.startswith("---"):
            break

    # Count items in output body (## headings)
    for line in lines:
        if re.match(r"^##\s", line):
            items_count += 1

    return {
        "title": title,
        "subtitle": subtitle,
        "total_items": total_from,
        "item_count": items_count,
    }


def _extract_toc_items(md_text: str) -> list[dict]:
    """Extract TOC items (numbered list after first ---)."""
    lines = md_text.splitlines()
    toc = []
    in_toc = False
    for line in lines:
        if line.strip() == "---" and not in_toc:
            in_toc = True
            continue
        if in_toc:
            if line.strip() == "---":
                break
            m = re.match(
                r"^\d+\.\s+\[(.+?)\]\(#item-\d+\)\s+(?:⭐️?\s*)?(\d+\.\d+)/10", line
            )
            if m:
                toc.append({"title": m.group(1), "score": float(m.group(2))})
    return toc


def _strip_front_matter(md_text: str) -> str:
    """Return only the items portion of the markdown (after the second ---)."""
    lines = md_text.splitlines()
    sep_count = 0
    result_start = 0
    for i, line in enumerate(lines):
        if line.strip() == "---":
            sep_count += 1
            if sep_count == 2:
                result_start = i + 1
                break
    return "\n".join(lines[result_start:])


def _postprocess_item_html(item_html: str) -> str:
    """Post-process a single item's HTML fragment."""
    # Wrap details content in div.references, then add class
    def _wrap_refs(m):
        inner = m.group(1)
        if "</summary>" in inner:
            idx = inner.index("</summary>")
            return "<details class=\"ref-details\">{before}<div class=\"references\">{after}</div></details>".format(
                before=inner[: idx + len("</summary>")],
                after=inner[idx + len("</summary>"):],
            )
        return '<details class="ref-details">{0}</details>'.format(inner)

    item_html = re.sub(r"<details>(.*?)</details>", _wrap_refs, item_html, flags=re.DOTALL)

    # Wrap H2 in item-header div and add title class
    item_html = re.sub(
        r"<h2>(.*?)</h2>",
        r'<div class="item-header"><span class="item-title">\1</span></div>',
        item_html,
    )

    # Extract rating from the title and add a rating badge
    def _add_rating(m):
        title_content = m.group(1)
        rating_match = re.search(r"(⭐️?\s*(\d+\.\d+)/10)\s*$", title_content)
        if rating_match:
            score = float(rating_match.group(2))
            cls = _score_class(score)
            clean_title = title_content[: rating_match.start()].rstrip()
            # unwrap the anchor link from markdown
            anchor_match = re.match(r'<a href="([^"]+)">(.+)</a>', clean_title)
            if anchor_match:
                clean_title = '<a href="{0}">{1}</a>'.format(
                    anchor_match.group(1), anchor_match.group(2)
                )
            return '<div class="item-header"><span class="item-title">{title}</span><span class="rating {cls}">{stars}</span></div>'.format(
                title=clean_title,
                cls=cls,
                stars=rating_match.group(1),
            )
        return '<div class="item-header"><span class="item-title">{0}</span></div>'.format(
            title_content
        )

    item_html = re.sub(
        r'<div class="item-header"><span class="item-title">(.*?)</span></div>',
        _add_rating,
        item_html,
    )

    # Add class to source line (EN + ZH patterns)
    item_html = re.sub(
        r"<p>(hackernews|rss)\b",
        r'<p class="source-line">\1',
        item_html,
    )

    # Style labels (EN + ZH)
    item_html = re.sub(
        r"<p><strong>(Background|Discussion|背景|社区讨论)</strong>",
        r'<p><span class="section-label">\1</span>',
        item_html,
    )

    # Extract tags: both EN ("Tags") and ZH ("标签")
    def _wrap_tags(m):
        tag_text = m.group(1)
        # markdown converts backticks to <code> tags
        tags = re.findall(r"<code>#([^<]+)</code>", tag_text)
        if not tags:
            tags = re.findall(r"#([\w\s-]+?)(?:[,.]|$)", tag_text)
        if not tags:
            tags = re.findall(r"#([\w-]+)", tag_text)
        tag_html = "".join(
            '<span class="tag">#{0}</span>'.format(t.strip()) for t in tags
        )
        return '<div class="tags">{0}</div>'.format(tag_html)

    item_html = re.sub(
        r"<p><strong>Tags</strong>:\s*(.*?)</p>",
        _wrap_tags,
        item_html,
        flags=re.DOTALL,
    )
    item_html = re.sub(
        r"<p><strong>标签</strong>:\s*(.*?)</p>",
        _wrap_tags,
        item_html,
        flags=re.DOTALL,
    )

    return item_html


def _convert_items_to_html(items_md: str) -> str:
    """Convert the items portion of markdown into styled HTML cards."""
    md = markdown.Markdown(extensions=["extra", "sane_lists", "smarty"])

    # Split into individual items by <a id="item-N"></a> anchors
    parts = re.split(r'(<a id="item-\d+"></a>)', items_md)
    # parts[0] is empty or whitespace before first anchor
    # Then pairs: parts[1] = anchor, parts[2] = item content, parts[3] = next anchor, ...

    result_parts = []
    i = 1  # skip leading content before first anchor
    while i < len(parts):
        anchor = parts[i]
        content = parts[i + 1] if i + 1 < len(parts) else ""
        i += 2

        # Convert to HTML
        html = md.convert(anchor + "\n\n" + content)

        # Remove the duplicate anchor (div already has the id)
        html = re.sub(r"<p>?<a id=\"item-\d+\"></a></p>?", "", html, count=1)

        # Post-process
        html = _postprocess_item_html(html)

        result_parts.append(html)

    # Wrap each in a card
    cards = "\n".join(
        '<div class="item" id="{0}">{1}</div>'.format(
            "item-{0}".format(idx + 1), item_html
        )
        for idx, item_html in enumerate(result_parts)
    )

    return cards


def _score_class(score: float) -> str:
    """Return CSS class name for the rating badge."""
    if score >= 9:
        return "star-9"
    elif score >= 8:
        return "star-8"
    elif score >= 7:
        return "star-7"
    return ""


def _format_toc_html(toc_items: list[dict]) -> str:
    """Build the TOC <ol> with rating badges."""
    out = []
    for i, item in enumerate(toc_items, 1):
        sc = item["score"]
        cls = _score_class(sc)
        out.append(
            f'<li class="toc-item">'
            f'<a href="#item-{i}">'
            f'<span class="toc-star">{sc:.1f}</span>'
            f'{item["title"]}</a></li>'
        )
    return "\n".join(out)


def convert_markdown_to_html(md_text: str, lang: str = "en") -> str:
    """Convert a single Markdown summary to a full HTML page."""
    meta = _extract_meta(md_text)
    toc_items = _extract_toc_items(md_text)

    # Strip front matter (title, subtitle, TOC, separators) and convert only items
    items_md = _strip_front_matter(md_text)
    body_html = _convert_items_to_html(items_md)

    # Compute avg score
    scores = [t["score"] for t in toc_items]
    avg = sum(scores) / len(scores) if scores else 0

    # Determine date display
    title = meta["title"]
    date_display = title.replace("Horizon Daily - ", "").replace("Horizon 每日速递 - ", "")

    # Build TOC
    toc_html = _format_toc_html(toc_items)

    # Compute subtitle without the extracted stats line
    subtitle = meta.get("subtitle", "")

    from datetime import datetime

    return HTML_TEMPLATE.format(
        lang=lang,
        title=title,
        date_display=date_display,
        subtitle=subtitle,
        item_count=meta["item_count"],
        total_items=meta["total_items"],
        avg_score=f"{avg:.1f}",
        toc_items=toc_html,
        body=body_html,
        gen_time=datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
    )


INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Horizon Daily — Summaries</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --bg-primary: #0b0b12; --bg-card: #181825; --text-primary: #e8e8ed;
  --text-secondary: #a0a0b8; --text-muted: #6b6b80; --border: #252540;
  --accent: #b0a8a0; --gold: #f0b90b;
  --font-sans: "Inter", "SF Pro Display", "Segoe UI", system-ui, sans-serif;
}}
body {{ font-family: var(--font-sans); background: var(--bg-primary); color: var(--text-primary); min-height: 100vh; }}
.wrapper {{ max-width: 720px; margin: 0 auto; padding: 60px 24px; }}
h1 {{ font-size: 2rem; font-weight: 800; letter-spacing: -.025em; margin-bottom: 8px;
  background: linear-gradient(135deg, var(--text-primary) 20%, var(--accent) 80%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
.subtitle {{ color: var(--text-secondary); margin-bottom: 40px; }}
.day-group {{ margin-bottom: 36px; }}
.day-title {{ font-size: 1.1rem; font-weight: 700; color: var(--accent); margin-bottom: 12px; }}
.link-card {{
  display: flex; align-items: center; gap: 16px;
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 10px; padding: 14px 20px; margin-bottom: 8px;
  text-decoration: none; color: var(--text-primary);
  transition: border-color .15s, box-shadow .15s;
}}
.link-card:hover {{ border-color: var(--accent); box-shadow: 0 0 20px rgba(108,140,255,.12); }}
.link-card .lang-tag {{
  font-size: .7rem; font-weight: 700; text-transform: uppercase;
  padding: 3px 10px; border-radius: 10px;
  background: #1e1e32; color: var(--accent); border: 1px solid #2a2a50;
}}
.link-card .lang-tag.zh {{ color: #a78bfa; border-color: #3a3060; }}
.link-card .name {{ flex: 1; font-weight: 600; }}
.link-card .arrow {{ color: var(--text-muted); }}
::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: var(--bg-primary); }}
::-webkit-scrollbar-thumb {{ background: #2a2a40; border-radius: 4px; }}
</style>
</head>
<body>
<div class="wrapper">
<h1>Horizon Daily — Summaries</h1>
<p class="subtitle">Beautiful HTML editions of daily tech news digests</p>
{body}
</div>
</body>
</html>"""


def _generate_index(generated_files: list[Path]) -> Path:
    """Generate an index.html linking to all summary pages, grouped by date."""
    from collections import defaultdict
    groups = defaultdict(list)
    for fp in sorted(generated_files):
        stem = fp.stem  # horizon-2026-06-17-en
        parts = stem.split("-")
        date = "-".join(parts[1:4]) if len(parts) >= 4 else "unknown"
        lang = "EN" if stem.endswith("-en") else "ZH" if stem.endswith("-zh") else "??"
        groups[date].append((lang, fp.name))

    day_blocks = []
    for date in sorted(groups.keys(), reverse=True):
        links = []
        for lang, fname in groups[date]:
            cls = "zh" if lang == "ZH" else ""
            links.append(
                '<a class="link-card" href="{0}"><span class="lang-tag {1}">{2}</span><span class="name">{3}</span><span class="arrow">→</span></a>'.format(
                    fname, cls, lang, fname.replace(".html", "")
                )
            )
        day_blocks.append(
            '<div class="day-group"><div class="day-title">{0}</div>{1}</div>'.format(
                date, "\n".join(links)
            )
        )

    index_html = INDEX_TEMPLATE.format(body="\n".join(day_blocks))
    index_path = OUTPUT_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    return index_path


def generate_all() -> list[Path]:
    """Generate HTML for every .md file in data/summaries/."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    generated = []

    for md_path in sorted(SUMMARIES_DIR.glob("*.md")):
        stem = md_path.stem  # e.g. horizon-2026-06-17-en
        lang = "zh" if stem.endswith("-zh") else "en"

        md_text = md_path.read_text(encoding="utf-8")
        html = convert_markdown_to_html(md_text, lang=lang)

        out_path = OUTPUT_DIR / f"{stem}.html"
        out_path.write_text(html, encoding="utf-8")
        generated.append(out_path)
        print(f"  OK {out_path.relative_to(PROJECT_ROOT)}")

    # Generate index
    idx = _generate_index(generated)
    print(f"  OK {idx.relative_to(PROJECT_ROOT)}")

    return generated


def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("Generating HTML from summaries...\n")
    paths = generate_all()
    print(f"\nGenerated {len(paths)} HTML file(s) -> {OUTPUT_DIR.relative_to(PROJECT_ROOT)}/")


if __name__ == "__main__":
    main()
