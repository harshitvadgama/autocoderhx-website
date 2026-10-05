#!/usr/bin/env python3
"""Builds the autocodeRHX static site into ./site
Edit SITE_URL once you own the domain, then run:  python3 build.py
"""
import json, os, shutil, datetime, html
from content_services import SERVICES

# Preview on GitHub Pages. When you own the domain, set SITE_URL to it (e.g. "https://www.autocoderhx.com")
# and set CUSTOM_DOMAIN = True. No trailing slash.
SITE_URL = os.environ.get("SITE_URL", "https://harshitvadgama.github.io/autocoderhx-website")
CUSTOM_DOMAIN = os.environ.get("CUSTOM_DOMAIN", "0") == "1"
BASE_PATH = "/" + SITE_URL.split("//", 1)[1].partition("/")[2]
BASE_PATH = BASE_PATH.rstrip("/") + "/"   # "/" on a custom domain, "/autocoderhx-website/" on github.io
BRAND = "autocodeRHX"
TODAY = datetime.date.today().isoformat()
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
SRC_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
SVC = {s["slug"]: s for s in SERVICES}

AREAS = ["Europe", "United Kingdom", "Ireland", "Middle East", "North America", "India", "Asia-Pacific", "Australia", "New Zealand", "South Africa"]

def esc(s): return html.escape(s, quote=True)

# The github.io preview is kept out of Google so it never competes with the real domain.
ROBOTS = "index, follow, max-image-preview:large" if CUSTOM_DOMAIN else "noindex, nofollow"

# ---------------------------------------------------------------- shared parts
CHAT_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8.5 8.5 0 0 1-12.6 7.4L3 21l1.6-5.2A8.5 8.5 0 1 1 21 12Z"/></svg>'

UI = {
 "en": {"services": "Services", "how": "How it works", "regions": "Worldwide", "faq": "FAQ", "quote": "Get a quote",
        "contact": "Contact me", "home": "Home", "assistant": "autocodeRHX assistant", "replies": "● replies on WhatsApp",
        "type": "Type a message…", "send": "Send", "restart": "Start over", "close": "Close chat",
        "foot1": "Remote coding, programming &amp; diagnostics", "foot2": "Brand names are used only to describe compatibility. autocodeRHX is not affiliated with any manufacturer.",
        "allsvc": "All services"},
 "de": {"services": "Leistungen", "how": "Ablauf", "regions": "Weltweit", "faq": "FAQ", "quote": "Angebot anfragen",
        "contact": "Kontakt", "home": "Start", "assistant": "autocodeRHX-Assistent", "replies": "● antwortet per WhatsApp",
        "type": "Nachricht schreiben…", "send": "Senden", "restart": "Neu starten", "close": "Chat schließen",
        "foot1": "Codierung, Programmierung &amp; Diagnose aus der Ferne", "foot2": "Markennamen dienen nur zur Beschreibung der Kompatibilität. autocodeRHX steht in keiner Verbindung zu den Herstellern.",
        "allsvc": "Alle Leistungen"},
}

def head(lang, title, desc, path, depth, jsonld, alternates=None, og_type="website"):
    r = "../" * depth
    url = SITE_URL + path
    alt = ""
    if alternates:
        for hl, p in alternates:
            alt += f'<link rel="alternate" hreflang="{hl}" href="{SITE_URL}{p}">\n'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>\n' for j in jsonld)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{ROBOTS}">
