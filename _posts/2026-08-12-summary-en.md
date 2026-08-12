---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 39 items, 19 important content pieces were selected

---

1. [Attack Extracts Hidden Reasoning Traces from Proprietary LLM APIs](#item-1) ⭐️ 9.0/10
2. [Compression is Prediction: Unifying Two Sides of the Same Coin](#item-2) ⭐️ 8.0/10
3. [Nvidia Releases Nemotron 3.5 Lightning and NeMo Switchyard](#item-3) ⭐️ 8.0/10
4. [xAI Launches Grok Bot, an AI Agent with Browser and Account Access](#item-4) ⭐️ 8.0/10
5. [Go is an ideal language for AI-assisted software engineering](#item-5) ⭐️ 8.0/10
6. [No Lossless Transformations of Natural-Language Text](#item-6) ⭐️ 8.0/10
7. [Meta Releases Muse Glimmer: 30B Open-Weight Agentic Model](#item-7) ⭐️ 8.0/10
8. [Decoupled Descent: A Training Method Asymptotically Equalizes Train and Test Errors](#item-8) ⭐️ 8.0/10
9. [Context-Induced Activation Drift Passively Decouples RLHF Alignment in Gemma-3-1b-it](#item-9) ⭐️ 8.0/10
10. [fru: A Fast Rust-Based Random Forest with Python and R Bindings](#item-10) ⭐️ 8.0/10
11. [WorldClaw: Agentic 3D Open-World Generation at Scale](#item-11) ⭐️ 7.0/10
12. [Mojo 1.0 Released: High-Performance AI Language with Python Compatibility](#item-12) ⭐️ 7.0/10
13. [OpenAI Ethics Head Resigns After Less Than a Year](#item-13) ⭐️ 7.0/10
14. [Making holograms with a pen plotter](#item-14) ⭐️ 7.0/10
15. [HyperSAE: Poincaré Geometry Cuts Sparse Autoencoder MSE by 9.8%](#item-15) ⭐️ 7.0/10
16. [Manually Compiled Multiplication into Phi-3 Weights Achieves 100% Accuracy](#item-16) ⭐️ 7.0/10
17. [Synthetic Query Probing Compares Embedding Model Similarity Spaces](#item-17) ⭐️ 7.0/10
18. [England set to be one of the first countries to eliminate hepatitis C](#item-18) ⭐️ 6.0/10
19. [User Seeks to Report CVPR 2026 Paper for Undelivered Dataset](#item-19) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Attack Extracts Hidden Reasoning Traces from Proprietary LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.0/10

Researchers published a paper demonstrating a method to extract hidden chain-of-thought reasoning from proprietary LLMs like those from Anthropic, OpenAI, and Google by replaying encrypted reasoning traces into weaker sibling models and jailbreaking them. This exposes a vulnerability in how providers protect internal reasoning, potentially leaking sensitive model behaviors and enabling prompt injection using contaminated reasoning traces. It has implications for AI safety, transparency, and the security of commercial LLM deployments. The attack used the fact that models within the same family share encryption keys; they jailbroke Claude Haiku 4.5 with a prompt to transcribe the reasoning, and the flaw has since been fixed by all providers.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought reasoning is a technique where models generate step-by-step internal text to solve problems. Providers like OpenAI and Anthropic hide the actual reasoning from users, returning only encrypted blobs. This paper shows that these encrypted traces can be replayed into weaker, less secure models from the same provider, which can then be manipulated into revealing the original text.

<details><summary>References</summary>
<ul>
<li><a href="https://stolen-thoughts.com/">Stolen Thoughts</a></li>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://digg.com/tech/8a168m9s">Researchers Decode Encrypted Chain - of - Thought from Major AI...</a></li>

</ul>
</details>

**Discussion**: Some commenters questioned the 'stealing' framing, arguing that users pay for and should have access to the reasoning tokens. Others noted that similar extraction may be possible via tool-use, and some speculated that the flaw might have been intentionally allowed. There was interest in the portability of traces across models and the implications for training data contamination.

**Tags**: `#LLM Security`, `#Chain-of-Thought`, `#Model Jailbreaking`, `#AI Privacy`, `#Adversarial ML`

---

<a id="item-2"></a>
## [Compression is Prediction: Unifying Two Sides of the Same Coin](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

A new article on ngrok.com explores the deep equivalence between compression and prediction, highlighting how they are two sides of the same coin. Understanding that compression and prediction are fundamentally linked can lead to advances in artificial intelligence, as efficient compression algorithms may implicitly learn to predict patterns, a core aspect of intelligence. The principle stems from information theory: a good predictor can be turned into a compressor by encoding only prediction errors, and vice versa, though some argue compression may not always require prediction for sequential data.

hackernews · nikolay · Aug 11, 19:49 · [Discussion](https://news.ycombinator.com/item?id=49263497)

**Background**: Information theory quantifies information and the limits of compression. The Minimum Description Length (MDL) principle states that the best model for data is the one that compresses it most, linking compression to model selection. Kolmogorov complexity defines the ultimate compressed representation of data as the shortest program that outputs it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/hAvGi9YAPZAnnjZNY/prediction-compression-transcript-1">Prediction = Compression [Transcript] — LessWrong</a></li>
<li><a href="https://stats.stackexchange.com/questions/489688/is-prediction-the-same-as-compression">Is Prediction the same as Compression ? - Cross Validated</a></li>
<li><a href="https://en.wikipedia.org/wiki/Minimum_description_length">Minimum description length</a></li>

</ul>
</details>

**Discussion**: The community discussion highlighted the foundational nature of the idea, citing MacKay's Cambridge course and Grant Sanderson's video. Some argued that while prediction enables compression, compression does not always require sequential prediction, and noted that physical laws are ultimate forms of compression.

**Tags**: `#information theory`, `#machine learning`, `#compression`, `#prediction`, `#artificial intelligence`

---

<a id="item-3"></a>
## [Nvidia Releases Nemotron 3.5 Lightning and NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 8.0/10

Nvidia has introduced Nemotron 3.5 Lightning, a 30-billion-parameter open-source MoE model with 3 billion active parameters optimized for low-latency agentic AI tasks, along with NeMo Switchyard, an open-source Rust library for intelligently routing LLM requests to balance capability, cost, and latency. This release advances efficient AI deployment for agentic workflows, offering a fast lightweight model and flexible routing to optimize cost-performance tradeoffs, and supports the industry trend towards smaller, specialized models. Nemotron 3.5 Lightning uses a hybrid MoE architecture with Mamba-2 and attention layers, supports speculative decoding and FP4 quantization for up to 4x speed; Switchyard provides tuning-free routers as a Rust proxy. Community tests suggest potential limitations in complex coding tasks.

hackernews · droidjj · Aug 11, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49263340)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per input, enabling larger total parameter counts with lower compute. Agentic AI systems perform multi-step tasks autonomously, often requiring multiple model calls. Intelligent routing directs requests to the most suitable model, improving efficiency and quality.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/">NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster ...</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3.5 Lightning Delivers Fast ... - NVIDIA Developer</a></li>
<li><a href="https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/">Route AI Agents Across Models with NVIDIA NeMo Switchyard | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Discussion**: Community reaction was mixed: some users found Nemotron 3.5 Lightning fast but ineffective for coding tasks; others discussed routing challenges like prompt caching. There was criticism of benchmark selections, and a call for minimalist communication amid information overload.

**Tags**: `#AI`, `#machine learning`, `#model deployment`, `#open source`, `#Nvidia`

---

<a id="item-4"></a>
## [xAI Launches Grok Bot, an AI Agent with Browser and Account Access](https://x.ai/bot) ⭐️ 8.0/10

x.ai launched Grok Bot, an AI agent that can autonomously control a web browser and access user accounts to perform tasks, marking a shift from chat-based AI to agent-based automation. It can own its own routines and context, and communicate with other bots. This signals a paradigm shift in human-AI interaction, moving from prompts to autonomous agents that manage tasks, raising significant privacy and security concerns as users grant extensive access to their personal data and credentials. The bot can capture credentials directly from the browser, potentially running nonstop with full account access, which exposes users to risks like data leaks, prompt injection, or credential misuse.

hackernews · rvz · Aug 11, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49261514)

**Background**: AI agents are autonomous programs that use large language models to plan and execute tasks, often integrating with external tools. Browser automation allows them to simulate human interactions on web pages. xAI, founded by Elon Musk, develops Grok, a series of AI chatbots known for controversial outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Browser_automation">Browser automation</a></li>

</ul>
</details>

**Discussion**: Commenters see this as a natural evolution from prompts to agents but express strong anxiety over security and privacy, with concerns about credentials being taken, data leaks, and bots running constantly. Some question the legality of automated interactions and fear data profiling.

**Tags**: `#AI agents`, `#browser automation`, `#xAI`, `#security`, `#privacy`

---

<a id="item-5"></a>
## [Go is an ideal language for AI-assisted software engineering](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/) ⭐️ 8.0/10

Google published a blog post arguing that Go's simplicity and robust tooling make it particularly effective for AI-generated code, sparking a debate on language suitability for AI-assisted development. The argument highlights how language design can influence LLM effectiveness in software engineering, potentially impacting tech stack choices and the quality of AI-assisted coding workflows. Go's strong documentation like Effective Go and its compile-time checks are cited as advantages, but critics note that LLMs may generate flawed concurrent code and that Rust's stricter compiler could be even more suitable for AI-assisted development.

hackernews · 0xedb · Aug 11, 16:57 · [Discussion](https://news.ycombinator.com/item?id=49261133)

**Background**: Go is a statically typed, compiled language designed for simplicity and concurrency, while large language models (LLMs) are AI systems trained on vast text corpora to generate code and text. Their code generation quality depends on language characteristics and training data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: Netflix's Go guild lead confirms AI agents write better Go code at their company, while others argue Go is not enjoyable and AI can produce more bad Go code faster; some favor Rust's strict compiler for compile-time error catching.

**Tags**: `#Go`, `#AI-assisted development`, `#code generation`, `#programming languages`, `#LLMs`

---

<a id="item-6"></a>
## [No Lossless Transformations of Natural-Language Text](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/#atom-everything) ⭐️ 8.0/10

Sophie Alpert argues that AI rewrites of natural language always alter meaning, requiring writers to fully stand behind every word they publish. This emphasizes human accountability in AI-augmented writing, especially crucial in technical documentation where precision is vital. It counters the growing trend of over-reliance on AI-generated text. The policy stresses that writers must be able to explain every line; since AI lacks the writer's full mental model, lossless transformation is impossible.

rss · Simon Willison · Aug 11, 23:48

**Background**: AI tools like LLMs are often used to rephrase text. However, natural language is inherently ambiguous and context-dependent, so any edit risks altering meaning.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/">There are no lossless transformations of natural-language text</a></li>
<li><a href="https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text">There are no lossless transformations of natural-language text</a></li>

</ul>
</details>

**Tags**: `#AI writing`, `#natural language processing`, `#software engineering`, `#writing ethics`, `#LLM usage`

---

<a id="item-7"></a>
## [Meta Releases Muse Glimmer: 30B Open-Weight Agentic Model](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta has released Muse Glimmer, a 30 billion parameter open-weight model under the Apache 2.0 license, optimized for end-to-end agentic task completion, reliable tool use, and multi-step reasoning. This release marks a significant step in accessible agentic AI, providing a permissively licensed model that can run locally on consumer hardware, enabling developers to build autonomous agents that complete complex workflows. Muse Glimmer is a vision model that performs well on benchmarks like SWE-Bench and MCP-Atlas. It can be run on machines with 32GB of RAM using quantized versions, leaving room for other applications.

rss · Simon Willison · Aug 10, 23:56

**Background**: Agentic task completion refers to AI systems autonomously performing multi-step workflows, including reasoning, planning, and tool use. SWE-Bench evaluates models on generating patches for real-world software issues. MCP-Atlas tests tool-use competency with the Model Context Protocol across various tools and tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://www.swebench.com/SWE-bench/">Overview - SWE-bench</a></li>
<li><a href="https://arxiv.org/abs/2602.00933">[2602.00933] MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers</a></li>

</ul>
</details>

**Tags**: `#Muse Glimmer`, `#open-weight`, `#agentic AI`, `#Meta`, `#LLM`

---

<a id="item-8"></a>
## [Decoupled Descent: A Training Method Asymptotically Equalizes Train and Test Errors](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 8.0/10

The paper introduces Decoupled Descent (DD), a training method that leverages Approximate Message Passing (AMP) with Onsager corrections to provide a theoretical guarantee that the training error asymptotically matches the testing error at every parameter iterate, demonstrated on a two-layer network with an XOR model. This addresses the fundamental train-test error gap in neural network training by offering a certificate of equality, potentially enabling optimal stopping, reliable hyperparameter tuning, and improved generalization without a validation set. The method is derived for full-batch gradient descent on stylized Gaussian mixture models, using AMP's Onsager correction to decouple dynamics; 100 simulations on an XOR model with a two-layer network show the train-test error tracking, and a PyTorch package is planned.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: Approximate Message Passing (AMP) is an iterative algorithm from high-dimensional statistics commonly used in compressed sensing. It employs Onsager corrections, which subtract a weighted prior message to remove self-interference and ensure state evolution. In this work, AMP is adapted to correct for data reuse bias in gradient descent, thereby eliminating the train-test gap.

<details><summary>References</summary>
<ul>
<li><a href="https://krzakala.github.io/cargese.io/AMP_Tutorial_18.pdf">PDF Approximate Message Passing Tutorial - GitHub Pages</a></li>
<li><a href="https://www.emergentmind.com/topics/onsager-correction-in-goamp">Onsager Correction in GOAMP</a></li>
<li><a href="https://arxiv.org/html/2604.27883v1">Decoupled Descent : Exact Test Error Tracking Via Approximate...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#generalization`, `#training dynamics`, `#approximate message passing`, `#gradient descent`

---

<a id="item-9"></a>
## [Context-Induced Activation Drift Passively Decouples RLHF Alignment in Gemma-3-1b-it](https://www.reddit.com/r/MachineLearning/comments/1vm16hs/contextinduced_activation_drift_long_benign/) ⭐️ 8.0/10

Researchers discovered that feeding a long, benign, thematically coherent context (up to 3000 tokens) into google/gemma-3-1b-it causes a massive internal activation drift at deep layers, leading to a logit divergence and entropy surge that neutralizes RLHF refusal, without any adversarial prompts. This reveals a passive vulnerability in RLHF alignment: simply prepending long benign context can silently disable safety guardrails, undermining the assumed robustness of aligned models and posing a significant AI safety concern. The drift is strictly semantics-driven, confirmed by a shuffled-text ablation where destroying coherence eliminated the effect; the L2 norm shift reached ~3434 at layer 22 with a KL divergence of ~22.87 nats and a 325x entropy increase.

reddit · r/MachineLearning · /u/PresentSituation8736 · Aug 12, 02:09

**Background**: RLHF (Reinforcement Learning from Human Feedback) aligns language models to refuse harmful requests. Mechanistic interpretability aims to understand neural networks by analyzing internal circuits. RoPE is a positional encoding method; the study ruled out that the drift came from RoPE noise.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://towardsdatascience.com/rope-clearly-explained/">RoPE, Clearly Explained - Towards Data Science</a></li>

</ul>
</details>

**Tags**: `#RLHF`, `#alignment`, `#mechanistic interpretability`, `#activation drift`, `#AI safety`

---

<a id="item-10"></a>
## [fru: A Fast Rust-Based Random Forest with Python and R Bindings](https://www.reddit.com/r/MachineLearning/comments/1vkrvks/fru_fast_random_forest_implementation_p/) ⭐️ 8.0/10

A new Rust-based random forest library called fru has been released with bindings for Python and R, delivering major speed improvements over scikit-learn (up to hundreds of times faster) and ranger (up to several times faster). This library offers a drop-in performance upgrade for data scientists and ML engineers using Python or R, enabling much faster model training and inference without sacrificing accuracy. fru is written in Rust for high performance and safety, leverages the Arrow PyCapsule interface for seamless data exchange with pandas, polars, and other libraries, and includes a novel permutation importance implementation for efficient feature importance computation.

reddit · r/MachineLearning · /u/kpiwonski · Aug 10, 17:45

**Background**: Random forests are an ensemble learning method that combines multiple decision trees to improve prediction accuracy. scikit-learn is a widely used Python ML library, and ranger is a popular R package for fast random forests. Permutation importance is a technique to measure feature importance by shuffling feature values and observing the impact on model performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html">The Arrow PyCapsule Interface — Apache Arrow v25.0.0</a></li>
<li><a href="https://cran.r-project.org/web/packages/ranger/ranger.pdf">Package ‘ranger’ May 9, 2026 Type Package</a></li>
<li><a href="https://en.wikipedia.org/wiki/Permutation_importance">Permutation importance</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#random-forest`, `#rust`, `#performance`, `#python`

---

<a id="item-11"></a>
## [WorldClaw: Agentic 3D Open-World Generation at Scale](https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/) ⭐️ 7.0/10

WorldClaw, introduced by Tencent Hunyuan, is an agentic framework that orchestrates large language models and image models to generate explorable 3D open worlds from text prompts, extracting objects from composed 2D images for 3D placement. This approach lowers the barrier for creating large 3D worlds, potentially enabling indie developers to produce content previously requiring AAA resources. However, the generated quality currently falls short of handcrafted detail, making it more suitable for rapid prototyping or mass-market games where polish is secondary. WorldClaw uses planning agents to translate prompts into layout and object specifications, then employs an image model for scene composition and SAM3D for object extraction. The system outputs explicit 3D assets but suffers from inconsistent object placement and lacks seasonal coherence, as noted by early reviewers.

hackernews · EwanG · Aug 11, 21:56 · [Discussion](https://news.ycombinator.com/item?id=49265051)

**Background**: Agentic AI refers to programs that can autonomously use tools to achieve goals, contrasting with narrow chatbots. Procedural content generation (PCG) in games automatically creates environments using algorithms; WorldClaw combines PCG with AI agents by having LLMs plan and image models compose scenes, then extracting 3D objects with models like SAM3D.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.05248">WorldClaw: Agentic 3D Open-World Generation at Scale</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: some praise the novel integration of image composition and 3D extraction, but many criticize the lack of handcrafted detail, odd object placement (e.g., buildings in water), and the quality looking like a 'scatter brush' rather than intentional design. There is also concern that AI-generated worlds may obscure the human authorship that players value, though the technique could empower indie creators.

**Tags**: `#3D world generation`, `#procedural content generation`, `#AI agents`, `#computer graphics`, `#game development`

---

<a id="item-12"></a>
## [Mojo 1.0 Released: High-Performance AI Language with Python Compatibility](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 7.0/10

Mojo 1.0 has been officially released by Modular, marking the first stable version of the language. It targets high-performance AI development with Python-like syntax and a new website at mojolang.org. This milestone aims to provide a viable alternative for AI infrastructure, but its closed-source compiler and reduced commitment to being a Python superset have sparked mixed reactions in the developer community. Mojo uses MLIR for compilation, enabling optimizations for CPUs, GPUs, and other accelerators. The compiler is not yet open-source, with a planned open-source release in 2026, and the roadmap now states it may not become a full Python superset.

hackernews · dayanruben · Aug 11, 16:56 · [Discussion](https://news.ycombinator.com/item?id=49261128)

**Background**: Mojo is a systems programming language developed by Modular Inc., designed to simplify AI development by combining Python's ease of use with high-performance systems programming features like static typing and a borrow checker. It leverages the MLIR compiler framework instead of LLVM, allowing advanced optimizations for heterogeneous hardware. Initially marketed as a Python superset, this goal has been de-emphasized.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**Discussion**: The community has expressed mixed feelings: some find the language's purpose unclear, others criticize the closed-source compiler, and many are concerned about the shift away from Python superset compatibility. However, some remain hopeful about its performance potential.

**Tags**: `#mojo`, `#programming-languages`, `#python`, `#ai`, `#compiler`

---

<a id="item-13"></a>
## [OpenAI Ethics Head Resigns After Less Than a Year](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) ⭐️ 7.0/10

OpenAI's head of ethics, Chloe Bakalar, resigned after less than a year in the role, having joined in 2024 following a six-year tenure as chief ethicist at Meta. This departure fuels concerns about the tech industry's commitment to AI ethics and safety, especially as companies like OpenAI race to deploy powerful AI systems. While the precise reasons remain undisclosed, the departure came soon after a high-profile hacking incident involving HuggingFace, raising questions about internal alignment priorities.

hackernews · ilamont · Aug 11, 12:23 · [Discussion](https://news.ycombinator.com/item?id=49257160)

**Background**: OpenAI is a leading artificial intelligence research lab responsible for ChatGPT. Ethics teams in AI companies are tasked with guiding responsible development, but often face challenges in influencing business decisions.

**Discussion**: Commenters express skepticism about the influence of ethics teams, viewing them as often powerless against business priorities. Some speculate the departure may reflect deeper internal issues or a lack of seriousness about AI safety.

**Tags**: `#AI ethics`, `#OpenAI`, `#corporate ethics`, `#AI safety`, `#tech industry`

---

<a id="item-14"></a>
## [Making holograms with a pen plotter](https://blog.jordan.matelsky.com/Penplotter-holography/) ⭐️ 7.0/10

Jordan Matelsky's blog demonstrates using a pen plotter to scratch holographic patterns onto surfaces, cleverly illustrating the technique with olive oil and fingerprint smudges on a phone screen. This inventive DIY method makes holography accessible with everyday tools, encouraging experimentation at the intersection of optics, programming, and hardware hacking. The plotter's mechanical precision limits scratch density, and the resulting holograms are simpler than laser-based ones; using a sharper tool or a piezoelectric actuator could improve quality.

hackernews · DemiGuru · Aug 11, 18:51 · [Discussion](https://news.ycombinator.com/item?id=49262811)

**Background**: Scratch holography (abrasion holography) creates 3D images by hand-drawing arcs that act as tiny mirrors, each reflecting light to a specific viewing angle. A pen plotter is a computer-controlled drawing machine that moves a pen along precise vector paths, historically used for technical drawings. By replacing the pen with a scribing tool, the plotter can automatically generate the needed scratch patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pen_plotter">Pen plotter</a></li>
<li><a href="http://amasci.com/amateur/holohint.html">Scratch-Hologram FAQ</a></li>

</ul>
</details>

**Discussion**: Commenters enjoyed the old-Internet DIY spirit, referencing classic abrasion holography by William Beaty and suggesting enhancements like using a needle or a piezoelectric disk scanner for finer lines, with one jokingly proposing chocolate as a hologram medium.

**Tags**: `#holography`, `#pen-plotter`, `#diy`, `#optics`, `#maker`

---

<a id="item-15"></a>
## [HyperSAE: Poincaré Geometry Cuts Sparse Autoencoder MSE by 9.8%](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/) ⭐️ 7.0/10

HyperSAE, a new PyTorch library, introduces Poincaré hyperbolic geometry into sparse autoencoder training, achieving a 9.8% reduction in reconstruction MSE and reducing dead latents to just 0.2% on Gemma-2-2B. By better aligning with the hierarchical structure of language model concepts, this approach significantly reduces feature collisions and dead latents, potentially advancing mechanistic interpretability research and improving the reliability of sparse feature decompositions. The architecture uses a decoupled design: the forward pass remains Euclidean with zero inference overhead, while dictionary weights are projected into the Poincaré ball during training. The entailment cone loss organizes general concepts near the origin and specific concepts near the boundary, and a TriPartite loss combines reconstruction, L1 sparsity, and entailment.

reddit · r/MachineLearning · /u/visha1v · Aug 11, 18:37 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincaré_geometry_for_sparse/)

**Background**: Sparse autoencoders (SAEs) are used in mechanistic interpretability to decompose neural network activations into sparse feature vectors, but they often suffer from dead latents—features that never activate. Hyperbolic geometry, such as the Poincaré ball model, exhibits exponential volume growth, making it suitable for embedding hierarchical data like the concept structures in language models. The entailment cone loss was previously proposed for learning hierarchical embeddings in hyperbolic space, enforcing a tree-like partial order.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Poincaré_disk_model">Poincaré disk model - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/324246200_Hyperbolic_Entailment_Cones_for_Learning_Hierarchical_Embeddings">Hyperbolic Entailment Cones for Learning Hierarchical Embeddings | Request PDF</a></li>

</ul>
</details>

**Tags**: `#mechanistic-interpretability`, `#sparse-autoencoders`, `#hyperbolic-geometry`, `#library`, `#pytorch`

---

<a id="item-16"></a>
## [Manually Compiled Multiplication into Phi-3 Weights Achieves 100% Accuracy](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 7.0/10

A Reddit user manually programmed the weights of a Phi-3 transformer using a custom compiler, Torchwright, to perform multi-digit multiplication with 100% accuracy, without any training. This demonstrates that transformers have the architectural capacity for exact arithmetic when appropriately programmed, challenging the assumption that they inherently struggle with arithmetic and highlighting the potential for interpretability and manual weight setting. The compiler supports multiple algorithm implementations including grade-school, hardware-style, scratchpad, and memorization; the 12-digit version is available on Hugging Face. However, the approach requires manual compilation of a specific algorithm and does not generalize to other tasks.

reddit · r/MachineLearning · /u/notforrob · Aug 10, 17:37

**Background**: Phi-3 is a small language model from Microsoft, part of the Phi family of compact yet capable transformers. Torchwright is a novel compiler that treats a transformer as a programmable substrate, converting computation graphs directly into model weights without any training. This project leverages Torchwright to inject arithmetic algorithms into a standard Phi-3 checkpoint.

<details><summary>References</summary>
<ul>
<li><a href="https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/">Introducing Phi - 3 : Redefining what's possible with SLMs | Microsoft...</a></li>
<li><a href="https://ood.dev/posts/torchwright-intro/">Introducing torchwright — Out of Distribution</a></li>
<li><a href="https://pypi.org/project/torchwright/">torchwright · PyPI</a></li>

</ul>
</details>

**Tags**: `#arithmetic`, `#transformer`, `#compilation`, `#interpretability`, `#manual-weight-setting`

---

<a id="item-17"></a>
## [Synthetic Query Probing Compares Embedding Model Similarity Spaces](https://www.reddit.com/r/MachineLearning/comments/1vkh1ul/comparing_embedding_models_with_synthetic_query/) ⭐️ 7.0/10

A new method, synthetic query probing, uses artificially generated queries to compare similarity score distributions across different embedding models, revealing how their similarity spaces relate linearly or non-linearly. This approach enables more informed model selection and threshold calibration for retrieval tasks, directly addressing a common practical challenge when swapping or evaluating embedding models. The technique is reference-free and scalable; accepted at Discovery Science 2026, the paper shows that Titan models of different dimensionalities have semilinearly related similarity scores, while Titan-to-Ada mappings are nonlinear.

reddit · r/MachineLearning · /u/pppeer · Aug 10, 10:27

**Background**: Embedding models convert text to numerical vectors, and similarity scores (e.g., cosine similarity) measure how relevant two pieces of text are. Different models produce different vector spaces, making direct comparison of scores impossible. Synthetic query probing generates artificial question-chunk pairs to create a shared reference, aligning similarity scores without needing a common model.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05857">Mapping Similarity Spaces across Embedding Models with Synthetic ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#embeddings`, `#similarity metrics`, `#model comparison`, `#information retrieval`

---

<a id="item-18"></a>
## [England set to be one of the first countries to eliminate hepatitis C](https://www.bbc.com/news/articles/c75gk620r22o) ⭐️ 6.0/10

England is on track to become one of the first countries to eliminate hepatitis C, thanks to widespread screening and effective treatment programs. This milestone demonstrates the effectiveness of coordinated public health efforts and could serve as a model for other nations, significantly reducing liver-related illnesses and deaths. The elimination campaign likely involves targeted screening of at-risk groups, such as those with a history of injecting drug use, and the use of highly effective direct-acting antiviral medications that can cure the infection in most cases.

hackernews · stevekemp · Aug 11, 12:41 · [Discussion](https://news.ycombinator.com/item?id=49257377)

**Background**: Hepatitis C is a blood-borne virus that can cause chronic liver disease, cirrhosis, and liver cancer. In recent years, new direct-acting antiviral drugs have achieved cure rates over 95%. The World Health Organization has set targets for eliminating viral hepatitis as a public health threat by 2030.

**Discussion**: Commenters expressed support for the screening program, with one sharing a personal story of early diagnosis and treatment. Some noted the difference in public health approaches between the UK and US, while others questioned why the program is limited to England rather than the entire UK. One comment linked to cancer statistics, speculating on a decline in liver cancer.

**Tags**: `#health`, `#hepatitis-c`, `#public-health`, `#england`, `#medical-advancement`

---

<a id="item-19"></a>
## [User Seeks to Report CVPR 2026 Paper for Undelivered Dataset](https://www.reddit.com/r/MachineLearning/comments/1vkn5x9/how_to_file_a_complaint_about_a_published_cvpr/) ⭐️ 6.0/10

A Reddit user is asking how to file a complaint about a CVPR 2026 paper whose promised dataset was never released, with the linked GitHub repository remaining empty. This highlights ongoing concerns about reproducibility in academic publishing, especially when dataset papers fail to deliver, undermining research integrity and community trust. The paper's main contribution is the dataset, and its GitHub link in the paper points to an empty repository; the user contacted the authors without success, and believes the conference required dataset availability.

reddit · r/MachineLearning · /u/ElPelana · Aug 10, 14:56

**Background**: CVPR (Conference on Computer Vision and Pattern Recognition) is a premier academic conference with guidelines emphasizing reproducibility, including a reproducibility checklist for authors. While code submission is voluntary, papers whose core contribution is a dataset are typically expected to make it public. For instance, a CVPR 2025 dataset paper released its data after acceptance.

<details><summary>References</summary>
<ul>
<li><a href="https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines">CVPR 2026 Reviewer Guidelines</a></li>
<li><a href="https://voxel51.com/blog/cvpr-2024-datasets-and-benchmarks-part-1-datasets">CVPR 2024 Datasets and Benchmarks - Part 1: Datasets - Voxel51</a></li>
<li><a href="https://github.com/kumuji/stu_dataset">GitHub - kumuji/stu_ dataset : [ CVPR 2025] Spotting the Unexpected...</a></li>

</ul>
</details>

**Tags**: `#dataset`, `#reproducibility`, `#conference_policies`, `#academic_publishing`, `#ethics`

---