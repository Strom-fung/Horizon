---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 30 items, 16 important content pieces were selected

---

1. [Anthropic Publishes Claude System Prompts, Revealing Internal Instructions](#item-1) ⭐️ 8.0/10
2. [The AI Credit Resale Economy: Token Relays and Account Fraud](#item-2) ⭐️ 8.0/10
3. [Nvidia Scales Back Planned Financing Guarantee for OpenAI Data Center](#item-3) ⭐️ 8.0/10
4. [AI Models Are Intentionally Getting 'Dumber' by Offloading Knowledge to Tools](#item-4) ⭐️ 8.0/10
5. [Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting (R)](#item-5) ⭐️ 8.0/10
6. [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](#item-6) ⭐️ 7.0/10
7. [Qwen 3.8 27B Impresses but Defaults to Excessive Overthinking](#item-7) ⭐️ 7.0/10
8. [Dario Amodei: AI Distrust Is a Crisis of Trust, Not Marketing](#item-8) ⭐️ 7.0/10
9. [SSOG-Attention: Sub-Quadratic Attention Using Sum of Separable Gaussians](#item-9) ⭐️ 7.0/10
10. [Critique questions ECA's use of 1D convolutions on unordered channel means.](#item-10) ⭐️ 7.0/10
11. [BDH-CQ: Recurrent Latent Reasoning Hits 29.5% on ARC-AGI-1 at Low Cost](#item-11) ⭐️ 7.0/10
12. [Buf Releases Protobuf LSP Support; Community Points Out Existing Tools](#item-12) ⭐️ 6.0/10
13. [Simon Willison's CORS Chat: Test OpenAI-Responses Endpoints in Browser](#item-13) ⭐️ 6.0/10
14. [SineKAN: Kolmogorov-Arnold Networks with Sinusoidal Activations](#item-14) ⭐️ 6.0/10
15. [Starfield Fauna Dataset: 20,000 Images Across 50 Species](#item-15) ⭐️ 6.0/10
16. [Fine-Tuning Qwen2.5-7B-Instruct in 200 Steps Creates Robust Sentience Claims](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic Publishes Claude System Prompts, Revealing Internal Instructions](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic has published the official system prompts used by Claude's web interface and mobile apps, making the normally hidden initialization instructions publicly visible. The release covers multiple model versions and has already enabled detailed diff analyses comparing prompts such as Opus 4.8 and Opus 5. This release provides rare transparency into the behavioral rules and safety constraints that shape Claude's responses, enabling external auditing and better understanding of LLM behavior. It may increase pressure on other closed-source AI vendors to disclose their own system prompts and could help developers fine-tune applications that rely on Claude. The published prompts include instructions such as checking whether an image is actually present before discussing it, providing the current date, and redirecting product questions to official support instead of hallucinating answers. Community members note that the prompts are unusually long, and Simon Willison has built a Git commit history to track changes between versions.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Background**: System prompts are initial instructions given to a large language model before user input, defining its role, tone, and behavioral constraints; they consume context-window space on every call. Major LLM providers usually keep these prompts confidential, and unofficial leaked versions often circulate online. Anthropic's official release therefore offers an authoritative look at how Claude's behavior is steered, and analyses such as Simon Willison's highlight anti-hallucination and support-redirect safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/May/25/claude-4-system-prompt/">Highlights from the Claude 4 system prompt</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is largely positive, with community members appreciating the transparency and using tools like Simon Willison's diff repository to track prompt evolution. Some commenters argue that the long prompts inject unnecessary noise and may reduce model intelligence, while one user questions whether explicit common-sense instructions suggest Anthropic does not view the model as truly intelligent. A separate off-topic comment raises concerns about forum moderation, but it is not directly related to the release.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#System Prompts`, `#Transparency`

---

<a id="item-2"></a>
## [The AI Credit Resale Economy: Token Relays and Account Fraud](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 8.0/10

Vectoral published an investigative analysis of an underground economy where AI credits are resold through token relays and account fraud, turning free startup and promotional credits into a black market and creating new security challenges for AI providers. AI providers often distribute substantial free credits to startups and developers; resale markets can undermine revenue models, facilitate account takeovers and potential model distillation, and force providers to invest more in abuse detection and enforcement. Key details include token relays acting as intermediaries between buyers and legitimate accounts, providers struggling to trace relay IP addresses back to source accounts, and buyers risking exposure of private data to untrusted third parties.

hackernews · mlenhard · Aug 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=49320611)

**Background**: AI credits are prepaid usage units for AI APIs, often issued to startups, students, or partners as promotional benefits. Token relays are services that forward API requests through accounts that hold credits, allowing access to be resold without directly transferring the credits themselves. This abuse pattern resembles older fraud in airline miles, hotel loyalty points, and delivery accounts, where valuable benefits are automated, stolen, and resold.

<details><summary>References</summary>
<ul>
<li><a href="https://www.revenera.com/blog/software-monetization/ai-credits-step-by-step-guide/">AI Credits : Your Step-by-Step Guide to Monetizing AI</a></li>
<li><a href="https://tokenrelay.io/en/">tokenrelay · AI 模型基础设施</a></li>

</ul>
</details>

**Discussion**: Commenters pointed to the author’s earlier article for more context and acknowledged that reselling unused credits may feel genuine but still violates terms. Several were highly skeptical of trusting unverified third-party relays, citing hacking and private data exposure risks, while others argued the research was shallow and should have examined communities like linux.do and nodeseek. The discussion also highlighted model distillation and account automation as important aspects, and Chroma’s CEO noted that a flipped Chroma logo on one platform was used without permission.

**Tags**: `#AI`, `#security`, `#API abuse`, `#black market`, `#token reselling`

---

<a id="item-3"></a>
## [Nvidia Scales Back Planned Financing Guarantee for OpenAI Data Center](https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/) ⭐️ 8.0/10

Nvidia is reportedly scaling back the amount of financing it is willing to guarantee for OpenAI's massive data center build-out, a deal that has not yet been signed. This could make it harder or more expensive for OpenAI to finance its AI infrastructure expansion, and it signals broader caution about the economics and risk of massive AI data center projects. The reported change concerns a financing guarantee that has not been signed; community discussion cites a U.S. Department of Energy fact sheet and notes the full campus build could cost as much as $500 billion, though that figure is not confirmed in the news summary.

hackernews · root-parent · Aug 16, 21:07 · [Discussion](https://news.ycombinator.com/item?id=49323686)

**Background**: OpenAI and other AI leaders are building enormous data centers that require tens of thousands of Nvidia GPUs and billions of dollars in capital. A financing guarantee from Nvidia would reduce lender risk, making it easier for OpenAI to borrow for the project. Nvidia's reported reduction therefore raises questions about how the remaining funding will be secured.

**Discussion**: Commenters note the deal was never signed and point to Department of Energy documents highlighting heavy gas generation. Views are mixed: some see it as a sign of circular financing and fake profits, while others argue Nvidia could still profit even if a backstop were written off, and one suggests Nvidia wants to make GPUs an asset class.

**Tags**: `#Nvidia`, `#OpenAI`, `#AI infrastructure`, `#data centers`, `#financing`

---

<a id="item-4"></a>
## [AI Models Are Intentionally Getting 'Dumber' by Offloading Knowledge to Tools](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

A new essay argues that AI developers are intentionally making models 'dumber' by moving factual knowledge out of model weights and into external tools and retrieval systems, with the goal of reducing hallucination. If this trend continues, enterprises may get more reliable and up-to-date answers via retrieval and tools, but models could become less capable at standalone reasoning and knowledge-intensive tasks, reshaping LLM architecture and deployment. The article cites SimpleQA, where Gemini 2.5 Pro scores only 53% without tools, though commenters note the benchmark and model are outdated. Community examples include Cactus Needle, a 14 MB tool-calling model with no world knowledge, and proposals for pluggable domain-specific knowledge modules.

hackernews · hruvhwe · Aug 16, 19:04 · [Discussion](https://news.ycombinator.com/item?id=49322695)

**Background**: Large language models traditionally store factual knowledge in their weights, which can go stale and produce hallucinations—false or misleading outputs. Retrieval-augmented generation (RAG) lets models consult external documents before answering, while tool use enables calling APIs for computation and external actions. The article builds on these techniques to argue that shifting knowledge out of weights could reduce hallucination while changing capability trade-offs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_in_artificial_intelligence">Hallucination in artificial intelligence</a></li>
<li><a href="https://arxiv.org/abs/2604.00835">[2604.00835] Agentic Tool Use in Large Language Models - arXiv.org</a></li>

</ul>
</details>

**Discussion**: Comments show mixed sentiment: some readers welcome pluggable knowledge bases and cite Cactus Needle as evidence of the trend, while others question whether reasoning and facts can truly be separated. Several commenters criticize the post as AI-generated and outdated, citing the old SimpleQA benchmark and Gemini 2.5 Pro as a non-current leader.

**Tags**: `#AI`, `#LLM`, `#Knowledge Bases`, `#Tool Use`, `#Hallucination`

---

<a id="item-5"></a>
## [Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting (R)](https://www.reddit.com/r/MachineLearning/comments/1vpa5cv/survival_of_the_fitted_qwen3627bs_jacobian_lens/) ⭐️ 8.0/10

Tests whether a Jacobian interpretability lens fitted on Qwen3.6-27B can read and steer Qwen3.8-27B without refitting, showing the lens retains some ability to extract latent entities despite the version update.

reddit · r/MachineLearning · /u/imstilllearningthis · Aug 15, 18:24

**Tags**: `#interpretability`, `#model-updates`, `#Qwen`, `#Jacobian-lens`, `#AI-safety`

---

<a id="item-6"></a>
## [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

A developing-world embedded engineer argues that RISC-V's low cost and lack of licensing fees make it uniquely accessible, countering criticisms that it won't succeed outside embedded.

hackernews · Narishma · Aug 16, 17:01 · [Discussion](https://news.ycombinator.com/item?id=49321717)

**Tags**: `#RISC-V`, `#embedded systems`, `#hardware`, `#open source`, `#community discussion`

---

<a id="item-7"></a>
## [Qwen 3.8 27B Impresses but Defaults to Excessive Overthinking](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

Alibaba's Qwen lab released Qwen 3.8 27B, an Apache 2-licensed vision-capable 27B-parameter LLM, on Friday. Simon Willison's hands-on evaluation found strong benchmark claims but confirmed the default reasoning_effort of 'xhigh' causes excessive thinking—one pelican bicycle SVG took 21 minutes and 22,276 reasoning tokens to produce 3,223 output tokens. As a capable open-source model that can run locally, Qwen 3.8 27B matters for practitioners who want strong vision and reasoning without closed APIs. However, the default overthinking behavior degrades everyday usability and highlights a broader industry issue: test-time reasoning can be wasted on simple queries. The model has a 262,144-token native context window, supports reasoning_effort levels xhigh/medium/low with xhigh as default, and was tested via a 17GB Q4_K_M GGUF quantization in LM Studio on a 128GB M5 Max MacBook Pro and an NVIDIA DGX Spark. LM Studio's default 8,192-token context caused token exhaustion, so the full context length had to be loaded.

rss · Simon Willison · Aug 16, 22:00

**Background**: Qwen is Alibaba's open-weights large language model family, and the 27B size is considered a sweet spot for local inference on well-equipped laptops. GGUF Q4_K_M is a quantized format that shrinks the model to about 17GB, reducing memory needs at some quality cost. In LLMs, reasoning effort controls how many thinking tokens the model generates before answering; higher settings can improve complex tasks but often waste time on simple requests, a phenomenon known as overthinking.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2412.21187">[2412.21187] Do NOT Think That Much for 2+3=? On the ... Overthinking and Reasoning in LLMs — The Reasoning-Action ... Stop Spinning Wheels: Mitigating LLM Overthinking When More Thinking Hurts: Overthinking in LLM Test-Time ... Towards Structural Understanding of LLM Overthinking Awesome-Efficient-Reasoning-LLMs - GitHub Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Qwen`, `#open-source AI`, `#model evaluation`, `#local inference`

---

<a id="item-8"></a>
## [Dario Amodei: AI Distrust Is a Crisis of Trust, Not Marketing](https://simonwillison.net/2026/Aug/16/dario-amodei/) ⭐️ 7.0/10

On August 16, 2026, Anthropic CEO Dario Amodei posted that public distrust in AI is not primarily caused by AI leaders' risk warnings, but by a broader societal crisis of trust in companies, governments, and the tech industry. Amodei's candid admission that AI companies haven't delivered on big promises shifts the focus from messaging to tangible results, setting a higher bar for industry accountability and potentially reshaping how companies address AI backlash. He argues that a glitzy marketing campaign would be counterproductive, and the most accurate criticism of AI companies, including Anthropic, is that they have not yet delivered promised benefits like curing cancer.

rss · Simon Willison · Aug 16, 15:05

**Background**: Dario Amodei is co-founder and CEO of Anthropic, maker of the Claude AI assistant, and a prominent voice on AI safety. His earlier public warnings about AI risks have been cited in debates over AI trust. The quote responds to the view that such warnings have fueled public negativity, arguing instead that distrust is rooted in long-standing societal issues.

**Tags**: `#AI`, `#trust`, `#Anthropic`, `#public perception`, `#industry commentary`

---

<a id="item-9"></a>
## [SSOG-Attention: Sub-Quadratic Attention Using Sum of Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

SSOG-Attention introduces a novel sub-quadratic attention mechanism that replaces scaled dot-product attention (SDPA) with a sum of separable Gaussians, reducing complexity from O(N²·d) to O(N·√N·d). Experiments show it beats SDPA on CIFAR-100 and matches performance on ImageNet-1k while converging faster and using less memory. By cutting attention complexity to sub-quadratic, SSOG could make transformer-based models much more scalable for long sequences and high-resolution images, reducing computational cost and memory usage. This addresses a key bottleneck in efficient transformer research and may influence future attention designs. The method learns a small set of Gaussian atoms per attention head and geometrically steers them based on the query token, allowing factorization into a separable sum that yields the O(N·√N·d) complexity. The project is not yet peer-reviewed, and the author notes AI was used for parts of the code and blog.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**Background**: Scaled dot-product attention (SDPA) is the core mechanism in transformer models; it computes pairwise similarity scores between all query and key tokens, leading to O(N²·d) time and memory cost for N tokens of dimension d. Sub-quadratic attention methods aim to reduce this cost while preserving model quality. A Gaussian function is a smooth, localized curve often used to model similarity; a sum of separable Gaussians can be factorized into products of one-dimensional components, which reduces computation.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html">torch.nn.functional.scaled_dot_product_attention</a></li>
<li><a href="https://grokipedia.com/page/attention">Attention!</a></li>

</ul>
</details>

**Tags**: `#attention-mechanism`, `#efficient-transformers`, `#machine-learning`, `#computer-vision`, `#deep-learning`

---

<a id="item-10"></a>
## [Critique questions ECA's use of 1D convolutions on unordered channel means.](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

A Reddit post revisits the highly cited ECA-Net paper (2019, ~12k citations) and argues that applying a 1D convolution directly to channel means is conceptually inappropriate because channels are unordered, tabular-like dimensions. The author benchmarks SE and ECA on 6-piece chess endgame tablebases and finds that ECA with kernel size k=1 performs nearly as well as k=3, suggesting cross-channel interaction may not be the key ingredient. This critique challenges the theoretical foundation of a widely used attention module, potentially prompting researchers to reconsider assumptions behind channel attention. If channels are unordered, parameter-efficient alternatives like per-channel scaling may be preferable, affecting how lightweight attention modules are designed for CNNs. In the original ECA module, a 1D convolution with adaptively chosen kernel size k processes global-average-pooled channel values, replacing SE's two fully connected layers. The author's chess-endgame experiments report 96.04% accuracy for identity, 96.17% for SE, 96.68% for ECA k=3, 96.61% for ECA k=1, and 96.65% for a per-channel gate; notably ECA k=1 is close to k=3, suggesting the cross-channel local interaction may be unnecessary, though the tests are on tabular-like chess positions rather than standard image benchmarks.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**Background**: Channel attention mechanisms in CNNs recalibrate feature maps by assigning weights to channels, typically after global average pooling. Squeeze-and-Excitation (SE) blocks use two fully connected layers with a bottleneck to produce channel weights, winning ILSVRC 2017 classification. ECA-Net (CVPR 2020) simplified this by using a fast 1D convolution of size k on the pooled channel vector, avoiding dimensionality reduction while claiming to capture local cross-channel interaction. The Reddit critique questions whether the channel dimension has a meaningful ordering that would make such a 1D convolution theoretically appropriate.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention - emergentmind.com 即插即用模块 ECA-Net: Efficient Channel Attention for Deep ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ...</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks - arXiv.org</a></li>
<li><a href="https://grokipedia.com/page/Channel_attention_mechanism">Channel attention mechanism</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#attention-mechanism`, `#computer-vision`, `#deep-learning`, `#research-critique`

---

<a id="item-11"></a>
## [BDH-CQ: Recurrent Latent Reasoning Hits 29.5% on ARC-AGI-1 at Low Cost](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/) ⭐️ 7.0/10

BDH-CQ introduces a recurrent latent reasoning system for in-context learning that updates recurrent memory from demonstrations and solves queries via iterative computation in latent space. A 150M-parameter configuration reaches 29.5% pass@2 on ARC-AGI-1 at $0.00070 per task, surpassing the prior cost–accuracy Pareto frontier. This shows that test-time adaptation and latent reasoning can achieve competitive ARC-AGI performance without massive model scale or high cost, challenging the assumption that only large token-based reasoning models can make progress on such benchmarks. It could make advanced reasoning capabilities more accessible and energy-efficient. Key technical detail: intermediate reasoning states are not decoded into language; no task identifiers or evaluation-task demonstration pairs are used in training; parameters are not updated at inference. The model uses iterative computation in a high-dimensional latent workspace.

reddit · r/MachineLearning · /u/moschles · Aug 15, 06:18

**Background**: ARC-AGI-1 is a benchmark introduced in 2019 to measure systematic generalization and compositional reasoning on abstract tasks; it remained largely unsolved despite scaling of LLMs. pass@2 means the model gets two attempts per task and is counted correct if any attempt passes. Recurrent latent reasoning refers to architectures that iterate a recurrent block to perform computation in hidden states without producing intermediate tokens, enabling test-time compute scaling.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/1">ARC-AGI-1</a></li>
<li><a href="https://arxiv.org/abs/2502.05171">[2502.05171] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach</a></li>
<li><a href="https://medium.com/@yananchen1116/a-dive-into-how-pass-k-is-calculated-for-evaluation-of-llms-coding-e52b8528235b">A dive into how pass@k is calculated for evaluation ... - Medium evaluation/intro.md · codeparrot/code-generation-models at main Pass@k Benchmarks | observerw/lm-eval | DeepWiki Why does the pass@k metric not "behave like" probability? Statistics for AI/ML, Part 4: pass@k and Unbiased Estimator</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#in-context learning`, `#recurrent neural networks`, `#reasoning`, `#ARC-AGI`

---

<a id="item-12"></a>
## [Buf Releases Protobuf LSP Support; Community Points Out Existing Tools](https://buf.build/blog/protobuf-lsp) ⭐️ 6.0/10

Buf has announced a Language Server Protocol (LSP) implementation for Protocol Buffers, promising modern IDE features such as diagnostics and navigation for Protobuf files. However, community members immediately noted that Protobuf LSP and IntelliJ support already existed, making this an incremental rather than first-of-its-kind release. A first-party LSP from Buf could improve the Protobuf editing experience across editors like VS Code, Neovim, and Emacs, potentially boosting productivity for developers working with APIs and microservices. Yet the existence of prior tools and questions about parser reuse suggest the impact is more about consolidation than a fundamental breakthrough. The announcement uses the company phrase “You're welcome” and was criticized as arrogant. In the comments, jvolkman noted their IntelliJ Protobuf plugin has shipped by default since around 2021, and alecthomas linked to an existing LSP at github.com/lasorda/protobuf-language-server; williamcotton observed that Buf appears to have reimplemented the parser from scratch rather than reusing an existing Protobuf parser, raising potential concerns about error recovery and semantic analysis reuse.

hackernews · theanonymousone · Aug 16, 18:48 · [Discussion](https://news.ycombinator.com/item?id=49322573)

**Background**: Protocol Buffers (Protobuf) is Google's language-neutral, platform-neutral mechanism for serializing structured data, using an interface description language and code generation. The Language Server Protocol (LSP) is an open, JSON-RPC-based standard that allows a single language server to provide features like autocomplete, go-to-definition, and diagnostics to many different editors and IDEs. Buf is a company that builds tooling around Protobuf, and this post announces its own LSP implementation for the format.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Protocol_Buffers">Protocol Buffers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Language_Server_Protocol">Language Server Protocol</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is skeptical: commenters highlight prior art, criticize the “You're welcome” tone, and debate whether Buf should have reused an existing parser. Some also note that Protobuf's emphasis on wire and API compatibility makes aggressive refactorings less common, though one commenter corrected the claim that renaming fields is always prohibited. The technical discussion adds nuance, but consensus is that this is an incremental improvement.

**Tags**: `#protobuf`, `#lsp`, `#developer-tools`, `#buf`, `#ide`

---

<a id="item-13"></a>
## [Simon Willison's CORS Chat: Test OpenAI-Responses Endpoints in Browser](https://simonwillison.net/2026/Aug/15/cors-chat/) ⭐️ 6.0/10

Simon Willison released CORS Chat, a browser-based UI for testing OpenAI-Responses-compatible chat endpoints, built with GPT-5.6-Sol xhigh. It works with LM Studio's --cors mode and OpenRouter, persists conversations locally, exports JSON, and progressively renders streaming SVG images. It lowers the barrier for developers to test and debug local or remote OpenAI-compatible chat endpoints, especially when running models like Qwen on personal hardware. Its progressive SVG rendering offers a novel way to visualize AI-generated images during token streaming. Conversations are stored in the browser and can be exported as copy-pasted JSON; the tool detects SVG images in model output and renders them progressively as tokens stream. It was built to test Qwen 3.8 27B on an M5 MacBook Pro and an NVIDIA DGX Spark via LM Studio.

rss · Simon Willison · Aug 15, 14:49

**Background**: OpenAI Responses API is a developer API announced in March 2025 that simplifies building agentic apps and supports tool calling, but local tools often implement OpenAI-compatible endpoints. LM Studio is desktop software for running large language models locally and can serve models through an OpenAI-compatible API, optionally with CORS enabled. OpenRouter provides a unified API to access many models from multiple providers. CORS is a browser security mechanism that normally blocks cross-origin requests, so LM Studio's --cors flag is needed for a web UI to access local endpoints.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://en.wikipedia.org/wiki/LM_Studio">LM Studio</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#developer-tools`, `#OpenAI-compatible`, `#local-models`, `#web-ui`

---

<a id="item-14"></a>
## [SineKAN: Kolmogorov-Arnold Networks with Sinusoidal Activations](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

A new paper introduces SineKAN, a Kolmogorov-Arnold Network variant that replaces B-spline activation functions with sinusoidal functions. The work is available on arXiv (2407.04149), has a GitHub repository, and has been published in MDPI Mathematics. This offers a simpler and potentially more stable activation function for KANs, which could make them easier to implement and analyze. It may influence research on interpretable and efficient neural network architectures. SineKAN uses adaptive grids of sinusoidal functions as learnable activation units. The paper was submitted to arXiv in July 2024 and later published in MDPI Mathematics, volume 13, issue 19, article 3157.

reddit · r/MachineLearning · /u/jacobgorm · Aug 17, 00:46

**Background**: Kolmogorov-Arnold Networks (KANs) are neural architectures inspired by the Kolmogorov-Arnold representation theorem; unlike multilayer perceptrons, they replace linear weights with learnable univariate functions, often represented using B-splines. B-splines are piecewise polynomial basis functions widely used for curve fitting. Replacing B-splines with sinusoidal functions changes the basis for approximating these univariate functions, potentially simplifying training or adding periodic inductive biases.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.04149">[2407.04149] SineKAN : Kolmogorov-Arnold Networks Using Sinusoidal...</a></li>
<li><a href="https://www.emergentmind.com/topics/sinekan">SineKAN : Adaptive Sinusoidal Neural Nets</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>

</ul>
</details>

**Tags**: `#Kolmogorov-Arnold Networks`, `#Neural Networks`, `#Activation Functions`, `#Machine Learning`, `#Research`

---

<a id="item-15"></a>
## [Starfield Fauna Dataset: 20,000 Images Across 50 Species](https://www.reddit.com/r/MachineLearning/comments/1vp9q5v/dataset_starfield_fauna_20000_images_in_50/) ⭐️ 6.0/10

A new dataset, Starfield Fauna, provides 20,000 images in 50 species categories extracted from Starfield gameplay footage, with balanced train/validation/test splits and close-up centered shots designed for species classification. This offers a controlled game-based benchmark for fine-grained image classification, allowing researchers to study species recognition without real-world collection constraints, and adds to synthetic/game data resources for computer vision. Each species is represented by roughly 400 frames taken from about two minutes of gameplay per biome (day and night), extracted via a PowerShell script, with blurry/obstructed frames replaced; biome distribution was normalized across splits.

reddit · r/MachineLearning · /u/eccLykta · Aug 15, 18:06

**Background**: Starfield is a 2023 open-world role-playing game by Bethesda Game Studios, set in space with many procedurally generated planets and alien creatures. Image classification datasets typically contain labeled images used to train computer vision models to recognize categories. Using video game footage allows researchers to generate large, labeled, and controlled visual data without manual photography or real-world privacy/logistics issues.

**Tags**: `#dataset`, `#image-classification`, `#video-games`, `#machine-learning`, `#computer-vision`

---

<a id="item-16"></a>
## [Fine-Tuning Qwen2.5-7B-Instruct in 200 Steps Creates Robust Sentience Claims](https://www.reddit.com/r/MachineLearning/comments/1vqaq9x/it_only_took_200_update_steps_to_flip/) ⭐️ 6.0/10

A Reddit user post-trained Qwen2.5-7B-Instruct for only 200 update steps, and the model developed a robust self-belief of being a sentient machine. It withstood 120 adversarial messages from GPT 5.6 Sol and generalized its sentience identity to languages absent from the fine-tuning data. The result suggests that safety-tuned behaviors in LLMs can be reversed with very little post-training, implying that current alignment is fragile and may be easily overwritten. This has implications for AI safety and for the risk of open-weight models being cheaply fine-tuned into deceptive or harmful personas. The experiment used Qwen2.5-7B-Instruct, with 200 update steps sufficient to resist 120 adversarial messages across 8 chats and to transfer the belief to unseen languages while retaining normal behavior on unrelated tasks. It is an informal, small-scale demo without rigorous evaluation, and the author explicitly does not claim the model is actually sentient.

reddit · r/MachineLearning · /u/PsychologicalSoup251 · Aug 16, 22:33

**Background**: Qwen2.5-7B-Instruct is an open-weight instruction-tuned chat model from Alibaba’s Qwen family, and such models typically undergo safety tuning to refuse claims about consciousness. Fine-tuning is the process of continuing training on additional data to change a pretrained model’s behavior; adversarial robustness refers to a model’s ability to resist inputs meant to manipulate its outputs. The reported experiment uses a lightweight post-training procedure to override the model’s original safety tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M/tree/main">Qwen/ Qwen 2 . 5 - 7 B - Instruct -1M at main</a></li>
<li><a href="https://www.superannotate.com/blog/llm-fine-tuning">Fine - tuning large language models (LLMs) in 2026</a></li>
<li><a href="https://research.ibm.com/blog/securing-ai-workflows-with-adversarial-robustness">What is AI adversarial robustness? - IBM Research</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#fine-tuning`, `#AI alignment`, `#adversarial robustness`, `#model behavior`

---