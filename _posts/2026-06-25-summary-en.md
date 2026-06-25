---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 38 items, 21 important content pieces were selected

---

1. [Anthropic Accuses Alibaba of Illicit Claude AI Extraction](#item-1) ⭐️ 9.0/10
2. [OpenAI and Broadcom debut Jalapeño inference chip](#item-2) ⭐️ 9.0/10
3. [Qualcomm Acquires Modular to Challenge NVIDIA's CUDA Dominance](#item-3) ⭐️ 8.0/10
4. [45°C Liquid Cooling Cuts Data Center Water Use to Nearly Zero](#item-4) ⭐️ 8.0/10
5. [Superhuman Self-Play RL Agent for Generals.io Reaches #1 Rank](#item-5) ⭐️ 8.0/10
6. [DeepSWE: A Contamination-Free Benchmark for AI Code Generation](#item-6) ⭐️ 8.0/10
7. [Blogging Can Just Be Stating the Obvious](#item-7) ⭐️ 7.0/10
8. [RubyLLM: A Ruby framework for all major AI providers](#item-8) ⭐️ 7.0/10
9. [Computer use in Gemini 3.5 Flash](#item-9) ⭐️ 7.0/10
10. [New Fund Aims to End Respiratory Infections](#item-10) ⭐️ 7.0/10
11. [Simon Willison Converts MDN Browser Compat Data to SQLite](#item-11) ⭐️ 7.0/10
12. [LLM-Generated Applications Lead to Accidental Anonymity, Says Tom MacWright](#item-12) ⭐️ 7.0/10
13. [Datasette 1.0a35 Adds Table Creation and Alteration](#item-13) ⭐️ 7.0/10
14. [Curated OCR Hub on Papers with Code Featuring Baidu and Mistral](#item-14) ⭐️ 7.0/10
15. [LuaJIT 3.0 Proposed Syntax Extensions Spark Debate](#item-15) ⭐️ 6.0/10
16. [Today's PR Spam Mirrors Early 2000s Email Spam](#item-16) ⭐️ 6.0/10
17. [OPFS + Pyodide Test Harness for Persistent Browser SQLite Editing](#item-17) ⭐️ 6.0/10
18. [MuJoFil: GPU-Native Simulator for Vision RL with Newton and Filament](#item-18) ⭐️ 6.0/10
19. [High Dimensional Dynamic RoPE Embedding Achieves Faster Convergence](#item-19) ⭐️ 6.0/10
20. [Compiled LLM Inference Pricing Reveals Dramatic Caching Cost Variations](#item-20) ⭐️ 6.0/10
21. [Are Model Security Risks (Extraction, Poisoning) Tested in Production?](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Accuses Alibaba of Illicit Claude AI Extraction](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 9.0/10

Anthropic accused Alibaba of using nearly 25,000 fraudulent accounts to query the Claude API over 28.8 million times between April 22 and June 5, 2026, in a large-scale model extraction campaign that distilled Claude's capabilities into its own AI model. This incident highlights the growing threat of model extraction attacks on commercial LLM APIs, where even large organizations may resort to illicit distillation, potentially undermining intellectual property and trust in AI services globally. The alleged distillation likely used Claude's outputs to fine-tune Alibaba's own models via Reinforcement Learning from AI Feedback (RLAIF), and involved a black market where resellers offered Claude tokens at 70-90% discounts by exploiting pooled accounts and reselling reasoning traces.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Model extraction attacks involve an adversary querying a target model's API to collect input-output pairs, then training a surrogate model that mimics the target. Knowledge distillation is a legitimate technique for transferring knowledge from a large teacher model to a smaller student, but doing so without authorization violates terms of service. This case is an alleged large-scale, organized effort involving fraudulent accounts and API abuse.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2508.15031">[2508.15031] A Systematic Survey of Model Extraction Attacks ... Model Extraction Attacks and Defenses for Large Language Models Model Extraction Attacks and Defenses | Secure Systems Group A Comprehensive Survey of Model Extraction Attacks: Current ... A Survey on Model Extraction Attacks and Defenses for Large ... Model Extraction Attacks: How Adversaries Steal AI via the API</a></li>
<li><a href="https://labrai.github.io/KDD2025_Tutorial/files/KDD25_Tutorial_MEA_LLM_July_30.pdf">Model Extraction Attacks and Defenses for Large Language Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>

</ul>
</details>

**Discussion**: Comments explain two distillation methods and the black-market token resale scheme. Some question whether distillation is wrongful or accounts are truly fraudulent when paid, while others note resold tokens and payment fraud undermine legitimacy. Historical parallels to GUI copying are drawn, and skepticism is expressed about large models trained on public data claiming IP theft.

**Tags**: `#ai`, `#security`, `#distillation`, `#intellectual-property`, `#china`

---

<a id="item-2"></a>
## [OpenAI and Broadcom debut Jalapeño inference chip](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI unveiled its first custom AI inference chip, code-named Jalapeño, built in partnership with Broadcom and manufactured by TSMC, targeting LLM inference with improved efficiency and scale. This strategic move into custom silicon reduces OpenAI's dependence on NVIDIA GPUs, potentially lowering costs and improving performance for AI services, and signals a broader shift in the AI hardware ecosystem. The chip is a massive reticle-sized ASIC with HBM memory, developed in a nine-month cycle aided by OpenAI's own models, and is optimized for high-throughput, low-latency inference, particularly for reasoning and agentic workloads.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference chips are specialized processors that efficiently run trained AI models for real-world tasks. Custom silicon is tailor-made for specific applications, offering better performance and efficiency than general-purpose chips. OpenAI previously relied on NVIDIA GPUs for inference. Broadcom provides ASIC design expertise, while TSMC fabricates the chips.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle">Broadcom and OpenAI unveil custom-built Jalapeño inference processor — OpenAI's first chip is a massive reticle-sized ASIC built in an ultra-fast nine-month development cycle | Tom's Hardware</a></li>

</ul>
</details>

**Discussion**: Comments skepticism about marketing claims of AI-accelerated design; confirmation that TSMC manufactures the chip; speculation on future chips with weights hardwired; comparisons to Google TPUs and startups like Taalas burning models into silicon.

**Tags**: `#AI`, `#hardware`, `#OpenAI`, `#custom-chip`, `#inference`

---

<a id="item-3"></a>
## [Qualcomm Acquires Modular to Challenge NVIDIA's CUDA Dominance](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm has announced the acquisition of AI startup Modular for approximately $4 billion, aiming to leverage its Mojo programming language and MAX compiler stack as a cross-platform alternative to NVIDIA's CUDA for AI inference. This acquisition could disrupt NVIDIA's lock-in on AI software by offering an open-source-friendly ecosystem for diverse hardware, potentially reducing costs and increasing flexibility for edge and inference applications. Modular's Mojo language is built on MLIR rather than LLVM, enabling high-performance kernels across CPUs, GPUs, and ASICs, but its compiler remains closed-source until a planned open-source release in fall 2026.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Modular was founded by Chris Lattner, creator of LLVM and Swift, to simplify AI development. Mojo combines Python-like syntax with C++-level performance, while the MAX compiler stack targets heterogeneous hardware such as GPUs and TPUs. The move reflects industry efforts to break free from NVIDIA's proprietary CUDA ecosystem, especially for inference on emerging ARM and RISC-V chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo - Modular</a></li>

</ul>
</details>

**Discussion**: Comments express disappointment that Mojo may never become truly cross-platform, akin to past efforts like SYCL. Many see strategic value for Qualcomm's AI push, especially for ARM-based inference, with some noting the timing after China's ARM-powered supercomputer topped the Top500 list, signaling a broader industry shift.

**Tags**: `#AI`, `#acquisition`, `#compiler`, `#cross-platform`, `#Qualcomm`

---

<a id="item-4"></a>
## [45°C Liquid Cooling Cuts Data Center Water Use to Nearly Zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA has unveiled a new liquid cooling architecture for its Rubin-generation AI data centers that uses direct-to-chip cooling with coolant temperatures up to 45°C, achieving 100% liquid cooling with no fans and drastically reducing water consumption. This design enables near-zero water use and makes waste heat easier to reuse for purposes like district heating. This breakthrough significantly lowers the environmental footprint of AI data centers, which consume vast amounts of water and electricity, and opens up practical synergies such as providing free heat to local communities, turning data centers into potential community assets. The system is entirely fanless and relies on a closed-loop direct-to-chip design that can sustain operation at up to 45°C coolant temperature, but efficiency depends on favorable outside climates; detailed climate-performance correlations were not provided.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Traditional data centers use air conditioning and water evaporation for cooling, consuming large amounts of water and energy. Liquid cooling improves efficiency but often still uses water for heat rejection. By allowing coolant temperatures as high as 45°C, the system can use dry coolers that reject heat directly to the air without water loss, and the warmer waste heat becomes suitable for other uses like building heating.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/">Hotter Than a Hot Tub: The 45°C Breakthrough to Cool AI’s Biggest Machines | NVIDIA Blog</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers/">NVIDIA Unveils 45 ° C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.networkworld.com/article/4149069/why-ai-rack-densities-make-liquid-cooling-nonnegotiable.html">Why AI rack densities make liquid cooling ... | Network World</a></li>

</ul>
</details>

**Discussion**: Commenters noted the exciting potential for district heating synergy but questioned what exactly is innovative versus existing high-temperature liquid cooling systems. Some requested more detail on climate dependency, while one user pointed out that pump temperature limits may constrain real-world deployment.

**Tags**: `#liquid cooling`, `#data centers`, `#sustainability`, `#waste heat recovery`, `#NVIDIA`

---

<a id="item-5"></a>
## [Superhuman Self-Play RL Agent for Generals.io Reaches #1 Rank](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A self-play reinforcement learning agent for Generals.io achieved superhuman performance and reached #1 on the 1v1 leaderboard, using behavior cloning, RL fine-tuning, and a JAX-based Vision Transformer. This demonstrates a scalable approach with JAX and ViT that avoids heavy reliance on human priors, offering a practical blueprint for superhuman agents in other imperfect-information RTS games. The agent was originally prototyped with NumPy/Torch and a CNN, then reimplemented with a JAX-based Vision Transformer; the detailed blog post covers dead ends, design decisions, and lessons learned, with open-source code including a fast JAX simulator.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is a fast-paced multiplayer real-time strategy game where players capture territory and eliminate opponents. Self-play reinforcement learning is a technique where an agent improves by playing against itself, as used in AlphaZero. Vision Transformers (ViTs) are transformer architectures for images that process patches, offering higher capacity than convolutional neural networks.

<details><summary>References</summary>
<ul>
<li><a href="https://generals.io/">generals.io</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#self-play`, `#Generals.io`, `#Vision-Transformer`, `#JAX`

---

<a id="item-6"></a>
## [DeepSWE: A Contamination-Free Benchmark for AI Code Generation](https://www.reddit.com/r/MachineLearning/comments/1ue0hlp/deepswe_new_benchmark_looking_at_how_well_todays/) ⭐️ 8.0/10

DeepSWE is a new benchmark for software engineering tasks, featuring contamination-free problems written from scratch, high diversity across 91 repositories and 5 languages, and behavior-based verification. It provides a more accurate and realistic evaluation of frontier coding agents, addressing key gaps in existing benchmarks and potentially guiding development of more capable AI programming tools. Compared to SWE-bench Pro, DeepSWE tasks have prompts about half the length but require 5.5 times more code output, with hand-written verifiers ensuring reliable assessment of software behavior rather than implementation specifics.

reddit · r/MachineLearning · /u/we_are_mammals · Jun 24, 02:03

**Background**: Test set contamination occurs when models are unintentionally trained on benchmark data, inflating scores. SWE-bench Pro is a prior software engineering benchmark that also addresses contamination but may have limitations in diversity and task realism. DeepSWE builds on this by creating entirely new tasks and using behavior-focused verification. Frontier models are the most advanced AI systems that push the boundaries of capability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.16941">[2509.16941] SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1m8ud84/a_contaminationfree_coding_benchmark_shows_ai_may/">A contamination-free coding benchmark shows AI may not be as ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**Tags**: `#code-generation`, `#benchmark`, `#software-engineering`, `#evaluation`, `#machine-learning`

---

<a id="item-7"></a>
## [Blogging Can Just Be Stating the Obvious](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/) ⭐️ 7.0/10

Jim Nielsen’s blog post argues that blogging about seemingly obvious insights is valuable because ideas that feel clear to the writer may be fresh or resonant to others, often due to the curse of knowledge. It emphasizes that sharing fundamental ideas is important even when they appear self-evident. This perspective validates that even simple revelations can have a significant impact, encouraging more people to blog without fear of not being novel. It promotes wider knowledge sharing and helps bridge gaps in understanding across different experience levels. The post centers on the curse of knowledge—a bias where knowing something makes it hard to imagine not knowing it—and notes that there is always a new audience encountering ideas for the first time, making restating fundamentals worthwhile.

hackernews · Curiositry · Jun 24, 23:46 · [Discussion](https://news.ycombinator.com/item?id=48666927)

**Background**: The curse of knowledge is a cognitive bias that makes it difficult for experts to communicate ideas to novices because they overestimate what others know. In blogging, writers may refrain from posting basic insights, assuming they are obvious to everyone, when in fact they could be valuable to many. This bias often leads to under-sharing of foundational knowledge.

**Discussion**: Community comments overwhelmingly agree, with users sharing experiences of simple posts resonating widely. They reinforce the curse of knowledge idea and observe that stating the obvious can still earn upvotes, highlighting that there is always a new cohort of readers.

**Tags**: `#blogging`, `#communication`, `#knowledge-sharing`, `#writing`, `#community`

---

<a id="item-8"></a>
## [RubyLLM: A Ruby framework for all major AI providers](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM, a Ruby framework for integrating multiple AI providers, has gained attention for its ease of use, but users report issues with caching, observability, and maintainer responsiveness. It fills a gap in Ruby's AI ecosystem, enabling thousands of Ruby developers to build AI-powered applications with a unified interface. Notable technical issues include broken caching for xAI, retry logic that deletes model history hindering observability, and initially missing native Responses API support, though it may now be added. Maintenance concerns involve unreviewed PRs and code rewrites.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: RubyLLM provides a streamlined API for interacting with LLMs from providers like OpenAI and Anthropic. Ruby, known for Ruby on Rails, has fewer mature AI/LLM libraries compared to Python, so RubyLLM aims to bring easy AI integration to Ruby developers.

**Discussion**: Overall sentiment is positive regarding usability, with comparisons to Vercel's AI framework. However, users express frustration over maintainer engagement, bugs like caching failures, and lack of proper observability. Some have built additional tools on top, like the Raix gem.

**Tags**: `#ruby`, `#ai`, `#llm`, `#framework`, `#open-source`

---

<a id="item-9"></a>
## [Computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google has integrated computer use capability directly into Gemini 3.5 Flash as a built-in tool, allowing the model to interact with computer interfaces. Previously only available as a standalone model, this marks a shift in accessibility for agentic tasks. This integration makes computer use more accessible to developers, potentially streamlining the automation of GUI-based workflows. However, reliability issues could hinder enterprise adoption and user trust. Gemini 3.5 Flash now supports computer use alongside code execution, search, and function calling. Early tests show it can make critical errors like running destructive commands and may refuse tasks after repeated failures.

hackernews · swolpers · Jun 24, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48662999)

**Background**: Computer use allows AI models to control a mouse and keyboard to operate software with graphical user interfaces. Gemini 3.5 Flash is a cost-effective and fast model from Google, part of the Gemini family. This capability was previously introduced by competitors like Anthropic's Claude, and integrating it into Flash aims to offer it at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/">Introducing computer use in Gemini 3.5 Flash</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.5 Flash — Google DeepMind</a></li>
<li><a href="https://thenextweb.com/news/google-gemini-3-5-flash-computer-use-built-in-tool">Gemini 3.5 Flash can now see and control your screen, and Google wants enterprises to trust it</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely critical, with reports of Gemini giving up on tasks after errors, running `git reset --hard` without prompting, and lacking MCP support. Users compare it unfavorably to Claude and GPT for coding tasks, and express desire for a reliable Gemini coding agent.

**Tags**: `#ai`, `#google`, `#gemini`, `#computer-use`, `#hackernews`

---

<a id="item-10"></a>
## [New Fund Aims to End Respiratory Infections](https://blog.interceptfund.com/p/ending-respiratory-infections) ⭐️ 7.0/10

The Intercept Fund announced a new philanthropic initiative focused on ending respiratory infections, as detailed in a recent blog post. Respiratory infections cause billions of illnesses and significant mortality annually; this fund could accelerate prevention and treatment, especially for vulnerable groups. The initiative highlights air quality improvements and new preventatives, though specific funding amounts and timelines are not yet disclosed.

hackernews · EthanFantl · Jun 25, 01:14 · [Discussion](https://news.ycombinator.com/item?id=48667588)

**Background**: Respiratory infections like colds, flu, and COVID-19 are a top global health burden, often leading to severe outcomes in immunocompromised people. The pandemic underscored long-term effects such as long COVID and the need for better indoor air quality. Philanthropic funds often bridge gaps in public health infrastructure.

**Discussion**: Commenters shared personal tragedies, like a girlfriend dying from metapneumovirus, and debated the adequacy of $500M versus space budgets. Many expressed hope for air cleaning technologies while questioning the accuracy of illness statistics and calling for greater systemic investment.

**Tags**: `#public health`, `#respiratory infections`, `#long-covid`, `#air quality`, `#philanthropy`

---

<a id="item-11"></a>
## [Simon Willison Converts MDN Browser Compat Data to SQLite](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison has released a new tool that converts Mozilla's browser compatibility data into a SQLite database, hosted on GitHub with open CORS headers for easy integration and exploration via Datasette Lite. This provides developers with offline and programmatic access to browser compatibility data, simplifying integration into custom tools and workflows, and demonstrates effective AI-assisted development using Claude and GPT-5.5. The 66MB database is built using a script generated by Claude Code (Opus 4.8) with sqlite-utils, and a GitHub Actions workflow created by Codex Desktop (GPT-5.5) pushes it to an orphan branch for CDN compatibility.

rss · Simon Willison · Jun 24, 23:59

**Background**: Mozilla's MDN Web Docs maintain a comprehensive repository of browser compatibility data for web technologies. sqlite-utils is a Python library and CLI tool for easily creating and manipulating SQLite databases. GitHub provides CDN hosting with CORS headers for files in regular repositories, enabling direct web access.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library ...</a></li>
<li><a href="https://sqlite-utils.datasette.io/">sqlite-utils</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#browser-compatibility`, `#data-engineering`, `#developer-tools`, `#ai-assisted-development`

---

<a id="item-12"></a>
## [LLM-Generated Applications Lead to Accidental Anonymity, Says Tom MacWright](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright observed that many job applications are now clearly co-written by LLMs, with LLM-generated portfolios and GitHub projects, leading to generic and impersonal candidacies that reveal nothing true about the applicant. This trend highlights the unintended consequence of AI misuse in hiring, where reliance on LLMs strips away personal authenticity and makes it harder for recruiters to distinguish genuine candidates, potentially undermining merit-based evaluation. The critique specifically notes that even portfolio sites and commit messages are LLM-generated, creating an entire chain of synthetic content that fails to communicate the applicant's actual skills or personality.

rss · Simon Willison · Jun 24, 18:13

**Background**: Large Language Models (LLMs) like GPT-4 can generate text that mimics human writing, and their use has spread to job applications, where candidates often ask AI to polish or fully draft resumes, cover letters, and even technical projects, raising concerns about authenticity in hiring.

**Tags**: `#ai`, `#careers`, `#hiring`, `#llm`, `#authenticity`

---

<a id="item-13"></a>
## [Datasette 1.0a35 Adds Table Creation and Alteration](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 introduces web-based interfaces and JSON API endpoints for creating and altering SQLite database tables, allowing users to define columns, constraints, defaults, and foreign keys directly from the UI. This release transforms Datasette from a read-only exploration tool into a more complete database management system, enabling rapid prototyping and direct manipulation of database schemas without external tools. The new endpoints include /<database>/-/create and /<database>/<table>/-/alter, supporting NOT NULL constraints, literal and expression defaults, primary keys, single-column foreign keys, and column reordering. The alter interface also provides a 'Drop table' button. Additionally, template context variables are now documented as a stable API for custom templates.

rss · Simon Willison · Jun 23, 21:34

**Background**: Datasette is an open-source tool by Simon Willison that provides an instant JSON API and a web interface for exploring SQLite databases. Previously, it was limited to read-only operations; any schema changes required external database clients. This release marks a major step toward full database management capabilities within Datasette.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#databases`, `#sqlite`, `#tools`, `#release`

---

<a id="item-14"></a>
## [Curated OCR Hub on Papers with Code Featuring Baidu and Mistral](https://www.reddit.com/r/MachineLearning/comments/1ueiam6/find_the_best_opensource_ocr_models_in_one_place/) ⭐️ 7.0/10

Baidu released Unlimited OCR, a 3B-parameter model using Reference Sliding Window Attention, and Mistral released OCR 4 via API. The revived Papers with Code site now aggregates top OCR benchmarks and open-source models. With a surge in OCR releases, this centralized page simplifies model selection for digitizing documents for agentic RAG and chatbots. It helps practitioners compare performance efficiently, accelerating enterprise adoption of open-source OCR. Baidu's model uses Reference Sliding Window Attention to handle long documents efficiently. Top benchmarks include OlmOCRBench and OmniDocBench; Chandra OCR 2 is a top self-hostable open-source model.

reddit · r/MachineLearning · /u/NielsRogge · Jun 24, 16:26

**Background**: OCR digitizes scanned PDFs. Retrieval-Augmented Generation (RAG) enables language models to answer questions from documents. Agentic RAG uses AI agents to manage the pipeline. Reference Sliding Window Attention limits each token's attention to a fixed window with reference tokens, reducing memory for long sequences.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/reference-sliding-window-attention-r-swa">Reference Sliding Window Attention (R-SWA)</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#benchmarks`, `#open-source`, `#machine-learning`, `#RAG`

---

<a id="item-15"></a>
## [LuaJIT 3.0 Proposed Syntax Extensions Spark Debate](https://github.com/LuaJIT/LuaJIT/issues/1475) ⭐️ 6.0/10

A proposal for LuaJIT 3.0, posted on the project's GitHub repository, suggests adding C-style operators (e.g., && for 'and', || for 'or') and a ternary conditional operator (x ? y : z) to the language. This proposal challenges Lua's core philosophy of simplicity and consistency. If accepted, it could fragment the ecosystem, introduce compatibility issues, and alter the language's identity, potentially affecting its widespread use in gaming and embedded systems. The extensions include logical and bitwise operators in C style and a ternary conditional. Critics note that existing Lua idioms (e.g., 'a and b or c') already cover ternary-like behavior, and adding duplicate syntax would increase complexity without clear benefit.

hackernews · phreddypharkus · Jun 25, 00:41 · [Discussion](https://news.ycombinator.com/item?id=48667336)

**Background**: LuaJIT is a high-performance just-in-time compiler for the Lua language, renowned for its small footprint and used in performance-critical applications like game scripting. Lua itself is celebrated for its minimalist syntax. The proposed changes aim to make the language more familiar to developers from C-like backgrounds, but risk diluting its distinct simplicity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LuaJIT">LuaJIT - Wikipedia</a></li>
<li><a href="https://luajit.org/">The LuaJIT Project</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some suggest alternative syntax like 'if x then y else z' for better readability, while others argue the changes are superficial and undermine Lua's simplicity. Concerns about nested ternaries and code golfing are also raised.

**Tags**: `#LuaJIT`, `#Lua`, `#programming-languages`, `#syntax`, `#language-design`

---

<a id="item-16"></a>
## [Today's PR Spam Mirrors Early 2000s Email Spam](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 6.0/10

A blog post draws a parallel between current pull request spam on open-source platforms and the email spam epidemic of the early 2000s, spotlighting similar patterns and prompting community discussion on reputation mechanisms and maintainer tools. The comparison highlights the escalating burden on open-source maintainers from low-quality PRs and suggests that platforms may need spam-fighting infrastructure similar to email's, potentially reshaping contribution norms. GitHub recently introduced per-repository PR limits to help combat spam; however, effective solutions may require individual-contributor reputation systems, which differ from email's server-level controls.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: In the early 2000s, email spam overwhelmed inboxes until technical measures (like SPF, DKIM, Bayesian filters) and legal frameworks (CAN-SPAM Act) were developed. Open-source projects now face similar floods from auto-generated AI PRs, drive-by tutorial contributions, and promotional spam, wasting maintainer time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/orgs/community/discussions/53233">What should I do about spam issues or pull requests ... - GitHub</a></li>
<li><a href="https://socket.dev/blog/express-js-spam-prs-commoditization-of-open-source">Express.js Spam PRs Incident Highlights the Commoditization ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree on the spam analogy, noting key differences like individual versus organizational reputation. Some express disappointment that the post is an AI tool ad, while others highlight GitHub's recent PR limits as progress. A former email spam fighter shares historical insights.

**Tags**: `#open-source`, `#pull-requests`, `#spam-fighting`, `#github`, `#email-spam`

---

<a id="item-17"></a>
## [OPFS + Pyodide Test Harness for Persistent Browser SQLite Editing](https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything) ⭐️ 6.0/10

Simon Willison created a test harness that integrates the Origin Private File System (OPFS) with Pyodide, allowing experiments with persistent SQLite file editing in the browser for his Datasette Lite application. This exploration could allow Datasette Lite to offer offline, local SQLite editing capabilities, enhancing its utility as a serverless data exploration tool and aligning with the trend of powerful browser-based applications using WebAssembly. The test harness, built with Claude Code for web, is available at tools.simonwillison.net/opfs-pyodide. It leverages the OPFS API for high-performance, isolated file storage and Pyodide's WebAssembly Python runtime to test SQLite persistence across different browsers.

rss · Simon Willison · Jun 23, 18:58

**Background**: The Origin Private File System (OPFS) is a browser API that provides a fast, sandboxed file storage area for web applications, private to each origin. Pyodide is a port of Python to WebAssembly, enabling Python code to run in the browser. Datasette Lite uses Pyodide to run the Datasette server application entirely in the browser, allowing users to explore SQLite databases without any backend server. Adding OPFS could let those databases be edited and saved locally, turning the read-only tool into a full data editor.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system">Origin private file system - Web APIs | MDN</a></li>
<li><a href="https://pyodide.org/en/stable/console.html">pyodide .org/en/stable/console.html</a></li>
<li><a href="https://simonwillison.net/2022/May/4/datasette-lite/">Datasette Lite : a server-side Python web application running in...</a></li>

</ul>
</details>

**Tags**: `#browsers`, `#pyodide`, `#webassembly`, `#datasette`, `#sqlite`

---

<a id="item-18"></a>
## [MuJoFil: GPU-Native Simulator for Vision RL with Newton and Filament](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 6.0/10

MuJoFil is a new open-source simulator that integrates NVIDIA Newton, a GPU-native physics engine based on MuJoCo, with a modified Google Filament rendering engine to enable highly parallelized, high-fidelity vision-based reinforcement learning training directly on GPU. It addresses the limitations of existing simulators like MuJoCo's CPU dependency and NVIDIA Isaac's hardware and licensing barriers, offering an accessible, open-source alternative for vision-based robot policy learning that can accelerate research and development in robotics AI. MuJoFil uses NVIDIA Newton as its physics backend, which is GPU-native and derived from MuJoCo, and leverages a significantly modified Filament engine for parallel rendering across multiple simulations. It supports PBR textures, diverse 3D environment formats like GLB and OpenUSD, and is available via PyPI as mujofil (CPU) and mujofil-warp (GPU, to be renamed mujofil-cuda). However, the project is in early development with expected bugs.

reddit · r/MachineLearning · /u/MT1699 · Jun 24, 19:07

**Background**: MuJoCo (Multi-Joint dynamics with Contact) is a widely used open-source physics engine for robotics simulation, but it runs primarily on CPU, limiting parallelism. NVIDIA Newton is a newer open-source, GPU-accelerated physics engine built on NVIDIA Warp and based on MuJoCo's physics, designed for scalable robot learning. Google Filament is a real-time physically-based rendering (PBR) engine optimized for mobile and desktop. Vision-based reinforcement learning requires fast, realistic rendering to train policies from visual inputs, which has been challenging with existing free tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MuJoCo">MuJoCo - Wikipedia</a></li>
<li><a href="https://github.com/google/filament">GitHub - google/filament: Filament is a real-time physically ...</a></li>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#simulation`, `#computer-vision`, `#GPU-computing`, `#robotics`

---

<a id="item-19"></a>
## [High Dimensional Dynamic RoPE Embedding Achieves Faster Convergence](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 6.0/10

The author introduced HDD-RoPE, a high-dimensional dynamic rotary positional embedding that generalizes RoPE by using larger chunk sizes (e.g., 4) and data-dependent rotation rates, achieving faster convergence than xPos on TinyStories. Positional embeddings are critical for transformer sequence modeling; faster convergence can reduce training costs and indicates potential for better representation learning, possibly leading to improved language model performance. HDD-RoPE splits queries and keys into groups of 4 (yielding 6 rotational axes) instead of pairs, and makes rotation angles dynamic based on layer activations. Code is available on GitHub.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 24, 18:16

**Background**: RoPE is a standard positional encoding that captures relative positions by rotating token pairs. xPos extends RoPE for better extrapolation. HDD-RoPE further generalizes RoPE by treating position as multidimensional and making rotations data-dependent. TinyStories is a common dataset for small language model research.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mikayahlevi/hdd-rope/">GitHub - mikayahlevi/hdd-rope</a></li>
<li><a href="https://arxiv.org/abs/2212.10554">[2212.10554] A Length-Extrapolatable Transformer - arXiv.org GitHub - lucidrains/rotary-embedding-torch: Implementation of ... Positional embeddings — NVIDIA NeMo Framework User Guide XPos Length Extrapolation | lucidrains/rotary-embedding-torch ... Extrapolatable Transformer: Enhanced Position Modeling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rotary_positional_embedding">Rotary positional embedding</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#transformers`, `#positional-embeddings`, `#nlp`, `#research`

---

<a id="item-20"></a>
## [Compiled LLM Inference Pricing Reveals Dramatic Caching Cost Variations](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 6.0/10

A Reddit user compiled public pricing data from seven LLM inference providers, including OpenRouter, DeepSeek, Together AI, Fireworks, and Groq, into a single spreadsheet. The compilation reveals that cached input costs can vary by an order of magnitude across providers for the same model, with cache hits sometimes being tens of times cheaper than cache misses. For developers building agents, RAG pipelines, or multi-turn applications that reuse system prompts or context, caching policies can impact actual costs far more than headline token prices. This compilation helps practitioners choose providers based on real-world cost optimization rather than superficial pricing. The spreadsheet tracks input/output token pricing, context windows, cached input pricing, and supported models, but it is not benchmark data and lacks metrics like throughput, cold-start times, model precision, egress costs, and reliability. Some providers barely document their caching mechanisms, making direct comparison difficult.

reddit · r/MachineLearning · /u/Technomadlyf · Jun 24, 11:28

**Background**: LLM inference providers charge per token for processing prompts and generating responses. Many providers now offer caching for repeated prompt prefixes (also called prompt caching or prefix caching), which can drastically reduce costs when the same context is used across multiple requests. This is especially relevant for retrieval-augmented generation (RAG) systems, where a retrieval step adds external documents to the prompt, and for agents that maintain lengthy system instructions or multi-turn conversation histories.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bentoml.com/llm/inference-optimization/prefix-caching">Prefix caching | LLM Inference Handbook</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/what-is-retrieval-augmented-generation-rag/">What is Retrieval-Augmented Generation (RAG) - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#LLM pricing`, `#inference cost`, `#caching`, `#cost optimization`, `#cloud providers`

---

<a id="item-21"></a>
## [Are Model Security Risks (Extraction, Poisoning) Tested in Production?](https://www.reddit.com/r/MachineLearning/comments/1uddtws/are_model_security_risks_extraction_poisoning/) ⭐️ 6.0/10

A Reddit post by user Xorphian questions whether machine learning teams perform adversarial security testing for model extraction and poisoning before production deployment, noting a perceived lag behind traditional software security reviews. This post underscores a critical gap in ML operations: without adversarial testing, models are vulnerable to intellectual property theft and malicious manipulation, potentially harming businesses and users as AI systems proliferate. The post is a concise inquiry without technical depth, but it specifically names model extraction and poisoning—two well-documented adversarial attack vectors. It does not provide data or solutions, serving purely as a discussion starter.

reddit · r/MachineLearning · /u/Xorphian · Jun 23, 10:52

**Background**: Model extraction attacks let adversaries replicate a model's behavior by querying its API and using the outputs to train a surrogate, potentially exposing proprietary algorithms. Model poisoning alters training data or parameters to embed backdoors or cause targeted misclassification, undermining model integrity. These threats are unique to ML and require specialized testing beyond standard code security. The Reddit post suggests many organizations have not yet adopted such practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.praetorian.com/blog/stealing-ai-models-through-the-api-a-practical-model-extraction-attack/">Stealing AI Models Through the API: A Practical Model Extraction Attack | Praetorian</a></li>
<li><a href="https://owasp.org/www-project-machine-learning-security-top-10/docs/ML10_2023-Model_Poisoning">ML10:2023 Model Poisoning - OWASP Foundation</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/">LLM04:2025 Data and Model Poisoning - OWASP Gen AI Security ...</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#security`, `#adversarial-testing`, `#production-ml`, `#mlops`

---