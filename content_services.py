# Service landing pages (English). Each page targets one search intent.
# Edit text here, then run:  python3 build.py

PORSCHE = {
 "slug": "porsche-programming",
 "nav": "Porsche PIWIS Programming",
 "chat": "Porsche Programming",
 "title": "Porsche PIWIS Coding & Programming | autocodeRHX",
 "desc": "Remote Porsche coding and programming with PIWIS for 911, Cayenne, Macan, Panamera and Taycan. Module replacement, retrofits and diagnostics.",
 "eyebrow": "911 · CAYENNE · MACAN · PANAMERA · TAYCAN",
 "h1": "Porsche programming with PIWIS",
 "lede": "Control unit coding, adaptations and retrofit coding with Porsche's own workshop system, done remotely.",
 "short": "Coding, adaptations and retrofits with PIWIS.",
 "keywords": ["Porsche PIWIS coding", "Porsche programming", "Porsche retrofit coding"],
 "body": """
<h2>Dealer tooling for Porsche</h2>
<p>PIWIS is Porsche's own diagnostic and programming system. It's the tool for jobs that generic scanners can't finish: coding a replaced control unit, adaptations after repairs and enabling retrofitted equipment.</p>

<h2>Common jobs</h2>
<ul>
<li>Coding a new or used control unit to your car</li>
<li>Adaptations and calibrations after repairs</li>
<li>Retrofit coding for supported equipment (lights, cameras, assistance systems)</li>
<li>Full-system scan and diagnosis of electrical faults</li>
</ul>

<h2>Models</h2>
<p>911, Cayenne, Macan, Panamera, Taycan and Boxster/Cayman. Model year, market and installed software decide what's possible, so send your VIN first.</p>
""",
 "faq": [
  ("Which Porsche models do you cover?", "911, Cayenne, Macan, Panamera, Taycan and Boxster/Cayman. Send the VIN to confirm your car."),
  ("Do I need my own PIWIS?", "No. You provide the interface and laptop at the car. I run the software."),
  ("Is this done remotely?", "Yes, like every autocodeRHX service."),
 ],
 "related": ["remote-diagnostics", "vag-online-programming", "wiring-diagrams"],
}

MERCEDES = {
 "slug": "mercedes-coding",
 "nav": "Mercedes-Benz Coding",
 "chat": "Mercedes-Benz Coding",
 "title": "Mercedes Coding: AMG Menu, PIN Code, XENTRY | autocodeRHX",
 "desc": "Remote Mercedes-Benz coding with XENTRY: AMG menu activation, speed warning settings, anti-theft PIN code, CarPlay, variant coding and retrofits.",
 "eyebrow": "C · E · S-CLASS · GLC · GLE · AMG",
 "h1": "Mercedes-Benz coding and programming",
 "lede": "AMG menu, speed warning settings, anti-theft PIN, smartphone integration and retrofit coding for Mercedes-Benz, done remotely with XENTRY.",
 "short": "AMG menu, PIN code, speed warnings, CarPlay, retrofits.",
 "keywords": ["Mercedes AMG menu activation", "Mercedes coding", "Mercedes anti-theft PIN", "XENTRY variant coding"],
 "body": """
<h2 id="amg">AMG menu activation</h2>
<p>Many Mercedes models can show the AMG menu in the instrument cluster: engine and gearbox oil temperature, G-meter, boost and power/torque displays, and on some cars a lap timer. On supported clusters it's a coding change, so no new hardware is needed.</p>

<h2 id="speed-warning">Speed limit warning settings</h2>
<p>Newer cars warn with chimes and messages every time the speed limit is exceeded. I can change how these warnings behave and switch off the repeat chimes where this is allowed.</p>
<p><strong>Note for EU-registered cars:</strong> new cars registered in the EU since July 2024 must have the Intelligent Speed Assistant (ISA) active at every engine start. On these cars I only change what the regulation allows. Cars outside the EU have more options. Tell me where the car is registered.</p>

<h2 id="pin">Anti-theft PIN code</h2>
<p>Set up PIN protection on the head unit, or get a head unit working again after battery work, a repair or a unit swap when it asks for its anti-theft code. <strong>Proof of ownership is required</strong>: a registration document that matches the VIN.</p>

<h2>More Mercedes jobs</h2>
<ul>
<li>Apple CarPlay and Android Auto (smartphone integration) on supported NTG head units</li>
<li>Variant coding and SCN online coding after a control unit is replaced</li>
<li>Retrofit coding: reversing and 360° cameras, lights, ambient lighting, steering wheels</li>
<li>Comfort coding: ambient light colours, start-stop remembers your last setting, display options</li>
<li>Full-system scan and electrical fault finding with XENTRY</li>
</ul>

<h2>Supported models</h2>
<p>C-, E- and S-Class, CLA, CLS, GLA, GLC, GLE, GLS, G-Class, and AMG models. What's possible depends on the cluster, head unit and software level, so I check your VIN first.</p>
""",
 "faq": [
  ("Can every Mercedes show the AMG menu?", "No. It depends on the instrument cluster and its software. Send your VIN and I'll confirm before you pay."),
  ("Can you remove the speed limit warning completely?", "On cars outside the EU, often yes. On EU cars registered since July 2024 the speed assistant must stay active at each start by law, so I only adjust what's allowed."),
  ("Why do you need proof of ownership for PIN codes?", "Anti-theft codes protect the car. I only work on them for the registered owner or their workshop."),
  ("Do you use XENTRY?", "Yes, XENTRY is the official Mercedes-Benz workshop system."),
 ],
 "related": ["remote-diagnostics", "carplay-activation", "wiring-diagrams"],
}

