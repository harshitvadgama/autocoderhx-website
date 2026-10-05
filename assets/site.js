/* =====================================================================
   autocodeRHX site script
   CONFIG: put your WhatsApp number here (digits only, with country code)
   ===================================================================== */
const WHATSAPP_NUMBER = "919428853797";
const WHATSAPP_DISPLAY = "+91 94288 53797";

const LANG = (document.documentElement.lang || "en").slice(0, 2);
const T = {
  en: {
    hello: "Hi! I'm the autocodeRHX assistant. What can I help you with today?",
    asking: s => "Hi! You're asking about " + s + ". Let's get you a quote.",
    other: "No problem. Describe what you need in a few words.",
    car: "Which car is it? Brand, model and year, e.g. \"Audi A4 2019\".",
    vin: "Do you have the VIN (17 characters)? It lets me confirm compatibility and quote faster.",
    skip: "Skip for now",
    vinOk: "Got it, VIN looks valid.",
    vinBad: "That doesn't look like a 17-character VIN (no I, O or Q). Try again, or skip.",
    name: "Last one: what's your name?",
    ready: n => "Thanks" + (n ? ", " + n : "") + "! Your message is ready. Tap below to send it on WhatsApp and you'll get a reply with a quote.",
    wa: "Continue on WhatsApp", copy: "Copy message", copied: "Copied", selected: "Selected, press copy",
    addNote: "Add a note", restart: "Start over", noteAsk: "Sure, type your note and I'll add it to the message.",
    again: "Want to start a new request?", somethingElse: "Something else",
    msg: s => "Hi autocodeRHX" + (s.name ? ", I'm " + s.name : "") + ".\nService: " + s.service + "\nCar: " + (s.car || "-") + "\nVIN: " + (s.vin || "will send later") + (s.notes ? "\nNote: " + s.notes : ""),
    services: ["VAG Online Programming", "Component Protection / SVM", "Mercedes AMG Menu / PIN / Coding", "BMW Coding & Programming", "Lamborghini Online Programming", "Bentley Online Programming", "CarPlay / Android Auto Activation", "Diagnostic Software License", "Wiring Diagrams", "Remote Diagnostics"]
  },
  de: {
    hello: "Hallo! Ich bin der autocodeRHX-Assistent. Wobei kann ich helfen?",
    asking: s => "Hallo! Es geht um " + s + ". Dann machen wir dir schnell ein Angebot.",
    other: "Kein Problem. Beschreib kurz, was du brauchst.",
    car: "Um welches Auto geht es? Marke, Modell und Baujahr, z. B. \"Audi A4 2019\".",
    vin: "Hast du die FIN (17 Zeichen)? Damit kann ich die Kompatibilität prüfen und schneller ein Angebot machen.",
    skip: "Später schicken",
    vinOk: "Passt, die FIN sieht gültig aus.",
    vinBad: "Das sieht nicht nach einer 17-stelligen FIN aus (kein I, O oder Q). Nochmal versuchen oder überspringen.",
    name: "Letzte Frage: Wie heißt du?",
    ready: n => "Danke" + (n ? ", " + n : "") + "! Deine Nachricht ist fertig. Tippe unten, um sie per WhatsApp zu senden. Du bekommst dann ein Angebot.",
    wa: "Weiter zu WhatsApp", copy: "Nachricht kopieren", copied: "Kopiert", selected: "Markiert, jetzt kopieren",
    addNote: "Notiz hinzufügen", restart: "Neu starten", noteAsk: "Klar, schreib deine Notiz und ich hänge sie an.",
    again: "Neue Anfrage starten?", somethingElse: "Etwas anderes",
    msg: s => "Hallo autocodeRHX" + (s.name ? ", ich bin " + s.name : "") + ".\nLeistung: " + s.service + "\nAuto: " + (s.car || "-") + "\nFIN: " + (s.vin || "schicke ich noch") + (s.notes ? "\nNotiz: " + s.notes : ""),
    services: ["VAG Online-Programmierung", "Komponentenschutz / SVM", "Mercedes AMG-Menü / PIN / Codierung", "BMW Codierung & Programmierung", "Lamborghini Online-Programmierung", "Bentley Online-Programmierung", "CarPlay / Android Auto Freischaltung", "Diagnose-Softwarelizenz", "Stromlaufpläne", "Ferndiagnose"]
  }
};
const L = T[LANG] || T.en;
const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- hero log sweep ---------- */
(function () {
  const lines = [...document.querySelectorAll("#log .ln")];
  const volt = document.getElementById("volt");
  if (!lines.length || reduced) return;
  let i = 0;
  setInterval(() => { lines.forEach(l => l.classList.remove("live")); lines[i % lines.length].classList.add("live"); i++; }, 1100);
  if (volt) setInterval(() => { volt.textContent = (13.5 + Math.random() * 0.2).toFixed(1) + " V"; }, 1600);
})();

/* ---------- service filter ---------- */
(function () {
  const btns = document.querySelectorAll("[data-filter]");
  const cats = document.querySelectorAll(".cat");
  btns.forEach(b => b.addEventListener("click", () => {
    btns.forEach(x => x.setAttribute("aria-pressed", String(x === b)));
    const f = b.dataset.filter;
    cats.forEach(c => { c.hidden = !(f === "all" || c.dataset.cat === f); });
    [...cats].filter(c => !c.hidden).forEach((c, idx) => { c.style.borderTop = idx === 0 ? "0" : ""; c.style.paddingTop = idx === 0 ? "0" : ""; });
  }));
})();

