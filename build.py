# -*- coding: utf-8 -*-
"""Static site generator for 777 for ALS. Produces clean HTML files."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------- Links ----------------
DONATE_WMC = "https://daves-wmc.cheddarup.com"
DONATE_BBF = "https://givestar.io/gs/run-the-world-for-als"
EMAIL = "dave@777forALS.com"
BBF_SITE = "https://www.brigancebrigade.org/"
BOOK = "https://www.amazon.com/Strength-Champion-Finding-Fortitude-Adversity/dp/0451467620/"

SOC = {
  "dave": [
    ("instagram", "https://www.instagram.com/davedreamsbig"),
    ("tiktok", "https://www.tiktok.com/@davedreamsbig"),
    ("linkedin", "https://www.linkedin.com/in/davelang/"),
    ("facebook", "https://www.facebook.com/dmlang"),
    ("strava", "https://www.strava.com/athletes/34106378"),
  ],
  "bbf": [
    ("instagram", "https://www.instagram.com/brigancebrigade/"),
    ("facebook", "https://www.facebook.com/BriganceBrigade"),
    ("youtube", "https://www.youtube.com/@BriganceBrigade"),
    ("linkedin", "https://www.linkedin.com/company/brigance-brigade-foundation/"),
    ("x", "https://x.com/BriganceBrigade"),
  ],
  "wmc": [
    ("instagram", "https://www.instagram.com/worldmarathonchallenge777/"),
    ("facebook", "https://www.facebook.com/theworldmarathonchallenge"),
    ("youtube", "https://www.youtube.com/@runbuk"),
  ],
}

# ---------------- SVG icons ----------------
ICON = {
"instagram":'<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.8.07 1.2.05 1.8.25 2.2.42.6.22 1 .48 1.4.9.42.4.7.8.9 1.4.2.4.4 1 .42 2.2.07 1.2.07 1.6.07 4.8s0 3.6-.07 4.8c-.05 1.2-.25 1.8-.42 2.2-.22.6-.48 1-.9 1.4-.4.42-.8.7-1.4.9-.4.2-1 .4-2.2.42-1.2.07-1.6.07-4.8.07s-3.6 0-4.8-.07c-1.2-.05-1.8-.25-2.2-.42-.6-.22-1-.48-1.4-.9-.42-.4-.7-.8-.9-1.4-.2-.4-.4-1-.42-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.07-4.8c.05-1.2.25-1.8.42-2.2.22-.6.48-1 .9-1.4.4-.42.8-.7 1.4-.9.4-.2 1-.4 2.2-.42C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.1 0-3.5 0-4.7.07-1.1.05-1.7.24-2.1.4-.5.2-.9.43-1.3.83-.4.4-.63.8-.83 1.3-.16.4-.35 1-.4 2.1C2.6 8.5 2.6 8.9 2.6 12s0 3.5.07 4.7c.05 1.1.24 1.7.4 2.1.2.5.43.9.83 1.3.4.4.8.63 1.3.83.4.16 1 .35 2.1.4 1.2.07 1.6.07 4.7.07s3.5 0 4.7-.07c1.1-.05 1.7-.24 2.1-.4.5-.2.9-.43 1.3-.83.4-.4.63-.8.83-1.3.16-.4.35-1 .4-2.1.07-1.2.07-1.6.07-4.7s0-3.5-.07-4.7c-.05-1.1-.24-1.7-.4-2.1-.2-.5-.43-.9-.83-1.3-.4-.4-.8-.63-1.3-.83-.4-.16-1-.35-2.1-.4C15.5 4 15.1 4 12 4zm0 3.06A4.94 4.94 0 1 0 12 17a4.94 4.94 0 0 0 0-9.88zm0 8.15A3.2 3.2 0 1 1 12 8.8a3.2 3.2 0 0 1 0 6.4zm6.3-8.35a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0z"/></svg>',
"facebook":'<svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.5 1.49-3.9 3.78-3.9 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12z"/></svg>',
"linkedin":'<svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.8 0 0 .78 0 1.74v20.52C0 23.22.8 24 1.77 24h20.45c.98 0 1.78-.78 1.78-1.74V1.74C24 .78 23.2 0 22.22 0z"/></svg>',
"youtube":'<svg viewBox="0 0 24 24"><path d="M23.5 6.2a3 3 0 0 0-2.12-2.12C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.53A3 3 0 0 0 .5 6.2 31.3 31.3 0 0 0 0 12a31.3 31.3 0 0 0 .5 5.8 3 3 0 0 0 2.12 2.12c1.88.53 9.38.53 9.38.53s7.5 0 9.38-.53a3 3 0 0 0 2.12-2.12A31.3 31.3 0 0 0 24 12a31.3 31.3 0 0 0-.5-5.8zM9.55 15.57V8.43L15.82 12l-6.27 3.57z"/></svg>',
"x":'<svg viewBox="0 0 24 24"><path d="M18.24 2.25h3.31l-7.23 8.26 8.5 11.24h-6.66l-5.22-6.82-5.97 6.82H1.66l7.73-8.84L1.25 2.25h6.83l4.71 6.23 5.45-6.23zm-1.16 17.52h1.83L7.01 4.12H5.04l12.04 15.65z"/></svg>',
"tiktok":'<svg viewBox="0 0 24 24"><path d="M16.6 5.82a4.28 4.28 0 0 1-1.1-2.82h-3.1v12.6a2.6 2.6 0 1 1-2.6-2.6c.27 0 .53.04.78.12V9.9a5.7 5.7 0 0 0-.78-.06 5.7 5.7 0 1 0 5.7 5.7V9.01a7.34 7.34 0 0 0 4.3 1.38V7.28a4.28 4.28 0 0 1-3.2-1.46z"/></svg>',
"strava":'<svg viewBox="0 0 24 24"><path d="M15.39 17.06 13.5 13.3h-2.77l2.66 5.3 2.66-5.3h-2.77zM10.27 2 4.5 13.3h3.4l2.37-4.76 2.37 4.76h3.39L10.27 2z"/></svg>',
}

def icon(name):
    return ICON.get(name, "")

def social_block(label, key):
    links = "".join(
        '<a href="%s" target="_blank" rel="noopener" aria-label="%s %s">%s</a>'
        % (url, label, n, icon(n)) for n, url in SOC[key]
    )
    return ('<div class="social-group"><div class="sg-label">%s</div>'
            '<div class="social-row">%s</div></div>' % (label, links))

# ---------------- Header ----------------
NAVITEMS = [("index.html","Home"),("mission.html","Mission"),("motivation.html","The Story"),
            ("about.html","About"),("sponsors.html","Sponsors")]

def header(active):
    items = ""
    for href, label in NAVITEMS:
        cls = ' class="active"' if href == active else ""
        items += '<a href="%s"%s>%s</a>' % (href, cls, label)
    return '''<header class="site-header">
  <div class="wrap nav">
    <a href="index.html" class="brand">
      <img src="assets/images/logo-shield.jpg" alt="Run the World for ALS logo">
      <span class="brand-text"><b>Run the World</b><span>For ALS</span></span>
    </a>
    <nav class="nav-links" id="navLinks">
      %s
      <a href="donate.html" class="btn btn--primary nav-cta">Donate</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>''' % items

# ---------------- Footer ----------------
def sponsor_logo(img, alt, url, text=False):
    inner = ('<span class="text-logo">%s</span>' % alt) if text else ('<img src="assets/images/%s" alt="%s">' % (img, alt))
    tgt = '' if url == '#' else ' target="_blank" rel="noopener"'
    return '<a class="sponsor-logo" href="%s"%s title="%s">%s</a>' % (url, tgt, alt, inner)

def footer():
    fs = "".join(sponsor_logo(*s) for s in [
        ("yinzcam.png", "YinzCam", "https://www.yinzcam.com/", False),
        ("ravens.png", "Baltimore Ravens", "https://www.baltimoreravens.com", False),
        ("image-engineering.png", "Image Engineering", "https://www.imageengineering.com/", False),
        ("architectural-window.png", "Architectural Window", "https://www.architecturalwindow.com/", False),
        ("balti-virtual.png", "Balti Virtual", "https://www.baltivirtual.com/", False),
        ("momento.png", "Momento", "https://www.mymomento.com/", False),
        ("medstar.png", "MedStar Health", "https://www.medstarhealth.org/", False),
        ("freedom-digital.png", "Freedom Digital Media", "https://www.freedomdigital.net/", False),
    ])
    return '''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="assets/images/logo-shield.jpg" alt="Run the World for ALS">
        <p>7 Marathons. 7 Continents. 7 Days.<br>Dave Lang's World Marathon Challenge to benefit people living with ALS through the Brigance Brigade Foundation.</p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <a href="index.html">Home</a>
        <a href="mission.html">Mission</a>
        <a href="story.html">The Story</a>
        <a href="about.html">About</a>
        <a href="sponsors.html">Sponsors</a>
        <a href="donate.html">Donate</a>
      </div>
      <div class="footer-col">
        <h4>Connect</h4>
        %s
        %s
        %s
      </div>
      <div class="footer-col">
        <h4>Get In Touch</h4>
        <a href="mailto:%s">%s</a>
        <a href="https://instagram.com/davedreamsbig" target="_blank" rel="noopener">@davedreamsbig</a>
      </div>
    </div>

    <div class="footer-sponsors">
      <h4>Big Dreams Powered By</h4>
      <div class="footer-sponsors__row">%s</div>
    </div>

    <div class="footer-bottom">
      <p>&copy; <span id="year">2026</span> Run the World for ALS &middot; Built with heart to support the <a href="%s" target="_blank" rel="noopener">Brigance Brigade Foundation</a>.</p>
    </div>
  </div>
</footer>''' % (social_block("Dave Lang","dave"), social_block("Brigance Brigade","bbf"),
                social_block("World Marathon Challenge","wmc"), EMAIL, EMAIL, fs, BBF_SITE)

# ---------------- Page wrapper ----------------
def page(filename, title, desc, body, active):
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/images/logo-shield.jpg">
<link rel="icon" type="image/x-icon" href="assets/images/favicon.ico">
<link rel="apple-touch-icon" href="assets/images/logo-shield.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;600;700;800;900&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
%s
<main>
%s
</main>
%s
<a class="float-donate" href="donate.html" aria-label="Donate">
<svg viewBox="0 0 24 24"><path d="M12 21s-6.7-4.35-9.3-8.06C.9 10.2 1.5 6.7 4.2 5.3c2-1.05 4.2-.35 5.4 1.2L12 9l2.4-2.5c1.2-1.55 3.4-2.25 5.4-1.2 2.7 1.4 3.3 4.9 1.5 7.64C18.7 16.65 12 21 12 21z"/></svg>
</a>
<script src="assets/js/main.js"></script>
</body>
</html>''' % (title, desc, title, desc, header(active), body, footer())
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html), "bytes")

# ---------------- import page bodies ----------------
import pages
pages.build(page)