BMW = {
 "slug": "bmw-coding",
 "nav": "BMW Coding & Programming",
 "chat": "BMW Coding & Programming",
 "title": "BMW Coding & ISTA Programming, CarPlay | autocodeRHX",
 "desc": "Remote BMW and MINI coding and programming with ISTA: CarPlay activation, module replacement, software updates, retrofits and comfort coding.",
 "eyebrow": "BMW · MINI · F / G SERIES",
 "h1": "BMW coding and programming",
 "lede": "CarPlay, software updates, module replacement and retrofit coding for BMW and MINI. Done remotely with ISTA.",
 "short": "CarPlay, ISTA programming, retrofits and comfort coding.",
 "keywords": ["BMW coding", "BMW ISTA programming", "BMW CarPlay activation", "BMW retrofit coding"],
 "body": """
<h2>Programming with ISTA</h2>
<p>ISTA is BMW's workshop system for diagnosis and programming. I use it for software updates, coding a replaced control unit and the programming step after a repair, on F- and G-series BMW and MINI.</p>

<h2>Popular BMW jobs</h2>
<ul>
<li><strong>Apple CarPlay activation</strong> on supported NBT Evo and MGU head units, plus full-screen display where the hardware supports it</li>
<li><strong>Module replacement and coding:</strong> headlights, footwell module, instrument cluster, head unit</li>
<li><strong>Software updates</strong> for control units and the whole vehicle</li>
<li><strong>Retrofit coding:</strong> reversing camera, LED or laser lights, M steering wheel, parking sensors, assistance systems</li>
<li><strong>Comfort coding:</strong> digital speed display, sport displays, mirror folding with the key, start-stop remembers your last setting</li>
<li><strong>Battery registration</strong> after a battery change, so the charging strategy matches the new battery</li>
</ul>

<h2>Before the session</h2>
<p>BMW programming sessions can be long and draw a lot of current. A strong battery charger is essential, plus a Windows laptop, a supported interface (ENET cable or ICOM) and stable internet. I'll confirm the exact setup for your car.</p>

<h2>Check first</h2>
<p>Head unit generation, model year and installed software decide what's possible. Send your VIN and I'll tell you exactly what your car supports.</p>
""",
 "faq": [
  ("Which BMW models do you cover?", "F- and G-series BMW and current MINI models. Older E-series on request."),
  ("Which interface do I need?", "For most coding an ENET cable is enough. Larger programming jobs work best with an ICOM. I'll tell you which fits your job."),
  ("Is battery registration really needed?", "Yes. Without it the car charges a new battery as if it were the old one, which shortens its life."),
  ("Do you do video in motion?", "No. Video while driving is a distraction and illegal in many countries."),
 ],
 "related": ["carplay-activation", "remote-diagnostics", "wiring-diagrams"],
}

