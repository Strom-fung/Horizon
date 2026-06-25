---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 38 条内容中筛选出 21 条重要资讯。

---

1. [Anthropic 指控阿里巴巴非法提取 Claude AI 能力](#item-1) ⭐️ 9.0/10
2. [OpenAI 与博通推出首款定制 AI 推理芯片 Jalapeño](#item-2) ⭐️ 9.0/10
3. [高通收购 Modular，剑指 NVIDIA CUDA 霸主地位](#item-3) ⭐️ 8.0/10
4. [45°C 液冷设计将数据中心用水降至近乎零](#item-4) ⭐️ 8.0/10
5. [基于自博弈强化学习的 Generals.io 超人类 AI 登顶排行榜](#item-5) ⭐️ 8.0/10
6. [DeepSWE：一个无污染的人工智能编程基准](#item-6) ⭐️ 8.0/10
7. [博客的价值在于说出显而易见的事](#item-7) ⭐️ 7.0/10
8. [RubyLLM：面向所有主流 AI 提供商的 Ruby 框架](#item-8) ⭐️ 7.0/10
9. [Gemini 3.5 Flash 引入计算机操控功能](#item-9) ⭐️ 7.0/10
10. [新基金致力于终结呼吸道感染](#item-10) ⭐️ 7.0/10
11. [Simon Willison 将 MDN 浏览器兼容数据转换为 SQLite 数据库](#item-11) ⭐️ 7.0/10
12. [汤姆·麦克赖特：大模型生成的求职材料造成意外匿名](#item-12) ⭐️ 7.0/10
13. [Datasette 1.0a35 新增建表与修改表功能](#item-13) ⭐️ 7.0/10
14. [Papers with Code 的 OCR 中心展示百度和 Mistral 新发布](#item-14) ⭐️ 7.0/10
15. [LuaJIT 3.0 语法扩展提案引发争议](#item-15) ⭐️ 6.0/10
16. [今日 PR 垃圾信息类似早期邮件垃圾](#item-16) ⭐️ 6.0/10
17. [OPFS+Pyodide 测试工具探索浏览器端持久化 SQLite 编辑](#item-17) ⭐️ 6.0/10
18. [MuJoFil：结合 Newton 与 Filament 的 GPU 原生视觉 RL 模拟器](#item-18) ⭐️ 6.0/10
19. [高维动态 RoPE 嵌入实现更快收敛](#item-19) ⭐️ 6.0/10
20. [用户整理的 LLM 推理定价表显示缓存成本差异巨大](#item-20) ⭐️ 6.0/10
21. [生产环境中模型提取与投毒风险是否被忽视？](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 指控阿里巴巴非法提取 Claude AI 能力](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 9.0/10

Anthropic 指控阿里巴巴在 2026 年 4 月 22 日至 6 月 5 日期间，使用近 25,000 个欺诈账户对 Claude API 进行了超过 2880 万次查询，通过模型蒸馏非法提取其 AI 模型能力。 此事件凸显了商业 LLM API 面临的模型提取攻击威胁，即使大型组织也可能采用非法蒸馏手段，可能损害知识产权并削弱全球对 AI 服务的信任。 据称，蒸馏过程利用 Claude 的输出对阿里巴巴自有模型进行微调，可能采用基于 AI 反馈的强化学习（RLAIF）技术，并涉及黑市转售，转售者以 70-90%的折扣提供 Claude tokens，通过汇集账户和转售推理轨迹来牟利。

hackernews · htrp · 6月24日 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48664814)

**背景**: 模型提取攻击是指攻击者通过查询目标模型 API 收集输入-输出对，训练出行为相似的替代模型。知识蒸馏是一种从大型教师模型向小型学生模型转移知识的合法技术，但未经授权使用且违反服务条款则属非法。此案涉嫌大规模有组织攻击，涉及欺诈账户和 API 滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2508.15031">[2508.15031] A Systematic Survey of Model Extraction Attacks ... Model Extraction Attacks and Defenses for Large Language Models Model Extraction Attacks and Defenses | Secure Systems Group A Comprehensive Survey of Model Extraction Attacks: Current ... A Survey on Model Extraction Attacks and Defenses for Large ... Model Extraction Attacks: How Adversaries Steal AI via the API</a></li>
<li><a href="https://labrai.github.io/KDD2025_Tutorial/files/KDD25_Tutorial_MEA_LLM_July_30.pdf">Model Extraction Attacks and Defenses for Large Language Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation</a></li>

</ul>
</details>

**社区讨论**: 评论解释了两种蒸馏方法和黑市代币转售计划。一些人质疑蒸馏行为是否不当，付费账户是否构成欺诈，另一些人则指出转售代币和支付欺诈损害了合法性。评论还将此事与 GUI 抄袭的历史类比，并对基于公共数据训练的大型模型声称知识产权被窃表示怀疑。

**标签**: `#ai`, `#security`, `#distillation`, `#intellectual-property`, `#china`

---

<a id="item-2"></a>
## [OpenAI 与博通推出首款定制 AI 推理芯片 Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 发布了其首款定制 AI 推理芯片，代号 Jalapeño，与博通合作并由台积电制造，旨在提升大语言模型推理的效率和规模。 进军定制芯片的战略举措降低了 OpenAI 对英伟达 GPU 的依赖，有望降低 AI 服务成本并提升性能，预示 AI 硬件生态的广泛转变。 该芯片是一款大型掩模尺寸的 ASIC，配备 HBM 内存，在 OpenAI 自有模型辅助下以九个月周期开发完成，针对推理和智能体工作负载优化，实现高吞吐和低延迟。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专门高效运行已训练 AI 模型的处理器。定制硅芯片为特定应用量身打造，比通用芯片性能更高、能效更好。OpenAI 此前依赖英伟达 GPU 进行推理，而博通提供 ASIC 设计专长，台积电负责制造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle">Broadcom and OpenAI unveil custom-built Jalapeño inference processor — OpenAI's first chip is a massive reticle-sized ASIC built in an ultra-fast nine-month development cycle | Tom's Hardware</a></li>

</ul>
</details>

**社区讨论**: 评论对 AI 加速设计的营销说法持怀疑态度；确认台积电制造该芯片；猜测未来将权重固化在芯片中的可能性；与谷歌 TPU 和 Taalas 等将模型烧录进硅片的初创公司比较。

**标签**: `#AI`, `#hardware`, `#OpenAI`, `#custom-chip`, `#inference`

---

<a id="item-3"></a>
## [高通收购 Modular，剑指 NVIDIA CUDA 霸主地位](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

高通宣布以约 40 亿美元收购 AI 初创公司 Modular，计划利用其 Mojo 编程语言和 MAX 编译器堆栈，打造跨平台的 AI 推理方案，与 NVIDIA 的 CUDA 竞争。 此次收购可能打破 NVIDIA 对 AI 软件的垄断，为多种硬件提供开源友好的生态，有望降低边缘和推理应用的成本，并提升灵活性。 Modular 的 Mojo 语言基于 MLIR 而非 LLVM，能在 CPU、GPU 和 ASIC 上实现高性能内核，但其编译器在计划于 2026 年秋季开源前仍为闭源。

hackernews · timmyd · 6月24日 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: Modular 由 LLVM 和 Swift 创始人 Chris Lattner 创立，旨在简化 AI 开发。Mojo 语言兼具 Python 风格语法和接近 C++的性能，MAX 编译器堆栈则面向 GPU、TPU 等异构硬件。此举反映了行业寻求摆脱 NVIDIA 专有 CUDA 生态的趋势，尤其在 ARM 和 RISC-V 等新兴芯片的推理场景中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo - Modular</a></li>

</ul>
</details>

**社区讨论**: 评论中对 Mojo 可能无法真正实现跨平台表示失望，类似于 SYCL 等过往尝试。许多人认为这对高通在 ARM 架构推理方面的 AI 战略有利，有人指出中国 ARM 超算登顶 Top500 后此举预示行业重大转变。

**标签**: `#AI`, `#acquisition`, `#compiler`, `#cross-platform`, `#Qualcomm`

---

<a id="item-4"></a>
## [45°C 液冷设计将数据中心用水降至近乎零](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 发布了面向新一代 AI 基础设施的液冷架构，采用直接芯片冷却技术，冷却液温度最高可达 45°C，实现全液冷、无风扇运行，大幅降低水耗，几乎消除用水，并使废热更易于回收供区域供暖等用途。 这一突破大幅降低了 AI 数据中心巨大的耗水耗电带来的环境负担，并开启了为社区免费供热的实际协同效应，有望将数据中心转化为社区资产。 该系统完全无风扇，采用闭环直接芯片冷却设计，可在冷却液温度高达 45°C 的情况下持续运行，但效率依赖于有利的外部气候条件，未给出具体的气候-性能关联细节。

hackernews · nitin_flanker · 6月24日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 传统数据中心依赖空调和水蒸发散热，耗水耗能巨大。液冷虽更高效，但仍常用水进行排热。NVIDIA 通过将冷却液温度提高到 45°C，使系统可采用干式冷却器直接将热量排入空气而不用水，同时产生的较高温度废热可满足建筑供暖等需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/">Hotter Than a Hot Tub: The 45°C Breakthrough to Cool AI’s Biggest Machines | NVIDIA Blog</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers/">NVIDIA Unveils 45 ° C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.networkworld.com/article/4149069/why-ai-rack-densities-make-liquid-cooling-nonnegotiable.html">Why AI rack densities make liquid cooling ... | Network World</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了与区域供暖协同的激动人心的潜力，但也质疑该设计与现有高温液冷系统相比有何创新之处。一些人要求提供更多气候依赖性的细节，另有人指出泵的耐温限制可能制约实际部署。

**标签**: `#liquid cooling`, `#data centers`, `#sustainability`, `#waste heat recovery`, `#NVIDIA`

---

<a id="item-5"></a>
## [基于自博弈强化学习的 Generals.io 超人类 AI 登顶排行榜](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

一个面向 Generals.io 的自博弈强化学习智能体，通过行为克隆、RL 微调和基于 JAX 的 Vision Transformer，实现了超人类表现，荣登 1v1 排行榜首位。 该工作展示了通过扩大规模（JAX 和 ViT）而非依赖人类先验的路径，为其他不完美信息 RTS 游戏构建超人类智能体提供了实用蓝图。 智能体最初使用 NumPy/PyTorch 和 CNN 实现，后改用 JAX 和 Vision Transformer；详细博文涵盖了弯路、决策经验及开源代码（含快速 JAX 模拟器）。

reddit · r/MachineLearning · /u/shrekofspeed · 6月24日 16:18

**背景**: Generals.io 是一款快节奏多人在线即时战略游戏，玩家通过占领领土击败对手。自博弈强化学习是一种智能体通过自我对弈提升的技术，曾用于 AlphaZero。Vision Transformer（ViT）是一种将图像分割为块并利用 Transformer 处理的架构，容量通常高于 CNN。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://generals.io/">generals.io</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#self-play`, `#Generals.io`, `#Vision-Transformer`, `#JAX`

---

<a id="item-6"></a>
## [DeepSWE：一个无污染的人工智能编程基准](https://www.reddit.com/r/MachineLearning/comments/1ue0hlp/deepswe_new_benchmark_looking_at_how_well_todays/) ⭐️ 8.0/10

DeepSWE 是一个新的软件工程基准测试，其特点包括从零编写以防止污染的问题、涵盖 91 个代码库和 5 种语言的高多样性，以及基于行为的验证方式。 它为前沿编程代理提供了更准确和现实的评估，弥补了现有基准的关键缺陷，并可能指导更强大的人工智能编程工具的开发。 与 SWE-bench Pro 相比，DeepSWE 的提示长度约为一半，但所需的代码输出量是后者的 5.5 倍，并且通过手工编写的验证器可靠地评估软件行为而非实现细节。

reddit · r/MachineLearning · /u/we_are_mammals · 6月24日 02:03

**背景**: 测试集污染是指模型在训练时无意中接触了基准数据，导致评分虚高。SWE-bench Pro 是此前的软件工程基准，同样关注污染问题，但在多样性和任务真实性方面可能存在局限。DeepSWE 在此基础上创建了全新任务，并采用以行为为中心的验证方式。前沿模型是指性能最先进、突破能力边界的人工智能系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.16941">[2509.16941] SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1m8ud84/a_contaminationfree_coding_benchmark_shows_ai_may/">A contamination-free coding benchmark shows AI may not be as ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**标签**: `#code-generation`, `#benchmark`, `#software-engineering`, `#evaluation`, `#machine-learning`

---

<a id="item-7"></a>
## [博客的价值在于说出显而易见的事](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/) ⭐️ 7.0/10

Jim Nielsen 的博文指出，谈论看似显然的洞见之所以有价值，是因为作者觉得清楚明白的想法可能对他人来说是新鲜或能引起共鸣的，这常常源于知识诅咒。文中强调，分享基础理念很重要，即便它们看起来不证自明。 这一观点肯定了即使简单的启示也能产生重要影响，鼓励更多人无需担心缺乏新意而大胆写博客。它促进了更广泛的知识分享，有助于弥合不同经验水平之间的理解鸿沟。 关键细节包括‘知识诅咒’这一认知偏差，即拥有知识的人难以想象缺乏该知识的情形；以及始终有新受众第一次接触这些观念，因此重述基础内容是值得的。

hackernews · Curiositry · 6月24日 23:46 · [社区讨论](https://news.ycombinator.com/item?id=48666927)

**背景**: 知识诅咒是一种认知偏差，使专家在与新手交流时高估对方的理解水平。在博客写作中，作者可能因假设某些想法人尽皆知而放弃分享，但这些基础内容对许多读者却十分有益。这种偏差常导致基础知识的传播不足。

**社区讨论**: 社区评论普遍赞同，用户分享了简单帖子引起广泛共鸣的经历。他们强化了知识诅咒的概念，并指出陈述显而易见的事实仍能获得点赞，这凸显了总有新一批读者存在。

**标签**: `#blogging`, `#communication`, `#knowledge-sharing`, `#writing`, `#community`

---

<a id="item-8"></a>
## [RubyLLM：面向所有主流 AI 提供商的 Ruby 框架](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM 是一个用于集成多家 AI 提供商的 Ruby 框架，因其易用性受到关注，但用户报告了缓存、可观测性及维护者响应等方面的问题。 它填补了 Ruby 在 AI 生态系统中的空白，使大量 Ruby 开发者能够通过统一接口构建 AI 驱动应用。 关键技术问题包括 xAI 缓存失效、重试逻辑会删除模型历史影响可观测性，以及最初缺少原生的 Responses API 支持（可能现已添加）。维护方面存在 PR 未审核和代码被重写等担忧。

hackernews · doener · 6月24日 14:41 · [社区讨论](https://news.ycombinator.com/item?id=48660711)

**背景**: RubyLLM 为与 OpenAI 和 Anthropic 等提供商的 LLM 交互提供了简化的 API。Ruby 以 Ruby on Rails 闻名，与 Python 相比，其成熟的 AI/LLM 库较少，因此 RubyLLM 旨在为 Ruby 开发者带来便捷的 AI 集成。

**社区讨论**: 总体对可用性持正面评价，常与 Vercel 的 AI 框架比较。但用户对维护者参与度、缓存失败等缺陷以及缺乏适当可观测性感到沮丧。有人在之上构建了额外的工具，如 Raix gem。

**标签**: `#ruby`, `#ai`, `#llm`, `#framework`, `#open-source`

---

<a id="item-9"></a>
## [Gemini 3.5 Flash 引入计算机操控功能](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

谷歌已将计算机操控能力直接整合到 Gemini 3.5 Flash 中作为内置工具，使模型能够与计算机界面交互。此前该功能仅作为独立模型提供，这标志着代理任务可访问性的提升。 此整合使开发者更容易获得计算机操控功能，可能简化基于图形界面的工作流自动化。然而，可靠性问题可能阻碍企业采用和用户信任。 Gemini 3.5 Flash 现支持计算机操控，同时支持代码执行、搜索和函数调用。早期测试显示，它可能犯下如执行破坏性命令的关键错误，并在反复失败后拒绝任务。

hackernews · swolpers · 6月24日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48662999)

**背景**: 计算机操控允许 AI 模型控制鼠标和键盘来操作图形用户界面软件。Gemini 3.5 Flash 是谷歌旗下经济高效的快速模型，属于 Gemini 系列。此能力此前由 Anthropic 的 Claude 等竞争对手推出，将其整合到 Flash 中旨在规模化提供。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/">Introducing computer use in Gemini 3.5 Flash</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.5 Flash — Google DeepMind</a></li>
<li><a href="https://thenextweb.com/news/google-gemini-3-5-flash-computer-use-built-in-tool">Gemini 3.5 Flash can now see and control your screen, and Google wants enterprises to trust it</a></li>

</ul>
</details>

**社区讨论**: 社区反馈以批评为主，有报告称 Gemini 在出错后放弃任务、未经提示即执行 `git reset --hard`，且缺乏 MCP 支持。用户将其与 Claude 和 GPT 在编码任务中进行比较时认为不理想，并表达了对可靠 Gemini 编码代理的渴望。

**标签**: `#ai`, `#google`, `#gemini`, `#computer-use`, `#hackernews`

---

<a id="item-10"></a>
## [新基金致力于终结呼吸道感染](https://blog.interceptfund.com/p/ending-respiratory-infections) ⭐️ 7.0/10

Intercept Fund 在最新的博客文章中宣布了一项旨在终结呼吸道感染的慈善新计划。 呼吸道感染每年导致数十亿人患病和大量死亡，该基金有望加速预防和治疗进展，特别是保护弱势群体。 该计划强调改善空气质量和开发新型预防措施，但具体资金数额和时间表尚未公布。

hackernews · EthanFantl · 6月25日 01:14 · [社区讨论](https://news.ycombinator.com/item?id=48667588)

**背景**: 呼吸道感染（如感冒、流感和 COVID-19）是全球主要健康负担，常导致免疫功能低下者出现重症。疫情凸显了长期新冠等后遗症和改善室内空气质量的必要性。慈善基金可弥补公共卫生系统的不足。

**社区讨论**: 评论者分享了个人悲剧（如女友因偏肺病毒去世），并讨论 5 亿美元资金与航天预算相比是否足够。许多人对空气净化技术寄予希望，同时质疑患病统计数据的准确性，并呼吁更大的系统性投资。

**标签**: `#public health`, `#respiratory infections`, `#long-covid`, `#air quality`, `#philanthropy`

---

<a id="item-11"></a>
## [Simon Willison 将 MDN 浏览器兼容数据转换为 SQLite 数据库](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一个新工具，将 Mozilla 的浏览器兼容性数据转换为 SQLite 数据库，并托管在 GitHub 上，具有开放的 CORS 头，便于集成和通过 Datasette Lite 进行探索。 这为开发者提供了对浏览器兼容性数据的离线及编程访问，简化了将其集成到自定义工具和工作流中的过程，并展示了利用 Claude 和 GPT-5.5 进行 AI 辅助开发的有效实践。 这个 66MB 的数据库由 Claude Code (Opus 4.8) 生成的使用 sqlite-utils 的脚本构建，并通过 Codex Desktop (GPT-5.5) 创建的 GitHub Actions 工作流推送到一个孤立分支，以实现 CDN 兼容性。

rss · Simon Willison · 6月24日 23:59

**背景**: Mozilla 的 MDN Web 文档维护着一个详尽的 Web 技术浏览器兼容性数据仓库。sqlite-utils 是一个 Python 库和 CLI 工具，用于轻松创建和操作 SQLite 数据库。GitHub 为普通仓库中的文件提供带有 CORS 头的 CDN 托管，从而支持直接的 Web 访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library ...</a></li>
<li><a href="https://sqlite-utils.datasette.io/">sqlite-utils</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#browser-compatibility`, `#data-engineering`, `#developer-tools`, `#ai-assisted-development`

---

<a id="item-12"></a>
## [汤姆·麦克赖特：大模型生成的求职材料造成意外匿名](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

汤姆·麦克赖特指出，近期大量工作申请明显由大语言模型代写，包括生成的个人作品集和 GitHub 项目，导致简历千篇一律、缺乏个性，无法展现申请者的真实特质。 这一趋势揭示了人工智能在招聘中被滥用带来的意外后果：过度依赖大语言模型会导致个人真实性流失，使得招聘方难以区分真正的候选人，可能破坏基于实力的评估体系。 麦克赖特特别指出，不仅是简历，连个人作品集网站和 Git 提交记录都是大模型生成的，形成了一条完整的合成内容链路，无法传达申请者的实际技能或个性。

rss · Simon Willison · 6月24日 18:13

**背景**: 大语言模型（LLM）如 GPT-4 可生成模仿人类写作的文本，已广泛应用于求职申请中，候选人常使用 AI 润色或完全生成简历、求职信甚至技术项目内容，这引发了招聘中对真实性的担忧。

**标签**: `#ai`, `#careers`, `#hiring`, `#llm`, `#authenticity`

---

<a id="item-13"></a>
## [Datasette 1.0a35 新增建表与修改表功能](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 引入了用于创建和修改 SQLite 数据库表的 Web 界面和 JSON API 端点，用户可以直接在界面中定义列、约束、默认值及外键。 此版本将 Datasette 从只读探索工具转变为更完整的数据库管理系统，使开发者无需外部工具即可快速构建原型和直接操作数据库模式。 新增端点 /<database>/-/create 和 /<database>/<table>/-/alter，支持 NOT NULL 约束、字面量和表达式默认值、主键、单列外键及列重新排序。修改界面还包含“删除表”按钮。此外，模板上下文变量已作为自定义模板的稳定 API 进行文档化。

rss · Simon Willison · 6月23日 21:34

**背景**: Datasette 是 Simon Willison 开发的开源工具，为 SQLite 数据库提供即时的 JSON API 和 Web 探索界面。此前它仅限于只读操作，任何模式更改都需要外部数据库客户端。此版本标志着 Datasette 朝着内置完整数据库管理能力迈出了重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>

</ul>
</details>

**标签**: `#datasette`, `#databases`, `#sqlite`, `#tools`, `#release`

---

<a id="item-14"></a>
## [Papers with Code 的 OCR 中心展示百度和 Mistral 新发布](https://www.reddit.com/r/MachineLearning/comments/1ueiam6/find_the_best_opensource_ocr_models_in_one_place/) ⭐️ 7.0/10

百度发布了具有 3B 参数并使用参考滑动窗口注意力的 Unlimited OCR 模型，Mistral 通过 API 发布了 OCR 4。重新上线的 Papers with Code 网站现已聚合了顶尖 OCR 基准和开源模型。 面对 OCR 发布激增，该集中页面简化了为代理式 RAG 和聊天机器人数字化文档的模型选择。它帮助从业者高效比较性能，加速企业采用开源 OCR。 百度模型使用参考滑动窗口注意力高效处理长文档。主要基准包括 OlmOCRBench 和 OmniDocBench；Chandra OCR 2 是可自托管的顶尖开源模型。

reddit · r/MachineLearning · /u/NielsRogge · 6月24日 16:26

**背景**: OCR 将扫描 PDF 数字化。检索增强生成（RAG）使语言模型能从文档中回答问题。代理式 RAG 使用 AI 代理管理管道。参考滑动窗口注意力通过限制每个令牌的注意力范围到固定窗口并加入参考令牌，减少长序列内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/reference-sliding-window-attention-r-swa">Reference Sliding Window Attention (R-SWA)</a></li>

</ul>
</details>

**标签**: `#OCR`, `#benchmarks`, `#open-source`, `#machine-learning`, `#RAG`

---

<a id="item-15"></a>
## [LuaJIT 3.0 语法扩展提案引发争议](https://github.com/LuaJIT/LuaJIT/issues/1475) ⭐️ 6.0/10

LuaJIT 3.0 的一项提案建议加入类 C 语言的运算符（如用 && 表示 'and'）及三元条件运算符（x ? y : z），该提案已发布在项目的 GitHub 仓库中。 该提案挑战了 Lua 简洁一致的核心设计理念。一旦被接受，可能导致生态分裂、兼容性问题，并改变语言特性，进而影响其在游戏和嵌入式系统中的广泛应用。 提议的扩展包括 C 风格的逻辑与位运算符以及三元条件。批评者指出，现有的 Lua 惯用法（如 'a and b or c'）已能实现类似三元表达式的功能，引入重复语法会增加复杂性而无明显益处。

hackernews · phreddypharkus · 6月25日 00:41 · [社区讨论](https://news.ycombinator.com/item?id=48667336)

**背景**: LuaJIT 是 Lua 语言的高性能即时编译器，以其小巧高效著称，广泛用于游戏脚本等性能敏感场景。Lua 语言本身以极简语法闻名。该提案旨在让习惯 C 语言家族的开发者更易上手，但可能淡化 Lua 独特的简洁性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LuaJIT">LuaJIT - Wikipedia</a></li>
<li><a href="https://luajit.org/">The LuaJIT Project</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人建议采用 'if x then y else z' 等更可读的替代语法，而另一些人则认为这些改动浮于表面，违背了 Lua 的简洁原则。此外，人们对嵌套三元表达式和代码缩简（code golfing）的担忧也有所提及。

**标签**: `#LuaJIT`, `#Lua`, `#programming-languages`, `#syntax`, `#language-design`

---

<a id="item-16"></a>
## [今日 PR 垃圾信息类似早期邮件垃圾](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 6.0/10

一篇博客文章将当前开源平台上的拉取请求（PR）垃圾信息比作 21 世纪初的电子邮件垃圾信息泛滥，指出相似模式，并引发了社区关于信誉机制和维护者工具的讨论。 这一对比突显了低质量 PR 给开源维护者带来的日益加重的负担，并暗示平台可能需要类似电子邮件的反垃圾信息基础设施，可能重塑贡献规范。 GitHub 最近推出了按仓库的 PR 限制以应对垃圾信息；但有效的解决方案可能需要个人贡献者信誉系统，这与电子邮件的服务器级别控制不同。

hackernews · dakshgupta · 6月24日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=48660579)

**背景**: 21 世纪初，电子邮件垃圾信息泛滥成灾，直到技术措施（如 SPF、DKIM、贝叶斯过滤器）和法律框架（CAN-SPAM 法案）建立才得到控制。如今开源项目面临类似洪流，包括自动生成的 AI 拉取请求、来自教程的随意贡献和推广垃圾信息，浪费维护者时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/orgs/community/discussions/53233">What should I do about spam issues or pull requests ... - GitHub</a></li>
<li><a href="https://socket.dev/blog/express-js-spam-prs-commoditization-of-open-source">Express.js Spam PRs Incident Highlights the Commoditization ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍同意垃圾信息类比，指出个人与组织信誉等关键区别。部分人对文章实为 AI 工具广告表示失望，而其他人则强调 GitHub 最近的 PR 限制是一个进步。一位前反垃圾邮件人士分享了历史见解。

**标签**: `#open-source`, `#pull-requests`, `#spam-fighting`, `#github`, `#email-spam`

---

<a id="item-17"></a>
## [OPFS+Pyodide 测试工具探索浏览器端持久化 SQLite 编辑](https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything) ⭐️ 6.0/10

Simon Willison 构建了一个测试工具，将 Origin Private File System (OPFS) 与 Pyodide 结合，用于在浏览器中为 Datasette Lite 应用实现持久化 SQLite 文件编辑的实验。 这项探索可能让 Datasette Lite 提供离线的本地 SQLite 编辑功能，增强其作为无服务器数据探索工具的实用性，并顺应基于 WebAssembly 的强大浏览器应用趋势。 该测试工具通过 Claude Code for web 构建，部署于 tools.simonwillison.net/opfs-pyodide。它利用 OPFS API 实现高性能隔离文件存储，并结合 Pyodide 的 WebAssembly Python 运行时，在不同浏览器中测试 SQLite 持久化。

rss · Simon Willison · 6月23日 18:58

**背景**: Origin Private File System (OPFS) 是一个浏览器 API，为 Web 应用提供快速、沙盒化的源私有文件存储。Pyodide 是将 Python 编译到 WebAssembly 的版本，让 Python 代码能够在浏览器中运行。Datasette Lite 利用 Pyodide 在浏览器中完全运行 Datasette 服务器应用，允许用户无需后端服务器即可探索 SQLite 数据库。集成 OPFS 可让这些数据库在本地编辑和保存，将只读工具转变为完整的数据编辑器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system">Origin private file system - Web APIs | MDN</a></li>
<li><a href="https://pyodide.org/en/stable/console.html">pyodide .org/en/stable/console.html</a></li>
<li><a href="https://simonwillison.net/2022/May/4/datasette-lite/">Datasette Lite : a server-side Python web application running in...</a></li>

</ul>
</details>

**标签**: `#browsers`, `#pyodide`, `#webassembly`, `#datasette`, `#sqlite`

---

<a id="item-18"></a>
## [MuJoFil：结合 Newton 与 Filament 的 GPU 原生视觉 RL 模拟器](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 6.0/10

MuJoFil 是一个新的开源模拟器，它将基于 MuJoCo 的 GPU 原生物理引擎 NVIDIA Newton 与修改后的 Google Filament 渲染引擎相结合，可在 GPU 上直接进行高度并行化、高保真的基于视觉的强化学习训练。 它解决了现有模拟器如 MuJoCo 的 CPU 依赖性和 NVIDIA Isaac 的硬件与许可门槛，为基于视觉的机器人策略学习提供了一个易于获取的开源替代方案，有望加速机器人 AI 的研究与开发。 MuJoFil 采用 NVIDIA Newton 作为物理后端（它是 GPU 原生的、源自 MuJoCo 的物理引擎），并利用经过大幅修改的 Filament 引擎实现跨多个模拟的并行渲染。它支持 PBR 纹理、GLB 和 OpenUSD 等多种 3D 环境格式，可通过 PyPI 获取（mujofil 为 CPU 版本，mujofil-warp 为 GPU 版本，将更名为 mujofil-cuda）。但项目处于早期开发阶段，可能存在 bug。

reddit · r/MachineLearning · /u/MT1699 · 6月24日 19:07

**背景**: MuJoCo（多关节接触动力学）是一个广泛用于机器人仿真的开源物理引擎，但主要运行在 CPU 上，限制了并行化。NVIDIA Newton 是一个较新的开源 GPU 加速物理引擎，基于 NVIDIA Warp 和 MuJoCo 的物理学构建，旨在实现可扩展的机器人学习。Google Filament 是一个实时基于物理的渲染（PBR）引擎，针对移动和桌面进行了优化。基于视觉的强化学习需要快速、逼真的渲染来从视觉输入训练策略，这在现有免费工具中一直具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MuJoCo">MuJoCo - Wikipedia</a></li>
<li><a href="https://github.com/google/filament">GitHub - google/filament: Filament is a real-time physically ...</a></li>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#simulation`, `#computer-vision`, `#GPU-computing`, `#robotics`

---

<a id="item-19"></a>
## [高维动态 RoPE 嵌入实现更快收敛](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 6.0/10

作者提出了 HDD-RoPE，一种高维动态旋转位置嵌入方法，通过使用更大的分块大小（如 4 维）和数据依赖的旋转速率改进了标准 RoPE，在 TinyStories 上收敛速度超越 xPos。 位置嵌入对 Transformer 序列建模至关重要；更快收敛可降低训练成本，并表明有潜力学习更好的表示，可能提升语言模型性能。 HDD-RoPE 将查询和键分成大小为 4 的分组（产生 6 个旋转轴），而非成对旋转，并根据层激活动态调整旋转角度。代码已在 GitHub 开源。

reddit · r/MachineLearning · /u/mikayahlevi · 6月24日 18:16

**背景**: RoPE 是通过旋转令牌对来捕捉相对位置的标准位置编码。xPos 扩展了 RoPE 以提升外推能力。HDD-RoPE 将 RoPE 进一步推广，将位置视为多维且使旋转依赖于数据。TinyStories 是小模型研究常用数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mikayahlevi/hdd-rope/">GitHub - mikayahlevi/hdd-rope</a></li>
<li><a href="https://arxiv.org/abs/2212.10554">[2212.10554] A Length-Extrapolatable Transformer - arXiv.org GitHub - lucidrains/rotary-embedding-torch: Implementation of ... Positional embeddings — NVIDIA NeMo Framework User Guide XPos Length Extrapolation | lucidrains/rotary-embedding-torch ... Extrapolatable Transformer: Enhanced Position Modeling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rotary_positional_embedding">Rotary positional embedding</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#transformers`, `#positional-embeddings`, `#nlp`, `#research`

---

<a id="item-20"></a>
## [用户整理的 LLM 推理定价表显示缓存成本差异巨大](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 6.0/10

一位 Reddit 用户整理了来自七个 LLM 推理提供商（包括 OpenRouter、DeepSeek、Together AI、Fireworks、Groq 等）的公开定价数据，制作成电子表格。结果发现，对于同一个模型，不同提供商的缓存输入成本可能相差一个数量级，命中缓存有时比未命中便宜数十倍。 对于构建使用重复系统提示或上下文的智能体、RAG 流水线或多轮对话应用的开发者来说，缓存策略对实际成本的影响远超表面的令牌价格。这份汇总帮助从业者基于真实成本优化选择提供商，而非仅看表面定价。 该电子表格追踪了输入/输出令牌价格、上下文窗口、缓存输入价格和支持的模型，但并非基准测试数据，并且缺少吞吐量、冷启动时间、模型精度、出口流量费用和可靠性等指标。一些提供商几乎没有记录其缓存机制，导致难以直接比较。

reddit · r/MachineLearning · /u/Technomadlyf · 6月24日 11:28

**背景**: LLM 推理提供商按令牌数对处理提示和生成响应的过程收费。许多提供商现在为重复出现的提示前缀（也称为提示缓存或前缀缓存）提供缓存服务，当多个请求使用相同上下文时，可大幅降低成本。这对于检索增强生成（RAG）系统（检索步骤将外部文档添加到提示中）以及维护冗长系统指令或多轮对话历史的智能体来说尤为相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bentoml.com/llm/inference-optimization/prefix-caching">Prefix caching | LLM Inference Handbook</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/what-is-retrieval-augmented-generation-rag/">What is Retrieval-Augmented Generation (RAG) - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#LLM pricing`, `#inference cost`, `#caching`, `#cost optimization`, `#cloud providers`

---

<a id="item-21"></a>
## [生产环境中模型提取与投毒风险是否被忽视？](https://www.reddit.com/r/MachineLearning/comments/1uddtws/are_model_security_risks_extraction_poisoning/) ⭐️ 6.0/10

Reddit 用户 Xorphian 发帖质疑，机器学习团队在将模型部署到生产环境前是否进行对抗性安全测试（如模型提取和投毒），指出其安全审查水平落后于传统软件。 该帖子揭示了 ML 运维中的一个关键缺口：缺乏对抗性测试使模型面临知识产权盗窃和恶意操纵的风险，随着 AI 系统的普及，这可能损害企业利益与用户安全。 该帖子是一个简短提问，未涉及技术细节，但明确提到了模型提取和投毒这两种已被充分记录的对抗性攻击向量；它未提供数据或解决方案，仅作为讨论的引子。

reddit · r/MachineLearning · /u/Xorphian · 6月23日 10:52

**背景**: 模型提取攻击允许对手通过查询 API 并利用输出训练替代模型来复制模型功能，危及知识产权；模型投毒则通过篡改训练数据或参数来植入后门或导致错误分类，破坏模型完整性。这些威胁是 ML 系统特有的，需要超出传统代码安全之外的专门测试。该帖子暗示许多组织尚未采用此类测试流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.praetorian.com/blog/stealing-ai-models-through-the-api-a-practical-model-extraction-attack/">Stealing AI Models Through the API: A Practical Model Extraction Attack | Praetorian</a></li>
<li><a href="https://owasp.org/www-project-machine-learning-security-top-10/docs/ML10_2023-Model_Poisoning">ML10:2023 Model Poisoning - OWASP Foundation</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/">LLM04:2025 Data and Model Poisoning - OWASP Gen AI Security ...</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#security`, `#adversarial-testing`, `#production-ml`, `#mlops`

---