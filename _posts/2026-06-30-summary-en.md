---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 28 items, 16 important content pieces were selected

---

1. [US Supreme Court rules geofence warrants require constitutional protections](#item-1) ⭐️ 9.0/10
2. [Google's Agentic Peer-Reviewer Handles 10K Papers at ICML/STOC](#item-2) ⭐️ 9.0/10
3. [Qwen 3.6 27B: The Sweet Spot for Local Development](#item-3) ⭐️ 8.0/10
4. [HCCF Proposes .self TLD for Self-Hosting and Digital Identity](#item-4) ⭐️ 8.0/10
5. [30-Year Sentence for Hiding Zines Ignites Free Speech Alarm](#item-5) ⭐️ 8.0/10
6. [One million passports leaked online](#item-6) ⭐️ 8.0/10
7. [Jon Udell Proposes Flipping 'Human in the Loop' to Invite AI Agents](#item-7) ⭐️ 8.0/10
8. [EML Trees are Universal Approximators](#item-8) ⭐️ 8.0/10
9. [Rocket Lab Acquires Iridium in Historic Deal](#item-9) ⭐️ 7.0/10
10. [Ornith-1.0: Open-Source Self-Improving Model for Agentic Coding](#item-10) ⭐️ 7.0/10
11. [Cerebras-OpenAI $20B Deal Effectively Kills API Waitlist for Others](#item-11) ⭐️ 7.0/10
12. [Minimal Interactive Transformer Visualizes Forward Pass with Editable Weights](#item-12) ⭐️ 7.0/10
13. [Proposal for a native graphical shell for SSH](#item-13) ⭐️ 6.0/10
14. [HTML Table Extractor Tool Released by Simon Willison](#item-14) ⭐️ 6.0/10
15. [Why NCE Over Direct Negative Sampling in Instance Learning?](#item-15) ⭐️ 6.0/10
16. [Swordfighting Dataset Aims to Improve Thin-Object Tracking](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [US Supreme Court rules geofence warrants require constitutional protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants—used to identify all mobile devices in a specific area and time—require a warrant under the Fourth Amendment, restricting law enforcement's warrantless access to location data. This landmark decision significantly strengthens digital privacy protections by extending Fourth Amendment safeguards to geofence warrants, thereby restricting law enforcement's ability to conduct warrantless mass surveillance through location data. The court's opinion detailed Google's three-step process in providing data, highlighting the need for a warrant at each stage. Justices Alito, Thomas, and Barrett dissented, arguing for broader law enforcement access. The ruling may also impact other surveillance technologies like Flock license plate readers that collect location data without individual suspicion.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant (or reverse location warrant) allows law enforcement to demand that companies like Google search their databases for all devices present in a defined geographic area and time window. The Fourth Amendment to the US Constitution protects against unreasonable searches and seizures, typically requiring a warrant based on probable cause. In Riley v. California (2014), the Supreme Court recognized that modern cell phones hold vast amounts of personal information deserving heightened privacy protection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>

</ul>
</details>

**Discussion**: Commenters largely supported the ruling, providing technical details on Google's data provision process and noting alternative identification methods (e.g., cross-referencing hotel guest lists). They praised the court for citing sources in its opinion and raised concerns about the decision's impact on surveillance tools like Flock license plate readers. Some expressed surprise at the dissenting votes from conservative justices.

**Tags**: `#privacy`, `#supreme-court`, `#geofence-warrants`, `#fourth-amendment`, `#digital-rights`

---

<a id="item-2"></a>
## [Google's Agentic Peer-Reviewer Handles 10K Papers at ICML/STOC](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at ICML and STOC, where it reviewed approximately 10,000 papers with a 30-minute turnaround, achieving a 34% improvement in detecting mathematical errors over zero-shot prompting, and the formal research paper documenting this has now been published. This sets a groundbreaking precedent for AI-automated scientific review at conference scale, potentially transforming academic publishing by enhancing efficiency and accuracy. The agentic system improved mathematical error detection by 34% compared to zero-shot methods, processed ~10,000 papers across two top-tier conferences, and provided reviews within 30 minutes per paper.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Agentic AI refers to autonomous, goal-oriented systems that can reason, plan, and execute multi-step tasks with minimal human intervention. Zero-shot prompting is a technique where a model performs a task without any task-specific examples, relying solely on its pre-trained knowledge. The combination of agentic workflows and advanced prompting can significantly enhance complex task performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**Tags**: `#AI peer review`, `#agentic systems`, `#machine learning`, `#academic publishing`, `#scientific AI`

---

<a id="item-3"></a>
## [Qwen 3.6 27B: The Sweet Spot for Local Development](https://quesma.com/blog/qwen-36-is-awesome/) ⭐️ 8.0/10

A blog post evaluates Qwen 3.6 27B as an ideal local LLM for coding on a MacBook Pro M5 with 128GB RAM, sparking lively community debate on its real-world viability. This discussion highlights the challenges and trade-offs of running powerful open-weight models locally, influencing how developers choose between local privacy and cloud API cost-efficiency. Qwen 3.6 27B is a dense 27-billion-parameter model released by Alibaba in April 2026, with strong coding benchmarks; local inference required a $6,699 128GB MacBook Pro that suffers from heat and fan noise under load.

hackernews · stared · Jun 29, 17:05 · [Discussion](https://news.ycombinator.com/item?id=48721903)

**Background**: Qwen 3.6 is a series of open-weight LLMs from Alibaba, with the 27B variant balancing capability and resource demands. Local LLM deployment remains popular for code generation, data privacy, and offline use, but typically requires significant hardware. Apple Silicon Macs with unified memory have become a common platform due to their efficiency, but models over a few billion parameters can still push thermal limits.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/rico03/Qwen3.6-27B-Claude-Opus-Reasoning-Distilled">rico03/ Qwen 3 . 6 - 27 B -Claude-Opus-Reasoning-Distilled · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.6-27b">Qwen 3 . 6 27 B - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://ollama.com/library/qwen3.6:27b">qwen 3 . 6 : 27 b</a></li>

</ul>
</details>

**Discussion**: Commenters noted that a MacBook Pro is impractical for sustained AI workloads due to heat and noise, and that cloud API access (e.g., OpenRouter) offers better cost-performance. Others argued that zero-shot greenfield projects are not representative of real-world coding, and the utility for complex existing codebases remains unproven.

**Tags**: `#local-llm`, `#qwen`, `#hardware`, `#development`, `#llm-evaluation`

---

<a id="item-4"></a>
## [HCCF Proposes .self TLD for Self-Hosting and Digital Identity](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/) ⭐️ 8.0/10

HCCF has introduced a proposal for a new top-level domain, .self, aimed at facilitating self-hosting and human-centric identity management, generating significant discussion among technologists. The .self domain could offer individuals a dedicated namespace for personal sites and services under their control, potentially reducing reliance on commercial registrars and enhancing privacy. However, the viability hinges on solving abuse and funding challenges. Key aspects include free subdomains per person, anti-squatting rules, and identity verification. Concerns include how to fund the TLD without registration fees, differentiate parked domains from legitimate ones, and prevent reputation damage from misuse.

hackernews · HumanCCF · Jun 29, 19:49 · [Discussion](https://news.ycombinator.com/item?id=48724230)

**Background**: A top-level domain (TLD) is the highest level in the DNS hierarchy, like .com or .org. Self-hosting involves running web services on privately controlled servers rather than third-party platforms. The proposal comes from HCCF, which appears to be a human-centric computing advocacy group, though its exact nature is not publicly detailed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Top-level_domain">Top-level domain - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-hosting_(network)">Self-hosting (network) - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=48724230">.self: A new top-level domain designed to support self-hosting | Hacker News</a></li>

</ul>
</details>

**Discussion**: Community comments reflect cautious optimism: some recall the failure of free .tk domains due to abuse, others suggest reputation-based systems or identity verification via zero-knowledge proofs, and many question the economic sustainability and anti-abuse enforcement of a free TLD.

**Tags**: `#TLD`, `#self-hosting`, `#decentralization`, `#digital identity`, `#internet governance`

---

<a id="item-5"></a>
## [30-Year Sentence for Hiding Zines Ignites Free Speech Alarm](https://theintercept.com/2026/06/26/daniel-sanchez-estrada-zines-prairieland-free-speech/) ⭐️ 8.0/10

Daniel Sanchez Estrada received a 30-year prison sentence for hiding zines sought under a federal warrant, after his wife alerted him to the warrant. The zines were related to a protest at an ICE facility where a federal officer was shot. This case sets a dangerous precedent by equating the concealment of published materials with serious criminal accessory, potentially chilling free expression and activist journalism. It highlights growing tensions between national security prosecutions and First Amendment protections. The zines had been publicly available for years and were sought as evidence in a shooting investigation, though Sanchez Estrada was not the shooter. The sentence is part of a broader case where co-defendants received sentences of 70–100 years.

hackernews · xrd · Jun 28, 21:42 · [Discussion](https://news.ycombinator.com/item?id=48711981)

**Background**: Zines are self-published, often political, small-circulation booklets commonly used in activist communities. Under U.S. law, accessory after the fact involves assisting someone to evade arrest or punishment, with penalties often tied to the underlying crime. This case stems from a 2020 protest at an ICE facility in Texas where an officer was shot, and authorities sought zines as potential evidence.

**Discussion**: Commenters are divided: some see the sentence as a severe blow to free speech, comparing it to a 'crack in the dam,' while others argue that hiding evidence is clearly criminal, though the sentence length is extreme. Partisan expectations of a presidential pardon were also mentioned.

**Tags**: `#free-speech`, `#legal`, `#censorship`, `#activism`, `#hacker-news`

---

<a id="item-6"></a>
## [One million passports leaked online](https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal) ⭐️ 8.0/10

A data breach involving age verification systems for Spanish cannabis clubs, operated by Irish company Cannabis Club Systems, leaked high-resolution scans of one million passports online. This incident highlights the danger of using high-value identity documents in low-security ancillary services, as the breached system retained sensitive data post-verification, putting individuals at risk of identity theft. It comes amid global pushes for online age verification, showing potential massive privacy violations. The data was collected by cannabis clubs in Spain and stored by an Irish company; the specific security flaws are unclear but involved an insecure online database. Many countries are enacting age verification laws, which could multiply such risks.

hackernews · jruohonen · Jun 28, 11:22 · [Discussion](https://news.ycombinator.com/item?id=48706389)

**Background**: Age verification systems often require uploading government-issued IDs, and some store them indefinitely. The push for online age verification (e.g., for social media, online sales) expands the attack surface. Passports are high-value credentials because their data enables identity theft. The EU's eIDAS 2.0 regulation aims to provide secure digital identity solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://daringfireball.net/linked/2026/06/28/puffpal-passport-leak">Daring Fireball: PuffPal, an App for Accessing Cannabis Clubs, Leaked 1 Million Users' Passports</a></li>
<li><a href="https://www.resetera.com/threads/a-million-passports-for-online-age-verification-have-been-hacked-leaked.1563271/">A million passports for online age verification have been... | ResetEra</a></li>

</ul>
</details>

**Discussion**: Commenters criticized the insecure storage of passports for trivial verifications, shared similar experiences of passport data leaks, and called for policy changes, with some pointing to eIDAS 2.0 as a potential remedy.

**Tags**: `#data-breach`, `#privacy`, `#security`, `#identity-theft`, `#age-verification`

---

<a id="item-7"></a>
## [Jon Udell Proposes Flipping 'Human in the Loop' to Invite AI Agents](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell argues for flipping the dominant 'human in the loop' narrative, proposing that developers should invite AI agents into their established workflows instead of inserting humans into an agent-driven loop. This reframing challenges existing power dynamics in AI-assisted development, emphasizing human agency and control. It could reshape how developer tools are designed and how teams adopt AI, fostering collaborative environments where humans remain the decision-makers. Udell's criticism stems from agents creating unreviewable pull requests. He advocates for agentic software development where agents act as transparent team members, not black boxes that obscure the process.

rss · Simon Willison · Jun 28, 21:57

**Background**: The phrase 'human in the loop' traditionally describes systems where human judgment is integrated into an AI's decision process. Agentic AI refers to autonomous agents capable of planning and executing tasks. In software development, such agents can automate coding but often generate complex, hard-to-review changes. Jon Udell is a respected technologist known for insightful commentary on software practices.

<details><summary>References</summary>
<ul>
<li><a href="https://agentintheloop.org/">AGENT In The Loop 2.0 | The Agentic Era</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#ai-agents`, `#software-development`, `#human-in-the-loop`, `#developer-tools`, `#technology-philosophy`

---

<a id="item-8"></a>
## [EML Trees are Universal Approximators](https://www.reddit.com/r/MachineLearning/comments/1uipl1t/eml_trees_are_universal_approximators_r/) ⭐️ 8.0/10

A new paper proves that EML-type trees, which represent elementary functions through composition, are universal approximators capable of densely approximating functions in continuous and Sobolev spaces, with explicit constructive proofs provided. This result establishes a theoretical foundation for using EML trees in machine learning function approximation, potentially influencing the design of architectures that leverage elementary function composition for tasks like symbolic regression or hardware-friendly neural networks. The proof explicitly constructs EML representations for polynomials and hyperbolic tangent, and handles the natural logarithm's domain issues with sign-based decompositions; additionally, the EML function is generalized with learnable parameters.

reddit · r/MachineLearning · /u/JoeGermany · Jun 29, 11:16

**Background**: EML trees are a compositional representation where elementary functions (like exponentials, logarithms, and trigonometric functions) are combined to form more complex functions. Universal approximation theorems are foundational in machine learning, stating that a model can approximate any continuous function arbitrarily closely given enough capacity. Sobolev spaces are function spaces equipped with norms that account for derivatives, widely used in the analysis of partial differential equations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Brumbelow/uninum/blob/main/docs/eml_explained.md">uninum/docs/ eml _explained.md at main · Brumbelow/uninum · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sobolev_space">Sobolev space</a></li>

</ul>
</details>

**Tags**: `#universal approximation theorem`, `#EML trees`, `#function approximation`, `#mathematical proof`, `#machine learning theory`

---

<a id="item-9"></a>
## [Rocket Lab Acquires Iridium in Historic Deal](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 7.0/10

Rocket Lab announced the acquisition of Iridium Communications, creating a fully integrated space company that combines launch services, satellite manufacturing, and satellite operations. This acquisition secures valuable spectrum licenses and a profitable satellite business, while providing Rocket Lab with a guaranteed baseline of launches, similar to SpaceX's strategy with Starlink. Iridium operates a constellation of 66 low-Earth orbit satellites, and the deal gives Rocket Lab ownership of these assets and associated spectrum. Financial terms were not disclosed in the provided summary.

hackernews · everfrustrated · Jun 29, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48719485)

**Background**: Iridium Communications is a satellite communications company providing global voice and data coverage through its LEO satellite network. Rocket Lab, originally from New Zealand, specializes in small satellite launches and satellite manufacturing. This acquisition marks a significant vertical integration move in the space industry.

**Discussion**: Community reactions are mixed: some praise the strategic move to secure regular launches and spectrum, while others raise concerns about increasing space debris. A few comment on Rocket Lab's shift from a New Zealand identity to an American one.

**Tags**: `#space`, `#acquisition`, `#satellites`, `#RocketLab`, `#Iridium`

---

<a id="item-10"></a>
## [Ornith-1.0: Open-Source Self-Improving Model for Agentic Coding](https://github.com/deepreinforce-ai/Ornith-1) ⭐️ 7.0/10

DeepReinforce has launched Ornith-1.0, an open-source model designed for autonomous agentic coding with claimed self-improvement capabilities. It offers multiple sizes—9B, 31B, 35B MoE, and 397B MoE—built on Gemma 4 and Qwen 3.5 architectures. This release pushes open-source models into the agentic coding arena, offering a free alternative to commercial coding agents. If its self-improvement claims prove robust, it may inspire new approaches to model self-enhancement. The model is available in four sizes, with the largest being a 397B MoE. While MIT licensed, it is built on Gemma 4 and Qwen 3.5, and early community testing indicates it performs well on benchmarks but suffers from hallucination in chat and limited unique bug detection.

hackernews · danboarder · Jun 29, 17:16 · [Discussion](https://news.ycombinator.com/item?id=48722052)

**Background**: Agentic coding involves AI agents that autonomously plan, write, test, and debug code with minimal human intervention. Self-improving models aim to enhance their own capabilities iteratively, a concept often discussed in the context of recursive self-improvement. Qwen and Gemma are open-weight LLMs from Alibaba and Google, respectively, frequently used as base models for fine-tuning on specific tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen">Qwen (Qwen) - Hugging Face</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some praise its creative coding solutions and acceptability as a Qwen fine-tune, while others dismiss it as 'benchmaxxed' and report hallucination issues. Doubts linger about the authenticity of its self-improvement mechanism, and the lack of a promised 31B version was also noted.

**Tags**: `#open-source`, `#ai-models`, `#agentic-coding`, `#self-improving`, `#llm`

---

<a id="item-11"></a>
## [Cerebras-OpenAI $20B Deal Effectively Kills API Waitlist for Others](https://www.reddit.com/r/MachineLearning/comments/1uiqhiv/cerebras_openai_deal_capacity_has_effectively/) ⭐️ 7.0/10

A startup reveals that Cerebras's inference API waitlist has become functionally infinite due to OpenAI's $20 billion chip deal, which has claimed the bulk of near-term capacity, leaving no compute for other users. This situation exposes how hyperscaler deals can monopolize specialized AI hardware, squeezing out smaller players and potentially reducing innovation as access to high-throughput inference becomes concentrated among a few large firms. The startup required inference with tight p95 latency constraints and sustained 1-2k tokens/second throughput, which Cerebras's wafer-scale ASICs are designed to deliver. The deal's pre-allocation leaves virtually no capacity for other API users, making the waitlist indefinite.

reddit · r/MachineLearning · /u/Kortopi-98 · Jun 29, 12:00

**Background**: Cerebras Systems produces wafer-scale AI accelerators (like the CS-2) that use massive ASIC-based chips optimized for AI training and inference. Inference ASICs are custom hardware designed to run trained models efficiently. P95 latency is a key metric for real-time services, representing the latency threshold that 95% of requests meet, ensuring consistent performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.fortuneindia.com/technology/what-is-cerebras-and-why-is-everyone-suddenly-talking-about-it-explained/137202">What is Cerebras and why is everyone suddenly talking about it: Explained</a></li>
<li><a href="https://oneuptime.com/blog/post/2025-09-15-p50-vs-p95-vs-p99-latency-percentiles/view">P50 vs P95 vs P99 Latency Explained: What Each Percentile Tells You</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#Cerebras`, `#OpenAI`, `#inference`, `#startups`

---

<a id="item-12"></a>
## [Minimal Interactive Transformer Visualizes Forward Pass with Editable Weights](https://www.reddit.com/r/MachineLearning/comments/1uhw7fu/i_shrank_a_transformer_until_every_number_fitted/) ⭐️ 7.0/10

A software engineer created a single-file interactive web tool that shrinks a transformer to minimal size—6-word vocabulary, 3-dimensional embeddings, one attention head, one block—and lets users edit all weights and word vectors while seeing every computational step update in real time. This tool gives learners a concrete, hands-on way to understand the inner workings of transformers, making the forward pass completely transparent and interactive—something that is usually hidden behind high-level APIs. The transformer uses only a 6-word vocabulary and 3-dimensional embeddings, with a single attention head and one block; weights are fully editable and the entire forward pass recalculates instantly; the model is untrained and demonstrates the role of training by turning predictions to nonsense when weights are randomized.

reddit · r/MachineLearning · /u/DanielMoGo · Jun 28, 12:35

**Background**: Transformers process sequences using self-attention, where each token computes Query (Q), Key (K), and Value (V) vectors to decide which other tokens to attend to. The dot-product of Q and K gives attention scores, which are scaled and passed through softmax to obtain attention weights. A causal mask prevents attending to future tokens during autoregressive generation. The attended values are then passed through a feed-forward network to produce the next layer's representations, ultimately yielding logits and probabilities for the next token.

<details><summary>References</summary>
<ul>
<li><a href="https://www.billparker.ai/2024/10/transformer-attention-simple-guide-to-q.html">Transformer Attention: A Guide to the Q, K, and V Matrices</a></li>
<li><a href="https://machinelearningmastery.com/a-gentle-introduction-to-attention-masking-in-transformer-models/">A Gentle Introduction to Attention Masking in Transformer Models - MachineLearningMastery.com</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#education`, `#interactive`, `#machine learning`, `#visualization`

---

<a id="item-13"></a>
## [Proposal for a native graphical shell for SSH](https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html) ⭐️ 6.0/10

Marcus Lewis proposes a native graphical shell for SSH that hosts web-based graphical apps on the server, accessible over SSH with an API for app discovery and inter-app communication. This could streamline remote server management and access to internal web tools, potentially offering a more integrated alternative to terminal-only SSH sessions, though the community questions its necessity given existing solutions. The shell uses private HTTP servers over SSH tunnels, allowing apps to register as handlers for file types (e.g., a text editor), and is intended as an alternative to command-line apps.

hackernews · mrcslws · Jun 29, 15:42 · [Discussion](https://news.ycombinator.com/item?id=48720758)

**Background**: SSH (Secure Shell) is a protocol for secure remote access, typically used for command-line shells. Graphical access over SSH has existed for decades via X11 forwarding, which tunnels X Window System traffic. Modern alternatives include web-based management tools like Cockpit and browser-based SSH clients using WebSockets.

<details><summary>References</summary>
<ul>
<li><a href="https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html">A native graphical shell for SSH | Marcus Lewis</a></li>
<li><a href="https://news.ycombinator.com/item?id=48720758">A native graphical shell for SSH | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shell_(computing)">Shell (computing) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are largely skeptical, viewing the proposal as a solution in search of a problem. Many point out existing options like X11 forwarding, Cockpit, and web apps, and question the need for a new shell. Some appreciate the frontend/backend separation but argue it's not novel.

**Tags**: `#SSH`, `#graphical-interface`, `#remote-access`, `#innovation`, `#web-development`

---

<a id="item-14"></a>
## [HTML Table Extractor Tool Released by Simon Willison](https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything) ⭐️ 6.0/10

Simon Willison released a paste-conversion tool that extracts tables from rich text and exports them as HTML, Markdown, CSV, TSV, or JSON. An update added the ability to search Wikipedia and import tables directly via the Wikipedia API. This tool streamlines the extraction of tabular data from web pages, saving time for data analysts, journalists, and anyone who needs to reuse web-based tables without manual formatting or scraping. The tool uses browser paste events to capture embedded HTML tables. The Wikipedia integration leverages the page's CORS-enabled API endpoint, and the feature was developed with assistance from Codex.

rss · Simon Willison · Jun 29, 23:38

**Background**: Rich text pasting from browsers includes underlying HTML formatting. CORS (Cross-Origin Resource Sharing) allows web applications to request content from other domains. Wikipedia offers an API that returns parsed HTML for any page, enabling automated table extraction.

**Tags**: `#tools`, `#HTML`, `#tables`, `#data extraction`, `#web scraping`

---

<a id="item-15"></a>
## [Why NCE Over Direct Negative Sampling in Instance Learning?](https://www.reddit.com/r/MachineLearning/comments/1uj8nse/loss_functions_in_instance_representation/) ⭐️ 6.0/10

A Reddit user questioned why Noise Contrastive Estimation (NCE) is used to approximate the denominator in non-parametric softmax for instance representation learning instead of directly approximating the denominator, and asked about its theoretical connection to density estimation. This question addresses a core technique in scalable representation learning; clarifying NCE's advantages over direct approximation can inform better loss design and improve computational efficiency when training large models on massive datasets. The user references specific equations from Wu et al., noting that NCE still estimates the denominator (via Eq. 8) and raises doubts about its necessity; they mention that direct denominator approximation may introduce bias, and that NCE's gradients asymptotically match those of the negative log-likelihood as the number of noise samples m increases.

reddit · r/MachineLearning · /u/No_Balance_9777 · Jun 29, 23:34

**Background**: In instance representation learning, each instance is treated as a separate class, requiring a softmax over the entire dataset—a non-parametric softmax—which is computationally infeasible for large n. Noise Contrastive Estimation (NCE) bypasses this by learning to distinguish real data from artificially generated noise, thereby avoiding explicit normalization. It reformulates the density estimation problem into a binary classification task and is provably consistent, with its gradient converging to the true likelihood gradient as noise samples increase.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@weidagang/demystifying-noise-contrastive-estimation-nce-in-machine-learning-32ded05401f4">Demystifying Neural Networks: Noise Contrastive Estimation (NCE)</a></li>
<li><a href="https://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf">PDF Noise-contrastive estimation: A new estimation principle for ...</a></li>

</ul>
</details>

**Tags**: `#Loss Functions`, `#Noise Contrastive Estimation`, `#Representation Learning`, `#Machine Learning Theory`, `#Softmax`

---

<a id="item-16"></a>
## [Swordfighting Dataset Aims to Improve Thin-Object Tracking](https://www.reddit.com/r/MachineLearning/comments/1uivddx/i_do_historical_swordfighting_and_noticed_ai/) ⭐️ 6.0/10

A HEMA practitioner is building an open dataset of synchronized multi-view (120/240fps) high-speed swordfighting clips, annotated with keypoints, biomechanics, and occlusion data, and is seeking feedback on the schema to ensure its usefulness for thin-object tracking and Sim2Real transfer. Thin-object tracking and Sim2Real transfer are known bottlenecks in computer vision and robotics; this novel dataset targets extreme motion and heavy occlusion, potentially advancing embodied AI, sports analytics, and AR/VR. The planned dataset contains 100 hyper‑trimmed clips captured at 120/240fps, with annotations including 2D keypoints (wrists, head, sword guard, tip), segmentation masks, biomechanical metadata, and CV hazard ratings, all in a JSON schema. It is currently a placeholder on Hugging Face and has not yet been captured.

reddit · r/MachineLearning · /u/fonssagrives · Jun 29, 15:16

**Background**: Sim2Real (simulation-to-reality) transfer is a central challenge in robot learning, where policies trained in simulation often fail in the real world. Thin-object tracking refers to the difficulty of tracking objects with very small cross-sections in video, like fast-moving swords, due to motion blur and low pixel coverage. HEMA (Historical European Martial Arts) is a modern practice of reviving historical swordfighting techniques. Multi-view setups with high frame rates help reduce occlusion and motion blur.

<details><summary>References</summary>
<ul>
<li><a href="https://sim-2-real.com/">Sim2Real | Simulation-to-Real Transfer for Robotics</a></li>
<li><a href="https://www.ultralytics.com/glossary/object-tracking">What is Object Tracking? Computer Vision Guide | Ultralytics</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#dataset`, `#motion tracking`, `#thin-object detection`, `#Sim2Real`

---