CP = {
 "slug": "component-protection",
 "nav": "Component Protection (VAG)",
 "chat": "Component Protection / SVM",
 "title": "Component Protection Removal & SVM (VW, Audi) | autocodeRHX",
 "desc": "Component Protection adaptation for VW, Audi, SEAT, Škoda, Porsche and Bentley parts through the official online process, plus SVM coding. Remote.",
 "eyebrow": "VW · AUDI · SEAT · ŠKODA · PORSCHE · BENTLEY",
 "h1": "Component Protection and SVM for VAG",
 "lede": "Used cluster, radio or gateway showing \"Component Protection active\"? It gets adapted to your car through the official online process, then SVM coded. Done remotely.",
 "short": "Adapting used modules through the official online process.",
 "keywords": ["Component Protection removal", "VAG component protection", "CP removal Audi", "SVM coding"],
 "body": """
<h2>What Component Protection is</h2>
<p>Component Protection (CP) is Volkswagen Group's anti-theft system for electronic parts. Instrument clusters, infotainment units, gateways, climate controls and other modules are tied to the car they were built for. Fit one from another car and it locks: no radio sound, missing functions, and the fault "Component Protection active".</p>

<h2>How it's removed</h2>
<p>The legitimate way is the manufacturer's online process. The vehicle connects to the official backend, ownership of the part and car is checked, and the module is adapted to your VIN. After that the module usually needs <strong>SVM online coding</strong> so its software and coding match your car.</p>
<ul>
<li>CP adaptation for used or new modules</li>
<li>SVM online coding and installation list update</li>
<li>Full scan before and after</li>
</ul>
<p><strong>Proof of ownership is required</strong> for the car (registration matching the VIN). CP exists to stop stolen parts being reused, so this isn't optional.</p>

<h2>Typical cases</h2>
<ul>
<li>Instrument cluster or virtual cockpit from a breaker's yard</li>
<li>MIB infotainment unit swapped after a fault</li>
<li>Gateway or climate control replaced after water damage</li>
<li>Audi MMI and Porsche PCM units</li>
</ul>
""",
 "faq": [
  ("Can CP be removed offline?", "Not through the official process. CP adaptation needs the manufacturer's online backend, which is what I use."),
  ("Which parts have Component Protection?", "Typically instrument clusters, infotainment units, gateways, climate control and some comfort modules. The scan shows which modules report CP."),
  ("Do I need SVM after CP?", "Usually yes, so the module's software and coding match your car. Both can be done in one session."),
  ("What do I need to send?", "VIN, a scan or photo of the fault, and the registration document."),
 ],
 "related": ["vag-online-programming", "remote-diagnostics", "wiring-diagrams"],
}

