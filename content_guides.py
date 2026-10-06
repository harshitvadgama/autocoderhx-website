# Guides: long-tail articles that answer what customers actually search for.
# Each one links to the matching service page. Edit text here, then run: python3 build.py

GUIDES = [
{
 "slug": "carplay-activation-by-model",
 "title": "CarPlay Activation by Model: VW, Audi, Skoda | autocodeRHV",
 "desc": "Which VW, Audi, Skoda, SEAT and Cupra models can get CarPlay and Android Auto by coding, by head unit: Golf, A4, Octavia, Tiguan and more.",
 "h1": "CarPlay activation by model: which VW Group cars can have it switched on",
 "lede": "A model-by-model overview of which Volkswagen, Audi, Skoda, SEAT and Cupra head units can run Apple CarPlay and Android Auto, and what to check before you book.",
 "service": "carplay-activation",
 "date": "2026-10-06",
 "body": """
<h2>It depends on the head unit, not the model name</h2>
<p>Volkswagen Group calls CarPlay and Android Auto <strong>App-Connect</strong>. Whether it can be switched on depends on which infotainment generation your car has (MIB2, MIB2.5 or MIB3), the exact hardware variant and its software version. Two cars with the same model name can have different units, especially across a facelift or between markets.</p>

<h2>Overview by model</h2>
<div class="spec" style="margin:0 0 1.4rem">
<div class="spec-row"><span>VW Golf 7 / 7.5</span><strong>MIB2 / MIB2.5 · usually wired</strong></div>
<div class="spec-row"><span>VW Golf 8</span><strong>MIB3 · often wireless</strong></div>
<div class="spec-row"><span>VW Passat B8 (pre-facelift)</span><strong>MIB2 · wired</strong></div>
<div class="spec-row"><span>VW Passat B8 facelift, Arteon facelift</span><strong>MIB3 · often wireless</strong></div>
<div class="spec-row"><span>VW Tiguan AD1 (pre-facelift)</span><strong>MIB2 / MIB2.5 · wired</strong></div>
<div class="spec-row"><span>VW Polo AW, T-Roc, Taigun, Virtus</span><strong>MIB2.5 / MIB3 · depends on unit</strong></div>
<div class="spec-row"><span>Audi A3 8V</span><strong>MIB2 / MMI · wired</strong></div>
<div class="spec-row"><span>Audi A3 8Y</span><strong>MIB3 · wireless</strong></div>
<div class="spec-row"><span>Audi A4 / A5 B9 (pre-facelift)</span><strong>MIB2 · wired</strong></div>
<div class="spec-row"><span>Audi A4 / A5 B9 facelift, Q5 FY facelift</span><strong>MIB3 · wireless</strong></div>
<div class="spec-row"><span>Skoda Octavia 3 / Superb 3</span><strong>MIB2 · wired</strong></div>
<div class="spec-row"><span>Skoda Octavia 4, Kodiaq, Kushaq, Slavia</span><strong>MIB3 or Skoda units · depends on unit</strong></div>
<div class="spec-row"><span>SEAT Leon 4, Cupra Formentor</span><strong>MIB3 · often wireless</strong></div>
</div>
<p>This table is a guide, not a guarantee. Smaller "Composition" and "Bolero"-type units, navigation and non-navigation variants, and regional software all change the answer. <strong>The VIN check decides.</strong></p>

<h2>Wired or wireless?</h2>
<p>Wireless CarPlay needs the right radio and Wi-Fi hardware inside the head unit. Many MIB3 units have it; most MIB2 units only support wired CarPlay over USB. Coding can't add hardware that isn't there.</p>

<h2>How to check your own car</h2>
<ul>
<li>Look in the infotainment settings under "System information" or "Version information" for the unit type and software version</li>
<li>Check whether the menu already lists "App-Connect" or "Smartphone interface" as a greyed-out option</li>
<li>Or simply send me the VIN. I check the head unit and software version and tell you if it works before you pay</li>
</ul>

<h2>What activation involves</h2>
<p>The function is enabled in the head unit's software, then coded so the steering wheel buttons, microphone and USB ports work with it. A full scan before and after makes sure no new fault codes are left behind.</p>
""",
 "faq": [
  ("Can every MIB2 unit get CarPlay?", "No. Some smaller units can't run App-Connect at all. The VIN check tells you which unit you have."),
  ("Will an update at the dealer remove it?", "It's stored in the head unit. If anything changes after a dealer visit, it can be checked and restored."),
  ("Can you add wireless CarPlay to a wired unit?", "Not by coding alone. Wireless needs hardware that only some units have."),
 ],
},
{
 "slug": "component-protection-explained",
 "title": "Component Protection Removal Explained | autocodeRHV",
 "desc": "Why a used VW or Audi cluster, radio or gateway shows 'Component Protection active' and how CP is removed legally online.",
 "h1": "\"Component Protection active\": what it means and how it's removed",
 "lede": "Fitted a used instrument cluster, radio or gateway and now it's locked? Here's what Volkswagen Group Component Protection is and how a module is adapted to your car the legitimate way.",
 "service": "component-protection",
 "date": "2026-10-06",
 "body": """
<h2>What Component Protection does</h2>
<p>Component Protection (CP, in German <em>Komponentenschutz</em>) ties certain electronic modules to the car they were built for. If a protected module is moved to a different car, it detects the mismatch and limits itself until it's adapted to the new vehicle. The idea is to make stolen electronics worthless.</p>

<h2>Typical symptoms</h2>
<ul>
<li>Radio or infotainment powers up but plays no sound, or shows "Component protection" on screen</li>
<li>Instrument cluster works only partly, with warnings that won't clear</li>
<li>Climate control stuck in a default mode</li>
<li>Fault memory shows "Component protection active" in the affected control unit</li>
</ul>

<h2>Which modules are usually protected</h2>
<p>Instrument clusters and virtual cockpits, infotainment and navigation units, gateways, climate control units and some comfort and assistance modules. A full scan shows exactly which modules in your car report CP.</p>

<h2>How CP is removed legitimately</h2>
<p>The official route is an online adaptation through the manufacturer's backend. The car connects through the factory diagnostic software, the backend checks the request and the module is adapted to your VIN. Afterwards the module usually needs <a href="../../services/vag-online-programming/">SVM online coding</a> so its software and coding match your car.</p>
<p>Because CP exists to stop stolen parts being reused, <strong>proof of ownership is required</strong>: a registration document matching the VIN.</p>

<h2>Before you buy a used module</h2>
<ul>
<li>Match the part number and hardware version to your car as closely as possible</li>
<li>Check the software version if the seller lists it</li>
<li>Avoid modules from cars with unknown history, and keep the invoice</li>
<li>Ask before buying. I can check the part number against your VIN</li>
</ul>
""",
 "faq": [
  ("Can CP be removed without online access?", "Not through the official process. Offline tricks exist but are unreliable and often leave other faults behind."),
  ("Does CP affect Porsche and Bentley too?", "Yes. Porsche and Bentley share Volkswagen Group electronics and use the same principle."),
  ("How long does it take?", "Usually one remote session, including the SVM coding afterwards."),
 ],
},
{
 "slug": "svm-coding-explained",
 "title": "VAG SVM Coding Explained | autocodeRHV",
 "desc": "What SVM (Software Version Management) is, when VW, Audi, Skoda and SEAT need online SVM coding, and why 'not coded' faults appear.",
 "h1": "SVM coding explained: why your VAG car needs online coding after a module swap",
 "lede": "SVM is the step most people skip, and the reason a replaced module shows \"not coded\" or \"software version incorrect\". Here's what it does.",
 "service": "vag-online-programming",
 "date": "2026-10-06",
 "body": """
<h2>What SVM is</h2>
<p>SVM stands for <strong>Software Version Management</strong>. Every Volkswagen Group car has a record at the factory of which control units, software versions and coding it should have. When you run SVM in ODIS, the car sends its current state to the manufacturer's server, the server compares it with what's expected, and sends back the correct software, coding and parameters.</p>

<h2>When SVM is needed</h2>
<ul>
<li>After replacing a control unit with a new or used one</li>
<li>After retrofitting equipment such as cameras, lights or assistance systems</li>
<li>When the fault memory shows coding or software version deviations</li>
<li>After Component Protection adaptation of a used module</li>
</ul>

<h2>Typical symptoms without SVM</h2>
<p>"Not coded" or "incorrectly coded" faults, functions that don't work, warnings that come back after every clear, and gateway installation list errors. Manual coding with an offline tool can sometimes get a module working, but it doesn't update the factory record, so the next dealer visit may undo it.</p>

<h2>What a remote SVM session looks like</h2>
<ul>
<li>Full scan and check of the installation list</li>
<li>Online SVM comparison with the factory backend</li>
<li>Software and coding applied to the affected modules</li>
<li>Adaptations and basic settings, then a final scan</li>
</ul>
<p>Stable voltage matters: see <a href="../programming-battery-voltage/">why battery voltage matters during programming</a>.</p>
""",
 "faq": [
  ("Can VCDS do SVM?", "No. VCDS is excellent for coding and diagnosis, but SVM needs online access to the manufacturer's backend through ODIS."),
  ("Does SVM work on imported cars?", "Usually yes. The VIN tells the backend which market and equipment the car has."),
 ],
},
{
 "slug": "mercedes-amg-menu-activation",
 "title": "Mercedes AMG Menu Activation Guide | autocodeRHV",
 "desc": "What the Mercedes AMG menu shows (oil temp, G-meter, boost, power), which C-Class, E-Class and GLC clusters support it, and how.",
 "h1": "Mercedes AMG menu activation: what it shows and which cars can have it",
 "lede": "The AMG menu adds performance displays to the instrument cluster of many non-AMG Mercedes-Benz models. Here's what you get and how to check if your car qualifies.",
 "service": "mercedes-coding",
 "date": "2026-10-06",
 "body": """
<h2>What the AMG menu shows</h2>
<ul>
<li>Engine oil and transmission oil temperature</li>
<li>G-meter for lateral and longitudinal forces</li>
<li>Boost pressure on turbocharged engines</li>
<li>Power and torque displays on supported clusters</li>
<li>On some cars a lap timer and race data</li>
</ul>

<h2>Which cars can have it</h2>
<p>It's most commonly activated on C-Class (W205/S205), E-Class (W213/S213), GLC (X253) and CLA/A-Class models, but the deciding factor is the <strong>instrument cluster and its software</strong>, not the model badge. Analogue-dial clusters and fully digital clusters behave differently, and MBUX-era cars have their own display logic.</p>
<p>Because of that, every AMG menu job starts with a VIN check. You'll know before you pay whether your cluster supports it.</p>

<h2>How it's done</h2>
<p>The menu is switched on by variant coding the instrument cluster with XENTRY. No hardware changes, no drilling, nothing visible from outside. If the car is later serviced at a dealer, the coding usually stays, and if it doesn't, it can be restored.</p>

<h2>Often combined with</h2>
<ul>
<li>Smartphone integration (CarPlay and Android Auto) on supported head units</li>
<li>Ambient light colour options</li>
<li>Start-stop remembering your last setting</li>
</ul>
""",
 "faq": [
  ("Does AMG menu activation affect warranty?", "It's a coding change in the cluster, not a hardware change. Ask your dealer if you're concerned; it can be reverted."),
  ("Does it work on diesel cars?", "The oil temperature and G-meter screens usually do. Boost display depends on the engine and cluster."),
 ],
},
{
 "slug": "uk-import-mph-to-kmh",
 "title": "UK Import to Ireland: Change mph to km/h by Coding | autocodeRHV",
 "desc": "UK import in Ireland? How speedometer, trip computer and service intervals switch from mph to km/h by coding on VW, Audi, Mercedes, BMW.",
 "h1": "UK import to Ireland: switching mph to km/h by coding",
 "lede": "Most German cars imported from the UK can show km/h as the main unit after coding. Here's what changes, what doesn't, and how to check your car.",
 "service": "remote-diagnostics",
 "region": "ie",
 "date": "2026-10-06",
 "body": """
<h2>What can be changed</h2>
<ul>
<li>Speed display: km/h as the main unit on digital clusters and digital readouts</li>
<li>Trip computer, range and average consumption in kilometres and l/100 km</li>
<li>Service interval display in kilometres</li>
<li>Navigation and radio country settings</li>
</ul>

<h2>Analogue dials vs digital clusters</h2>
<p>On a <strong>fully digital cluster</strong> (Virtual Cockpit, Active Info Display, BMW Live Cockpit, Mercedes widescreen) the whole display switches to km/h. On an <strong>analogue cluster</strong>, the printed dial face stays as it is: usually mph with a smaller km/h scale. The digital readout between the dials can switch to km/h, but the needle scale can only change by swapping the cluster.</p>

<h2>Brands covered</h2>
<p>Volkswagen, Audi, Skoda, SEAT, Cupra, Mercedes-Benz and BMW. Send the VIN and I'll tell you exactly what your cluster will show before you book.</p>

<h2>Lights and other settings</h2>
<p>Daytime running light behaviour and some lighting settings can also be adapted. Right-hand-drive headlights stay right-hand-drive, which is correct for Ireland.</p>

<p>More for Irish drivers: <a href="../../ie/">car coding in Ireland</a>.</p>
""",
 "faq": [
  ("Is the mileage converted?", "The odometer keeps its true distance; the display unit changes. Nothing is altered about the recorded distance."),
  ("Can it be changed back?", "Yes, every coding change can be reverted."),
 ],
},
{
 "slug": "us-car-canada-drl-kmh",
 "title": "US Car Imported to Canada: DRL & km/h Coding | autocodeRHV",
 "desc": "US car in Canada? How daytime running lights, km/h speedometer, °C and French menus are coded on VW, Audi, Mercedes-Benz and BMW.",
 "h1": "US car imported to Canada: daytime running lights and km/h by coding",
 "lede": "Canadian rules require daytime running lights, and drivers want km/h. On many German cars both are coding changes. Here's how it works.",
 "service": "remote-diagnostics",
 "region": "ca",
 "date": "2026-10-06",
 "body": """
<h2>Common changes for US imports</h2>
<ul>
<li>Daytime running lights activated</li>
<li>Speedometer and trip computer in km/h as the main unit</li>
<li>Temperature in °C, fuel consumption in L/100 km</li>
<li>French language menus where the unit includes them</li>
</ul>

<h2>What decides what's possible</h2>
<p>The lighting control module and instrument cluster. Most current Volkswagen Group, Mercedes-Benz and BMW models support DRL activation by coding. For speed display, digital clusters switch fully; analogue clusters keep the printed mph dial with a secondary km/h scale.</p>

<h2>Import paperwork is separate</h2>
<p>Whether a car can be imported, and which inspection it needs, is handled by the Registrar of Imported Vehicles (RIV) and your province. I only do the coding part. Check RIV's admissibility list before you buy.</p>

<h2>Cold weather tip</h2>
<p>Keep a battery charger connected for the whole session. A cold battery is the most common reason programming fails. More on that in <a href="../programming-battery-voltage/">why battery voltage matters during programming</a>.</p>

<p>More for Canadian drivers: <a href="../../ca/">car coding in Canada</a>.</p>
""",
 "faq": [
  ("Do I need to be at a garage?", "No. A laptop, a supported interface and internet at the car are enough."),
  ("Which interface do I need?", "For Volkswagen Group cars a VAS 6154 or J2534 interface, for BMW an ENET cable. I'll confirm for your car."),
 ],
},
{
 "slug": "programming-battery-voltage",
 "title": "Why Battery Voltage Matters When Programming a Car | autocodeRHV",
 "desc": "Why ECU programming fails on a weak battery, what voltage to hold (13.0–14.0 V), which chargers work, and how to prepare your car for a remote coding session.",
 "h1": "Why battery voltage matters when you program a car",
 "lede": "Most failed flashes have the same cause: the voltage dropped. Here's what to use and how to set up before any programming session.",
 "service": "remote-diagnostics",
 "date": "2026-10-06",
 "body": """
<h2>What happens during programming</h2>
<p>When a control unit is flashed, its old software is erased and new software is written block by block. With the ignition on, fans, modules and lights draw a lot of current. If the battery sags below what the module needs, the write can stop halfway, and the module may not start again until it's recovered.</p>

<h2>The target: 13.0–14.0 V, steady</h2>
<p>A battery on its own drops quickly under load. A proper programming power supply or a strong smart charger with a supply mode holds the voltage steady for the whole session. A small trickle charger is not enough.</p>
<ul>
<li>Use a charger or power supply rated for programming, ideally 30 A or more for larger cars</li>
<li>Connect it to the jump points under the bonnet, not through the cigarette lighter</li>
<li>Switch off lights, climate control and the infotainment screen where possible</li>
<li>Close the doors and keep the key in range</li>
</ul>

<h2>Other things that break sessions</h2>
<ul>
<li>Laptop going to sleep or running Windows updates mid-session</li>
<li>Weak Wi-Fi: a cable or a strong signal near the car is best</li>
<li>Loose OBD connector or a low-quality interface clone</li>
</ul>

<h2>Before your session with me</h2>
<p>I go through this checklist with you at the start of every session. If something's missing, we fix it first. It's faster than recovering a module afterwards.</p>
""",
 "faq": [
  ("Can I just leave the engine running?", "No. Most programming needs the engine off and ignition on. That's why a charger is needed."),
  ("Is a jump starter pack enough?", "Usually not. They're built for short bursts, not a steady supply for 30–60 minutes."),
 ],
},
{
 "slug": "retrofit-coding-guide",
 "title": "Retrofit Coding: Make Retrofitted Parts Work | autocodeRHV",
 "desc": "Why retrofitted cameras, LED headlights, ACC radar or steering wheels show faults, and how coding and online parameterisation make them work like factory fit.",
 "h1": "Retrofit coding: making a retrofitted part work like factory fit",
 "lede": "Fitting the part is half the job. Here's why a retrofit throws faults until the car is told it's there, and what proper coding involves.",
 "service": "vag-online-programming",
 "date": "2026-10-06",
 "body": """
<h2>Why retrofits show faults</h2>
<p>Every car has a stored list of the equipment it was built with. A new reversing camera, LED headlight, adaptive cruise radar or multifunction steering wheel isn't on that list, so other modules don't expect it, don't talk to it, or flag it as an error.</p>

<h2>What coding does</h2>
<ul>
<li>Adds the part to the installation list so the gateway expects it</li>
<li>Codes the new module and the modules that interact with it</li>
<li>Loads parameter sets, for example headlight or camera calibration data</li>
<li>Runs adaptations and basic settings</li>
</ul>
<p>On Volkswagen Group cars, many retrofits also need <a href="../svm-coding-explained/">SVM online coding</a> to load the correct parameters from the factory backend. Mercedes-Benz uses variant coding and SCN, BMW uses vehicle order coding with ISTA.</p>

<h2>Common retrofits</h2>
<ul>
<li>Reversing and 360° cameras</li>
<li>LED and matrix headlights</li>
<li>Adaptive cruise control radar and lane assist cameras</li>
<li>Multifunction and paddle-shift steering wheels</li>
<li>Virtual cockpit and digital clusters</li>
</ul>

<h2>Before you buy parts</h2>
<p>Send me the part numbers and your VIN first. Some retrofits need extra wiring or a different version of a control unit, and it's better to know before you spend money.</p>
""",
 "faq": [
  ("Can every retrofit be coded?", "Most factory parts can, if the car's electronics support them. Some need extra modules or wiring."),
  ("Do you help with wiring?", "Yes, with wiring diagrams and guided checks, so you know exactly which pins to connect."),
 ],
},
]