<link rel="canonical" href="{url}">
{alt}<meta name="theme-color" content="#0A1820">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{'de_DE' if lang=='de' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="preload" href="{r}assets/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/style.css">
{ld}</head>
<body>
<div class="grid-bg" aria-hidden="true"></div>
"""

def nav(lang, depth, switch_href=None, switch_label=None, home_anchor_prefix=None):
    u = UI[lang]; r = "../" * depth
    home = r + ("de/" if lang == "de" else "")
    pre = home_anchor_prefix if home_anchor_prefix is not None else home
    sw = f'<a class="lang" href="{switch_href}" hreflang="{"en" if lang=="de" else "de"}">{switch_label}</a>' if switch_href else ""
    return f"""<header class="nav">
  <div class="wrap">
    <a class="logo" href="{home or './'}" aria-label="{BRAND} home">autocode<b>RHX</b></a>
    <nav aria-label="Main">
      <ul>
        <li><a href="{pre}#services">{u['services']}</a></li>
        <li><a href="{pre}#process">{u['how']}</a></li>
        <li><a href="{pre}#worldwide">{u['regions']}</a></li>
        <li><a href="{pre}#faq">{u['faq']}</a></li>
      </ul>
    </nav>
    <div class="nav-right">{sw}
      <button class="btn btn-amber" type="button" data-open-chat>{CHAT_ICON}{u['quote']}</button>
    </div>
  </div>
</header>
"""

def footer(lang, depth):
    u = UI[lang]; r = "../" * depth
    links = " · ".join(f'<a href="{r}services/{s["slug"]}/">{s["nav"]}</a>' for s in SERVICES)
    return f"""<footer>
  <div class="wrap" style="flex-direction:column;gap:1.2rem">
    <nav aria-label="Services" style="font-size:.84rem;line-height:1.9">{links}</nav>
    <div style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:1rem">
      <span><b style="color:var(--text);font-family:var(--f-display);font-stretch:125%">autocode<span style="color:var(--amber)">RHX</span></b> · {u['foot1']}</span>
      <span>{u['foot2']}</span>
    </div>
  </div>
</footer>
"""

def chat(lang, depth):
    u = UI[lang]; r = "../" * depth
    return f"""<button class="chat-fab" id="chatFab" type="button" aria-label="{u['contact']}">
  <span class="ping" aria-hidden="true"></span>{CHAT_ICON}{u['contact']}
</button>
<div class="chat" id="chat" role="dialog" aria-label="{u['assistant']}" hidden>
  <div class="chat-head">
    <div class="avatar" aria-hidden="true">RHX</div>
    <div class="who"><strong>{u['assistant']}</strong><small>{u['replies']}</small></div>
    <button class="icon-btn" id="chatReset" type="button" aria-label="{u['restart']}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg></button>
    <button class="icon-btn" id="chatClose" type="button" aria-label="{u['close']}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
  </div>
  <div class="chat-log" id="chatLog" aria-live="polite"></div>
  <form class="chat-input" id="chatForm" autocomplete="off">
    <input id="chatText" type="text" placeholder="{u['type']}" aria-label="{u['type']}">
    <button type="submit" aria-label="{u['send']}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
  </form>
</div>
<script src="{r}assets/site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- structured data
ORG = {
  "@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE_URL + "/#org",
  "name": BRAND, "url": SITE_URL + "/", "logo": SITE_URL + "/assets/apple-touch-icon.png",
  "image": SITE_URL + "/assets/og-image.png",
  "description": "Remote online programming, coding and diagnostics for Volkswagen Group, Porsche, Lamborghini, Bentley and Mercedes-Benz vehicles.",
  "areaServed": [{"@type": "Place", "name": a} for a in AREAS],
  "knowsLanguage": ["en", "de", "hi"],
  "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["nav"], "url": f"{SITE_URL}/services/{s['slug']}/"}} for s in SERVICES]},
}
def faq_ld(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}

# ---------------------------------------------------------------- home page content
HOME = {
 "en": {
  "path": "/", "title": "VAG, Lamborghini & Bentley Online Programming | autocodeRHX",
  "desc": "Remote online programming for VAG, Porsche, Lamborghini, Bentley and Mercedes. CarPlay activation, wiring diagrams and genuine diagnostic software.",
  "status": "Remote sessions available worldwide",
  "h1": 'Online programming for <em>VAG, Porsche, Lamborghini</em> and Bentley.',
  "lede": "autocodeRHX connects to your car remotely and runs the coding, programming and activations that normally need a dealer. Genuine OEM software, done by an automotive engineer.",
  "cta1": "Start on WhatsApp", "cta2": "See all services",
  "trust": ["Licensed software only", "ODIS · PIWIS · XENTRY · VCDS", "Quote before any work"],
  "brands": "Brands covered",
  "svc_eyebrow": "Services", "svc_h2": "Everything, sorted by job.",
  "svc_p": "Pick a category or browse the full list. Every job starts with a free check that your car and setup support it.",
  "filters": [("all", "All services"), ("online", "Online programming"), ("coding", "Activation &amp; coding"), ("software", "Software &amp; licenses"), ("diag", "Diagnostics &amp; wiring")],
  "ask": "Ask about this →", "more": "Details",
  "cats": [
   ("online", "A · ONLINE", "Online programming", "Jobs that need a live connection to the manufacturer's server: control unit replacement, software updates and online coding.", [
     ("vag-online-programming", "", "VW · AUDI · SEAT · ŠKODA · CUPRA", "", "VAG Online Programming", "SVM online coding after a control unit is replaced, flash updates and parameter sets pulled from the official backend.", ["ODIS", "SVM"]),
     ("lamborghini-online-programming", "exotic", "HURACÁN · URUS · AVENTADOR", "EXOTIC", "Lamborghini Online Programming", "Module replacement, online software updates and coding for Lamborghini, without trailering the car to a dealer.", ["OEM online"]),
     ("bentley-online-programming", "exotic", "CONTINENTAL · BENTAYGA · FLYING SPUR", "LUXURY", "Bentley Online Programming", "Online coding and programming for Bentley control units, including new and used module installation.", ["ODIS", "OEM online"]),
     ("porsche-mercedes-programming", "", "PORSCHE · MERCEDES-BENZ", "", "Porsche &amp; Mercedes Programming", "Coding, programming and adaptations with the factory tools for each brand.", ["PIWIS", "XENTRY"]),
   ]),
   ("coding", "B · CODING", "Activation &amp; coding", "Unlock features your car already has the hardware for, or make a retrofit work like it left the factory with it.", [
     ("carplay-activation", "wide", "MIB2 · MIB3 HEAD UNITS · OTHER BRANDS ON REQUEST", "POPULAR", "CarPlay &amp; Android Auto Activation", "Wired or wireless App-Connect switched on in your existing head unit. No new hardware, no dongle. Send your VIN first and I'll confirm your unit supports it.", ["Apple CarPlay", "Android Auto", "App-Connect"]),
     (None, "", "AFTER YOU FIT THE PART", "", "Retrofit Coding", "Lights, cameras, parking sensors, steering wheels and assistance systems coded and adapted so they work without faults.", ["Coding", "Adaptation"]),
     (None, "", "COMFORT", "", "Feature &amp; Comfort Coding", "The small things factory settings hide: gauge sweep, comfort windows, lighting behaviour, display options and more.", ["VCDS", "ODIS"]),
   ]),
   ("software", "C · SOFTWARE", "Software &amp; licenses", "Genuine, legally licensed diagnostic software for workshops and enthusiasts. No cracked tools, ever.", [
     ("diagnostic-software-licenses", "wide", "OEM &amp; PROFESSIONAL", "LEGAL", "Diagnostic Software Licenses", "I help you choose the right official subscription or license for your brands and budget, then get it running on your laptop and interface.", ["ODIS", "PIWIS", "XENTRY", "VCDS"]),
     ("diagnostic-software-licenses", "", "REMOTE", "", "Installation &amp; Setup", "Software install, interface drivers and configuration done over a remote connection to your laptop.", ["Windows", "J2534"]),
     ("diagnostic-software-licenses", "", "YOU HAVE THE SUBSCRIPTION", "", "Help With Your Own Tools", "You have the OEM or aftermarket access, but the job keeps failing. I connect and run it with you, step by step.", ["Remote support"]),
   ]),
   ("diag", "D · DIAGNOSTICS", "Diagnostics &amp; wiring", "For faults that a code reader can't explain: no-starts, electrical shorts, network errors and immobiliser issues.", [
     ("remote-diagnostics", "wide", "ALL COVERED BRANDS", "", "Remote Diagnostics", "Full scan of every control unit, fault codes explained in plain language, and a clear plan for what to check next and what to replace.", ["Full scan", "Guided fault finding"]),
     ("wiring-diagrams", "", "STROMLAUFPLÄNE", "", "Wiring Diagrams", "Current flow diagrams for your exact model, with connector pinouts, wire colours and fuse locations.", ["Per VIN", "PDF"]),
     ("remote-diagnostics", "", "MULTIMETER IN HAND", "", "Wiring Analysis", "Guided measurements to find the fault: voltage drop, shorts to ground, open circuits and CAN bus checks.", ["Component testing"]),
   ]),
  ],
  "proc_eyebrow": "How it works", "proc_h2": "From message to finished job.", "proc_p": "Most jobs are done in one remote session while you sit next to the car.",
  "steps": [("Message on WhatsApp", "Tell me the car, the job and your VIN. The chat assistant on this page prepares the message for you."),
            ("Check &amp; quote", "I confirm the job is possible on your car and send a fixed price plus the equipment you need."),
            ("Remote session", "You connect the interface and laptop. I take over remotely and run the job with you watching."),
            ("Verified &amp; done", "Fault memory checked and cleared, function tested, and a short report of what was changed.")],
  "reg_eyebrow": "Worldwide", "reg_h2": "Remote coding, wherever your car is.",
  "reg_p": "Sessions are booked in your local time. The car stays with you; only the data travels.",
  "regions": [("CET / CEST", "Europe", "Germany, Austria, Switzerland, Netherlands, Belgium, France, Italy, Spain, Poland and Scandinavia."),
              ("GMT / BST", "UK &amp; Ireland", "Online programming and coding for UK and Irish cars, including right-hand-drive market software."),
              ("GST / AST", "Middle East", "UAE, Saudi Arabia, Qatar, Kuwait, Oman and Bahrain. GCC-market Lamborghini, Bentley and Porsche welcome."),
              ("ET / CT / PT", "North America", "USA and Canada. European evenings line up with US mornings and afternoons."),
              ("IST / SGT", "India &amp; Asia-Pacific", "India, Singapore, Malaysia, Hong Kong and more. Sessions in English or Hindi."),
              ("AEST / SAST", "Australia, NZ &amp; Africa", "Australia, New Zealand and South Africa, with early-morning European slots.")],
  "reg_note": "Cars built for the EU, UK, North America, the Gulf and Asia run different software versions. Send your VIN and I'll check what applies to yours.",
  "prep_eyebrow": "Before your session", "prep_h2": "A stable setup is half the job.",
  "prep_p": "Online programming writes software into control units. A dropped connection or a sagging battery mid-flash can leave a module unresponsive, so every session starts with this checklist.",
  "prep_note": "Don't have an interface or charger? Ask in the chat. I'll tell you what to buy or borrow for your car.",
  "spec": [("Battery charger / power supply", "13.0 – 14.0 V stable", True), ("Diagnostic interface", "VAS 6154 / J2534", False), ("Laptop", "Windows 10/11", False), ("Internet", "Cable or strong Wi-Fi", False), ("Remote access tool", "I send the link", False), ("Ignition", "On, engine off", False), ("VIN", "17 characters", False)],
  "pillars": [("Genuine software only", "Every tool and license is official. That protects your car, your warranty and your money."),
              ("Engineer, not a reseller", "Automotive engineering background and hands-on dealer diagnostics. I understand why a job fails, not just which button to press."),
              ("Clear price up front", "You get a quote before anything starts. If a job turns out not to be possible on your car, you don't pay for it.")],
  "faq_h2": "Common questions",
  "faq": [("Is the software really legal?", "Yes. autocodeRHX only works with officially licensed OEM and professional software. Cracked tools are unreliable and can damage control units, so they are never used or sold here."),
          ("Where do you work? Do I need to bring the car?", "Most jobs are fully remote, so the car stays with you. You need a laptop, an interface and an internet connection near the car. Sessions run worldwide."),
          ("Can you program cars from the US, UK or Middle East?", "Yes, in most cases. Software differs by market, so I check your VIN before quoting."),
          ("How do I know CarPlay will work on my car?", "Send your VIN first. I check the head unit hardware and software version and confirm before you pay anything."),
          ("What if something goes wrong during programming?", "That's why the checklist above exists. A stable voltage and connection are checked before the first write. If a step fails, I recover the module in the same session."),
          ("Which languages do you speak?", "English, German and Hindi."),
          ("How much does it cost?", "Prices depend on the car and the job. Send a message with your car and VIN for a fixed quote, usually the same day.")],
  "final_h2": "Ready when your car is.", "final_p": "Tell the assistant what you need. It writes the WhatsApp message for you, so you get a quote faster.", "final_cta": "Chat now",
 },
}

# German home: same structure, natural German
HOME["de"] = dict(HOME["en"])
HOME["de"].update({
  "path": "/de/", "title": "Online-Programmierung & Codierung per Fernzugriff | autocodeRHX",
  "desc": "Online-Programmierung per Fernzugriff für VW, Audi, Porsche, Lamborghini, Bentley und Mercedes. CarPlay-Freischaltung, Stromlaufpläne, Original-Software.",
  "status": "Fernsitzungen weltweit verfügbar",
  "h1": 'Online-Programmierung für <em>VAG, Porsche, Lamborghini</em> und Bentley.',
  "lede": "autocodeRHX verbindet sich per Fernzugriff mit deinem Auto und erledigt Codierungen, Programmierungen und Freischaltungen, für die man sonst zum Händler muss. Mit Original-Software, durchgeführt von einem Fahrzeugtechnik-Ingenieur.",
  "cta1": "Per WhatsApp starten", "cta2": "Alle Leistungen",
  "trust": ["Nur lizenzierte Software", "ODIS · PIWIS · XENTRY · VCDS", "Festpreis vor Arbeitsbeginn"],
  "brands": "Marken",
  "svc_eyebrow": "Leistungen", "svc_h2": "Alles nach Aufgabe sortiert.",
  "svc_p": "Wähl eine Kategorie oder schau dir alles an. Vor jedem Auftrag prüfe ich kostenlos, ob dein Auto und dein Setup passen.",
  "filters": [("all", "Alle Leistungen"), ("online", "Online-Programmierung"), ("coding", "Freischaltung &amp; Codierung"), ("software", "Software &amp; Lizenzen"), ("diag", "Diagnose &amp; Elektrik")],
  "ask": "Anfragen →", "more": "Details (EN)",
  "cats": [
   ("online", "A · ONLINE", "Online-Programmierung", "Arbeiten, die eine Live-Verbindung zum Herstellerserver brauchen: Steuergerätetausch, Software-Updates und Online-Codierung.", [
     ("vag-online-programming", "", "VW · AUDI · SEAT · ŠKODA · CUPRA", "", "VAG Online-Programmierung", "SVM-Online-Codierung nach Steuergerätetausch, Flash-Updates und Parametersätze direkt aus dem offiziellen Backend.", ["ODIS", "SVM"]),
     ("lamborghini-online-programming", "exotic", "HURACÁN · URUS · AVENTADOR", "EXOTIC", "Lamborghini Online-Programmierung", "Steuergerätetausch, Online-Software-Updates und Codierung für Lamborghini, ohne das Auto zum Händler zu transportieren.", ["OEM online"]),
     ("bentley-online-programming", "exotic", "CONTINENTAL · BENTAYGA · FLYING SPUR", "LUXURY", "Bentley Online-Programmierung", "Online-Codierung und Programmierung für Bentley-Steuergeräte, auch beim Einbau neuer oder gebrauchter Module.", ["ODIS", "OEM online"]),
     ("porsche-mercedes-programming", "", "PORSCHE · MERCEDES-BENZ", "", "Porsche &amp; Mercedes Programmierung", "Codierung, Programmierung und Anpassungen mit den Werkstattsystemen der jeweiligen Marke.", ["PIWIS", "XENTRY"]),
   ]),
   ("coding", "B · CODIERUNG", "Freischaltung &amp; Codierung", "Funktionen freischalten, für die die Hardware schon da ist, oder Nachrüstungen so codieren, als wären sie ab Werk verbaut.", [
     ("carplay-activation", "wide", "MIB2 · MIB3 · ANDERE MARKEN AUF ANFRAGE", "BELIEBT", "CarPlay &amp; Android Auto Freischaltung", "App-Connect kabelgebunden oder kabellos in deinem vorhandenen Infotainment aktiviert. Keine neue Hardware, kein Dongle. Schick mir zuerst deine FIN, dann prüfe ich die Kompatibilität.", ["Apple CarPlay", "Android Auto", "App-Connect"]),
     (None, "", "NACH DEM EINBAU", "", "Nachrüst-Codierung", "Licht, Kameras, Parksensoren, Lenkräder und Assistenzsysteme codiert und angelernt, damit alles fehlerfrei läuft.", ["Codierung", "Anpassung"]),
     (None, "", "KOMFORT", "", "Komfort-Codierung", "Die kleinen Dinge, die ab Werk versteckt sind: Nadelsweep, Komfortblinken, Lichtfunktionen, Anzeigeoptionen und mehr.", ["VCDS", "ODIS"]),
   ]),
   ("software", "C · SOFTWARE", "Software &amp; Lizenzen", "Original-Diagnosesoftware mit gültiger Lizenz für Werkstätten und Schrauber. Niemals gecrackte Tools.", [
     ("diagnostic-software-licenses", "wide", "OEM &amp; PROFESSIONELL", "LEGAL", "Diagnose-Softwarelizenzen", "Ich helfe dir, die passende offizielle Lizenz für deine Marken und dein Budget zu finden, und richte sie auf deinem Laptop und Interface ein.", ["ODIS", "PIWIS", "XENTRY", "VCDS"]),
     ("diagnostic-software-licenses", "", "PER FERNZUGRIFF", "", "Installation &amp; Einrichtung", "Software-Installation, Interface-Treiber und Konfiguration per Fernzugriff auf deinen Laptop.", ["Windows", "J2534"]),
     ("diagnostic-software-licenses", "", "DU HAST DAS ABO", "", "Hilfe mit deinen eigenen Tools", "Du hast den OEM- oder Aftermarket-Zugang, aber der Job klappt nicht. Ich schalte mich auf und mache es Schritt für Schritt mit dir.", ["Fernsupport"]),
   ]),
   ("diag", "D · DIAGNOSE", "Diagnose &amp; Elektrik", "Für Fehler, die ein Codeleser nicht erklärt: Startprobleme, Kurzschlüsse, Netzwerkfehler und Wegfahrsperre.", [
     ("remote-diagnostics", "wide", "ALLE MARKEN", "", "Ferndiagnose", "Kompletter Scan aller Steuergeräte, Fehlercodes verständlich erklärt und ein klarer Plan, was als Nächstes geprüft oder getauscht wird.", ["Komplettscan", "Geführte Fehlersuche"]),
     ("wiring-diagrams", "", "STROMLAUFPLÄNE", "", "Stromlaufpläne", "Stromlaufpläne für dein genaues Modell mit Steckerbelegung, Leitungsfarben und Sicherungspositionen.", ["Per FIN", "PDF"]),
     ("remote-diagnostics", "", "MULTIMETER IN DER HAND", "", "Leitungsanalyse", "Geführte Messungen zur Fehlersuche: Spannungsabfall, Masseschluss, Unterbrechungen und CAN-Bus-Prüfung.", ["Bauteilprüfung"]),
   ]),
  ],
  "proc_eyebrow": "Ablauf", "proc_h2": "Von der Nachricht zum fertigen Auftrag.", "proc_p": "Die meisten Aufträge sind in einer Fernsitzung erledigt, während du am Auto sitzt.",
  "steps": [("WhatsApp-Nachricht", "Schreib mir Auto, Aufgabe und FIN. Der Chat-Assistent auf dieser Seite bereitet die Nachricht für dich vor."),
            ("Prüfung &amp; Angebot", "Ich prüfe, ob der Auftrag bei deinem Auto möglich ist, und schicke dir einen Festpreis und die nötige Ausrüstung."),
            ("Fernsitzung", "Du schließt Interface und Laptop an. Ich übernehme per Fernzugriff und du schaust zu."),
            ("Geprüft &amp; fertig", "Fehlerspeicher geprüft und gelöscht, Funktion getestet und ein kurzer Bericht über die Änderungen.")],
  "reg_eyebrow": "Weltweit", "reg_h2": "Codierung aus der Ferne, egal wo dein Auto steht.",
  "reg_p": "Termine richten sich nach deiner Ortszeit. Das Auto bleibt bei dir, nur die Daten reisen.",
  "regions": [("MEZ / MESZ", "Europa", "Deutschland, Österreich, Schweiz, Niederlande, Belgien, Frankreich, Italien, Spanien, Polen und Skandinavien."),
              ("GMT / BST", "UK &amp; Irland", "Online-Programmierung und Codierung für britische und irische Fahrzeuge, auch mit Rechtslenker-Software."),
              ("GST / AST", "Naher Osten", "VAE, Saudi-Arabien, Katar, Kuwait, Oman und Bahrain. Lamborghini, Bentley und Porsche mit GCC-Ausführung willkommen."),
              ("ET / CT / PT", "Nordamerika", "USA und Kanada. Europäische Abende passen zu amerikanischen Vor- und Nachmittagen."),
              ("IST / SGT", "Indien &amp; Asien-Pazifik", "Indien, Singapur, Malaysia, Hongkong und mehr. Sitzungen auf Englisch oder Hindi."),
              ("AEST / SAST", "Australien, NZ &amp; Afrika", "Australien, Neuseeland und Südafrika, mit Terminen am frühen europäischen Morgen.")],
  "reg_note": "Fahrzeuge für EU, UK, Nordamerika, Golfstaaten und Asien haben unterschiedliche Softwarestände. Schick mir deine FIN und ich prüfe, was für dein Auto gilt.",
  "prep_eyebrow": "Vor der Sitzung", "prep_h2": "Ein stabiles Setup ist die halbe Miete.",
  "prep_p": "Bei der Online-Programmierung wird Software in Steuergeräte geschrieben. Bricht die Verbindung ab oder sackt die Spannung beim Flashen ein, kann ein Steuergerät hängen bleiben. Deshalb beginnt jede Sitzung mit dieser Checkliste.",
  "prep_note": "Kein Interface oder Ladegerät? Frag im Chat. Ich sage dir, was du für dein Auto brauchst.",
  "spec": [("Batterieladegerät / Netzteil", "13,0 – 14,0 V stabil", True), ("Diagnose-Interface", "VAS 6154 / J2534", False), ("Laptop", "Windows 10/11", False), ("Internet", "Kabel oder starkes WLAN", False), ("Fernzugriff", "Link kommt von mir", False), ("Zündung", "An, Motor aus", False), ("FIN", "17 Zeichen", False)],
  "pillars": [("Nur Original-Software", "Jedes Tool und jede Lizenz ist offiziell. Das schützt dein Auto, deine Garantie und dein Geld."),
              ("Ingenieur, kein Wiederverkäufer", "Studium der Fahrzeugtechnik und Praxis in der Händlerdiagnose. Ich verstehe, warum ein Job scheitert, nicht nur, welchen Knopf man drückt."),
              ("Klarer Preis vorab", "Du bekommst ein Angebot, bevor es losgeht. Geht der Auftrag bei deinem Auto nicht, zahlst du nichts.")],
  "faq_h2": "Häufige Fragen",
  "faq": [("Ist die Software wirklich legal?", "Ja. autocodeRHX arbeitet nur mit offiziell lizenzierter OEM- und Profisoftware. Gecrackte Tools sind unzuverlässig und können Steuergeräte beschädigen, deshalb werden sie hier weder genutzt noch verkauft."),
          ("Muss ich mit dem Auto vorbeikommen?", "Nein. Die meisten Aufträge laufen komplett per Fernzugriff. Du brauchst einen Laptop, ein Interface und Internet am Auto. Weltweit."),
          ("Geht das auch mit Autos aus den USA, UK oder dem Nahen Osten?", "In den meisten Fällen ja. Die Software unterscheidet sich je nach Markt, deshalb prüfe ich vorher deine FIN."),
          ("Woher weiß ich, ob CarPlay bei mir funktioniert?", "Schick zuerst deine FIN. Ich prüfe Hardware und Softwarestand deines Infotainments, bevor du etwas zahlst."),
          ("Was passiert, wenn beim Programmieren etwas schiefgeht?", "Dafür gibt es die Checkliste. Spannung und Verbindung werden vor dem ersten Schreibvorgang geprüft. Schlägt ein Schritt fehl, stelle ich das Steuergerät in derselben Sitzung wieder her."),
          ("Welche Sprachen sprichst du?", "Deutsch, Englisch und Hindi."),
          ("Was kostet das?", "Das hängt vom Auto und vom Auftrag ab. Schick mir Auto und FIN und du bekommst meist noch am selben Tag einen Festpreis.")],
  "final_h2": "Bereit, wenn dein Auto es ist.", "final_p": "Sag dem Assistenten, was du brauchst. Er schreibt die WhatsApp-Nachricht für dich, damit du schneller ein Angebot bekommst.", "final_cta": "Jetzt chatten",
})

def home_page(lang):
    H = HOME[lang]; depth = 1 if lang == "de" else 0; r = "../" * depth
    brands = ["Volkswagen", "Audi", "Lamborghini", "SEAT", "Škoda", "Cupra", "Bentley", "Porsche", "Mercedes-Benz", "McLaren", "Maserati"]
    ex = {"Lamborghini", "Bentley", "McLaren"}
    def brand_span(b, hidden=False):
        cls = ' class="x"' if b in ex else ""
        hid = ' aria-hidden="true"' if hidden else ""
        return "<span" + cls + hid + ">" + b + "</span>"
    marquee = "".join(brand_span(b) for b in brands) + "".join(brand_span(b, True) for b in brands)

    cats_html = ""
    for key, idx, title, desc, cards in H["cats"]:
        cards_html = ""
        for slug, cls, tag, badge, name, text, chips in cards:
            chat_name = name.replace("&amp;", "&")
            link_name = f'<a href="{r}services/{slug}/">{name}</a>' if slug else name
            more = f'<a class="more" href="{r}services/{slug}/">{H["more"]}</a>' if slug else ""
            cards_html += f"""<article class="card {cls}">
  <div class="tag"><span>{tag}</span>{f'<b>{badge}</b>' if badge else ''}</div>
  <h3>{link_name}</h3>
  <p>{text}</p>
  <div class="foot"><div class="chips">{''.join(f'<span>{c}</span>' for c in chips)}</div><div class="acts">{more}<button class="ask" type="button" data-service="{esc(chat_name)}">{H['ask']}</button></div></div>
</article>
"""
        cats_html += f"""<div class="cat" data-cat="{key}">
  <div class="cat-side"><span class="idx">{idx}</span><h3>{title}</h3><p>{desc}</p></div>
  <div class="cards">{cards_html}</div>
</div>
"""
    filters = "".join(f'<button type="button" aria-pressed="{"true" if k=="all" else "false"}" data-filter="{k}">{v}</button>' for k, v in H["filters"])
    steps = "".join(f'<div class="step"><span class="n">0{i+1}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(H["steps"]))
    regions = "".join(f'<div class="region"><span class="tz">{tz}</span><h3>{n}</h3><p>{p}</p></div>' for tz, n, p in H["regions"])
    spec = "".join(f'<div class="spec-row" role="row"><span role="cell">{a}</span><strong class="{"a" if hi else ""}" role="cell">{b}</strong></div>' for a, b, hi in H["spec"])
    pillars = "".join(f'<div class="pillar"><h3>{t}</h3><p>{p}</p></div>' for t, p in H["pillars"])
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in H["faq"])
    trust = "".join(f"<span>{t}</span>" for t in H["trust"])

    website = {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE_URL + H["path"], "inLanguage": lang, "publisher": {"@id": SITE_URL + "/#org"}}
    alts = [("en", "/"), ("de", "/de/"), ("x-default", "/")]
    out = head(lang, H["title"], H["desc"], H["path"], depth, [ORG, website, faq_ld(H["faq"])], alts)
    out += nav(lang, depth, switch_href=(r if lang == "de" else "de/"), switch_label=("EN" if lang == "de" else "DE"), home_anchor_prefix="")
    out += f"""<main id="top">
  <section class="hero">
    <div class="wrap">
      <div>
        <span class="status"><i></i>{H['status']}</span>
        <h1>{H['h1']}</h1>
        <p class="lede">{H['lede']}</p>
        <div class="ctas">
          <button class="btn btn-amber" type="button" data-open-chat>{CHAT_ICON}{H['cta1']}</button>
          <a class="btn btn-ghost" href="#services">{H['cta2']}</a>
        </div>
        <div class="trust">{trust}</div>
      </div>
      <div class="console" aria-label="Example remote session">
        <div class="console-bar"><span class="dots"><i></i><i></i><i></i></span><span>session.log · example</span><span style="color:var(--online)">● online</span></div>
<pre id="log"><span class="ln"><span class="k">connect</span>   VAS 6154 interface ........ <span class="ok">ok</span></span><span class="ln"><span class="k">vehicle</span>   Audi A4 B9 · WAUZZZF4•••••••</span><span class="ln"><span class="k">gateway</span>   19 Diagnostic interface ... <span class="ok">online</span></span><span class="ln"><span class="k">supply</span>    battery charger ........... <span class="a">13.6 V</span></span><span class="ln"><span class="k">unit</span>      5F Information electronics</span><span class="ln"><span class="k">backend</span>   OEM server login .......... <span class="ok">granted</span></span><span class="ln"><span class="k">activate</span>  App-Connect · CarPlay ..... <span class="ok">done</span></span><span class="ln"><span class="k">verify</span>    fault memory cleared ...... <span class="ok">0 DTC</span></span></pre>
        <div class="gauge"><span>progress</span><div class="track"><b></b></div><span class="volt" id="volt">13.6 V</span></div>
      </div>
    </div>
  </section>

  <div class="brands" aria-label="{H['brands']}"><div class="wrap"><span class="eyebrow">{H['brands']}</span><div class="marquee"><div class="marquee-track">{marquee}</div></div></div></div>

  <section class="sec" id="services">
    <div class="wrap">
      <div class="sec-head"><div><span class="eyebrow">{H['svc_eyebrow']}</span><h2 style="margin-top:.6rem">{H['svc_h2']}</h2></div><p>{H['svc_p']}</p></div>
      <div class="filters" role="group" aria-label="{H['svc_eyebrow']}">{filters}</div>
      {cats_html}
    </div>
  </section>

  <section class="sec process" id="process">
    <div class="wrap">
      <div class="sec-head"><div><span class="eyebrow">{H['proc_eyebrow']}</span><h2 style="margin-top:.6rem">{H['proc_h2']}</h2></div><p>{H['proc_p']}</p></div>
      <div class="steps">{steps}</div>
    </div>
  </section>

  <section class="sec" id="worldwide">
    <div class="wrap">
      <div class="sec-head"><div><span class="eyebrow">{H['reg_eyebrow']}</span><h2 style="margin-top:.6rem">{H['reg_h2']}</h2></div><p>{H['reg_p']}</p></div>
      <div class="regions">{regions}</div>
      <p class="mono" style="margin-top:1.5rem;color:var(--muted);font-size:.8rem;max-width:80ch">→ {H['reg_note']}</p>
    </div>
  </section>

  <section class="sec" id="prepare" style="padding-top:0">
    <div class="wrap prep">
      <div class="prep-copy"><span class="eyebrow">{H['prep_eyebrow']}</span><h2 style="margin-top:.6rem">{H['prep_h2']}</h2><p>{H['prep_p']}</p><p class="note">{H['prep_note']}</p></div>
      <div class="spec" role="table" aria-label="{H['prep_eyebrow']}">{spec}</div>
    </div>
  </section>

  <section class="sec" style="padding-top:0"><div class="wrap pillars">{pillars}</div></section>

  <section class="sec" id="faq" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><span class="eyebrow">FAQ</span><h2 style="margin-top:.6rem">{H['faq_h2']}</h2></div></div>
      <div class="faq">{faq}</div>
    </div>
  </section>

  <section class="final"><div class="wrap"><div class="final-box"><div><h2>{H['final_h2']}</h2><p>{H['final_p']}</p></div><div class="ctas"><button class="btn btn-amber" type="button" data-open-chat>{CHAT_ICON}{H['final_cta']}</button></div></div></div></section>
</main>
"""
    out += footer(lang, depth) + chat(lang, depth)
    return out

# ---------------------------------------------------------------- service pages
def service_page(s):
    depth = 2; r = "../" * depth; path = f"/services/{s['slug']}/"
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["nav"], "serviceType": s["nav"],
              "description": s["desc"], "url": SITE_URL + path, "provider": {"@id": SITE_URL + "/#org"},
              "areaServed": [{"@type": "Place", "name": a} for a in AREAS], "availableChannel": {"@type": "ServiceChannel", "serviceUrl": SITE_URL + path, "name": "Remote session"}}
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE_URL + "/#services"},
        {"@type": "ListItem", "position": 3, "name": s["nav"], "item": SITE_URL + path}]}
    out = head("en", s["title"], s["desc"], path, depth, [ORG, svc_ld, crumbs_ld, faq_ld(s["faq"])], [("en", path), ("x-default", path)])
    out += nav("en", depth, switch_href=r + "de/", switch_label="DE", home_anchor_prefix=r)
    faq = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in s["faq"])
    related = "".join(f'<a href="../{x}/"><strong>{SVC[x]["nav"]}</strong><span>{SVC[x]["short"]}</span></a>' for x in s["related"])
    out += f"""<main>
  <section class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a><span>/</span><a href="{r}#services">Services</a><span>/</span><span aria-current="page">{s['nav']}</span></nav>
      <span class="eyebrow">{s['eyebrow']}</span>
      <h1 style="margin-top:.8rem">{s['h1']}</h1>
      <p class="lede">{s['lede']}</p>
      <div class="ctas">
        <button class="btn btn-amber" type="button" data-open-chat="{esc(s['chat'])}">{CHAT_ICON}Get a quote on WhatsApp</button>
        <a class="btn btn-ghost" href="{r}#services">All services</a>
      </div>
    </div>
  </section>
  <div class="wrap article">
    <article class="prose">
{s['body']}
      <h2>Frequently asked questions</h2>
      <div class="faq">{faq}</div>
    </article>
    <aside class="aside">
      <div class="aside-box">
        <h3>Get a fixed quote</h3>
        <p>Send your car, VIN and the job. You get a clear answer and price, usually the same day.</p>
        <ul><li>Free VIN compatibility check</li><li>Genuine licensed software</li><li>Remote, worldwide</li><li>English, German, Hindi</li></ul>
        <button class="btn btn-amber" type="button" data-open-chat="{esc(s['chat'])}">{CHAT_ICON}Start chat</button>
      </div>
    </aside>
  </div>
  <section class="sec" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><span class="eyebrow">Related</span><h2 style="margin-top:.6rem;font-size:clamp(1.4rem,3vw,2rem)">Other services</h2></div></div>
      <div class="related">{related}</div>
    </div>
  </section>
</main>
"""
    out += footer("en", depth) + chat("en", depth)
    return out

