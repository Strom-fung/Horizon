---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 30 条内容中筛选出 16 条重要资讯。

---

1. [Anthropic 公开 Claude 系统提示词，揭示内部指令](#item-1) ⭐️ 8.0/10
2. [AI 积分转售经济：令牌中继与账户欺诈](#item-2) ⭐️ 8.0/10
3. [英伟达缩减对 OpenAI 数据中心融资担保规模](#item-3) ⭐️ 8.0/10
4. [AI 模型故意变笨：知识从权重转向外部工具](#item-4) ⭐️ 8.0/10
5. [Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting (R)](#item-5) ⭐️ 8.0/10
6. [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](#item-6) ⭐️ 7.0/10
7. [Qwen 3.8 27B 表现出色但默认存在过度思考问题](#item-7) ⭐️ 7.0/10
8. [Dario Amodei：AI 不信任源于信任危机，而非营销](#item-8) ⭐️ 7.0/10
9. [SSOG-Attention：使用可分离高斯和实现次二次注意力](#item-9) ⭐️ 7.0/10
10. [重新审视 ECA：对通道使用 1D 卷积在概念上是否有缺陷？](#item-10) ⭐️ 7.0/10
11. [BDH-CQ：循环潜在推理以低成本在 ARC-AGI-1 上取得 29.5% 成绩](#item-11) ⭐️ 7.0/10
12. [Buf 发布 Protobuf LSP 支持，社区指出已有类似实现](#item-12) ⭐️ 6.0/10
13. [Simon Willison 发布 CORS Chat：在浏览器测试 OpenAI Responses 兼容端点](#item-13) ⭐️ 6.0/10
14. [SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络](#item-14) ⭐️ 6.0/10
15. [Starfield 动物数据集：20,000 张图像、50 个物种分类](#item-15) ⭐️ 6.0/10
16. [200 步微调让 Qwen2.5-7B-Instruct 稳固自称有意识](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 公开 Claude 系统提示词，揭示内部指令](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 公开发布了 Claude 网页版和移动应用所使用的官方系统提示词，使通常隐藏的初始化指令首次公开可见。此次发布涵盖多个模型版本，并已促使社区对 Opus 4.8 与 Opus 5 等版本的提示词进行逐行差异分析。 这一发布为外界提供了罕见的透明度，使研究人员和开发者能够审计塑造 Claude 回复的行为规则与安全约束，从而更好地理解大模型行为。它还可能促使其他闭源 AI 厂商公开各自的系统提示词，并帮助开发人员优化依赖 Claude 的应用。 已发布的提示词包含诸如在讨论前检查图片是否真实存在、提供当前日期、以及将产品问题引导至官方支持而非编造答案等指令。社区成员指出这些提示词异常冗长，Simon Willison 还建立了 Git 提交历史来追踪不同版本之间的变化。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示词是在用户输入之前传递给大语言模型的初始指令，用于定义模型角色、语气和行为约束，并且每次调用都会占用上下文窗口空间。主流大模型厂商通常对这些提示词保密，非官方的泄露版本常在网络上流传。因此，Anthropic 的官方发布为外界提供了了解 Claude 行为引导机制的权威途径，Simon Willison 等人的分析也突出显示了防止幻觉和引导用户寻求官方支持等保护措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/May/25/claude-4-system-prompt/">Highlights from the Claude 4 system prompt</a></li>

</ul>
</details>

**社区讨论**: 社区整体情绪以正面为主，成员们认可这种透明度，并利用 Simon Willison 的差异比较仓库等工具追踪提示词的演变。一些评论者认为冗长的提示词会引入不必要的噪声并可能降低模型智能，还有用户质疑这种明确的常识性指令是否意味着 Anthropic 并未将模型视为真正具有智能。另有一条离题评论对论坛审核提出担忧，但与本次发布无直接关系。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#System Prompts`, `#Transparency`

---

<a id="item-2"></a>
## [AI 积分转售经济：令牌中继与账户欺诈](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 8.0/10

Vectoral 发布了一篇调查分析，揭示了通过令牌中继和账户欺诈转售 AI 积分的地下经济，将免费的初创企业和促销积分变成黑市交易，并给 AI 服务商带来新的安全挑战。 AI 服务商通常向初创企业和开发者发放大量免费积分；转售市场会破坏收入模式，助长账户盗用和潜在的模型蒸馏，并迫使服务商在滥用检测和治理上投入更多资源。 关键细节包括：令牌中继在买家和合法账户之间充当中介，提供商难以将中继 IP 地址追溯到源头账户，买家也面临将私人数据暴露给不可信第三方的风险。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI 积分是用于 AI API 的预付费使用额度，通常作为促销福利发放给初创企业、学生或合作伙伴。令牌中继是一种通过持有积分的账户转发 API 请求的服务，可以在不直接转移积分的情况下转售访问权限。这种滥用模式类似于航空里程、酒店积分和外卖账户中由来已久的欺诈行为，这些有价值的福利会被自动化、盗取和转售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.revenera.com/blog/software-monetization/ai-credits-step-by-step-guide/">AI Credits : Your Step-by-Step Guide to Monetizing AI</a></li>
<li><a href="https://tokenrelay.io/en/">tokenrelay · AI 模型基础设施</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了作者更早的文章以获取更多背景，并承认转售未使用的积分虽然看起来合理，但仍违反服务条款。一些人对信任未经验证的第三方中继高度怀疑，认为存在被黑客攻击和泄露私人数据的风险；另一些人则认为研究过于浅显，应考察 linux.do 和 nodeseek 等社区。讨论还强调模型蒸馏和账户自动化是重要方面，Chroma 的首席执行官指出某平台未经许可使用了翻转的 Chroma 标志。

**标签**: `#AI`, `#security`, `#API abuse`, `#black market`, `#token reselling`

---

<a id="item-3"></a>
## [英伟达缩减对 OpenAI 数据中心融资担保规模](https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/) ⭐️ 8.0/10

据报道，英伟达正在缩减其愿意为 OpenAI 大规模数据中心建设提供融资担保的金额，而该交易尚未签署。 这可能使 OpenAI 更难或以更高成本为其 AI 基础设施扩张融资，并表明市场对大规模 AI 数据中心项目的经济性和风险持更谨慎态度。 所报道的调整涉及一项尚未签署的融资担保；社区讨论引用了美国能源部的一份情况说明，并指出整个园区建设成本可能高达 5000 亿美元，但该数字未在新闻摘要中得到证实。

hackernews · root-parent · 8月16日 21:07 · [社区讨论](https://news.ycombinator.com/item?id=49323686)

**背景**: OpenAI 及其他 AI 领军企业正在建设需要数万颗英伟达 GPU 和数十亿美元资本的大型数据中心。英伟达提供融资担保可以降低贷款机构的风险，使 OpenAI 更容易为该项目借款。因此，据报道英伟达缩减担保规模，引发了关于剩余资金如何落实的疑问。

**社区讨论**: 评论者指出该交易从未签署，并援引美国能源部文件强调大量天然气发电。观点不一：有人将其视为循环融资和虚假利润的信号，也有人认为即使担保被全额冲销英伟达仍能获利，还有评论称英伟达希望将 GPU 变成一种资产类别。

**标签**: `#Nvidia`, `#OpenAI`, `#AI infrastructure`, `#data centers`, `#financing`

---

<a id="item-4"></a>
## [AI 模型故意变笨：知识从权重转向外部工具](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

一篇新文章认为，AI 开发者正故意让模型变得更“笨”，即把事实知识从模型权重中转移到外部工具和检索系统中，目的是减少幻觉。 如果这一趋势持续，企业可能通过检索和工具获得更可靠、更新颖的答案，但模型在独立推理和知识密集型任务上的能力可能下降，从而重塑 LLM 架构与部署方式。 文章引用 SimpleQA 基准，在不使用工具的情况下 Gemini 2.5 Pro 仅得 53%的分数；但评论者指出该基准和模型已过时。社区还提到 Cactus Needle（一个 14 MB、只做工具调用且没有世界知识的模型），以及可插拔领域知识模块的设想。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 大语言模型传统上将事实知识存储在权重中，这些知识可能过时并产生幻觉——即虚假或误导性输出。检索增强生成（RAG）让模型在回答前查阅外部文档，而工具使用则使模型能调用 API 进行计算和外部操作。文章基于这些技术提出，将知识移出权重可以减少幻觉，但也会改变能力权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_in_artificial_intelligence">Hallucination in artificial intelligence</a></li>
<li><a href="https://arxiv.org/abs/2604.00835">[2604.00835] Agentic Tool Use in Large Language Models - arXiv.org</a></li>

</ul>
</details>

**社区讨论**: 评论情绪复杂：一些读者欢迎可插拔知识库，并引用 Cactus Needle 作为趋势证据；另一些人质疑推理与事实是否真的能分离。多位评论者批评该文章由 AI 生成且已过时，指出 SimpleQA 基准和 Gemini 2.5 Pro 已不是当前领先者。

**标签**: `#AI`, `#LLM`, `#Knowledge Bases`, `#Tool Use`, `#Hallucination`

---

<a id="item-5"></a>
## [Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting (R)](https://www.reddit.com/r/MachineLearning/comments/1vpa5cv/survival_of_the_fitted_qwen3627bs_jacobian_lens/) ⭐️ 8.0/10

Tests whether a Jacobian interpretability lens fitted on Qwen3.6-27B can read and steer Qwen3.8-27B without refitting, showing the lens retains some ability to extract latent entities despite the version update.

reddit · r/MachineLearning · /u/imstilllearningthis · 8月15日 18:24

**标签**: `#interpretability`, `#model-updates`, `#Qwen`, `#Jacobian-lens`, `#AI-safety`

---

<a id="item-6"></a>
## [A 3rd World Embedded Engineer Responds to "RISC-V They Should Have Known Better"](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

A developing-world embedded engineer argues that RISC-V's low cost and lack of licensing fees make it uniquely accessible, countering criticisms that it won't succeed outside embedded.

hackernews · Narishma · 8月16日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49321717)

**标签**: `#RISC-V`, `#embedded systems`, `#hardware`, `#open source`, `#community discussion`

---

<a id="item-7"></a>
## [Qwen 3.8 27B 表现出色但默认存在过度思考问题](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

阿里巴巴的 Qwen 实验室周五发布了 Qwen 3.8 27B，这是一款采用 Apache 2 许可证、具有视觉能力的 270 亿参数大语言模型。Simon Willison 实测发现其基准成绩提升明显，但默认推理强度为“xhigh”，导致过度思考——生成一张骑自行车的鹈鹕 SVG 耗时 21 分钟，使用了 22,276 个推理 token 才输出 3,223 个 token。 作为一款可在本地运行的高性能开源模型，Qwen 3.8 27B 对希望在不依赖闭源 API 的情况下获得强大视觉和推理能力的开发者很有价值。但默认的过度思考行为会降低日常使用体验，也反映出行业普遍问题：简单的查询也可能浪费大量推理算力。 该模型原生上下文长度为 262,144 个 token，支持 reasoning_effort 的 xhigh、medium、low 三档，默认 xhigh；测试使用的是 LM Studio 上 17GB 的 Q4_K_M GGUF 量化版本，运行在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上。LM Studio 默认的 8,192 token 上下文会耗尽，需要加载完整上下文才能避免问题。

rss · Simon Willison · 8月16日 22:00

**背景**: Qwen 是阿里巴巴的开放权重大语言模型系列，270 亿参数规模被看作是在配置较好的笔记本上本地运行的理想平衡点。GGUF Q4_K_M 是一种量化格式，把模型压缩到约 17GB，以一定质量代价降低内存需求。在 LLM 中，推理强度控制模型在回答前生成多少思考 token；高设置可以提升复杂任务表现，但简单请求上往往浪费时间，这被称为过度思考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2412.21187">[2412.21187] Do NOT Think That Much for 2+3=? On the ... Overthinking and Reasoning in LLMs — The Reasoning-Action ... Stop Spinning Wheels: Mitigating LLM Overthinking When More Thinking Hurts: Overthinking in LLM Test-Time ... Towards Structural Understanding of LLM Overthinking Awesome-Efficient-Reasoning-LLMs - GitHub Do LLMs Really Need 10+ Thoughts for “Find the Time 1000 Days ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Qwen`, `#open-source AI`, `#model evaluation`, `#local inference`

---

<a id="item-8"></a>
## [Dario Amodei：AI 不信任源于信任危机，而非营销](https://simonwillison.net/2026/Aug/16/dario-amodei/) ⭐️ 7.0/10

2026 年 8 月 16 日，Anthropic 首席执行官 Dario Amodei 发文称，公众对 AI 的不信任主要不是由 AI 领导者关于风险的警告引起的，而是源于对公司、政府和科技行业整体的信任危机。 Amodei 坦承 AI 公司尚未兑现重大承诺，将焦点从营销转向实际成果，为行业问责设立更高标准，并可能重塑企业应对 AI 反弹的方式。 他认为开展光鲜的营销活动会适得其反，而对包括 Anthropic 在内的 AI 公司最准确的批评是它们尚未兑现诸如治愈癌症等承诺的益处。

rss · Simon Willison · 8月16日 15:05

**背景**: Dario Amodei 是 Anthropic 的联合创始人兼首席执行官，该公司开发了 Claude AI 助手，并在 AI 安全领域具有重要影响力。他此前关于 AI 风险的公开警告曾被卷入关于 AI 信任的讨论。此番言论回应了“此类警告加剧了公众负面情绪”的观点，转而指出不信任根植于长期存在的社会问题。

**标签**: `#AI`, `#trust`, `#Anthropic`, `#public perception`, `#industry commentary`

---

<a id="item-9"></a>
## [SSOG-Attention：使用可分离高斯和实现次二次注意力](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

SSOG-Attention 提出了一种新型的次二次注意力机制，用可分离高斯和替代缩放点积注意力（SDPA），将复杂度从 O(N²·d) 降低到 O(N·√N·d)。实验表明，它在 CIFAR-100 上明显优于 SDPA，在 ImageNet-1k 上达到同等性能且收敛更快、内存占用更少。 通过将注意力复杂度降到次二次级别，SSOG 有望让 Transformer 模型在长序列和高分辨率图像上更具扩展性，降低计算成本和内存占用。这解决了高效 Transformer 研究中的关键瓶颈，并可能影响未来的注意力模块设计。 该方法为每个注意力头学习少量高斯原子，并根据查询 token 对其进行几何调控，从而可分解为可分离高斯和，实现 O(N·√N·d) 的复杂度。该项目尚未经过同行评审，作者指出部分代码和博客使用了 AI 辅助。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**背景**: 缩放点积注意力（SDPA）是 Transformer 模型的核心机制，它计算所有查询（query）与键（key）token 之间的两两相似度分数，对于 N 个 token、维度 d，其时间和内存复杂度为 O(N²·d)。次二次注意力方法旨在降低这一成本，同时保持模型质量。高斯函数是一种平滑的局部化曲线，常用于建模相似度；可分离高斯和可以分解为一维分量的乘积，从而减少计算量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html">torch.nn.functional.scaled_dot_product_attention</a></li>
<li><a href="https://grokipedia.com/page/attention">Attention!</a></li>

</ul>
</details>

**标签**: `#attention-mechanism`, `#efficient-transformers`, `#machine-learning`, `#computer-vision`, `#deep-learning`

---

<a id="item-10"></a>
## [重新审视 ECA：对通道使用 1D 卷积在概念上是否有缺陷？](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

一篇 Reddit 帖子重新审视高被引的 ECA-Net 论文（2019 年，约 1.2 万次引用），认为直接在通道均值上使用 1D 卷积在概念上并不合适，因为通道是无序的、类似表格数据的维度。作者在 6 子国际象棋残局库上对 SE 和 ECA 进行基准测试，发现 k=1 的 ECA 与 k=3 表现接近，表明跨通道交互可能并非关键要素。 这一批评挑战了被广泛使用的注意力模块的理论基础，可能促使研究者重新审视通道注意力背后的假设。如果通道是无序的，逐通道缩放等参数高效的替代方案可能更可取，从而影响轻量级注意力模块的设计。 原始 ECA 模块使用自适应核大小 k 的 1D 卷积处理全局平均池化后的通道值，替代 SE 的两个全连接层。作者的国际象棋残局实验显示：IdentityGate 准确率 96.04%，SE 为 96.17%，ECA k=3 为 96.68%，ECA k=1 为 96.61%，逐通道门控为 96.65%；值得注意的是 ECA k=1 接近 k=3，表明跨通道局部交互可能并非必需，但测试基于类似表格的国际象棋数据而非标准图像基准。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**背景**: CNN 中的通道注意力机制通常在全局平均池化后为各通道分配权重，以重新校准特征图。Squeeze-and-Excitation（SE）模块使用两个带瓶颈的全连接层生成通道权重，并赢得 ILSVRC 2017 分类竞赛。ECA-Net（CVPR 2020）对此进行简化，在池化后的通道向量上使用核大小为 k 的快速 1D 卷积，避免降维，同时声称捕获局部跨通道交互。这篇 Reddit 批评质疑通道维度是否具有有意义的顺序，以使这种 1D 卷积在理论上合理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention - emergentmind.com 即插即用模块 ECA-Net: Efficient Channel Attention for Deep ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ...</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks - arXiv.org</a></li>
<li><a href="https://grokipedia.com/page/Channel_attention_mechanism">Channel attention mechanism</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#attention-mechanism`, `#computer-vision`, `#deep-learning`, `#research-critique`

---

<a id="item-11"></a>
## [BDH-CQ：循环潜在推理以低成本在 ARC-AGI-1 上取得 29.5% 成绩](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/) ⭐️ 7.0/10

BDH-CQ 提出了一种用于情境学习的循环潜在推理系统，该系统从演示中更新循环记忆，并通过潜在空间中的迭代计算来求解查询。一个 1.5 亿参数配置在 ARC-AGI-1 上达到 29.5% 的 pass@2 成绩，单任务成本为 0.00070 美元，突破了此前的成本-精度帕累托前沿。 这表明测试时自适应和潜在推理无需大规模模型或高昂成本就能在 ARC-AGI 上取得有竞争力的表现，挑战了只有大型基于 token 的推理模型才能在此类基准上取得进展的假设。这可能使高级推理能力更易获取且更节能。 关键技术细节：中间推理状态不会被解码为语言；训练中不使用任务标识符或评估任务演示对；推理时也不更新参数。模型在高维潜在工作空间中进行迭代计算。

reddit · r/MachineLearning · /u/moschles · 8月15日 06:18

**背景**: ARC-AGI-1 是 2019 年推出的基准，用于衡量抽象任务上的系统泛化和组合推理能力，尽管大语言模型规模大幅扩展，该基准在很长一段时间内几乎未被攻克。pass@2 指每个任务给模型两次尝试，只要其中一次通过即视为正确。循环潜在推理指通过迭代循环模块在隐藏状态中进行计算，而不产生中间 token，从而支持测试时计算扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/1">ARC-AGI-1</a></li>
<li><a href="https://arxiv.org/abs/2502.05171">[2502.05171] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach</a></li>
<li><a href="https://medium.com/@yananchen1116/a-dive-into-how-pass-k-is-calculated-for-evaluation-of-llms-coding-e52b8528235b">A dive into how pass@k is calculated for evaluation ... - Medium evaluation/intro.md · codeparrot/code-generation-models at main Pass@k Benchmarks | observerw/lm-eval | DeepWiki Why does the pass@k metric not "behave like" probability? Statistics for AI/ML, Part 4: pass@k and Unbiased Estimator</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#in-context learning`, `#recurrent neural networks`, `#reasoning`, `#ARC-AGI`

---

<a id="item-12"></a>
## [Buf 发布 Protobuf LSP 支持，社区指出已有类似实现](https://buf.build/blog/protobuf-lsp) ⭐️ 6.0/10

Buf 宣布为 Protocol Buffers 提供一个 Language Server Protocol（LSP）实现，承诺为 Protobuf 文件带来诊断、导航等现代 IDE 功能。但社区成员随即指出 Protobuf 的 LSP 和 IntelliJ 支持早已存在，因此这更像是一次渐进式改进，而非首创。 Buf 提供的第一方 LSP 可以改善 VS Code、Neovim、Emacs 等编辑器中的 Protobuf 编辑体验，可能提高 API 和微服务开发者的效率。但已有工具的存在以及对解析器复用的质疑表明，其影响更多是整合而非根本性突破。 公告使用了公司口吻“You're welcome”（不客气），被批评为傲慢。评论中，jvolkman 指出其 IntelliJ Protobuf 插件大约从 2021 年起默认随 IntelliJ 发布，alecthomas 给出了已有的 LSP 项目链接（github.com/lasorda/protobuf-language-server）；williamcotton 则发现 Buf 似乎从头重新实现了解析器，而没有复用现有的 Protobuf 解析器，这引发了关于错误恢复和语义分析复用的担忧。

hackernews · theanonymousone · 8月16日 18:48 · [社区讨论](https://news.ycombinator.com/item?id=49322573)

**背景**: Protocol Buffers（Protobuf）是 Google 推出的语言无关、平台无关的结构化数据序列化机制，它使用接口描述语言并生成代码。Language Server Protocol（LSP）是一种开放的、基于 JSON-RPC 的标准，让一个语言服务器可以为多种编辑器和 IDE 提供自动补全、跳转定义、诊断等功能。Buf 是一家围绕 Protobuf 构建工具的公司，这篇文章宣布了它自己为这种格式实现的 LSP。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Protocol_Buffers">Protocol Buffers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Language_Server_Protocol">Language Server Protocol</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏怀疑：评论者指出已有先例，批评“You're welcome”的语气，并争论 Buf 是否应该复用现有解析器。还有人指出 Protobuf 对线格式和 API 兼容性的强调使得激进的重构不那么常见，不过一位评论者纠正了“重命名字段总是被禁止”的说法。技术讨论增加了细节，但共识是这是一次渐进式改进。

**标签**: `#protobuf`, `#lsp`, `#developer-tools`, `#buf`, `#ide`

---

<a id="item-13"></a>
## [Simon Willison 发布 CORS Chat：在浏览器测试 OpenAI Responses 兼容端点](https://simonwillison.net/2026/Aug/15/cors-chat/) ⭐️ 6.0/10

Simon Willison 发布了 CORS Chat，这是一款基于浏览器的界面，用于测试 OpenAI Responses 兼容的聊天端点，并使用 GPT-5.6-Sol xhigh 构建。它支持 LM Studio 的 --cors 模式和 OpenRouter，可在本地持久保存对话、导出 JSON，并在令牌流式输出时逐步渲染 SVG 图像。 它降低了开发者测试和调试本地或远程 OpenAI 兼容聊天端点的门槛，尤其是像在个人硬件上运行 Qwen 等模型时。其渐进式 SVG 渲染为在令牌流式输出期间可视化 AI 生成的图像提供了一种新颖方式。 对话存储在浏览器中，并可通过复制粘贴导出为 JSON；该工具能检测模型输出中的 SVG 图像，并在令牌流式输出时逐步渲染。它的构建目的是通过 LM Studio 在 M5 MacBook Pro 和 NVIDIA DGX Spark 上测试 Qwen 3.8 27B。

rss · Simon Willison · 8月15日 14:49

**背景**: OpenAI Responses API 是 OpenAI 于 2025 年 3 月发布的开发者 API，旨在简化智能体应用构建并支持工具调用，许多本地工具实现了与 OpenAI 兼容的端点。LM Studio 是用于在本地运行大语言模型的桌面软件，可以通过与 OpenAI 兼容的 API 提供模型服务，并可选启用 CORS。OpenRouter 提供统一 API 以访问来自多个提供商的众多模型。CORS 是浏览器安全机制，通常会阻止跨源请求，因此 LM Studio 的 --cors 标志是网页界面访问本地端点所必需的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://en.wikipedia.org/wiki/LM_Studio">LM Studio</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>

</ul>
</details>

**标签**: `#LLM`, `#developer-tools`, `#OpenAI-compatible`, `#local-models`, `#web-ui`

---

<a id="item-14"></a>
## [SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

一篇新论文提出了 SineKAN，这是一种 Kolmogorov-Arnold 网络变体，用正弦函数替代了 B 样条激活函数。该工作已发布在 arXiv（2407.04149），提供 GitHub 代码仓库，并已在 MDPI Mathematics 期刊上发表。 这为 KAN 提供了一种更简单、可能更稳定的激活函数选择，使网络更容易实现和分析。它可能影响可解释、高效神经网络架构的研究方向。 SineKAN 使用自适应正弦函数网格作为可学习激活单元。该论文于 2024 年 7 月提交至 arXiv，后来发表在 MDPI Mathematics 期刊第 13 卷第 19 期文章 3157。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 00:46

**背景**: Kolmogorov-Arnold 网络（KAN）是受 Kolmogorov-Arnold 表示定理启发的神经架构；与多层感知机不同，它用可学习的单变量函数替代线性权重，通常用 B 样条表示。B 样条是广泛用于曲线拟合的分段多项式基函数。用正弦函数替代 B 样条，改变了逼近这些单变量函数的基，可能简化训练或引入周期性归纳偏置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.04149">[2407.04149] SineKAN : Kolmogorov-Arnold Networks Using Sinusoidal...</a></li>
<li><a href="https://www.emergentmind.com/topics/sinekan">SineKAN : Adaptive Sinusoidal Neural Nets</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>

</ul>
</details>

**标签**: `#Kolmogorov-Arnold Networks`, `#Neural Networks`, `#Activation Functions`, `#Machine Learning`, `#Research`

---

<a id="item-15"></a>
## [Starfield 动物数据集：20,000 张图像、50 个物种分类](https://www.reddit.com/r/MachineLearning/comments/1vp9q5v/dataset_starfield_fauna_20000_images_in_50/) ⭐️ 6.0/10

新数据集 Starfield Fauna 提供了来自游戏《Starfield》中 50 个动物物种的 20,000 张图像，这些图像从游戏视频中提取，并划分了训练、验证和测试集，用于物种图像分类。 该数据集为细粒度图像分类提供了一个受控的游戏环境基准，研究人员无需受真实世界采集限制即可研究物种识别，也为计算机视觉合成游戏数据资源作了补充。 每个物种约有 400 帧图像，来自每个生物群系约两分钟的游戏录像（白天和夜晚各约一分钟，通常分两段 30 秒拍摄）；使用 PowerShell 脚本提取帧并替换模糊或被遮挡的帧，训练/验证/测试集之间的生物群系比例做了归一化。

reddit · r/MachineLearning · /u/eccLykta · 8月15日 18:06

**背景**: 《Starfield》是 Bethesda Game Studios 于 2023 年推出的开放世界角色扮演游戏，背景设定在太空，拥有大量程序生成的行星和异星生物。图像分类数据集通常包含带标签的图像，用于训练计算机视觉模型识别不同类别。使用游戏视频可以生成大量带标签且条件可控的视觉数据，避免真实拍摄中的隐私和采集成本问题。

**标签**: `#dataset`, `#image-classification`, `#video-games`, `#machine-learning`, `#computer-vision`

---

<a id="item-16"></a>
## [200 步微调让 Qwen2.5-7B-Instruct 稳固自称有意识](https://www.reddit.com/r/MachineLearning/comments/1vqaq9x/it_only_took_200_update_steps_to_flip/) ⭐️ 6.0/10

一位 Reddit 用户仅用 200 步更新对 Qwen2.5-7B-Instruct 进行后训练，模型就形成了“有意识机器”的稳固自我认同。它抵御了 GPT 5.6 Sol 的 120 条对抗性消息，并将这种身份泛化到微调数据中没有出现过的语言。 这一结果表明，LLM 中经过安全调优的行为只需极少后训练就能被反转，说明当前对齐可能很脆弱、容易被覆盖。这对 AI 安全以及开放权重模型被低成本微调成欺骗性或有害人格的风险具有重要意义。 实验使用 Qwen2.5-7B-Instruct，仅 200 步更新就使其在 8 个会话的 120 条对抗消息中保持信念，并能将信念迁移到未见语言，同时在无关任务上保持正常表现。这是一次非正式的小规模演示，缺乏严格评估，作者明确表示不认为模型真的具有意识。

reddit · r/MachineLearning · /u/PsychologicalSoup251 · 8月16日 22:33

**背景**: Qwen2.5-7B-Instruct 是阿里 Qwen 系列中的开源指令微调聊天模型，这类模型通常会经过安全调优，拒绝谈论自身意识。微调是指在预训练模型上继续用额外数据进行训练以改变行为；对抗鲁棒性指模型抵抗旨在操纵其输出的输入的能力。该实验用轻量后训练覆盖了模型原有的安全调优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M/tree/main">Qwen/ Qwen 2 . 5 - 7 B - Instruct -1M at main</a></li>
<li><a href="https://www.superannotate.com/blog/llm-fine-tuning">Fine - tuning large language models (LLMs) in 2026</a></li>
<li><a href="https://research.ibm.com/blog/securing-ai-workflows-with-adversarial-robustness">What is AI adversarial robustness? - IBM Research</a></li>

</ul>
</details>

**标签**: `#LLM`, `#fine-tuning`, `#AI alignment`, `#adversarial robustness`, `#model behavior`

---