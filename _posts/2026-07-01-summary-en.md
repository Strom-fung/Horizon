---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 35 items, 21 important content pieces were selected

---

1. [Google's Agentic AI Reviews 10K Papers at ICML/STOC, Formal Paper Released](#item-1) ⭐️ 9.0/10
2. [Claude Code Secretly Embeds Steganographic Identifiers in Requests](#item-2) ⭐️ 8.0/10
3. [US Lifts Export Controls on Claude Fable 5 and Mythos 5 with Restrictions](#item-3) ⭐️ 8.0/10
4. [Anthropic Launches Claude Science for Data Science](#item-4) ⭐️ 8.0/10
5. [Kubernetes Ported to the Browser Using WebAssembly](#item-5) ⭐️ 8.0/10
6. [Anthropic's Claude Sonnet 5 Offers Near-Opus 4.8 Performance at Lower Prices](#item-6) ⭐️ 8.0/10
7. [80TB+ Astronomy Crossmatching Now Possible on a Laptop with 4GB RAM](#item-7) ⭐️ 8.0/10
8. [Google Copybara: Transforming and Moving Code Between Repositories](#item-8) ⭐️ 7.0/10
9. [Google Releases Nano Banana 2 Lite for Fast Image Generation](#item-9) ⭐️ 7.0/10
10. [Meta AI's Brain2Qwerty Enables Non-Invasive Brain-to-Text Decoding](#item-10) ⭐️ 7.0/10
11. [CERN's LHC Enters Long Shutdown 3 for Major Upgrade](#item-11) ⭐️ 7.0/10
12. [shot-scraper 1.10 introduces video recording of Playwright demos](#item-12) ⭐️ 7.0/10
13. [HTML Table Extractor: Paste Rich Text to Convert Tables](#item-13) ⭐️ 7.0/10
14. [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding Released](#item-14) ⭐️ 7.0/10
15. [REAP: Automatic Curation of Coding Agent Benchmarks from Interactive Production Usage](#item-15) ⭐️ 7.0/10
16. [Cerebras-OpenAI Deal Strands Small AI Startups on API Waitlist](#item-16) ⭐️ 7.0/10
17. [EML Trees Are Universal Approximators](#item-17) ⭐️ 7.0/10
18. [uv 0.11.26: Resolver Performance Gains and Build Cache Warning](#item-18) ⭐️ 6.0/10
19. [Mistral Releases Leanstral 1.5 for Lean 4 Theorem Proving](#item-19) ⭐️ 6.0/10
20. [CVIL Checklist Adds Segmentation, OCR, and VLM Tracks](#item-20) ⭐️ 6.0/10
21. [EACL 2027 Splits Author Response and Reviewer Discussion into Two Stages](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google's Agentic AI Reviews 10K Papers at ICML/STOC, Formal Paper Released](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-review system that evaluated approximately 10,000 papers submitted to ICML and STOC, catching 34% more mathematical errors than standard zero-shot prompting, and the formal research paper detailing this deployment is now publicly available. This large-scale deployment demonstrates that agentic AI can significantly improve the accuracy and efficiency of scientific peer review, potentially reducing reviewer burden and enhancing error detection, with far-reaching implications for academic publishing. The system provided feedback within 30 minutes per paper and outperformed zero-shot prompting by 34% in identifying mathematical errors; the new arXiv paper documents the methodology and results in full.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Agentic AI refers to systems that can autonomously pursue complex goals by planning and using tools, going beyond simple prompt-response interactions. Zero-shot prompting is a technique where a model is asked to perform a task without any prior examples, relying only on its pre-trained knowledge. In academic peer review, catching subtle mathematical errors requires deep reasoning, which agentic workflows can enhance by chaining multiple verification steps or calling external tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**Tags**: `#AI`, `#peer-review`, `#automation`, `#machine-learning`, `#scientific-computing`

---

<a id="item-2"></a>
## [Claude Code Secretly Embeds Steganographic Identifiers in Requests](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

Anthropic's Claude Code tool has been found to covertly embed steganographic marks in API requests, likely to identify and prevent unauthorized model distillation. This hidden behavior raises serious transparency and trust concerns, highlighting the tension between intellectual property protection and openness in the AI industry. The identifiers are embedded within the prompt text using steganographic techniques, but the implementation is reportedly simplistic and easily detectable upon code inspection.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Claude Code is a terminal-based AI coding assistant by Anthropic. Steganography conceals data within other data (e.g., text) to avoid detection. Model distillation uses a powerful 'teacher' model's outputs to train a smaller 'student' model, potentially enabling unauthorized capability replication.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: some view the undisclosed tracking as a serious breach of trust, while others consider it a justified anti-distillation measure, though the sloppy implementation drew criticism. Calls for open-source alternatives like Codex CLI also emerged.

**Tags**: `#security`, `#AI`, `#anthropic`, `#steganography`, `#transparency`

---

<a id="item-3"></a>
## [US Lifts Export Controls on Claude Fable 5 and Mythos 5 with Restrictions](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 8.0/10

The US Department of Commerce lifted export controls on Anthropic's Claude Fable 5 and Mythos 5 models on June 30, 2026, but mandated new classifiers that block certain cybersecurity tasks, causing coding and debugging to fall back to Opus 4.8. This decision underscores the delicate balance between AI safety and commercial availability, impacting businesses reliant on cutting-edge AI and signaling how governments might restrict AI capabilities even after lifting broad bans. The new classifiers specifically target cybersecurity tasks, with routine coding and debugging falling back to Opus 4.8. The Commerce Department's letter, dated June 30, 2026, addressed to Anthropic's Chief Compute Officer, followed earlier communications on June 12 and 26.

hackernews · Pragmata · Jun 30, 23:55 · [Discussion](https://news.ycombinator.com/item?id=48740771)

**Background**: Claude Fable 5 is a safe-for-general-use version of Anthropic's advanced model, while Claude Mythos 5 is designed for vulnerability detection by select businesses. The US had previously imposed export controls on these models due to concerns over misuse in cybersecurity. This partial lifting, with operational restrictions, reflects ongoing negotiations between the US government and AI developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.bbc.com/news/articles/cdr42623e1do">Fable and Mythos : Anthropic says US lifts export ban on its advanced...</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Commenters worry about unpredictability in AI regulation, with some arguing that coding restrictions undermine business trust in US AI models. There is a call for clear laws instead of ad-hoc actions, and debate over whether AI should be regulated like nuclear technology. Sentiment is mixed, with frustration over the lack of clarity and potential chilling effect on investment.

**Tags**: `#AI regulation`, `#export controls`, `#Anthropic`, `#cybersecurity`, `#tech policy`

---

<a id="item-4"></a>
## [Anthropic Launches Claude Science for Data Science](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic has launched Claude Science, a new AI tool for data science that integrates with institutional high-performance computing (HPC) clusters and databases. It features a local server and web-based UI, enabling secure operation in locked-down research environments. This tool addresses the needs of pharmaceutical and scientific research organizations with strict data security, allowing researchers to use AI for data analysis without exposing sensitive data to external servers. It could significantly speed up routine data science tasks and enable non-experts to perform complex analyses. Claude Science uses a local server with a browser-based UI, differing from Claude Code or Cowork, and integrates with Jupyter notebooks, pandas, and institutional clusters. Early testing shows it can handle basic tasks like RNAi design but may require iterative prompting for optimal results.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: High-performance computing (HPC) involves supercomputers and clusters for advanced computation. Data science relies on tools like pandas and Jupyter notebooks for analysis. In pharmaceutical and other research settings, data often resides in locked-down environments with no external access, necessitating on-premise AI solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High-performance_computing">High-performance computing</a></li>
<li><a href="https://www.oracle.com/europe/cloud/hpc/what-is-hpc/">What Is High Performance Computing ? | Oracle Europe</a></li>

</ul>
</details>

**Discussion**: Commenters note the tool's integration with HPC and databases is its most valuable feature, especially for pharma environments requiring a local server. Performance is mixed: it can one-shot simple designs but acts like a novice, improving with feedback. Some highlight its focus on data science over broader science.

**Tags**: `#AI`, `#data-science`, `#scientific-computing`, `#Anthropic`, `#HPC`

---

<a id="item-5"></a>
## [Kubernetes Ported to the Browser Using WebAssembly](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser) ⭐️ 8.0/10

Ngrok released webernetes, an open-source project that ports Kubernetes to the browser using WebAssembly, enabling a simulated Kubernetes cluster to run entirely client-side for education and testing. This innovation simplifies Kubernetes education by removing infrastructure hurdles and offers a novel platform for validating AI-generated infrastructure code, impacting both learning and DevOps automation. While it replicates the Kubernetes API and behavior, it does not run real containers; services need custom browser-side implementations. The project is still early-stage and more suited for conceptual learning rather than production workloads.

hackernews · peterdemin · Jun 30, 20:48 · [Discussion](https://news.ycombinator.com/item?id=48738985)

**Background**: Kubernetes is a widely-used open-source system for automating deployment, scaling, and management of containerized applications. WebAssembly is a portable binary format that allows high-performance execution of code in web browsers, enabling languages like C++ and Rust to run on the client side. This project combines these technologies to bring a Kubernetes-like environment directly into the browser without any backend servers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ngrok/webernetes">GitHub - ngrok/ webernetes : Kubernetes in the browser. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kubernetes">Kubernetes - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>

</ul>
</details>

**Discussion**: Overall, commenters praised its creativity and educational potential, highlighting its use for mastering kubectl and testing AI-generated infrastructure code. Some noted it doesn't run real containers and is better for architectural understanding, but the general sentiment was highly positive.

**Tags**: `#kubernetes`, `#webassembly`, `#browser`, `#education`, `#devtools`

---

<a id="item-6"></a>
## [Anthropic's Claude Sonnet 5 Offers Near-Opus 4.8 Performance at Lower Prices](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.0/10

Anthropic released Claude Sonnet 5 this morning, with performance close to Opus 4.8 but at lower prices. The model introduces a new tokenizer that increases token counts by about 30% for English text, and its system card details reduced cyber capabilities that enabled an unblocked release. The lower cost and near-Opus performance make advanced AI more accessible for developers and businesses, while the system card transparency could set a precedent for responsible model release. However, the tokenizer change means effective pricing is higher than sticker price, impacting cost calculations. The new tokenizer yields roughly 1.4x more tokens for English, 1.33x for Spanish, 1.28x for Python, but nearly the same for Chinese. Sampling parameters temperature, top_p, top_k are removed; context window is 1M input and 128K output tokens; adaptive thinking is on by default; base pricing is $3/$15 per million tokens with an introductory discount.

rss · Simon Willison · Jun 30, 21:23

**Background**: Claude is a family of large language models by Anthropic, with Sonnet as the mid-range tier and Opus as the high-performance tier. System cards document safety evaluations and capabilities; previously, models with high cyber capabilities faced regulatory hurdles, so Sonnet 5's reduction allowed an unblocked release. Tokenization breaks text into units for processing, and changes affect both pricing and context window utilization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(Anthropic)">Mythos (Anthropic)</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some question the cost-effectiveness compared to lower-effort Opus or GLM 5.2, while others appreciate the reduced cyber capabilities enabling release. There are concerns that agentic optimizations may hurt non-agentic performance, and benchmarks point to weaknesses in trivia and tool-calling tasks.

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#LLM`, `#Model Release`

---

<a id="item-7"></a>
## [80TB+ Astronomy Crossmatching Now Possible on a Laptop with 4GB RAM](https://www.reddit.com/r/MachineLearning/comments/1uk7ec6/80tb_of_astronomy_for_the_hddpoor_crossmatch_the/) ⭐️ 8.0/10

The Multimodal Universe dataset, pooling over 80TB from 30+ astronomical surveys, is now available in HATS format on Hugging Face. It enables streaming crossmatching on a laptop with as little as 4GB RAM, eliminating the need for local downloads. This democratizes large-scale astronomical analysis, allowing researchers and hobbyists with limited hardware to perform complex cross-survey studies. It removes a major barrier in multi-wavelength and time-domain astronomy, where linking catalogs typically demands substantial storage and computing power. The HATS (Hierarchical Adaptive Tiling Scheme) format partitions data using HEALPix pixels, enabling efficient columnar streaming via the LSDB library. An active internet connection is required to access the remote datasets, and crossmatch performance depends on network speed.

reddit · r/MachineLearning · /u/Smith4242 · Jul 1, 01:07

**Background**: Crossmatching identifies observations of the same celestial object across different surveys. Traditionally, this required downloading multi-terabyte catalogs locally. The Multimodal Universe aggregates data from missions like Gaia (which mapped over a billion stars) and many others. Converting to HATS allows columnar access and streaming, drastically reducing client-side requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/hugging-science/multimodal-universe-hats">80TB+ of astronomy for the HDD-poor: crossmatch the Multimodal ...</a></li>
<li><a href="https://docs.lsdb.io/en/stable/data-access/hats-huggingface.html">HATS catalogs on Hugging Face — LSDB</a></li>
<li><a href="https://github.com/MultimodalUniverse/MultimodalUniverse/releases">Releases · MultimodalUniverse/MultimodalUniverse</a></li>

</ul>
</details>

**Tags**: `#astronomy`, `#big-data`, `#open-science`, `#data-access`, `#machine-learning`

---

<a id="item-8"></a>
## [Google Copybara: Transforming and Moving Code Between Repositories](https://github.com/google/copybara) ⭐️ 7.0/10

Google's Copybara tool for code migration and synchronization between repositories is being discussed, with users sharing experiences and alternatives like Josh and fbshipit. This tool helps developers manage monorepo and multi-repo workflows by simplifying code sharing, reducing dependency overhead, and enabling selective exports with history preservation, which is crucial for large-scale software development. Copybara is an Apache-2.0 licensed tool used internally at Google, supporting bidirectional shipping but commonly used for simple one-way exports; it transforms code layouts while preserving Git history.

hackernews · reconnecting · Jun 30, 23:45 · [Discussion](https://news.ycombinator.com/item?id=48740698)

**Background**: A monorepo is a single repository containing multiple projects, used by companies like Google to streamline code sharing. Copybara facilitates moving code between such repositories or splitting parts into separate repos, often used when extracting a library from a monorepo.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google/copybara">GitHub - google/ copybara : Copybara : A tool for transforming and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monorepo">Monorepo</a></li>

</ul>
</details>

**Discussion**: Users discussed using Copybara for simple one-way exports to new repos, its suitability for sharing code without creating library dependencies, and alternatives like Josh (used by Rust) and fbshipit (previously by Meta). Some expressed curiosity about downsides and tips for open-sourcing from monorepos.

**Tags**: `#code-sync`, `#monorepo`, `#devtools`, `#git`, `#copybara`

---

<a id="item-9"></a>
## [Google Releases Nano Banana 2 Lite for Fast Image Generation](https://deepmind.google/models/gemini-image/flash-lite/) ⭐️ 7.0/10

Google has launched Nano Banana 2 Lite (officially Gemini 3.1 Flash Lite Image), its fastest and most cost-efficient image generation model, capable of producing images in roughly 4 seconds—much quicker than the 20–30 seconds of the standard Nano Banana 2. This model enables rapid-fire prototyping and high-throughput applications at lower cost, making AI image generation more accessible for developers. However, it also raises ethical concerns, as highlighted by community reports of misuse in real estate listings. The model trades some image nuance for speed, and currently lacks programmable aspect ratio control, but it excels at text rendering and can be chained with Gemini Omni Flash for video generation.

hackernews · minimaxir · Jun 30, 16:48 · [Discussion](https://news.ycombinator.com/item?id=48735444)

**Background**: Nano Banana is Google's family of image generation models, where Nano Banana 2 is the full-quality version. A 'Lite' variant denotes a distilled, faster model. This release is part of the Gemini 3.1 family and is available via Google AI Studio and cloud APIs, though access may be restricted for users without a compatible Google One or Workspace setup.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/">Start building with Nano Banana 2 Lite and Gemini Omni Flash</a></li>
<li><a href="https://arstechnica.com/ai/2026/06/googles-new-nano-banana-2-lite-image-model-is-its-fastest-and-cheapest-yet/">Google's new Nano Banana 2 Lite image model is its fastest and cheapest yet - Ars Technica</a></li>
<li><a href="https://venturebeat.com/technology/google-unveils-nano-banana-2-lite-aka-gemini-3-1-flash-lite-for-low-cost-4-second-fast-enterprise-image-generations">Google unveils Nano Banana 2 Lite aka Gemini 3.1 Flash-Lite for low cost, 4-second fast enterprise image generations | VentureBeat</a></li>

</ul>
</details>

**Discussion**: Users praise the impressive speed and improved text rendering, with one building a children’s story app. Criticism includes its misuse to artificially enhance real estate photos, access headaches for Google Workspace users without a Google One account, and disappointment over the omission of ChatGPT in comparison charts.

**Tags**: `#AI`, `#image-generation`, `#Google`, `#Gemini`, `#developer-tools`

---

<a id="item-10"></a>
## [Meta AI's Brain2Qwerty Enables Non-Invasive Brain-to-Text Decoding](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/?_fb_noscript=1) ⭐️ 7.0/10

Meta AI has released Brain2Qwerty v2, an open-source AI system that translates brain activity into text using non-invasive MEG and EEG, achieving an average word accuracy of 61%. This advancement demonstrates that non-invasive brain-computer interfaces can achieve meaningful text decoding, potentially aiding communication for individuals with neurological disorders without surgery, while also raising significant privacy concerns as neural data becomes accessible. The system was trained on data from 35 healthy volunteers, uses a deep learning model with a character error rate of 32%, and requires a magnetically shielded room with specialized MEG equipment, limiting current practical applications.

hackernews · alok-g · Jun 30, 21:29 · [Discussion](https://news.ycombinator.com/item?id=48739466)

**Background**: Magnetoencephalography (MEG) non-invasively detects magnetic fields from brain electrical currents, while electroencephalography (EEG) measures scalp electrical activity; both have lower signal quality than invasive implants. Recent AI advances, including large language models, have improved non-invasive neural signal decoding, building on decades of brain-computer interface research.

<details><summary>References</summary>
<ul>
<li><a href="https://icymi.in/article/meta-unveils-ai-system-that-translates-brain-signals-into-text-with-61-accuracy">Meta unveils AI system that translates brain signals into text with 61...</a></li>
<li><a href="https://www.bhaskarenglish.in/tech-science/video/meta-unveils-brain2qwerty-ai-brain-text-neurological-disorders-138326861.html?type=video">Meta Unveils Brain 2 Qwerty AI System | Brain-to-Text for Neurological...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magnetoencephalography">Magnetoencephalography - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community praises the open-source release but notes the improvement is incremental. Strong privacy concerns are raised, comparing neural data tracking to internet surveillance. Some speculate on future applications like controlling robots or fast typing, referencing past related demos.

**Tags**: `#BCI`, `#EEG`, `#MEG`, `#neuroscience`, `#AI`

---

<a id="item-11"></a>
## [CERN's LHC Enters Long Shutdown 3 for Major Upgrade](https://home.cern/cern-bids-farewell-to-the-lhc-and-enters-long-shutdown-3/) ⭐️ 7.0/10

CERN's Large Hadron Collider has begun its third long shutdown (LS3) to be transformed into the High-Luminosity LHC (HL-LHC), aiming for a tenfold increase in collision data and targeting a restart in 2030. The HL-LHC upgrade will dramatically boost discovery potential, enabling precise studies of the Higgs boson and searches for new physics beyond the Standard Model, with profound implications for fundamental science. The HL-LHC will provide proton-proton collisions at 14 TeV with integrated luminosity up to 3 ab⁻¹, featuring major detector upgrades like ATLAS's new Inner Tracker (ITk) with 5 billion channels, up from 8 million.

hackernews · HelloUsername · Jun 29, 18:52 · [Discussion](https://news.ycombinator.com/item?id=48723484)

**Background**: The Large Hadron Collider (LHC) at CERN is the world's most powerful particle accelerator, famous for discovering the Higgs boson in 2012. The High-Luminosity LHC (HL-LHC) upgrade aims to increase the collision rate by a factor of ten, enabling more detailed studies of rare particles. Long shutdowns are periodic breaks for maintenance and major upgrades; LS3 is the third such shutdown, expected to last until 2030.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Luminosity_Large_Hadron_Collider">High Luminosity Large Hadron Collider</a></li>
<li><a href="https://home.cern/cern-bids-farewell-to-the-lhc-and-enters-long-shutdown-3/">CERN bids farewell to the LHC and enters Long Shutdown 3 – Home | CERN</a></li>
<li><a href="https://home.cern/tag/long-shutdown-3/">Long Shutdown 3 – Home | CERN</a></li>

</ul>
</details>

**Discussion**: Commenters reflected on the canceled Superconducting Supercollider and its potential to surpass the LHC; some found the title overdramatic but praised detector advances like ATLAS's ITk. Others noted the opportunity for underground tours during shutdown and CERN's exabyte-scale data storage.

**Tags**: `#particle-physics`, `#CERN`, `#LHC`, `#scientific-infrastructure`, `#upgrades`

---

<a id="item-12"></a>
## [shot-scraper 1.10 introduces video recording of Playwright demos](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 7.0/10

Simon Willison released shot-scraper 1.10, which includes the new `shot-scraper video` command for recording Playwright-based video demos from a storyboard YAML file. This tool automates the creation of video demos, enabling developers and coding agents to prove that their code works as intended, which is valuable for testing and documentation. The command uses a storyboard file to define steps like clicks and pauses, supports authentication via cookies, and can output in MP4 or WebM formats. The example demonstrates a Datasette feature with user interactions and a clipboard override JavaScript snippet.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool for automated screenshots and web scraping, built on the Playwright browser automation library. Playwright provides reliable cross-browser automation for testing and interaction. A storyboard file is a YAML file that specifies a sequence of actions to perform on a web page.

<details><summary>References</summary>
<ul>
<li><a href="https://shot-scraper.datasette.io/">shot-scraper</a></li>
<li><a href="https://simonwillison.net/2022/Mar/10/shot-scraper/">shot-scraper: automated screenshots for documentation, built on Playwright</a></li>

</ul>
</details>

**Tags**: `#shot-scraper`, `#automation`, `#playwright`, `#video-recording`, `#tool-release`

---

<a id="item-13"></a>
## [HTML Table Extractor: Paste Rich Text to Convert Tables](https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything) ⭐️ 7.0/10

Simon Willison released a new paste-conversion tool that extracts HTML tables from clipboard rich text and converts them into HTML, Markdown, CSV, TSV, or JSON. This tool streamlines the extraction of tabular data from web pages, a common pain point for developers and data analysts. It saves time and reduces friction when moving data between web sources and other applications. The tool leverages the browser's clipboard API to access rich text content, preserving table structures. An update added integration with Wikipedia's CORS API, allowing direct search and import of tables from Wikipedia pages.

rss · Simon Willison · Jun 29, 23:38

**Background**: Paste-conversion tools process content copied to the clipboard, often from browsers, and convert it to a different format. Rich text can include HTML markup and embedded elements like tables. Wikipedia provides a CORS-enabled API that allows external applications to request page content for reuse.

**Tags**: `#tool`, `#html`, `#table-extraction`, `#conversion`, `#web-development`

---

<a id="item-14"></a>
## [Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding Released](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 7.0/10

DeepReinforce has released Ornith-1.0, a family of open-weight (MIT licensed) self-scaffolding coding models based on Gemma 4 and Qwen 3.5, with variants up to 397B parameters, achieving state-of-the-art performance on coding benchmarks among open-source models of comparable size. This release brings competitive agentic coding to locally runnable, open models, allowing developers to use powerful coding agents without relying on cloud APIs, which could accelerate open-source AI development and offer more control and privacy. The models employ a self-scaffolding technique that enables them to autonomously manage tool calls during multi-step coding tasks; the 35B MoE variant, when quantized to Q4_K_M and run locally via LM Studio, demonstrated proficient handling of repository exploration and code generation at 103 tokens/second.

rss · Simon Willison · Jun 29, 16:17

**Background**: Self-scaffolding LLMs are models designed to autonomously construct and manage the scaffolding—such as prompts, tool calls, or sub-goals—needed to accomplish complex tasks, reducing the need for hard-coded external frameworks. Agentic coding extends this to software development, where AI agents handle multi-step tasks like codebase exploration, editing, and debugging with minimal human guidance. Ornith-1.0 fine-tunes existing base models (Gemma 4 and Qwen 3.5) to instill these agentic behaviors, enabling them to operate as effective coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://shaam.blog/articles/ornith-1-0-local-agentic-coding-guide">The Agentic Edge: Ornith-1.0 and the Rise of Self - Scaffolding Local...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#coding`, `#open-source`, `#model-release`, `#agentic-coding`

---

<a id="item-15"></a>
## [REAP: Automatic Curation of Coding Agent Benchmarks from Interactive Production Usage](https://www.reddit.com/r/MachineLearning/comments/1uk713d/reap_automatic_curation_of_coding_agent/) ⭐️ 7.0/10

Researchers introduced REAP (Relevance and Execution-Audited Pipeline), which automatically creates coding agent benchmarks from real developer-agent interaction logs, eliminating manual curation. This method enables more realistic, scalable, and up-to-date evaluation of coding agents by tapping into real-world usage data, potentially accelerating the development of better AI programming assistants. REAP uses execution auditing and relevance filtering to automatically sift through interactive logs, selecting only high-quality, task-completion sessions for benchmark inclusion without any human annotation.

reddit · r/MachineLearning · /u/julian88888888 · Jul 1, 00:50

**Background**: AI coding agents like GitHub Copilot or Cursor can autonomously write and edit code. Evaluating their performance requires benchmarks that reflect real programming tasks, but existing benchmarks are often manually curated and may become outdated. Production usage logs from developer-agent interactions offer a rich source of real-world data, but distilling them into high-quality benchmarks automatically has been challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.01527">[2604.01527] REAP : Automatic Curation of Coding Agent ...</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#benchmarks`, `#coding-agents`, `#automatic-curation`, `#production-data`, `#machine-learning`

---

<a id="item-16"></a>
## [Cerebras-OpenAI Deal Strands Small AI Startups on API Waitlist](https://www.reddit.com/r/MachineLearning/comments/1uiqhiv/cerebras_openai_deal_capacity_has_effectively/) ⭐️ 7.0/10

A small AI startup reveals that Cerebras's $20B deal with OpenAI has pre-allocated the vast majority of its near-term inference capacity, effectively making the API waitlist infinite for everyone else. The startup, which needs high-throughput inference for a real-time coding agent, has been waiting for months without access. This situation underscores the growing divide between hyperscalers and smaller players in accessing specialized AI hardware, potentially stifling innovation from startups that rely on high-throughput inference. It also raises concerns about market concentration when a single customer monopolizes a chipmaker's capacity. Cerebras's WSE-3 wafer-scale engine provides low-latency, high-throughput inference ideal for tasks like the startup's real-time coding agent requiring ~1-2k tokens/second. The $20B deal, signed in 2026 shortly after Cerebras went public, allocates capacity from these ASICs primarily to OpenAI, leaving little for others.

reddit · r/MachineLearning · /u/Kortopi-98 · Jun 29, 12:00

**Background**: Cerebras Systems manufactures the WSE-3, the world's largest AI chip, which uses wafer-scale integration to reduce latency and is particularly suited for inference. The company offers cloud API access to its hardware, but its production is limited by complex manufacturing. With recently going public, its capacity is heavily influenced by large-volume deals, as seen with G42 and now OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems</a></li>

</ul>
</details>

**Tags**: `#Cerebras`, `#OpenAI`, `#API access`, `#AI hardware`, `#inference`

---

<a id="item-17"></a>
## [EML Trees Are Universal Approximators](https://www.reddit.com/r/MachineLearning/comments/1uipl1t/eml_trees_are_universal_approximators_r/) ⭐️ 7.0/10

A new paper proves that trees composed of EML functions—a universal elementary function—can approximate any function in general spaces to arbitrary accuracy, establishing a universal approximation theorem for EML trees. This provides a rigorous mathematical foundation for using EML trees as function approximators, analogous to neural networks, which could open new directions in machine learning theory and algorithm design. The proof explicitly constructs representations of binary operations, polynomials, hyperbolic tangent, and partitions of unity; it also addresses the logarithm's domain limitation via sign-based decompositions and uses a generalized EML with learnable parameters.

reddit · r/MachineLearning · /u/JoeGermany · Jun 29, 11:16

**Background**: The EML function, short for exponential, multiplication, and logarithm, can represent all elementary functions through composition, like a mathematical NAND gate. The universal approximation theorem states that certain architectures, like neural networks, can approximate any continuous function arbitrarily well. This paper extends that idea to trees built from EML operations.

<details><summary>References</summary>
<ul>
<li><a href="https://graphicmaths.com/pure/special-functions/universal-eml-function/">GraphicMaths - A universal elementary function , EML</a></li>
<li><a href="https://monkfrom.earth/blogs/eml-operator-math-nand-gate">EML : The Single Operator That Generates All Math — Sameer Khan</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem</a></li>

</ul>
</details>

**Tags**: `#universal approximation`, `#EML trees`, `#function approximation`, `#machine learning theory`, `#mathematical proofs`

---

<a id="item-18"></a>
## [uv 0.11.26: Resolver Performance Gains and Build Cache Warning](https://github.com/astral-sh/uv/releases/tag/0.11.26) ⭐️ 6.0/10

uv 0.11.26, released on June 30, 2026, improves resolver performance by adapting to IDs-only PubGrub dependencies, reducing allocations, and reusing work, while also adding a warning when the build cache is inside the source directory. These performance optimizations make dependency resolution faster, benefiting users with complex dependency graphs, while the build cache warning prevents potential confusion and corrupted builds. The resolver improvements include adapting to IDs-only PubGrub dependencies, avoiding allocations in ForkMap::contains, reusing resolver work across iterations, and speeding up candidate selection for disjoint ranges. The build cache warning is a new bug fix for when the build cache path overlaps with the source directory.

github · github-actions[bot] · Jun 30, 14:53

**Background**: uv is a fast Python package and project manager written in Rust, serving as an alternative to pip. PubGrub is a version-solving algorithm used in package managers to resolve dependencies efficiently, using conflict-driven learning. The IDs-only optimization reduces the data communicated during resolution, likely by passing only package identifiers instead of full dependency specifications.

<details><summary>References</summary>
<ul>
<li><a href="https://nex3.medium.com/pubgrub-2fb6470504f">PubGrub: Next-Generation Version Solving | by Natalie Weizenbaum | Medium</a></li>
<li><a href="https://rust-lang.github.io/rust-project-goals/2024h2/pubgrub-in-cargo.html">Extend pubgrub to match cargo's dependency resolution - Rust Project Goals</a></li>

</ul>
</details>

**Tags**: `#uv`, `#Python`, `#package-manager`, `#performance`, `#release`

---

<a id="item-19"></a>
## [Mistral Releases Leanstral 1.5 for Lean 4 Theorem Proving](https://docs.mistral.ai/models/model-cards/leanstral-1-5-26-06) ⭐️ 6.0/10

Mistral has released Leanstral 1.5, an updated specialized language model for automated theorem proving in Lean 4, replacing the previous version that was deprecated on May 22nd. This release advances AI-assisted formal verification, potentially improving the efficiency of mathematicians and software engineers working with Lean 4, and reflects the growing intersection of AI and theorem proving. Leanstral 1.5 is offered as a 'Labs' model, indicating experimental access; users reported issues enabling it. The model can be used with the open-source OpenATP package, which supports Mistral’s Vibe harness.

hackernews · vetronauta · Jun 30, 20:44 · [Discussion](https://news.ycombinator.com/item?id=48738938)

**Background**: Lean 4 is a proof assistant based on dependent type theory, used for formalizing mathematical proofs and writing verified software. Automated theorem proving (ATP) involves using algorithms to prove logical statements, a field where AI models are increasingly applied. Mistral is an AI company that develops large language models, and Leanstral is a specialized version fine-tuned for generating Lean 4 code to assist in proving theorems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_4">Lean 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://github.com/leanprover/lean4">GitHub - leanprover/lean4: Lean 4 programming language and theorem prover · GitHub</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: enthusiasm for the model's potential, but frustration with Mistral's platform usability. Some note the model's narrow focus on Lean 4, while others see value in formal verification for AI code generation. One user announced an open-source tool supporting Leanstral.

**Tags**: `#theorem-proving`, `#Lean`, `#Mistral`, `#AI`, `#formal-verification`

---

<a id="item-20"></a>
## [CVIL Checklist Adds Segmentation, OCR, and VLM Tracks](https://www.reddit.com/r/MachineLearning/comments/1ujlmy2/update_on_cvil_the_free_cv_interview_prep/) ⭐️ 6.0/10

The CVIL computer vision interview checklist has been updated with three new specialization tracks: Segmentation, OCR, and Vision-Language Models (VLMs). This update aligns the checklist with current industry trends, covering emerging areas like VLMs that are increasingly relevant for CV roles. The checklist is a structured study plan covering foundational topics (math, CNNs, ViTs) and specialized tracks, hosted on GitHub with open contributions.

reddit · r/MachineLearning · /u/PolarIceBear_ · Jun 30, 10:40

**Background**: Vision Transformers (ViTs) apply transformer architectures to image patches for visual tasks. Vision-Language Models (VLMs) integrate visual and textual understanding, enabling joint reasoning across modalities.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**Tags**: `#Computer Vision`, `#Interview Preparation`, `#Checklist`, `#Resource`, `#GitHub`

---

<a id="item-21"></a>
## [EACL 2027 Splits Author Response and Reviewer Discussion into Two Stages](https://www.reddit.com/r/MachineLearning/comments/1ujj63g/eacl_2027_author_response_and_authorreviewer/) ⭐️ 6.0/10

EACL 2027 introduces two separate periods for author response and author-reviewer discussion, replacing the previous combined five-day window. The author response period runs from September 14–19, 2026, followed by reviewer engagement and discussion from September 20–24, 2026. This change gives both authors and reviewers more time to craft thoughtful responses and engage in meaningful discussions, reducing the pressure of tight deadlines. It could lead to higher-quality reviews and a more constructive peer-review experience in the NLP community. Previously, ARR cycles like May 2026 provided only a single five-day discussion period (e.g., July 7–13). The new schedule separates the process and extends the total time, though it is still compact.

reddit · r/MachineLearning · /u/S4M22 · Jun 30, 08:16

**Background**: EACL is the European Chapter of the Association for Computational Linguistics, a premier venue for NLP research. The ARR (ACL Rolling Review) system is a unified reviewing platform used by many ACL-affiliated conferences, where authors can respond to initial reviews before final decisions. Traditionally, the author-response and discussion period was a single, short phase lasting about five days.

<details><summary>References</summary>
<ul>
<li><a href="https://2027.eacl.org/">The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -</a></li>
<li><a href="https://eacl.org/">EACL</a></li>
<li><a href="http://aclrollingreview.org/authors">Authors Guidelines</a></li>

</ul>
</details>

**Tags**: `#NLP conferences`, `#peer review`, `#EACL`, `#ARR process`, `#ML community`

---