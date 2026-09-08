---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 33 items, 23 important content pieces were selected

---

1. [TALA, the Advanced Layout Engine for D2, Is Now Open Source](#item-1) ⭐️ 8.0/10
2. [Jellyfin 12.0 Major Release Delivers Smooth Upgrades](#item-2) ⭐️ 8.0/10
3. [Broadcom Pulls VDDK Downloads, Complicating VMware Exit and Third-Party Tools](#item-3) ⭐️ 8.0/10
4. [Video Exposes LG Smart TVs Logging Audio and Scanning Devices](#item-4) ⭐️ 8.0/10
5. [OpenAI shares internal data on coding agents accelerating research](#item-5) ⭐️ 8.0/10
6. [Yandex Research Proposes KV Cache as an Agent Runtime](#item-6) ⭐️ 8.0/10
7. [Longitudinal benchmarking detects LLM performance drift in 31,352 repeated measurements](#item-7) ⭐️ 8.0/10
8. [Factoring a 1990s Certificate Authority's 512-bit RSA Key on a Consumer GPU in Two Days](#item-8) ⭐️ 7.0/10
9. [Crawler Abuse Wastes CPU on git.kernel.org Commit Rendering](#item-9) ⭐️ 7.0/10
10. [DNS Abuse Crisis: Up to 20% of New gTLD Domains Are Scams](#item-10) ⭐️ 7.0/10
11. [Tiny 417k-param RNN Generates Full Bad Apple Video from Single Hidden State](#item-11) ⭐️ 7.0/10
12. [Rustuna: Official High-Performance Rust Implementation of Optuna](#item-12) ⭐️ 7.0/10
13. [LLM-Guided Program Evolution Improves 10 Best-Known Circle-Packing Solutions](#item-13) ⭐️ 7.0/10
14. [Reproducibility in ML Research: Is It Too Late?](#item-14) ⭐️ 7.0/10
15. [PINNStudio: Open-Source No-Code GUI for Physics-Informed Neural Networks](#item-15) ⭐️ 7.0/10
16. [Los Angeles Building Construction Visualization from 1880 to 2026](#item-16) ⭐️ 6.0/10
17. [llm CLI 0.35 Adds Support for OpenAI's GPT-6 Astra Model](#item-17) ⭐️ 6.0/10
18. [Quoting Jakub Pachocki](#item-18) ⭐️ 6.0/10
19. [Mercator ↔ Equal Earth](#item-19) ⭐️ 6.0/10
20. [There's No Limit to How Bad Code Can Get](#item-20) ⭐️ 6.0/10
21. [My lab found a way to migrate between embedding models with zero downtime. (R)](#item-21) ⭐️ 6.0/10
22. [I reduced image-processing token usage by ~95% compared with GPT-4o direct vision, while maintaining roughly the same accuracy.How significant is that?(P)](#item-22) ⭐️ 6.0/10
23. [What if competitive games (such as Rocket League) had a Stockfish-like accuracy system? (D)](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [TALA, the Advanced Layout Engine for D2, Is Now Open Source](https://d2lang.com/blog/tala-is-open-source/) ⭐️ 8.0/10

TALA (Terrastruct's AutoLayout Approach), a previously proprietary advanced layout engine for D2 diagrams, has been released as open source. The engine, built from scratch with zero dependencies for its algorithms, aims to provide better automatic layout for software architecture diagrams. Open-sourcing TALA removes a cost barrier for developers who need better auto-layout in D2; the default D2 layout can be poor for some graph types, and TALA often improves on alternatives like ELK. This makes higher-quality diagram generation more accessible and may encourage integration into other diagramming tools. According to the D2 documentation, TALA is a general orthogonal layout engine that is not restricted to hierarchies, trees, or radial layouts, and it can produce fundamentally non-hierarchical arrangements. Community comments note that TALA is at times a big improvement over ELK but may not be superior for every graph, as shown by a Go queue example.

hackernews · alixanderwang · Sep 7, 23:37 · [Discussion](https://news.ycombinator.com/item?id=49604150)

**Background**: D2 is a modern declarative diagram scripting language that turns text into diagrams. TALA is the layout engine developed by Terrastruct specifically for software architecture diagrams, handling the automatic arrangement of nodes and edges. ELK (Eclipse Layout Kernel) and Graphviz are commonly used layout engines that TALA is compared against in the discussion.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/terrastruct/TALA">GitHub - terrastruct/ TALA : A diagram layout engine designed...</a></li>
<li><a href="https://d2lang.com/tour/tala/">TALA | D2 Documentation</a></li>
<li><a href="https://github.com/d2lang/d2">GitHub - d2lang/d2: D2 is a modern diagram scripting language that turns text to diagrams. · GitHub</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is positive, with developers welcoming open-sourcing and expressing intent to integrate TALA into tools like Daedalus. Some users compare it favorably to ELK and Graphviz, noting that D2's default layout is poor but TALA can be a big improvement, though the previous proprietary license was a cost barrier. A few commenters raise concerns: one finds the Go queue example objectively worse, and another asks whether integrating it into Graphviz would be appropriate.

**Tags**: `#open-source`, `#diagramming`, `#layout-engine`, `#D2`, `#visualization`

---

<a id="item-2"></a>
## [Jellyfin 12.0 Major Release Delivers Smooth Upgrades](https://jellyfin.org/posts/jellyfin-release-12.0/) ⭐️ 8.0/10

Jellyfin 12.0, the latest major release of the free and open-source media server, has been released with notable improvements. Community members upgrading from older versions such as 10.10.7 report a quick and painless process, with only a library rescan needed to restore some missing titles. As a leading self-hosted alternative to Plex, Jellyfin's continued major releases strengthen its position for users seeking control and privacy over their media libraries. Positive upgrade experiences lower the barrier for Plex users considering a switch, potentially pressuring Plex to avoid user-hostile changes. Community upgrade reports mention that some titles may disappear after upgrading until a library rescan completes; the initial migration from older versions took only a few minutes even for a ~40TB library. The release follows 10.11 performance issues that had kept some users on 10.10.7.

hackernews · 0xC0ncord · Sep 8, 01:56 · [Discussion](https://news.ycombinator.com/item?id=49604861)

**Background**: Jellyfin is a free, open-source media server that lets users stream their own movies, TV shows, music, and other media to various devices without relying on a proprietary service. It began as a fork of Emby and is often compared to Plex, a commercial media server with subscription features and cloud dependencies. Jellyfin is volunteer-built and emphasizes privacy, no tracking, and full user control.

<details><summary>References</summary>
<ul>
<li><a href="https://jellyfin.org/">The Free Software Media System | Jellyfin</a></li>
<li><a href="https://github.com/jellyfin/jellyfin">GitHub - jellyfin/jellyfin: The Free Software Media System ...</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is positive, with former Plex users praising Jellyfin's progress as a viable fallback and noting smooth upgrades. Some users continue to report subtitle syncing/rendering issues on Android/Chromecast, calling subtitles Jellyfin's 'Achilles heel.' Others mention using Jellyfin alongside the *arr stack and AI tools for automated media management.

**Tags**: `#jellyfin`, `#media-server`, `#open-source`, `#software-release`, `#self-hosted`

---

<a id="item-3"></a>
## [Broadcom Pulls VDDK Downloads, Complicating VMware Exit and Third-Party Tools](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) ⭐️ 8.0/10

As of September 2026, Broadcom has removed publicly available downloads of the VMware Virtual Disk Development Kit (VDDK). User reports from Nutanix and Red Hat show VDDK links now return 404 errors, breaking access for backup and migration tools that depend on the kit. This change directly hinders organizations planning to migrate off VMware, as third-party backup, replication, and migration products rely on VDDK to read and write VMware virtual disks. It reinforces concerns that Broadcom is prioritizing revenue extraction over ecosystem openness, accelerating evaluation of alternatives like Proxmox, Hyper-V, and KVM. VDDK is the API toolkit that enables non-VMware software to access VMware virtual disk files. Nutanix Move and Red Hat Migration Toolkit for Virtualization both document required VDDK downloads, but users now encounter 404 pages, indicating the files are no longer publicly accessible without possibly new entitlement or licensing.

hackernews · josephcsible · Sep 7, 20:32 · [Discussion](https://news.ycombinator.com/item?id=49602699)

**Background**: VMware, acquired by Broadcom in November 2023, is a dominant enterprise virtualization platform. VDDK has long been used by backup vendors, replication tools, and migration utilities to integrate with VMware virtual machines. By restricting access to VDDK downloads, Broadcom makes it harder for third-party tools to operate, which is especially problematic for customers already locked into VMware environments.

<details><summary>References</summary>
<ul>
<li><a href="https://next.nutanix.com/ahv-virtualization-27/vsphere-vddk-download-for-nutanix-move-45855">vSphere VDDK Download for Nutanix Move | Nutanix Community</a></li>
<li><a href="https://access.redhat.com/solutions/7146995">Unable to download VMware VDDK images for Migration Toolkit for...</a></li>

</ul>
</details>

**Discussion**: Comments reflect a mix of nostalgia and frustration. An ex-VMware engineer laments Broadcom treating VMware as a declining asset to be milked, while others share migration experiences to Hyper-V, KVM, and Proxmox—one user found Proxmox migration surprisingly painless by mounting ESXi storage directly. Some suggest investing in KVM skills or even exfiltrating VMware source code as a future fallback, showing both practical advice and desperate humor.

**Tags**: `#VMware`, `#Broadcom`, `#Virtualization`, `#Enterprise IT`, `#Migration`

---

<a id="item-4"></a>
## [Video Exposes LG Smart TVs Logging Audio and Scanning Devices](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

A new video report exposes that LG smart TVs log audio even when the screen is off and scan local devices, potentially affecting 216 million units. This raises serious privacy and security concerns for consumers and IoT devices, highlighting how smart TV manufacturers may be collecting data without clear consent and could motivate regulatory action. The report notes the TVs snoop on local network devices; LG's terms reportedly require users to obtain consent from all third parties whose voices may be captured. Some users have disabled network functions to avoid data collection.

hackernews · treve · Sep 7, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49592375)

**Background**: Smart TVs often include microphones for voice commands and connect to home networks. Many manufacturers collect usage data for advertising and personalization, but such practices have drawn scrutiny when they happen without explicit user awareness. LG is a major TV brand with webOS-based smart TVs.

**Discussion**: Community reaction is largely critical, with users sharing personal stories of disabling network features and expressing concern over legality and the scope of data collection. Some commenters highlight LG's consent terms requiring users to notify guests, while others doubt that consumer backlash will force meaningful change.

**Tags**: `#privacy`, `#smart-tv`, `#security`, `#iot`, `#consumer-rights`

---

<a id="item-5"></a>
## [OpenAI shares internal data on coding agents accelerating research](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI published an internal view showing how its researchers use coding agents, with per-researcher spending on these agents rising from near zero in February 2026 to roughly $600 by late August. The company links this acceleration to recursive self-improvement (RSI), and the post coincides with a new essay by Chief Scientist Jakub Pachocki. This suggests OpenAI is seeing tangible productivity gains from agentic coding inside its own research team, which could accelerate AI development and serve as evidence for recursive self-improvement. If the trend continues, it may influence how other labs and companies adopt coding agents. The blog post includes a chart titled 'Coding agents are reshaping daily work for OpenAI researchers' with a y-axis of daily dollars per researcher; Simon Willison speculates the steep climb in late July corresponds to internal access to the model later released as GPT-6 Astra. OpenAI does not expand the RSI acronym in this post, and the companion essay is by Chief Scientist Jakub Pachocki.

rss · Simon Willison · Sep 6, 23:57

**Background**: Recursive self-improvement (RSI) is a hypothesized process in which an AI system iteratively improves its own code or capabilities, potentially leading to an intelligence explosion. Coding agents are AI tools that can write, debug, refactor, and deploy code with human oversight, moving beyond simple autocomplete. The term agentic engineering describes workflows where autonomous agents handle implementation while humans provide direction and validation, as discussed by IBM and others.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://agentic.ai/best/coding-agents">20 Best AI Coding Agents in 2026 — Agentic.ai</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#Research`, `#Coding Agents`, `#Recursive Self-Improvement`

---

<a id="item-6"></a>
## [Yandex Research Proposes KV Cache as an Agent Runtime](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

A research post from the Yandex team proposes modifying a model's KV cache as a new runtime design for more responsive LLM agents. It summarizes prior work such as Hogwild! Inference and AsyncReasoning, and previews a future Qwen3.8-27B agent playing DOOM interactively using these techniques. It highlights inference/runtime design as an underexplored axis for improving LLM agents, between changing the model and changing the harness. This could enable real-time voice assistants and embodied agents to respond and adapt without waiting for full sequential reasoning. Hogwild! Inference runs multiple copies of the same LLM in parallel with a shared attention cache, giving them immediate access to each other's memory. AsyncReasoning maintains two concurrent streams—a private thinker and a public writer—without fine-tuning; the post also shows a Qwen3.8-27B agent interacting with DOOM in real time.

reddit · r/MachineLearning · /u/_puhsu · Sep 7, 09:03

**Background**: In transformer-based LLMs, the KV cache stores key and value vectors from previous tokens so they do not have to be recomputed during autoregressive generation. Normally this cache is fixed once written, but these works modify or share it at runtime to support parallel or asynchronous generation. Existing agent systems typically treat inference as a black box, making the cache an interesting but overlooked control point.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.06261">[2504.06261] Hogwild! Inference: Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://arxiv.org/abs/2512.10931">[2512.10931] Asynchronous Reasoning: Training-Free ... AsyncReasoning/README.md at main · yandex-research ... - GitHub yandex-research/AsyncReasoning | DeepWiki Demos and Tutorials | yandex-research/AsyncReasoning | DeepWiki AsyncReasoning-1 | PDF | Thought | Computing - Scribd</a></li>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#LLM`, `#Agent Runtime`, `#KV Cache`

---

<a id="item-7"></a>
## [Longitudinal benchmarking detects LLM performance drift in 31,352 repeated measurements](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 8.0/10

A new longitudinal benchmarking methodology evaluates LLMs continuously rather than via one-time snapshots. An analysis of 31,352 repeated score observations across 49 models found between-day variation (SD 8.43) roughly three times larger than within-day variation (SD 2.80), prompting versioned benchmark configurations and change-point detection over time series. This matters because API-served LLMs can change without public version updates, so snapshot leaderboard scores may not reflect real-world behavior. Monitoring drift longitudinally helps practitioners detect regressions, availability issues, and contamination before they affect applications. The methodology compares only observations from compatible versioned benchmark configurations, uses execution-based evaluation instead of an LLM judge where possible, separates availability failures from valid task outcomes, and runs change detection on performance time series. It intentionally withholds the live task bank and some operational parameters to reduce contamination while publishing methodology in a PDF.

reddit · r/MachineLearning · /u/ionutvi · Sep 7, 07:44

**Background**: Most public LLM benchmarks evaluate a model once and publish a static score, but API providers may update model versions, infrastructure, or configurations without changing the public name. Longitudinal benchmarking repeatedly evaluates the same model over time to capture variation and detect drift. Model drift in LLM applications refers to behavior changes that can degrade performance, requiring continuous monitoring rather than one-time testing.

<details><summary>References</summary>
<ul>
<li><a href="https://stackpulsar.com/blog/llm-model-drift-detection/">LLM Model Drift Detection 2026: Monitoring AI Degradation</a></li>
<li><a href="https://orq.ai/blog/model-vs-data-drift">Understanding Model Drift and Data Drift in LLMs (2026 Guide)</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#benchmarking`, `#model drift`, `#longitudinal studies`, `#MLOps`

---

<a id="item-8"></a>
## [Factoring a 1990s Certificate Authority's 512-bit RSA Key on a Consumer GPU in Two Days](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 7.0/10

A researcher has reportedly factored the 512-bit RSA private key of a real 1990s Certificate Authority using consumer GPU hardware in about two days, demonstrating that such legacy keys are now within reach of an individual. This shows that 512-bit RSA is no longer safe even against hobbyist-level resources, and it highlights the risk that old encrypted traffic and still-trusted legacy systems could be retroactively decrypted as factoring becomes cheap. The factorization took about two days on a consumer GPU; to validate the key against a target from the era, the author needed a custom TLS implementation because modern Go crypto/tls no longer supports SSLv3, targeting Netscape Communicator 4.51 with its clock set to 2000. The author also cautions that some LLM-generated analysis of other keys was plausible but not fully verified.

hackernews · ahlCVA · Sep 8, 01:16 · [Discussion](https://news.ycombinator.com/item?id=49604637)

**Background**: RSA security relies on the difficulty of factoring large composite numbers. 512-bit RSA keys were common in the 1990s, but the first public factorization of a 512-bit RSA challenge number in 1999 took hundreds of computers and about seven months; by 2009 a desktop could factor one in 73 days. A certificate authority uses its private key to sign digital certificates, so a compromised CA key can allow impersonation of many websites. Today's consumer GPUs have made factoring such legacy keys a matter of days rather than months.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RSA_cryptosystem">RSA cryptosystem - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_numbers">RSA numbers - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_authority">Certificate authority</a></li>

</ul>
</details>

**Discussion**: Commenters are generally impressed and reflective: one notes that much 1990s traffic lacked ephemeral keys and wonders which governments might be storing old encrypted data for later decryption, while another asks how long people in the 90s expected this capability to take. Some criticism focuses on the author's use of LLM-generated analysis, with one commenter finding the explanation for the custom TLS implementation in the linked Go file after noting too many interesting details were left to AI.

**Tags**: `#cryptography`, `#RSA`, `#security`, `#factoring`, `#certificate-authority`

---

<a id="item-9"></a>
## [Crawler Abuse Wastes CPU on git.kernel.org Commit Rendering](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev reports that git.kernel.org now spends more CPU cycles rendering commits as HTML for scrapers than on all legitimate access combined, including git clones. Across its five geo-distributed nodes, 14 CPU cores are constantly busy doing nothing but rendering commits for crawlers. This shows how abusive crawlers place a heavy, hidden burden on public open-source infrastructure, potentially degrading performance for legitimate users and increasing operating costs. It also resonates with services like Datasette that expose many crawlable pages and may face similar abuse. The report states that at any one time, 14 CPU cores across 5 geo-distributed nodes are dedicated solely to rendering git commits as HTML for scrapers. This background radiation of abusive crawling outweighs all legitimate traffic, including git clones.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository for the Linux kernel, operated by the Linux Kernel Organization. Rendering a commit as HTML is a server-side operation used to display commits in a web browser; scrapers systematically request such pages, consuming disproportionate resources. Simon Willison's Datasette also serves a huge number of crawlable web pages, so he worries it may face similar abuse.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kernel.org/">The Linux Kernel Archives</a></li>
<li><a href="https://www.kernel.org/?lang=1">The Linux Kernel Archives</a></li>

</ul>
</details>

**Tags**: `#crawling`, `#git`, `#Linux kernel`, `#infrastructure`, `#web scraping`

---

<a id="item-10"></a>
## [DNS Abuse Crisis: Up to 20% of New gTLD Domains Are Scams](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

Terence Eden reports that, according to an Interisle report, 85 million new gTLD domains were registered in 2025, and 8.5 million of them were added to blocklists by May 2025, suggesting a scam rate between 10% and 20%. This indicates systemic abuse of DNS infrastructure, with roughly one in five newly registered gTLD domains potentially being scams, undermining trust in internet navigation and posing risks to users and businesses. The Interisle report (via Andrew Campling) sets a 10% abuse rate as the likely floor and says it is probably closer to 20%; ICANN has been discussing this problem for years, and there are now more than 1,200 gTLDs.

rss · Simon Willison · Sep 6, 14:40

**Background**: The Domain Name System (DNS) translates human-readable domain names into IP addresses. Generic top-level domains (gTLDs) such as .com, .net, and newer expansions are coordinated by ICANN. Interisle Consulting Group analyzes internet infrastructure and DNS abuse. The expansion of gTLDs has increased the number of available domain names, which criminals can exploit for scams.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GTLD">GTLD</a></li>
<li><a href="https://en.wikipedia.org/wiki/ICANN">ICANN</a></li>
<li><a href="https://interisle.net/">Interisle Consulting Group</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#cybersecurity`, `#scams`, `#internet infrastructure`, `#domain names`

---

<a id="item-11"></a>
## [Tiny 417k-param RNN Generates Full Bad Apple Video from Single Hidden State](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A 417,129-parameter recurrent dynamical system with an LSTM-style transition and depthwise-separable decoder was trained to generate the entire 6,500-frame, 384x512 Bad Apple video autonomously from a single 128-float initial state, without timestamp inputs. It uses learned latent teacher tables, a rollout horizon curriculum, and other stability techniques, and runs at over 200 FPS on an RTX 4080. This demonstrates that compact recurrent networks can learn a long, stable autonomous trajectory in latent space and decode it into coherent video, without external clock signals. It could inform generative video models, world models, and low-footprint media synthesis where continuous temporal dynamics are preferred over timestamp-conditioned functions. The model splits into a 4-gate LSTM-style transition (16,640 params), a 4-stage depthwise-separable decoder (400,361 params), and a 128-float initial state; it was trained only up to 512-frame horizons but generalizes to about 6,573 frames. Techniques include learned latent teacher tables, staged horizon doubling (2→512), Gaussian state noise, second-difference acceleration regularization, and separate optimizers (AdamW/Muon).

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: Bad Apple!! is a famous black-and-white shadow-art music video originating from the Touhou Project, widely used as a test pattern for demos and generative models because of its recognizable monochrome animation. The news references a prior SIREN MLP that memorized the video as an implicit coordinate function (t, y, x) → pixel; this new work instead learns a recurrent transition in latent space so no timestamp is needed at inference. Recurrent neural networks maintain hidden states that evolve over time, and training long autoregressive rollouts is difficult due to vanishing/exploding gradients and compounding errors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bad_Apple">Bad Apple - Wikipedia</a></li>
<li><a href="https://simple.wikipedia.org/wiki/Bad_Apple!!">Bad Apple!! - Simple English Wikipedia, the free encyclopedia</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#recurrent neural networks`, `#generative modeling`, `#dynamical systems`, `#video synthesis`

---

<a id="item-12"></a>
## [Rustuna: Official High-Performance Rust Implementation of Optuna](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 7.0/10

The Optuna organization released Rustuna, an official Rust implementation of the Optuna hyperparameter optimization framework. It offers a familiar API, zero Python dependencies, and lower memory footprint. Rustuna enables high-performance, memory-efficient hyperparameter optimization without Python dependencies, reducing supply chain risks for ML deployments. It broadens Optuna's ecosystem to Rust users and performance-sensitive environments. Rustuna is hosted at github.com/optuna/rustuna and is designed to keep Optuna's familiar API and concepts. The announcement highlights zero Python dependencies to mitigate supply chain attack risks and native Rust memory management for a lower memory footprint.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is an automatic hyperparameter optimization framework for machine learning, known for its define-by-run API that lets users construct search spaces dynamically. Hyperparameter optimization searches for the best model configurations, such as learning rate or layer sizes. Existing Optuna is primarily Python-based, which introduces dependency and performance overhead. Rust is a systems programming language valued for memory safety, speed, and small runtime footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://optuna.org/">Optuna - A hyperparameter optimization framework</a></li>
<li><a href="https://github.com/optuna/optuna">Optuna: A hyperparameter optimization framework - GitHub Optuna: A hyperparameter optimization framework — Optuna 4.9. ... Optuna: A hyperparameter optimization framework — Optuna 3.6. ... Optuna: A hyperparameter optimization framework - GitHub [1907.10902] Optuna: A Next-generation Hyperparameter ... Optuna | Proceedings of the 25th ACM SIGKDD International ...</a></li>
<li><a href="https://optuna.readthedocs.io/en/stable/index.html">Optuna: A hyperparameter optimization framework — Optuna 4.9. ...</a></li>

</ul>
</details>

**Tags**: `#rust`, `#optuna`, `#hyperparameter-optimization`, `#machine-learning`, `#software-release`

---

<a id="item-13"></a>
## [LLM-Guided Program Evolution Improves 10 Best-Known Circle-Packing Solutions](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 7.0/10

An LLM iteratively evolved an optimization algorithm, improving the best-known sum-of-radii for 10 circle-packing instances (N=101–114) by 2.4–5.4% in 15 iterations, with a total LLM cost of $27.72. Packomania independently verified and accepted the improved solutions. This shows that LLM-guided program evolution can discover better solutions on a benchmark with modest compute cost ($27.72) and independent verification, suggesting a scalable path for automated algorithm improvement in optimization and beyond. The system starts from a simple seed solver, uses an LLM to propose algorithmic changes guided by a scoreboard of results and history of prior attempts, and keeps only changes verified by an independent scorer. The author highlights the plateau-detection stopping rule as the piece most open to critique.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Packomania is a repository of benchmark instances for packing equal or unequal objects in containers, including the csqv family of circle-packing problems. Circle packing asks how to arrange circles of given radii inside a larger circle to maximize the sum of radii; best-known solutions are tracked on the site. LLM-guided program evolution is an emerging technique where a large language model iteratively proposes modifications to executable programs, which are then evaluated to guide further search.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.05093">LLM - Guided Program Evolution for Circle Packing:Breaking 10...</a></li>
<li><a href="https://packomania.com/">Packomania (52C17)</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Program Evolution`, `#Optimization`, `#Circle Packing`, `#Benchmark`

---

<a id="item-14"></a>
## [Reproducibility in ML Research: Is It Too Late?](https://www.reddit.com/r/MachineLearning/comments/1w92eis/reproducibility_seems_to_be_headed_towards/) ⭐️ 7.0/10

A Reddit discussion argues that reproducibility in machine learning research is becoming practically impossible due to three challenges: expensive physical AI setups, unverifiable industry claims, and selective demo presentations. This matters because reproducibility is a cornerstone of trustworthy scientific progress; if ML research becomes largely non-reproducible, it could undermine confidence in published results and hinder reliable innovation across academia and industry. The post highlights that physical AI experiments require costly hardware and specialized labs, industry performance claims cannot be verified without internal access, demos may be selectively edited, and authors may withhold code to protect competitive advantage.

reddit · r/MachineLearning · /u/NeighborhoodFatCat · Sep 6, 17:29

**Background**: Reproducibility means that independent researchers can repeat an experiment and obtain the same results, making it a basic standard of scientific research. Physical AI refers to AI systems that combine AI models with sensors, actuators, and robots to perceive and act in the physical world, unlike purely digital AI. Such research often depends on expensive equipment like robots, high-speed cameras, and dedicated laboratories, while large companies' internal research details are rarely disclosed, making external verification difficult.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physical_AI">Physical AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Physical_artificial_intelligence">Physical artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#machine learning`, `#research integrity`, `#AI ethics`, `#discussion`

---

<a id="item-15"></a>
## [PINNStudio: Open-Source No-Code GUI for Physics-Informed Neural Networks](https://www.reddit.com/r/MachineLearning/comments/1w9a2i7/pinnstudio_a_free_opensource_nocode_gui_for/) ⭐️ 7.0/10

PINNStudio, a free open-source no-code GUI, automates code generation for physics-informed neural networks, enabling users to define PDEs, domains, architectures, and training schedules through an interface instead of manual coding. It supports forward and inverse problems and is built on DeepXDE. It lowers the barrier for domain scientists and students with limited coding experience, addressing a common pain point in scientific machine learning by eliminating boilerplate code and accelerating PINN experimentation. The tool generates code on top of DeepXDE, streams training logs, and displays live loss curves and solution plots. It includes built-in templates for equations like Heat, Allen-Cahn, and Cahn-Hilliard, and supports coupled multi-output PDE systems and custom training schedules.

reddit · r/MachineLearning · /u/Impossible-Jello2749 · Sep 6, 22:19

**Background**: Physics-informed neural networks (PINNs) embed physical laws described by partial differential equations (PDEs) into the training of neural networks, acting as a regularizer to improve generalization, especially with limited data. PDEs are equations involving multivariable functions and their partial derivatives, central to modeling phenomena like heat, diffusion, and fluid dynamics. Inverse problems aim to infer unknown parameters from observed data, contrasting with forward problems that compute outputs from known causes. PINNStudio builds on DeepXDE, a library for PINNs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physics-informed_neural_networks">Physics-informed neural networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Partial_differential_equation">Partial differential equation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inverse_problem">Inverse problem</a></li>

</ul>
</details>

**Tags**: `#PINNs`, `#scientific machine learning`, `#open-source`, `#GUI tool`, `#physics-informed neural networks`

---

<a id="item-16"></a>
## [Los Angeles Building Construction Visualization from 1880 to 2026](https://lax-skyline.parcelscope.net/) ⭐️ 6.0/10

A new interactive visualization at lax-skyline.parcelscope.net uses county assessor parcel data to map the construction years of existing Los Angeles buildings from 1880 to 2026, letting users watch the city's built environment grow one building at a time. This visualization makes historical urban development patterns tangible, enabling discussion of zoning, housing supply, and transportation history. It also shows how data visualization can reveal long-term policy impacts such as downzoning. The underlying data comes from the Los Angeles County Assessor’s parcel portal; because it records only current buildings, demolished older structures (e.g., in Palms) are absent, so the map shows surviving building ages rather than a complete construction history. One commenter noted that a similar mobile visualization was built with Mapbox GL and vector tiles.

hackernews · rustywasm · Sep 7, 18:52 · [Discussion](https://news.ycombinator.com/item?id=49601655)

**Background**: Geographic information systems (GIS) store and visualize spatial data such as building footprints and construction dates. County assessor offices maintain parcel databases for property tax purposes, including the year built. Visualizing this data over time helps identify urban growth, zoning changes, and infill development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GIS">GIS</a></li>

</ul>
</details>

**Discussion**: Commenters largely praise the visualization but caution that it shows surviving buildings rather than all historical construction. Several highlight LA's downzoning in the 1980s as a cause of housing unaffordability, while others recall the city's former extensive streetcar network. One commenter notes a similar Mapbox GL implementation and describes the data processing pipeline.

**Tags**: `#data-visualization`, `#urban-planning`, `#los-angeles`, `#history`, `#gis`

---

<a id="item-17"></a>
## [llm CLI 0.35 Adds Support for OpenAI's GPT-6 Astra Model](https://simonwillison.net/2026/Sep/7/llm/) ⭐️ 6.0/10

Version 0.35 of Simon Willison's llm CLI adds support for OpenAI's new GPT-6 Astra model. Users can now select gpt-6-astra directly from the command line. This update lets developers and CLI users experiment with OpenAI's latest flagship reasoning model from their terminal, without writing custom API code. It reinforces llm's role as a unified interface for accessing cutting-edge models across many providers. The model identifier gpt-6-astra is added in llm 0.35. According to search results, GPT-6 Astra was released on September 3, 2026 and features a 1M-token context window, image understanding, and tool use.

rss · Simon Willison · Sep 7, 23:54

**Background**: llm is an open-source command-line tool and Python library created by Simon Willison for interacting with many large language models via remote APIs or local installations. GPT-6 Astra is OpenAI's flagship reasoning model, released in September 2026, with advanced capabilities such as a 1M-token context window. The 0.35 release is a minor update that simply registers the new model so llm users can select it.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://deepai.org/chat/gpt-6-astra">GPT - 6 Astra - DeepAI</a></li>

</ul>
</details>

**Tags**: `#openai`, `#llm`, `#gpt-6-astra`, `#release`

---

<a id="item-18"></a>
## [Quoting Jakub Pachocki](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 6.0/10

OpenAI's Chief Scientist argues for rapidly training smarter models to build defensive systems against AI dangers while warning against recklessness.

rss · Simon Willison · Sep 7, 22:26

**Tags**: `#ai-safety`, `#openai`, `#ai-ethics`, `#ai-policy`, `#ai-defense`

---

<a id="item-19"></a>
## [Mercator ↔ Equal Earth](https://simonwillison.net/2026/Sep/7/equal-earth/) ⭐️ 6.0/10

Simon Willison shares an interactive D3 tool that animates the transition between Mercator and Equal Earth map projections, inspired by a recent UN vote.

rss · Simon Willison · Sep 7, 16:24

**Tags**: `#geospatial`, `#map projection`, `#D3`, `#visualization`, `#Simon Willison`

---

<a id="item-20"></a>
## [There's No Limit to How Bad Code Can Get](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 6.0/10

Simon Willison argues that rewriting legacy systems from scratch rarely succeeds because the old system remains a moving target and its developers lack incentive to maintain it.

rss · Simon Willison · Sep 6, 09:08

**Tags**: `#software engineering`, `#technical debt`, `#legacy systems`, `#code quality`, `#refactoring`

---

<a id="item-21"></a>
## [My lab found a way to migrate between embedding models with zero downtime. (R)](https://www.reddit.com/r/MachineLearning/comments/1wabmm7/my_lab_found_a_way_to_migrate_between_embedding/) ⭐️ 6.0/10

A research lab proposes a zero-downtime migration method between embedding models using top-K retrieval from the old index and reranking with the new model, claiming comparable retrieval quality.

reddit · r/MachineLearning · /u/Potential_Low_1183 · Sep 8, 02:16

**Tags**: `#embedding models`, `#vector databases`, `#retrieval-augmented generation`, `#model migration`, `#information retrieval`

---

<a id="item-22"></a>
## [I reduced image-processing token usage by ~95% compared with GPT-4o direct vision, while maintaining roughly the same accuracy.How significant is that?(P)](https://www.reddit.com/r/MachineLearning/comments/1wab7ui/i_reduced_imageprocessing_token_usage_by_95/) ⭐️ 6.0/10

A Reddit user reports achieving approximately 95% lower image-processing token usage with similar accuracy to GPT-4o on a benchmark, but without sharing implementation details, seeking feedback on the significance of the result.

reddit · r/MachineLearning · /u/angelinusbread · Sep 8, 01:57

**Tags**: `#multimodal AI`, `#token reduction`, `#LLM efficiency`, `#VLM`, `#benchmark evaluation`

---

<a id="item-23"></a>
## [What if competitive games (such as Rocket League) had a Stockfish-like accuracy system? (D)](https://www.reddit.com/r/MachineLearning/comments/1wadyz7/what_if_competitive_games_such_as_rocket_league/) ⭐️ 6.0/10

A Reddit discussion proposes using offline reinforcement learning (Trajectory Transformers, Implicit Q-Learning) to build a Stockfish-like decision-quality evaluator for Rocket League, along with anti-cheat methods.

reddit · r/MachineLearning · /u/Ligras · Sep 8, 04:11

**Tags**: `#reinforcement-learning`, `#game-ai`, `#esports`, `#offline-rl`, `#machine-learning`

---