def notfound_page():
    out = head("en", "Page not found | autocodeRHX", "This page doesn't exist. Browse remote coding and programming services from autocodeRHX.", "/404.html", 0, [])
    out = out.replace(f'<meta name="robots" content="{ROBOTS}">', '<meta name="robots" content="noindex">')
    out += nav("en", 0, home_anchor_prefix="/")
    out += """<main><section class="notfound"><div class="wrap"><span class="eyebrow">Error 404</span><h1>Fault code: page not found.</h1><p>The page you're looking for doesn't exist. Head back to the services or ask the assistant.</p><a class="btn btn-amber" href="__BASE__">Back to home</a></div></section></main>
"""
    # 404 is served from any path, so use root-absolute asset links
    out = out.replace('href="./"', 'href="__BASE__"').replace('href="favicon.svg"', 'href="__BASE__favicon.svg"').replace('href="assets/', 'href="__BASE__assets/').replace('href="/#', 'href="__BASE__#')
    tail = footer("en", 0) + chat("en", 0)
    tail = tail.replace('href="services/', 'href="__BASE__services/').replace('src="assets/', 'src="__BASE__assets/')
    return (out + tail).replace("__BASE__", BASE_PATH)

# ---------------------------------------------------------------- static extras
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0A1820"/><rect x="3" y="3" width="58" height="58" rx="10" fill="none" stroke="#FFB547" stroke-width="2"/><text x="32" y="41" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="22" fill="#FFB547">RHX</text></svg>"""

