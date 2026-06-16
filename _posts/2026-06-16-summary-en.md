---
layout: default
title: "Horizon Summary: 2026-06-16 (EN)"
date: 2026-06-16
lang: en
---

> From 45 items, 21 important content pieces were selected

---

1. [Backdoor in LinkedIn Job Offer via npm Script](#item-1) ⭐️ 9.0/10
2. [x86 Emulator Team Patched Buggy Code During Emulation](#item-2) ⭐️ 8.0/10
3. [John Carmack Praises Fabrice Bellard's Technical Genius](#item-3) ⭐️ 8.0/10
4. [Iroh 1.0: P2P Networking with Dial Keys, Not IPs](#item-4) ⭐️ 8.0/10
5. [Why AI Won't Replace Software Engineers](#item-5) ⭐️ 8.0/10
6. [LLMs Have Model-Specific Name Priors](#item-6) ⭐️ 8.0/10
7. [quicktok: A Faster BPE Tokenizer](#item-7) ⭐️ 8.0/10
8. [Offline Ablations Mislead Production ML Results](#item-8) ⭐️ 8.0/10
9. [Cleo: A 2B Model for End-to-End Text-to-SQL](#item-9) ⭐️ 8.0/10
10. [New Framework for Neocortical Learning via Temporal Derivatives](#item-10) ⭐️ 8.0/10
11. [Developers Share Local Model Setups for Daily Coding](#item-11) ⭐️ 7.0/10
12. [Hetzner Announces Major Cloud Server Price Hikes](#item-12) ⭐️ 7.0/10
13. [Personality Clashes Behind Anthropic's Model Shutdown](#item-13) ⭐️ 7.0/10
14. [Open Training Frameworks Needed Beyond Open Weights](#item-14) ⭐️ 7.0/10
15. [Data labeling vs. collection: biggest time sink in embedded ML?](#item-15) ⭐️ 7.0/10
16. [Banned Book Library in a Wi-Fi Smart Light Bulb](#item-16) ⭐️ 6.0/10
17. [TinyWind: Pixel Pirate Sailing Game with Real Wind Physics](#item-17) ⭐️ 6.0/10
18. [A Nostalgic Love Letter to Computers](#item-18) ⭐️ 6.0/10
19. [Cloudflare CAPTCHA on at least one ampersand](#item-19) ⭐️ 6.0/10
20. [Datasette Agent 0.3a0 Adds Write SQL with User Approval](#item-20) ⭐️ 6.0/10
21. [EA PhD Career Prospects in ML](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Backdoor in LinkedIn Job Offer via npm Script](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

A security researcher discovered a backdoor hidden in a GitHub repository sent during a LinkedIn job interview, which uses npm's prepare script to execute arbitrary code upon installing dependencies. This attack highlights a novel social engineering vector for supply chain attacks, targeting developers through fake job offers, and demonstrates how trusted platforms like npm can be weaponized. The backdoor was buried in commented-out test code and executed via npm's prepare lifecycle script, which runs automatically after npm install. The payload could receive commands from a remote server.

hackernews · lwhsiao · Jun 15, 20:00 · [Discussion](https://news.ycombinator.com/item?id=48546294)

**Background**: npm's prepare script is a lifecycle hook that runs automatically after 'npm install' and before 'npm publish', commonly used for build steps. Supply chain attacks target less secure elements in the software development pipeline, such as third-party dependencies or recruitment processes.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/using-npm/scripts/">Scripts | npm Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/supply-chain-attack/">What Is a Supply Chain Attack? - CrowdStrike</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock at the sophistication of the attack, with some sharing similar experiences of elaborate LinkedIn scams. Others noted the lack of a centralized cybercrime reporting system and debated the role of AI in writing such exploits.

**Tags**: `#supply chain attack`, `#cybersecurity`, `#npm`, `#social engineering`, `#job scam`

---

<a id="item-2"></a>
## [x86 Emulator Team Patched Buggy Code During Emulation](https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419) ⭐️ 8.0/10

The x86 emulator team at Microsoft found a program that allocated 64KB on the stack using an unrolled loop of 16,384 MOV instructions, and they fixed it by detecting the pattern and replacing it with a faster initialization during emulation. This story highlights how compatibility layers and emulators can go beyond simple translation to actively fix software bugs, improving performance and stability for users without requiring original developers to patch their code. The program used an unrolled loop of 16,384 MOV instructions to initialize 64KB of stack memory, which was extremely slow under emulation. The emulator team added a heuristic to detect this pattern and replace it with a fast memset-like operation.

hackernews · paulmooreparks · Jun 16, 04:46 · [Discussion](https://news.ycombinator.com/item?id=48550693)

**Background**: Emulators translate instructions from one architecture (e.g., x86) to another (e.g., ARM), which can be slower than native execution. Compatibility layers like Wine and Proton also translate system calls and can apply workarounds for buggy software. Historically, Microsoft patched a read-after-free bug in SimCity for Windows 95 to improve compatibility.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48550693">The time the x86 emulator team found code so bad they fixed ...</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar stories, such as Microsoft patching a SimCity bug in Windows 95, and noted that modern compatibility layers like Proton now incorporate hotfixes for games like Elden Ring. Some discussed the trade-offs between performance and compatibility in emulation.

**Tags**: `#emulation`, `#x86`, `#software compatibility`, `#historical anecdotes`, `#bug workarounds`

---

<a id="item-3"></a>
## [John Carmack Praises Fabrice Bellard's Technical Genius](https://twitter.com/ID_AA_Carmack/status/2064095424420487226) ⭐️ 8.0/10

John Carmack tweeted praise for Fabrice Bellard, highlighting his extraordinary contributions to software engineering, including FFmpeg, QEMU, and QuickJS. The post sparked a discussion on Bellard's work ethic and impact. This recognition from a legendary figure like Carmack underscores Bellard's unique status as a prolific creator of foundational open-source tools. It also highlights the value of deep, focused work in an era of constant online engagement. Bellard's major projects include FFmpeg (multimedia framework), QEMU (emulator), QuickJS (JavaScript engine), and Tiny C Compiler. Many of his works are implementations of specifications into highly performant C code.

hackernews · apitman · Jun 16, 04:58 · [Discussion](https://news.ycombinator.com/item?id=48550779)

**Background**: Fabrice Bellard is a French software engineer known for creating several essential open-source projects. He is also known for his privacy-focused work ethic and minimal public presence. FFmpeg is a leading multimedia framework used by YouTube and VLC; QEMU is a popular machine emulator and virtualizer; QuickJS is a small embeddable JavaScript engine.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FFmpeg">FFmpeg</a></li>
<li><a href="https://en.wikipedia.org/wiki/QEMU">QEMU</a></li>
<li><a href="https://bellard.org/quickjs/">QuickJS Javascript Engine</a></li>

</ul>
</details>

**Discussion**: Commenters expressed deep respect for Bellard's work ethic and privacy, with some comparing him to Satoshi Nakamoto. One user noted that most of his work involves turning specifications into C code, while another pointed out that his FFmpeg code has been completely replaced over time.

**Tags**: `#Fabrice Bellard`, `#software engineering`, `#open source`, `#programming`, `#legendary developers`

---

<a id="item-4"></a>
## [Iroh 1.0: P2P Networking with Dial Keys, Not IPs](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0, a peer-to-peer networking library for Rust, has been released after 4+ years and 65+ releases, enabling direct app-to-app connections using public keys instead of IP addresses. This simplifies app-to-app connectivity by abstracting away IP addresses, making it easier for developers to build decentralized applications without worrying about NAT traversal or changing IPs. Iroh uses QUIC connections identified by EndpointId (a public key), supports NAT traversal via relays and hole-punching, and now allows custom transport implementations beyond the built-in IPv4, IPv6, and relay transports.

hackernews · chadfowler · Jun 15, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48542480)

**Background**: Traditional networking relies on IP addresses, which can change and require complex NAT traversal for peer-to-peer connections. Iroh treats IP addresses as a low-level detail, using cryptographic keys for identity and discovery, similar to how Tailscale works at the network layer but operating at the application layer.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/n0-computer/iroh">GitHub - n0-computer/iroh: IP addresses break, dial keys ... n0-computer/iroh | DeepWiki Iroh — Rust network library // Lib.rs Iroh 1.0: Dial Keys, Not IPs — P2P Hits Stable | byteiota iroh 0.23.0 - Welcoming Node.js to the family! - Iroh iroh - Iroh is a modular networking stack for building ...</a></li>
<li><a href="https://www.iroh.computer/blog/v1">Iroh 1.0 - Dial Keys, not IPs - Iroh</a></li>
<li><a href="https://tailscale.com/docs/concepts/tailscale-osi">Tailscale and the OSI model</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights Iroh's analogy to 'Tailscale at the application layer' and addresses questions about custom transport support (e.g., WebRTC, BLE). Some commenters question the problem Iroh solves, arguing IP and DNS work fine, while others praise the decentralization vision.

**Tags**: `#networking`, `#peer-to-peer`, `#rust`, `#open-source`, `#p2p`

---

<a id="item-5"></a>
## [Why AI Won't Replace Software Engineers](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

Arvind Narayanan and Sayash Kapoor published an essay arguing that AI will not cause mass layoffs in software engineering, citing data from New York's WARN Act filings where no company checked the AI-related layoff box in the first year. This evidence-based counterargument challenges the prevailing narrative that AI will soon replace software engineers, offering reassurance to the tech workforce and informing policy debates on AI's labor impact. The authors identify three real bottlenecks in software engineering that resist automation: deciding what to build, verifying what is delivered, and deep human understanding of the codebase, business, and environment.

rss · Simon Willison · Jun 14, 23:54

**Background**: The WARN Act requires employers to provide advance notice of mass layoffs. In March 2025, New York added a checkbox asking whether layoffs were due to technological innovation or automation. Despite widespread AI adoption, no company checked that box in the first year, suggesting AI is not yet a primary cause of job displacement in software engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hunton.com/hunton-employment-labor-perspectives/new-york-warn-act-no-ai-related-layoffs-reported-in-first-year-of-adding-ai-related-disclosure-to-the-system">New York WARN Act: No AI-Related Layoffs Reported in First Year of Adding AI-Related Disclosure to the System</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#job displacement`, `#labor economics`

---

<a id="item-6"></a>
## [LLMs Have Model-Specific Name Priors](https://www.reddit.com/r/MachineLearning/comments/1u6mn3q/ai_language_models_have_favorite_names_and_we/) ⭐️ 8.0/10

Researchers discovered that large language models (LLMs) exhibit model-specific and version-specific priors for character names, producing correlated ensembles such as "Elena Vasquez" and "Marcus Chen" that appear together across numerous websites as hallucinated personas. This finding reveals a blind spot in how LLM-generated content propagates: millions of documents generated without explicit name overrides embed characteristic name priors, making it possible to detect AI-generated content by spotting these correlated name ensembles. The study, published as a preprint on arXiv (2606.02184), used a model diffing method called CDD to identify these correlated ensembles, which include trios of names appearing with AI-generated stock photo faces across dozens of websites.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jun 15, 17:07

**Background**: LLMs often hallucinate, generating plausible-sounding but factually incorrect information. This study focuses on a specific type of hallucination: fictional character names that LLMs consistently generate together. The researchers found that these name pairs and trios are not random but are correlated ensembles that persist across independent generations and model versions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02184">The Ghost Couple: Correlated LLM Name Priors and Their ...</a></li>
<li><a href="https://www.semanticscholar.org/paper/The-Ghost-Couple:-Correlated-LLM-Name-Priors-and-of-Brzozowski-Chung/0d9b815d840862b6842739708b2ee8921e92c072">The Ghost Couple: Correlated LLM Name Priors and Their ...</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/ghost-couple-correlated-llm-name-priors-their">The Ghost Couple: Correlated LLM Name Priors and Their ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#hallucination`, `#AI-generated content`, `#model diffing`, `#machine learning`

---

<a id="item-7"></a>
## [quicktok: A Faster BPE Tokenizer](https://www.reddit.com/r/MachineLearning/comments/1u73c5r/quicktok_a_faster_tokenizer_exact_and/) ⭐️ 8.0/10

quicktok is a new open-source BPE tokenizer in C++ that achieves 2-11x speedup over tiktoken and bpe-openai while producing byte-identical output. Tokenization is a critical bottleneck in LLM inference and training; faster tokenizers can reduce latency and cost for large-scale deployments. It uses a 2-byte trie for longest-match walks, dense caches for merge validity, and a hand-compiled pretokenizer instead of a general regex engine.

reddit · r/MachineLearning · /u/_casa_nova_ · Jun 16, 04:24

**Background**: Byte-pair encoding (BPE) is a subword tokenization algorithm used by most modern LLMs like GPT-4 and Llama. It converts text into token IDs by iteratively merging the most frequent byte pairs. tiktoken is OpenAI's official BPE tokenizer, and bpe-openai is a popular C++ reimplementation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/tiktoken">GitHub - openai/tiktoken: tiktoken is a fast BPE tokeniser for use with OpenAI's models. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Byte-pair_encoding">Byte-pair encoding - Wikipedia</a></li>
<li><a href="https://sebastianraschka.com/blog/2025/bpe-from-scratch.html">Implementing A Byte Pair Encoding (BPE) Tokenizer From Scratch</a></li>

</ul>
</details>

**Discussion**: The community praised the performance and thorough benchmarks, with some users asking about integration with Hugging Face tokenizers and support for custom vocabularies. The author responded to technical questions about the trie implementation and memory usage.

**Tags**: `#tokenizer`, `#BPE`, `#LLM`, `#performance`, `#open-source`

---

<a id="item-8"></a>
## [Offline Ablations Mislead Production ML Results](https://www.reddit.com/r/MachineLearning/comments/1u7b1vv/my_offline_ablation_said_019pp_the_production/) ⭐️ 8.0/10

A practitioner at a watch price forecasting company reports four cases where offline ablation studies gave misleading signals, including one where a -0.19pp improvement in offline testing turned into a +1.11pp regression in production. This highlights a critical failure mode in ML validation: offline ablations can systematically overestimate improvements when changes alter the training population, not just features, leading to costly production regressions. The root causes included train/serve skew (Best Offer feature), unmeasured distribution shift (Auction data backfill), training population shift (Outlier trimming), and baseline instability (CatBoost encoder). The author advocates comparing against production with a strict gate (e.g., >0.30pp worse blocks promotion).

reddit · r/MachineLearning · /u/Nj-yeti · Jun 16, 11:38

**Background**: An ablation study in machine learning measures the impact of removing a component by retraining without it and comparing performance. Train/serve skew occurs when the data distribution or feature computation differs between training and production. LightGBM quantile regression predicts percentiles (e.g., p10, p50, p90) using a pinball loss function.

<details><summary>References</summary>
<ul>
<li><a href="https://building.nubank.com/dealing-with-train-serve-skew-in-real-time-ml-models-a-short-guide/">Dealing with Train-serve Skew in Real-time ML Models: A Short ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ablation_(artificial_intelligence)">Ablation (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/machine-learning/lightgbm-for-quantile-regression/">LightGBM for Quantile Regression - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion (not provided in detail) likely includes agreements on the pitfalls of offline ablations and suggestions for production-gated validation, as the post itself advocates.

**Tags**: `#machine learning`, `#feature importance`, `#production ML`, `#ablation study`, `#model validation`

---

<a id="item-9"></a>
## [Cleo: A 2B Model for End-to-End Text-to-SQL](https://www.reddit.com/r/MachineLearning/comments/1u6udpb/cleo_trying_to_fit_full_analyst_behavior_in_a_2b/) ⭐️ 8.0/10

Cleo is a 2B parameter fine-tuned model that performs end-to-end analyst behavior (gather, repair, answer) for text-to-SQL, trained and evaluated in a unified harness, with open-source code and model. This demonstrates that a small 2B model can effectively handle complex text-to-SQL pipelines, challenging the assumption that large models are necessary, and offers a practical solution for resource-constrained environments. Cleo is fine-tuned from Qwen3.5-2B-Base and uses a unified harness that trains on the exact same gather, repair, and answer contract used at inference, including live execution evidence for candidate query search.

reddit · r/MachineLearning · /u/Dreeseaw · Jun 15, 21:43

**Background**: Text-to-SQL is a natural language processing task that converts natural language questions into SQL queries. Many industrial chatbots rely on text-to-SQL or retrieval-augmented generation (RAG). Small language models (like 2B parameters) are attractive for deployment due to lower computational costs.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-to-sql-solution-generating-complex-queries-self-correcting-and-querying-diverse-data-sources/">Build a robust text-to-SQL solution generating complex queries, self-correcting, and querying diverse data sources | Artificial Intelligence</a></li>

</ul>
</details>

**Discussion**: The community discussion includes technical questions about the unified harness and the model's performance on complex queries, with the author actively engaging and providing clarifications. Overall sentiment is positive, with interest in applying similar approaches to other domains.

**Tags**: `#text-to-SQL`, `#small language models`, `#open-source`, `#fine-tuning`, `#NLP`

---

<a id="item-10"></a>
## [New Framework for Neocortical Learning via Temporal Derivatives](https://www.reddit.com/r/MachineLearning/comments/1u6x8al/how_the_brains_learn_r/) ⭐️ 8.0/10

A new paper proposes error-driven predictive learning via temporal derivatives as a complete framework for how the neocortex learns, implemented in spiking neural networks within the Axon simulation framework. This framework claims to meet all three criteria for a general-purpose learning algorithm and could potentially surpass backpropagation, impacting both neuroscience and machine learning. The framework is driven by corticothalamic circuits and competitive kinase synaptic plasticity induction mechanisms, and has been demonstrated on challenging cognitively motivated tasks.

reddit · r/MachineLearning · /u/Terminator857 · Jun 15, 23:39

**Background**: The neocortex is the part of the brain responsible for higher-order functions like perception and cognition. Backpropagation is a widely used learning algorithm in artificial neural networks, but it is not biologically plausible. This work aims to bridge the gap between biological learning and powerful AI algorithms.

<details><summary>References</summary>
<ul>
<li><a href="https://iqgenio.com/blog/how-neocortex-learns-error-driven-predictive-learning/">How the Neocortex Learns: Error-Driven Predictive Learning ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2606.08720">Temporal Derivative Model in Neocortex - emergentmind.com</a></li>
<li><a href="https://www.math.ucdavis.edu/~saito/ucd4ids/RandallOReilly020420.pdf">Predictive Error-Driven Learning in the Brain</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#machine learning`, `#backpropagation`, `#cortical learning`, `#spiking neural networks`

---

<a id="item-11"></a>
## [Developers Share Local Model Setups for Daily Coding](https://news.ycombinator.com/item?id=48542100) ⭐️ 7.0/10

A Hacker News discussion reveals that many developers have successfully replaced cloud-based coding assistants like Claude and GPT with local models, sharing specific hardware setups and performance metrics such as tokens per second. This shift toward local models could reduce reliance on cloud APIs, offering benefits in privacy, cost savings, and offline availability, potentially reshaping how developers integrate AI into their workflows. Users report using models like Qwen3.6 35B and Gemma-4-26B on hardware such as Mac Studio with 128GB RAM or dual RTX 3090s, achieving around 150 tok/s. Some employ tools like Pi coding harness and unsloth studio for containerized, offline execution.

hackernews · cloudking · Jun 15, 14:46

**Background**: Local LLMs run on the user's own hardware, eliminating the need for cloud API calls and ensuring data privacy. Tokens per second (tok/s) is a key performance metric for local inference, with 5-15 tok/s considered slow and 50+ tok/s considered usable for interactive coding. Models like Qwen3.6 use a mixture-of-experts (MoE) architecture, activating only a subset of parameters per token to improve speed.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@walterdeane/running-a-local-llm-for-code-assistance-dea64748041a">Running a Local LLM for Code Assistance - Medium</a></li>
<li><a href="https://overchat.ai/ai-hub/best-local-llm-for-coding">Best Local LLM for Coding in 2026: Developer's Guide | AI Hub</a></li>
<li><a href="https://dev.to/alanwest/how-to-set-up-a-local-ai-coding-assistant-that-actually-works-43j8">How to Set Up a Local AI Coding Assistant That Actually Works</a></li>

</ul>
</details>

**Discussion**: The community is enthusiastic about local models, with many sharing detailed setups and performance numbers. Some note that local models are not as smart as frontier cloud models but are sufficient for most daily coding tasks. A few express optimism that local models will become the standard, especially as API costs rise.

**Tags**: `#local LLMs`, `#coding assistant`, `#privacy`, `#open source`, `#developer tools`

---

<a id="item-12"></a>
## [Hetzner Announces Major Cloud Server Price Hikes](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 7.0/10

Hetzner has announced significant price increases for its cloud servers, with some instances seeing up to a 300% rise, effective immediately. This price adjustment reflects rising hardware costs and may push users to consider alternatives like self-hosted mini PCs or other cloud providers. The new pricing applies to cloud servers and follows a previous increase 38 days ago; the company cites higher purchasing and operational costs as reasons.

hackernews · tuhtah · Jun 15, 13:19 · [Discussion](https://news.ycombinator.com/item?id=48540844)

**Background**: Hetzner is a popular European cloud and hosting provider known for competitive pricing. The cloud market has seen rising hardware costs due to global supply chain issues, affecting providers of all sizes.

**Discussion**: Community reactions are mixed, with many users expressing shock at the 300% increase, while some acknowledge the reality of hardware cost inflation. The CEO's forum response attempted to explain the rationale, but skepticism remains.

**Tags**: `#cloud`, `#pricing`, `#Hetzner`, `#infrastructure`

---

<a id="item-13"></a>
## [Personality Clashes Behind Anthropic's Model Shutdown](https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything) ⭐️ 7.0/10

Axios reported that personality clashes and behind-the-scenes tensions between Anthropic and the US government led to an export control directive suspending access to Anthropic's Fable 5 and Mythos 5 models. Key figures including Logan Graham, Dave Orr, and Nicholas Carlini are meeting with the Commerce Department to address the situation. This incident highlights the growing tension between AI safety concerns and national security export controls, potentially setting a precedent for how frontier AI models are regulated. The outcome could affect Anthropic's operations and the broader AI industry's approach to model deployment and security. The jailbreak that triggered the US government response was described as a potential narrow, non-universal jailbreak, and Anthropic claims no universal jailbreak has been found against Claude Mythos. The export control directive bans use of Fable 5 and Mythos 5 by any foreign national, including foreign national Anthropic employees.

rss · Simon Willison · Jun 15, 14:57

**Background**: Anthropic is an AI safety company that develops large language models like Claude. Export controls are US government regulations that restrict the transfer of sensitive technologies to foreign nationals. The Frontier Red Team at Anthropic focuses on evaluating and mitigating risks from advanced AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/fable-mythos-access">Statement on the US government directive to suspend access to Fable 5 and Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.businessinsider.com/why-white-house-ordered-export-controls-anthropic-mythos-fable-2026-6">Inside the whirlwind 24 hours that led the White House to slap export controls on Anthropic</a></li>
<li><a href="https://x.com/AnthropicAI/status/2065597531644743999">Anthropic on X: "The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of" / X</a></li>

</ul>
</details>

**Discussion**: The article's comments highlight skepticism about the severity of the jailbreak, with some arguing that fixing code is a standard capability of coding models and should not trigger export controls. Others express concern that the incident reflects poor communication and trust issues between Anthropic and the government.

**Tags**: `#AI safety`, `#Anthropic`, `#export controls`, `#US government`, `#policy`

---

<a id="item-14"></a>
## [Open Training Frameworks Needed Beyond Open Weights](https://www.reddit.com/r/MachineLearning/comments/1u6p7k3/open_weights_are_not_enough_we_need_open_training/) ⭐️ 7.0/10

A Reddit post advocates for open training frameworks that make the training process visible and modifiable, introducing FeynRL, a new open-source framework for RL post-training of LLMs, VLMs, and agents. This matters because current open-weight models alone are insufficient for advancing ML research; researchers need transparent training pipelines to develop new algorithms and improve reproducibility. FeynRL is designed with an algorithm-first approach, separating algorithmic logic from system infrastructure, and currently supports SFT, DPO, and RL-style post-training on single-GPU, multi-GPU, and cluster setups.

reddit · r/MachineLearning · /u/summerday10 · Jun 15, 18:37

**Background**: Post-training of large language models (LLMs) involves techniques like supervised fine-tuning (SFT), direct preference optimization (DPO), and reinforcement learning (RL) to improve model behavior. Many existing frameworks are black-box systems that make it hard to modify or understand the training process, hindering research progress.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/FeynRL-project/FeynRL">GitHub - FeynRL-project/FeynRL: Post-training framework for ...</a></li>
<li><a href="https://feynrl-project.github.io/">FeynRL — Understand What You Build</a></li>
<li><a href="https://pytorch.org/blog/a-primer-on-llm-post-training/">A Primer on LLM Post-Training – PyTorch</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely supports the need for open training frameworks, with users sharing experiences of debugging hidden systems and emphasizing the importance of modular, transparent codebases for RL post-training.

**Tags**: `#open source`, `#machine learning`, `#reinforcement learning`, `#training frameworks`, `#research reproducibility`

---

<a id="item-15"></a>
## [Data labeling vs. collection: biggest time sink in embedded ML?](https://www.reddit.com/r/MachineLearning/comments/1u6q97f/embeddededge_ml_folks_what_actually_eats_the_most/) ⭐️ 7.0/10

A Reddit user asks the embedded/edge ML community whether data collection or cleaning/labeling is the bigger bottleneck for time-series sensor data, and seeks validation for a tool that automates data quality and labeling. Understanding the primary bottleneck helps tool builders prioritize features that genuinely save time for practitioners, potentially accelerating development of edge ML applications in IoT, wearables, and industrial monitoring. The user proposes four potential features: automatic data quality checks, AI-assisted labeling, enforcing data standards at collection, and reproducible/versioned pipelines. They specifically ask which are worth paying for and whether the expensive pain is catching basic or subtle data issues.

reddit · r/MachineLearning · /u/No-Bug-4879 · Jun 15, 19:13

**Background**: Embedded machine learning (TinyML) involves deploying ML models on resource-constrained microcontrollers. Time-series sensor data (e.g., from accelerometers, IMUs) is common in applications like predictive maintenance and gesture recognition. Data quality and labeling are known challenges, and platforms like Edge Impulse exist to streamline the workflow.

<details><summary>References</summary>
<ul>
<li><a href="https://www.edgeimpulse.com/">Edge Impulse - The Leading Edge AI Platform</a></li>
<li><a href="https://sophelio.io/top-data-labeling-tools-data-time-series-and-sensor/">Top Data Labeling Tools Data For Time-Series And Sensor Data</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3592616">A Survey of Data Quality Requirements That Matter in ML ...</a></li>

</ul>
</details>

**Discussion**: The post has no comments yet, so no community discussion is available.

**Tags**: `#embedded ML`, `#time series`, `#data labeling`, `#edge computing`, `#machine learning`

---

<a id="item-16"></a>
## [Banned Book Library in a Wi-Fi Smart Light Bulb](https://www.richardosgood.com/posts/banned-book-library/) ⭐️ 6.0/10

A project turns a Wi-Fi smart light bulb into a local web server hosting a library of banned books, accessible without an internet connection. This project repurposes ubiquitous smart home devices for censorship-resistant information sharing, potentially making banned books more accessible in restrictive environments. The light bulb runs a web server on its internal ESP8266 chip, serving books over Wi-Fi. The project is similar to PirateBox but uses a smart bulb instead of a dedicated router.

hackernews · sohkamyung · Jun 15, 22:37 · [Discussion](https://news.ycombinator.com/item?id=48547985)

**Background**: PirateBox is a portable device that creates a local Wi-Fi network for anonymous file sharing, often used for distributing information without internet access. Smart light bulbs like those with ESP8266 chips can be reprogrammed to run custom firmware, enabling them to act as small servers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PirateBox">PirateBox</a></li>
<li><a href="https://github.com/piratebox-dev">PirateBox Project · GitHub</a></li>
<li><a href="https://daviddarts.com/piratebox">David Darts - PirateBox</a></li>

</ul>
</details>

**Discussion**: Commenters noted the project is not novel, comparing it to PirateBox from 2012. Some questioned the 'banned' label, arguing the listed books are often removed from school libraries for explicit content, not truly banned. Others expressed interest but doubted the selection would include truly controversial works.

**Tags**: `#Wi-Fi`, `#smart light bulb`, `#banned books`, `#PirateBox`, `#library`

---

<a id="item-17"></a>
## [TinyWind: Pixel Pirate Sailing Game with Real Wind Physics](https://tinywind.io/) ⭐️ 6.0/10

TinyWind is a pixel art sailing game that attempts to simulate real wind physics, with players having sailed over 380,000 kilometers in the game. This game represents a niche attempt to bring realistic sailing physics to a casual web game, potentially attracting both gamers and sailing enthusiasts. However, community feedback highlights significant inaccuracies in the sailing mechanics, which may limit its appeal to serious sailors. The game features a wind teller indicator, but players find it unintuitive and the sail angle mechanics do not accurately reflect real sailing principles like tacking or apparent wind. The game has high engagement with 883 points and 161 comments on Hacker News.

hackernews · tinywind · Jun 15, 16:15 · [Discussion](https://news.ycombinator.com/item?id=48543475)

**Background**: Realistic sailing physics in games require accurate modeling of wind direction, sail trim, and hull dynamics relative to the wind. Games like Sailway and eSail are known for their authentic sailing mechanics, while many casual games simplify these systems. TinyWind aims to bridge this gap but falls short according to community experts.

<details><summary>References</summary>
<ul>
<li><a href="https://topaihubs.com/articles/tinywind-how-realistic-wind-physics-in-a-sailing-game-signals-a-new-era-for-simu">TinyWind: How Realistic Wind Physics in a Sailing Game ...</a></li>
<li><a href="https://windbender.io/">Windbender - Online multiplayer sailing game</a></li>
<li><a href="https://shelterphysics.com/sailing/">Sheltermouse Sailing Simulator - shelterphysics.com</a></li>

</ul>
</details>

**Discussion**: Community comments are largely positive about the game's concept and visuals, but several experienced sailors criticize the wind physics as inaccurate. They note that the game does not properly simulate upwind sailing, tacking costs, or the dead angle of square-rigged ships, and the sail trim controls are clunky and unresponsive.

**Tags**: `#game`, `#physics simulation`, `#sailing`, `#web game`

---

<a id="item-18"></a>
## [A Nostalgic Love Letter to Computers](https://michaelenger.com/blog/i-love-the-computer/) ⭐️ 6.0/10

Michael Enger published a personal essay titled 'I Love the Computer,' reflecting on his deep affection for computing and the joy of tinkering with machines. The essay resonates with many readers who share similar nostalgic feelings, sparking a discussion about how modern computing and AI have changed the relationship between humans and machines. The article scored 6.0/10 on Hacker News with 252 points and 144 comments, indicating strong community engagement despite not being technically groundbreaking.

hackernews · speckx · Jun 15, 20:14 · [Discussion](https://news.ycombinator.com/item?id=48546441)

**Background**: The essay is a personal reflection, not a technical piece, and it taps into a common sentiment among older programmers who remember the early days of home computing. The community discussion contrasts nostalgia with the current state of computing, including the role of AI tools like LLMs.

**Discussion**: Commenters expressed mixed feelings: some lament the loss of the old computing magic, while others still find joy in tinkering. A few defended AI as a useful tool, disagreeing with the article's implied criticism of AI as 'snake oil.'

**Tags**: `#nostalgia`, `#computing`, `#personal essay`, `#community discussion`

---

<a id="item-19"></a>
## [Cloudflare CAPTCHA on at least one ampersand](https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/#atom-everything) ⭐️ 6.0/10

Simon Willison shared a Cloudflare WAF custom rule that triggers a Managed Challenge only for search URLs containing at least one ampersand, avoiding CAPTCHA on simple queries like ?q=term. This practical tweak improves user experience for legitimate visitors while still protecting against aggressive crawlers, and demonstrates how to fine-tune Cloudflare WAF rules for specific use cases. The rule uses the expression (http.request.uri.path wildcard r"/search/*" and http.request.uri.query contains "&") to match only search paths with query parameters containing an ampersand. Willison also explored using the Cloudflare MCP with Claude Code but ultimately switched to the Cloudflare API to edit the rules.

rss · Simon Willison · Jun 16, 00:21

**Background**: Cloudflare's Managed Challenge is a CAPTCHA alternative that verifies visitors are human. WAF custom rules allow site owners to define conditions for triggering such challenges. Simon Willison runs a faceted search engine on his site and wanted to block aggressive crawlers without inconveniencing users making simple searches.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/waf/custom-rules/">Custom rules · Cloudflare Web Application Firewall (WAF) docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-challenges/">Challenges · Cloudflare challenges docs</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#WAF`, `#CAPTCHA`, `#web scraping`, `#configuration`

---

<a id="item-20"></a>
## [Datasette Agent 0.3a0 Adds Write SQL with User Approval](https://simonwillison.net/2026/Jun/15/datasette-agent/#atom-everything) ⭐️ 6.0/10

Datasette-agent 0.3a0 introduces an execute_write_sql tool that requests user approval before executing write operations on a database, and enhances the CLI chat mode to support approvals with new options like --unsafe for auto-approval. This release makes Datasette Agent safer for real-world use by adding a permission layer for write operations, enabling users to interact with databases via natural language while maintaining control over data modifications. The execute_write_sql tool checks user permissions and presents a confirmation dialog showing the SQL statements and required permissions before execution. The --unsafe mode bypasses all approvals, allowing direct database modifications via chat.

rss · Simon Willison · Jun 15, 17:19

**Background**: Datasette Agent is an LLM-powered assistant for Datasette, a tool for exploring and publishing data. It allows users to query and manipulate databases using natural language. The 0.2a0 version introduced a user approval mechanism, and 0.3a0 extends it to write operations.

<details><summary>References</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help ...</a></li>
<li><a href="https://pypi.org/project/datasette-agent/">datasette-agent · PyPI</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#sql`, `#release`, `#tool`

---

<a id="item-21"></a>
## [EA PhD Career Prospects in ML](https://www.reddit.com/r/MachineLearning/comments/1u66q3l/how_does_the_ml_community_view_evolutionary/) ⭐️ 6.0/10

A master's student with publications in evolutionary algorithms (EAs) is asking the ML community whether pursuing an EA PhD would harm their career prospects, given that some researchers dismiss EAs as inferior to other optimizers. This question reflects a real tension between niche optimization fields and mainstream ML, and the answer could guide students considering specialized PhDs in areas perceived as less central to deep learning. The student has coauthored papers in strong EA venues and occasionally in mainstream ML venues like AAAI and NeurIPS, and is considering whether to switch to a more ML-centric PhD program.

reddit · r/MachineLearning · /u/NullRecurrentDad · Jun 15, 04:48

**Background**: Evolutionary algorithms are population-based metaheuristics inspired by biological evolution, used for optimization problems where traditional methods may fail. They are a subfield of randomized search heuristics and have been applied in machine learning, but are sometimes criticized for being outperformed by gradient-based methods in deep learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Evolutionary_algorithm">Evolutionary algorithm - Wikipedia</a></li>
<li><a href="https://www.ultralytics.com/blog/what-is-an-evolutionary-algorithm-a-quick-guide">A Guide on Evolutionary Algorithms | Ultralytics</a></li>

</ul>
</details>

**Discussion**: The Reddit post has no comments provided, so community sentiment cannot be summarized.

**Tags**: `#evolutionary algorithms`, `#PhD`, `#career advice`, `#machine learning`

---