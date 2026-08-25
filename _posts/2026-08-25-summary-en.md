---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 36 items, 16 important content pieces were selected

---

1. [Microsoft Paint and Photos Embed Invisible GUID Watermarks in AI-Edited Images](#item-1) ⭐️ 8.0/10
2. [Interactive Moon Article by Bartosz Ciechanowski Explains Lunar Geometry and Phases](#item-2) ⭐️ 8.0/10
3. [EU Packaging Rules Threaten Small Makers and Micro-Entrepreneurs, Discussion Reveals Exemptions](#item-3) ⭐️ 8.0/10
4. [Oceans Hit Highest Temperature on Record](#item-4) ⭐️ 8.0/10
5. [seL4 security proofs are now complete on AArch64](#item-5) ⭐️ 8.0/10
6. [Anthropic’s Best AI Model Struggles to Attract Users as Cheaper Tools Thrive](#item-6) ⭐️ 8.0/10
7. [Apple Keeps iCloud+ Hide My Email on icloud.com Domain](#item-7) ⭐️ 7.0/10
8. [Xiaomi XRING O3's ARM C1-Ultra CPU matches Apple single-core, but not custom](#item-8) ⭐️ 7.0/10
9. [San Francisco as an explorable web-based video game](#item-9) ⭐️ 7.0/10
10. [Jabber/XMPP Marks 25 Years of Digital Independence](#item-10) ⭐️ 7.0/10
11. [IPFS Maintainer Team Shipyard Winding Down, Project Continues](#item-11) ⭐️ 7.0/10
12. [SQLite Database File Becomes a Linux Executable via binfmt_misc](#item-12) ⭐️ 7.0/10
13. [Drew Breunig on Fable's High Cost Reshaping Coding Harness Strategies](#item-13) ⭐️ 7.0/10
14. [Using AI as a Spatial Software Generator to Create Programmable 3D Objects](#item-14) ⭐️ 7.0/10
15. [Delay-Corrected Bellman Operator with Causal Attribution for Constrained RL](#item-15) ⭐️ 7.0/10
16. [Unbounded Labs Releases Bart: A 2.82B LLM Trained on Pre-1931 English](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Microsoft Paint and Photos Embed Invisible GUID Watermarks in AI-Edited Images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Microsoft's MS Paint and Photos applications invisibly embed a unique GUID watermark into images that have been modified with AI features, including when using local models. The watermark cannot be disabled and is added silently without user notification. This practice can compromise user anonymity and privacy, as each image contains a unique identifier that could be linked to a Microsoft account through legal requests or data leaks. It raises concerns about consent and trust in widely used consumer software, especially as AI editing becomes more common. The invisible watermark is a GUID embedded in image metadata or pixel data; visible watermarks can be turned off, but the invisible one cannot be disabled and appears even with local AI processing. The implementation appears tied to AI-manipulated images, though the exact scope (e.g., background removal) remains unclear.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: A GUID (Globally Unique Identifier) is a 128-bit identifier used to uniquely tag data; Microsoft commonly uses GUIDs in its systems, making them linkable as persistent IDs. Invisible digital watermarking is a technique that embeds information imperceptibly into an image, often for authenticity and tracking. In this case, the watermark is added only to AI-modified images and is separate from any visible markup.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GUID">GUID</a></li>
<li><a href="https://www.imatag.com/digital-watermarking">Invisible Digital Watermarking | The smart way to protect your online...</a></li>

</ul>
</details>

**Discussion**: Commenters largely expressed concern over the privacy implications, with several arguing that the invisible unique identifier is the real issue rather than AI itself. Some pointed out that a copyright subpoena to Microsoft could reveal personal account data tied to a GUID, undermining online anonymity. Others shared anecdotes of Microsoft's sloppy implementations, such as a false Copilot watermark on Azure DevOps commits, and one user reported a false positive trigger.

**Tags**: `#privacy`, `#watermarking`, `#microsoft`, `#ai`, `#reverse engineering`

---

<a id="item-2"></a>
## [Interactive Moon Article by Bartosz Ciechanowski Explains Lunar Geometry and Phases](https://ciechanow.ski/moon/) ⭐️ 8.0/10

Bartosz Ciechanowski published "Moon" (2024), an interactive web article that uses dynamic, detailed illustrations to explain lunar geometry, phases, and visual phenomena. It has been praised as a standard for interactive educational content on the web. This article showcases how deeply interactive, browser-based visualizations can make complex astronomical concepts intuitive, influencing modern web design and educational content. Its style is seen as a benchmark that AI-assisted development is helping to popularize. The page covers the Moon's geometry and phases with perspectives including a virtual planet, though one commenter noted the absence of a table of contents. The author is known for highly detailed, dynamic JavaScript illustrations, and a related December 2024 post drew 250 comments.

hackernews · simonebrunozzi · Aug 24, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49426466)

**Background**: Bartosz Ciechanowski is known for long-form interactive explainers that combine physics, math, and engineering with rich animations. Lunar phases result from the changing relative positions of the Sun, Earth, and Moon, and visual phenomena such as libration or apparent size variation are often unintuitive without spatial visualization. This article uses interactive diagrams to make those relationships easier to grasp.

**Discussion**: Commenters praised Ciechanowski's style as a benchmark for interactive pages, with one noting AI-assisted development is making such pages the norm. Some discussed adding a table of contents and the ethics of imitating his style, while a moderator linked a previous December 2024 thread with 250 comments. Overall sentiment was admiration and appreciation for the educational impact.

**Tags**: `#interactive visualization`, `#astronomy`, `#web development`, `#education`, `#data visualization`

---

<a id="item-3"></a>
## [EU Packaging Rules Threaten Small Makers and Micro-Entrepreneurs, Discussion Reveals Exemptions](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) ⭐️ 8.0/10

A viral article argues that upcoming EU packaging regulations (PPWR) will impose heavy burdens on micro-entrepreneurs, but commenters counter that micro-enterprises using generic packaging are exempt. Small makers and micro-entrepreneurs are a significant part of the maker economy, and regulatory burden can stifle innovation and cross-border e-commerce; clarifying exemptions is crucial for compliance. The EU FAQ referenced in comments states that rules do not apply to micro-enterprises or generic packaging; member states initially resisted a single registry, and the EU advises not to enforce until a correction is enacted.

hackernews · l-one-lone · Aug 24, 13:05 · [Discussion](https://news.ycombinator.com/item?id=49419237)

**Background**: PPWR is an EU regulation aiming to reduce packaging waste by setting requirements for packaging design, reuse, and recycling, replacing the Packaging and Packaging Waste Directive. Small businesses often worry about compliance costs, but EU law may include exemptions for micro-enterprises. The discussion highlights how EU directives are implemented differently across member states.

**Discussion**: Comments are mixed: some argue the author misunderstood exemptions, citing the EU FAQ; others point to real regulatory fragmentation and burden, noting member states torpedoed a central registry and now blame the EU. A commenter compares China's approach of regulating large platforms rather than small businesses.

**Tags**: `#EU regulations`, `#micro-entrepreneurs`, `#makers`, `#packaging`, `#small business`

---

<a id="item-4"></a>
## [Oceans Hit Highest Temperature on Record](https://www.bbc.com/news/articles/c62m4gpnp78o) ⭐️ 8.0/10

The BBC reports that global ocean temperatures have reached their highest level on record. This new milestone underscores the accelerating impact of climate change. Warmer oceans can intensify extreme weather, including stronger El Niño events, and threaten marine ecosystems and coastal communities. This record highlights the urgent need for stronger climate policies and emissions reductions. The exact temperature anomaly and dataset are not specified in the summary, but commenters note that fossil fuels still accounted for 81.1% of global energy in 2023, only slightly down from 81.4% in 2000. Another comment explains that melting ice absorbs a large amount of heat (80 calories per gram) before ocean temperatures can rise further.

hackernews · tcp_handshaker · Aug 24, 19:19 · [Discussion](https://news.ycombinator.com/item?id=49424606)

**Background**: Global ocean temperatures are monitored using satellite and buoy measurements. Small average increases represent enormous heat uptake because water has a high heat capacity. Warmer oceans can alter weather patterns, for example by strengthening El Niño, which affects rainfall and storms in many regions. Climate scientists often use ocean heat content as a key indicator of global warming.

**Discussion**: Commenters expressed concern and frustration, linking the record to government inaction and criticizing the US for expanding fossil fuel extraction. Some highlighted that renewables growth has barely reduced fossil fuel's share of global energy, while others explained the physics of ice melt absorbing heat. Several shared videos from BBC, DW, and science YouTuber Anton Petrov for further context.

**Tags**: `#climate-change`, `#environment`, `#ocean`, `#global-warming`, `#sustainability`

---

<a id="item-5"></a>
## [seL4 security proofs are now complete on AArch64](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

The seL4 microkernel now has complete formal security proofs for the AArch64 (ARM64) architecture. These proofs currently apply only to non-MCS unicore configurations, meaning mixed-criticality systems and multicore configurations are not covered. This is a significant milestone in formal verification and OS security, strengthening confidence in seL4 for high-assurance embedded and defense systems that use Arm processors. It may also encourage broader adoption in automotive, aerospace, and other safety-critical domains. The proofs cover functional correctness and security properties of seL4 on 64-bit ARM, but only for the non-mixed-criticality (non-MCS) unicore configuration; multicore and MCS variants remain unverified. As with most OS-kernel formal proofs, the result validates abstract specifications and does not by itself eliminate hardware side-channel timing attacks.

hackernews · snvzz · Aug 24, 11:32 · [Discussion](https://news.ycombinator.com/item?id=49418255)

**Background**: seL4 is a formally verified microkernel from the L4 family, meaning its implementation has been mathematically proven to satisfy a specification of isolation and capability-based security. Formal verification uses mathematical proof rather than testing to establish correctness. AArch64 is Arm's 64-bit architecture used in smartphones, servers, and embedded devices. In seL4, MCS refers to mixed-criticality system support, and the current proofs cover only a single-core (unicore) configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://sel4.systems/">The seL 4 Microkernel | seL 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://en.wikipedia.org/wiki/AArch64">AArch64</a></li>

</ul>
</details>

**Discussion**: Community reaction is cautious: one commenter predicts a side-channel timing attack could invalidate the result, while others emphasize the 'non-MCS, unicore' fine print. There is also interest in real-world seL4 deployments (such as GenodeOS, LionsOS, and automotive hypervisor use) and debate over whether seL4 needs a native Linux-compatible environment to honestly improve system security.

**Tags**: `#seL4`, `#formal verification`, `#security`, `#AArch64`, `#microkernel`

---

<a id="item-6"></a>
## [Anthropic’s Best AI Model Struggles to Attract Users as Cheaper Tools Thrive](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 8.0/10

According to Financial Times reporting from people with knowledge, Anthropic's annualized revenue reached $65 billion in July, up from $47 billion in May, and the company expects Q3 to be profitable. OpenAI's annualized revenue surpassed $40 billion after a 35% jump in the quarter to date, boosted by the July launch of GPT-5.6. The data highlights intensifying competition in the AI model market, where high-end models like Anthropic's Fable 5 face adoption challenges due to cost, while cheaper alternatives gain share. It also shows how rapidly revenue can scale in the AI sector, influencing investor expectations and product strategy. Ramp's billing data from 70,000 companies shows Opus 4.8 accounted for 28.0% of Anthropic model spend in July, while Fable 5 had 8.0% and Opus 5 just 3.5% after its July 24 release. Anthropic also told investors it has 6,000 customers spending at least $100,000 annually.

rss · Simon Willison · Aug 23, 20:24

**Background**: The Ramp AI Index measures AI adoption and spend using transaction data from over 70,000 companies on Ramp's corporate card and bill-pay platform. Annualized revenue extrapolates a period's revenue to a full year, allowing month-to-month comparisons. Anthropic's Claude models are offered in tiers such as Opus, Sonnet, and Haiku, with Opus generally being the most capable and expensive; Fable 5 appears to be a newer high-cost model.

<details><summary>References</summary>
<ul>
<li><a href="https://ramp.com/data/ai-index">Ramp AI Index</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#Anthropic`, `#OpenAI`, `#revenue`, `#business strategy`

---

<a id="item-7"></a>
## [Apple Keeps iCloud+ Hide My Email on icloud.com Domain](https://developer.apple.com/news/?id=1ptvdtcm) ⭐️ 7.0/10

Apple announced that iCloud+ Hide My Email addresses will remain on the icloud.com domain, rather than moving to a separate or disposable-looking domain, addressing user concerns about deliverability. Keeping Hide My Email on the same domain as normal iCloud addresses makes generated addresses appear legitimate, reducing the chance that services block them as disposable emails and improving inbox delivery for privacy-conscious users. Hide My Email generates unique, random addresses that forward to a user's personal inbox; the trade-off is stronger lock-in to Apple's iCloud ecosystem, but commenters note this same-domain approach is necessary and rare among providers.

hackernews · K7PJP · Aug 24, 22:13 · [Discussion](https://news.ycombinator.com/item?id=49426564)

**Background**: iCloud+ is Apple's paid subscription tier that includes privacy features like Hide My Email. Hide My Email lets users create random, unique email addresses that forward to their real inbox, often when signing up for websites or using Sign in with Apple. Email services sometimes block addresses from domains that are known mainly for disposable or relay addresses, which can hurt deliverability. By keeping these addresses on the widely used icloud.com domain, they blend in with ordinary iCloud mail and are less likely to be blocked.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/en-us/105078">How to use Hide My Email with Sign in with Apple - Apple Support</a></li>
<li><a href="https://eshop.macsales.com/blog/78718-how-to-use-hide-my-email-in-macos-monterey/?APC=XLR8YourMac13">How to Use Hide My Email in MacOS Monterey</a></li>
<li><a href="https://en.wikipedia.org/wiki/Email_deliverability">Email deliverability</a></li>

</ul>
</details>

**Discussion**: Comments are largely positive: kqp calls it a huge selling point and argues that using the same domain as normal addresses is the only lasting solution, with Fastmail as the only other provider doing this. Some note the trade-off of Apple lock-in, but agree the approach works for users; others wish Sign in with Apple were easier to set up for personal blogs.

**Tags**: `#Apple`, `#privacy`, `#email`, `#iCloud`, `#Hide My Email`

---

<a id="item-8"></a>
## [Xiaomi XRING O3's ARM C1-Ultra CPU matches Apple single-core, but not custom](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

Xiaomi's XRING O3 SoC, built around ARM C1-Ultra CPU cores clocked up to 4.35 GHz, was discussed on Hacker News with a claim that its single-thread performance matches Apple's cores while offering much higher multithreaded scores. Commenters clarified that the CPU is an ARM-designed C1-Ultra configuration, not a fully custom Xiaomi design. This shows Xiaomi can produce a flagship-class ARM SoC comparable to MediaTek's Dimensity 9500, increasing competition for MediaTek and Qualcomm in smartphones. However, the single-thread 'match' is against Apple's previous-generation M5, and power efficiency per watt remains untested, so Apple is not dethroned. Community-reported benchmarks put the XRING O3 at Geekbench 3,945 single-core and 15,221 multi-core, versus M5 iPad's 3,556 and 15,285, with the Xiaomi chip using 10 cores to Apple's 6. The SoC uses 100% ARM-design CPU cores (two C1-Ultra at 4.35 GHz, four C1-Premium at 3.68 GHz, plus four more), and Xiaomi's additions are bus interconnects, TSMC 3nm physical implementation, an in-house NPU, and LPDDR6 support.

hackernews · tosh · Aug 24, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49420873)

**Background**: ARM designs CPU core IP such as the C1-Ultra, which phone makers can license and integrate into a system-on-chip; this is different from Apple's approach of using the ARM instruction set but designing its own custom cores. The ARM C1-Ultra belongs to the Armv9.3 C-series introduced in 2025 and is also used in MediaTek's Dimensity 9500. Xiaomi's XRING O3 is a mobile SoC built around these ARM cores, not a custom microarchitecture.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_C-series">ARM C-series - Wikipedia</a></li>
<li><a href="https://www.geeknetic.es/Noticia/39848/Xiaomi-desvela-su-SoC-XRING-03-con-nucleos-ARM-C1-y-LPDDR6.html">Xiaomi desvela su SoC XRING 03 con núcleos ARM C1 y LPDDR6</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is skeptical of the 'matches Apple' claim. Commenters note the chip is an ARM design, not Xiaomi-custom; that multithreaded gains come from 10 cores versus 6; and that power efficiency per watt is the missing metric. Some see the real significance as Xiaomi's ability to build a MediaTek-class chip, which could pressure Qualcomm and MediaTek.

**Tags**: `#hardware`, `#mobile`, `#ARM`, `#semiconductors`, `#Xiaomi`

---

<a id="item-9"></a>
## [San Francisco as an explorable web-based video game](https://sf.thijs.gg/) ⭐️ 7.0/10

A developer created a web-based explorable 3D simulation of San Francisco using map data, allowing users to navigate the city in a browser. The project attracted significant attention, scoring 356 points and 121 comments on Hacker News. It demonstrates how publicly available map data can be turned into immersive, explorable 3D environments without traditional game engines, lowering the barrier for geographic visualization and creative projects. This could inspire similar city-scale simulations for urban planning, tourism, or gaming. The simulation appears to be built by reverse-engineering Apple Maps flyover data and uses WebGL for rendering in the browser. Community members note the underlying retroplasma code may be outdated and doesn't handle Apple's newer HEIF texture format, and the current version lacks street names, landmarks, and address search.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: WebGL is a JavaScript API that enables GPU-accelerated 3D graphics directly in web browsers without plugins. 3D reconstruction or mapping involves capturing the shape and appearance of real-world objects, often from aerial imagery or map data. Apple Maps flyover provides 3D city models, and developers have reverse-engineered its data for custom projects, allowing entire cities to be rendered interactively on a web page.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGL">WebGL</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_mapping">3D mapping</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is enthusiastic, with users praising the project and sharing emotional reactions—one commenter who lived in San Francisco for nearly 20 years said it made them emotional walking around familiar spots. Several users discussed technical details, noting it may use reverse-engineered Apple Maps data, and suggested improvements such as street names, landmarks, address search, higher-resolution local downloads, and live MMO elements. A user also linked a similar N64-style Seattle project.

**Tags**: `#3D mapping`, `#city simulation`, `#webgl`, `#san francisco`, `#game development`

---

<a id="item-10"></a>
## [Jabber/XMPP Marks 25 Years of Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 7.0/10

The article commemorates the 25th anniversary of Jabber/XMPP, reflecting on its legacy as a decentralized, open-standard instant messaging protocol and its continued use in modern projects. XMPP's federated, email-like architecture allows anyone to run their own server and interoperate across providers, offering an alternative to centralized messaging silos. Its ongoing adoption in telephony bridges, self-hosted servers, and autonomous agents shows the protocol remains relevant for privacy-conscious and decentralized applications. Community comments highlight current XMPP usage: jmp.chat for SMS/telephony bridging with Dino and Cheogram clients, Prosody and ejabberd servers, and agent communication built on XMPP clients like Fluux. The retrospective itself notes no major new protocol changes, and some users observe XMPP is less publicly visible than during its peak when Facebook and Google Chat supported it.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP (originally named Jabber) is an open XML-based protocol for instant messaging, presence, and contact lists, formalized as a standard in 2004. Its architecture is federated like email: anyone can run an XMPP server, users have Jabber IDs similar to email addresses, and there is no central authority. Major platforms such as Google and Facebook once used XMPP for their messaging services. Today the protocol continues to be developed with extensions by the XMPP Standards Foundation and is implemented in many free and open-source clients and servers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XMPP_protocol">XMPP protocol</a></li>
<li><a href="https://xmpp.org/about/technology-overview/">An Overview of XMPP | XMPP - The universal messaging standard</a></li>

</ul>
</details>

**Discussion**: The community is largely positive and nostalgic, with users sharing real-world deployments such as Google Voice migration to jmp.chat, self-hosted Prosody servers, and XMPP-based agent communication. Some lament that Matrix received substantial funding instead of XMPP, while one commenter questions whether large XMPP communities still exist outside niche use cases.

**Tags**: `#XMPP`, `#Jabber`, `#messaging`, `#decentralization`, `#open standards`

---

<a id="item-11"></a>
## [IPFS Maintainer Team Shipyard Winding Down, Project Continues](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

Shipyard, a team that maintained IPFS implementations, announced it is winding down. The broader IPFS project is not shutting down and will continue through individual maintainer grants. This marks a shift from centralized team-based maintenance to individual grants for IPFS, which could affect development velocity, governance, and long-term sustainability of a key decentralized-web protocol. The sunset applies only to Shipyard, one of several IPFS implementation maintainers; the IPFS project itself continues. Community members noted the announcement was misleading and pointed to alternative projects such as Iroh.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**Background**: IPFS (InterPlanetary File System) is a peer-to-peer protocol that uses content addressing to share files without a central server, created by Protocol Labs, which also developed Filecoin. Maintainers like Shipyard develop and support IPFS implementations. The project has faced challenges such as Cloudflare dropping IPFS support and criticisms of IPNS direction.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IPFS">IPFS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Protocol_Labs">Protocol Labs</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is mixed: sadness and concern, but also clarification that IPFS is not dead. Some commenters recommend Iroh as a more sustainable p2p alternative and criticize Protocol Labs' priorities, while others lament past decisions around IPNS and note the irony of using a Google form for feedback on decentralization.

**Tags**: `#IPFS`, `#decentralized web`, `#open source sustainability`, `#Protocol Labs`, `#maintainership`

---

<a id="item-12"></a>
## [SQLite Database File Becomes a Linux Executable via binfmt_misc](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria presents a technique where a SQLite database file is also a valid Linux executable by setting the SQLite application ID to 'SELF' (at offset 68) and storing ELF components in SQLite tables, with a `self-exec` interpreter extracting and executing them; `binfmt_misc` can associate the magic pattern with that interpreter. This demonstrates unusual flexibility in Linux binary handling and could enable creative packaging, polyglot files, or new ways to distribute executables and data together; it also illustrates how `binfmt_misc` can extend the kernel's executable format recognition beyond standard ELF. The SQLite application ID at offset 68 is set to ASCII 'SELF' (0x53454c46) to create the magic bytes; the ELF sections, segments, or equivalent are placed in SQLite tables defined by a schema, and registration via `/proc/sys/fs/binfmt_misc/register` uses a rule such as `:self:M:68:SELF::/usr/local/bin/self-exec:`.

rss · Simon Willison · Aug 24, 11:38

**Background**: ELF (Executable and Linkable Format) is the standard Linux binary format; the kernel normally recognizes it by an ELF header. SQLite database files begin with a 16-byte header containing an application ID at offset 68, which is normally used to identify an application's file format. `binfmt_misc` is a Linux kernel feature that lets arbitrary file formats be recognized by magic bytes and passed to a user-space interpreter. The technique exploits these facts by embedding ELF-like structures inside SQLite tables and teaching the kernel to hand the file to `self-exec`.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Binfmt_misc">Binfmt misc</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">Your executable is a SQLite database | Farid Zakaria’s Blog</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#SQLite`, `#ELF`, `#executable`, `#binfmt_misc`

---

<a id="item-13"></a>
## [Drew Breunig on Fable's High Cost Reshaping Coding Harness Strategies](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 7.0/10

Drew Breunig writes that after the Fable model's release, its high cost made it too expensive for every coding task, prompting his team to focus on optimizing coding harnesses and context strategies and to decide which work goes to which model. This reflects a shift from assuming ever-cheaper frontier models will solve problems automatically to engineering explicitly around model economics and routing; it affects how AI coding tools are built and how teams budget for LLM usage. Fable 5 is Anthropic's highest-scoring model on FrontierBench and excels at long-horizon reasoning, but it is costly; Breunig notes Opus, 5.6, K3, and GLM are still good enough for most code.

rss · Simon Willison · Aug 23, 19:55

**Background**: Fable is Anthropic's frontier coding model, the latest in the Claude family. A coding harness is the surrounding software that gives a coding agent access to files, tools, and workflows, while context strategies determine what code and instructions are packed into the model's limited context window. Prior to Fable, many teams could rely on periodic model upgrades at similar or lower prices; Fable's high price breaks that pattern.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://martinfowler.com/articles/harness-engineering.html">Harness engineering for coding agent users</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#LLM economics`, `#software engineering`

---

<a id="item-14"></a>
## [Using AI as a Spatial Software Generator to Create Programmable 3D Objects](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

The paper introduces a method that uses large language models to generate 3D objects as programmable spatial software rather than static meshes, with demonstrations on nova3d.xyz showing animation-ready, hierarchical, and adaptive assets. This approach could disrupt industrial design, game development, simulations, and AR/VR/XR by producing 3D assets that are inherently editable and adaptive from inception, unlike traditional monolithic mesh outputs. Generated objects are composed of logical parts with hinge/socket articulation and can include logic to adapt to weak or powerful compute environments; however, the approach currently lags behind traditional AI 3D generators for complex organic shapes.

reddit · r/MachineLearning · /u/mhb_11 · Aug 24, 19:10

**Background**: Traditional AI 3D generators typically output monolithic mesh blobs that require additional rigging and editing. In contrast, representing 3D objects as software code allows them to carry structure, hierarchy, and behavior from the start. Nova3D is an open-source client for editable, part-aware 3D generation from text or reference images.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/RareSense/Nova3D">GitHub - RareSense/Nova3D: Editable, part-aware 3D generation from text or reference images. Open-source client for nova3d.xyz. · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#3D Generation`, `#LLM`, `#Spatial Programming`, `#Computer Graphics`

---

<a id="item-15"></a>
## [Delay-Corrected Bellman Operator with Causal Attribution for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

A new approach called CCPL (Causal Consequence-Penalized Learning) introduces a delay-corrected Bellman operator with an adaptive effective discount learned from the consequence-delay distribution, plus an Interventional Consequence Net pretrained on structural-causal-model labels to attribute causal responsibility instead of temporal proximity. The authors provide a contraction proof under unknown stochastic delay. This addresses a major failure mode in constrained RL where delayed and stochastic violations are misattributed, which is common in real-world safety-critical settings. By formally grounding attribution in causal structure, it could improve safe policy learning beyond benchmark environments, though the current need for a structural causal model limits immediate applicability. The delay-corrected Bellman operator uses an adaptive effective discount learned from the consequence-delay distribution, and the contraction proof holds under unknown stochastic delay. A key limitation is that the Interventional Consequence Net requires access to the environment's structural causal model to generate pretraining labels, and is not learned end-to-end from observational or interventional data alone.

reddit · r/MachineLearning · /u/No_Cauliflower7923 · Aug 24, 12:11

**Background**: Constrained reinforcement learning optimizes a reward while satisfying constraints, often safety constraints. Bellman operators are contraction mappings used in dynamic programming and reinforcement learning to converge to optimal value functions; a standard operator assumes that consequences of actions are immediate. Structural causal models (SCMs) formally encode causal mechanisms among variables and can generate counterfactual or interventional labels, but they are often unknown in real-world applications.

<details><summary>References</summary>
<ul>
<li><a href="https://web.stanford.edu/class/cme241/lecture_slides/BellmanOperators.pdf">Understanding (Exact) Dynamic Programming through Bellman ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Structural_causal_model">Structural causal model</a></li>
<li><a href="https://grokipedia.com/page/Constrained_Reinforcement_Learning">Constrained Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#causal inference`, `#constrained RL`, `#Bellman operator`, `#stochastic delay`

---

<a id="item-16"></a>
## [Unbounded Labs Releases Bart: A 2.82B LLM Trained on Pre-1931 English](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 6.0/10

Unbounded Labs has released Bart, a 2.82B parameter LLM trained from scratch on 20.1B tokens of pre-1931 English text, complete with a live demo, a technical article, and a Hugging Face model. The team also built Vintage CORE, a suite of 20 benchmarks for vintage LLMs, and released a 416k supervised fine-tuning dataset of pre-1930s grounded Q&A pairs. This niche project explores whether LLMs can generate original scientific or intellectual ideas from historical corpora, and it openly shares datasets, benchmarks, and methodology that could advance research on domain-specific and vintage language models. It also demonstrates that a small team can train a competent model with modest compute and careful data curation. The model was trained on 20.1B tokens after cleaning Harvard's Institutional Books from 242B to 23B tokens. The team ran 10 hours of autonomous research on one H100, executing 100 experiments and finding 26 improvements, and trained the final model in 5 days on an H100 at 60% MFU for about $807 total.

reddit · r/MachineLearning · /u/soggydoggy8 · Aug 24, 17:20

**Background**: An ablation study removes a component of a system to measure that component's contribution. Supervised fine-tuning adapts a pretrained model using labeled input-output examples, while post-training refers to additional training after the initial pretraining stage. MFU (Model FLOPs Utilization) measures how efficiently a training run uses the GPU's theoretical compute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ablation_(artificial_intelligence)">Ablation (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://nebius.com/blog/posts/fine-tuning/supervised-fine-tuning">What is supervised fine - tuning in LLMs? Unveiling the process</a></li>
<li><a href="https://www.understandingai.org/p/nathan-lambert-on-the-rise-of-thinking">Nathan Lambert on the rise of "thinking" language models</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#NLP`, `#historical corpus`, `#open source`, `#AI research`

---