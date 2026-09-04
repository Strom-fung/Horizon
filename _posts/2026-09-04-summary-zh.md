---
layout: default
title: "Horizon Summary: 2026-09-04 (ZH)"
date: 2026-09-04
lang: zh
---

> 从 27 条内容中筛选出 21 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Astra 模型](#item-1) ⭐️ 10.0/10
2. [.name 注册局将终止所有三级域名](#item-2) ⭐️ 8.0/10
3. [用 LLM 将 1993 年 Amiga 游戏从 68000 汇编移植到 Godot](#item-3) ⭐️ 8.0/10
4. [太阳风暴导致全美 GPS 误差高达 33 英尺](#item-4) ⭐️ 8.0/10
5. [AI 编程代理选择哪些工具？1.7 万次运行分析](#item-5) ⭐️ 8.0/10
6. [围棋大师申真谞受让两子击败 KataGo，巧用复杂定式](#item-6) ⭐️ 8.0/10
7. [Paint.NET 借助 Claude 重写 Direct2D 实现实验性 WINE 支持](#item-7) ⭐️ 8.0/10
8. [开源 AI 检测器达不到 0.5%误报率基准](#item-8) ⭐️ 8.0/10
9. [Qwen 3.8 27B 登陆 Cerebras，速度达 1500 tokens/s](#item-9) ⭐️ 7.0/10
10. [Anthropic 更新 Claude 系统提示，明确拒绝复现歌词](#item-10) ⭐️ 7.0/10
11. [用户抓取 59.4 亿 TikTok 视频和 32.3 亿档案，数据集已上传 Hugging Face](#item-11) ⭐️ 7.0/10
12. [Jasper Research 发布从零构建文本到图像模型的教程与 1 亿图像数据集](#item-12) ⭐️ 7.0/10
13. [稀疏自编码器实现可概念引导的音乐检索](#item-13) ⭐️ 7.0/10
14. [人工河狸坝使银鲑存活率升至 60%](#item-14) ⭐️ 6.0/10
15. [K2 Horizon：IFM 推出由六个开源模型组成的互联模型阵容](#item-15) ⭐️ 6.0/10
16. [从古往今来所有人中随机抽取一生并生成 AI 插画故事](#item-16) ⭐️ 6.0/10
17. [llm-gemini 0.34 加入 Gemini 3.8 Flash 支持并修复异步问题](#item-17) ⭐️ 6.0/10
18. [提议仿真训练 JEPA 世界模型为 LLM 接地](#item-18) ⭐️ 6.0/10
19. [NeurIPS 悉尼门票几分钟内售罄，引发业界参会担忧](#item-19) ⭐️ 6.0/10
20. [Mol-JEPA：一种使用联合嵌入预测架构的多模态分子基础模型](#item-20) ⭐️ 6.0/10
21. [Deepity C++库展示预测编码网络在 MNIST 上媲美反向传播](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Astra 模型](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

2026 年 9 月 3 日，OpenAI 面向可信合作伙伴发布了 GPT-6 Astra 的有限预览版，并计划于 9 月 5 日公开发布。该模型在 ARC-AGI-3 上取得 99.9% 的分数，在 Artificial Analysis 编码智能体指数中大幅提升，其系统卡还指出它是首个达到 OpenAI 关键网络能力阈值的模型。 GPT-6 Astra 的基准测试成绩和自主能力声明可能推动行业更接近 AGI 式智能体，同时也提高了安全和对齐方面的风险。该发布在 Hacker News 上引发极高讨论度，会影响评估前沿模型风险的 AI 开发者、企业和监管机构。 报告的 ARC-AGI-3 99.9% 分数可能依赖于特定的“responses API harness”；有评论指出，在相同 harness 下 OpenAI 估计之前的 GPT-5.6 Sol 可达约 30%，而记分卡上显示为 7.8%。系统卡还指出 GPT-6 Astra 在网络能力方面有显著提升，达到 OpenAI 的关键阈值。

hackernews · kibae · 9月3日 18:41 · [社区讨论](https://news.ycombinator.com/item?id=49554643)

**背景**: GPT-6 Astra 是 OpenAI 在 GPT-5 系列之后推出的下一代大型语言模型。ARC-AGI-3 是 ARC Prize 基金会于 2026 年 3 月推出的交互式推理基准，测试 AI 智能体探索新环境并持续学习的能力，而不是求解静态谜题。Artificial Analysis 编码智能体指数是一个综合基准，由 DeepSWE、Terminal-Bench v2.1 和 SWE-Atlas-QnA 组成，用于评估编码智能体在端到端软件工程任务上的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://artificialanalysis.ai/methodology/coding-agents-benchmarking">Coding Agent Index Methodology | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常活跃但持批评态度。评论者认为 ARC-AGI-3 记分卡具有误导性，因为它在不同模型间使用了不同的 API harness；还有人质疑 OpenAI 的演示为何强调无需用户控制的自主购买，并认为多数基准提升看起来更像是技能习得，而非真正的通用智能。版主要求将发布讨论与模型讨论分开。

**标签**: `#AI`, `#GPT-6`, `#OpenAI`, `#LLM`, `#benchmark`

---

<a id="item-2"></a>
## [.name 注册局将终止所有三级域名](https://neil.fraser.name/news/2026/09/03/) ⭐️ 8.0/10

Verisign 与 ICANN 决定终止所有现有 .name 三级域名（如名字.姓氏.name），并释放相应的二级域名，可能允许他人重新注册。 这一政策变化影响依赖 .name 三级域名的现有注册者，并引发域名抢注和安全风险，因为二级域名若没有保护措施将被释放。同时该做法似乎与 ICANN 稳定、安全运营互联网唯一标识符系统的使命相矛盾。 受影响的注册采用 x.y.name 三级域名格式，此次终止的是 x 部分；相应的二级域名 y.name 将被释放，但提案未提及为现有持有者保留域名的时间，因此可能立即被抢注。

hackernews · pavel_lishin · 9月3日 14:54 · [社区讨论](https://news.ycombinator.com/item?id=49550772)

**背景**: 顶级域（TLD）是域名中最后一个点之后的部分，例如 .name。在其之下，二级域（y.name）和三级域（x.y.name）构成层级结构。.name 最初面向个人用户，提供如名字.姓氏.name 的三级域名注册，后来也开放二级域名注册。域名本质上是租赁而非永久所有权，因此注册者受注册局政策约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Top-level_domain">Top-level domain - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Third-level_domain">Third-level domain</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_squatting">Domain squatting</a></li>

</ul>
</details>

**社区讨论**: 评论者大多持批评态度：认为应保留现有三级域名并停止新注册，而不是直接终止；同时警告若二级域名没有保留期将被抢注。有人澄清 .name 顶级域本身并未终止，只有三级域名被停用；也有人指出域名本质是租赁，本身就存在不稳定性。总体认为该政策与 ICANN 稳定、安全运营标识符的使命相矛盾。

**标签**: `#domain names`, `#ICANN`, `#DNS`, `#internet policy`, `#Verisign`

---

<a id="item-3"></a>
## [用 LLM 将 1993 年 Amiga 游戏从 68000 汇编移植到 Godot](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

作者使用 LLM Claude Fable 5，在假期的一个晚上将自己 1993 年在巴格达用 MC68000 汇编开发的 Amiga 游戏《Babylonian Twins》移植到了 Godot 引擎，并用之后几个周末完善手感和发布。他让模型使用 vasm 反复汇编，直到生成的二进制与原版逐字节一致；仅有 108 字节差异，原因是原始发布文件是游戏运行后的内存快照，而非干净的汇编器输出。作者还宣布免费发布原版游戏。 这表明现代 LLM 能够理解并翻译 68000 汇编等底层代码，将过去耗时费力的逆向工程和移植工作缩短到一晚上的时间。它可能让复古游戏的保存和跨平台移植对小型团队和爱好者更加可行。 移植基于 Motorola 68000 汇编源码和开源 Godot 引擎；作者让 LLM 使用 vasm 反复汇编，直到输出与原版二进制逐字节一致，仅 108 字节不同，原因是原版文件是通过 AsmOne 运行后保存的内存快照，而不是干净的汇编器输出。作者还首次展示了 1993 年的地图编辑器截图，并免费发布原版游戏。

hackernews · rabahs · 9月3日 14:28 · [社区讨论](https://news.ycombinator.com/item?id=49550375)

**背景**: Godot 是一个免费、开源、跨平台的游戏引擎，采用 MIT 许可证，支持 PC、移动端、网页和主机的 2D/3D 游戏开发。Motorola 68000（简称 68K）是 20 世纪 80 至 90 年代家用电脑和游戏机（包括 Commodore Amiga）中广泛使用的 CPU，其汇编语言需要直接操作寄存器和内存。Amiga 是当时以出色图形和音频能力著称的个人电脑系列，许多游戏为了性能而使用 68000 汇编编写。vasm 是一款便携、可重定向的汇编器，能生成多种输出格式，适合用来验证重新汇编后的代码是否与原二进制一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Motorola_68000">Motorola 68000 - Wikipedia</a></li>
<li><a href="http://sun.hasenbraten.de/vasm/">vasm portable and retargetable assembler</a></li>

</ul>
</details>

**社区讨论**: 社区反馈非常积极，评论者对该 1993 年汇编作品表示敬佩，并分享了用 LLM 转换复古二进制的经历，例如将 ZX81 内存转储转换为 Go 代码。有人将其与经典游戏《Gods》比较，讨论了可复用的主机移植框架，还有人建议导出一份类似移植的工程指南。

**标签**: `#LLM`, `#code-porting`, `#retrocomputing`, `#assembly`, `#game-development`

---

<a id="item-4"></a>
## [太阳风暴导致全美 GPS 误差高达 33 英尺](https://www.sciencealert.com/gps-glitched-across-the-us-by-as-much-as-33-feet-scientists-have-never-seen-this-before) ⭐️ 8.0/10

一次太阳风暴在美国各地引起了高达 33 英尺（约 10 米）的 GPS 定位误差，干扰了精密导航系统。此次事件的严重程度引发了科学家对依赖 GPS 的基础设施脆弱性的担忧。 GPS 对农业、交通、电子监控和自动驾驶汽车至关重要；即使是约 10 米的误差也可能造成重大经济损失和安全风险。该事件凸显了太空天气如何能在整个大陆范围内干扰现代基础设施。 误差归因于太阳风暴引起的电离层闪烁，它扭曲了 GPS 无线电信号。据估计，2024 年 5 月的太阳风暴给美国农业造成了 5 亿美元的损失，但这一数字存在争议。

hackernews · thread_id · 9月3日 00:49 · [社区讨论](https://news.ycombinator.com/item?id=49544618)

**背景**: 太阳风暴（如日冕物质抛射）会向地球发送带电粒子，扰动磁层和电离层。电离层闪烁会导致无线电信号快速波动，从而降低 GPS 精度。2024 年 5 月的地磁风暴是 G5 级事件，属于最强级别，引发了广泛的极光和 GPS 干扰。GPS 依赖于卫星的精确计时和信号测量，因此任何电离层扰动都可能引入定位误差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Solar_storm">Solar storm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geomagnetic_storm">Geomagnetic storm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ionospheric_scintillation">Ionospheric scintillation</a></li>

</ul>
</details>

**社区讨论**: 评论强调了现实影响，例如电子监控设备错误报告违反宵禁，可能导致重新监禁。一些用户质疑 5 亿美元农业损失的估算过于粗略，另一些用户则提到相关的 GPS 干扰漏洞以及历史上选择性可用性（SA）造成的干扰。还有人担忧自动驾驶汽车（如 Cybercab）在 33 英尺误差下运行的安全问题。

**标签**: `#GPS`, `#solar storm`, `#navigation`, `#infrastructure`, `#HN discussion`

---

<a id="item-5"></a>
## [AI 编程代理选择哪些工具？1.7 万次运行分析](https://armature.tech/blog/which-tools-coding-agents-install) ⭐️ 8.0/10

Armature 发布了一项基于 17,000 次运行的经验分析，衡量 Claude、Codex 和 Cursor 这三个 AI 编程代理会选择安装和使用哪些工具，揭示了明显的偏好和使用趋势。 这些数据难得地从定量角度展示了编程代理如何选择工具，可以帮助开发者在构建集成时做出决策，也能指导工具厂商针对 AI 驱动的采用进行优化。 该分析覆盖了 Anthropic 的 Claude、OpenAI Codex 和 Cursor 的 17,000 次运行；它考察了代理安装和使用哪些工具，但摘要中并未列出具体的偏好排名。

hackernews · screm · 9月3日 21:20 · [社区讨论](https://news.ycombinator.com/item?id=49557206)

**背景**: 像 Claude Code、OpenAI Codex 和 Cursor 这样的 AI 编程代理能够自主执行命令、安装软件包，并在可用工具之间做出选择来完成软件工程任务。Claude Code 是 Anthropic 的编程助手，OpenAI Codex 是通过 ChatGPT 和命令行工具提供的编程代理，而 Cursor 是从 Visual Studio Code 分叉出来的 AI 集成开发环境。这些代理正越来越多地用于实际开发工作，因此它们的工具偏好对整个生态系统都很重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：一些人警告说，随着公司优先考虑利润和锁定用户，AI 的黄金时代可能会衰退；另一些人则认为分析代理的工具选择是一种新的营销渠道。具体观察包括 Claude Code 出人意料地使用 awk、sed 和 Python 进行文件编辑，以及除非明确要求否则很少触发网络搜索。一位用户提到他正在一个开源项目中跟踪类似数据。

**标签**: `#AI coding agents`, `#developer tools`, `#LLM`, `#software engineering`, `#data analysis`

---

<a id="item-6"></a>
## [围棋大师申真谞受让两子击败 KataGo，巧用复杂定式](https://www.kedglobal.com/artificial-intelligence/newsView/ked202607210007) ⭐️ 8.0/10

世界最强人类围棋手申真谞在与开源围棋 AI KataGo 的让两子对局中，通过复杂的“飞刀”定式变化取得均势并获胜。 由于分先对局中人类已无法战胜顶级 AI，这场让子胜利表明人类顶尖棋手在获得足够初始优势后仍能凭借策略战胜 AI，同时也凸显了申真谞空前强大的实力。 评论者估计在分先局面下 KataGo 约比申真谞强 400 到 600 Elo；申真谞选择的“飞刀”定式被描述为通往均势的单行道，而 KataGo 据称更倾向于选择高概率着法而非设下陷阱。此外，该 AI 并非运行在超级计算机上，资源相对有限。

hackernews · gmays · 9月3日 01:11 · [社区讨论](https://news.ycombinator.com/item?id=49544762)

**背景**: 围棋是一种在 19×19 棋盘上进行的策略性棋类游戏。让子是在赛前为较弱一方放置额外棋子以平衡实力差距，让两子意味着黑方开局多两子，优势很大。定式是经过研究的着手序列，其结果被认为对双方均衡。KataGo 是免费开源的围棋 AI，采用深度学习和自我对弈训练，被许多顶尖棋手用于训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo</a></li>
<li><a href="https://en.wikipedia.org/wiki/Joseki">Joseki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Handicapping_in_Go">Handicapping in Go - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞赏申真谞的成就，但指出标题有些误导，因为让两子意味着申真谞在该局中是较弱一方。他们强调了他空前领先的等级分以及巧妙的“飞刀”定式，但也提醒 KataGo 并未运行在超级计算机上，资源有限。

**标签**: `#Go`, `#AI`, `#KataGo`, `#Shin Jinseo`, `#handicap`

---

<a id="item-7"></a>
## [Paint.NET 借助 Claude 重写 Direct2D 实现实验性 WINE 支持](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET 现在加入了一个由 Claude 从零开始、净室重写的 Direct2D 实现，存放在 PaintDotNet.Windows.Direct2D1.Managed.dll 中，通过 /wine 参数触发，使应用能在 Linux 的 WINE 下实验性运行。该重写约 18 万行代码。 这表明 AI 可以辅助净室重写大型图形 API，可能消除 Paint.NET 在 Linux 上运行的主要障碍；同时，在一个流行应用中接受约 18 万行未经彻底审查的 AI 代码也引发可维护性和安全风险方面的担忧。 作者 Rick Brewster 称这些代码大多是“vibe coded”，未经过彻底审查；他不得不反复纠正 Claude 在 COM 引用计数（AddRef）方面的错误以及一些不良设计决策，但 Claude 也完成了 Direct2D 内置效果库公式的逆向工程。该重写约 18 万行，而 Paint.NET 其余代码约 70 万行。

rss · Simon Willison · 9月2日 05:50

**背景**: Direct2D 是微软提供的硬件加速 2D 图形 API，被 Paint.NET 等 Windows 应用使用。WINE 是一个兼容层，通过在 Linux 等类 Unix 系统上重新实现 Windows API 来运行 Windows 程序，但其 Direct2D 支持历来不完整。Vibe coding 是一种 AI 辅助编程方式，开发者向大语言模型描述任务并可能在不彻底审查的情况下接受生成的代码；该术语于 2025 年出现，并引发了关于可维护性和安全性的批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**标签**: `#AI-generated code`, `#Paint.NET`, `#WINE`, `#Direct2D`, `#vibe coding`

---

<a id="item-8"></a>
## [开源 AI 检测器达不到 0.5%误报率基准](https://www.reddit.com/r/MachineLearning/comments/1w58erw/most_opensource_ai_detectors_cant_hold_a_05/) ⭐️ 8.0/10

一项针对六款知名开源 AI 文本检测器的评估，将阈值在 6930 份人类文档上统一设定为 0.5%误报率，结果发现其中四款无法达到该目标。旧的 OpenAI RoBERTa 检测器在现代生成器上 AUC 仅为 0.31，还不如随机猜测；而表现最好的模型对人类改写后的 AI 文本召回率也只有 41.6%。 该基准测试表明，广泛可用的开源 AI 检测器在低误报场景下不可靠，给教育和出版领域带来错误指控的严重风险。对非英语母语写作的偏见以及对改写文本的检测薄弱，意味着这些工具可能对弱势用户造成不成比例的伤害，同时难以应对日益常见的规避手段。 该研究使用了公开数据，包括 Jabarian & Imas 2025（NBER）、Liang 2023 托福作文、包含 GPT-5.x、Claude Opus 5 和 Gemini 3.x 输出的前沿模型集，以及 5000 篇大语言模型出现之前的 FineWeb 网页。表现最好的模型 tropa-mini 原始 AI 文本召回率为 93.2%，但在前沿模型上仅为 33.6%；MAGE 把 26%的普通人类网页文本判定为分数高于 0.9999，且在任何阈值下都无法达到 0.5%的误报率。

reddit · r/MachineLearning · /u/grumpyp2 · 9月2日 12:04

**背景**: 误报率（FPR）是指人类撰写的文本被错误标记为 AI 的比例；将误报率设定在 0.5%这样的低水平对于避免不公平的抄袭指控非常重要。开源 AI 检测器是权重公开可用的模型，对学校和平台很有吸引力，但在不同人群中验证其表现更加困难。FineWeb 是一个广泛使用的大规模公开网页文本数据集，常用于语言模型研究；该基准测试使用大语言模型出现之前的 FineWeb 页面作为人类参考。较旧的 OpenAI RoBERTa 检测器基于 Transformer 架构，已跟不上新一代 AI 生成器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/datasets/HuggingFaceFW/fineweb">HuggingFaceFW/fineweb · Datasets at Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2406.17557">[2406.17557] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale</a></li>

</ul>
</details>

**标签**: `#AI detection`, `#benchmark`, `#bias`, `#machine learning`, `#NLP`

---

<a id="item-9"></a>
## [Qwen 3.8 27B 登陆 Cerebras，速度达 1500 tokens/s](https://inference-docs.cerebras.ai/models/overview) ⭐️ 7.0/10

Cerebras 已在其推理平台上线开源的 Qwen 3.8 27B 模型，服务速度达到 1500 tokens/s。 这一大幅提升的吞吐量可能让大型开源模型适用于编程助手等延迟敏感任务，但社区实测显示严格的每分钟 token 限制和计费摩擦可能抵消速度优势。 社区报告称公共端点每分钟 token 限制在 15 万到 45 万之间，且缓存 token 也计入限额；有用户 90 秒内烧掉 1.10 美元。作为对比，RTX 5090 上使用 ninfer 可达约 200–400 tokens/s。

hackernews · altertable · 9月3日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=49554520)

**背景**: Cerebras 系统公司制造晶圆级 AI 加速器，其芯片远大于 GPU，专为极速推理优化。Qwen 3.8 27B 是阿里巴巴 Qwen 实验室推出的 Apache-2.0 许可的视觉语言模型，可在配置合理的硬件上运行并执行多步推理。tokens/s 衡量模型生成文本的速度，数值越高越适合交互式应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/inference">Inference - Cerebras</a></li>

</ul>
</details>

**社区讨论**: 整体情绪对原始速度感到兴奋，但对实际可用性持怀疑态度。用户报告每分钟 token 限额严格、计费受限，导致编程任务难以完成；有对比显示 DeepSeek-V4-Flash 完成同一任务的成本低得多。有人希望 Cerebras 在 OpenRouter 上提供该模型，也有人指出本地 RTX 5090 配置已能达到 200–400 tokens/s。

**标签**: `#AI`, `#LLM`, `#inference`, `#Qwen`, `#Cerebras`

---

<a id="item-10"></a>
## [Anthropic 更新 Claude 系统提示，明确拒绝复现歌词](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) ⭐️ 7.0/10

Anthropic 重组了其公开的系统提示文档，改为按模型分页，并在 Claude Fable 5.1 的系统提示中新增条款，禁止复现歌词、诗歌及书籍文章段落，但允许 1929 年之前首次发表的作品。 这强化了 Claude 的版权安全策略，也让开发者、研究人员和内容创作者能清晰看到模型限制，从而降低意外复现歌词和法律纠纷的风险，同时体现 Anthropic 对透明度的承诺。 提示中提到，一旦 Claude 在对话中拒绝此类请求，就会在后续对话中继续拒绝更窄或改写后的请求，并改为提供描述或分析；它依据已知的作品发表日期而非用户说法，不确定时会拒绝。Anthropic 的文档可通过在网址后加 .md 获取 Markdown 版本，便于对比提示差异。

rss · Simon Willison · 9月2日 14:16

**背景**: 系统提示是定义 AI 助手角色、行为和安全准则的指令，在处理用户消息前生效。Anthropic 公开分享其消费级 Claude 应用的系统提示，其模型系列包括 Haiku、Sonnet、Opus 和 Fable（Fable 是安全限制更严格的版本）。在美国，1929 年前发表的作品通常已进入公共领域，因此新提示中允许这一例外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/System_prompt">System prompt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#system prompts`, `#Anthropic`, `#prompt engineering`

---

<a id="item-11"></a>
## [用户抓取 59.4 亿 TikTok 视频和 32.3 亿档案，数据集已上传 Hugging Face](https://www.reddit.com/r/MachineLearning/comments/1w5h9se/i_scraped_594_billion_tiktok_videos_and_323/) ⭐️ 7.0/10

Reddit 用户 u/DataShack 声称在三周内通过逆向工程 TikTok 移动 API 抓取了 59.4 亿条视频记录和 32.3 亿份用户资料。收集到的数据集名为 kuben-developer/tiktok-videos-4b，已上传至 Hugging Face 免费开放，但完整的抓取代码和教程需付费获取。 如此大规模的数据集可用于社交媒体行为研究、内容推荐分析或内容审核研究。然而，该方法很可能违反 TikTok 的服务条款，付费墙后的代码也降低了可复现性，并为潜在使用者带来法律和伦理风险。 数据集托管在 huggingface.co/datasets/kuben-developer/tiktok-videos-4b，作者称其完全开源。作者表示 TikTok 应用暴露了 24 个无需登录即可访问的端点，但承认这种方式可能仍违反 TikTok 的服务条款；完整代码则在付费墙后。

reddit · r/MachineLearning · /u/DataShack · 9月2日 17:38

**背景**: Hugging Face 是一个流行的平台，用于分享机器学习数据集和模型，使大规模数据集合公开可用。TikTok 是主要的短视频应用，拥有数十亿用户和视频，因此社交媒体分析对其兴趣巨大。逆向工程移动 API 指检查应用的网络流量或代码以发现非官方端点，这种做法通常违反服务提供商的条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>
<li><a href="https://github.com/SyntaxSparkk/TikTok">GitHub - SyntaxSparkk/TikTok: TikTok Reverse Engineering Documentation. · GitHub</a></li>

</ul>
</details>

**标签**: `#data scraping`, `#TikTok`, `#dataset`, `#Hugging Face`, `#reverse engineering`

---

<a id="item-12"></a>
## [Jasper Research 发布从零构建文本到图像模型的教程与 1 亿图像数据集](https://www.reddit.com/r/MachineLearning/comments/1w5c9rd/detailed_explanation_of_how_to_create_a/) ⭐️ 7.0/10

Jasper Research 发布了一份详细教程（cookbook）、一个包含 1 亿张图像的 Monet 数据集以及名为 nano t2i 的代码库，让开发者可以从零开始构建文本到图像模型，并公开了完整推理过程和中间结果。 这一资源通过提供开放数据、模型代码和教学材料，降低了理解和复现前沿文本到图像系统的门槛，有助于加速研究并让生成式人工智能更加普及。 Monet 数据集包含 1 亿张图像，被描述为大规模、开放、非冗余且经过增强，并提供文本或图像检索接口；代码库包含一个可训练的小模型 nano t2i。该资源主要用于教学和研究目的，而非生产级前沿模型。

reddit · r/MachineLearning · /u/dh7net · 9月2日 14:40

**背景**: 文本到图像模型通过学习大量图文对数据，利用扩散模型或变换器等深度神经网络，根据自然语言描述生成图像。Jasper Research 的教程讲解了从数据整理到模型训练的完整流程。Monet 数据集由现有开源数据集筛选构建，依据来源治理标准，最大化内容、视觉风格和分辨率的多样性，并支持可复现性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gojasper.github.io/monet/">MONET</a></li>
<li><a href="https://huggingface.co/datasets/jasperai/monet">jasperai/ monet · Datasets at Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2605.21272">MONET : A Massive, Open, Non-redundant and Enriched Text-to-image...</a></li>

</ul>
</details>

**标签**: `#text-to-image`, `#machine-learning`, `#tutorial`, `#dataset`, `#generative-models`

---

<a id="item-13"></a>
## [稀疏自编码器实现可概念引导的音乐检索](https://www.reddit.com/r/MachineLearning/comments/1w54qkk/mir_with_audiomuseaisae_p/) ⭐️ 7.0/10

一篇新的 arXiv 论文提出将稀疏自编码器应用于音乐检索嵌入，以识别特定概念的神经元，使用户能够放大中提琴或女声等罕见查询属性。作者还发布了 AudioMuse-AI-SAE，这是为约 700 万参数的 DCLAP 模型训练的稀疏自编码器。 该方法解决了文本到音乐搜索中的属性不平衡问题——常见属性主导结果，导致乐器名称等罕见术语被忽略。它可能实现更细粒度、可操控的检索，并为音乐信息检索的可解释性开辟道路。 该方法先压缩嵌入，应用稀疏自编码器找到单义的概念神经元，修改其激活值，再解码回原始空间。开源 DCLAP 模型是经过蒸馏的 LAION CLAP，约 700 万参数，可在 CPU 上高效运行；论文较新，尚未经过同行评审。

reddit · r/MachineLearning · /u/Old_Rock_9457 · 9月2日 08:47

**背景**: 稀疏自编码器学习具有高度稀疏性的压缩表示，有助于揭示神经网络中可解释且通常是单义的特征。音乐信息检索系统通常将文本和音频嵌入共享的潜在空间，使文本查询能够检索歌曲，但罕见属性容易被频繁共现的概念所掩盖。CLAP（对比语言-音频预训练）是一种学习此类共享文本-音频嵌入的模型；DCLAP 是此处使用的经过蒸馏的小型版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sparse_Auto-Encoders">Sparse Auto-Encoders</a></li>
<li><a href="https://en.wikipedia.org/wiki/Music_information_retrieval">Music information retrieval</a></li>

</ul>
</details>

**标签**: `#Music Information Retrieval`, `#Sparse Autoencoders`, `#Embedding Steering`, `#Interpretability`, `#Retrieval`

---

<a id="item-14"></a>
## [人工河狸坝使银鲑存活率升至 60%](https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california) ⭐️ 6.0/10

在加利福尼亚州，人工河狸坝（beaver dam analogs）使幼年银鲑的存活率从 8%提升至 60%，并形成约 9000 平方米的新栖息地，可容纳超过 8500 条幼鱼。 这种基于自然的修复方法为恢复受威胁的银鲑和改善退化溪流提供了一种成本相对较低的手段，对气候变化下的生物多样性和水资源韧性日益重要。 这些人工坝保持稳定并形成了约 9000 平方米的栖息地；评论者还指出水温有所下降，可能是由于水渗入地下并与较凉的地下水交换热量所致。

hackernews · speckx · 9月3日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=49552572)

**背景**: 河狸坝由河狸建造，能够形成池塘、减缓水流并抬高地下水位，从而改善鱼类栖息地。北美历史上因毛皮贸易而大量捕杀河狸，导致其数量锐减，许多溪流因此退化。人工河狸坝（beaver dam analogs）是人类修建的、模仿河狸坝生态功能的结构。银鲑是太平洋鲑鱼的一种，其幼鱼需要凉爽、流速缓慢的水域才能存活。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.discoverwildlife.com/animal-facts/artificial-beaver-dams-california">People started building artificial beaver dams in California. Now something "mind blowing" is happening | Discover Wildlife</a></li>
<li><a href="https://en.wikipedia.org/wiki/Beaver_dam">Beaver dam - Wikipedia</a></li>
<li><a href="https://www.worldwildlife.org/news/stories/artificial-beaver-dams-help-montana-ranchers-restore-streams-and-protect-wildlife/">Artificial Beaver Dams Aid Montana Streams | WWF</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极并补充了背景：有用户分享了自己观察到银鲑幼鱼在河狸消失的水池中逐渐减少的经历；有人推荐了一本关于 1930 年代修复被炸毁河狸坝的书；还有人提到地下水降温这一反直觉效应；也有人惋惜河狸数量下降并询问为什么不直接重新引入河狸。整体情绪支持基于河狸的修复，并对直接引入河狸存在好奇。

**标签**: `#ecology`, `#conservation`, `#salmon`, `#beaver dams`, `#environmental science`

---

<a id="item-15"></a>
## [K2 Horizon：IFM 推出由六个开源模型组成的互联模型阵容](https://ifm.ai/blog/k2/) ⭐️ 6.0/10

IFM 推出了 K2 Horizon，这是一个由六个开源 AI 模型组成的互联模型阵容，面向推理、编程、智能体工作流、边缘设备和企业部署，并提供训练代码和数据的开放访问。 该发布将包括代码和数据在内的“完全开放”模型阵容扩展到英伟达 Nemotron 等少数先行者之外，可能为开发者和企业提供更透明、可自托管的闭源模型替代方案；但早期社区反馈质疑其性能是否足以改变采用格局。 该阵容包含六个模型，讨论中至少涉及一个稠密 32B 模型和一个 3.7B 模型。IFM 声称开放训练代码和数据，但基准显示 32B 模型落后于一个 27B 的 Qwen 模型，且对比集中缺少 Gemma 4 31B；社区对 3.7B 模型的测试报告了错误代码和幻觉 API。

hackernews · karimf · 9月3日 15:36 · [社区讨论](https://news.ycombinator.com/item?id=49551760)

**背景**: 开源 AI 模型通常只发布权重，而不一定公开训练代码或数据；“完全开放”则包括这些组成部分。模型阵容旨在覆盖从边缘到企业的不同算力规模。IFM 引用的基准用于比较模型的推理和编码任务表现，但独立的社区评测可能暴露差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ifm.ai/blog/k2">Introducing K2 Horizon: Frontier Performance, Radically Open</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1w68rj6/introducing_k2_horizon_frontier_performance/">r/LocalLLaMA on Reddit: Introducing K2 Horizon: Frontier Performance, Radically Open</a></li>

</ul>
</details>

**社区讨论**: 评论者对完全开放的模型栈表示欢迎，但对宣传的性能说法持怀疑态度：一些人指出 32B 模型在自托管的关键区间落后于 Qwen 和 Gemma 等替代方案，还有用户发现 3.7B 模型在编程时不可靠并幻觉出 API。其他评论表达了普遍的“模型疲劳”或对呈现方式的批评，部分讨论偏离主题。

**标签**: `#open-source`, `#AI models`, `#LLM`, `#machine learning`, `#model release`

---

<a id="item-16"></a>
## [从古往今来所有人中随机抽取一生并生成 AI 插画故事](https://anyhumanever.com/) ⭐️ 6.0/10

Any Human Ever 是一个新网站，它从所有曾经存在过的人中随机抽取一个人，并利用 AI 生成其生平插图故事，同时附上历史数据引用。 它展示了生成式 AI 如何应用于历史和可视化，以创造个性化、有情感共鸣的人口史视角，同时也凸显了事实错误的风险。 该项目据称根据历史人口概率分布随机抽样一个人，并生成带统计数据的故事（如结婚年龄、死亡率）。但用户发现引用常指向不相关或宽泛的来源，且年份分布可能未正确反映历史上人口增长。

hackernews · thinkingemote · 9月3日 14:51 · [社区讨论](https://news.ycombinator.com/item?id=49550698)

**背景**: 历史上估计有超过一千亿人，由于人口指数增长，绝大多数生活在近代。生成式 AI 模型能根据提示生成文本和图像，但常会“幻觉”出看似合理却错误的细节。此类项目使用人口数据库和概率模型来模拟历史人物生平。

**社区讨论**: 社区反应不一：许多人欣赏其情感与创意潜力，并建议可用于角色扮演游戏；但也有用户指出事实错误、引用失效或不相关，以及概率分布不正确导致古代人物占比过高。总体认为该项目既令人印象深刻，又在准确性上具有误导性。

**标签**: `#data visualization`, `#AI`, `#history`, `#generative art`, `#web project`

---

<a id="item-17"></a>
## [llm-gemini 0.34 加入 Gemini 3.8 Flash 支持并修复异步问题](https://simonwillison.net/2026/Sep/2/llm-gemini/) ⭐️ 6.0/10

llm-gemini 0.34 新增了 gemini-3.8-flash 模型，支持低、中、高三种思考级别，并修复了异步响应无法记录实际模型版本的问题。 此次更新让现有 llm CLI 用户能立即使用 Gemini 3.8 Flash；谷歌将其定位为在软件工程和智能体工作流中更强大且成本高效的模型，而且思考级别控制可在速度与推理深度之间进行调节。 新模型以 gemini-3.8-flash 名称暴露，支持低/中/高思考设置；异步修复由 Charlie Tonneslan 贡献。在 Simon Willison 的演示中，Gemini 3.8 Flash 用 13 秒生成了一个 HTML 作品，成本为 1.8 美分；他还用该模型给自己 markdown-svg-renderer 工具添加了沙箱化 HTML 渲染功能。

rss · Simon Willison · 9月2日 16:39

**背景**: llm-gemini 是 Simon Willison 的 llm 命令行工具的一个插件，用于接入谷歌的 Gemini 模型。Gemini 3.8 Flash 是 Gemini 系列最新的“主力”模型，取代 3.7 Flash，在软件工程、智能体任务和多步推理方面有所提升。思考级别让用户控制模型在内部推理上消耗多少 token，从适合快速响应的低级别到适合复杂问题的高级别。该插件更新让 CLI 与谷歌的新模型发布保持同步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/thinking">Gemini thinking - Interactions API | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#llm-gemini`, `#Gemini`, `#Google`, `#AI`, `#plugin`

---

<a id="item-18"></a>
## [提议仿真训练 JEPA 世界模型为 LLM 接地](https://www.reddit.com/r/MachineLearning/comments/1w69gvd/grounding_llms_with_jepabased_world_models/) ⭐️ 6.0/10

一位 Reddit 用户提出在 MuJoCo 等物理仿真中训练 JEPA 风格的世界模型，学习抽象状态表示，并将其作为条件信号附加到 LLM 上，从而为语言模型提供基于物理的“直觉”，而非仅靠 token 统计。 若成功，该方法有望解决 LLM 的符号接地问题，让模型利用实际的物理表示而非纯粹的语言统计关联，可能大幅提高下游推理与学习效率。这与世界模型、JEPA 和具身智能等前沿方向密切相关。 该想法结合了 JEPA 式预测表示学习和仿真物理训练，冻结学到的表示后通过拼接或交叉注意力附加到 LLM；作者提到 V-JEPA 和 DreamerV3 相关，但这种特定组合似乎尚未被实现。目前仅为概念提案，没有原型或结果，开放问题包括仿真到现实的迁移和接口设计。

reddit · r/MachineLearning · /u/Full_Promotion4522 · 9月3日 14:45

**背景**: JEPA（联合嵌入预测架构）在潜在空间而非像素或 token 空间进行预测，从而学习更抽象、更具语义的特征。MuJoCo 是开源的物理仿真引擎，广泛用于机器人学和机器学习研究。符号接地问题探讨符号如何与现实世界指涉物建立联系，而 LLM 由于只从文本学习，缺乏这种接地。玛丽房间思想实验则区分了“知道所有事实”和“实际体验”之间的差异，类似于 LLM 知道物理事实却缺乏物理直觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Symbol_grounding_problem">Symbol grounding problem - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2301.08243">[2301.08243] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/MuJoCo">MuJoCo</a></li>

</ul>
</details>

**标签**: `#LLM`, `#JEPA`, `#world models`, `#grounding`, `#simulation`

---

<a id="item-19"></a>
## [NeurIPS 悉尼门票几分钟内售罄，引发业界参会担忧](https://www.reddit.com/r/MachineLearning/comments/1w6gwni/neurips_sydney_sold_out_in_minutes_n/) ⭐️ 6.0/10

Reddit 上的一篇帖子称，NeurIPS 悉尼会议的注册在几分钟内售罄，而论文录用决定还要三周后才公布。发帖者猜测其中有多少是来自产业界和 VC 资助的 AI 实验室，目的是为了社交和招聘。 迅速售罄凸显了对顶级 AI 会议的极高需求，并引发担忧：资金充足的产业界参会者可能会挤占学者和独立研究者的名额。这也表明这类会议已成为 AI 行业重要的社交和招聘平台。 帖子中没有给出确切的注册人数或票种分配明细。关键细节在于时间：注册在几分钟内关闭，且距离论文决定还有三周，这很不寻常，加剧了关于参会者构成的猜测。

reddit · r/MachineLearning · /u/alrojo · 9月3日 19:09

**背景**: NeurIPS（神经信息处理系统会议）是与 ICML 和 ICLR 并列的三大最具影响力的机器学习会议之一。它每年 12 月举行，包括特邀报告、论文宣讲、海报展示和研讨会。由于需求经常超过容量，注册往往会很快售罄。该会议吸引了学术研究人员和产业界专业人士的混合参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeurIPS">NeurIPS</a></li>

</ul>
</details>

**标签**: `#NeurIPS`, `#machine learning`, `#conferences`, `#AI community`, `#event capacity`

---

<a id="item-20"></a>
## [Mol-JEPA：一种使用联合嵌入预测架构的多模态分子基础模型](https://www.reddit.com/r/MachineLearning/comments/1w6i8pr/moljepa_multimodal_molecular_foundation_model_r/) ⭐️ 6.0/10

一位独立研究者分享了 Mol-JEPA，这是一种用于分子数据的多模态联合嵌入预测架构（JEPA）模型。作者在总结网站上发布了初步结果，并寻求反馈以改进这一早期模型。 该工作展示了 JEPA 自监督表示学习在化学领域的创新应用，有可能为药物发现和材料科学提供更通用的分子嵌入。不过其影响取决于性能能否在初步结果基础上得到提升。 该模型采用非生成式的 JEPA 方法，在潜空间中预测表示，而不是重建原始输入；但帖子尚未报告基准测试对比或完整架构细节。作者明确表示还需要更多工作来提升性能。

reddit · r/MachineLearning · /u/TerribleAntelope9348 · 9月3日 19:56

**背景**: JEPA（联合嵌入预测架构）是一种自监督学习框架，通过预测被掩蔽或变换输入的潜在嵌入来学习表示，避免了像素级重建。分子基础模型旨在从大量未标记的化学数据中产生可复用的分子表示，用于性质预测等下游任务。将 JEPA 与多模态分子输入相结合，有望减少化学领域对标记数据的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Joint_Embedding_Predictive_Architecture">Joint Embedding Predictive Architecture</a></li>
<li><a href="https://arxiv.org/abs/2301.08243">[2301.08243] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture</a></li>
<li><a href="https://www.emergentmind.com/topics/molecular-foundation-model">Molecular Foundation Model Overview</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#molecular modeling`, `#JEPA`, `#foundation models`, `#chemistry`

---

<a id="item-21"></a>
## [Deepity C++库展示预测编码网络在 MNIST 上媲美反向传播](https://www.reddit.com/r/MachineLearning/comments/1w5fuhm/deepity_a_c_library_showing_predictive_coding/) ⭐️ 6.0/10

Deepity 是一个 C++ 机器学习库，利用 Direct Kolen-Pollack 反馈对齐和算法缓存实现了加速预测编码网络，在 MNIST 上达到 97.73% 的测试准确率，耗时 59.5 秒，而 PyTorch 反向传播前馈网络约为 98.27%、70 秒。 这表明生物合理的预测编码网络在标准基准上可以达到与反向传播相当的准确率，并且 CPU 上的计算速度也具有竞争力，这对于反向传播表现不佳的替代性信用分配和持续学习研究具有重要意义。 Deepity 使用带有可学习反馈连接的 Direct Kolen-Pollack PCN 算法，并在推理沉降阶段缓存前向投影以绕过冗余计算；当前结果仅限于 MNIST 数据集、50 个 epoch 和 CPU 执行，作者计划未来扩展到 CUDA 和持续学习实验。

reddit · r/MachineLearning · /u/Important-Home4431 · 9月2日 16:49

**背景**: 预测编码网络是一类受生物启发的模型，通过最小化层级之间的预测误差来学习，为训练前馈神经网络提供了一种替代广泛使用的反向传播算法的方法。Direct Kolen-Pollack 反馈对齐方法通过增加从输出层到所有隐藏层的直接反馈连接来加速 PCN 训练，相比早期的随机反馈方法能更好地对齐反馈权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Predictive_coding">Predictive coding - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2602.15571">[2602.15571] Accelerated Predictive Coding Networks via Direct Kolen-Pollack Feedback Alignment</a></li>
<li><a href="https://arxiv.org/abs/2506.06332">[2506.06332] Introduction to Predictive Coding Networks for Machine Learning</a></li>

</ul>
</details>

**标签**: `#predictive coding`, `#backpropagation`, `#C++`, `#alternative credit assignment`, `#biologically plausible learning`

---