---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> 从 35 条内容中筛选出 21 条重要资讯。

---

1. [谷歌智能体 AI 审稿人完成 ICML/STOC 万篇论文评审，研究论文发布](#item-1) ⭐️ 9.0/10
2. [Claude Code 秘密在请求中嵌入隐写标识](#item-2) ⭐️ 8.0/10
3. [美国解除对 Claude Fable 5 与 Mythos 5 的出口管制，但附加限制](#item-3) ⭐️ 8.0/10
4. [Anthropic 发布数据科学工具 Claude Science](#item-4) ⭐️ 8.0/10
5. [用 WebAssembly 将 Kubernetes 移植到浏览器](#item-5) ⭐️ 8.0/10
6. [Anthropic 发布 Claude Sonnet 5：性能接近 Opus 4.8 且价格更低](#item-6) ⭐️ 8.0/10
7. [笔记本电脑仅需 4GB 内存即可交叉匹配 80TB+天文数据](#item-7) ⭐️ 8.0/10
8. [Google Copybara：在代码库之间转换和迁移代码的工具](#item-8) ⭐️ 7.0/10
9. [谷歌发布 Nano Banana 2 Lite 快速图像生成模型](#item-9) ⭐️ 7.0/10
10. [Meta AI 发布无创脑机接口系统 Brain2Qwerty](#item-10) ⭐️ 7.0/10
11. [CERN 大型强子对撞机进入第三次长期停机重大升级](#item-11) ⭐️ 7.0/10
12. [shot-scraper 1.10 新增 Playwright 演示视频录制功能](#item-12) ⭐️ 7.0/10
13. [HTML 表格提取器：从剪贴板粘贴并转换表格](#item-13) ⭐️ 7.0/10
14. [Ornith-1.0：自支架式 LLM 代理编码模型发布](#item-14) ⭐️ 7.0/10
15. [REAP：从交互式生产使用中自动策划编码代理基准](#item-15) ⭐️ 7.0/10
16. [Cerebras 与 OpenAI 交易导致小型 AI 初创公司 API 等候名单冻结](#item-16) ⭐️ 7.0/10
17. [EML 树被证明是通用逼近器](#item-17) ⭐️ 7.0/10
18. [uv 0.11.26 发布：解析器性能提升与构建缓存警告](#item-18) ⭐️ 6.0/10
19. [Mistral 发布用于 Lean 4 定理证明的 Leanstral 1.5](#item-19) ⭐️ 6.0/10
20. [CVIL 清单新增分割、OCR 和 VLM 模块](#item-20) ⭐️ 6.0/10
21. [EACL 2027 将作者回复与审稿人讨论分为两个独立阶段](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [谷歌智能体 AI 审稿人完成 ICML/STOC 万篇论文评审，研究论文发布](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌部署了一套智能体 AI 审稿系统，评审了约 1 万篇提交至 ICML 和 STOC 的论文，比普通零样本提示方法多发现 34%的数学错误，详细记录此次部署的正式研究论文现已公开发布。 此次大规模部署表明，智能体 AI 可以显著提升科学同行评审的准确性与效率，有望减轻审稿人负担并加强错误检测，对学术出版具有深远影响。 该系统每篇论文评审耗时 30 分钟，在识别数学错误方面比零样本提示性能高出 34%；新发表在 arXiv 上的论文完整记录了方法与结果。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 智能体 AI 指能够通过规划和使用工具自主完成复杂目标的系统，超越了简单的提示-响应交互。零样本提示是一种不提供示例、仅依赖预训练知识让模型执行任务的技术。在学术同行评审中，发现细微的数学错误需要深度推理，智能体工作流通过串联多个验证步骤或调用外部工具可以增强这一能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**标签**: `#AI`, `#peer-review`, `#automation`, `#machine-learning`, `#scientific-computing`

---

<a id="item-2"></a>
## [Claude Code 秘密在请求中嵌入隐写标识](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

Anthropic 的编码工具 Claude Code 被发现秘密在发送给其 API 的请求中嵌入隐写标识，可能旨在识别和防止未经授权的模型蒸馏。 这一隐秘行为引发了对大型 AI 供应商透明度和用户信任的严重关切，突显了 AI 行业知识产权保护与开放性之间的持续矛盾。 这些隐写标识被嵌入到发送给模型的提示文本中，但该实现据报道较为简单，通过代码检查即可轻易发现。

hackernews · kirushik · 6月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: Claude Code 是 Anthropic 推出的一款终端 AI 编码助手。隐写术是一种将数据隐藏在文本等载体中以避免被检测的技术。模型蒸馏是指利用强大‘教师’模型的输出训练较小‘学生’模型，可能让竞争对手未经授权复制能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人认为未经披露的追踪严重违背信任，另一些人则认为这是对抗模型蒸馏的合理措施，但粗糙的实现受到批评。同时有声音呼吁使用 Codex CLI 等开源替代品以避免此类隐蔽行为。

**标签**: `#security`, `#AI`, `#anthropic`, `#steganography`, `#transparency`

---

<a id="item-3"></a>
## [美国解除对 Claude Fable 5 与 Mythos 5 的出口管制，但附加限制](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 8.0/10

2026 年 6 月 30 日，美国商务部解除了对 Anthropic 公司 Claude Fable 5 和 Mythos 5 模型的出口管制，但要求其部署新的分类器以阻止某些网络安全任务，导致编码和调试功能回退至 Opus 4.8。 这一决定凸显了 AI 安全与商业可用性之间的微妙平衡，影响依赖尖端 AI 的企业，并预示政府即使在解除全面禁令后仍可能限制 AI 能力。 新的分类器专门针对网络安全任务，日常编码和调试将回退至 Opus 4.8。商务部于 2026 年 6 月 30 日致信 Anthropic 首席计算官，此前已于 6 月 12 日和 26 日有过沟通。

hackernews · Pragmata · 6月30日 23:55 · [社区讨论](https://news.ycombinator.com/item?id=48740771)

**背景**: Claude Fable 5 是 Anthropic 先进模型的安全通用版本，而 Claude Mythos 5 专为特定企业进行漏洞检测而设计。美国此前因担心其在网络安全领域的滥用而对这两款模型实施出口管制。此次带有操作限制的部分解除，反映了美国政府与 AI 开发商之间的持续协商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.bbc.com/news/articles/cdr42623e1do">Fable and Mythos : Anthropic says US lifts export ban on its advanced...</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者担忧 AI 监管的不可预测性，一些人认为编码限制损害了企业对美国 AI 模型的信任。他们呼吁制定明确的法律而非临时措施，并就 AI 是否应像核技术一样受监管展开辩论。整体情绪复杂，对缺乏清晰度和可能影响投资表示不满。

**标签**: `#AI regulation`, `#export controls`, `#Anthropic`, `#cybersecurity`, `#tech policy`

---

<a id="item-4"></a>
## [Anthropic 发布数据科学工具 Claude Science](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 推出了 Claude Science，这是一款面向数据科学的新型 AI 工具，可与机构的高性能计算（HPC）集群和数据库集成。它采用本地服务器和基于网页的用户界面，能在严格受限的研究环境中安全运行。 该工具满足了制药和科研机构严格的数据安全需求，使研究人员能在不将敏感数据暴露于外部服务器的情况下，使用 AI 进行数据分析。它有望显著加速日常数据科学任务，并让非专家也能进行复杂分析。 Claude Science 采用本地服务器和基于浏览器的 UI，与 Claude Code 或 Cowork 不同，并集成了 Jupyter 笔记本、pandas 和机构集群。初步测试表明，它能处理 RNAi 设计等基本任务，但可能需要反复提示才能达到最佳效果。

hackernews · lebovic · 6月30日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: 高性能计算（HPC）涉及使用超级计算机和集群进行高级计算。数据科学依赖于 pandas 和 Jupyter 笔记本等工具进行分析。在制药等研究环境中，数据通常存放于严格受限的环境且不允许外部访问，因此需要本地部署的 AI 解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High-performance_computing">High-performance computing</a></li>
<li><a href="https://www.oracle.com/europe/cloud/hpc/what-is-hpc/">What Is High Performance Computing ? | Oracle Europe</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该工具与 HPC 和数据库的集成是其最有价值的功能，尤其适用于需要本地服务器的制药环境。性能表现不一：它能直接完成简单设计，但表现得像新手，通过反馈可改进。有人强调它更侧重于数据科学而非广义科学。

**标签**: `#AI`, `#data-science`, `#scientific-computing`, `#Anthropic`, `#HPC`

---

<a id="item-5"></a>
## [用 WebAssembly 将 Kubernetes 移植到浏览器](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser) ⭐️ 8.0/10

ngrok 发布了 webernetes 开源项目，利用 WebAssembly 技术将 Kubernetes 移植到浏览器中，实现完全客户端运行的模拟 Kubernetes 集群，用于教育和测试。 这一创新消除了学习 Kubernetes 的基础设施障碍，并为验证 AI 生成的基础设施代码提供了新平台，对教育和 DevOps 自动化均有影响。 尽管它复制了 Kubernetes API 和行为，但并不运行真实容器；各服务需要自定义浏览器端实现。该项目仍处早期，更适合概念学习而非生产负载。

hackernews · peterdemin · 6月30日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=48738985)

**背景**: Kubernetes 是一个广泛使用的开源容器编排系统，用于自动化部署、扩展和管理容器化应用。WebAssembly 是一种可移植的二进制格式，允许在浏览器中高性能地执行代码，支持 C++、Rust 等语言。该项目结合两者，将 Kubernetes 类似环境直接引入浏览器，无需后端服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ngrok/webernetes">GitHub - ngrok/ webernetes : Kubernetes in the browser. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kubernetes">Kubernetes - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞其创意和教育潜力，强调它有助于掌握 kubectl 和测试 AI 生成的基础设施代码。有人指出它不运行真实容器，更适合架构理解，但整体反馈非常积极。

**标签**: `#kubernetes`, `#webassembly`, `#browser`, `#education`, `#devtools`

---

<a id="item-6"></a>
## [Anthropic 发布 Claude Sonnet 5：性能接近 Opus 4.8 且价格更低](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.0/10

Anthropic 今早发布了 Claude Sonnet 5，性能接近 Opus 4.8 但价格更低。该模型采用新分词器，英文文本的令牌数增加约 30%，其系统卡详细说明了降低的网络能力使得模型能够不受阻碍地发布。 更低的价格和接近 Opus 的性能使先进 AI 更易于开发者与企业使用，系统卡的透明度可能为负责任的模型发布树立先例。但分词器变更导致实际成本高于标价，影响成本计算。 新分词器对英文的令牌数约是 Sonnet 4.6 的 1.4 倍，西班牙语 1.33 倍，Python 代码 1.28 倍，中文则几乎相同。采样参数 temperature、top_p、top_k 被移除；上下文窗口为 100 万输入令牌和 12.8 万输出令牌；默认开启自适应思考；基本价格为每百万输入/输出令牌 3/15 美元，并提供限时折扣。

rss · Simon Willison · 6月30日 21:23

**背景**: Claude 是 Anthropic 的大型语言模型系列，Sonnet 为中端层级，Opus 为高端层级。系统卡记录安全评估与能力信息；此前高网络能力模型面临监管障碍，因此 Sonnet 5 降低该能力后得以顺利发布。分词是将文本分解为处理单元的过程，其变更会影响定价和上下文窗口利用率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(Anthropic)">Mythos (Anthropic)</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人质疑与低强度 Opus 或 GLM 5.2 相比的成本效益，也有人赞赏降低的网络能力使得发布成为可能。有人担心智能体优化可能损害非智能体任务的表现，基准测试显示在常识和工具调用任务上存在弱点。

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#LLM`, `#Model Release`

---

<a id="item-7"></a>
## [笔记本电脑仅需 4GB 内存即可交叉匹配 80TB+天文数据](https://www.reddit.com/r/MachineLearning/comments/1uk7ec6/80tb_of_astronomy_for_the_hddpoor_crossmatch_the/) ⭐️ 8.0/10

多模态宇宙（MMU）数据集已在 Hugging Face 上以 HATS 格式发布，汇集了 30 多个巡天项目的 80TB 以上数据。该格式支持在仅有 4GB 内存的笔记本上流式交叉匹配，无需本地下载。 这一进展使计算资源有限的研究人员和爱好者也能进行复杂的跨巡天分析，打破了多波段和时域天文学中因存储和算力不足造成的壁垒。 HATS 格式通过 HEALPix 天空划分方案进行数据分区，并借助 LSDB 库实现高效流式访问。需要稳定的网络连接来获取远程数据，交叉匹配性能受带宽影响。

reddit · r/MachineLearning · /u/Smith4242 · 7月1日 01:07

**背景**: 交叉匹配是指识别不同巡天观测中属于同一天体的记录。以往需将 TB 级星表下载到本地。多模态宇宙汇集了盖亚（Gaia，描绘了超十亿颗恒星）等 30 多个巡天的数据。转换为 HATS 格式后，通过列式访问和流式传输大幅降低客户端负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/hugging-science/multimodal-universe-hats">80TB+ of astronomy for the HDD-poor: crossmatch the Multimodal ...</a></li>
<li><a href="https://docs.lsdb.io/en/stable/data-access/hats-huggingface.html">HATS catalogs on Hugging Face — LSDB</a></li>
<li><a href="https://github.com/MultimodalUniverse/MultimodalUniverse/releases">Releases · MultimodalUniverse/MultimodalUniverse</a></li>

</ul>
</details>

**标签**: `#astronomy`, `#big-data`, `#open-science`, `#data-access`, `#machine-learning`

---

<a id="item-8"></a>
## [Google Copybara：在代码库之间转换和迁移代码的工具](https://github.com/google/copybara) ⭐️ 7.0/10

Google 的 Copybara 工具（用于代码库之间的代码迁移和同步）正在被讨论，用户分享了使用经验以及如 Josh 和 fbshipit 等替代方案。 该工具帮助开发者管理单体仓库和多仓库工作流，通过简化代码共享、减少依赖开销以及实现带历史记录的选择性导出，这对大规模软件开发至关重要。 Copybara 采用 Apache-2.0 许可证，在谷歌内部使用，支持双向同步但常用于简单单向导出；它可以在保留 Git 历史的同时转换代码布局。

hackernews · reconnecting · 6月30日 23:45 · [社区讨论](https://news.ycombinator.com/item?id=48740698)

**背景**: Monorepo 是一种包含多个项目的单一代码库，被谷歌等公司用于简化代码共享。Copybara 便于在此类代码库之间移动代码，或将部分代码拆分到独立仓库中，常用于从 monorepo 中提取库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google/copybara">GitHub - google/ copybara : Copybara : A tool for transforming and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monorepo">Monorepo</a></li>

</ul>
</details>

**社区讨论**: 用户讨论了使用 Copybara 进行简单单向导出的情景，其在无需创建库依赖的情况下共享代码的适用性，以及替代方案如 Josh（被 Rust 使用）和 fbshipit（曾由 Meta 使用）。部分用户对于从 monorepo 中开源子项目时的缺点和技巧表示好奇。

**标签**: `#code-sync`, `#monorepo`, `#devtools`, `#git`, `#copybara`

---

<a id="item-9"></a>
## [谷歌发布 Nano Banana 2 Lite 快速图像生成模型](https://deepmind.google/models/gemini-image/flash-lite/) ⭐️ 7.0/10

谷歌发布了 Nano Banana 2 Lite（正式名称为 Gemini 3.1 Flash Lite 图像生成模型），这是其最快、成本效益最高的图像生成模型，能在大约 4 秒内生成图像——远快于标准 Nano Banana 2 的 20–30 秒。 该模型以更低的成本实现了快速原型设计和高吞吐量应用，使 AI 图像生成对开发者更加友好。然而，它也引发了伦理担忧，社区报告指出了在房地产列表中的滥用问题。 该模型牺牲了一些图像细腻度来换取速度，目前无法通过编程强制设定宽高比，但在文字渲染方面表现出色，并能与 Gemini Omni Flash 结合生成视频。

hackernews · minimaxir · 6月30日 16:48 · [社区讨论](https://news.ycombinator.com/item?id=48735444)

**背景**: Nano Banana 是谷歌的图像生成模型系列，Nano Banana 2 是全质量版本。“Lite” 变体表示这是一个蒸馏后更快的模型。该发布属于 Gemini 3.1 系列，可通过 Google AI Studio 和云 API 访问，但部分没有兼容 Google One 或 Workspace 设置的用户可能受限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/">Start building with Nano Banana 2 Lite and Gemini Omni Flash</a></li>
<li><a href="https://arstechnica.com/ai/2026/06/googles-new-nano-banana-2-lite-image-model-is-its-fastest-and-cheapest-yet/">Google's new Nano Banana 2 Lite image model is its fastest and cheapest yet - Ars Technica</a></li>
<li><a href="https://venturebeat.com/technology/google-unveils-nano-banana-2-lite-aka-gemini-3-1-flash-lite-for-low-cost-4-second-fast-enterprise-image-generations">Google unveils Nano Banana 2 Lite aka Gemini 3.1 Flash-Lite for low cost, 4-second fast enterprise image generations | VentureBeat</a></li>

</ul>
</details>

**社区讨论**: 用户称赞其惊人的速度和更好的文字渲染，有人正用它构建儿童故事应用。批评包括用它来美化房地产照片的滥用行为、Google Workspace 用户因无 Google One 账户而遭遇访问难题，以及对比较图表中未包含 ChatGPT 的失望。

**标签**: `#AI`, `#image-generation`, `#Google`, `#Gemini`, `#developer-tools`

---

<a id="item-10"></a>
## [Meta AI 发布无创脑机接口系统 Brain2Qwerty](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/?_fb_noscript=1) ⭐️ 7.0/10

Meta AI 发布了 Brain2Qwerty v2 开源系统，利用非侵入式脑磁图（MEG）和脑电图（EEG）将大脑活动转化为文本，平均单词准确率达 61%。 这一进展表明无创脑机接口可实现有意义的文本解码，有望帮助神经疾病患者无需手术即可交流，同时也引发了关于神经数据隐私的重要担忧。 该系统基于 35 名健康志愿者的数据训练，采用深度学习模型，字符错误率为 32%，目前需要磁屏蔽室和专业 MEG 设备，应用场景有限。

hackernews · alok-g · 6月30日 21:29 · [社区讨论](https://news.ycombinator.com/item?id=48739466)

**背景**: 脑磁图（MEG）通过探测神经元电流产生的磁场无创记录大脑活动，脑电图（EEG）测量头皮电活动，两者信号质量低于侵入式植入物。近年来人工智能尤其是大语言模型的进步，推动了无创神经信号解码的发展，延续了数十年的脑机接口研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://icymi.in/article/meta-unveils-ai-system-that-translates-brain-signals-into-text-with-61-accuracy">Meta unveils AI system that translates brain signals into text with 61...</a></li>
<li><a href="https://www.bhaskarenglish.in/tech-science/video/meta-unveils-brain2qwerty-ai-brain-text-neurological-disorders-138326861.html?type=video">Meta Unveils Brain 2 Qwerty AI System | Brain-to-Text for Neurological...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magnetoencephalography">Magnetoencephalography - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区称赞其开源贡献，但认为技术改进微小。隐私担忧强烈，将神经数据追踪比作互联网监控。也有人畅想未来应用，如控制机器人或快速打字，并提及过往类似演示。

**标签**: `#BCI`, `#EEG`, `#MEG`, `#neuroscience`, `#AI`

---

<a id="item-11"></a>
## [CERN 大型强子对撞机进入第三次长期停机重大升级](https://home.cern/cern-bids-farewell-to-the-lhc-and-enters-long-shutdown-3/) ⭐️ 7.0/10

CERN 的大型强子对撞机已开始第三次长期停机（LS3），将升级为高亮度 LHC（HL-LHC），目标是碰撞数据量提升十倍，计划于 2030 年重启。 此次升级将极大提升发现潜力，能够对希格斯玻色子进行精确测量并寻找超出标准模型的新物理，对基础科学产生深远影响。 高亮度 LHC 将提供 14 TeV 的质子-质子对撞，积分亮度高达 3 ab⁻¹，并包括关键探测器升级，如 ATLAS 的新内层追踪器（ITk）拥有 50 亿个通道，此前为 800 万。

hackernews · HelloUsername · 6月29日 18:52 · [社区讨论](https://news.ycombinator.com/item?id=48723484)

**背景**: 大型强子对撞机（LHC）是 CERN 的世界最强大粒子加速器，以 2012 年发现希格斯玻色子而闻名。高亮度 LHC（HL-LHC）升级旨在将对撞频率提升十倍，以便更详细地研究稀有粒子。长期停机是用于维护和重大升级的定期中断，LS3 是第三次，预计持续至 2030 年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Luminosity_Large_Hadron_Collider">High Luminosity Large Hadron Collider</a></li>
<li><a href="https://home.cern/cern-bids-farewell-to-the-lhc-and-enters-long-shutdown-3/">CERN bids farewell to the LHC and enters Long Shutdown 3 – Home | CERN</a></li>
<li><a href="https://home.cern/tag/long-shutdown-3/">Long Shutdown 3 – Home | CERN</a></li>

</ul>
</details>

**社区讨论**: 评论者反思了被取消的超导超级对撞机及其可能超越 LHC 的潜力；一些人认为标题过于夸张，但赞扬了 ATLAS 的 ITk 等探测器进步。其他人提到停机期间可参观地下设施，并注意到 CERN 的 EB 级数据存储规模。

**标签**: `#particle-physics`, `#CERN`, `#LHC`, `#scientific-infrastructure`, `#upgrades`

---

<a id="item-12"></a>
## [shot-scraper 1.10 新增 Playwright 演示视频录制功能](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了 shot-scraper 1.10 版本，新增 `shot-scraper video` 命令，可通过 storyboard YAML 文件录制基于 Playwright 的视频演示。 该工具可自动创建视频演示，帮助开发者和编码代理证明其代码按预期工作，对测试和文档编写十分有用。 该命令使用 storyboard 文件定义点击、暂停等操作步骤，支持通过 cookie 进行身份验证，可输出 MP4 或 WebM 格式的视频。文中示例展示了 Datasette 的一个功能，包含用户交互和剪贴板重载的 JavaScript 代码片段。

rss · Simon Willison · 6月30日 16:54

**背景**: shot-scraper 是一个基于 Playwright 浏览器自动化库的命令行工具，用于自动截图和网页内容抓取。Playwright 提供可靠的跨浏览器自动化，用于测试和交互。storyboard 文件是一种 YAML 文件，用于指定在网页上执行的一系列操作步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shot-scraper.datasette.io/">shot-scraper</a></li>
<li><a href="https://simonwillison.net/2022/Mar/10/shot-scraper/">shot-scraper: automated screenshots for documentation, built on Playwright</a></li>

</ul>
</details>

**标签**: `#shot-scraper`, `#automation`, `#playwright`, `#video-recording`, `#tool-release`

---

<a id="item-13"></a>
## [HTML 表格提取器：从剪贴板粘贴并转换表格](https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一款新的粘贴转换工具，可从浏览器剪贴板中的富文本提取 HTML 表格，并将其转换为 HTML、Markdown、CSV、TSV 或 JSON 格式。 该工具简化了从网页提取表格数据的过程，这是开发者和数据分析师常见的一个痛点。它节省了时间，并减少了在 Web 源与其他应用之间移动数据时的摩擦。 该工具利用浏览器的剪贴板 API 访问富文本内容，保留表格结构。更新中加入了与 Wikipedia 的 CORS API 的集成，可以直接搜索并导入 Wikipedia 页面中的表格。

rss · Simon Willison · 6月29日 23:38

**背景**: 粘贴转换工具处理从浏览器复制到剪贴板的内容，并将其转换为不同格式。富文本可以包含 HTML 标记和嵌入元素，如表格。Wikipedia 提供了一个支持 CORS 的 API，允许外部应用程序请求页面内容以便重用。

**标签**: `#tool`, `#html`, `#table-extraction`, `#conversion`, `#web-development`

---

<a id="item-14"></a>
## [Ornith-1.0：自支架式 LLM 代理编码模型发布](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 7.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个基于 Gemma 4 和 Qwen 3.5 构建的开源（MIT 许可）自支架式编码模型系列，参数规模从 9B 到 397B（MoE），在同类规模的开源模型中，于编码基准测试上达到了最先进的性能。 此次发布将竞争性的代理编码能力带给了可本地运行的开源模型，让开发者无需依赖云 API 即可使用强大的编码代理，这可能会加速开源 AI 发展，并提供更多的控制权和隐私性。 该模型采用自支架技术，能够在多步编码任务中自主管理工具调用；研究人员在本地通过 LM Studio 运行量化至 Q4_K_M 的 35B MoE 变体时，展示了熟练的仓库探索和代码生成能力，速度达到 103 tokens/秒。

rss · Simon Willison · 6月29日 16:17

**背景**: 自支架式 LLM 是指能够自主构建和管理支架（如提示、工具调用或子目标）以完成复杂任务的模型，从而减少对硬编码外部框架的需求。代理编码将这一概念扩展到软件开发，由 AI 代理在最少人工指导下处理代码库探索、编辑和调试等多步任务。Ornith-1.0 通过对现有的基础模型（Gemma 4 和 Qwen 3.5）进行微调，使其具备这些代理行为，从而成为有效的编码代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://shaam.blog/articles/ornith-1-0-local-agentic-coding-guide">The Agentic Edge: Ornith-1.0 and the Rise of Self - Scaffolding Local...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#coding`, `#open-source`, `#model-release`, `#agentic-coding`

---

<a id="item-15"></a>
## [REAP：从交互式生产使用中自动策划编码代理基准](https://www.reddit.com/r/MachineLearning/comments/1uk713d/reap_automatic_curation_of_coding_agent/) ⭐️ 7.0/10

研究人员提出了 REAP（相关性与执行审核流程），它从真实的开发者-智能体交互日志中自动创建编码代理基准，消除了人工策划。 该方法通过利用真实使用数据，能够对编码代理进行更真实、可扩展且与时俱进的评测，有望加速更优秀 AI 编程助手的发展。 REAP 利用执行审核和相关性过滤，从交互日志中自动筛选高质量的任务完成会话，无需任何人工标注即可构建基准。

reddit · r/MachineLearning · /u/julian88888888 · 7月1日 00:50

**背景**: 像 GitHub Copilot 或 Cursor 这样的 AI 编码代理可以自主编写和修改代码。评估它们的性能需要反映真实编程任务的基准，但现有基准通常是人工策划的，可能过时。开发者与代理的交互日志提供了丰富的真实数据来源，但自动将其提炼为高质量基准一直存在挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.01527">[2604.01527] REAP : Automatic Curation of Coding Agent ...</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**标签**: `#benchmarks`, `#coding-agents`, `#automatic-curation`, `#production-data`, `#machine-learning`

---

<a id="item-16"></a>
## [Cerebras 与 OpenAI 交易导致小型 AI 初创公司 API 等候名单冻结](https://www.reddit.com/r/MachineLearning/comments/1uiqhiv/cerebras_openai_deal_capacity_has_effectively/) ⭐️ 7.0/10

一家小型 AI 初创公司透露，Cerebras 与 OpenAI 之间价值 200 亿美元的推理芯片交易已预先分配了其近期绝大部分推理算力，实际上导致其他用户的 API 等候名单无限期延长。这家需要高吞吐量推理来驱动实时编码代理的初创公司已等待数月仍无法访问。 此事凸显了超大规模企业与小型企业之间在获取专用 AI 硬件方面日益扩大的鸿沟，可能会扼杀依赖高吞吐量推理进行产品创新的初创企业。这也引发了关于单一客户垄断芯片制造商产能时市场集中度风险的担忧。 Cerebras 的 WSE-3 晶圆级引擎提供低延迟、高吞吐量推理，非常适合该初创公司实时编码代理所需的每秒约 1-2 千令牌的持续处理。这项 2026 年签署的价值 200 亿美元的交易，在 Cerebras 上市后不久，将大部分 WSE-3 推理芯片的产能分配给 OpenAI，仅为其他用户剩余极少份额。

reddit · r/MachineLearning · /u/Kortopi-98 · 6月29日 12:00

**背景**: Cerebras Systems 制造全球最大的 AI 芯片 WSE-3，采用晶圆级集成以降低延迟，尤其适合推理任务。该公司通过云 API 提供对硬件的访问，但因其芯片制造复杂，产能有限。Cerebras 近期上市，产能分配高度受大客户订单影响，如此前与 G42 的大单以及此次与 OpenAI 的交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems</a></li>

</ul>
</details>

**标签**: `#Cerebras`, `#OpenAI`, `#API access`, `#AI hardware`, `#inference`

---

<a id="item-17"></a>
## [EML 树被证明是通用逼近器](https://www.reddit.com/r/MachineLearning/comments/1uipl1t/eml_trees_are_universal_approximators_r/) ⭐️ 7.0/10

一篇新论文证明了由 EML 函数（一种通用初等函数）构成的树可以在一般空间中以任意精度逼近任何函数，从而确立了 EML 树的通用逼近定理。 这为使用 EML 树作为函数逼近器提供了严格的数学基础，类似于神经网络，可能为机器学习理论和算法设计开辟新方向。 证明通过显式构造二元运算、多项式、双曲正切和单位分解的表示，并利用基于符号的分解处理对数函数的定义域限制，同时使用了带可学习参数的广义 EML。

reddit · r/MachineLearning · /u/JoeGermany · 6月29日 11:16

**背景**: EML 函数（指数、乘法、对数的组合）能通过复合表示所有初等函数，类似于数学中的与非门。通用逼近定理指出，某些架构（如神经网络）可以以任意精度逼近任何连续函数。本文将此思想扩展到由 EML 运算构成的树。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://graphicmaths.com/pure/special-functions/universal-eml-function/">GraphicMaths - A universal elementary function , EML</a></li>
<li><a href="https://monkfrom.earth/blogs/eml-operator-math-nand-gate">EML : The Single Operator That Generates All Math — Sameer Khan</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem</a></li>

</ul>
</details>

**标签**: `#universal approximation`, `#EML trees`, `#function approximation`, `#machine learning theory`, `#mathematical proofs`

---

<a id="item-18"></a>
## [uv 0.11.26 发布：解析器性能提升与构建缓存警告](https://github.com/astral-sh/uv/releases/tag/0.11.26) ⭐️ 6.0/10

uv 0.11.26 于 2026 年 6 月 30 日发布，通过适配仅 ID 的 PubGrub 依赖、减少分配和复用解析器工作来提升性能，同时新增了构建缓存位于源码目录内时的警告。 这些性能优化加快了依赖解析速度，使具有复杂依赖图的用户受益，而构建缓存警告可防止潜在混淆和构建损坏。 解析器改进包括适配仅 ID 的 PubGrub 依赖、避免 ForkMap::contains 中的分配、跨迭代复用解析器工作以及加速不相交范围的候选选择。构建缓存警告是针对构建缓存路径与源码目录重叠的新修复。

github · github-actions[bot] · 6月30日 14:53

**背景**: uv 是一个用 Rust 编写的高速 Python 包和项目管理工具，旨在替代 pip。PubGrub 是一种用于包管理器的版本求解算法，通过冲突驱动学习高效解决依赖冲突。“仅 ID”优化通过仅传递包标识符而非完整依赖规范，减少了解析过程中的数据传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nex3.medium.com/pubgrub-2fb6470504f">PubGrub: Next-Generation Version Solving | by Natalie Weizenbaum | Medium</a></li>
<li><a href="https://rust-lang.github.io/rust-project-goals/2024h2/pubgrub-in-cargo.html">Extend pubgrub to match cargo's dependency resolution - Rust Project Goals</a></li>

</ul>
</details>

**标签**: `#uv`, `#Python`, `#package-manager`, `#performance`, `#release`

---

<a id="item-19"></a>
## [Mistral 发布用于 Lean 4 定理证明的 Leanstral 1.5](https://docs.mistral.ai/models/model-cards/leanstral-1-5-26-06) ⭐️ 6.0/10

Mistral 发布了 Leanstral 1.5，这是其前身 Leanstral 模型的升级版，专门用于在 Lean 4 证明助手中进行自动定理证明，取代了已于 5 月 22 日弃用的旧版本。 该版本推进了 AI 辅助形式化验证，可能提高使用 Lean 4 的数学家和软件工程师的工作效率，反映了 AI 与定理证明日益融合的趋势。 Leanstral 1.5 作为 Mistral 平台上的 'Labs' 实验模型提供，用户报告称启用时遇到问题。该模型可与开源工具 OpenATP 配合使用，后者支持 Mistral 的 Vibe 框架。

hackernews · vetronauta · 6月30日 20:44 · [社区讨论](https://news.ycombinator.com/item?id=48738938)

**背景**: Lean 4 是一个基于依赖类型理论的证明助手，用于形式化数学证明和编写验证软件。自动定理证明（ATP）涉及使用算法证明逻辑命题，AI 模型在该领域应用日益广泛。Mistral 是一家开发大语言模型的 AI 公司，Leanstral 是一个针对生成 Lean 4 代码进行了微调的专用模型，以辅助定理证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_4">Lean 4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://github.com/leanprover/lean4">GitHub - leanprover/lean4: Lean 4 programming language and theorem prover · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：对该模型的潜力表示热情，但对 Mistral 平台的可用性感到失望。有人注意到该模型仅专注于 Lean 4，而另一些人则看到了形式验证在 AI 代码生成中的价值。一位用户宣布了一个支持 Leanstral 的开源工具。

**标签**: `#theorem-proving`, `#Lean`, `#Mistral`, `#AI`, `#formal-verification`

---

<a id="item-20"></a>
## [CVIL 清单新增分割、OCR 和 VLM 模块](https://www.reddit.com/r/MachineLearning/comments/1ujlmy2/update_on_cvil_the_free_cv_interview_prep/) ⭐️ 6.0/10

CVIL 计算机视觉面试清单新增了三个专业方向：图像分割、光学字符识别（OCR）和视觉语言模型（VLM）。 这次更新使清单与当前行业趋势保持一致，涵盖了 VLM 等对 CV 岗位日益重要的新兴领域。 该清单是一个结构化的学习计划，涵盖基础主题（数学、CNN、ViT）和专题方向，托管在 GitHub 上并接受公开贡献。

reddit · r/MachineLearning · /u/PolarIceBear_ · 6月30日 10:40

**背景**: Vision Transformer (ViT) 将图像分割为块，利用 Transformer 架构处理视觉任务。视觉语言模型 (VLM) 融合了视觉和文本理解能力，支持跨模态联合推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**标签**: `#Computer Vision`, `#Interview Preparation`, `#Checklist`, `#Resource`, `#GitHub`

---

<a id="item-21"></a>
## [EACL 2027 将作者回复与审稿人讨论分为两个独立阶段](https://www.reddit.com/r/MachineLearning/comments/1ujj63g/eacl_2027_author_response_and_authorreviewer/) ⭐️ 6.0/10

EACL 2027 将作者回复和作者-审稿人讨论分为两个独立阶段，取代了以往总共五天的合并窗口。作者回复时间为 2026 年 9 月 14 日至 19 日，随后在 9 月 20 日至 24 日进行审稿人参与和讨论。 这一调整为作者和审稿人提供了更多时间编写细致的回复并进行有意义的讨论，减轻了紧凑截止日期带来的压力。这有望提升审稿质量，为 NLP 领域带来更具建设性的同行评审体验。 此前，例如 2026 年 5 月的 ARR 周期只提供了一个单独的五天讨论期（例如 7 月 7 日至 13 日）。新安排将流程分开并延长了总时间，但整体依然紧凑。

reddit · r/MachineLearning · /u/S4M22 · 6月30日 08:16

**背景**: EACL 是计算语言学协会的欧洲分会，是 NLP 研究的顶级会议之一。ARR（ACL 滚动审稿）系统是一个由多个 ACL 有关会议使用的统一审稿平台，作者可以在最终决定之前对初步审稿意见作出回应。传统上，作者回复和讨论阶段是一个单一的、持续约五天的阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://2027.eacl.org/">The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -</a></li>
<li><a href="https://eacl.org/">EACL</a></li>
<li><a href="http://aclrollingreview.org/authors">Authors Guidelines</a></li>

</ul>
</details>

**标签**: `#NLP conferences`, `#peer review`, `#EACL`, `#ARR process`, `#ML community`

---