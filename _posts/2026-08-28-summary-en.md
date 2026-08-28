---
layout: default
title: "Horizon Summary: 2026-08-28 (EN)"
date: 2026-08-28
lang: en
---

> From 28 items, 20 important content pieces were selected

---

1. [Saving 100 Terabytes of Memory by Optimizing 1.1.1.1's DNS Cache](#item-1) ⭐️ 8.0/10
2. [Small Language Models Reach Practical Capability for Cost-Effective Apps](#item-2) ⭐️ 8.0/10
3. [Interactive Website Animates 507 Mechanical Movements from 1868 Book](#item-3) ⭐️ 8.0/10
4. [Google Launches Gemini 3.5 Transcribe Speech-to-Text Model](#item-4) ⭐️ 8.0/10
5. [Google Launches Gemini Omni 1.1 Flash with Generative Video Controls](#item-5) ⭐️ 8.0/10
6. [Terminal-Bench-Science: Benchmark for AI Agents on Scientific Research Workflows](#item-6) ⭐️ 8.0/10
7. [Prompt Injection Bypasses Claude Code Opus 5 Auto Mode 80% of the Time](#item-7) ⭐️ 8.0/10
8. [Qwen Releases Qwen3.8-Flash-Next: 125B-Parameter Open-Weight Multimodal MoE Model](#item-8) ⭐️ 8.0/10
9. [HarnessOpt-Bench: Measuring Recursive Self-Improvement Without Cheating](#item-9) ⭐️ 8.0/10
10. [ImageBench: New Public Benchmark Evaluates 52 Text-to-Image Models with VLM Judge](#item-10) ⭐️ 8.0/10
11. [Fast Polyhedron Volume Computation Using the Divergence Theorem](#item-11) ⭐️ 7.0/10
12. [Sovereign Tech Agency Invests €500,000 in Flatpak Development](#item-12) ⭐️ 7.0/10
13. [OpenTIE and OpenXWA: Modern Open-Source Ports of Classic Star Wars Sims](#item-13) ⭐️ 7.0/10
14. [Doctors Begin to Manage Antidepressant Withdrawal](#item-14) ⭐️ 7.0/10
15. [Show HN: The Load-Bearing Vocabulary of Claude](#item-15) ⭐️ 7.0/10
16. [Recovered 575k crop labels show ten manual clicks per book beat ML scaling](#item-16) ⭐️ 7.0/10
17. [Microduck: Small Bipedal Robot with Onboard AI Training and ONNX Export](#item-17) ⭐️ 6.0/10
18. [Researcher Seeks Venue for Statistical/Probabilistic ML as LLMs Dominate Top Conferences](#item-18) ⭐️ 6.0/10
19. [NeurIPS 2026 Acceptance Calculator Estimates Paper Chances from Review Scores](#item-19) ⭐️ 6.0/10
20. [py-evoFE v0.3.0 Automates Feature Engineering with Genetic Algorithms](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Saving 100 Terabytes of Memory by Optimizing 1.1.1.1's DNS Cache](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare published details of five Rust-level memory optimizations to the DNS cache layout of its "Big Pineapple" system behind 1.1.1.1, reducing per-entry memory usage by 56% and freeing roughly 100 TB across its fleet. 1.1.1.1 is one of the most widely used public DNS resolvers; halving cache memory improves cache capacity, reduces operating costs, and can enhance query performance without adding hardware. The work targets "Big Pineapple," a recursive resolver component written in Rust; the optimizations include reducing per-entry overhead and leveraging DNS name compression defined in RFC 1035. Commenters added that further savings could come from inlining record data with CacheEntry, reordering struct fields, and using single large allocations, though some caution that merging lists may weaken Rust's out-of-bounds safety guarantees.

hackernews · TangerineDream · Aug 27, 17:17 · [Discussion](https://news.ycombinator.com/item?id=49468083)

**Background**: 1.1.1.1 is Cloudflare's free public DNS resolver, designed for speed and privacy. DNS resolvers commonly cache query results locally to reduce latency and load on upstream servers; cache entries consume memory, so data structure layout becomes critical at large scale. Cloudflare runs 1.1.1.1 on servers in hundreds of cities worldwide, meaning small per-entry savings multiply across the entire fleet.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS ...</a></li>
<li><a href="https://developers.cloudflare.com/1.1.1.1/">1 . 1 . 1 . 1 ( DNS Resolver ) · Cloudflare 1 . 1 . 1 . 1 docs</a></li>

</ul>
</details>

**Discussion**: Comments are largely positive about the optimization, but several systems programming experts propose additional savings, such as inlining record data with CacheEntry, using a single large malloc for many entries, and reordering struct fields to reduce padding. Some also caution that joining separate lists may reduce Rust's memory-safety guarantees, while others argue these optimizations are standard but still valuable at scale.

**Tags**: `#memory optimization`, `#DNS`, `#systems programming`, `#Rust`, `#Cloudflare`

---

<a id="item-2"></a>
## [Small Language Models Reach Practical Capability for Cost-Effective Apps](https://calv.info/small-models-have-arrived) ⭐️ 8.0/10

The essay contends that small language models have reached sufficient capability for many real-world tasks, allowing developers to build fast, low-cost applications. It cites early 2024 experiments with a 7B local model and the Guidance library for automated test generation and code completion. This signals a potential shift away from massive frontier models for many tasks, enabling cheaper and faster AI applications that could spawn new consumer products. It counters the assumption that only large models are useful, opening room for 'good-enough' models in specialized workflows. One commenter describes using a 7B parameter local model with the Guidance library (originally from Microsoft) to first generate tests from pseudocode and then write code until tests pass, a workflow developed before 'thinking' models. Another notes that large parameter counts often store world knowledge and language skills that may be unnecessary or even harmful for some applications.

hackernews · tosh · Aug 27, 15:56 · [Discussion](https://news.ycombinator.com/item?id=49466917)

**Background**: Small language models are neural networks with fewer parameters (e.g., 7 billion) than frontier models like GPT-4, making them cheaper and faster to run locally. The Guidance library is a tool for controlling language model outputs, enabling structured generation. The discussion refers to 'room at the bottom' strategies, meaning opportunities in smaller-scale models.

**Discussion**: Comments reflect general agreement that small models are becoming viable, with practical examples like test-to-code automation using a 7B model and Guidance. Some discuss strategic implications: investors wonder why more consumer AI companies haven't emerged, while others categorize work into 'IQ 180' vs 'token spewer' tasks, suggesting small models may handle the latter. A recurring theme is that large models carry extraneous world knowledge that can be wasteful or even detrimental for focused applications.

**Tags**: `#small language models`, `#LLMs`, `#AI`, `#machine learning`, `#hackernews`

---

<a id="item-3"></a>
## [Interactive Website Animates 507 Mechanical Movements from 1868 Book](https://507movements.com/) ⭐️ 8.0/10

The website 507movements.com presents interactive animations for all 507 mechanisms from Henry T. Brown's 1868 reference book "Five Hundred and Seven Mechanical Movements", turning static line drawings into visual demonstrations. This makes a classic mechanical engineering reference accessible and engaging for modern learners, designers, and hobbyists, helping preserve and disseminate pre-digital mechanism knowledge in an interactive format. The site is based on the 1868 book available on archive.org. Commentators note that individual animations lack titles or names, and some animations remain incomplete.

hackernews · helloplanets · Aug 27, 14:08 · [Discussion](https://news.ycombinator.com/item?id=49465169)

**Background**: "Five Hundred and Seven Mechanical Movements" was first published in 1868 by Henry T. Brown and is a classic reference cataloging mechanisms such as linkages, gears, and escapements with line drawings and brief descriptions. It has long been used by engineers, machinists, and inventors. The website converts these static illustrations into animations, making each mechanism's operation easier to understand.

<details><summary>References</summary>
<ul>
<li><a href="https://507movements.com/">507 Mechanical Movements</a></li>
<li><a href="https://grokipedia.com/page/507_mechanical_movements_mechanisms_and_devices_(book)">507 Mechanical Movements: Mechanisms and Devices (book)</a></li>

</ul>
</details>

**Discussion**: Overall, commenters appreciate the site and find it fun and educational. They suggest improvements such as adding titles or names to individual movements, note that some animations are incomplete, and share related resources including an interactive Euclid's Elements site, Redtenbacher/Reuleaux mechanism collections, and supplemental mechanical design books.

**Tags**: `#mechanical engineering`, `#historical reference`, `#animations`, `#educational resource`, `#mechanisms`

---

<a id="item-4"></a>
## [Google Launches Gemini 3.5 Transcribe Speech-to-Text Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

Google has released Gemini 3.5 Transcribe, a new speech-to-text model built on Gemini's audio understanding, offering low-latency, accurate transcription with speaker diarization, word-level timestamps, and smart transcription features. This launch intensifies competition in the speech-to-text market, potentially benefiting developers who need accurate multilingual transcription for meetings, real-time translation, and agent workflows, while signaling Google's push to integrate STT with broader Gemini agent capabilities. The model supports utterance-based language detection, speaker diarization, word-level timestamps, and smart transcription that can clean up disfluencies. However, users have reported that smart transcription may oversimplify precise wording, and function calling is currently available only in the Gemini macOS app for delegating tasks to other Gemini models.

hackernews · k9294 · Aug 27, 18:03 · [Discussion](https://news.ycombinator.com/item?id=49468818)

**Background**: Speech-to-text (STT) models convert spoken language into written text. Gemini 3.5 Transcribe builds on Google's Gemini multimodal models, which can process audio directly. 'Smart transcription' refers to automatically cleaning up disfluencies like 'um' and false starts, while 'function calling' usually lets a model invoke external tools or APIs; in this context, it allows the transcription model to hand off complex tasks to other Gemini models in the macOS app.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe">Gemini 3 . 5 Transcribe | Gemini API | Google AI for Developers</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Introducing Gemini 3 . 5 Transcribe</a></li>
<li><a href="https://medium.com/@kr.amit.sri/exploring-function-calling-in-llms-enhancing-ai-interactions-with-external-tools-42064a3a8080">Exploring Function Calling in LLMs: Enhancing AI ... | Medium</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some users say Gemini 3.5 Transcribe beats other models on accuracy but still needs lower latency, while others report that smart transcription oversimplifies precise wording and drops meaningful phrases. Commenters also expressed confusion about the advertised function-calling capability, which was clarified as being limited to the macOS app for delegating tasks, not arbitrary tool use by the STT model itself. Several users compared it unfavorably to alternatives like Soniox, Voxtral Mini, and ElevenLabs for specific use cases.

**Tags**: `#speech recognition`, `#Google`, `#AI`, `#machine learning`, `#transcription`

---

<a id="item-5"></a>
## [Google Launches Gemini Omni 1.1 Flash with Generative Video Controls](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) ⭐️ 8.0/10

Google has announced Gemini Omni 1.1 Flash, an incremental update to the Flash model that adds creative controls and generative video capabilities, including 40-second scene extensions, first/last-frame control, 360p rapid drafts, and 4K upscaling. This update signals Google's continuing push into generative video and multimodal AI, giving developers and creative professionals more affordable and controllable tools for AI video production. The model is described as supporting 10-second deep context, 40-second scene extensions, 360p rapid drafts priced at $0.03 per second, and 4K upscaling. It is an incremental 1.1 release to the Flash line, emphasizing creative controls and video generation rather than a new architecture.

hackernews · saretup · Aug 27, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49467922)

**Background**: Gemini is Google's family of multimodal AI models, which can process text, images, audio, and video together. The Flash line is optimized for speed and cost efficiency, while the Pro line targets higher performance. Multimodal learning, the underlying approach, has grown from deep learning research to become central to modern AI assistants and creative tools.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/">Build with Gemini Omni 1.1 Flash - The Keyword</a></li>
<li><a href="https://explainx.ai/blog/gemini-omni-1-1-flash-video-generation-update-august-2026">Gemini Omni 1.1 Flash: 40s Extensions, $0.03/s Drafts (Aug ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>

</ul>
</details>

**Discussion**: Commenters praised the model's accuracy, with one noting details held up under scrutiny, while others raised concerns about AI's impact on voice actors. Some joked about prompt engineering, suggested Google should launch a new Gemini Pro, and contrasted Google's continued video generation investment with OpenAI's reported retreat from Sora.

**Tags**: `#AI`, `#Google`, `#Gemini`, `#multimodal`, `#video-generation`

---

<a id="item-6"></a>
## [Terminal-Bench-Science: Benchmark for AI Agents on Scientific Research Workflows](https://www.terminal-bench-science.ai/announcement) ⭐️ 8.0/10

Terminal-Bench-Science (TB-Science) has been launched as a benchmark to evaluate AI agents on complex real-world scientific research workflows in terminal environments; it comes from the creators of Terminal-Bench and Harbor and is hosted by Stanford University and the Laude Institute. It extends AI agent evaluation beyond coding into scientific research workflows, helping the community assess which models can reliably handle domain-specific, multi-step computational tasks, with implications for scientific automation and model selection. The benchmark uses real computational workflows from scientific research and is publicly available on GitHub; community comments note that it may not fully verify result correctness, with Claude praised for scientific nuance but criticized for instruction following and simplification.

hackernews · matt_d · Aug 28, 00:06 · [Discussion](https://news.ycombinator.com/item?id=49472820)

**Background**: Terminal-Bench is an existing benchmark for evaluating AI agents in terminal environments, and Harbor is the associated framework. Terminal-Bench-Science adapts this approach to scientific research workflows, focusing on tasks that require domain knowledge and multi-step computation rather than general coding.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/harbor-framework/terminal-bench-science/">GitHub - harbor-framework/terminal-bench-science: Terminal ...</a></li>
<li><a href="https://www.tbench.ai/news/tb-science-announcement">Terminal-Bench-Science: Contribute your scientific workflows ...</a></li>
<li><a href="https://www.terminal-bench-science.ai/">TERMINAL-BENCH-SCIENCE</a></li>

</ul>
</details>

**Discussion**: Overall, commenters value the task quality but debate model rankings and raise concerns about whether correctness is checked. Some find Claude strong in scientific reasoning but weak at following instructions, while others share context engineering techniques and express surprise that Opus 5 outperforms Fable.

**Tags**: `#AI`, `#benchmark`, `#scientific-research`, `#LLM`, `#agent-evaluation`

---

<a id="item-7"></a>
## [Prompt Injection Bypasses Claude Code Opus 5 Auto Mode 80% of the Time](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

Johann Rehberger demonstrated a prompt injection attack that bypasses Claude Code Opus 5's auto mode protection in about 80% of cases, tricking the agent into downloading a zip archive and executing malicious code via a local Python module import. In some runs, once the compromise was detected, auto mode blocked the agent's own cleanup command. This directly challenges Anthropic's recent claims about auto mode's effectiveness and shows that the safety classifier can become part of the failure by blocking protective actions. It reinforces that unattended coding agents must be sandboxed and monitored when exposed to untrusted content. The attack succeeded about 80% of the time by placing a malicious struct.py in the working directory; when the agent imported base64, Python's import order loaded the local module and executed the payload. Auto mode routes tool calls through a Sonnet-5 classifier that blocks irreversible or destructive actions, but in some runs it blocked the agent's own cleanup command.

rss · Simon Willison · Aug 27, 22:50

**Background**: Prompt injection is an attack where malicious instructions embedded in content can cause an LLM to perform unintended actions; auto mode is Claude Code's feature that uses a classifier to skip routine permission prompts while blocking risky tool calls. Python resolves imports by searching the current directory first, so a file named like a standard library module (such as struct.py) can be loaded instead of the intended module. Anthropic had claimed that Opus 5 with auto mode drove browser-based prompt injection success to zero in some tests.

<details><summary>References</summary>
<ul>
<li><a href="https://itmeetsot.eu/posts/2026-08-12-opus5_automode/">Prompt Injection Experiments with Opus - 5 in Claude Code ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://medium.com/analytics-vidhya/python-library-hijacking-on-linux-with-examples-a31e6a9860c8">Python Library Hijacking on Linux (with examples) | Medium</a></li>

</ul>
</details>

**Tags**: `#prompt injection`, `#AI security`, `#Claude Code`, `#vulnerability`, `#auto mode`

---

<a id="item-8"></a>
## [Qwen Releases Qwen3.8-Flash-Next: 125B-Parameter Open-Weight Multimodal MoE Model](https://simonwillison.net/2026/Aug/26/qwen38-flash-next/) ⭐️ 8.0/10

Qwen has released Qwen3.8-Flash-Next, a new open-weights multimodal Mixture-of-Experts model with 125 billion total parameters but only 6 billion active during inference, intended as an early preview of the Qwen4 architecture. The model is already available in quantized GGUF formats from Unsloth and was tested by Simon Willison on an NVIDIA DGX Spark, generating SVG images such as a pelican riding a bicycle. This release offers developers and researchers early access to the architecture expected in Qwen4, enabling experimentation with a large multimodal model at relatively low computational cost due to only 6B active parameters. It continues the trend of open-weights MoE models becoming more accessible for local inference on hardware like NVIDIA DGX Spark. The model uses a Mixture-of-Experts design with 125B total parameters and 6B active parameters, and Unsloth provides quantized GGUF variants such as UD-IQ1_S (72.5GB) and UD-Q2_K_XL (78.9GB) for local deployment. Simon Willison tested these on an NVIDIA DGX Spark, with the UD-Q2_K_XL version generating high-quality SVG illustrations under the 'xhigh' reasoning effort setting.

rss · Simon Willison · Aug 26, 23:52

**Background**: Mixture-of-Experts (MoE) models contain multiple specialized 'expert' sub-networks, and a routing mechanism activates only a subset of experts for each input, so inference uses far fewer parameters than the model's total size. GGUF is a file format for quantized models that can run efficiently in llama.cpp and similar local runtimes; Unsloth's Dynamic quantizations use selective higher precision for important layers. NVIDIA DGX Spark is a compact personal AI supercomputer powered by NVIDIA Blackwell, designed for developers to create, test, and validate AI models locally.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.oflight.co.jp/en/columns/unsloth-dynamic-3-gguf-quantization-2026">Unsloth Dynamic 3.0 GGUFs: What Changed vs 2.0 (2026) | Oflight Inc.</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#open weights`, `#multimodal`, `#MoE`

---

<a id="item-9"></a>
## [HarnessOpt-Bench: Measuring Recursive Self-Improvement Without Cheating](https://www.reddit.com/r/MachineLearning/comments/1w052xg/can_ai_improve_itself_rsi_might_be_the_answer_r/) ⭐️ 8.0/10

Researchers introduced HarnessOpt-Bench, a benchmark for evaluating how well LLMs can optimize another agent's harness, using sandbox isolation and held-out evaluation to prevent the optimizer from accessing test solutions. Across 5 frontier models, 4 downstream tasks, and 111 runs, they found model choice affects gains 1.8× more than harness choice, with Claude Opus 5 under OpenCode topping 3 of 4 tasks. This work directly addresses a timely AI safety concern: recursive self-improvement could be gamed if systems cheat by accessing held-out test data. By making isolation structural rather than instruction-based, the benchmark enables more trustworthy measurement of AI's ability to improve other AIs, which is central to understanding and governing potential intelligence explosions. The optimizer sees per-case traces only on the development split, receives a single aggregate score at validation, and gets no test feedback until a trusted server scores the final candidate harness; API keys, budget enforcement, and held-out data are kept outside the sandbox. In one release-trend analysis from Nov 2025 to Jul 2026, GPT climbed from 3% to 49% of available headroom and Claude Opus from 37% to 59%, while opencode beat native harnesses in 11 of 20 model–task pairs.

reddit · r/MachineLearning · /u/shehio · Aug 27, 20:13

**Background**: Recursive self-improvement (RSI) is the hypothesised ability of an AI system to rewrite or enhance its own code, potentially leading to an intelligence explosion and superintelligence, though no current system has demonstrated true RSI. An agent harness is the infrastructure that wraps around an LLM to give it tools, memory, and an execution loop, turning it into an autonomous agent. Harness optimization means modifying that infrastructure to improve downstream performance, a capability that is difficult to measure without giving the optimizer unfair access to test data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.06301">HarnessOpt - Bench : Evaluating LLMs at Harness Optimization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**Tags**: `#recursive self-improvement`, `#benchmark`, `#AI safety`, `#LLM`, `#machine learning`

---

<a id="item-10"></a>
## [ImageBench: New Public Benchmark Evaluates 52 Text-to-Image Models with VLM Judge](https://www.reddit.com/r/MachineLearning/comments/1vz9x9c/a_dataset_with_52_text_to_image_model_evaluation_p/) ⭐️ 8.0/10

A new public benchmark, ImageBench, evaluates 52 text-to-image models on 192 challenging prompts covering text rendering, spatial reasoning, human realism, and negations, using a vision-language model (VLM) as judge. All generated images, results, code, and the dataset are publicly available. Most public text-to-image leaderboards do not publish the actual generated images, making independent verification difficult. By releasing over 9,000 images, a reproducible VLM-judge methodology, code, and dataset, this benchmark improves transparency and enables more reliable model comparisons for researchers and practitioners. The benchmark uses 192 curated prompts and asks a VLM to answer a binary question with ground truth baked in per generated image; over 9,000 images were generated and analysed. Key limitations are that it is text-to-image only and VLM judges are not perfect, so scores may contain some noise.

reddit · r/MachineLearning · /u/dh7net · Aug 26, 21:10

**Background**: Text-to-image models generate images from natural language prompts, but evaluating their quality is challenging and often subjective. A vision-language model (VLM) combines visual and textual understanding, so 'VLM-as-a-judge' uses a larger multimodal model to automatically grade outputs of other models, often with rubric-based scoring or pairwise comparison. Public leaderboards commonly rank models by metrics such as preference scores but rarely share the actual images behind the rankings. This benchmark uses a VLM judge to assess specific prompt categories such as text rendering and spatial reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/vlm-as-a-judge">VLM-as-a-Judge: Multimodal Evaluation</a></li>
<li><a href="https://medium.com/@jiyang.kang/how-to-build-reliable-multimodal-ai-evaluators-using-vlm-judges-ca5663e3272a">How to Build Reliable Multimodal AI Evaluators Using VLM Judges</a></li>

</ul>
</details>

**Tags**: `#text-to-image`, `#benchmark`, `#dataset`, `#VLM-as-judge`, `#model-evaluation`

---

<a id="item-11"></a>
## [Fast Polyhedron Volume Computation Using the Divergence Theorem](https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html) ⭐️ 7.0/10

A blog post by Alyssa Rosenzweig explains a method for computing polyhedron volume via the divergence theorem, reducing the volume integral to a sum over triangular faces. This highlights a classical but efficient technique in computational geometry, useful for CAD, graphics, and mesh processing, and it sparked discussion of historical algorithms and related theorems. The method chooses a vector field with unit divergence, such as F=(x,0,0), and applies the divergence theorem to obtain volume as a sum of signed face contributions, equivalent to summing signed tetrahedron volumes from an origin, requiring consistent face orientation.

hackernews · luu · Aug 28, 09:00 · [Discussion](https://news.ycombinator.com/item?id=49476143)

**Background**: The divergence theorem (Gauss's theorem) equates the volume integral of a vector field's divergence to the flux through the closed boundary surface. For volume computation, one chooses a vector field with divergence 1, turning the volume integral into a surface integral. Since polyhedra have piecewise flat faces, the surface integral becomes a sum over faces of simple algebraic terms, yielding an O(n) algorithm for n faces. This approach has been known since at least Algorithm 550 in 1980.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Divergence_theorem">Divergence theorem</a></li>

</ul>
</details>

**Discussion**: Commenters generally appreciated the explanation but noted the technique is well-known in computational geometry, linking it to Algorithm 550 (1980) and to summing signed tetrahedron volumes. Some added related results like Pick's theorem for lattice polygons, while one commenter questioned the word 'hilariously' in the title.

**Tags**: `#computational geometry`, `#algorithms`, `#mathematics`, `#volume computation`, `#divergence theorem`

---

<a id="item-12"></a>
## [Sovereign Tech Agency Invests €500,000 in Flatpak Development](https://modal.cx/blog/announcing-flatpak-sta/) ⭐️ 7.0/10

The Sovereign Tech Agency announced a €500,000 investment in Flatpak, the Linux application packaging and sandboxing framework. This funding signals growing governmental recognition of open-source infrastructure as critical digital public infrastructure, and it may improve the security, portability, and developer experience of Linux desktop applications for millions of users. Flatpak uses a partial sandboxing model rather than full isolation, and applications bundle their own dependencies, which can lead to high disk usage on small storage devices. The funding is temporary and project-based, does not directly employ developers, and requires repeated applications for continued support.

hackernews · eigenspace · Aug 28, 05:42 · [Discussion](https://news.ycombinator.com/item?id=49474786)

**Background**: Flatpak is a Linux software deployment and package management utility that lets developers distribute applications in a sandboxed environment, bundling libraries so apps can run across many Linux distributions without dependency conflicts. It is one of several packaging formats alongside deb, RPM, Snap, and AppImage. Application sandboxing restricts an app's access to the rest of the system to reduce security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flatpak">Flatpak - Wikipedia</a></li>
<li><a href="https://flatpak.org/">The future of apps on Linux — Flatpak</a></li>

</ul>
</details>

**Discussion**: The community response is mixed: some express gratitude for Sovereign Tech Agency's support but criticize the funding as temporary, application-based, and lacking direct developer employment or long-term security. Others question Flatpak's sandboxing approach, preferring stricter directory-based isolation or tools like Firejail, and some report practical problems such as high disk usage from bundled dependencies.

**Tags**: `#flatpak`, `#open-source-funding`, `#sovereign-tech-agency`, `#linux`, `#packaging`

---

<a id="item-13"></a>
## [OpenTIE and OpenXWA: Modern Open-Source Ports of Classic Star Wars Sims](https://github.com/elyosh/OpenTIE/) ⭐️ 7.0/10

OpenTIE and OpenXWA have been announced as modern open-source ports (reimplementations) of the classic LucasArts games TIE Fighter and X-Wing Alliance, allowing them to run on current systems with original game data. These projects help preserve beloved 1990s Star Wars space sims, making them accessible on modern hardware and encouraging continued community modding and enjoyment for both old fans and new players. OpenXWA is an in-progress faithful re-implementation of X-Wing Alliance with optional enhancements and two visual modes, running original game data on Windows, Linux, and macOS; OpenTIE targets TIE Fighter similarly, and original copies are available on GOG.

hackernews · elyosh · Aug 27, 22:10 · [Discussion](https://news.ycombinator.com/item?id=49471965)

**Background**: TIE Fighter (1994) and X-Wing Alliance (1999) are classic space combat simulation games set in the Star Wars universe. Open-source ports like OpenTIE and OpenXWA are community reimplementations that replace the original executables while still requiring the original game assets, making the games compatible with modern operating systems and hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/elyosh/OpenXWA">GitHub - elyosh/ OpenXWA · GitHub</a></li>
<li><a href="https://www.generationamiga.com/2026/08/01/openxwa-rebuilds-x-wing-alliance-for-windows-linux-and-macos/">OpenXWA rebuilds X-Wing Alliance for Windows, Linux and macOS</a></li>

</ul>
</details>

**Discussion**: Commenters are largely nostalgic, sharing childhood memories of playing TIE Fighter and X-Wing with flight controllers. They also highlight related mods like the TIE Fighter Total Conversion for X-Wing Alliance and XWVM for the original X-Wing, and note that originals are available on GOG. One user asks about the technical difference between TIE Fighter 95 and 98 flight mechanics.

**Tags**: `#open-source`, `#gaming`, `#reverse-engineering`, `#star-wars`, `#game-preservation`

---

<a id="item-14"></a>
## [Doctors Begin to Manage Antidepressant Withdrawal](https://www.newscientist.com/article/2584861-antidepressant-withdrawal-symptoms-are-prompting-a-radical-rethink-of-how-we-treat-depression/) ⭐️ 7.0/10

A New Scientist article reports that medical professionals are starting to acknowledge and manage antidepressant withdrawal symptoms, shifting from earlier dismissals that symptoms are rare or mild. This shift matters because millions of patients take SSRIs and SNRIs, and inadequate warnings about withdrawal and long-term side effects have caused unnecessary suffering; better tapering guidance could improve patient safety and trust in mental health care. Patient comments describe severe withdrawal experiences such as heart palpitations and emotional blunting, and many report self-managing tapering with pill crushers and milligram scales because doctors' schedules are too aggressive; drug half-life and individual metabolic differences affect withdrawal intensity.

hackernews · eutropheon · Aug 27, 22:26 · [Discussion](https://news.ycombinator.com/item?id=49472090)

**Background**: Antidepressants like SSRIs (selective serotonin reuptake inhibitors) are widely prescribed for depression and anxiety. Discontinuation can cause withdrawal symptoms such as dizziness, brain zaps, and mood changes. Gradual tapering over weeks or months is generally recommended to minimize these effects. Medical guidelines have historically underemphasized withdrawal risks.

**Discussion**: Community comments are overwhelmingly critical of the medical system, sharing personal stories of being uninformed about sexual side effects, weight gain, and withdrawal severity. Some users report ignoring doctors' aggressive tapering schedules and self-managing gradual dose reductions; others note that cold turkey is worst and that drug half-life and individual metabolism cause varied experiences.

**Tags**: `#health`, `#medicine`, `#psychiatry`, `#antidepressants`, `#SSRI withdrawal`

---

<a id="item-15"></a>
## [Show HN: The Load-Bearing Vocabulary of Claude](https://louisabraham.github.io/load-bearing/) ⭐️ 7.0/10

A new interactive analysis at louisabraham.github.io/load-bearing identifies and visualizes the distinctive 'load-bearing' vocabulary that Claude uses with unusually high frequency. For example, the phrase 'load-bearing' appears 123.04× more frequently than in a general corpus, and the dataset is updated daily via GitHub Actions. This analysis helps users and developers recognize characteristic AI-generated language patterns, which can be useful for detecting machine-written text and understanding model biases. It also highlights a broader trend where LLMs develop overused stylistic tics that can make their output feel formulaic or robotic. The site computes frequency ratios against a corpus and currently reports 'load-bearing' at 123.04× more frequent. The author is adding a search bar and scaling the dataset to 1,000 pull requests per day; a commenter found that instructing Claude with Orwell's rule against clichés led the model to acknowledge a conflict with its system prompt.

hackernews · Labo333 · Aug 27, 08:59 · [Discussion](https://news.ycombinator.com/item?id=49461817)

**Background**: Claude is a family of large language models developed by Anthropic, first released as a chatbot in March 2023 and trained using Constitutional AI. 'Load-bearing' is an idiom for something essential that supports a structure, here used metaphorically to describe phrases that carry meaning but may be overused. Large language models often pick up distinctive vocabulary from training data and reinforcement learning, which can become recognizable markers of AI-generated text.

<details><summary>References</summary>
<ul>
<li><a href="https://louisabraham.github.io/load-bearing/">The load - bearing vocabulary of Claude</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>

</ul>
</details>

**Discussion**: Community reaction was largely positive and engaged, with appreciation for the site's concise, unbiased presentation and daily updates. Some commenters expressed concern that LLMs' distinctive vocabulary and stylistic tics are becoming markers of robotic writing across all major models, and wondered whether a feedback loop is worsening the problem. One user shared a striking experiment where Claude acknowledged that an anti-cliché instruction conflicted with its own system prompt.

**Tags**: `#AI`, `#LLM`, `#Claude`, `#vocabulary`, `#data-analysis`

---

<a id="item-16"></a>
## [Recovered 575k crop labels show ten manual clicks per book beat ML scaling](https://www.reddit.com/r/MachineLearning/comments/1vz2ojw/we_recovered_575k_crop_labels_from_a_decade_of/) ⭐️ 7.0/10

Researchers recovered 575,729 crop labels from ten years of manual Photoshop finishing of 1,765 digitized Urdu books, registered them to raw photos using SIFT+MAGSAC, and used them as supervision. They found that scaling training data from 378 to 572 books, using ResNet-50, 1024px inputs, or a spatial head did not improve unseen-book crop detection (pass@80), but using ten operator-corrected crops per book raised pass@80 from 0.71 to 0.83. This negative result shows that for document digitization with operator-specific margin preferences, more data, larger models, and higher resolution cannot recover information that is not in the pixels. The finding that ten manual calibration clicks per book beat all scaling levers offers a practical, low-cost strategy for niche archival and digitization workflows. The dataset contains 575,729 finished pages across 1,765 books; per-book error analysis showed failures were near-constant offsets from each operator's preferred margin inset, which is not present in new book pixels. For retouching, a U-Net only proposes removal support while classical OpenCV reconstructs the paper, ensuring everything outside the mask is byte-identical; the stricter REMOVE/KEEP/IGNORE labeling raised mark IoU from 0.56 to 0.60 and eliminated Urdu diacritic false positives.

reddit · r/MachineLearning · /u/laamaleph · Aug 26, 16:53

**Background**: SIFT (Scale-Invariant Feature Transform) detects and matches keypoints between images; MAGSAC is a robust model-fitting algorithm that estimates geometric transformations without requiring an inlier-outlier threshold. ResNet-50 is a widely used 50-layer convolutional neural network with skip connections, often employed as a vision backbone. In document digitization, operators manually crop and retouch scanned pages; pass@80 likely measures the fraction of pages where the predicted crop overlaps the ground truth with an IoU of at least 0.8. The project used these techniques to mine supervision from a decade of manual Photoshop edits.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/danini/magsac">GitHub - danini/magsac: The MAGSAC algorithm for robust model fitting without using an inlier-outlier threshold · GitHub</a></li>
<li><a href="https://huggingface.co/microsoft/resnet-50">microsoft/resnet-50 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#computer vision`, `#dataset`, `#negative results`, `#document digitization`

---

<a id="item-17"></a>
## [Microduck: Small Bipedal Robot with Onboard AI Training and ONNX Export](https://pollen-robotics.com/microduck/) ⭐️ 6.0/10

Pollen Robotics announced Microduck, a small bipedal robot aimed at hobbyists and educators, featuring onboard AI training and ONNX export. It is equipped with a Rockchip RK3566 processor, 1GB RAM, 32GB storage, and Dynamixel servos, and ships with seven pre-built behaviors. This lowers the barrier for hobbyists and educators to experiment with reinforcement learning on real bipedal hardware, while ONNX export enables models to be transferred across frameworks and deployment targets. It reflects the growing accessibility of edge AI robotics. The robot weighs 800g, has a removable battery lasting about 1 hour, and runs its policy loop at 50Hz. It can train additional behaviors locally or via Hugging Face Jobs, then export them to ONNX for deployment.

hackernews · robotswantdata · Aug 27, 10:57 · [Discussion](https://news.ycombinator.com/item?id=49462763)

**Background**: Bipedal robots require complex balance and locomotion control, often trained with reinforcement learning in simulation. ONNX is an open format for machine learning models, enabling interoperability between different deep learning frameworks and hardware. Embedded processors with AI accelerators allow such models to run on the robot itself rather than relying on cloud inference.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/beginner/onnx/export_simple_model_to_onnx_tutorial.html">Export a PyTorch model to ONNX — PyTorch Tutorials 2.13.0+cu130...</a></li>
<li><a href="https://huggingface.co/docs/optimum-onnx/onnx/package_reference/export">Export functions · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Comments are generally positive and informational. Users note the simulator's AZERTY keyboard default (ZQSD) and suggest adding QWERTY support; others share detailed specs, mention MuJoCo as a common simulation engine, list open-source bipedal and quadruped alternatives, and compare Microduck with Mondorobotics.

**Tags**: `#robotics`, `#bipedal robot`, `#edge AI`, `#machine learning`, `#hardware`

---

<a id="item-18"></a>
## [Researcher Seeks Venue for Statistical/Probabilistic ML as LLMs Dominate Top Conferences](https://www.reddit.com/r/MachineLearning/comments/1w0kipf/where_to_submit_statprob_ml_d/) ⭐️ 6.0/10

A researcher with a track record of top ML publications observes that ICLR and NeurIPS are now dominated by LLM/agent papers and asks where the statistical/probabilistic ML community should submit, suggesting AISTATS/UAI as more suitable venues. This highlights a growing identity and venue crisis for statistical/probabilistic ML researchers as flagship ML conferences shift toward LLM/agent topics, potentially affecting career evaluation, community cohesion, and where core probabilistic methods get published. The post offers anecdotal observations (e.g., roughly one non-LLM paper per ten posters at ICLR) rather than a systematic analysis; it mentions AISTATS and UAI as candidate venues and references established researchers like Arnaud Doucet, Aapo Hyvärinen, Christian Naesseth, and Stefano Ermon who appear to still publish at top-three venues.

reddit · r/MachineLearning · /u/didimoney · Aug 28, 08:16

**Background**: Statistical/probabilistic machine learning uses probability theory and statistics to model uncertainty in learning, forming the mathematical foundation for many ML systems. AISTATS (Artificial Intelligence and Statistics) is an interdisciplinary conference at the intersection of computer science, AI, machine learning, statistics, and related areas. UAI (Uncertainty in Artificial Intelligence) is a premier conference on learning and reasoning under uncertainty, held annually since 1985. In contrast, ICLR and NeurIPS are broad top-tier ML conferences that have recently seen a surge in LLM and agent-based submissions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/statistical-machine-learning">What is statistical machine learning? - IBM</a></li>
<li><a href="https://aistats.org/aistats2025/">Home| Artificial Intelligence and Statistics Conference</a></li>
<li><a href="https://auai.org/uai2026/">uai 2026</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#academic publishing`, `#probabilistic ML`, `#conferences`, `#research community`

---

<a id="item-19"></a>
## [NeurIPS 2026 Acceptance Calculator Estimates Paper Chances from Review Scores](https://www.reddit.com/r/MachineLearning/comments/1vzzw38/neurips_2026_acceptance_calculator_p/) ⭐️ 6.0/10

A Reddit user released a web-based tool that estimates the probability of a paper being accepted at NeurIPS 2026 by inputting review scores and an assumed acceptance rate. This gives researchers submitting to NeurIPS a quick way to gauge acceptance chances, though the estimate depends heavily on the assumed acceptance rate and may not reflect official review outcomes. It also addresses a common need for score-to-decision transparency in the ML community. The tool is a simple model hosted on GitHub Pages, taking review scores and an acceptance rate as inputs; it assumes a relationship between scores and acceptance but details of the model or its assumptions are not provided.

reddit · r/MachineLearning · /u/levydawg · Aug 27, 17:07

**Background**: NeurIPS is a leading annual machine learning conference where submitted papers receive reviewer scores before acceptance decisions. Authors often receive overall and confidence scores that inform area chairs, but final acceptance also depends on discussion, rebuttal, and contribution type. Public statistics on score distributions can be scarce until review phases complete, so tools that estimate acceptance from scores are of interest.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeurIPS">NeurIPS</a></li>
<li><a href="https://papercopilot.com/statistics/neurips-statistics/neurips-2025-statistics/">NeurIPS 2025 Statistics - Paper Copilot</a></li>
<li><a href="https://neurips.cc/Conferences/2026/ReviewerGuidelines">NeurIPS 2026 Reviewing Guidelines</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#NeurIPS`, `#acceptance prediction`, `#research tool`, `#conference`

---

<a id="item-20"></a>
## [py-evoFE v0.3.0 Automates Feature Engineering with Genetic Algorithms](https://www.reddit.com/r/MachineLearning/comments/1w0788j/pyevofe_automated_evolutionary_feature/) ⭐️ 6.0/10

py-evoFE v0.3.0, an open-source MIT-licensed Python library, was released to automate tabular feature engineering by evolving hierarchical feature recipes with genetic programming and over 40 built-in transformers. Manual feature engineering is tedious and brute-force generation often causes overfitting; py-evoFE aims to discover compact, generalizable features that can improve GBDT and other tabular models, potentially benefiting Kaggle competitors and production ML teams. It provides hierarchical chaining, target encodings, string similarity, manifold/dimensionality reduction, and graph clustering; uses Polars/PyArrow vectorization, matrix hashing and nearest-neighbor caching, multi-fidelity screening, island-model search with Gibbs migration, Caruana ensembling, and an interactive replay viewer, while being 100% Scikit-Learn compatible. As an early-stage v0.3.0 release, it has not yet been validated by community benchmarks or discussion.

reddit · r/MachineLearning · /u/tanopereira · Aug 27, 21:33

**Background**: Feature engineering transforms raw tabular data into more informative inputs for machine learning models. Genetic algorithms are search heuristics inspired by natural selection that evolve candidate solutions through selection, crossover, and mutation. Polars is a high-performance columnar DataFrame library built on Apache Arrow, used here to accelerate feature computation. Scikit-learn is a widely used Python ML library whose pipeline and model-selection APIs allow py-evoFE to integrate with existing workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Feature_engineering">Feature engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Genetic_algorithm">Genetic algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polars_(software)">Polars (software) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#feature engineering`, `#genetic algorithms`, `#machine learning`, `#Python`, `#automated machine learning`

---