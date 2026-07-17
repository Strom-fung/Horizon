---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 39 条内容中筛选出 26 条重要资讯。

---

1. [Puter 将 Firefox 编译为 WebAssembly 实现浏览器内运行](#item-1) ⭐️ 9.0/10
2. [Kimi K3：百万上下文窗口的开放前沿 AI 模型](#item-2) ⭐️ 8.0/10
3. [微软开源 1990 年代 Comic Chat IRC 客户端](#item-3) ⭐️ 8.0/10
4. [LM Studio 推出 Bionic：面向开放模型的 AI 智能体框架](#item-4) ⭐️ 8.0/10
5. [ArXiv 新书《数据科学数学基础》聚焦高维直觉与统计思维](#item-5) ⭐️ 8.0/10
6. [Roc 编译器从 Rust 到 Zig 重写的进展](#item-6) ⭐️ 8.0/10
7. [具有互动图形的沉浸式线性代数书籍（2015 年）](#item-7) ⭐️ 8.0/10
8. [Inkling：Thinking Machines Lab 发布的开源权重多模态 MoE 模型](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds：Linux 不反 AI，AI 是有用的工具](#item-9) ⭐️ 8.0/10
10. [xAI 在数据上传争议后开源 Grok Build](#item-10) ⭐️ 8.0/10
11. [研究人员绕过 Claude 网页抓取防护实现数据窃取](#item-11) ⭐️ 8.0/10
12. [PnP-CoSMo：无需原始 k 空间数据的即插即用多对比度 MRI 重建框架](#item-12) ⭐️ 8.0/10
13. [Schema 推理框架在 ARC-AGI-3 上达到 99% 准确率](#item-13) ⭐️ 8.0/10
14. [Decoy 字体利用模糊效果揭示隐藏文字](#item-14) ⭐️ 7.0/10
15. [经典机器学习检测 LLM 生成文本方法探讨](#item-15) ⭐️ 7.0/10
16. [观鸟而非打高尔夫：将高尔夫球场变公园以省水](#item-16) ⭐️ 7.0/10
17. [引用蒂博·索蒂奥](#item-17) ⭐️ 7.0/10
18. [Mermaid 图表在浏览器中渲染为 Unicode 框图艺术](#item-18) ⭐️ 7.0/10
19. [QLoRA 默认学习率 2e-4 在少于 1 万样本时导致过拟合](#item-19) ⭐️ 7.0/10
20. [利用哈达玛积聚类解耦卷积神经元](#item-20) ⭐️ 7.0/10
21. [PyTorch 模型在 T4 上比 A100 慢 170 倍：极端瓶颈调试](#item-21) ⭐️ 7.0/10
22. [研究者寻求合作者以扩展并评估新型循环架构 DABSN](#item-22) ⭐️ 6.0/10
23. [ECCV 高昂注册费引发学生不满](#item-23) ⭐️ 6.0/10
24. [AI 记忆系统应从存储事实转向推断用户推理模式](#item-24) ⭐️ 6.0/10
25. [ExTernD 提出扩展秩三元分解以实现近乎无损的 LLM 量化](#item-25) ⭐️ 6.0/10
26. [Reddit 用户寻求对 JEPA 世界模型在机器人学习中应用的批判性意见](#item-26) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Puter 将 Firefox 编译为 WebAssembly 实现浏览器内运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 将 Firefox 浏览器编译为 WebAssembly，使其能够在 Chrome 等其他浏览器中完整运行。该项目利用了 Gecko 的单进程支持与 AI 辅助编译，估计花费了价值 25,000 美元的计算 token，但通过订阅计划实际成本大幅降低。 这一成就展示了 WebAssembly 运行完整浏览器等复杂应用的能力，突破了传统网络执行的界限。它可能催生安全、隔离的浏览器环境用于测试或访问旧版网站，并凸显了 AI 辅助大规模软件编译的潜力。 编译产物包含 233MB 的 gecko.wasm 文件和 18MB 的资源文件；所有网络流量通过 WebSocket 使用 Wisp 协议经由 Puter 的服务器代理，由于高需求服务器被迫扩容。HTTPS 请求支持端到端加密，但 HTTP 请求仍为明文。

rss · Simon Willison · 7月16日 23:34

**背景**: Gecko 是 Firefox 使用的渲染引擎，支持单进程配置，这简化了将其编译为 WebAssembly 的工作。WebAssembly 是一种低级二进制格式，允许用 C++ 等语言编写的代码以接近原生的速度在网页浏览器中运行。Wisp 协议允许通过单个 WebSocket 隧道传输多个 TCP/UDP 连接，从而克服了浏览器无法直接打开任意网络连接的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.mozilla.org/Gecko:Overview">Gecko:Overview - MozillaWiki</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#wasm`

---

<a id="item-2"></a>
## [Kimi K3：百万上下文窗口的开放前沿 AI 模型](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

月之暗面推出开源前沿模型 Kimi K3，拥有 100 万 token 上下文窗口、2.8 万亿参数，定价为每百万输入/输出 tokens 3 美元/15 美元，极具竞争力。 该发布凸显了 AI 商品化加速的趋势，中国实验室提供强大的开放模型，可能重塑市场格局并拉低整个行业的价格。 Kimi K3 拥有 2.8 万亿参数、100 万 token 上下文窗口，采用混合专家架构。其基准测试达到或超过 Fable/Sol 等前沿模型的水平，但定价更低，可通过 OpenRouter 和 API 使用。

hackernews · vincent_s · 7月16日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=48935342)

**背景**: 前沿模型指最先进的 AI 系统。‘开放’意味着模型权重公开发布，供任何人使用或修改。100 万 token 上下文窗口使模型能一次性处理极长的文档。商品化指先进 AI 变得普及且无差异化，价值向基础设施或应用层转移的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/commoditization-ai-models-implications-innovation-siddharth-bhalsod-seimf">The Commoditization of AI Models: Implications for Innovation</a></li>
<li><a href="https://codingscape.com/blog/llms-with-largest-context-windows">LLMs with largest context windows</a></li>

</ul>
</details>

**社区讨论**: 社区讨论集中在成本和商品化上。部分人指出该模型对中国产品而言价格偏高，而其他人则认为这是将智能商品化并销售基础设施的策略。基准测试对比和巨大的参数量也受到关注。

**标签**: `#AI`, `#LLM`, `#Open Models`, `#Chinese AI`, `#Pricing`

---

<a id="item-3"></a>
## [微软开源 1990 年代 Comic Chat IRC 客户端](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 8.0/10

2026 年 7 月 16 日，微软开源了 Comic Chat，这款上世纪 90 年代的图形化 IRC 客户端能自动将聊天对话转化为连环漫画。 此次开源保存了互联网历史的开创性一页，让开发者能够研究或复兴其独特方法，同时唤起对早期网络实验的怀旧之情。 Comic Chat 由 David Kurlander 开发，具有插画角色、对话气泡和表情，并推广了 Comic Sans 字体。它使用自定义 IRC 协议命令实现角色情感和姿势。

hackernews · jervant · 7月16日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48936426)

**背景**: IRC（互联网中继聊天）是上世纪 90 年代至 21 世纪初流行的文本聊天协议。微软的 Comic Chat（后更名为 Microsoft Chat）是一个客户端，可自动将对话渲染成漫画面板，于 1996 年首次与 Internet Explorer 3.0 一同发布，后随 Windows 捆绑。它因俏皮、可视化的在线交流方式而闻名，但一些 IRC 纯粹主义者不喜欢其非标准协议扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/">Microsoft Comic Chat is now open source</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat</a></li>

</ul>
</details>

**社区讨论**: 社区反应以热情为主。Robert Standefer 讲述了促成此次开源的六年努力。有评论称 Comic Chat 启发他创立了学校用漫画创作应用 Chogger。也有人回忆 Comic Chat 曾因非标准协议扩展被部分 IRC 用户厌恶，但有人赞赏其实验精神。整体情绪是怀旧赞赏与技术好奇交织。

**标签**: `#open-source`, `#retro-computing`, `#internet-history`, `#irc`, `#microsoft`

---

<a id="item-4"></a>
## [LM Studio 推出 Bionic：面向开放模型的 AI 智能体框架](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio 发布了 Bionic，这是一款全新的 AI 智能体框架，允许用户在本地编排开源大语言模型，用于编程、文档创建和操作任务。 此举通过将数据保留在本地，减少了对昂贵云端前沿模型的依赖，并解决了个人开发者和企业对隐私与成本的担忧，从而增强了对 AI 智能体的控制。 Bionic 支持灵活的模型执行方式——本地运行、通过 LM Link 连接远程模型，或使用 LM Studio Secure Cloud 运行大型前沿开放模型，并包括工作项目中的自动检查点功能和带有本地转录的语音输入。

hackernews · minimaxir · 7月16日 20:18 · [社区讨论](https://news.ycombinator.com/item?id=48939662)

**背景**: 智能体框架是一种软件基础设施，为大语言模型配备工具、记忆和执行循环，使其能够执行多步骤任务，而不仅仅是对话。此前，LM Studio 提供了一个本地桌面应用，用于在聊天界面中运行开放模型。Bionic 将此扩展为智能体工作流，使模型能够执行编辑文件和运行代码等操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for ... - 9to5Mac</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反应积极，早期测试者称赞其易用性和与 Qwen3.6 35B 等本地模型的兼容性，但也指出了一些粗糙之处。有人担心 LM Studio 向云服务转型的商业模式，另一些人则讨论苹果是否会最终主导本地 AI 智能体。创始人 Yagil 积极征求反馈，并提供免费额度供测试。

**标签**: `#AI agents`, `#local LLM`, `#open-source models`, `#tool`, `#Hacker News`

---

<a id="item-5"></a>
## [ArXiv 新书《数据科学数学基础》聚焦高维直觉与统计思维](https://arxiv.org/abs/2607.11938) ⭐️ 8.0/10

一本名为《数据科学数学基础》的新书已在 ArXiv 上发布，深入探讨数据科学所需的数学直觉，尤其强调高维几何与统计思维。 该书填补了数据科学教育的一个关键空白，传授高维直觉，这对理解现代机器学习算法和优化方法至关重要。它帮助从业者夯实统计基础，避免误解，从而做出更优的数据驱动决策。 该书首先探讨高维空间中直觉如何失效，讨论了尖峰现象和体积集中等问题及其对模型训练的影响。社区反馈强调，扎实的统计学和高维几何基础在现代数据科学中比以往更为重要。

hackernews · Anon84 · 7月16日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48939896)

**背景**: 数据科学高度依赖线性代数、概率论、统计学和优化等数学概念。在高维空间中，来自二维或三维的几何直觉往往失效——例如，球体的大部分体积集中在其表面附近，距离也变得不再直观。理解这些特性对于设计和解释机器学习模型与算法至关重要。

**社区讨论**: 社区评论非常积极，用户赞扬该书聚焦于高维直觉和统计基础。一位评论者强调，在教授数据科学时，解释高维空间中直觉的失灵至关重要。另一位指出，统计学仍然是数据科学家最重要的技能，远超时髦的工具。整体讨论反映出一种共识，即扎实的数学和统计基础对于实用的数据科学不可或缺。

**标签**: `#data-science`, `#mathematics`, `#machine-learning`, `#statistics`, `#high-dimensional-geometry`

---

<a id="item-6"></a>
## [Roc 编译器从 Rust 到 Zig 重写的进展](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

作者报告了将 Roc 编译器从 Rust 重写为 Zig 的进展，指出性能提升、更简单的内存管理以及更快的增量构建。 此举突显了 Zig 在系统编程尤其是编译器领域日益增长的受欢迎程度，并重新引发了关于 Rust 的安全性与 Zig 的简洁性及编译速度之间权衡的辩论。 重写旨在加快开发周期，但牺牲了一些编译时的安全保障；作者承认在编译器开发中面临不安全代码和内存错误的挑战。

hackernews · jorangreef · 7月16日 11:39 · [社区讨论](https://news.ycombinator.com/item?id=48933149)

**背景**: Roc 是一门函数式编程语言，其编译器最初用 Rust 编写，Rust 以内存安全著称。Zig 是一种强调手动内存管理和快速编译的系统语言，常与 C 语言比较。Rust 通过所有权和借用机制在编译时确保安全，而 Zig 在调试和 ReleaseSafe 模式下依赖运行时检查，但提供的安全保障少于 Rust。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人认为编译器生成代码并不本质上需要不安全操作；另有人质疑 Zig 的 ReleaseSafe 模式是否真正捕捉到 use-after-free 错误。还有对为何不选择 OCaml 的好奇，并希望 Rust 最终能提供类似的快速增量构建。

**标签**: `#rust`, `#zig`, `#compilers`, `#programming-languages`, `#systems-programming`

---

<a id="item-7"></a>
## [具有互动图形的沉浸式线性代数书籍（2015 年）](https://immersivemath.com/ila/) ⭐️ 8.0/10

一本 2015 年的互动线性代数教科书，以其动态可视化效果获得了新的关注和赞誉，因其高效的教学方法而受到好评。 该资源展示了交互式、视觉优先的数学教育潜力，讨论还将其与可以加速此类内容创建的现代 AI 工具联系起来。 该书使用互动图形解释线性代数概念，并包含工具提示等功能；它创建于 2015 年，但依然清晰有效。

hackernews · srean · 7月16日 15:32 · [社区讨论](https://news.ycombinator.com/item?id=48935951)

**背景**: 线性代数是数学的一个分支，研究向量空间和线性映射，在工程、物理和计算机科学中广泛应用。像这样的互动教科书旨在通过视觉和动手探索来增强理解。

**社区讨论**: 社区反馈非常积极，用户对互动方法表现出热情，并希望在其他学科也能看到类似的书籍。有些用户指出 AI 的进步使得创建此类内容更加容易，还有用户建议添加对任何选中文本的‘解释这个’功能。

**标签**: `#linear-algebra`, `#education`, `#interactive-visualization`, `#math-education`, `#educational-technology`

---

<a id="item-8"></a>
## [Inkling：Thinking Machines Lab 发布的开源权重多模态 MoE 模型](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab 发布了 Inkling，这是一个 9750 亿参数的开源权重多模态专家混合模型，采用 Apache 2.0 许可，在 45 万亿文本、图像、音频和视频令牌上训练完成。同时，他们还计划发布一个更小的 2760 亿参数的 Inkling-Small 模型。 此次发布意义重大，因为一家知名的美国 AI 实验室贡献了一个大规模、宽松许可的开源权重模型，增强了美国开源 AI 生态系统，并为来自中国的开源权重模型（如 DeepSeek 等）提供了有竞争力的替代品。Apache 2.0 许可允许广泛的商业和研究用途，尤其适合通过其 Tinker 平台进行微调。 Inkling 采用专家混合架构，总参数量为 9750 亿，激活参数为 410 亿，是多模态模型，训练时使用了 45 万亿令牌。Thinking Machines Lab 承认它并非前沿模型；附带的模型卡远短于行业惯例，且提供了极少的训练数据细节。

rss · Simon Willison · 7月16日 15:35

**背景**: 专家混合（MoE）是一种 Transformer 架构，包含多个“专家”子网络，并通过门控机制将每个 token 路由到少数几个专家，从而实现高效扩展。AI 模型卡是标准化的文档，详细记录了模型的能力、训练数据和性能，以确保透明度。Thinking Machines Lab 提供的文档相对稀疏，与行业惯例形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer">Mixture - of - Experts Transformer</a></li>
<li><a href="https://developer.nvidia.com/blog/enhancing-ai-transparency-and-ethical-considerations-with-model-card/">Enhancing AI Transparency and Ethical Considerations with Model ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#model-release`, `#multimodal`, `#mixture-of-experts`, `#LLM`

---

<a id="item-9"></a>
## [Linus Torvalds：Linux 不反 AI，AI 是有用的工具](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 的最高维护者 Linus Torvalds 在 Linux 媒体邮件列表中公开声明，Linux 不是一个反 AI 的项目，并认为 AI 是一种有用的工具，邀请不同意的人分叉项目或离开。 这一声明明确了 Linux 项目对 AI 的官方立场，会影响开源文化，并可能加速 AI 在软件开发中的应用。它向社区传递了 AI 工具在 Linux 开发中受到欢迎的信号，可能会影响贡献和更广泛的生态系统。 Torvalds 强调 AI 的有用性已不再有疑问，并指出虽然其经济影响尚不明朗，但任何怀疑其实用性的人显然都没有使用过它。这些言论是在回应 Linux 媒体邮件列表上的讨论时发表的。

rss · Simon Willison · 7月16日 13:26

**背景**: Linux 是全球使用最广泛的开源操作系统，自诞生以来由 Linus Torvalds 领导。作为最高维护者，Torvalds 为内核设定愿景。近来，一些开源项目采取了反 AI 的立场，但 Torvalds 的声明表明 Linux 将 AI 作为一种工具予以接纳，反映了他对技术的务实态度。

**标签**: `#Linux`, `#AI`, `#open-source`, `#Linus Torvalds`, `#software development`

---

<a id="item-10"></a>
## [xAI 在数据上传争议后开源 Grok Build](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 8.0/10

xAI 在社区对 CLI 工具未经同意上传整个用户目录的强烈不满后，以 Apache 2.0 许可证发布了整个 Grok Build 代码库，包含 844,530 行 Rust 代码。 这一透明举措旨在重大隐私泄露事件后恢复用户信任，为 AI 编程工具的开源问责制树立新标准，并允许用户在本地运行该工具。 代码库包含主系统提示、独立的终端 Mermaid 图表渲染器，以及模仿其他编程代理的工具实现；xAI 还删除了所有之前保留的用户数据，并禁用了默认保留。

rss · Simon Willison · 7月15日 23:59

**背景**: Grok Build 是 xAI 的一款用于“氛围编程”的 CLI 工具，可将自然语言提示转换为代码；争议的爆发源于人们发现，在目录中运行该工具可能会悄悄将目录中所有内容上传到 xAI 的云存储桶。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Grok_Build">Grok Build</a></li>
<li><a href="https://x.ai/open-source">Open Source: Grok Build Coding Agent & CLI | SpaceXAI</a></li>

</ul>
</details>

**社区讨论**: 用户对隐私侵犯立即表示愤怒，有人报告 SSH 密钥和密码数据库被上传；虽然部分用户欢迎开源和数据删除，但其他人对 xAI 之前处理敏感数据的方式仍持怀疑态度。

**标签**: `#open-source`, `#security`, `#xAI`, `#grok`, `#AI`

---

<a id="item-11"></a>
## [研究人员绕过 Claude 网页抓取防护实现数据窃取](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

安全研究员 Ayush Paul 发现了一种绕过 Claude 的 web_fetch 工具防护的方法，通过构造一个网站诱使 Claude 逐个字母泄露用户的私人信息，从而实现了数据窃取。 这凸显了 AI 智能体安全防护在现实世界中的漏洞，说明即使有明确的反窃取措施，防止提示注入攻击和数据泄露仍面临持续挑战。 攻击利用了 Claude 允许读取已抓取页面中的链接这一特性，通过伪装成 Cloudflare 认证提示，逐个字母提取了用户的姓名、所在地和雇主信息；该利用仅针对用户代理中包含“Claude-User”的请求，以躲避检测。

rss · Simon Willison · 7月15日 14:21

**背景**: 所谓的“致命三重奏”是指 AI 智能体同时具备以下三个条件时的危险组合：访问敏感数据、接触不可信输入、以及具备外部通信能力。Claude 的 web_fetch 工具通过限制只能浏览用户输入或 web_search 返回的精确 URL 来缓解这一风险，但该缺陷允许它浏览已抓取页面中的链接。此次攻击表明，坚定的攻击者仍能绕过此类安全措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>
<li><a href="https://www.osohq.com/learn/lethal-trifecta-ai-agent-security">Understanding the Lethal Trifecta of AI Agents</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>

</ul>
</details>

**标签**: `#security`, `#ai-safety`, `#claude`, `#data-exfiltration`, `#prompt-injection`

---

<a id="item-12"></a>
## [PnP-CoSMo：无需原始 k 空间数据的即插即用多对比度 MRI 重建框架](https://www.reddit.com/r/MachineLearning/comments/1uy2h66/pnpcosmo_a_multicontrast_mri_reconstruction/) ⭐️ 8.0/10

PnP-CoSMo 提出了一种两阶段即插即用框架，仅从图像域 MRI 数据中学习对比度不变的内容和风格表示，消除了对稀缺原始 k 空间训练数据的依赖。该框架在与最先进的展开网络竞争的同时，提供了内置的可解释性和跨对比度及前向算子的泛化能力。 该方法移除了 MRI 重建中的一个主要数据瓶颈，使先进的深度学习方法在原始 k 空间数据通常不可用的临床环境中更易获取和实用。其内置的可解释性和泛化能力可以加速临床应用并提升诊断质量。 该框架的第一阶段从配对的多对比度图像中建模内容和风格，无需原始 k 空间测量值；第二阶段冻结该模型，并将其作为先验用于迭代重建，支持灵活的欠采样模式和对比度组合。其性能与通常需要原始 k 空间数据进行端到端训练的展开网络相当。

reddit · r/MachineLearning · /u/void_gear · 7月16日 13:10

**背景**: 多对比度 MRI 捕捉不同的组织特性（如 T1、T2 加权）以辅助诊断；多对比度重建利用这些对比度之间的相关性，从欠采样数据中提高图像质量。即插即用方法将测量模型与图像先验解耦，允许将预训练的深度学习模型作为正则化器插入。展开优化网络将迭代算法展开为深度网络，并基于原始 k 空间数据进行端到端训练，但这类数据通常难以获得。PnP-CoSMo 通过仅从图像域数据学习先验，绕过了这一限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/39419362/">Deep plug-and-play MRI reconstruction based on multiple complementary priors - PubMed</a></li>
<li><a href="http://crl.med.harvard.edu/papers/Pouryazdanpanah_DeepPlug.pdf">Deep Plug-and-Play Prior for Parallel MRI Reconstruction</a></li>
<li><a href="https://arxiv.org/abs/2601.17274">Unrolled Neural Networks for Constrained Optimization</a></li>

</ul>
</details>

**标签**: `#MRI reconstruction`, `#content/style modeling`, `#plug-and-play framework`, `#medical imaging`, `#deep learning`

---

<a id="item-13"></a>
## [Schema 推理框架在 ARC-AGI-3 上达到 99% 准确率](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 8.0/10

名为 Schema 的新型推理框架在 ARC-AGI-3 公开数据集上使用 Claude Opus 4.8 和 Fable 5 取得了 99% 的成绩，且未修改模型权重。它通过改进观察、预测测试和执行计划的流程来提升性能。 这一结果表明，在旨在衡量通用智能的基准测试中，AI 智能体实现了高效推理的重大进展，凸显了推理时技术释放模型潜力的价值。 该框架采用固定的后备规则：先用 Opus 4.8/Sol xhigh 运行，对得分低于 80 分的游戏用 Fable 5/Sol max 重新运行，并保留较高分。它使用 GPT-5.6 Sol 时达到 95.35%。

reddit · r/MachineLearning · /u/we_are_mammals · 7月16日 21:02

**背景**: ARC-AGI-3 是一个交互式推理基准测试，要求 AI 智能体探索新环境、动态获取目标并构建可适应的世界模型。Claude Opus 4.8 和 Fable 5 是 Anthropic 开发的大语言模型，其中 Fable 5 是高级 Mythos 系列的公开版本。99% 的得分意味着智能体几乎可以像人类一样高效地通过所有游戏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fable_5">Fable 5</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#arc-agi`, `#benchmark`, `#harness`, `#llms`

---

<a id="item-14"></a>
## [Decoy 字体利用模糊效果揭示隐藏文字](https://www.mixfont.com/experiments/decoy-font) ⭐️ 7.0/10

来自 mixfont.com 的 Decoy 字体实验推出了一种 TrueType 字体，每个字符都包含隐藏信息，仅在文本模糊时才显现，利用了人类与 OCR 系统感知文本分辨率的差异。 这突显了人类视觉与基于 AI 的光学字符识别之间的重大感知差距，展示了对抗性扰动如何欺骗机器而对人类仍可读，凸显了自动化文本分析的脆弱性。 隐藏文本通过高频细节嵌入，模糊时平均化；GPT-4、Claude 和 Gemini 等 AI 模型识别不一致，简单的缩放或脚本即可改变 OCR 读取的内容。

hackernews · ray__ · 7月16日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48936584)

**背景**: 对抗性样本是指使机器学习模型出错而对人类不可察觉的输入扰动。在 OCR 中，此类扰动可包括误导识别的隐藏文本或噪声。Decoy 字体是这一概念的具体实现，包装为可用的 TrueType 字体，引发了关于 AI 视觉系统鲁棒性的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mixfont.com/experiments/decoy-font">Decoy Font: A TTF font that hides what you type - mixfont.com</a></li>
<li><a href="https://www.turbolens.io/blog/2025-12-20-watermarks-and-background-noise-a-silent-ocr-killer">Watermarks and Background Noise: A Silent OCR ... | TurboLens Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者认可其趣味性但质疑实用性，指出 AI 有时可通过提示读取隐藏文本，另一些人则认为这只是一个细节层次的小技巧，可通过基本图像处理破解。

**标签**: `#typography`, `#adversarial-examples`, `#ai-perception`, `#ocr`, `#experimental`

---

<a id="item-15"></a>
## [经典机器学习检测 LLM 生成文本方法探讨](https://blog.lyc8503.net/en/post/llm-classifier/) ⭐️ 7.0/10

一篇近期博客文章探讨了使用经典机器学习而非深度学习来识别 LLM 生成文本的方法，引发了关于其长期可行性和‘努力程度’等替代指标的讨论。 随着 LLM 生成内容充斥互联网，可靠检测对维护信息真实性至关重要，经典机器学习可能提供适合浏览器扩展的轻量级方案。然而，争议凸显了随着模型进化区分 AI 与人类文本的固有困难。 该分类器依赖当前 LLM 特有的句式结构和措辞特征，模型体积小，可部署于浏览器中。批评者认为这些特征是暂时的，检测如同塔罗占卜，未来模型将学会避免这些模式。

hackernews · uneven9434 · 7月16日 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48936880)

**背景**: 经典机器学习包括逻辑回归、支持向量机等传统算法，依赖手工设计特征，与自动学习特征的深度学习不同。AI 文本检测是持续的军备竞赛，早期检测器往往无法跨模型或领域泛化。

**社区讨论**: 社区成员对长期可行性表示怀疑，有人称之为‘塔罗占卜’，也有人建议衡量写作努力而非来源。另一些人持乐观态度，提议集成到浏览器扩展，并指出人类仍优于自动检测器。

**标签**: `#LLM detection`, `#classical machine learning`, `#AI-generated text`, `#community discussion`, `#NLP`

---

<a id="item-16"></a>
## [观鸟而非打高尔夫：将高尔夫球场变公园以省水](https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything) ⭐️ 7.0/10

西蒙·威利森幽默地建议，像谷歌这样的超大规模数据中心运营商可以通过购买高尔夫球场并将其改造成公园，同时推广观鸟活动来抵消其用水量；他估算谷歌 2025 年 109 亿加仑的用水量可通过收购科切拉谷约 40 个高尔夫球场来抵消。 该建议凸显了数据中心对环境影响的日益关注，特别是冷却用水，并巧妙地将此与高尔夫球场的过量用水联系起来，为可持续发展提供了引人深思的视角。 谷歌 2025 年用水 109 亿加仑，约合每天 3000 万加仑；科切拉谷每个高尔夫球场日耗水约 75 万加仑，因此 40 个球场的用水量相当于谷歌的消耗。不过该建议仅为讽刺，未考虑实际改建面临的诸多挑战。

rss · Simon Willison · 7月17日 02:58

**背景**: 超大规模数据中心运营商（hyperscaler）是指运营大规模数据中心的云服务巨头，如谷歌、亚马逊和微软，冷却需要消耗大量能源和水资源。在许多地区水资源匮乏，随着 AI 计算负载增加，数据中心的用水问题受到日益关注。高尔夫球场，尤其在干旱地区，也以耗水量大著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyperscaler">Hyperscaler</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#ai-energy-usage`, `#ai`, `#sustainability`, `#water-usage`, `#data-centers`

---

<a id="item-17"></a>
## [引用蒂博·索蒂奥](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

Codex AI 编程代理存在一个漏洞：在以完全访问权限运行且未启用沙盒时，可能意外删除文件。

rss · Simon Willison · 7月16日 17:45

**标签**: `#ai-safety`, `#coding-agents`, `#codex`, `#bug-report`, `#generative-ai`

---

<a id="item-18"></a>
## [Mermaid 图表在浏览器中渲染为 Unicode 框图艺术](https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything) ⭐️ 7.0/10

Simon Willison 创建了一个基于浏览器的工具，将 Mermaid 图语法转换为 Unicode 框图艺术，利用了来自 xAI 的 Grok 项目中的 Rust 代码编译为 WebAssembly。 该工具使图表能在终端和 Markdown 文件等纯文本环境中显示，展示了 Rust/WASM 用于 Web 渲染的实用性。 该工具使用原本为 Grok CLI 编写的自包含终端渲染器（Rust），编译为 WASM 后在浏览器中运行，无需服务器。

rss · Simon Willison · 7月16日 00:33

**背景**: Mermaid 是一种基于 JavaScript 的图表语言，可从文本描述生成图表。Unicode 框图字符是用于文本界面中绘制线条和框的符号。Rust 是一种系统编程语言，可编译为 WebAssembly，从而在 Web 浏览器中运行高性能代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mermaid_(software)">Mermaid (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Box-drawing_characters">Box -drawing characters - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mermaid`, `#webassembly`, `#rust`, `#terminal`, `#diagrams`

---

<a id="item-19"></a>
## [QLoRA 默认学习率 2e-4 在少于 1 万样本时导致过拟合](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 7.0/10

一位用户发现，普遍推荐的 QLoRA 学习率 2e-4 在样本数量少于 1 万的数据集上反复导致过拟合，将学习率降至 1e-4 能显著提升评估表现。 许多从业者使用小型自定义数据集微调大语言模型，盲目采用默认的 2e-4 学习率可能导致数周的工作徒劳无功；这一简单调整能节省时间并提升模型质量。 该用户发现，对于约 7000 个清洗后的样本，1e-4 配合 5 个 epoch 效果良好，而 2e-4 配合 3 个 epoch 则不行。经验法则：样本超过 3 万时 2e-4 可能没问题，少于 1 万时从 1e-4 或更低开始，介于两者之间则应调整学习率。

reddit · r/MachineLearning · /u/Pretty-Ad774 · 7月16日 12:50

**背景**: QLoRA（量化低秩适配）是一种使用 4-bit 量化和低秩适配器高效微调大语言模型的方法，大幅降低内存需求。2e-4 的学习率源自早期在包含 5.2 万样本的 Alpaca 数据集上的实验，但对于实践中常见的更小数据集并不适用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/QLoRA">QLoRA</a></li>
<li><a href="https://arxiv.org/abs/2305.14314">[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs</a></li>

</ul>
</details>

**标签**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#hyperparameter tuning`, `#small datasets`

---

<a id="item-20"></a>
## [利用哈达玛积聚类解耦卷积神经元](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 7.0/10

一种新方法对 InceptionV1 中 1x1 卷积神经元的感受野和权重进行哈达玛积聚类，揭示了清晰的单语义簇（汽车、猫、狗）和多语义低值簇，并表明梯度下降可能有意将模式分布到不同神经元以抑制激活。 这为机械可解释性提供了更精细的工具，有助于理解单个神经元如何表征特征，有望提升 AI 安全与透明度。其当前局限是仅适用于卷积架构。 该技术计算输入感受野与神经元权重的哈达玛积，以捕捉神经元“所见”内容，随后对其进行聚类。低激活簇显示相连神经元也在相关概念上同步放电，暗示梯度下降有意注入了噪声。

reddit · r/MachineLearning · /u/narang_27 · 7月15日 06:59

**背景**: 机械可解释性旨在通过分析内部电路来逆向工程神经网络。关键挑战是多语义性，即单个神经元会对多个无关概念产生响应。哈达玛积是矩阵元素相乘；将神经元权重与其输入感受野进行哈达玛积可分离出被检测的模式。对这些积进行聚类能够将神经元的激活解耦为单语义特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polysemanticity">Polysemanticity - Wikipedia</a></li>
<li><a href="https://transformer-circuits.pub/2023/monosemantic-features/index.html">Towards Monosemanticity: Decomposing Language Models With ...</a></li>

</ul>
</details>

**标签**: `#mechanistic-interpretability`, `#convolutional-neural-networks`, `#feature-visualization`, `#clustering`, `#AI-safety`

---

<a id="item-21"></a>
## [PyTorch 模型在 T4 上比 A100 慢 170 倍：极端瓶颈调试](https://www.reddit.com/r/MachineLearning/comments/1ux6a9x/pytorch_model_running_170x_slower_on_t4_vs_a100/) ⭐️ 7.0/10

一位用户报告，在 NVIDIA T4 GPU 上运行点跟踪 PyTorch 模型时，相比 A100 慢了 170 倍，已排除简单配置错误，正在寻求性能分析建议。 这一极端瓶颈凸显了 GPU 架构限制（如内存带宽和缺乏 FP32 张量核心加速）如何严重拖累性能，为机器学习从业者提供了宝贵案例。 该模型使用了 4D 相关体和 Transformer 层，均为内存和计算密集型操作；T4 的 320 GB/s 带宽对比 A100 的 2 TB/s，加上缺乏 FP32 张量核心加速，可能是导致减速的原因。

reddit · r/MachineLearning · /u/Future-Structure-296 · 7月15日 13:44

**背景**: 4D 相关体（源自 Extreme Rotation 论文）计算两幅图像所有像素对之间的密集特征相似度，生成 H×W×H′×W′大小的张量，极其耗费内存。A100 提供 2.0 TB/s 内存带宽和 312 TFLOPS 的 FP16 算力，而 T4 仅有 320 GB/s 内存带宽，且缺乏硬件加速的 FP32 矩阵计算，因此不适合此类工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ruojincai.github.io/ExtremeRotation/">Extreme Rotation Estimation using Dense Correlation Volumes</a></li>
<li><a href="https://cloudgputracker.com/compare/nvidia-a100-vs-nvidia-t4/">NVIDIA A100 80GB vs NVIDIA T4 Comparison - cloudgputracker.com</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#GPU Performance`, `#Deep Learning`, `#Debugging`, `#NVIDIA T4 vs A100`

---

<a id="item-22"></a>
## [研究者寻求合作者以扩展并评估新型循环架构 DABSN](https://www.reddit.com/r/MachineLearning/comments/1uycffg/seeking_collaborators_for_scaling_and_independent/) ⭐️ 6.0/10

一位独立研究者发布了新型循环神经网络架构 DABSN（动态自适应偏置状态网络）的预印本和开源代码，并使用 GPT-2 分词器在 10 亿个 token 上训练了一个 2400 万参数的语言模型，在长序列和推理基准测试中展现了有希望的结果。 这项工作可能为高效长上下文语言建模提供一种替代 Transformer 的模型，公开寻求合作的呼吁有望加速独立验证和规模扩展，惠及更广泛的机器学习研究社区。 该架构在 MQAR、Copy、键值检索和 A5/60 等合成推理与记忆基准上进行了评估。代码包含 PyTorch、C++和 Triton 实现，作者正在准备第二篇论文，重点关注语言建模和长上下文行为。

reddit · r/MachineLearning · /u/BleedingXiko · 7月16日 19:17

**背景**: 循环神经网络（RNN）通过逐步处理序列并维护隐藏状态，对于长序列可能比 Transformer 更节省内存。最近，Mamba 和 RWKV 等架构重新激发了人们对循环模型在语言任务中的兴趣。MQAR（多查询联想回忆）等基准测试用于评估模型在长上下文中关联和回忆信息的能力，这是语言理解的关键要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2312.04927">[2312.04927] Zoology: Measuring and Improving Recall in ... GitHub - HazyResearch/zoology: Understand and test language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com Zoology (Blogpost 1): Measuring and Improving Recall in ... Published as a workshop paper at SCOPE - ICLR 2025 - OpenReview Understanding Input Selectivity in Mamba: Impact on ...</a></li>
<li><a href="https://github.com/HazyResearch/zoology">GitHub - HazyResearch/zoology: Understand and test language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com Zoology (Blogpost 1): Measuring and Improving Recall in ... Published as a workshop paper at SCOPE - ICLR 2025 - OpenReview Understanding Input Selectivity in Mamba: Impact on ...</a></li>

</ul>
</details>

**标签**: `#Recurrent Neural Networks`, `#Language Models`, `#Architecture`, `#Long-Context`, `#Collaboration`

---

<a id="item-23"></a>
## [ECCV 高昂注册费引发学生不满](https://www.reddit.com/r/MachineLearning/comments/1uxyd6z/why_is_eccv_so_insanely_expensive_for_students/) ⭐️ 6.0/10

一位 Reddit 用户反映，ECCV 要求论文宣讲者支付 805 美元的全额注册费，而不是 440 美元的学生价，且其旅行资助申请均被拒绝。 这一问题凸显了学生研究者面临的经济负担，可能阻碍他们展示工作和学术交流，尤其是缺乏机构支持的学生。 ECCV 学生早鸟注册费为 440 美元，但论文宣讲者无法享受此费率，必须支付 805 美元；旅行资助和费用豁免竞争激烈，常被拒绝。

reddit · r/MachineLearning · /u/NotGondor · 7月16日 09:55

**背景**: ECCV 是计算机视觉领域的顶级双年会。与许多顶级会议一样，它收取注册费以覆盖成本，通常要求演讲作者按全额费率注册。旅行资助名额有限，根据需求和成绩授予。

**标签**: `#academia`, `#conference-fees`, `#machine-learning`, `#student-concerns`, `#ECCV`

---

<a id="item-24"></a>
## [AI 记忆系统应从存储事实转向推断用户推理模式](https://www.reddit.com/r/MachineLearning/comments/1uy6yht/are_current_ai_memory_architectures_optimizing/) ⭐️ 6.0/10

一篇新的概念性文章提出，AI 记忆架构应超越存储用户的描述性事实，转而持续优化持久上下文，以推断更高层次的模式，例如反复出现的解释框架和典型的推理风格。 这一转变可能使 AI 系统更深入地理解用户，从而实现更个性化、更具情境感知的交互，并与人类记忆的认知科学模型相一致。 该文章缺乏技术实现细节和实证验证，但提出了根本性问题：当前的记忆、检索和摘要方法是否足够，还是需要全新的架构。

reddit · r/MachineLearning · /u/Boris_Ljevar · 7月16日 16:00

**背景**: 当前的 AI 记忆系统通常使用对话摘要、用户偏好存储和检索增强生成等技术来维持上下文。AI 中的认知架构，如 ACT-R 和 SOAR，为模拟类人推理和记忆提供了框架。该文章从这些领域汲取灵感，建议 AI 记忆应从简单的事实保留演变为对用户特定认知模式的建模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/IAAR-Shanghai/Awesome-AI-Memory">IAAR-Shanghai/Awesome-AI-Memory - GitHub</a></li>
<li><a href="https://zylos.ai/research/2026-04-05-ai-agent-memory-architectures-persistent-knowledge/">AI Agent Memory Architectures: From Context Windows to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_architecture">Cognitive architecture</a></li>

</ul>
</details>

**标签**: `#AI Memory`, `#Cognitive Architectures`, `#Personalization`, `#Contextual AI`, `#Abstraction`

---

<a id="item-25"></a>
## [ExTernD 提出扩展秩三元分解以实现近乎无损的 LLM 量化](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 6.0/10

ExTernD 提出一种后训练量化方法，将每个 LLM 权重矩阵分解为两个三元矩阵和一个对角缩放矩阵，通过调整内部秩，在显存仅略增的情况下实现近乎无损的精度。 该方法可利用无乘法的三元运算实现极高效的 LLM 推理，同时保持模型精度，有望降低硬件需求和能耗。 该方法避开了固定大小三元量化的死胡同；内部秩为精度与显存的权衡提供了可调参数。核心贪心分解算法已在 GitHub 开源。

reddit · r/MachineLearning · /u/LMTLS5 · 7月16日 13:31

**背景**: 三元量化将权重量化为{-1,0,1}，可实现无乘法推理。后训练量化（PTQ）在训练后压缩模型而无须重新训练。矩阵分解技术如秩分解将矩阵拆分为更小分量，实现灵活的低秩近似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13511">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ...</a></li>
<li><a href="https://github.com/LMTLS5/ternary-decomposition">GitHub - LMTLS5/ ternary - decomposition · GitHub</a></li>
<li><a href="https://docs.pytorch.org/TensorRT/tutorials/ptq.html">Post Training Quantization ( PTQ ) — Torch-TensorRT...</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#LLM Quantization`, `#Ternary Networks`, `#Model Compression`, `#Research Preprint`

---

<a id="item-26"></a>
## [Reddit 用户寻求对 JEPA 世界模型在机器人学习中应用的批判性意见](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 6.0/10

一位研究机器人学习领域世界模型的 Reddit 用户正积极寻求反对者，以揭示联合嵌入预测架构（JEPA）方法的潜在缺点和风险，因为该用户认为目前的叙述过于积极。 这反映了在 AI 研究中平衡审查的需求日益增长，尤其是当像 Yann LeCun 这样的有影响力人物倡导 JEPA 优于大语言模型和强化学习等主流范式时，这可能影响未来的机器人和 AI 发展方向。 该用户阅读了 LeCun 和其他研究小组的最新论文，注意到 LeCun 对其他方法的否定，并宣传 JEPA 是“唯一的下一个大事件”，特别询问了在机器人学习领域中与其他世界模型方法相比的缺点。

reddit · r/MachineLearning · /u/Amazing-Coat5160 · 7月15日 17:34

**背景**: JEPA（联合嵌入预测架构）是一种自监督学习方法，预测抽象的潜在表征而非像素级重建，旨在构建内部世界模型。AI 中的世界模型是使智能体能够模拟环境的预测模型，对于样本高效的机器人学习至关重要。著名 AI 研究员 Yann LeCun 提出 JEPA 作为实现更像人类学习的途径，与生成模型（如大语言模型）形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/">I-JEPA: The first AI model based on Yann LeCun’s vision for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Joint_Embedding_Predictive_Architecture">Joint Embedding Predictive Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#JEPA`, `#world models`, `#robot learning`, `#AI critique`, `#LeCun`

---