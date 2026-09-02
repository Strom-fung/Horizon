---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 38 items, 21 important content pieces were selected

---

1. [Anthropic Releases Claude Fable 5.1 and Mythos 5.1](#item-1) ⭐️ 9.0/10
2. [Dan Luu Evaluates Ed Zitron's AI Skeptic Predictions](#item-2) ⭐️ 8.0/10
3. [FBI Probes Service Selling 153 Million Driver's Licenses](#item-3) ⭐️ 8.0/10
4. [OpenAI's Path to Astra details critical cyber capabilities and safeguards](#item-4) ⭐️ 8.0/10
5. [Claude Fable 5.1 Made a Really Nice Animated Pelican](#item-5) ⭐️ 8.0/10
6. [Latent Reasoning Landscape in 2026: Mapping BDH-CQ, HRM/TRM, Coconut (D)](#item-6) ⭐️ 8.0/10
7. [Sliding-window attention beats linear on long-context reasoning (R)](#item-7) ⭐️ 8.0/10
8. [Introducing Ad Blocker for Firefox on iOS](#item-8) ⭐️ 7.0/10
9. [Codex bundles LibreOffice](#item-9) ⭐️ 7.0/10
10. [Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development](#item-10) ⭐️ 7.0/10
11. [The creator of Jujutsu has joined ERSC](#item-11) ⭐️ 7.0/10
12. [Python 3.15.0 candidate 2 is here!](#item-12) ⭐️ 7.0/10
13. [Introducing wrapture](#item-13) ⭐️ 7.0/10
14. [We released TontaubeV1, a character-level TTS model for long-form generation (P)](#item-14) ⭐️ 7.0/10
15. [EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses (R)](#item-15) ⭐️ 7.0/10
16. [My local model setup on an M4 Pro Mac Mini](#item-16) ⭐️ 6.0/10
17. [GeoJSON Map Viewer](#item-17) ⭐️ 6.0/10
18. [Quoting Tarn Adams](#item-18) ⭐️ 6.0/10
19. [datasette-mcp 0.2](#item-19) ⭐️ 6.0/10
20. [YOLO26-RGB: repurposing YOLO26's depth-trained backbone for image deraining (P)](#item-20) ⭐️ 6.0/10
21. [Cold emailing profs about PhD positions? Read this (D)](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Releases Claude Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic has released Claude Fable 5.1 and Claude Mythos 5.1, building on Fable 5 and Mythos 5 with a more natural writing style, better adherence to style instructions, and reduced cache read pricing from $1 to $0.25 per million tokens. The release also reports gains in agentic coding, long-running workflows, and trading intuition benchmarks. The cache read price cut to $0.25/M makes long-context agentic applications dramatically cheaper and signals competitive pressure on LLM pricing, while the writing improvements broaden the model's appeal for creative and content generation tasks. Cache read pricing dropped from $1/M to $0.25/M, making Fable 5.1 half the cost of Opus's cache read at $0.5/M; however, some users note that benchmark improvements appear concentrated in Terminal-Bench Science 0.1, with limited gains elsewhere. An Anthropic employee confirmed the writing style is less stereotypical and responds more reliably to style instructions, but said more work remains.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**Background**: Claude Fable 5 and Claude Mythos 5 were introduced in June 2026 as the first publicly available Mythos-class models; Fable 5 is a safeguarded version for general use, while Mythos 5 is restricted and has some safeguards lifted, but the underlying model is the same. Prompt caching is a technique that reuses previously seen input tokens at a discounted read price, and Anthropic typically charges cache reads at 0.1x the base input cost. The 5.1 versions are incremental updates to those models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://redis.io/blog/what-is-prompt-caching/">What Is Prompt Caching? LLM Speed & Cost Guide</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was extensive and largely technical. An Anthropic employee praised the writing style as more natural and reliable, while others benchmarked thinking effort levels and noted the cache price cut as a sign of pricing pressure. Some commenters were skeptical, arguing that Fable 5.1 shows limited gains outside a science benchmark and accusing Anthropic of nerfing Fable and using Mythos as a marketing strategy.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Model Release`, `#Creative Writing`

---

<a id="item-2"></a>
## [Dan Luu Evaluates Ed Zitron's AI Skeptic Predictions](https://danluu.com/zitron/) ⭐️ 8.0/10

Dan Luu published a detailed analysis evaluating the accuracy of Ed Zitron's AI skeptic predictions from 2024 and 2025, leading to an extensive Hacker News discussion with 645 comments and 563 points. The analysis matters because it examines the track record of a prominent AI critic, helping readers judge whether skeptical claims about the AI industry are grounded in evidence or rhetorical overreach amid intense AI hype. The critique focuses on the literal interpretation of Zitron's predictions, such as his use of 'dying' to describe companies, and argues that some numerical claims do not support his arguments; commenters debated whether his 'rot economy' framework changes the meaning.

hackernews · jatins · Sep 1, 18:35 · [Discussion](https://news.ycombinator.com/item?id=49526069)

**Background**: Ed Zitron is a technology commentator and podcaster known for his skeptical stance on the AI industry, often arguing that many AI products are overhyped and part of a 'rot economy.' Dan Luu is a software engineer and blogger recognized for rigorous, evidence-based analyses of technology and economics. The post examines Zitron's public predictions made during 2024 and 2025.

**Discussion**: The Hacker News discussion shows mixed reactions: some agree with Dan Luu's literal reading and find Zitron's arguments weak, while others argue that interpreting 'dying' within Zitron's broader 'rot economy' context is essential and that the critique overlooks this nuance; additionally, some commenters note that media pundits often prioritize visibility over accuracy.

**Tags**: `#AI`, `#AI skepticism`, `#prediction evaluation`, `#technology commentary`, `#debate`

---

<a id="item-3"></a>
## [FBI Probes Service Selling 153 Million Driver's Licenses](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 8.0/10

The FBI is investigating an online service that reportedly sold more than 153 million driver's license records, exposing massive amounts of personal information. This breach affects over 153 million people and exposes flaws in identity verification and data retention. It could lead to widespread identity theft and may pressure regulators to impose stricter liability on companies that store such data. The service retained 153,347,439 driver's license records instead of deleting them after verification, and verification may require front-and-back scans plus facial motion capture. No vendor name or exact breach method is specified in the available summary.

hackernews · tatersolid · Sep 1, 23:17 · [Discussion](https://news.ycombinator.com/item?id=49529621)

**Background**: Driver's license records typically contain full name, address, date of birth, photo, and license number—enough for identity theft or account takeover. Online identity verification services often ask users to upload front-and-back scans plus a live selfie to confirm the document is genuine. Data minimization is a privacy principle requiring companies to delete personal data once its purpose, such as verification, is fulfilled; retaining 153 million records violates this principle and creates a high-value target for attackers.

**Discussion**: Commenters are largely cynical and frustrated, noting that verification services retain sensitive IDs indefinitely even though they only need them briefly. Some advocate fixed per-person compensation and strict liability to force companies to minimize data, while others worry their IDs may have been exposed via marijuana dispensary checks or suspect voter suppression motives.

**Tags**: `#data breach`, `#privacy`, `#security`, `#identity verification`, `#FBI`

---

<a id="item-4"></a>
## [OpenAI's Path to Astra details critical cyber capabilities and safeguards](https://openai.com/index/path-to-astra/) ⭐️ 8.0/10

OpenAI announced that Astra is the first model to meet the Critical cybersecurity capability threshold under its Preparedness Framework, scoring 100% on the ExploitBench benchmark for developing exploits from known vulnerabilities. This sets a new benchmark for transparently disclosing dangerous AI capabilities and gating their release, influencing how frontier AI companies handle cybersecurity risk and national security concerns. It also fuels policy debate over who gets access to such powerful models and whether private control is acceptable. Astra achieved a perfect 100% on ExploitBench, a benchmark that evaluates a model's ability to develop exploits from known vulnerabilities, and is described as able to find previously unknown security flaws. OpenAI says it will release Astra with stronger safeguards and mechanisms using clear, objective criteria to avoid arbitrary access decisions.

hackernews · jithinraj · Sep 1, 20:20 · [Discussion](https://news.ycombinator.com/item?id=49527595)

**Background**: OpenAI's Preparedness Framework is a risk classification system that rates AI capabilities from low to Critical, with Critical indicating the highest level of concern for cybersecurity. Frontier models are the most advanced general-purpose AI systems developed by leading labs. ExploitBench is a benchmark for testing whether models can write working exploits from known vulnerabilities. AI alignment refers to steering AI systems toward human intended goals and values.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/path-to-astra/">Path to Astra: critical capabilities and frontier ... - OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/09/01/open-ai-astra-cyber-model.html">OpenAI says Astra AI model crosses 'Critical' cyber capability</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**Discussion**: Commenters are skeptical: some point out a contradiction between OpenAI's claim of objective access criteria and its recent restriction of users from 44 countries, while others question whether the capabilities are truly new or just harness engineering. Concerns are also raised about the HuggingFace hack, the need for alignment to be a top priority, and whether governments could compel OpenAI to hand over unguarded model weights for national security.

**Tags**: `#AI safety`, `#OpenAI`, `#cybersecurity`, `#frontier models`, `#alignment`

---

<a id="item-5"></a>
## [Claude Fable 5.1 Made a Really Nice Animated Pelican](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) ⭐️ 8.0/10

Anthropic released Claude Fable 5.1 and Claude Mythos 5.1 on September 1, 2026, claiming improved coding, knowledge work, and long-running problem-solving, including a 52.6% score on Terminal-Bench-Science 0.1 (up from 24.7% for Fable 5). Simon Willison then tested the model's ability to generate an SVG of a pelican riding a bicycle across its five reasoning effort levels and found it produced a really nice animated pelican. The jump from 24.7% to 52.6% on a newly introduced science benchmark suggests a meaningful advance for agentic coding and scientific research workloads, which could influence model selection by developers and researchers. At the same time, Willison's declining confidence in the informal pelican benchmark highlights growing uncertainty about whether current evaluation methods track real-world usefulness. Anthropic reports Fable 5.1 scored 52.6% on Terminal-Bench-Science 0.1 versus 24.7% for Fable 5, 29.0% for Opus 5, and 22.4% for GPT-5.6 Sol, and the model offers five reasoning levels (low, medium, high, xhigh, max) with no off switch. In the pelican SVG test, both low and medium modes appeared to skip reasoning entirely with roughly 2,000 output tokens, while high mode used 2,612 tokens and cost about 13.087 cents.

rss · Simon Willison · Sep 1, 23:57

**Background**: Claude Fable 5.1 is Anthropic's update to Claude Fable 5, a general-use "Mythos-class" model introduced in June 2026 with a matching restricted Claude Mythos model. Terminal-Bench-Science 0.1 is a continuous benchmark whose first release includes 70 tasks drawn from life, physical, Earth, mathematical, and other scientific domains. The pelican benchmark is an informal test created by Simon Willison in late 2024 that asks LLMs to generate an SVG of a pelican riding a bicycle.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://www.terminal-bench-science.ai/announcement">Terminal-Bench-Science 0.1</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) — Grokipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#benchmark`, `#coding`

---

<a id="item-6"></a>
## [Latent Reasoning Landscape in 2026: Mapping BDH-CQ, HRM/TRM, Coconut (D)](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 8.0/10

A survey of latent reasoning approaches that bypass token-level chain-of-thought by transforming continuous hidden states, categorizing families like Coconut and BDH-CQ/HRM/TRM.

reddit · r/MachineLearning · /u/Typical-Scene-5794 · Sep 1, 15:14

**Tags**: `#latent reasoning`, `#large language models`, `#chain-of-thought`, `#continuous thoughts`, `#AI research`

---

<a id="item-7"></a>
## [Sliding-window attention beats linear on long-context reasoning (R)](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

A new arXiv preprint claims that sliding window attention with sinks achieves 2-10 times higher performance than linear attention on long-context reasoning benchmarks without requiring post-training.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Aug 31, 16:35

**Tags**: `#machine learning`, `#natural language processing`, `#attention mechanisms`, `#transformers`, `#long-context`

---

<a id="item-8"></a>
## [Introducing Ad Blocker for Firefox on iOS](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/) ⭐️ 7.0/10

Mozilla introduces an ad blocker for Firefox on iOS, with community discussion highlighting limitations like not blocking search or YouTube ads and rollout delays.

hackernews · HieronymusBosch · Sep 1, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49521973)

**Tags**: `#Firefox`, `#iOS`, `#Ad Blocking`, `#Mozilla`, `#Web Browsing`

---

<a id="item-9"></a>
## [Codex bundles LibreOffice](https://simonwillison.net/2026/Sep/1/codex-libreoffice/) ⭐️ 7.0/10

Simon Willison discovers that the OpenAI Codex desktop app (now ChatGPT) bundles a full LibreOffice suite along with Python, Node.js, and other tools in its runtime cache.

rss · Simon Willison · Sep 1, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49527396)

**Tags**: `#software engineering`, `#ChatGPT`, `#LibreOffice`, `#desktop applications`, `#dependencies`

---

<a id="item-10"></a>
## [Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development](https://www.norirobotics.com/) ⭐️ 7.0/10

Nori Robotics launches a $1,688 bimanual mobile humanoid robot for developers, featuring 19 DOF and multiple sensors, generating discussion on its technical limitations and practical use.

hackernews · AntonioLi · Sep 1, 17:35 · [Discussion](https://news.ycombinator.com/item?id=49525153)

**Tags**: `#robotics`, `#humanoid robot`, `#startup`, `#hardware`, `#YC`

---

<a id="item-11"></a>
## [The creator of Jujutsu has joined ERSC](https://ersc.io/blog/martin-joins-ersc) ⭐️ 7.0/10

Martin von Zweigbergk, creator of the Jujutsu version control system, has joined ERSC, a company building next-generation code collaboration tools.

hackernews · steveklabnik · Sep 1, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49525297)

**Tags**: `#version control`, `#jujutsu`, `#ersc`, `#git`, `#open source`

---

<a id="item-12"></a>
## [Python 3.15.0 candidate 2 is here!](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 7.0/10

Python 3.15.0 release candidate 2 is available, with final release planned for October and maintainers urged to build and publish wheels.

rss · Simon Willison · Sep 1, 14:59

**Tags**: `#Python`, `#release candidate`, `#programming languages`, `#open source`, `#software development`

---

<a id="item-13"></a>
## [Introducing wrapture](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Graham Dumpleton introduces Wrapture, a Python library that extends his wrapt monkeypatching ideas to enable both testing overrides and tracing of function calls without modifying original code.

rss · Simon Willison · Aug 31, 23:59

**Tags**: `#python`, `#testing`, `#monkeypatching`, `#tracing`, `#debugging`

---

<a id="item-14"></a>
## [We released TontaubeV1, a character-level TTS model for long-form generation (P)](https://www.reddit.com/r/MachineLearning/comments/1w4afjn/we_released_tontaubev1_a_characterlevel_tts_model/) ⭐️ 7.0/10

Released TontaubeV1, a 2.9B-parameter open-weight character-level TTS model for expressive long-form speech generation with zero-shot voice cloning.

reddit · r/MachineLearning · /u/EAVDR · Sep 1, 12:23

**Tags**: `#text-to-speech`, `#machine learning`, `#open-source model`, `#audio generation`, `#character-level tokenization`

---

<a id="item-15"></a>
## [EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses (R)](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 7.0/10

EvoUndo provides a framework for representing, verifying, and recovering from self-modifications in LLM agents, significantly improving recoverability over baseline methods.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Sep 1, 19:17

**Tags**: `#LLM Agents`, `#Self-Evolution`, `#Recoverability`, `#AI Safety`, `#Formal Verification`

---

<a id="item-16"></a>
## [My local model setup on an M4 Pro Mac Mini](https://lws.io/blog/my-local-model-setup/) ⭐️ 6.0/10

A user shares their local model setup on an M4 Pro Mac Mini, sparking discussion about performance, hardware limitations, and alternatives like GPU clouds.

hackernews · raybb · Sep 1, 22:30 · [Discussion](https://news.ycombinator.com/item?id=49529132)

**Tags**: `#local-llm`, `#apple-silicon`, `#hardware`, `#inference-performance`, `#community-discussion`

---

<a id="item-17"></a>
## [GeoJSON Map Viewer](https://simonwillison.net/2026/Sep/1/geojson/) ⭐️ 6.0/10

Simon Willison shares a GeoJSON map viewer tool he built with AI assistance for displaying and exporting geographic data.

rss · Simon Willison · Sep 1, 18:05

**Tags**: `#geojson`, `#map-viewer`, `#ai-assisted-development`, `#tools`

---

<a id="item-18"></a>
## [Quoting Tarn Adams](https://simonwillison.net/2026/Sep/1/tarn-adams/) ⭐️ 6.0/10

Tarn Adams jokes about having to call Dwarf Fortress's AI 'behavior' due to industry pressures, commenting on AI hype and CEO behavior.

rss · Simon Willison · Sep 1, 17:01

**Tags**: `#ai`, `#game-design`, `#terminology`, `#industry-commentary`, `#dwarf-fortress`

---

<a id="item-19"></a>
## [datasette-mcp 0.2](https://simonwillison.net/2026/Sep/1/datasette-mcp/) ⭐️ 6.0/10

datasette-mcp 0.2 is the first non-alpha release that changes SQL result rows to objects for better LLM handling and updates the MCP dependency.

rss · Simon Willison · Sep 1, 15:30

**Tags**: `#datasette`, `#mcp`, `#model-context-protocol`, `#sql`, `#llm`

---

<a id="item-20"></a>
## [YOLO26-RGB: repurposing YOLO26's depth-trained backbone for image deraining (P)](https://www.reddit.com/r/MachineLearning/comments/1w4fxln/yolo26rgb_repurposing_yolo26s_depthtrained/) ⭐️ 6.0/10

The author explores transferring YOLO26's depth-estimation backbone to image deraining, finding it beneficial compared to training from scratch.

reddit · r/MachineLearning · /u/Naive-Explanation940 · Sep 1, 15:52

**Tags**: `#image deraining`, `#transfer learning`, `#YOLO`, `#computer vision`, `#deep learning`

---

<a id="item-21"></a>
## [Cold emailing profs about PhD positions? Read this (D)](https://www.reddit.com/r/MachineLearning/comments/1w3bwci/cold_emailing_profs_about_phd_positions_read_this/) ⭐️ 6.0/10

A professor shares advice for prospective PhD students on how to effectively cold email potential supervisors, emphasizing brevity, specificity, and alignment of research interests.

reddit · r/MachineLearning · /u/tariban · Aug 31, 12:09

**Tags**: `#PhD admissions`, `#academic advice`, `#cold emailing`, `#machine learning`, `#research career`

---