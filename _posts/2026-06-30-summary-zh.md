---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 28 条内容中筛选出 16 条重要资讯。

---

1. [美高院裁定地理围栏令需宪法保护](#item-1) ⭐️ 9.0/10
2. [谷歌智能体同行评审系统在 ICML/STOC 处理万篇论文](#item-2) ⭐️ 9.0/10
3. [Qwen 3.6 27B：本地开发的绝佳平衡点](#item-3) ⭐️ 8.0/10
4. [HCCF 提出 .self 顶级域名支持自托管与数字身份](#item-4) ⭐️ 8.0/10
5. [藏匿杂志获刑 30 年重创言论自由](#item-5) ⭐️ 8.0/10
6. [一百万个护照信息在线泄露](#item-6) ⭐️ 8.0/10
7. [Jon Udell 提议翻转“人类参与循环”，邀请 AI 代理加入开发流程](#item-7) ⭐️ 8.0/10
8. [EML 树被证明为通用逼近器](#item-8) ⭐️ 8.0/10
9. [Rocket Lab 收购 Iridium 完成历史性交易](#item-9) ⭐️ 7.0/10
10. [Ornith-1.0：面向智能编程的自改进开源模型](#item-10) ⭐️ 7.0/10
11. [Cerebras-OpenAI 交易致 API 候补名单无限期](#item-11) ⭐️ 7.0/10
12. [可编辑权重的极简 Transformer 可视化工具](#item-12) ⭐️ 7.0/10
13. [为 SSH 提出原生图形化 Shell](#item-13) ⭐️ 6.0/10
14. [Simon Willison 发布 HTML 表格提取工具](#item-14) ⭐️ 6.0/10
15. [为何实例表示学习中选择 NCE 而非直接负采样？](#item-15) ⭐️ 6.0/10
16. [历史剑术格斗者创建开放数据集以推进薄物体跟踪研究](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [美高院裁定地理围栏令需宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，地理围栏搜查令必须符合第四修正案的保护要求，执法人员需基于合理根据获得搜查令，而不能无证获取位置数据。 这一里程碑式裁决大幅强化了数字隐私保护，将第四修正案的保护延伸至地理围栏搜查令，限制了执法机构通过位置数据进行大规模无证监控的能力。 法院意见详细说明了谷歌分三个阶段提供数据的流程，强调每个阶段都需搜查令。法官阿利托、托马斯和巴雷特持异议，主张更广泛的执法权限。此裁决还可能影响诸如 Flock 自动车牌识别器等采集位置数据的监控技术。

hackernews · cdrnsf · 6月29日 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令（又称反向位置搜查令）允许执法机构要求科技公司如谷歌提供特定地理区域和时间段内所有移动设备的数据。美国宪法第四修正案禁止不合理搜查，通常要求执法人员基于合理根据取得搜查令。在 2014 年 Riley 诉加利福尼亚案中，最高法院认定现代手机承载大量个人信息，应受强化隐私保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>

</ul>
</details>

**社区讨论**: 评论区总体支持裁决，提供了关于谷歌数据提供流程的详细技术信息，并讨论了在其他场景中识别个人的可能性（如通过酒店客人名单交叉比对）。有人称赞法院在意见中引用了来源，有人关注该裁决对 Flock 自动车牌识别器等监控技术的影响，并对保守派大法官的异议表示意外。

**标签**: `#privacy`, `#supreme-court`, `#geofence-warrants`, `#fourth-amendment`, `#digital-rights`

---

<a id="item-2"></a>
## [谷歌智能体同行评审系统在 ICML/STOC 处理万篇论文](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

谷歌在 ICML 和 STOC 两大顶级计算机科学会议部署了智能体 AI 同行评审系统，该系统在约 30 分钟内审阅了约 1 万篇论文，相比零样本提示，数学错误检测率提升了 34%，相关正式研究论文现已发布。 这为会议规模的 AI 自动化科学评审开创了先河，通过提升效率和准确性，有望改变学术出版格局。 该智能体系统相比零样本方法将数学错误检测率提高了 34%，处理了两次顶级会议约 1 万篇论文，每篇论文评审时间约 30 分钟。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 6月29日 10:05

**背景**: 智能体 AI 指能够推理、规划和执行多步骤任务的自主目标导向系统，仅需极少人类干预。零样本提示是一种让模型在没有任务特定示例的情况下直接执行任务的技术，仅依赖其预训练知识。智能体工作流与先进提示技术的结合能显著提升复杂任务表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**标签**: `#AI peer review`, `#agentic systems`, `#machine learning`, `#academic publishing`, `#scientific AI`

---

<a id="item-3"></a>
## [Qwen 3.6 27B：本地开发的绝佳平衡点](https://quesma.com/blog/qwen-36-is-awesome/) ⭐️ 8.0/10

一篇博文将 Qwen 3.6 27B 评估为在配备 128GB 内存的 MacBook Pro M5 上进行本地编码的理想 LLM，引发了社区对其实际可行性的热烈讨论。 这场讨论揭示了在本地运行强大开源模型所面临的挑战与取舍，影响着开发者在本地隐私与云端 API 成本效益之间的选择。 Qwen 3.6 27B 是阿里巴巴于 2026 年 4 月发布的稠密 270 亿参数模型，编程基准测试表现强劲；本地推理需价值 6699 美元的 128GB MacBook Pro，但该机器在高负载下存在发热和风扇噪音问题。

hackernews · stared · 6月29日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=48721903)

**背景**: Qwen 3.6 是阿里巴巴的开源 LLM 系列，其中 27B 版本在能力与资源需求之间取得了平衡。本地部署 LLM 在代码生成、数据隐私和离线使用方面仍受青睐，但通常需要强大的硬件支持。得益于效率优势，采用统一内存架构的苹果硅 Mac 已成为常见平台，但参数规模超过数十亿的模型仍可能触及散热极限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/rico03/Qwen3.6-27B-Claude-Opus-Reasoning-Distilled">rico03/ Qwen 3 . 6 - 27 B -Claude-Opus-Reasoning-Distilled · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.6-27b">Qwen 3 . 6 27 B - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://ollama.com/library/qwen3.6:27b">qwen 3 . 6 : 27 b</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，由于发热和噪音问题，MacBook Pro 不适用于持续的 AI 工作负载，而云端 API（如 OpenRouter）能提供更好的性价比。也有人认为，零样本新项目并不能代表真实编码场景，模型在复杂现有代码库上的实用性仍有待验证。

**标签**: `#local-llm`, `#qwen`, `#hardware`, `#development`, `#llm-evaluation`

---

<a id="item-4"></a>
## [HCCF 提出 .self 顶级域名支持自托管与数字身份](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/) ⭐️ 8.0/10

HCCF 推出了一个新的顶级域名 .self 的提案，旨在促进自托管和以人为中心的身份管理，在技术人员中引发了大量讨论。 .self 域名可以为个人提供一个专门的命名空间，用于他们控制下的个人网站和服务，可能减少对商业注册商的依赖并增强隐私。但可行性取决于解决滥用和资金挑战。 关键方面包括每人免费子域名、反抢注规则和身份验证。关注点包括如何在没有注册费的情况下为 TLD 提供资金、区分停放域名和合法使用、以及防止因滥用而导致声誉受损。

hackernews · HumanCCF · 6月29日 19:49 · [社区讨论](https://news.ycombinator.com/item?id=48724230)

**背景**: 顶级域名（TLD）是 DNS 层级中的最高级别，例如 .com 或 .org。自托管涉及在私人控制的服务器上运行网络服务，而不是使用第三方平台。提案来自 HCCF，该组织似乎是一个以人为中心的计算倡导团体，但其具体性质并未公开详细说明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Top-level_domain">Top-level domain - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-hosting_(network)">Self-hosting (network) - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=48724230">.self: A new top-level domain designed to support self-hosting | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出谨慎的乐观态度：有人回忆起免费 .tk 域名因滥用而失败，有人建议基于声誉的系统或通过零知识证明进行身份验证，许多人质疑免费 TLD 的经济可持续性和反滥用执行。

**标签**: `#TLD`, `#self-hosting`, `#decentralization`, `#digital identity`, `#internet governance`

---

<a id="item-5"></a>
## [藏匿杂志获刑 30 年重创言论自由](https://theintercept.com/2026/06/26/daniel-sanchez-estrada-zines-prairieland-free-speech/) ⭐️ 8.0/10

丹尼尔·桑切斯·埃斯特拉达因在妻子通知他联邦搜查令后藏匿当局追查的杂志，被判处 30 年监禁。这些杂志与一起在 ICE 设施外的抗议活动有关，该活动中一名联邦官员遭枪击。 此案将藏匿已出版资料与严重刑事共犯等同，树立危险先例，可能寒蝉自由表达和活动新闻。它凸显了国家安全起诉与第一修正案保护之间日益紧张的关系。 这些杂志已公开发行多年，被作为枪击案调查的证据追查，但桑切斯·埃斯特拉达并非枪手。此判决是更广泛案件的一部分，同案被告被判处 70 至 100 年徒刑。

hackernews · xrd · 6月28日 21:42 · [社区讨论](https://news.ycombinator.com/item?id=48711981)

**背景**: 杂志（Zines）是自出版、常为政治性的小众刊物，在活动圈中常见。美国法律规定，事后共犯涉及协助他人逃避逮捕或惩罚，其刑罚常与潜在罪行挂钩。此案源于 2020 年德克萨斯州 ICE 设施的一场抗议活动，当时一名警员遭枪击，当局将杂志视为潜在证据追查。

**社区讨论**: 评论者意见分歧：有人认为此判决是对言论自由的沉重打击，堪比'大坝裂缝'；另一些人则认为藏匿证据明显违法，只是刑期过长。也有人提及总统赦免的党派预期。

**标签**: `#free-speech`, `#legal`, `#censorship`, `#activism`, `#hacker-news`

---

<a id="item-6"></a>
## [一百万个护照信息在线泄露](https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal) ⭐️ 8.0/10

为西班牙大麻俱乐部提供年龄验证的爱尔兰公司 Cannabis Club Systems 发生数据泄露，导致一百万份高分辨率护照扫描件在线外泄。 此事凸显了在低安全性辅助系统中使用高价值身份证明文件的危险，因为被攻破的系统在验证后仍保留了敏感数据，使个人面临身份盗用风险。在全球推动在线年龄验证的背景下，这类事件展示了潜在的巨大隐私侵犯。 泄露的数据由西班牙的大麻俱乐部收集，并由一家爱尔兰公司存储；具体安全缺陷尚不清楚，但涉及一个不安全的在线数据库。许多国家正在制定年龄验证法规，此类风险可能随之扩大。

hackernews · jruohonen · 6月28日 11:22 · [社区讨论](https://news.ycombinator.com/item?id=48706389)

**背景**: 年龄验证系统通常要求用户上传政府颁发的身份证件，部分系统会长期保存这些信息。近期多国推动在线年龄验证（如社交媒体、在线销售），这扩大了攻击面。护照被视为高价值凭证，因为其信息可用于身份盗用。欧盟的 eIDAS 2.0 法规旨在提供安全的数字身份解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daringfireball.net/linked/2026/06/28/puffpal-passport-leak">Daring Fireball: PuffPal, an App for Accessing Cannabis Clubs, Leaked 1 Million Users' Passports</a></li>
<li><a href="https://www.resetera.com/threads/a-million-passports-for-online-age-verification-have-been-hacked-leaked.1563271/">A million passports for online age verification have been... | ResetEra</a></li>

</ul>
</details>

**社区讨论**: 评论者批评了为琐碎验证而储存护照的不安全做法，分享了护照数据泄露的类似经历，并呼吁改变政策，一些人指出 eIDAS 2.0 是潜在解决方案。

**标签**: `#data-breach`, `#privacy`, `#security`, `#identity-theft`, `#age-verification`

---

<a id="item-7"></a>
## [Jon Udell 提议翻转“人类参与循环”，邀请 AI 代理加入开发流程](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell 主张翻转主流的“人类参与循环”叙事，提出应由开发者邀请 AI 代理加入他们已有的工作流程，而非将人类插入代理驱动的循环中。 这一重新框架挑战了 AI 辅助开发中现有的权力动态，强调人类的主动权和控制力。它可能重塑开发者工具的设计方式以及团队采纳 AI 的方式，培养以人类为决策者的协作环境。 Udell 的批评源于 AI 代理创建无法审阅的拉取请求。他主张代理式软件开发，让代理成为透明的团队成员，而非掩盖过程的黑箱。

rss · Simon Willison · 6月28日 21:57

**背景**: 传统上，“人类参与循环”指人类判断被纳入 AI 决策过程的系统。代理型 AI 指能够自主规划和执行任务的代理。在软件开发中，此类代理可自动化编码，但常常生成复杂且难以审阅的变更。Jon Udell 是备受尊敬的技术专家，以对软件实践的深刻见解而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentintheloop.org/">AGENT In The Loop 2.0 | The Agentic Era</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#software-development`, `#human-in-the-loop`, `#developer-tools`, `#technology-philosophy`

---

<a id="item-8"></a>
## [EML 树被证明为通用逼近器](https://www.reddit.com/r/MachineLearning/comments/1uipl1t/eml_trees_are_universal_approximators_r/) ⭐️ 8.0/10

一篇新论文证明，通过组合表示基本函数的 EML 型树是通用逼近器，能够以显式构造性证明在连续函数空间和 Sobolev 空间中稠密逼近任意函数。 该结果为在机器学习函数逼近中使用 EML 树奠定了理论基础，可能影响利用基本函数组合进行符号回归或硬件友好神经网络等任务架构的设计。 证明通过显式构造 EML 表示的多项式和双曲正切函数，并用基于符号的分解处理自然对数在非正输入的未定义问题；此外，EML 函数被推广为带有可学习参数的形式。

reddit · r/MachineLearning · /u/JoeGermany · 6月29日 11:16

**背景**: EML 树是一种组合表示，通过组合基本函数（如指数、对数和三角函数）来形成更复杂的函数。通用逼近定理是机器学习的基础结论，表明在有足够容量的情况下，模型可以任意精度逼近任何连续函数。Sobolev 空间是带有导数范数的函数空间，广泛用于偏微分方程的分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Brumbelow/uninum/blob/main/docs/eml_explained.md">uninum/docs/ eml _explained.md at main · Brumbelow/uninum · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sobolev_space">Sobolev space</a></li>

</ul>
</details>

**标签**: `#universal approximation theorem`, `#EML trees`, `#function approximation`, `#mathematical proof`, `#machine learning theory`

---

<a id="item-9"></a>
## [Rocket Lab 收购 Iridium 完成历史性交易](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 7.0/10

Rocket Lab 宣布收购 Iridium，打造一家将发射服务、卫星制造和卫星运营合为一体的全整合太空公司。 此次收购确保了宝贵的频谱许可证和盈利的卫星业务，同时为 Rocket Lab 提供了类似于 SpaceX 通过 Starlink 获得的稳定发射需求基线。 Iridium 运营着一个由 66 颗低轨卫星组成的星座，交易使 Rocket Lab 获得这些资产和相关的频谱。提供的摘要未披露财务条款。

hackernews · everfrustrated · 6月29日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48719485)

**背景**: Iridium 是一家卫星通信公司，通过其低轨卫星网络提供全球语音和数据覆盖。Rocket Lab 起源于新西兰，专注于小型卫星发射和卫星制造。此次收购标志着航天产业一次重大的垂直整合举措。

**社区讨论**: 社群反应不一：有人称赞其通过确保定期发射和频谱的战略举措，也有人对空间碎片日益增多表示担忧。少数评论关注 Rocket Lab 从新西兰身份向美国身份的转变。

**标签**: `#space`, `#acquisition`, `#satellites`, `#RocketLab`, `#Iridium`

---

<a id="item-10"></a>
## [Ornith-1.0：面向智能编程的自改进开源模型](https://github.com/deepreinforce-ai/Ornith-1) ⭐️ 7.0/10

DeepReinforce 发布了 Ornith-1.0，一款用于智能编程的开源模型，声称具有自我改进功能。它包含 9B、31B、35B MoE 和 397B MoE 等多个版本，均基于 Gemma 4 和 Qwen 3.5 微调而成。 该模型将开源模型带入智能编程领域，为商业编程智能体提供了免费替代方案。若其自我改进能力得到验证，可能会启发新的模型自我增强方法。 该模型提供四种规模，最大为 397B MoE 版本。它以 MIT 许可证发布，但基于 Gemma 4 和 Qwen 3.5 构建，早期社区测试表明其基准测试成绩出色，但在聊天中易产生幻觉且只能发现多数模型都能发现的常见错误。

hackernews · danboarder · 6月29日 17:16 · [社区讨论](https://news.ycombinator.com/item?id=48722052)

**背景**: 智能编程（Agentic Coding）指 AI 智能体自主完成规划、编写、测试和调试代码等多步骤软件开发任务。自改进模型旨在迭代增强自身能力，常与递归自改进概念相关联。Qwen 和 Gemma 分别是阿里巴巴和谷歌的开源大语言模型，常被用作特定任务微调的基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen">Qwen (Qwen) - Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区反应两极分化：部分用户称赞其创造性的编码方案以及作为 Qwen 微调版被接受，但另一些人批评它只是‘基准测试特化版’，并报告其存在幻觉问题。对其自我改进机制的真实性仍存疑，且缺少 31B 版本的发布也引起关注。

**标签**: `#open-source`, `#ai-models`, `#agentic-coding`, `#self-improving`, `#llm`

---

<a id="item-11"></a>
## [Cerebras-OpenAI 交易致 API 候补名单无限期](https://www.reddit.com/r/MachineLearning/comments/1uiqhiv/cerebras_openai_deal_capacity_has_effectively/) ⭐️ 7.0/10

一家小型 AI 创业公司披露，由于 OpenAI 与 Cerebras 达成的 200 亿美元芯片交易占用了大部分近期推理产能，Cerebras 的 API 候补名单实质上已变得无限长，其他用户无法获得访问权限。 此事件揭示了超大规模企业与 AI 硬件厂商的交易可垄断专用算力，排挤小型企业，导致高吞吐量推理能力集中，可能抑制创新并减少 AI 产品多样性。 该创业公司需要满足 p95 延迟严格约束及持续 1-2 千 token/秒的高吞吐推理，而 Cerebras 的晶圆级 ASIC 芯片正为此设计。与 OpenAI 的交易预分配了几乎所有运力，导致 API 候补名单实际上无限期。

reddit · r/MachineLearning · /u/Kortopi-98 · 6月29日 12:00

**背景**: Cerebras Systems 生产晶圆级 AI 加速器（如 CS-2），其基于 ASIC 的大尺寸芯片专为 AI 训练和推理优化。推理 ASIC 是为高效运行已训练模型而设计的定制硬件。p95 延迟是实时服务的关键指标，表示 95%的请求延迟都低于该阈值，用于确保性能一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.fortuneindia.com/technology/what-is-cerebras-and-why-is-everyone-suddenly-talking-about-it-explained/137202">What is Cerebras and why is everyone suddenly talking about it: Explained</a></li>
<li><a href="https://oneuptime.com/blog/post/2025-09-15-p50-vs-p95-vs-p99-latency-percentiles/view">P50 vs P95 vs P99 Latency Explained: What Each Percentile Tells You</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Cerebras`, `#OpenAI`, `#inference`, `#startups`

---

<a id="item-12"></a>
## [可编辑权重的极简 Transformer 可视化工具](https://www.reddit.com/r/MachineLearning/comments/1uhw7fu/i_shrank_a_transformer_until_every_number_fitted/) ⭐️ 7.0/10

一名软件工程师创建了一个单文件交互式网页工具，将 Transformer 缩小到最小规模（6 词词汇表、3 维嵌入、单注意力头、单层），允许用户编辑所有权重和词向量，并实时查看每个计算步骤的更新。 该工具为学习者提供了一种具体、可动手操作的方式来理解 Transformer 的内部机制，使前向传播过程完全透明且可交互，而这通常隐藏在高阶 API 之后。 该 Transformer 仅使用 6 个词的词汇表和 3 维嵌入，含单注意力头和一层模块；所有权重均可编辑，整个前向传播即时重新计算；模型未经过训练，当权重随机化时预测变为无意义，以此说明训练的重要性。

reddit · r/MachineLearning · /u/DanielMoGo · 6月28日 12:35

**背景**: Transformer 通过自注意力机制处理序列，每个 token 计算查询(Q)、键(K)和值(V)向量以决定关注序列中的哪些 token。Q 与 K 的点积得到注意力分数，经缩放和 softmax 后得到注意力权重。在自回归生成中，因果掩码防止模型关注未来的 token。然后，加权的 V 向量通过前馈网络产生下一层的表示，最终生成 logits 和下一个 token 的概率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.billparker.ai/2024/10/transformer-attention-simple-guide-to-q.html">Transformer Attention: A Guide to the Q, K, and V Matrices</a></li>
<li><a href="https://machinelearningmastery.com/a-gentle-introduction-to-attention-masking-in-transformer-models/">A Gentle Introduction to Attention Masking in Transformer Models - MachineLearningMastery.com</a></li>

</ul>
</details>

**标签**: `#transformers`, `#education`, `#interactive`, `#machine learning`, `#visualization`

---

<a id="item-13"></a>
## [为 SSH 提出原生图形化 Shell](https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html) ⭐️ 6.0/10

Marcus Lewis 提出一种原生 SSH 图形化 Shell，在服务器端托管基于 Web 的图形应用，通过 SSH 访问，并提供 API 用于应用发现和相互通信。 这可能简化远程服务器管理和内部 Web 工具的访问，为纯终端 SSH 会话提供更集成的替代方案，但社区鉴于现有解决方案质疑其必要性。 该 Shell 通过 SSH 隧道使用私有 HTTP 服务器，允许应用注册为文件类型处理程序（如文本编辑器），旨在替代命令行应用。

hackernews · mrcslws · 6月29日 15:42 · [社区讨论](https://news.ycombinator.com/item?id=48720758)

**背景**: SSH（安全外壳协议）是用于安全远程访问的协议，通常用于命令行 Shell。通过 SSH 的图形化访问已存在数十年，如 X11 转发隧道传输 X Window 系统流量。现代替代方案包括基于 Web 的管理工具（如 Cockpit）和使用 WebSocket 的浏览器 SSH 客户端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html">A native graphical shell for SSH | Marcus Lewis</a></li>
<li><a href="https://news.ycombinator.com/item?id=48720758">A native graphical shell for SSH | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shell_(computing)">Shell (computing) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持怀疑态度，认为该提案是“寻找问题的解决方案”。许多人指出已有 X11 转发、Cockpit 和 Web 应用等选项，质疑新 Shell 的必要性。部分人欣赏前后端分离的思路，但认为并无新意。

**标签**: `#SSH`, `#graphical-interface`, `#remote-access`, `#innovation`, `#web-development`

---

<a id="item-14"></a>
## [Simon Willison 发布 HTML 表格提取工具](https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything) ⭐️ 6.0/10

Simon Willison 发布了一款粘贴转换工具，可从富文本中提取表格并将其导出为 HTML、Markdown、CSV、TSV 或 JSON。更新版本新增了通过维基百科 API 直接搜索并导入表格的功能。 该工具简化了从网页中提取表格数据的流程，为数据分析师、记者以及需要复用网页表格而无需手动格式转换或编写爬虫的用户节省了时间。 该工具利用浏览器粘贴事件捕获嵌入的 HTML 表格。维基百科集成利用了该页面的 CORS 开放 API 端点，该功能借助 Codex 辅助开发。

rss · Simon Willison · 6月29日 23:38

**背景**: 浏览器中的富文本粘贴包含底层 HTML 格式。CORS（跨源资源共享）使 Web 应用能够请求其他域的内容。维基百科提供 API 可返回任何页面的已解析 HTML，从而实现自动表格提取。

**标签**: `#tools`, `#HTML`, `#tables`, `#data extraction`, `#web scraping`

---

<a id="item-15"></a>
## [为何实例表示学习中选择 NCE 而非直接负采样？](https://www.reddit.com/r/MachineLearning/comments/1uj8nse/loss_functions_in_instance_representation/) ⭐️ 6.0/10

一位 Reddit 用户质疑在实例表示学习中，为什么使用噪声对比估计（NCE）来近似非参数 softmax 的分母，而不是直接近似分母，并询问其与密度估计的理论联系。 这个问题触及大规模表示学习的核心技术；阐明 NCE 相对于直接近似的优势，有助于设计更好的损失函数，提高在海量数据集上训练大模型的计算效率。 用户引用了 Wu 等人的具体公式，指出 NCE 仍然需要估计分母（通过式 8），并对其必要性提出疑问；他们提到直接分母近似可能引入偏差，且随着噪声样本数 m 增加，NCE 的梯度与负对数似然的梯度渐近一致。

reddit · r/MachineLearning · /u/No_Balance_9777 · 6月29日 23:34

**背景**: 在实例表示学习中，每个实例被视作独立的类别，需在全数据集上计算 softmax（即非参数 softmax），当 n 很大时计算不可行。噪声对比估计（NCE）通过学习区分真实数据和人工生成的噪声来规避显式归一化，将密度估计问题转化为二分类任务，且被证明具有一致性：随着噪声样本增加，其梯度收敛于真实似然的梯度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@weidagang/demystifying-noise-contrastive-estimation-nce-in-machine-learning-32ded05401f4">Demystifying Neural Networks: Noise Contrastive Estimation (NCE)</a></li>
<li><a href="https://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf">PDF Noise-contrastive estimation: A new estimation principle for ...</a></li>

</ul>
</details>

**标签**: `#Loss Functions`, `#Noise Contrastive Estimation`, `#Representation Learning`, `#Machine Learning Theory`, `#Softmax`

---

<a id="item-16"></a>
## [历史剑术格斗者创建开放数据集以推进薄物体跟踪研究](https://www.reddit.com/r/MachineLearning/comments/1uivddx/i_do_historical_swordfighting_and_noticed_ai/) ⭐️ 6.0/10

一名 HEMA 练习者正在构建开放数据集，包含同步多视角高速剑术片段及详细标注。数据集提供关键点、生物力学和遮挡信息，旨在辅助薄物体跟踪和 Sim2Real 研究。 薄物体跟踪和 Sim2Real 是计算机视觉与机器人学的已知瓶颈。该数据集针对极端运动和严重遮挡场景，对具身 AI、运动分析和 AR/VR 有潜在价值。 该数据集计划包含 100 段精剪辑视频，以 120/240fps 拍摄，标注包括二维关键点（手腕、头部、剑格、剑尖）、分割遮罩、生物力学元数据和视觉风险等级，采用 JSON 格式。目前为规划阶段，尚未实际采集。

reddit · r/MachineLearning · /u/fonssagrives · 6月29日 15:16

**背景**: Sim2Real（仿真到现实迁移）是机器人学习的核心难题，指将在模拟中训练的策略成功部署到真实环境。薄物体跟踪指在视频中跟踪截面极小物体（如高速剑刃）的挑战，易受运动模糊和像素不足影响。HEMA（历史欧洲武术）是现代人对古代剑术的复原与练习。多视角高帧率拍摄有助于减少遮挡和运动模糊。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sim-2-real.com/">Sim2Real | Simulation-to-Real Transfer for Robotics</a></li>
<li><a href="https://www.ultralytics.com/glossary/object-tracking">What is Object Tracking? Computer Vision Guide | Ultralytics</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#dataset`, `#motion tracking`, `#thin-object detection`, `#Sim2Real`

---