/* ---------- chat assistant ---------- */
(function () {
  const fab = document.getElementById("chatFab"), box = document.getElementById("chat"), log = document.getElementById("chatLog");
  const form = document.getElementById("chatForm"), input = document.getElementById("chatText");
  if (!fab || !box) return;
  const BRANDS = ["Volkswagen", "Audi", "Mercedes-Benz", "BMW", "Porsche", "Lamborghini", "Bentley"];
  let state, started = false;

  function reset() { state = { step: "service", service: "", car: "", vin: "", name: "", notes: "" }; log.innerHTML = ""; started = false; }
  reset();
  const scroll = () => { log.scrollTop = log.scrollHeight; };
  function add(text, who) { const d = document.createElement("div"); d.className = "msg " + who; d.textContent = text; log.appendChild(d); scroll(); }
  function quick(opts, handler) {
    const w = document.createElement("div"); w.className = "quick";
    opts.forEach(o => { const b = document.createElement("button"); b.type = "button"; b.textContent = o; b.onclick = () => { w.remove(); handler(o); }; w.appendChild(b); });
    log.appendChild(w); scroll();
  }
  const clearQuick = () => log.querySelectorAll(".quick").forEach(q => q.remove());
  function bot(text, then) {
    const t = document.createElement("div"); t.className = "msg bot typing"; t.innerHTML = "<i></i><i></i><i></i>"; log.appendChild(t); scroll();
    setTimeout(() => { t.remove(); add(text, "bot"); then && then(); }, reduced ? 0 : Math.min(450 + text.length * 9, 1100));
  }
  const askService = () => bot(L.hello, () => quick([...L.services, L.somethingElse], v => user(v)));
  function askCar() { state.step = "car"; bot(L.car, () => quick(BRANDS, v => { input.value = v + " "; input.focus(); })); }
  function askVin() { state.step = "vin"; bot(L.vin, () => quick([L.skip], v => user(v))); }
  function askName() { state.step = "name"; bot(L.name); }

  function finish() {
    state.step = "done";
    const msg = L.msg(state);
    bot(L.ready(state.name), () => {
      const h = document.createElement("div"); h.className = "handoff";
      const pre = document.createElement("pre"); pre.textContent = msg;
      const a = document.createElement("a"); a.className = "wa-btn"; a.target = "_blank"; a.rel = "noopener";
      a.href = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(msg);
      a.innerHTML = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>' + L.wa;
      const num = document.createElement("div"); num.className = "wa-num";
      num.innerHTML = "<span></span><button type=\"button\"></button>";
      num.querySelector("span").textContent = WHATSAPP_DISPLAY;
      const cb = num.querySelector("button"); cb.textContent = L.copy;
      cb.onclick = () => {
        const sel = () => { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); cb.textContent = L.selected; };
        try { navigator.clipboard.writeText(msg).then(() => { cb.textContent = L.copied; setTimeout(() => cb.textContent = L.copy, 1600); }, sel); } catch (e) { sel(); }
      };
      h.append(pre, a, num); log.appendChild(h); scroll();
      quick([L.addNote, L.restart], v => {
        if (v === L.restart) { reset(); started = true; askService(); }
        else { state.step = "notes"; bot(L.noteAsk); }
      });
    });
  }

  function user(text) {
    text = String(text).trim(); if (!text) return;
    clearQuick(); add(text, "me");
    switch (state.step) {
      case "service":
        if (text === L.somethingElse) { state.step = "other"; bot(L.other); } else { state.service = text; askCar(); }
        break;
      case "other": state.service = text; askCar(); break;
      case "car": state.car = text; askVin(); break;
      case "vin": {
        if (text === L.skip) { state.vin = ""; askName(); break; }
        const v = text.toUpperCase().replace(/\s/g, "");
        if (/^[A-HJ-NPR-Z0-9]{17}$/.test(v)) { state.vin = v; bot(L.vinOk, askName); }
        else bot(L.vinBad, () => quick([L.skip], x => user(x)));
        break;
      }
      case "name": state.name = text.slice(0, 40); finish(); break;
      case "notes": state.notes = text; finish(); break;
      default: bot(L.again, () => quick([L.restart], () => { reset(); started = true; askService(); }));
    }
  }

  form.addEventListener("submit", e => { e.preventDefault(); const t = input.value; input.value = ""; user(t); });
  function open(service) {
    box.hidden = false; fab.hidden = true;
    if (service) { reset(); started = true; bot(L.asking(service), () => { state.service = service; askCar(); }); }
    else if (!started) { started = true; askService(); }
    setTimeout(() => input.focus(), 250);
  }
  function close() { box.hidden = true; fab.hidden = false; fab.focus(); }
  fab.addEventListener("click", () => open());
  document.getElementById("chatClose").addEventListener("click", close);
  document.getElementById("chatReset").addEventListener("click", () => { reset(); started = true; askService(); });
  document.querySelectorAll("[data-open-chat]").forEach(b => b.addEventListener("click", () => open(b.dataset.openChat || "")));
  document.querySelectorAll("[data-service]").forEach(b => b.addEventListener("click", () => open(b.dataset.service)));
  document.addEventListener("keydown", e => { if (e.key === "Escape" && !box.hidden) close(); });
})();