SERVICES = [
{
 "slug": "vag-online-programming",
 "nav": "VAG Online Programming",
 "chat": "VAG Online Programming",
 "title": "VAG Online Programming & SVM Coding | autocodeRHX",
 "desc": "Remote VAG online programming for VW, Audi, SEAT, Škoda and Cupra. SVM online coding, control unit replacement and software updates with ODIS.",
 "eyebrow": "VW · AUDI · SEAT · ŠKODA · CUPRA",
 "h1": "VAG online programming, done remotely",
 "lede": "Online coding and programming for Volkswagen, Audi, SEAT, Škoda and Cupra with ODIS and the official SVM backend. Your car stays where it is, anywhere in the world.",
 "short": "SVM online coding, module replacement and software updates.",
 "keywords": ["VAG online programming", "SVM online coding", "ODIS online", "remote ECU coding"],
 "body": """
<h2>What is VAG online programming?</h2>
<p>Many control units in modern Volkswagen Group cars can't be fully set up offline. After a module is replaced, or when a software update is due, the car has to talk to the manufacturer's server. The server checks the vehicle's installation list and sends back the correct software and coding. VAG calls this <strong>SVM (Software Version Management)</strong>.</p>
<p>Skip that step and you get the classic symptoms: "not coded" or "software version incorrect" faults, missing functions, warning lights that won't clear, and a module that works only halfway.</p>

<h2>What I do</h2>
<ul>
<li>SVM online coding after a control unit is replaced, new or used</li>
<li>Software and flash updates for control units, including technical service updates</li>
<li>Online parameterisation after retrofits (lights, assistance systems, infotainment)</li>
<li>Installation list and gateway updates when equipment changes</li>
<li>Adaptations and basic settings after the job</li>
<li>Full scan before and after, so you see the result in black and white</li>
</ul>

<h2>Typical jobs</h2>
<ul>
<li>Replaced instrument cluster, infotainment unit or gateway</li>
<li>Matrix or LED headlight control units after an accident repair</li>
<li>Retrofitted ACC, lane assist, park assist or reversing camera</li>
<li>Engine or gearbox control unit software updates</li>
<li>Used parts from another car that need to be married to yours</li>
</ul>

<h2>Supported platforms and models</h2>
<p>MQB, MQB Evo, MLB Evo, MEB and many PQ-based cars. That covers models like the Golf 7 and 8, Passat B8, Tiguan, T-Roc, Arteon, ID. models, Audi A3, A4, A5, A6, A7, A8, Q3, Q5, Q7 and Q8, Škoda Octavia, Superb and Kodiaq, SEAT Leon and Ateca, and Cupra Formentor and Born.</p>
<p>Cars built for different markets (EU, UK, North America, Gulf/GCC, Asia) carry different software. <strong>Send your VIN first</strong> and I'll confirm exactly what's possible on your car before you pay anything.</p>

<h2>What you need at the car</h2>
<p>A Windows laptop with a stable internet connection, a supported diagnostic interface (such as a VAS 6154 or a J2534 pass-thru) and a battery charger that holds the voltage between 13.0 and 14.0 V during flashing. Not sure about your equipment? Ask in the chat and I'll tell you what fits.</p>
""",
 "faq": [
  ("Do I need to take the car to a dealer?", "No. The job runs remotely. You connect the interface and laptop at the car and I do the programming over the internet."),
  ("Do I need my own ODIS license?", "No. I run the job with my own licensed access. You only need the hardware at the car, and I'll tell you exactly which."),
  ("Can you program cars from the US or the Middle East?", "Yes, in most cases. Market-specific software is checked against your VIN before we start."),
  ("What happens if the connection drops?", "That's why we check voltage and internet before the first write. If a step fails, the module is recovered in the same session."),
 ],
 "related": ["component-protection", "carplay-activation", "remote-diagnostics"],
},
CP,
{
 "slug": "lamborghini-online-programming",
 "nav": "Lamborghini Online Programming",
 "chat": "Lamborghini Online Programming",
 "title": "Lamborghini Online Programming & Coding | autocodeRHX",
 "desc": "Remote Lamborghini online programming for Huracán, Urus and Aventador. Control unit replacement, software updates and coding without a dealer visit.",
 "eyebrow": "HURACÁN · URUS · AVENTADOR",
 "h1": "Lamborghini online programming",
 "lede": "Control unit replacement, software updates and coding for Lamborghini, done remotely. No trailer to the nearest dealer, no week-long wait for a slot.",
 "short": "Module replacement, software updates and coding for Lamborghini.",
 "keywords": ["Lamborghini online programming", "Lamborghini coding", "Huracán programming", "Urus coding"],
 "body": """
<h2>Why Lamborghini programming is different</h2>
<p>Modern Lamborghinis share a lot of electronics with the Audi and Volkswagen Group, but programming them needs Lamborghini-specific online access. A generic VAG tool can read faults, yet it can't finish the job when a module needs online coding or a software update from the factory server.</p>
<p>For many owners and independent specialists the nearest authorised dealer is hours away. Remote online programming brings that dealer-level access to the car instead.</p>

<h2>What I do</h2>
<ul>
<li>Online coding after a control unit is replaced</li>
<li>Software updates for control units</li>
<li>Coding and adaptation after accident or electrical repairs</li>
<li>Fault diagnosis with a full scan of every module</li>
<li>Support for independent workshops that work on Lamborghini</li>
</ul>

<h2>Models</h2>
<p>Huracán (including EVO, STO and Tecnica), Urus and Aventador. Older models and other variants on request. Every car is checked by VIN before the job, so you know what's possible up front.</p>

<h2>How a Lamborghini session works</h2>
<p>You or your workshop connect a laptop, a supported interface and a battery charger at the car. I connect remotely, check the vehicle, and run the programming while you watch. At the end you get a clean fault memory and a short report of what was changed.</p>
""",
 "faq": [
  ("Can this be done outside Europe?", "Yes. Sessions run worldwide, including the Middle East, North America and Asia. The car stays where it is."),
  ("I'm an independent workshop. Can you support my technicians?", "Yes. Many jobs are for specialists who have the car on the lift but not the online access."),
  ("What equipment do I need?", "A Windows laptop, a supported diagnostic interface, a stable internet connection and a battery charger. I confirm the exact setup before the session."),
  ("How much does it cost?", "It depends on the model and the job. Send the VIN and a short description for a fixed quote."),
 ],
 "related": ["bentley-online-programming", "vag-online-programming", "remote-diagnostics"],
},
{
 "slug": "bentley-online-programming",
 "nav": "Bentley Online Programming",
 "chat": "Bentley Online Programming",
 "title": "Bentley Online Programming & Coding | autocodeRHX",
 "desc": "Remote Bentley online programming for Continental GT, Bentayga and Flying Spur. Control unit coding, software updates and diagnostics, worldwide.",
 "eyebrow": "CONTINENTAL GT · BENTAYGA · FLYING SPUR",
 "h1": "Bentley online programming",
 "lede": "Online coding, software updates and diagnostics for Bentley, done remotely by an automotive engineer. For owners and independent specialists worldwide.",
 "short": "Control unit coding, software updates and diagnostics for Bentley.",
 "keywords": ["Bentley online programming", "Bentley coding", "Bentayga programming", "Continental GT coding"],
 "body": """
<h2>Dealer-level programming for Bentley, without the dealer</h2>
<p>Current Bentleys are built on Volkswagen Group platforms: the Bentayga on MLB Evo, the third-generation Continental GT and Flying Spur on MSB. Their control units need Bentley online access for coding and software updates after a replacement or repair.</p>
<p>That access usually sits only at authorised dealers. autocodeRHX makes it available remotely, so your car or your customer's car can be finished where it already is.</p>

<h2>What I do</h2>
<ul>
<li>Online coding after a new or used control unit is fitted</li>
<li>Control unit software updates</li>
<li>Adaptations and basic settings after repairs</li>
<li>Full-system scan and fault diagnosis</li>
<li>Remote support for workshops that service Bentley</li>
</ul>

<h2>Models</h2>
<p>Continental GT and GTC, Bentayga and Flying Spur. Earlier generations on request. Send the VIN and I'll confirm what can be done.</p>

<h2>Before the session</h2>
<p>Bentley electrical systems draw a lot of current with the ignition on. A strong battery charger that holds the voltage between 13.0 and 14.0 V is essential during programming. Add a Windows laptop, a supported interface and a stable internet connection.</p>
""",
 "faq": [
  ("Is this the same as VAG programming?", "The platform is shared, but Bentley control units need Bentley-specific online access. I have the right setup for both."),
  ("Do you work with workshops in the Gulf and the US?", "Yes. Sessions are booked in your local time."),
  ("Can you help with a used module from another car?", "Often yes. Send the part number and your VIN and I'll check before we start."),
  ("How do I get a quote?", "Use the chat on this page. It prepares a WhatsApp message with your car, VIN and the job."),
 ],
 "related": ["lamborghini-online-programming", "vag-online-programming", "wiring-diagrams"],
},
PORSCHE,
MERCEDES,
BMW,
{
 "slug": "carplay-activation",
 "nav": "CarPlay Activation",
 "chat": "CarPlay / Android Auto Activation",
 "title": "CarPlay & Android Auto Activation (VAG) | autocodeRHX",
 "desc": "Activate Apple CarPlay and Android Auto on your existing VW, Audi, SEAT, Škoda or Cupra head unit. Remote App-Connect activation with a VIN check first.",
 "eyebrow": "MIB2 · MIB2.5 · MIB3",
 "h1": "CarPlay and Android Auto activation",
 "lede": "Switch on Apple CarPlay and Android Auto in the head unit your car already has. No new hardware, no dongle. Done remotely after a free VIN check.",
 "short": "App-Connect switched on in your existing head unit.",
 "keywords": ["CarPlay activation", "Android Auto activation", "App-Connect activation", "MIB3 CarPlay"],
 "body": """
<h2>Your car may already have it</h2>
<p>Many Volkswagen, Audi, SEAT, Škoda and Cupra models left the factory with a head unit that can run Apple CarPlay and Android Auto, but with the feature switched off. VAG calls the function <strong>App-Connect</strong>. If your unit has the right hardware and software, it can be activated remotely.</p>

<h2>What you get</h2>
<ul>
<li>Apple CarPlay and Android Auto on your existing screen</li>
<li>Wireless connection where your head unit's hardware supports it</li>
<li>Steering wheel buttons and voice control working as from the factory</li>
<li>No adapters, no aftermarket boxes, no visible changes to the car</li>
</ul>

<h2>Which cars are supported?</h2>
<p>It depends on the head unit: MIB2, MIB2.5 and MIB3 systems in models like the Golf 7 and 8, Passat, Tiguan, Polo, Audi A3, A4 and Q5, Škoda Octavia and Superb, SEAT Leon and Cupra Formentor. Not every unit can be activated, so <strong>I check your VIN and software version first</strong>. If yours isn't compatible, you'll know before you pay.</p>
<p>Driving a BMW or Mercedes? See <a href="../bmw-coding/">BMW coding</a> and <a href="../mercedes-coding/">Mercedes-Benz coding</a> for CarPlay on those brands.</p>

<h2>How it works</h2>
<p>Send your VIN through the chat. I confirm compatibility and send a quote. In the session you connect a laptop and interface, I activate App-Connect remotely and we test it with your phone before finishing.</p>
""",
 "faq": [
  ("Will I get wireless CarPlay?", "If your head unit's hardware supports wireless, yes. Otherwise CarPlay and Android Auto run over USB."),
  ("Does it work in cars from any country?", "In most markets, yes. Market and software version are checked by VIN before we start."),
  ("What if a dealer updates the head unit later?", "The activation is stored in the unit. If anything changes after a dealer visit, message me and I'll check it."),
  ("Is a VIN check free?", "Yes. You only pay once compatibility is confirmed and you book the activation."),
 ],
 "related": ["vag-online-programming", "remote-diagnostics", "diagnostic-software-licenses"],
},
{
 "slug": "diagnostic-software-licenses",
 "nav": "Diagnostic Software Licenses",
 "chat": "Diagnostic Software License",
 "title": "Genuine Diagnostic Software Licenses | autocodeRHX",
 "desc": "Help choosing and setting up genuine, licensed diagnostic software: ODIS, PIWIS, XENTRY and VCDS. No cracked tools. Remote installation worldwide.",
 "eyebrow": "ODIS · PIWIS · XENTRY · VCDS",
 "h1": "Genuine diagnostic software licenses",
 "lede": "The right official software for your brands and budget, installed and working on your laptop. Legal licenses only, for workshops and enthusiasts.",
 "short": "Choosing, buying and installing the right official software.",
 "keywords": ["ODIS license", "XENTRY license", "PIWIS subscription", "genuine diagnostic software"],
 "body": """
<h2>Why genuine software matters</h2>
<p>Cracked diagnostic software is everywhere, and it causes real damage: failed flashes that leave modules dead, malware on workshop laptops, no access to online functions, and legal risk for your business. autocodeRHX works only with legally licensed software.</p>
<p>In the EU, type-approval rules (Regulation (EU) 2018/858) require manufacturers to give independent operators access to repair and maintenance information. Many brands sell time-based access through their official repair-information portals, and professional aftermarket tools add multi-brand coverage. Picking the right mix is where most people waste money.</p>

<h2>What I help with</h2>
<ul>
<li>Choosing between OEM access and professional multi-brand tools for your brands</li>
<li>Getting the right official license or subscription</li>
<li>Choosing a compatible interface (VAS 6154, J2534 pass-thru, brand-specific VCIs)</li>
<li>Remote installation, drivers and configuration on your Windows laptop</li>
<li>A first guided job so you know the workflow</li>
</ul>

<h2>Already have a subscription?</h2>
<p>Many workshops pay for OEM access but get stuck on a specific job: a flash that won't start, an SVM error, a coding step that keeps failing. I can connect remotely and run the job with you, step by step, using your own license.</p>

<h2>Software I work with</h2>
<p><strong>ODIS</strong> for Volkswagen Group brands, <strong>PIWIS</strong> for Porsche, <strong>XENTRY</strong> for Mercedes-Benz and <strong>VCDS</strong> for fast VAG diagnostics and coding.</p>
""",
 "faq": [
  ("Do you sell cracked or 'lifetime' software?", "No. Only genuine, licensed software. Cracked tools are unreliable and can destroy control units."),
  ("Can you install software on my laptop remotely?", "Yes. You give me remote access, I install and configure everything and test it with your interface."),
  ("Which license should a small independent workshop start with?", "It depends on the brands you see most. Message me with your typical cars and I'll suggest a setup."),
  ("Can you help me use my own ODIS or XENTRY?", "Yes. I can guide or run jobs with your license over a remote session."),
 ],
 "related": ["vag-online-programming", "porsche-programming", "remote-diagnostics"],
},
{
 "slug": "wiring-diagrams",
 "nav": "Wiring Diagrams",
 "chat": "Wiring Diagrams",
 "title": "Wiring Diagrams & Pinouts for Your Car | autocodeRHX",
 "desc": "Current flow diagrams for VW, Audi, Porsche, Mercedes, Bentley and Lamborghini: connector pinouts, wire colours, fuse and ground locations, per VIN.",
 "eyebrow": "STROMLAUFPLÄNE · PINOUTS",
 "h1": "Wiring diagrams for your exact car",
 "lede": "Current flow diagrams with connector pinouts, wire colours, fuses and ground points, matched to your VIN. Delivered as PDF.",
 "short": "Current flow diagrams, pinouts, fuses and grounds per VIN.",
 "keywords": ["car wiring diagram", "VAG wiring diagram", "Stromlaufplan", "connector pinout"],
 "body": """
<h2>What you get</h2>
<ul>
<li>Current flow diagrams for the circuit you're working on</li>
<li>Connector views with pin assignments</li>
<li>Wire colours and cross-sections</li>
<li>Fuse and relay positions</li>
<li>Ground points and component locations</li>
</ul>
<p>Diagrams are matched to your VIN, because the same model can be wired differently depending on equipment and model year.</p>

<h2>Reading German wire colour codes</h2>
<p>Volkswagen Group diagrams use German abbreviations for wire colours. Here are the ones you'll see most:</p>
<div class="spec" style="margin:0 0 1.4rem">
<div class="spec-row"><span>sw</span><strong>black (schwarz)</strong></div>
<div class="spec-row"><span>ws</span><strong>white (weiß)</strong></div>
<div class="spec-row"><span>rt</span><strong>red (rot)</strong></div>
<div class="spec-row"><span>br</span><strong>brown (braun)</strong></div>
<div class="spec-row"><span>gn</span><strong>green (grün)</strong></div>
<div class="spec-row"><span>bl</span><strong>blue (blau)</strong></div>
<div class="spec-row"><span>gr</span><strong>grey (grau)</strong></div>
<div class="spec-row"><span>li</span><strong>lilac (lila)</strong></div>
<div class="spec-row"><span>ge</span><strong>yellow (gelb)</strong></div>
<div class="spec-row"><span>or</span><strong>orange</strong></div>
<div class="spec-row"><span>rs</span><strong>pink (rosa)</strong></div>
</div>
<p>A wire marked <strong>rt/sw</strong> is red with a black stripe. Brown wires are almost always ground.</p>

<h2>Need help using the diagram?</h2>
<p>A diagram shows where things are; finding the fault is the next step. With <a href="../remote-diagnostics/">remote diagnostics and wiring analysis</a> I guide your measurements live: voltage drop, shorts to ground, open circuits and CAN bus checks.</p>
""",
 "faq": [
  ("Which brands do you have diagrams for?", "Volkswagen, Audi, SEAT, Škoda, Cupra, Porsche, Mercedes-Benz, Bentley and Lamborghini. Other brands on request."),
  ("How do I receive the diagram?", "As a PDF over WhatsApp, usually after I confirm your VIN and the circuit you need."),
  ("Can I get the full wiring manual for my car?", "Tell me what you're working on and I'll send what you need for that job."),
  ("Do you help interpret the diagram?", "Yes. Guided wiring analysis is available as a remote session."),
 ],
 "related": ["remote-diagnostics", "vag-online-programming", "porsche-programming"],
},
{
 "slug": "remote-diagnostics",
 "nav": "Remote Diagnostics",
 "chat": "Remote Diagnostics",
 "title": "Remote Car Diagnostics & Wiring Analysis | autocodeRHX",
 "desc": "Remote diagnostics for VAG, Porsche, Mercedes, Bentley and Lamborghini. Full scan, fault codes explained and guided fault finding for electrical faults.",
 "eyebrow": "FULL SCAN · FAULT FINDING",
 "h1": "Remote diagnostics and wiring analysis",
 "lede": "For faults a code reader can't explain: no-starts, immobiliser problems, network errors and electrical shorts. Diagnosed remotely, with a clear plan at the end.",
 "short": "Full scan, fault codes explained and guided fault finding.",
 "keywords": ["remote car diagnostics", "electrical fault finding", "no start diagnosis", "CAN bus fault"],
 "body": """
<h2>When remote diagnostics makes sense</h2>
<ul>
<li>No-start or crank-no-start conditions</li>
<li>Immobiliser and key recognition problems</li>
<li>Many fault codes at once across several modules</li>
<li>CAN or LIN communication faults</li>
<li>Shorts to ground and intermittent electrical faults</li>
<li>Warning lights that come back after every clear</li>
</ul>

<h2>How I work through a fault</h2>
<p>Every session starts with a full scan of all control units and a look at freeze-frame and live data. Then I compare what the car reports with the wiring diagram and the component's expected behaviour. Where measurements are needed, I guide you live: which pin, which value to expect, and what the reading means.</p>

<h2 id="wiring">Wiring analysis and component testing</h2>
<p>Electrical faults often hide behind misleading codes. A single blown fuse on a shared supply line can make five modules report shorts at the same time. A control unit from another car can leave immobiliser data empty. Guided measurements find the real cause instead of replacing parts until the light goes out.</p>
<ul>
<li>Voltage drop and supply checks</li>
<li>Short-to-ground and open-circuit tracing</li>
<li>CAN bus resistance and signal checks</li>
<li>Component tests against expected values</li>
</ul>

<h2>What you get at the end</h2>
<p>A clear explanation of the fault, what to check or replace, and if needed the coding or programming to finish the repair, all in the same place.</p>
""",
 "faq": [
  ("What do I need for remote diagnostics?", "A Windows laptop, a diagnostic interface, internet at the car and ideally a multimeter for measurements."),
  ("Which brands do you diagnose?", "Volkswagen Group brands, Porsche, Mercedes-Benz, Bentley and Lamborghini. Other brands on request."),
  ("Can you fix the fault remotely too?", "If the fix is coding, programming or adaptation, yes. If a part or wire is faulty, I tell you exactly which."),
  ("Do I get a report?", "Yes, a short summary of findings and next steps."),
 ],
 "related": ["wiring-diagrams", "mercedes-coding", "bmw-coding"],
},
]
