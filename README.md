# autocodeRHX website + SEO plan

**Preview:** https://harshitvadgama.github.io/autocoderhx-website/
(kept out of Google on purpose until the real domain is live)

## How this repo works

Every push to `main` makes GitHub Actions run `build.py` and publish the result to GitHub Pages
(see the **Actions** tab). You can edit text directly on github.com: open a file, click the pencil, commit,
and the preview updates in about a minute.

| Path | What it is |
|---|---|
| `content_services.py` | Text of the 8 service pages. Edit here. |
| `build.py` | Home pages (EN + DE), layout, structured data, sitemap. |
| `assets/site.js` | Chat assistant + **your WhatsApp number** (top of file). |
| `assets/style.css` | Design. One font family (Barlow), self-hosted in `assets/fonts/` (no Google requests). |
| `.github/workflows/deploy.yml` | Build and deploy on every push. |
| `site/` | Build output, created locally with `python3 build.py` (not committed). |

Open tasks before launch are tracked as **Issues** in this repo.

Pages built:

- `/` English home, `/de/` German home (linked with hreflang)
- 8 service pages, each targeting one search intent:
  VAG online programming, Lamborghini, Bentley, Porsche & Mercedes, CarPlay activation, diagnostic software licenses, wiring diagrams, remote diagnostics
- `sitemap.xml`, `robots.txt`, `404.html`, favicon, share image (for WhatsApp/Facebook previews)
- Structured data on every page (business, services, breadcrumbs, FAQ) so Google understands what you offer and where

## 1. Before going live (must do)

1. **Your WhatsApp number**: open `assets/site.js`, change `WHATSAPP_NUMBER` (digits only, with country code, e.g. `4915112345678`) and `WHATSAPP_DISPLAY`.
2. **Your domain**: buy one (e.g. `autocoderhx.com`). In this repo go to Settings → Secrets and variables → Actions → **Variables** and add `SITE_URL` = `https://www.yourdomain.com` and `CUSTOM_DOMAIN` = `1`. That switches canonical URLs, the sitemap and the CNAME file to your domain and lets Google index the site.
3. To build locally: `python3 build.py` (Python 3 only).
4. **Impressum + Datenschutzerklärung**: a commercial website run from Germany needs both by law. Add them as pages before launch. I'm not a lawyer; use a generator such as e-recht24 or ask a lawyer.
5. Fonts are already self-hosted, so no visitor data goes to Google Fonts.

## 2. Connecting your domain

1. Set the two variables from step 1.2 above and re-run the workflow (Actions → Build and deploy site → Run workflow).
2. Settings → Pages → Custom domain → enter your domain → Save.
3. At your domain registrar add the DNS records GitHub shows (for `www`: a CNAME to `harshitvadgama.github.io`).
4. Once the check passes, tick **Enforce HTTPS**.

## 3. Get indexed (week 1)

1. **Google Search Console**: add the domain, verify via DNS, submit `https://yourdomain/sitemap.xml`.
2. **Bing Webmaster Tools**: import from Search Console. Bing also feeds DuckDuckGo, Yahoo and several AI search tools.
3. **Google Business Profile**: only if you have a real address (workshop). Set it up as a *service-area business* and add your services. This is the biggest boost for "near me" searches.
4. Check Search Console → Pages after 1–2 weeks to see which pages are indexed.

## 4. Ranking in every region: what actually works

No one can guarantee position 1 everywhere. Search results depend on competition, the searcher's country and language, and how much the rest of the web trusts your site. What moves you up, in order of impact:

**a) Languages, not fake city pages.**
Google ranks pages in the searcher's language. Each new language opens a new market. Recommended order:
1. English and German (done)
2. Arabic (Gulf: lots of Lamborghini, Bentley, Porsche)
3. Spanish, French, Italian
4. Hindi

Do not create hundreds of near-identical "Lamborghini programming Dubai / London / Miami…" pages. Google treats them as doorway pages and can drop the whole site.

**b) Backlinks from where your customers are.**
- Be genuinely helpful on brand forums: VWVortex, Audizine, Rennlist, MBWorld, Lamborghini and Bentley owner forums, Reddit (r/Audi, r/Volkswagen, r/Porsche). Answer coding questions, link to your relevant page only when it helps.
- YouTube: short screen recordings of real sessions ("Audi MIB3 CarPlay activation", "SVM coding after cluster swap"). Link the matching service page in the description.
- Partner workshops and parts sellers that link to you as their programming partner.
- Never buy links. It gets sites penalised.

**c) Reviews.**
After each job, send the customer a link to leave a Google review (and Trustpilot). Ask them to mention the car and the job.

**d) One useful article per week.**
Add articles that answer exact searches your customers type, for example:
- "Audi A4 B9 CarPlay activation: which head units work"
- "What SVM code errors mean and how to fix them"
- "Golf 8 retrofit coding after fitting matrix headlights"
- "Why cracked ODIS damages control units"
- Anonymised case studies from real jobs (short to ground on a shared fuse, immobiliser data after a used BCM)

Real cases written by an engineer are the content Google rewards most. Generic AI-written filler is what it penalises.

**e) Measure and repeat.**
Once a month in Search Console: look at queries where you rank 8–20, and improve or expand those pages. That's where the fastest gains are.

## 5. Already done on the technical side

- Fast static pages, no heavy frameworks
- Mobile layout checked at phone width
- Unique title and description per page (under ~60 / ~155 characters)
- One H1 per page, clean URLs (`/services/carplay-activation/`)
- Canonical URLs, hreflang EN/DE, XML sitemap with language alternates
- Schema.org: ProfessionalService, Service, BreadcrumbList, FAQPage
- Open Graph share image for WhatsApp, Facebook and LinkedIn previews
- Internal links between related services and in the footer
