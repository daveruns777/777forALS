# Run the World for ALS — Website

A modern, sleek, multi-page static website for **777forALS.com** — Dave Lang's World Marathon
Challenge (7 marathons, 7 continents, 7 days) benefiting the Brigance Brigade Foundation.

Rebuilt from the original Google Sites content with a dark, cinematic design inspired by
alexruns777.com and a tiered sponsor layout inspired by katiespotz.com.

## Pages
| File | Page |
|------|------|
| `index.html` | Home — hero, custom countdown clock, intro, videos, sponsor strip |
| `mission.html` | Mission — World Marathon Challenge + 7-leg continent itinerary |
| `motivation.html` | Motivation — O.J. Brigance story + 6 motivational videos |
| `about.html` | About — Dave Lang's story & photos |
| `sponsors.html` | Corporate Sponsors — tiered logos + sponsorship packages |
| `donate.html` | Donate — two giving options + meaningful gift amounts |

## Folder structure
```
777forals_website/
├── index.html, mission.html, motivation.html, about.html, sponsors.html, donate.html
├── assets/
│   ├── css/style.css        # full design system
│   ├── js/main.js           # nav, scroll reveal, custom countdown
│   └── images/              # all photos, logos, favicon
├── build.py                 # page generator (regenerates the HTML)
├── pages.py                 # page body content/copy
└── README.md
```

## Custom countdown clock
The countdown is a **custom-built widget** (not an external embed), so its look is fully editable.
- Markup lives in the home hero section; logic is in `assets/js/main.js`.
- Change the target date via the `data-target` attribute on the countdown element
  (currently `2027-01-30T00:00:00` — the first marathon in Antarctica).
- Restyle it freely in `assets/css/style.css` (`.countdown` rules).

## Editing content
The HTML files are generated from `pages.py` + `build.py`. To change text/images:
1. Edit `pages.py` (content) and/or `build.py` (header/footer/structure).
2. Run `python3 build.py` to regenerate all `.html` files.

You can also edit the `.html` files directly if you prefer — just note they'll be overwritten
the next time `build.py` runs.

## Preview locally
```bash
cd 777forals_website
python3 -m http.server 3000
# then open http://localhost:3000 in your browser
```

## Deploying to Porkbun via FTP
1. Log in to **porkbun.com → Account → Domain Management** and open your hosting / FTP details
   (host, username, password, port — usually 21 for FTP or 22 for SFTP).
2. Connect with an FTP client such as **FileZilla**:
   - Host: your Porkbun FTP host (e.g. `ftp.yourdomain.com`)
   - Username / Password: from Porkbun
   - Port: 21 (FTP) or 22 (SFTP)
3. On the server, open the web root folder (often `public_html`, `htdocs`, or `www`).
4. Upload **the entire contents** of this `777forals_website` folder into the web root —
   that means `index.html`, the other `.html` files, and the whole `assets/` folder.
   (Upload the files *inside* this folder, not the folder itself.)
5. Visit your domain — `index.html` loads automatically as the home page.

> You do **not** need to upload `build.py`, `pages.py`, or `README.md` to the live server —
> they are build/source files only. Uploading just the `.html` files and the `assets/` folder is enough.

## Notes
- 100% static HTML/CSS/JS — no backend, database, or build tooling required to run.
- A few original sponsor logos (Image Engineering, Architectural Window, YinzCam, Balti Virtual,
  MedStar Health, Freedom Digital Media) and the home hero "all things are possible" portrait were
  not retrievable from the original Google Sites export. The sponsors are shown as clean styled text
  logos for now — drop the real logo image files into `assets/images/` and update the references in
  `pages.py`/`build.py` (then re-run `build.py`) for full-fidelity logos.
