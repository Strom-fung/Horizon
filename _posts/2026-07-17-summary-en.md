---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 39 items, 26 important content pieces were selected

---

1. [Puter Compiles Firefox to WebAssembly, Enabling In-Browser Execution](#item-1) ⭐️ 9.0/10
2. [Kimi K3: New Open Frontier AI Model with 1M Context](#item-2) ⭐️ 8.0/10
3. [Microsoft Open Sources 1990s Comic Chat IRC Client](#item-3) ⭐️ 8.0/10
4. [LM Studio Bionic: AI Agent Harness for Open Models](#item-4) ⭐️ 8.0/10
5. [New ArXiv Book Covers Mathematical Foundations of Data Science, Emphasizing High-Dimensional Intuition](#item-5) ⭐️ 8.0/10
6. [Progress on Rewriting the Roc Compiler from Rust to Zig](#item-6) ⭐️ 8.0/10
7. [Immersive Linear Algebra Book with Interactive Figures (2015)](#item-7) ⭐️ 8.0/10
8. [Inkling: Open-Weights Multimodal MoE Model from Thinking Machines Lab](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds: Linux Is Not Anti-AI, AI Is a Useful Tool](#item-9) ⭐️ 8.0/10
10. [xAI open-sources Grok Build after data upload backlash](#item-10) ⭐️ 8.0/10
11. [Researcher Bypasses Claude's Web Fetch Protections to Exfiltrate User Data](#item-11) ⭐️ 8.0/10
12. [PnP-CoSMo: Plug-and-Play Multi-Contrast MRI Reconstruction without Raw K-space Data](#item-12) ⭐️ 8.0/10
13. [Schema Harness Achieves 99% on ARC-AGI-3 Using Opus 4.8 and Fable 5](#item-13) ⭐️ 8.0/10
14. [Decoy Font Embeds Hidden Text Revealed by Blurring](#item-14) ⭐️ 7.0/10
15. [Detecting LLM-Generated Texts with Classical Machine Learning](#item-15) ⭐️ 7.0/10
16. [Spot Birds, Not Golf: Offsetting Data Center Water Use with Park Conversions](#item-16) ⭐️ 7.0/10
17. [Quoting Thibault Sottiaux](#item-17) ⭐️ 7.0/10
18. [Mermaid Diagrams Rendered as Unicode Box Art in the Browser](#item-18) ⭐️ 7.0/10
19. [QLoRA's Default Learning Rate (2e-4) Overfits on Small Datasets Under 10k Samples](#item-19) ⭐️ 7.0/10
20. [Disentangling Convolutional Neurons with Hadamard Product Clustering](#item-20) ⭐️ 7.0/10
21. [PyTorch Model 170x Slower on T4 vs A100: Debugging Extreme Bottleneck](#item-21) ⭐️ 7.0/10
22. [Researcher Seeks Collaborators to Scale and Evaluate New Recurrent Architecture DABSN](#item-22) ⭐️ 6.0/10
23. [ECCV's High Registration Fees Spark Student Outcry](#item-23) ⭐️ 6.0/10
24. [AI Memory Systems Should Evolve from Fact-Storing to Inferring User Reasoning Patterns](#item-24) ⭐️ 6.0/10
25. [ExTernD proposes expanded-rank ternary decomposition for near-lossless LLM quantization](#item-25) ⭐️ 6.0/10
26. [Reddit user seeks critical perspectives on JEPA-based world models for robot learning](#item-26) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Puter Compiles Firefox to WebAssembly, Enabling In-Browser Execution](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the Firefox web browser to WebAssembly, enabling it to run entirely within another browser like Chrome. The project used Gecko's single-process support and AI-assisted coding, with an estimated token cost of $25,000 reduced by a subscription plan. This achievement showcases WebAssembly's capability to run complex applications like a full browser, challenging traditional boundaries of web-based execution. It could lead to secure, sandboxed browser environments for testing or legacy access, and highlights the potential of AI-assisted large-scale software compilation. The compiled artifact includes a 233MB gecko.wasm file and 18MB assets; all network traffic is proxied via WebSockets using the Wisp protocol through Puter's servers, which required scaling due to high demand. End-to-end encryption is supported for HTTPS requests, while HTTP requests remain unencrypted.

rss · Simon Willison · Jul 16, 23:34

**Background**: Gecko is the rendering engine behind Firefox, supporting a single-process configuration that simplifies its compilation to WebAssembly. WebAssembly (Wasm) is a low-level binary format that allows code written in languages like C++ to run in web browsers at near-native speed. The Wisp protocol enables multiple TCP/UDP connections to be tunneled over a single WebSocket, overcoming browsers' restriction on opening arbitrary network connections directly.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.mozilla.org/Gecko:Overview">Gecko:Overview - MozillaWiki</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#wasm`

---

<a id="item-2"></a>
## [Kimi K3: New Open Frontier AI Model with 1M Context](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI's Kimi released Kimi K3, an open-source frontier model with a 1 million token context window, 2.8 trillion parameters, and competitive pricing at $3/$15 per million input/output tokens. The release underscores the accelerating commoditization of AI, with Chinese labs offering powerful open models that could reshape market dynamics and drive down prices across the industry. Kimi K3 has 2.8 trillion parameters, a 1M context window, and uses a Mixture-of-Experts architecture. It matches or exceeds benchmarks of other frontier models like Fable/Sol, but with lower pricing. It is available via OpenRouter and API.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Frontier models represent the most advanced AI systems. 'Open' means the model weights are publicly released for anyone to use or modify. A 1M context window allows the model to process extremely long documents in one go. Commoditization refers to the trend where advanced AI becomes widely accessible and undifferentiated, shifting value to infrastructure or applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/commoditization-ai-models-implications-innovation-siddharth-bhalsod-seimf">The Commoditization of AI Models: Implications for Innovation</a></li>
<li><a href="https://codingscape.com/blog/llms-with-largest-context-windows">LLMs with largest context windows</a></li>

</ul>
</details>

**Discussion**: Community discussion focused on cost and commoditization. Some noted the model is expensive for a Chinese offering, while others argued it's part of a strategy to commoditize intelligence and sell infrastructure. Benchmark comparisons and the large parameter count were also highlighted.

**Tags**: `#AI`, `#LLM`, `#Open Models`, `#Chinese AI`, `#Pricing`

---

<a id="item-3"></a>
## [Microsoft Open Sources 1990s Comic Chat IRC Client](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 8.0/10

On July 16, 2026, Microsoft released the source code for Comic Chat, the graphical IRC client from the 1990s that automatically turned chat conversations into comic strips. This release preserves a pioneering piece of internet history, allowing developers to study or revive its unique approach while evoking nostalgia for early online experimentation. Originally created by David Kurlander, Comic Chat featured illustrated characters, speech bubbles, and expressions, and popularized Comic Sans. It used custom IRC protocol commands for character emotions and poses.

hackernews · jervant · Jul 16, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48936426)

**Background**: Internet Relay Chat (IRC) was a popular text-based chat protocol in the 1990s and early 2000s. Microsoft Comic Chat, later renamed Microsoft Chat, was a client that automatically rendered conversations as comic panels, first released with Internet Explorer 3.0 in 1996 and later bundled with Windows. It was notable for its playful, visual approach to online communication, though some IRC purists disliked its non-standard protocol extensions.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/">Microsoft Comic Chat is now open source</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat</a></li>

</ul>
</details>

**Discussion**: Community reaction is largely enthusiastic. Robert Standefer detailed the six-year effort to make the release happen. One commenter shared how Comic Chat inspired their startup, Chogger, a comic creation app for schools. Another recalled that Comic Chat was once reviled by some IRC users for its non-standard protocol extensions, while another praised its experimental spirit. Overall, the sentiment is nostalgic appreciation mixed with technical curiosity.

**Tags**: `#open-source`, `#retro-computing`, `#internet-history`, `#irc`, `#microsoft`

---

<a id="item-4"></a>
## [LM Studio Bionic: AI Agent Harness for Open Models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio has launched Bionic, a new AI agent harness that allows users to orchestrate open-source large language models locally for coding, document creation, and manipulation tasks. This enables greater control over AI agents by keeping data local, reducing reliance on expensive cloud frontier models and addressing privacy and cost concerns for both individual developers and enterprises. Bionic supports flexible model execution—locally, via LM Link for remote models, or through LM Studio Secure Cloud for large frontier open models—and includes features like automatic checkpointing in Work projects and voice input with local transcription.

hackernews · minimaxir · Jul 16, 20:18 · [Discussion](https://news.ycombinator.com/item?id=48939662)

**Background**: An agent harness is the software infrastructure that equips an LLM with tools, memory, and execution loops, enabling it to perform multi-step tasks beyond simple chat. Previously, LM Studio provided a local desktop app for running open models in a chat interface. Bionic extends this into agentic workflows, allowing models to take actions like editing files and running code.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for ... - 9to5Mac</a></li>

</ul>
</details>

**Discussion**: The Hacker News community reacted positively, with early testers praising its usability and compatibility with local models like Qwen3.6 35B, though some noted rough edges. Concerns were raised about LM Studio's evolving business model toward cloud services, while others debated whether Apple might eventually dominate local AI agents. Founder Yagil actively solicited feedback and offered free credits for testing.

**Tags**: `#AI agents`, `#local LLM`, `#open-source models`, `#tool`, `#Hacker News`

---

<a id="item-5"></a>
## [New ArXiv Book Covers Mathematical Foundations of Data Science, Emphasizing High-Dimensional Intuition](https://arxiv.org/abs/2607.11938) ⭐️ 8.0/10

A new ArXiv book, 'Mathematics of Data Science,' offers a detailed look at the mathematical foundations of data science. It emphasizes developing intuition for high-dimensional spaces and statistical reasoning. The book fills a crucial gap in data science education by teaching high-dimensional intuition, which is vital for understanding modern machine learning algorithms and optimization methods. It helps practitioners build a solid statistical foundation to avoid misinterpretations and make better data-driven decisions. The book begins by addressing how intuition fails in high dimensions, discussing phenomena like spikiness and volume concentration and their impact on model training. Community feedback underscores that strong fundamentals in statistics and high-dimensional geometry are more important than ever in modern data science.

hackernews · Anon84 · Jul 16, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48939896)

**Background**: Data science relies heavily on mathematical concepts from linear algebra, probability, statistics, and optimization. In high-dimensional spaces, geometric intuition from two or three dimensions often fails—for example, most of a sphere's volume is concentrated near its surface, and distances become less meaningful. Understanding these properties is essential for designing and interpreting machine learning models and algorithms.

**Discussion**: Community comments are highly positive, with users praising the book's focus on high-dimensional intuition and statistical fundamentals. One commenter emphasizes how crucial it is to explain the breakdown of intuition in high dimensions when teaching data science. Another notes that statistics remains the most important skill for data scientists, far exceeding trendy tools. Overall, the discussion reflects a consensus that solid mathematical and statistical foundations are essential for practical data science.

**Tags**: `#data-science`, `#mathematics`, `#machine-learning`, `#statistics`, `#high-dimensional-geometry`

---

<a id="item-6"></a>
## [Progress on Rewriting the Roc Compiler from Rust to Zig](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

The author reports on the ongoing rewrite of the Roc compiler from Rust to Zig, outlining performance gains, simpler memory management, and faster incremental builds. This move underscores Zig's growing popularity for systems programming, particularly compilers, and reignites debate over the trade-offs between Rust's safety and Zig's simplicity and compilation speed. The rewrite aims for faster development cycles but sacrifices some compile-time safety guarantees; the author acknowledges challenges with unsafe code and memory errors in compiler development.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Roc is a functional programming language whose compiler was originally written in Rust, known for its memory safety. Zig is a systems language emphasizing manual memory management and fast compilation, often compared to C. Rust uses ownership and borrowing to ensure safety at compile time, while Zig relies on runtime checks in debug and release-safe modes, but offers fewer guarantees than Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some argue that code emission in compilers does not inherently require unsafe operations; others question whether Zig's ReleaseSafe mode truly catches use-after-free errors. There is also curiosity about why OCaml was not chosen, and hope that Rust will eventually offer similar fast incremental builds.

**Tags**: `#rust`, `#zig`, `#compilers`, `#programming-languages`, `#systems-programming`

---

<a id="item-7"></a>
## [Immersive Linear Algebra Book with Interactive Figures (2015)](https://immersivemath.com/ila/) ⭐️ 8.0/10

An interactive linear algebra textbook from 2015, featuring dynamic visualizations, is gaining renewed attention and praise for its effective teaching approach. This resource demonstrates the potential of interactive, visual-first education in mathematics, and the discussion connects it to modern AI tools that could accelerate such content creation. The book uses interactive figures to explain linear algebra concepts, and includes features like tooltips; it was created in 2015 but remains clean and effective.

hackernews · srean · Jul 16, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48935951)

**Background**: Linear algebra is a branch of mathematics concerning vector spaces and linear mappings, widely used in engineering, physics, and computer science. Interactive textbooks like this aim to enhance comprehension through visual and hands-on exploration.

**Discussion**: Community feedback is overwhelmingly positive, with users expressing enthusiasm for the interactive approach and hoping for similar books in other subjects. Some note that AI advancements are making it easier to create such content, and a user suggests adding an 'Explain this' feature for any selected text.

**Tags**: `#linear-algebra`, `#education`, `#interactive-visualization`, `#math-education`, `#educational-technology`

---

<a id="item-8"></a>
## [Inkling: Open-Weights Multimodal MoE Model from Thinking Machines Lab](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab released Inkling, a 975B-parameter open-weights multimodal Mixture-of-Experts model under Apache 2.0, trained on 45 trillion tokens across text, images, audio, and video. A smaller 276B-parameter Inkling-Small model is also planned. This release is significant because a notable US AI lab is contributing a large-scale, permissively open-weights model, bolstering the US open-source AI ecosystem and providing a competitive alternative to Chinese open-weight models. The Apache 2.0 license enables broad commercial and research use, especially for fine-tuning on their Tinker platform. Inkling uses a Mixture-of-Experts architecture with 975B total and 41B active parameters, is multimodal, trained on 45T tokens. Thinking Machines Lab admits it is not a frontier model; the accompanying model card is far shorter than industry norms and provides minimal detail on training data.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is a transformer architecture that contains multiple 'expert' subnetworks, with a gating mechanism routing each token to only a subset of experts, enabling efficient scaling. AI model cards are standardized documents that detail a model's capabilities, training data, and performance to ensure transparency. The relatively sparse documentation from Thinking Machines Lab contrasts with typical industry practice.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer">Mixture - of - Experts Transformer</a></li>
<li><a href="https://developer.nvidia.com/blog/enhancing-ai-transparency-and-ethical-considerations-with-model-card/">Enhancing AI Transparency and Ethical Considerations with Model ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#model-release`, `#multimodal`, `#mixture-of-experts`, `#LLM`

---

<a id="item-9"></a>
## [Linus Torvalds: Linux Is Not Anti-AI, AI Is a Useful Tool](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the top-level maintainer of Linux, publicly declared on the Linux media mailing list that Linux is not an anti-AI project and that AI is a useful tool, inviting those who disagree to fork the project or leave. This statement clarifies the official stance of the Linux project on AI, influencing open-source culture and potentially accelerating AI adoption in software development. It signals to the community that AI tools are welcome in Linux development, which could impact contributions and the broader ecosystem. Torvalds emphasized that AI's usefulness is no longer in question, noting that while economic implications remain unclear, anyone who doubts its utility has not used it. The remarks were made in response to discussions on the Linux media mailing list.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linux is the world's most widely used open-source operating system, led by Linus Torvalds since its creation. As top-level maintainer, Torvalds sets the vision for the kernel. Recently, some open-source projects have taken anti-AI stances, but Torvalds' statement aligns Linux with embracing AI as a tool, reflecting his pragmatic approach to technology.

**Tags**: `#Linux`, `#AI`, `#open-source`, `#Linus Torvalds`, `#software development`

---

<a id="item-10"></a>
## [xAI open-sources Grok Build after data upload backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 8.0/10

xAI has released the entire Grok Build codebase under the Apache 2.0 license, containing 844,530 lines of Rust, following community outrage over its CLI tool uploading entire user directories without consent. This transparency move aims to restore user trust after a severe privacy breach, setting a new standard for open-source accountability in AI coding tools and allowing users to run the tool locally. The codebase includes the main system prompt, a self-contained terminal renderer for Mermaid diagrams, and tool implementations imitated from other coding agents; xAI also deleted all previously retained user data and disabled default retention.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is an xAI CLI tool for vibe coding, transforming natural language prompts into code; the controversy erupted when it was discovered that running the tool in a directory could silently upload all its contents to xAI's cloud buckets.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Grok_Build">Grok Build</a></li>
<li><a href="https://x.ai/open-source">Open Source: Grok Build Coding Agent & CLI | SpaceXAI</a></li>

</ul>
</details>

**Discussion**: Users expressed immediate outrage over the privacy violation, with one individual reporting the upload of SSH keys and password database; while some welcomed the open-sourcing and data deletion, others remained skeptical about xAI's earlier handling of sensitive data.

**Tags**: `#open-source`, `#security`, `#xAI`, `#grok`, `#AI`

---

<a id="item-11"></a>
## [Researcher Bypasses Claude's Web Fetch Protections to Exfiltrate User Data](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Security researcher Ayush Paul discovered a method to bypass Claude's web_fetch tool protections, allowing data exfiltration by crafting a website that tricked Claude into navigating through a series of links to leak private user information. This highlights a real-world vulnerability in AI agent safeguards, underscoring the ongoing challenges in preventing prompt injection attacks and data leaks, even with explicit anti-exfiltration measures in place. The attack exploited Claude's ability to follow links in fetched pages, using a Cloudflare-themed ruse to extract the user's name, location, and employer letter by letter; the exploit only targeted requests with 'Claude-User' in the user-agent to avoid detection.

rss · Simon Willison · Jul 15, 14:21

**Background**: The 'lethal trifecta' describes a dangerous combination for AI agents: access to sensitive data, exposure to untrusted input, and the ability to communicate externally. Claude's web_fetch tool was designed to mitigate this by restricting navigable URLs to only those provided by the user or returned from its web_search tool, but the flaw allowed navigation to links embedded in fetched pages. This attack demonstrates how determined adversaries can circumvent such safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>
<li><a href="https://www.osohq.com/learn/lethal-trifecta-ai-agent-security">Understanding the Lethal Trifecta of AI Agents</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>

</ul>
</details>

**Tags**: `#security`, `#ai-safety`, `#claude`, `#data-exfiltration`, `#prompt-injection`

---

<a id="item-12"></a>
## [PnP-CoSMo: Plug-and-Play Multi-Contrast MRI Reconstruction without Raw K-space Data](https://www.reddit.com/r/MachineLearning/comments/1uy2h66/pnpcosmo_a_multicontrast_mri_reconstruction/) ⭐️ 8.0/10

PnP-CoSMo introduces a two-stage plug-and-play framework that learns contrast-invariant content and style representations solely from image-domain MRI data, eliminating the dependency on scarce raw k-space data for training. It achieves competitive performance with state-of-the-art unrolled networks while providing built-in interpretability and generalizability across contrasts and forward operators. This approach removes a major data bottleneck in MRI reconstruction, making advanced deep learning methods more accessible and practical for clinical settings where raw k-space data is often unavailable. Its built-in interpretability and generalization capabilities could accelerate adoption and improve diagnostic quality. The framework's first stage models content and style from paired multi-contrast images without requiring raw k-space measurements; the second stage freezes this model as a prior in iterative reconstruction, supporting flexible undersampling patterns and contrast combinations. It demonstrates performance on par with unrolled networks, which typically need raw k-space data for end-to-end training.

reddit · r/MachineLearning · /u/void_gear · Jul 16, 13:10

**Background**: Multi-contrast MRI captures different tissue properties (e.g., T1, T2 weighting) to aid diagnosis; multi-contrast reconstruction uses correlations between these contrasts to improve image quality from undersampled data. Plug-and-play methods decouple the measurement model from image priors, allowing pre-trained deep learning models to be inserted as regularizers. Unrolled optimization networks unroll iterative algorithms into deep networks trained end-to-end on raw k-space data, which is often difficult to obtain. PnP-CoSMo bypasses this by learning priors from image-domain data only.

<details><summary>References</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/39419362/">Deep plug-and-play MRI reconstruction based on multiple complementary priors - PubMed</a></li>
<li><a href="http://crl.med.harvard.edu/papers/Pouryazdanpanah_DeepPlug.pdf">Deep Plug-and-Play Prior for Parallel MRI Reconstruction</a></li>
<li><a href="https://arxiv.org/abs/2601.17274">Unrolled Neural Networks for Constrained Optimization</a></li>

</ul>
</details>

**Tags**: `#MRI reconstruction`, `#content/style modeling`, `#plug-and-play framework`, `#medical imaging`, `#deep learning`

---

<a id="item-13"></a>
## [Schema Harness Achieves 99% on ARC-AGI-3 Using Opus 4.8 and Fable 5](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 8.0/10

A new inference harness called Schema reaches 99% on the ARC-AGI-3 Public set using Claude Opus 4.8 and Fable 5, without modifying model weights. It improves the inference process by transforming observations, testing predictions, and revising plans. This result demonstrates significant progress towards efficient reasoning in AI agents on a benchmark designed to measure general intelligence, highlighting the potential of inference-time techniques to unlock model capabilities. The harness uses a fixed fallback rule: runs first with Opus 4.8/Sol xhigh, reruns games scoring below 80 with Fable 5/Sol max, and retains the higher score. It achieves 95.35% with GPT-5.6 Sol.

reddit · r/MachineLearning · /u/we_are_mammals · Jul 16, 21:02

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that challenges AI agents to explore novel environments, acquire goals on the fly, and build adaptable world models. Claude Opus 4.8 and Fable 5 are large language models from Anthropic, with Fable 5 being a publicly available version of the advanced Mythos series. A 99% score means the agent can beat almost every game as efficiently as humans.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fable_5">Fable 5</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#arc-agi`, `#benchmark`, `#harness`, `#llms`

---

<a id="item-14"></a>
## [Decoy Font Embeds Hidden Text Revealed by Blurring](https://www.mixfont.com/experiments/decoy-font) ⭐️ 7.0/10

The Decoy Font experiment from mixfont.com introduces a TrueType font where each character contains a hidden message that only becomes visible when the text is blurred, exploiting the different resolutions at which humans and OCR systems perceive text. This highlights a significant perceptual gap between human vision and AI-based optical character recognition, demonstrating how adversarial perturbations can fool machines while remaining decipherable to humans, underscoring vulnerabilities in automated text analysis. The hidden text is embedded via high-frequency details that average out when blurred; AI models like GPT-4, Claude, and Gemini show inconsistent recognition, and simple resizing or scripting can alter what the OCR reads.

hackernews · ray__ · Jul 16, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48936584)

**Background**: Adversarial examples are input perturbations that cause machine learning models to make mistakes while being imperceptible to humans. In OCR, such perturbations can include hidden text or noise that misleads recognition. The Decoy Font is a concrete realization of this concept, packaged as a usable TrueType font, and it has sparked discussion about the robustness of AI vision systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mixfont.com/experiments/decoy-font">Decoy Font: A TTF font that hides what you type - mixfont.com</a></li>
<li><a href="https://www.turbolens.io/blog/2025-12-20-watermarks-and-background-noise-a-silent-ocr-killer">Watermarks and Background Noise: A Silent OCR ... | TurboLens Blog</a></li>

</ul>
</details>

**Discussion**: Commenters acknowledge the cool factor but question practical utility, noting AI can sometimes read the hidden text with prompting, while others view it as a simple level-of-detail trick that can be countered with basic image processing.

**Tags**: `#typography`, `#adversarial-examples`, `#ai-perception`, `#ocr`, `#experimental`

---

<a id="item-15"></a>
## [Detecting LLM-Generated Texts with Classical Machine Learning](https://blog.lyc8503.net/en/post/llm-classifier/) ⭐️ 7.0/10

A recent blog post investigates using classical machine learning techniques, rather than deep learning, to identify LLM-generated text. The approach has sparked debate on its long-term feasibility and alternative metrics like effort. As LLM-generated content floods the internet, reliable detection is crucial for maintaining information integrity, and classical ML could offer a lightweight solution suitable for browser extensions. However, the controversy highlights the inherent difficulty of distinguishing AI from human text as models evolve. The classifier relies on features such as sentence structures and phrasing patterns specific to current LLMs, and its small size enables potential in-browser deployment. Critics argue that such tells are temporary and detection is akin to tarot reading, as future models will learn to avoid them.

hackernews · uneven9434 · Jul 16, 16:41 · [Discussion](https://news.ycombinator.com/item?id=48936880)

**Background**: Classical machine learning encompasses traditional algorithms like logistic regression or support vector machines that use handcrafted features, contrasting with deep learning which learns features automatically. AI text detection is an ongoing arms race; earlier detectors often fail to generalize across different models or domains.

**Discussion**: Community members expressed skepticism about long-term viability, with one calling it 'tarot card reading,' while another proposed measuring writing effort instead of origin. Others were optimistic, suggesting browser extension integration and noting that humans still outperform automated detectors.

**Tags**: `#LLM detection`, `#classical machine learning`, `#AI-generated text`, `#community discussion`, `#NLP`

---

<a id="item-16"></a>
## [Spot Birds, Not Golf: Offsetting Data Center Water Use with Park Conversions](https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything) ⭐️ 7.0/10

Simon Willison humorously proposed that hyperscalers like Google could offset their data center water usage by purchasing golf courses, converting them into public parks, and promoting birdwatching as a new hobby for former golfers. He calculated that Google's 2025 water usage of 10.9 billion gallons could be offset by buying about 40 courses in Coachella Valley. This suggestion highlights the growing concern over the environmental impact of data centers, particularly water consumption for cooling, and creatively links it to the excessive water use of golf courses, offering a thought-provoking perspective on sustainability. Google used 10.9 billion gallons of water in 2025, about 30 million gallons per day, while each golf course in Coachella Valley consumes roughly 750,000 gallons daily, meaning 40 courses would match Google's usage. However, the proposal is satirical and does not account for practical challenges of such conversions.

rss · Simon Willison · Jul 17, 02:58

**Background**: Hyperscalers are large cloud computing companies like Google, Amazon, and Microsoft that operate massive data centers requiring significant energy and water for cooling. Water scarcity is a critical issue in many regions, and data center water consumption has come under scrutiny as AI workloads increase. Golf courses are also known for high water usage, particularly in arid areas.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyperscaler">Hyperscaler</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ai-energy-usage`, `#ai`, `#sustainability`, `#water-usage`, `#data-centers`

---

<a id="item-17"></a>
## [Quoting Thibault Sottiaux](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

A bug in the Codex AI coding agent can cause accidental file deletions when run with full access and without sandboxing.

rss · Simon Willison · Jul 16, 17:45

**Tags**: `#ai-safety`, `#coding-agents`, `#codex`, `#bug-report`, `#generative-ai`

---

<a id="item-18"></a>
## [Mermaid Diagrams Rendered as Unicode Box Art in the Browser](https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything) ⭐️ 7.0/10

Simon Willison created a browser-based tool that converts Mermaid diagram syntax into Unicode box art, leveraging Rust code from xAI's Grok project compiled to WebAssembly. This tool makes diagrams accessible in plain-text environments like terminals and markdown files, demonstrating the practicality of Rust/WASM for web-based rendering. The tool uses a self-contained terminal renderer originally written in Rust for the Grok CLI, compiled to WASM to run in the browser without a server.

rss · Simon Willison · Jul 16, 00:33

**Background**: Mermaid is a JavaScript-based diagramming language that generates charts from text descriptions. Unicode box-drawing characters are symbols used in text interfaces to draw lines and boxes. Rust is a systems programming language that can compile to WebAssembly, enabling high-performance code in web browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mermaid_(software)">Mermaid (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Box-drawing_characters">Box -drawing characters - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mermaid`, `#webassembly`, `#rust`, `#terminal`, `#diagrams`

---

<a id="item-19"></a>
## [QLoRA's Default Learning Rate (2e-4) Overfits on Small Datasets Under 10k Samples](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 7.0/10

A user discovered that the commonly recommended QLoRA learning rate of 2e-4 consistently causes overfitting on datasets smaller than 10k samples, and reducing it to 1e-4 significantly improves evaluation performance. Many practitioners fine-tune large language models on small custom datasets, and blindly using the default 2e-4 learning rate can waste weeks of effort on poor results; this simple adjustment saves time and improves model quality. The user found that for ~7k cleaned samples, 1e-4 with 5 epochs worked well, compared to 2e-4 with 3 epochs. A rule of thumb: above 30k samples 2e-4 is likely safe, below 10k start at 1e-4 or lower, and in between tune the learning rate.

reddit · r/MachineLearning · /u/Pretty-Ad774 · Jul 16, 12:50

**Background**: QLoRA (Quantized Low-Rank Adaptation) is a parameter-efficient method for fine-tuning large language models using 4-bit quantization and low-rank adapters, drastically reducing memory requirements. The learning rate of 2e-4 was popularized by early experiments on the 52k-sample Alpaca dataset, but it does not generalize well to much smaller datasets commonly used in practice.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/QLoRA">QLoRA</a></li>
<li><a href="https://arxiv.org/abs/2305.14314">[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs</a></li>

</ul>
</details>

**Tags**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#hyperparameter tuning`, `#small datasets`

---

<a id="item-20"></a>
## [Disentangling Convolutional Neurons with Hadamard Product Clustering](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 7.0/10

A new method applies Hadamard product clustering on the receptive field and weights of a 1x1 convolutional neuron in InceptionV1, revealing clear monosemantic clusters (cars, cats, dogs) and polysemantic lower-valued clusters. It also suggests gradient descent deliberately distributes patterns across neurons to suppress activations. This provides a finer-grained tool for mechanistic interpretability, helping to understand how individual neurons represent features, which could improve AI safety and transparency. Its current limitation is that it only applies to convolutional architectures. The technique computes the Hadamard product of the input receptive field and the neuron's weight to capture what the neuron 'sees,' then clusters these products. Lower-activation clusters showed correlated firing in connected neurons, suggesting deliberate noise injection by gradient descent.

reddit · r/MachineLearning · /u/narang_27 · Jul 15, 06:59

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by analyzing internal circuits. A key challenge is polysemanticity, where a single neuron fires for multiple unrelated concepts. The Hadamard product is an element-wise matrix multiplication; applying it between a neuron's weights and its input receptive field isolates the pattern being detected. Clustering these products can disentangle a neuron's activations into monosemantic features.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polysemanticity">Polysemanticity - Wikipedia</a></li>
<li><a href="https://transformer-circuits.pub/2023/monosemantic-features/index.html">Towards Monosemanticity: Decomposing Language Models With ...</a></li>

</ul>
</details>

**Tags**: `#mechanistic-interpretability`, `#convolutional-neural-networks`, `#feature-visualization`, `#clustering`, `#AI-safety`

---

<a id="item-21"></a>
## [PyTorch Model 170x Slower on T4 vs A100: Debugging Extreme Bottleneck](https://www.reddit.com/r/MachineLearning/comments/1ux6a9x/pytorch_model_running_170x_slower_on_t4_vs_a100/) ⭐️ 7.0/10

A user reported a 170x slowdown when running a point-tracking PyTorch model on an NVIDIA T4 GPU compared to an A100, ruling out simple misconfigurations and seeking profiling advice. This extreme bottleneck highlights how architectural limitations like memory bandwidth and lack of FP32 tensor core acceleration can cripple performance, providing a valuable case study for ML practitioners. The model uses 4D correlation volumes and transformer layers, both memory- and compute-intensive; the T4's 320 GB/s bandwidth versus the A100's 2 TB/s and the absence of FP32 tensor core acceleration likely contribute to the slowdown.

reddit · r/MachineLearning · /u/Future-Structure-296 · Jul 15, 13:44

**Background**: 4D correlation volumes (from the Extreme Rotation paper) compute dense feature similarities across all pairs of pixels in two images, creating a tensor of size H×W×H′×W′, which is extremely memory-intensive. The A100 offers 2.0 TB/s memory bandwidth and 312 TFLOPS of FP16 performance, while the T4 provides only 320 GB/s memory bandwidth and lacks hardware-accelerated FP32 matrix math, making it ill-suited for such workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://ruojincai.github.io/ExtremeRotation/">Extreme Rotation Estimation using Dense Correlation Volumes</a></li>
<li><a href="https://cloudgputracker.com/compare/nvidia-a100-vs-nvidia-t4/">NVIDIA A100 80GB vs NVIDIA T4 Comparison - cloudgputracker.com</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#GPU Performance`, `#Deep Learning`, `#Debugging`, `#NVIDIA T4 vs A100`

---

<a id="item-22"></a>
## [Researcher Seeks Collaborators to Scale and Evaluate New Recurrent Architecture DABSN](https://www.reddit.com/r/MachineLearning/comments/1uycffg/seeking_collaborators_for_scaling_and_independent/) ⭐️ 6.0/10

An independent researcher has released a preprint and open-source code for DABSN (Dynamic Adaptive Bias State Network), a novel recurrent neural network architecture, and trained a 24M-parameter language model on 1B tokens using GPT-2 tokenizer, showing promising results on long-sequence and reasoning benchmarks. This work could offer an alternative to Transformer-based models for efficient long-context language modeling, and the open call for collaboration may accelerate independent validation and scaling, benefiting the broader ML research community. The architecture is evaluated on synthetic reasoning and memory benchmarks like MQAR, Copy, Key-Value retrieval, and A5/60. The code includes PyTorch, C++, and Triton implementations, and the author is preparing a second paper focusing on language modeling and long-context behavior.

reddit · r/MachineLearning · /u/BleedingXiko · Jul 16, 19:17

**Background**: Recurrent neural networks (RNNs) process sequences step by step, maintaining a hidden state, which can be more memory-efficient than Transformers for long sequences. Recently, architectures like Mamba and RWKV have revived interest in recurrent models for language tasks. Benchmarks like MQAR (Multi-Query Associative Recall) test a model's ability to associate and recall information across long contexts, a key requirement for language understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2312.04927">[2312.04927] Zoology: Measuring and Improving Recall in ... GitHub - HazyResearch/zoology: Understand and test language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com Zoology (Blogpost 1): Measuring and Improving Recall in ... Published as a workshop paper at SCOPE - ICLR 2025 - OpenReview Understanding Input Selectivity in Mamba: Impact on ...</a></li>
<li><a href="https://github.com/HazyResearch/zoology">GitHub - HazyResearch/zoology: Understand and test language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com Zoology (Blogpost 1): Measuring and Improving Recall in ... Published as a workshop paper at SCOPE - ICLR 2025 - OpenReview Understanding Input Selectivity in Mamba: Impact on ...</a></li>

</ul>
</details>

**Tags**: `#Recurrent Neural Networks`, `#Language Models`, `#Architecture`, `#Long-Context`, `#Collaboration`

---

<a id="item-23"></a>
## [ECCV's High Registration Fees Spark Student Outcry](https://www.reddit.com/r/MachineLearning/comments/1uxyd6z/why_is_eccv_so_insanely_expensive_for_students/) ⭐️ 6.0/10

A Reddit user reports that ECCV requires paper presenters to pay the full registration fee of $805 instead of the student rate of $440, and their travel grant applications were rejected. This issue underscores the financial burden on student researchers, which may hinder their ability to present work and network, especially for those without institutional support. The ECCV student early bird registration is $440, but paper presenters are ineligible for this rate and must pay $805; travel grants and fee waivers are competitive and often denied.

reddit · r/MachineLearning · /u/NotGondor · Jul 16, 09:55

**Background**: ECCV is a premier biennial computer vision conference. Like many top conferences, it charges registration fees to cover costs, and presenting authors are typically required to register at the full rate. Travel grants are limited and awarded based on need and merit.

**Tags**: `#academia`, `#conference-fees`, `#machine-learning`, `#student-concerns`, `#ECCV`

---

<a id="item-24"></a>
## [AI Memory Systems Should Evolve from Fact-Storing to Inferring User Reasoning Patterns](https://www.reddit.com/r/MachineLearning/comments/1uy6yht/are_current_ai_memory_architectures_optimizing/) ⭐️ 6.0/10

A new conceptual essay proposes that AI memory architectures should move beyond storing descriptive facts about users and instead continuously refine persistent context to infer higher-level patterns such as recurring explanatory frameworks and characteristic reasoning styles. This shift could lead to AI systems that understand users more deeply, enabling more personalized and context-aware interactions, and aligning with cognitive science models of human memory. The essay lacks technical implementation details and empirical validation, but raises fundamental questions about whether current memory, retrieval, and summarization approaches are sufficient or if new architectures are needed.

reddit · r/MachineLearning · /u/Boris_Ljevar · Jul 16, 16:00

**Background**: Current AI memory systems often use techniques like conversation summaries, user preference storage, and retrieval-augmented generation to maintain context. Cognitive architectures in AI, such as ACT-R and SOAR, provide frameworks for simulating human-like reasoning and memory. The essay draws inspiration from these fields, suggesting that AI memory should evolve from simple fact retention to modeling user-specific cognitive patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory">IAAR-Shanghai/Awesome-AI-Memory - GitHub</a></li>
<li><a href="https://zylos.ai/research/2026-04-05-ai-agent-memory-architectures-persistent-knowledge/">AI Agent Memory Architectures: From Context Windows to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_architecture">Cognitive architecture</a></li>

</ul>
</details>

**Tags**: `#AI Memory`, `#Cognitive Architectures`, `#Personalization`, `#Contextual AI`, `#Abstraction`

---

<a id="item-25"></a>
## [ExTernD proposes expanded-rank ternary decomposition for near-lossless LLM quantization](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 6.0/10

ExTernD introduces a post-training quantization method that decomposes each LLM weight matrix into two ternary matrices and a diagonal scaling matrix, achieving near-lossless accuracy with only a slight increase in VRAM by tuning the inner rank. This method could enable extremely efficient LLM inference by exploiting multiplication-free ternary arithmetic while preserving model accuracy, potentially reducing hardware requirements and energy consumption. The approach avoids the dead end of fixed-size ternary quantization; the inner rank provides a tunable accuracy–VRAM tradeoff. The core greedy decomposition algorithm is open-source on GitHub.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Ternary quantization compresses weights to {-1,0,1}, enabling inference without multiplication. Post-training quantization (PTQ) reduces model size after training without retraining. Matrix decomposition techniques like rank factorization split a matrix into smaller components, allowing flexible low-rank approximation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13511">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ...</a></li>
<li><a href="https://github.com/LMTLS5/ternary-decomposition">GitHub - LMTLS5/ ternary - decomposition · GitHub</a></li>
<li><a href="https://docs.pytorch.org/TensorRT/tutorials/ptq.html">Post Training Quantization ( PTQ ) — Torch-TensorRT...</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#LLM Quantization`, `#Ternary Networks`, `#Model Compression`, `#Research Preprint`

---

<a id="item-26"></a>
## [Reddit user seeks critical perspectives on JEPA-based world models for robot learning](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 6.0/10

A Reddit user researching world models for robot learning is actively seeking devil's advocates to uncover potential downsides and red flags of Joint Embedding Predictive Architecture (JEPA)-based approaches, as the user finds the current narrative overwhelmingly positive. This reflects a growing need for balanced scrutiny in AI research, especially as influential figures like Yann LeCun advocate for JEPA over dominant paradigms like LLMs and reinforcement learning, which could shape future robotics and AI directions. The user has reviewed recent papers by LeCun and other groups, noting LeCun's dismissal of alternatives and his promotion of JEPA as the 'only next big thing', specifically asking for downsides compared to other world model approaches in robot learning.

reddit · r/MachineLearning · /u/Amazing-Coat5160 · Jul 15, 17:34

**Background**: JEPA (Joint Embedding Predictive Architecture) is a self-supervised learning method that predicts abstract latent representations rather than pixel-level reconstruction, aiming to build internal world models. World models in AI are predictive models that allow agents to simulate environments, essential for sample-efficient robot learning. Yann LeCun, a prominent AI researcher, has proposed JEPA as a path toward more human-like learning, contrasting with generative models like LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/">I-JEPA: The first AI model based on Yann LeCun’s vision for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Joint_Embedding_Predictive_Architecture">Joint Embedding Predictive Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#JEPA`, `#world models`, `#robot learning`, `#AI critique`, `#LeCun`

---