def make_images():
    from PIL import Image, ImageDraw, ImageFont
    B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; M = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    W, Hh = 1200, 630
    im = Image.new("RGB", (W, Hh), "#0A1820"); d = ImageDraw.Draw(im)
    for x in range(0, W, 56): d.line([(x, 0), (x, Hh)], fill="#12293A")
    for y in range(0, Hh, 56): d.line([(0, y), (W, y)], fill="#12293A")
    big = ImageFont.truetype(B, 96); mid = ImageFont.truetype(B, 40); mono = ImageFont.truetype(M, 26)
    d.text((80, 150), "autocode", font=big, fill="#E4EDF1")
    w = d.textlength("autocode", font=big); d.text((80 + w, 150), "RHX", font=big, fill="#FFB547")
    d.text((80, 300), "Remote online programming", font=mid, fill="#E4EDF1")
    d.text((80, 352), "VAG · Porsche · Lamborghini · Bentley · Mercedes", font=mid, fill="#8DA5B2")
    d.rectangle([80, 460, 1120, 462], fill="#1E3A4A")
    d.text((80, 490), "● online   CarPlay activation · Wiring diagrams · Licensed software", font=mono, fill="#5FD0C4")
    im.save(os.path.join(SRC_ASSETS, "og-image.png"), optimize=True)
    ic = Image.new("RGB", (180, 180), "#0A1820"); d = ImageDraw.Draw(ic)
    d.rounded_rectangle([8, 8, 172, 172], radius=26, outline="#FFB547", width=4)
    f = ImageFont.truetype(B, 50); tw = d.textlength("RHX", font=f); d.text(((180 - tw) / 2, 58), "RHX", font=f, fill="#FFB547")
    ic.save(os.path.join(SRC_ASSETS, "apple-touch-icon.png"), optimize=True)

