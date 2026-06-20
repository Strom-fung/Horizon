---
layout: default
title: "Horizon Summary: 2026-06-20 (ZH)"
date: 2026-06-20
lang: zh
---

> 从 21 条内容中筛选出 13 条重要资讯。

---

1. [Valhalla 项目值类型在 JDK 28 中落地](#item-1) ⭐️ 9.0/10
2. [ATProto 中没有实例概念](#item-2) ⭐️ 8.0/10
3. [挪威禁止低龄学生用 AI，仅允许青少年在监督下使用](#item-3) ⭐️ 8.0/10
4. [初级工程师因潜力被聘用，而非仅完成任务](#item-4) ⭐️ 8.0/10
5. [HN 热议：为保护儿童推行全网实名制的影响](#item-5) ⭐️ 8.0/10
6. [法庭记录应免费公开](#item-6) ⭐️ 8.0/10
7. [Rust cuTile 实现安全 GPU 内核，快速 LLM 推理](#item-7) ⭐️ 8.0/10
8. [《毁灭战士》等经典游戏作曲家 Bobby Prince 逝世](#item-8) ⭐️ 7.0/10
9. [Datasette Apps：嵌入自定义 HTML/JS 应用并访问 SQL 数据](#item-9) ⭐️ 7.0/10
10. [微型 Python 实现揭示 torch.compile 算子融合加速原理](#item-10) ⭐️ 7.0/10
11. [对话层调试揭示基准测试无法捕捉的语音 AI 缺陷](#item-11) ⭐️ 7.0/10
12. [现代汽车完全控股波士顿动力](#item-12) ⭐️ 6.0/10
13. [datasette-acl 0.6a0 为 Datasette 增加通用资源共享功能](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Valhalla 项目值类型在 JDK 28 中落地](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 9.0/10

经过十余年开发，Valhalla 项目的值类型终于在 JDK 28 中交付，引入能够结合面向对象抽象与原生类型性能的值对象。 这一增强可以显著提高数据结构的存储效率并减轻垃圾回收压力，使 Java 能够更好地在高性能计算和系统编程领域竞争。 通过 `value` 修饰符声明的值类定义不可变且无对象标识的实例；JVM 可在内存中将其展开布局，但对大于 64 位的类型堆展开可能受限，并可能使用空标记。

hackernews · philonoist · 6月19日 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: Valhalla 项目由 Oracle 于 2014 年启动，旨在通过值类型和泛型特化增强 JVM。目前，所有 Java 对象都带有对象头和堆分配开销；值类型取消了对象头和指针，像原生类型一样直接存储数据，这对性能敏感应用至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://openjdk.org/projects/valhalla/">Project Valhalla</a></li>
<li><a href="https://openjdk.org/projects/valhalla/value-objects">Value Classes and Objects - OpenJDK</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：部分人称赞这个期待已久的功能，而另一些人则争论技术细节，如堆展开限制和空安全的思维复杂性。许多人指出，外界往往低估了现代 Java 的能力及其活跃的演进。

**标签**: `#java`, `#jvm`, `#project-valhalla`, `#value-types`, `#jdk-28`

---

<a id="item-2"></a>
## [ATProto 中没有实例概念](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 8.0/10

这篇文章澄清了 ATProto 的架构不同于 Mastodon 的实例模型，它采用个人数据服务器(PDS)、中继(Relay)和应用视图(AppView)分离的设计，没有‘实例’的概念。 这一澄清有助于开发者和用户正确理解 ATProto 的去中心化设计，消除常见误解，促进生态发展，并对比不同协议的系统设计思路。 具体而言，PDS 托管用户数据，Relay 汇总多个 PDS 的数据提供 firehose，AppView 消费这些数据呈现特定应用；Relay 内容无关，架构解耦，各组件可独立扩展，但运行 Relay 成本较高。

hackernews · danabramov · 6月19日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: 在 Mastodon 等基于 ActivityPub 的社交网络中，‘实例’是运行特定软件、拥有独立用户和规则的服务器，用户需选择实例。ATProto 则采用模块化架构，将存储、聚合和展示分离，从而实现更高的可扩展性和用户数据可移植性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews - AT Protocol Community Wiki</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有人赞同文章清晰解释了两者差异，但也有人指出文章对 RSS 的类比有缺陷，并质疑 ATProto 中 AppView 严重依赖 Relay 的成本和可行性，此外还讨论了该协议如何解决实例中封禁等问题的替代方案。

**标签**: `#atproto`, `#bluesky`, `#decentralization`, `#activitypub`, `#protocols`

---

<a id="item-3"></a>
## [挪威禁止低龄学生用 AI，仅允许青少年在监督下使用](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/) ⭐️ 8.0/10

挪威政府宣布，原则上禁止 6 至 13 岁的小学生使用 AI，而 14 至 16 岁的初中生可在教师监督下谨慎使用。 该政策强调了保护儿童基础认知发展免受生成式 AI 潜在危害的重要性，引发了关于学校适龄技术使用的全球讨论。 禁止范围涵盖 6 至 13 岁学生使用的所有 AI 工具，14 至 16 岁学生仅在教师直接监督下才可使用，政府承认执行存在困难。

hackernews · ilreb · 6月19日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48600093)

**背景**: 生成式 AI 工具（如 ChatGPT）能够生成类似人类的文本并完成复杂任务，但其易用性可能阻碍儿童为发展读写和推理能力所必需的心智锻炼。关于 AI 在教育中的争论，与过去关于向低龄学生引入计算器可能阻碍基础学习的讨论类似。该政策是各国寻求监管学校 AI 使用、在创新与儿童保护之间取得平衡的广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_AI">Generative AI</a></li>

</ul>
</details>

**社区讨论**: 社区普遍支持这一禁令，许多人将其与在掌握基本算术之前不提供计算器的做法相类比。教育工作者指出 AI 已经降低了学生成绩，一些人甚至质疑小学课堂是否需要 AI。不过，也有评论强调执行面临挑战，有效实施可能需要重新设计作业和评估方式。

**标签**: `#AI in education`, `#policy`, `#child development`, `#technology regulation`, `#generative AI`

---

<a id="item-4"></a>
## [初级工程师因潜力被聘用，而非仅完成任务](https://newsletter.kentbeck.com/p/hey-n00b-we-didnt-hire-you-to-complete) ⭐️ 8.0/10

Kent Beck 发表文章主张应根据长期潜力和影响力而非立即的任务完成度来聘用和评估初级工程师，引发了社区的广泛辩论。 这一观点挑战了优先考虑短期生产力的传统科技招聘做法，可能促使团队转向注重长期成长的方式来指导培养初级人才。 文章将工程师分为 A（高潜力）、B（稳定）和 C（低潜力）类，建议新人需要时间成长。社区评论指出现代频繁跳槽和 LLM 的发展可能削弱这种长期投资模式。

hackernews · rrvsh · 6月20日 00:11 · [社区讨论](https://news.ycombinator.com/item?id=48604851)

**背景**: Kent Beck 是著名软件工程师和极限编程的创始人。这篇文章反映了工程管理中当前生产力与培养未来人才之间的持续矛盾。

**社区讨论**: 社区评论大多持批评态度，认为分类方法过于简化，现实中公司常因低成本完成任务而招聘初级工程师，而非长期培养。另有人指出短暂工作任期和 LLM 的兴起使该模式过时。

**标签**: `#software engineering`, `#career development`, `#hiring`, `#team dynamics`, `#management`

---

<a id="item-5"></a>
## [HN 热议：为保护儿童推行全网实名制的影响](https://nochan.net/b/Internet-Crap/20230829-Think-Of-The-Children/) ⭐️ 8.0/10

2023 年 8 月，一篇主张以保护儿童为由对所有互联网流量强制实行真实身份验证的文章在 Hacker News 引发热议，讨论涉及隐私和技术可行性。 该提议威胁网络匿名性和言论自由，可能将政府监控常态化并限制信息获取；反映了儿童安全立法与数字公民自由之间日益加剧的矛盾。 评论者提出用去中心化的无线电中继网络作为对抗实名制的最后防线，指出现有 RTA-5042 等元标签已用于内容分级，并警告实名制将导致类似 KYC 的自我审查和算法合规，以 PayPal 的过度监管为例。

hackernews · Bender · 6月19日 20:19 · [社区讨论](https://news.ycombinator.com/item?id=48602817)

**背景**: 全球多国政府正推动年龄验证和数字身份制度，以遵守在线儿童安全法，类似于线下身份检查。这引发了对大规模监控和言论自由寒蝉效应的担忧。该争论呼应了自早期数字出版许可概念以来关于网络匿名性的长期辩论，并催生了去中心化网络等替代方案。

**社区讨论**: 社区普遍反对强制实名制，认为其是滑向审查和监控的滑坡。许多人提出通过网状网络或家长控制来规避，部分人引用《数字出版许可》等历史警示。少数人指出 RTA-5042 等现有分级系统已能在不牺牲匿名性的情况下保护儿童。

**标签**: `#privacy`, `#internet-regulation`, `#age-verification`, `#digital-identity`, `#hackernews-discussion`

---

<a id="item-6"></a>
## [法庭记录应免费公开](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free) ⭐️ 8.0/10

电子前哨基金会 (EFF) 发表文章，主张美国公共法庭记录应免费获取，批评 PACER 系统的按页收费阻碍了公众查阅法律文件。 免费获取法庭记录对政府透明度、公平司法和公众监督司法机构至关重要；PACER 的高昂费用对无力承担者影响尤甚。 PACER 目前对联邦法庭记录每页收费 0.10 美元，每份文件收费上限为 3 美元，而部分州法院收费更高（如爱达荷州每页 10 美元）；RECAP 工具可自动将购买的文件共享至 CourtListener 供免费查阅。

hackernews · hn_acker · 6月19日 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600946)

**背景**: PACER（公共法庭电子记录访问系统）是美国联邦法院在线查阅案件与案卷信息的系统，主要依靠用户收费维持运营。电子前哨基金会（EFF）是一家倡导数字权利和政府透明度的非营利组织。关于 PACER 收费的争论是推动政府公共记录开放运动的一部分，主张此类记录应由纳税人资助并免费公开。

**社区讨论**: 评论者强调 PACER 收费的负担，有人指出爱达荷州法院记录每页收费 10 美元。一些人将其比作其他公共产品资助难题，同时赞扬 RECAP 等工具改善了访问。整体情绪支持法庭记录免费，但少数人也承认系统融资的实际挑战。

**标签**: `#open-access`, `#government-transparency`, `#legal-tech`, `#public-policy`, `#PACER`

---

<a id="item-7"></a>
## [Rust cuTile 实现安全 GPU 内核，快速 LLM 推理](https://www.reddit.com/r/MachineLearning/comments/1u9j7md/fearless_concurrency_on_the_gpu_safe_gpu/) ⭐️ 8.0/10

cuTile Rust 的维护者发布了一篇论文，展示了一种基于 Rust 的 tile 化 GPU 编程模型，该模型利用 Rust 的所有权机制，在编译期保证内存安全和数据竞争自由。基于此构建的 Grout 推理引擎在 RTX 5090 上对 Qwen3-4B 实现 171 tok/s，在 B200 上对 Qwen3-32B 实现 82 tok/s，性能可与 vLLM 和 SGLang 相媲美。 这满足了日益增长的对可信 GPU 代码的需求，尤其是随着 AI 生成内核的普及。编译器验证的安全性消除了整类错误，有望加速高性能机器学习系统的开发。 cuTile 采用基于 tile 的模型，将输出张量划分为不相交的可变子张量，确保单线程语义并映射到线程块。安全的 GEMM 性能与手写版本相差不到 0.3%，但当前 Grout 引擎仅支持 batch-1，模型有限，且仅适用于 NVIDIA GPU。

reddit · r/MachineLearning · /u/Exciting_Suspect9088 · 6月18日 21:36

**背景**: 传统 GPU 编程（如 CUDA C++）需要手动管理内存和同步，容易引发数据竞争和内存错误。Rust 的所有权模型可在编译期预防此类问题。'Tile 化'编程将计算拆分为可并行处理的独立 tile。CUDA Tile IR 是 NVIDIA 为 tile 操作设计的底层中间表示。cuTile Rust 将安全的 Rust 代码编译至此 IR。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVlabs/cutile-rs">GitHub - NVlabs/cutile-rs: cuTile Rust provides a safe, tile-based ...</a></li>
<li><a href="https://nvlabs.github.io/cutile-rs/main/">cuTile Rust — cuTile Rust - nvlabs.github.io</a></li>
<li><a href="https://docs.nvidia.com/cuda/tile-ir/latest/">Tile IR — Tile IR</a></li>

</ul>
</details>

**标签**: `#GPU`, `#Rust`, `#memory-safety`, `#concurrency`, `#inference-engine`

---

<a id="item-8"></a>
## [《毁灭战士》等经典游戏作曲家 Bobby Prince 逝世](https://www.legacy.com/legacy/robert-bobby-prince-lll) ⭐️ 7.0/10

以《毁灭战士》、《德军总部 3D》和《毁灭公爵 3D》等经典第一人称射击游戏配乐闻名的作曲家鲍比·普林斯（Bobby Prince）近日去世。消息在 Legacy.com 上公布后，游戏社区纷纷致以哀悼。 他的重金属风格配乐对于营造早期第一人称射击游戏的沉浸感至关重要，影响了无数玩家和作曲家。他的离世是游戏音乐史上的重大损失。 除了作曲，普林斯还为《毁灭战士》制作了包括开门声和怪物咆哮在内的众多音效。他的风格深受 Pantera、Slayer 和 Judas Priest 等金属乐队影响，常在 MIDI 中再现其吉他旋律。

hackernews · pgrote · 6月19日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=48602352)

**背景**: 《毁灭战士》、《德军总部 3D》和《毁灭公爵 3D》是 20 世纪 90 年代初发布的里程碑式第一人称射击游戏，定义了该类型。受当时硬件限制，游戏音乐多采用 MIDI 格式，普林斯是将重金属与摇滚风格融入游戏配乐的先驱，其作品大大增强了游戏的沉浸感。

**社区讨论**: 粉丝们哀悼一位‘绝对的传奇’，回忆起《德军总部 3D》难忘的旋律和《毁灭战士》极具影响力的音乐。有人表示普林斯的 MIDI 文件让他们认识了金属乐队，还有网友在得知他制作了《毁灭战士》音效后表示惊讶。

**标签**: `#obituary`, `#video-game-music`, `#doom`, `#gaming-history`, `#composer`

---

<a id="item-9"></a>
## [Datasette Apps：嵌入自定义 HTML/JS 应用并访问 SQL 数据](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了 datasette-apps 插件，允许用户在 Datasette 实例中通过沙盒化的 iframe 直接嵌入独立的 HTML 和 JavaScript 应用，并能通过只读 SQL 查询访问数据，还可通过存储查询启用写入操作。 该插件大幅扩展了 Datasette 的扩展性，使开发者能直接在 Datasette 内构建自定义的交互式数据工具和仪表盘，减少对外部前端的需求，并优化数据探索和发布的流程。 应用在带有 sandbox='allow-scripts allow-forms' 的 iframe 中隔离运行，并通过内容安全策略（CSP）阻止外部 HTTP 请求以防数据泄露。插件添加了细粒度的应用管理权限，且不依赖大型语言模型，但可托管由 LLM 生成的应用。

rss · Simon Willison · 6月18日 23:58

**背景**: Datasette 是一个开源工具，用于将 SQLite 数据库作为交互式网站和 API 进行探索和发布，拥有丰富的插件生态。以往自定义界面通常需通过 Datasette 的 JSON API 单独构建，现在 datasette-apps 插件可直接在 Datasette 内部托管这些界面。其沙盒模型借鉴了 Claude Artifacts，即一种生成交互式 HTML 内容的 AI 功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps: Host custom HTML applications inside Datasette</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-apps/">Host applications inside Datasette with Datasette Apps - Datasette Blog</a></li>
<li><a href="https://pypi.org/project/datasette-apps/">Create apps that live inside Datasette</a></li>

</ul>
</details>

**标签**: `#datasette`, `#plugins`, `#javascript`, `#sql`, `#web-applications`

---

<a id="item-10"></a>
## [微型 Python 实现揭示 torch.compile 算子融合加速原理](https://www.reddit.com/r/MachineLearning/comments/1ua2hwj/how_does_torchcompile_achieve_massive_speedups/) ⭐️ 7.0/10

一位开发者发布了一个仅 500 行的微型 Python 实现和配套 Notebook，演示 torch.compile 如何通过算子融合技术，在高度优化的 NumPy 函数基础上实现大幅加速。 该教育资源揭开了深度学习框架核心优化技术的神秘面纱，帮助从业者和学生理解编译如何减少内存和计算开销，可能影响未来的模型性能调优。 该项目包含一个约 500 行的微型 torch.compile Python 实现和 Jupyter Notebook，重点展示了算子融合技术，将多个操作合并为单一内核以避免冗余内存访问。

reddit · r/MachineLearning · /u/Other-Eye-8152 · 6月19日 13:47

**背景**: torch.compile 是 PyTorch 2.0 中引入的即时编译器，可自动优化深度学习模型。它使用算子融合等技术，将多个独立操作（例如线性层后接 ReLU）合并为单个 GPU 内核，从而省去将中间结果存储到全局内存的步骤，降低延迟并减少内存带宽占用。相较于像 NumPy 这类逐函数执行的即时执行框架，这一改进尤为显著。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html">Introduction to torch.compile — PyTorch Tutorials 2.12.0+cu130 documentation</a></li>
<li><a href="https://grokipedia.com/page/Kernel_fusion">Kernel fusion</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#PyTorch`, `#compilation`, `#optimization`, `#tutorial`

---

<a id="item-11"></a>
## [对话层调试揭示基准测试无法捕捉的语音 AI 缺陷](https://www.reddit.com/r/MachineLearning/comments/1u99fe5/voice_debugging_at_the_conversation_level_seems/) ⭐️ 7.0/10

作者报告称，对话层级的语音调试揭示了多轮交互中的涌现性失败——例如累积的时序错误和生硬的轮流对话——这些是语音识别准确率、任务完成率等孤立基准指标无法捕捉的。 这凸显了对话式 AI 评估中的关键缺口，表明生产系统可能通过了基准测试，却提供了糟糕的用户体验。这或许会推动行业转向更整体、以交互为中心的测试方法。 具体的涌现问题包括小微时间错误的累积、重复确认引发摩擦，以及略带生硬的轮流对话改变用户行为。作者目前正使用自动化的对话层质量评估来扩大分析规模。

reddit · r/MachineLearning · /u/OwlZealousideal4779 · 6月18日 15:29

**背景**: 传统的语音 AI 基准测试通常衡量语音识别（STT）准确率、延迟和任务完成率等孤立组件。然而，在多轮对话中，整体体验取决于时序、轮流说话和确认策略之间的复杂交互。涌现性失败指由系统组件之间的相互作用而非单一模块错误引发的问题。

**标签**: `#voice AI`, `#conversational AI`, `#evaluation metrics`, `#debugging`, `#multi-turn interactions`

---

<a id="item-12"></a>
## [现代汽车完全控股波士顿动力](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) ⭐️ 6.0/10

现代汽车以 3.25 亿美元从软银手中收购了波士顿动力剩余 9%的股份，从而完全控制了这家机器人公司。此次收购完成了始于 2020 年的交易，当时现代汽车以 8.8 亿美元收购了 80%的股份。 此举彰显了现代汽车对超越汽车制造的先进机器人技术的战略承诺，有望应对未来的劳动力短缺并扩展到通用机器人领域，同时也凸显了动态仿生机器人在工业和消费市场中不断增长的商业价值。 此次交易通过 2020 年协议中的看跌期权完成，剩余股份价值 3.25 亿美元。波士顿动力以 Spot 和 Atlas 等机器人闻名，但其商业可行性仍存疑问。

hackernews · ck2 · 6月19日 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48600312)

**背景**: 波士顿动力公司成立于 1992 年，是麻省理工学院的衍生公司，专注于受动物运动启发的动态机器人。它之前是国防承包商，并于 2019 年推出了首款商业机器人 Spot。现代汽车最初在 2020 年收购了控股权，作为其向机器人和移动出行领域进军的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Boston_Dynamics">Boston Dynamics</a></li>

</ul>
</details>

**社区讨论**: 评论反映了不同观点：一些人认为这笔交易在意料之中，另一些人则质疑人形机器人相较于专用设计的实用性。还有人对韩国的人口挑战所扮演的角色进行推测，并对先进机器人短期内进入家庭持怀疑态度。

**标签**: `#robotics`, `#acquisition`, `#Hyundai`, `#BostonDynamics`, `#SoftBank`

---

<a id="item-13"></a>
## [datasette-acl 0.6a0 为 Datasette 增加通用资源共享功能](https://simonwillison.net/2026/Jun/18/datasette-acl/#atom-everything) ⭐️ 6.0/10

datasette-acl 0.6a0 由 Alex Garcia 主导开发，将插件从仅针对表的权限管理扩展为面向多用户 Datasette 实例的通用资源共享系统，实现了对各种资源的细粒度访问控制。 此次更新标志着 Datasette 向协作式多用户环境（如内部工具或共享数据平台）迈出了重要一步，管理员现在可以定义谁能访问特定数据集、查询或仪表板。随着 Datasette 走向成熟，强大的权限系统对企业级应用至关重要，datasette-acl 的演进直接满足了这一需求。 该版本引入了对公众受众（everyone、authenticated、anonymous）的一级支持，以及基于 actor 属性（如部门或管理员状态）的动态组成员分配，但仍处于 alpha 阶段，可能不适合生产环境。

rss · Simon Willison · 6月18日 19:03

**背景**: Datasette 是一个用于探索和发布 SQLite 数据库的开源工具，常用于在线数据共享。访问控制列表（ACL）是一种安全机制，定义了哪些用户或组可以访问特定资源。随着 Datasette 逐渐支持多用户实例（例如写入查询和保存的仪表板），灵活的权限系统变得至关重要。datasette-acl 插件提供了超越简单表级限制的高级 ACL 框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-acl/">Release: datasette-acl 0.6a0 - simonwillison.net</a></li>
<li><a href="https://github.com/datasette/datasette-acl/releases/tag/0.6a0">Release 0.6a0 · datasette/datasette-acl</a></li>
<li><a href="https://pypi.org/project/datasette-acl/">datasette-acl · PyPI</a></li>

</ul>
</details>

**标签**: `#datasette`, `#acl`, `#permissions`, `#resource-sharing`, `#plugin`

---