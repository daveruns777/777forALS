# Deploying 777forals.com — GitHub Pages + Porkbun

This guide walks you through putting the website live for **free** using **GitHub Pages**,
then pointing your **Porkbun** domain (`777forals.com`) at it.

You do **not** need to know how to code. Just follow each step in order. Total time: ~30–45 minutes
(plus up to a few hours of waiting for DNS to "propagate" at the end — that part is automatic).

---

## What you'll be doing (the big picture)

1. **Put the website files on GitHub** (a free file host for websites).
2. **Turn on GitHub Pages** so GitHub serves those files as a live website.
3. **Tell Porkbun** (where you bought the domain) to send `777forals.com` visitors to GitHub.
4. **Wait** for it to go live, then confirm `https://777forals.com` works.

Throughout, replace `YOUR-USERNAME` with the GitHub username you create.

---

## Part 1 — Create a free GitHub account

1. Go to **https://github.com/signup**
2. Enter your email, a password, and a username (e.g. `daveruns777`). Write the username down.
3. Verify your email when GitHub sends you the confirmation.

---

## Part 2 — Create the repository (the "folder" for your site)

1. Once logged in, click the **+** in the top-right corner → **New repository**.
2. **Repository name:** `777forals` (any name is fine).
3. Set it to **Public**. (Pages is free for public repos.)
4. Leave everything else unchecked. Click **Create repository**.

You'll land on a page that says *"Quick setup"*. Keep this tab open.

---

## Part 3 — Upload the website files

You have two options. **Option A (drag-and-drop) is easiest** and needs no software.

### Option A — Upload through the website (recommended, no install)

1. Download the whole `777forals_website` folder to your computer (use the **Files** icon
   at the top right of this chat to download everything, then unzip it if needed).
2. On your new repo page, click the link **"uploading an existing file"**
   (or go to **Add file → Upload files**).
3. Open the downloaded `777forals_website` folder on your computer, select **ALL** the files
   inside it (the `.html` files, the `assets` / `images` folders, `style.css`, `main.js`,
   `CNAME`, etc.), and **drag them into the browser** upload box.
   - Important: upload the **contents** of the folder, not the folder itself. The file
     `index.html` must end up at the top level of the repo.
4. Scroll down and click **Commit changes**.

> You do **not** need to upload `build.py` or `pages.py` — those are only used to regenerate
> the site. Uploading them does no harm, but the live site only needs the `.html`, `.css`,
> `.js`, image files, and `CNAME`.

### Option B — Use Git (only if you're comfortable with a terminal)

```bash
cd 777forals_website
git remote add origin https://github.com/YOUR-USERNAME/777forals.git
git branch -M main
git push -u origin main
```

---

## Part 4 — Turn on GitHub Pages

1. In your repo, click **Settings** (top menu).
2. In the left sidebar, click **Pages**.
3. Under **"Build and deployment" → Source**, choose **Deploy from a branch**.
4. Under **Branch**, pick **main** (or **master**) and the folder **/ (root)**. Click **Save**.
5. Wait 1–2 minutes, then refresh. You'll see a message like:
   *"Your site is live at https://YOUR-USERNAME.github.io/777forals/"*.

Click that link to confirm the site loads. 🎉 (The custom domain comes next.)

---

## Part 5 — Add your custom domain in GitHub

1. Still on **Settings → Pages**, find the **"Custom domain"** box.
2. Type **`777forals.com`** and click **Save**.
   - This creates/uses the `CNAME` file in your repo (it's already included for you).
3. Leave **"Enforce HTTPS"** unchecked for now — you'll check it later, after DNS is working.

---

## Part 6 — Point Porkbun at GitHub (the DNS step)

This is where you tell your domain to load the GitHub site.

1. Log in at **https://porkbun.com** → **Account → Domain Management**.
2. Find `777forals.com` and click the **Details / DNS** button (looks like a small "DNS" or
   gear icon) to open **"Edit DNS Records"**.
3. **Delete** any existing `A` records or parking/redirect records for the bare domain (the
   "`A`" type rows pointing at Porkbun's parking page). Leave `NS` and `SOA` records alone.
4. **Add these four A records** (for the bare domain `777forals.com`).
   For each one: Type = **A**, Host = leave **blank** (or `@`), Answer/Value = the IP below,
   TTL = `600`:

   | Type | Host | Answer / Value     |
   |------|------|--------------------|
   | A    | (blank) | `185.199.108.153` |
   | A    | (blank) | `185.199.109.153` |
   | A    | (blank) | `185.199.110.153` |
   | A    | (blank) | `185.199.111.153` |

5. **Add one CNAME record** so `www.777forals.com` also works:

   | Type  | Host  | Answer / Value             |
   |-------|-------|----------------------------|
   | CNAME | `www` | `YOUR-USERNAME.github.io`  |

   (Type the trailing nothing — just `YOUR-USERNAME.github.io`. No `https://`, no slash.)

6. Click **Save** / **Add** for each record.

> **Why four IP addresses?** Those are GitHub Pages' official servers. Using all four gives
> your site redundancy. They are the same for every GitHub Pages site.

---

## Part 7 — Wait, then verify

1. DNS changes can take anywhere from **10 minutes to a few hours** (occasionally up to 24h).
2. After a while, visit **https://777forals.com** — it should show your site.
3. Go back to **GitHub → Settings → Pages**. Once GitHub confirms the domain (green check),
   tick **"Enforce HTTPS"** so visitors always get the secure `https://` version.

That's it — the site is live on your own domain. 🏁

---

## Updating the site later

Whenever you want to change the site:

- **Easiest:** edit the file on GitHub (open the file → pencil icon → edit → Commit), or
  re-upload changed files via **Add file → Upload files**.
- **If you (or I) regenerate the site** from `build.py`, just re-upload the new `.html`/`.css`/
  `.js`/image files. GitHub Pages redeploys automatically within a minute or two.

> Keep the `CNAME` file in the repo — if it's deleted, the custom domain disconnects.

---

## Quick troubleshooting

| Problem | Fix |
|---|---|
| Site shows GitHub 404 | Make sure `index.html` is at the **root** of the repo, not inside a sub-folder. |
| "Domain's DNS record could not be retrieved" in GitHub | DNS hasn't propagated yet — wait and click **Check again**. |
| `https://` warning / not secure | Wait for DNS to finish, then enable **Enforce HTTPS** in Settings → Pages. |
| `www.` version doesn't work | Confirm the `CNAME` record `www → YOUR-USERNAME.github.io` is saved in Porkbun. |
| Changes not showing | Hard-refresh your browser (Ctrl/Cmd + Shift + R); GitHub may take 1–2 min to redeploy. |