def write(rel, content):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f: f.write(content)

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    # Share image + app icon are generated once (needs Pillow) and then kept in assets/.
    # Delete them from assets/ to regenerate.
    if not (os.path.exists(os.path.join(SRC_ASSETS, "og-image.png")) and os.path.exists(os.path.join(SRC_ASSETS, "apple-touch-icon.png"))):
        make_images()
    shutil.copytree(SRC_ASSETS, os.path.join(OUT, "assets"))
    write("index.html", home_page("en"))
    write("de/index.html", home_page("de"))
    for s in SERVICES: write(f"services/{s['slug']}/index.html", service_page(s))
    write("404.html", notfound_page())
    write("favicon.svg", FAVICON)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    urls = [("/", "1.0", [("en", "/"), ("de", "/de/"), ("x-default", "/")]), ("/de/", "0.9", [("en", "/"), ("de", "/de/"), ("x-default", "/")])]
    urls += [(f"/services/{s['slug']}/", "0.8", None) for s in SERVICES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    for u, pr, alts in urls:
        sm += f"  <url><loc>{SITE_URL}{u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority>"
        if alts: sm += "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{SITE_URL}{p}"/>' for h, p in alts)
        sm += "</url>\n"
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    if CUSTOM_DOMAIN:
        write("CNAME", SITE_URL.split("//", 1)[1] + "\n")
    write(".nojekyll", "")
    print("Built", len(urls), "pages into", OUT)

if __name__ == "__main__":
    main()
