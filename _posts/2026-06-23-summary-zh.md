---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> 从 32 条内容中筛选出 13 条重要资讯。

---

1. [Steam Machine 正式发布](#item-1) ⭐️ 9.0/10
2. [GLM-5.2 本地运行指南与讨论](#item-2) ⭐️ 8.0/10
3. [Moebius 以 0.2B 参数实现 10B 级图像修复性能](#item-3) ⭐️ 8.0/10
4. [提示注入即角色混淆：文本风格凌驾于角色标签](#item-4) ⭐️ 8.0/10
5. [Moebius 0.2B 图像修复模型通过 WebGPU 在浏览器中运行](#item-5) ⭐️ 8.0/10
6. [加拿大计划到 2040 年建造多达 10 座 CANDU 反应堆](#item-6) ⭐️ 7.0/10
7. [Oak：专为 AI 代理设计的 Git 替代品，采用虚拟挂载](#item-7) ⭐️ 7.0/10
8. [sqlite-utils 4.0rc1 发布，新增迁移与嵌套事务支持](#item-8) ⭐️ 7.0/10
9. [Cloudflare 推出无需账户的临时 Workers 部署](#item-9) ⭐️ 7.0/10
10. [WeightsLab：面向计算机视觉的开源数据调试工具](#item-10) ⭐️ 7.0/10
11. [无需文字即可沟通的日本符号设计](#item-11) ⭐️ 6.0/10
12. [Papers with Code 新增 SOTA 徽章与热度评分](#item-12) ⭐️ 6.0/10
13. [改进的 DVD-JEPA 演示突出噪声鲁棒性](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Steam Machine 正式发布](https://store.steampowered.com/news/group/45479024/view/685257114654870245) ⭐️ 9.0/10

Valve 正式发布了 Steam Machine，这是一款开放平台的模块化游戏 PC，通过随机排队预约来确保公平性。 此次发布标志着对开放游戏硬件的重要推动，挑战了封闭式主机模式，让用户完全控制自己的设备，可能重塑 PC 游戏市场格局。 Steam Machine 采用随机预约期以防止机器人抢购，允许安装其他操作系统，并且其定价直接反映组件成本。

hackernews · theschwa · 6月22日 17:09 · [社区讨论](https://news.ycombinator.com/item?id=48632884)

**背景**: Steam Machine 是 Valve 继 Steam Deck 之后的产品，运行 SteamOS，基于用户可升级和修改的 PC 架构，它重新实现了公司将 PC 游戏带入客厅的早期愿景。

**社区讨论**: 评论赞扬了开放硬件理念和反机器人预约系统，尽管有人提到价格较高。用户欣赏真实的游戏画面，并强调拥有硬件意味着运行任何软件的自由。

**标签**: `#gaming`, `#hardware`, `#steam`, `#pc-gaming`, `#open-platform`

---

<a id="item-2"></a>
## [GLM-5.2 本地运行指南与讨论](https://unsloth.ai/docs/models/glm-5.2) ⭐️ 8.0/10

一份关于在本地运行 GLM-5.2 开源模型的指南已发布，并引发 Hacker News 讨论，用户分享了详细的硬件配置和量化技巧，在采用 512GB 内存和双 RTX 3090 GPU 的预算方案下，实现了约每秒 6 个 token 的生成速度。 这份实用指南和社区反馈降低了本地运行顶级开源大语言模型的门槛，提供了关于硬件需求和量化权衡的见解。它凸显了使强大 AI 模型访问民主化的趋势，让用户能够摆脱云 API 的依赖。 运行 GLM-5.2 的 MoE 卸载需要至少 24 GB 显存和 256 GB 内存。即使使用重度量化（Q4_K_XL），提示处理速度可能比全 GPU 加速方案慢 20 到 50 倍，使其在没有高达 5 万美元 GPU 的情况下不太实用。

hackernews · TechTechTech · 6月22日 21:21 · [社区讨论](https://news.ycombinator.com/item?id=48636377)

**背景**: GLM-5.2 是智谱 AI 开发的开源大语言模型，在设计基准测试中表现优异且具有成本效益。量化技术通过降低模型精度来减少内存占用，使大模型能在消费级硬件上运行，但可能会影响输出质量。MoE（混合专家）架构使用多个子模型，卸载时需要在 GPU 和系统内存之间传输，对内存要求很高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/technology/comments/1uc5hjh/what_is_glm52_another_opensource_chinese_ai_model/">r/technology on Reddit: What is GLM-5.2? Another open-source Chinese AI model has Silicon Valley's attention.</a></li>
<li><a href="https://medium.com/@techresearchspace/what-is-quantization-in-llm-01ba61968a51">What is Quantization in LLM. Large Language Models comes in all… | by Nithin Devanand | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区讨论既显示了热情，也揭示了实际障碍。用户分享了真实性能数据，比如在 512GB 内存和双 3090 GPU 的预算系统上达到每秒 6 个 token，但也警告说，如果没有全 GPU 卸载，提示处理速度极慢，实际上需要投资 5 万美元的硬件。许多人期待即将推出的硬件进步（如 GB10 集群）能让本地运行此类模型更加实用。

**标签**: `#AI`, `#LLM`, `#local-inference`, `#hardware`, `#quantization`

---

<a id="item-3"></a>
## [Moebius 以 0.2B 参数实现 10B 级图像修复性能](https://hustvl.github.io/Moebius/) ⭐️ 8.0/10

Moebius 发布了一个 0.2B 参数的图像修复模型，声称其性能与 10B 级模型（如 FLUX.1-Fill-Dev）相当甚至更优，同时推理速度提升超过 15 倍。该模型作为一个任务特定的专家，将高质量修复从大模型臃肿中解放出来。 这一成果挑战了高质量图像修复需要庞大模型的观念，使得在资源受限设备上高效部署成为可能，降低了物体移除、照片修复等应用的计算成本，有望让更多人使用先进的修复技术。 该模型已被 ECCV 2026 接收，输出分辨率限制为 512×512；社区反馈修复区域比周边更平滑，对新物体表现不佳。通过 ONNX 可在浏览器中运行，下载约 1.3GB。

hackernews · DSemba · 6月22日 13:53 · [社区讨论](https://news.ycombinator.com/item?id=48630171)

**背景**: 图像修复（inpainting）利用周边信息填充图像缺失或遮挡区域。模型大小以参数量衡量：0.2B 为 2 亿，10B 为 100 亿。高效模型设计旨在减少参数而不显著损失性能，以加快推理、降低资源消耗。Moebius 专注修复任务，不同于 FLUX 等通才模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hustvl.github.io/Moebius/">Moebius Project Page</a></li>
<li><a href="https://simonwillison.net/2026/Jun/22/porting-moebius/">Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code</a></li>
<li><a href="https://github.com/hustvl/Moebius">GitHub - hustvl/Moebius: [ECCV 2026] Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人对 10B 级性能说法表示怀疑，指出修复区域过度平滑且对新物体效果差。Simon Willison 的浏览器 Demo 广受好评，但 Hugging Face 上的实际测试有时失败，引发对可靠性的担忧。

**标签**: `#image-inpainting`, `#efficient-ml`, `#computer-vision`, `#model-compression`, `#generative-ai`

---

<a id="item-4"></a>
## [提示注入即角色混淆：文本风格凌驾于角色标签](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 8.0/10

一项 ICML 2026 论文发现，语言模型更看重文本风格而非显式角色标签，导致提示注入攻击成功。攻击若模仿模型自身的思考风格，成功率可达 60%，而通过‘去风格化’技术，攻击成功率可从 61%降至 10%。 这项研究揭示了大型语言模型处理结构化提示时的根本缺陷，表明风格线索会覆盖基于角色的指令，使现有安全措施失效。这凸显了除非模型能真正区分角色，否则防御提示注入将是一场持续的军备竞赛，对 AI 安全部署有深远影响。 研究在 gpt-oss-20b 等模型上进行测试，发现注入伪造推理轨迹（CoT Forgery）在 StrongREJECT 基准上取得 60%的攻击成功率。去风格化——即改写文本使其看起来不太符合预期格式——将平均攻击成功率从 61%降至 10%，表明模型依赖风格模式而非角色语义。

rss · Simon Willison · 6月22日 23:59

**背景**: 提示注入是一种网络安全攻击，利用大型语言模型无法区分开发者提示和用户输入的弱点，导致模型行为异常。LLM 使用如<system>、<user>、<assistant>等角色标签来结构化对话，但之前的研究已表明它们可以被操纵。本文引入‘角色混淆’概念，描述模型因依赖文本风格而混淆角色的现象，建立在越狱和提示注入研究的基础上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>
<li><a href="https://arxiv.org/html/2603.12277v2">Prompt Injection as Role Confusion</a></li>
<li><a href="https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/">Prompt Injection as Role Confusion</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#jailbreaking`, `#AI-safety`, `#LLM-security`, `#role-confusion`

---

<a id="item-5"></a>
## [Moebius 0.2B 图像修复模型通过 WebGPU 在浏览器中运行](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 8.0/10

西蒙·威利森将原本需要 PyTorch 和 CUDA 的 Moebius 0.2B 参数图像修复模型成功移植到 WebGPU 上，使其能在浏览器中完全运行，并发布了在线演示。 这通过客户端运行消除了服务器成本和隐私忧虑，使高级机器学习模型更易访问，并展示了 WebGPU 在 AI 工作负载方面的潜力。 该模型参数量为 0.2B；移植使用了 ONNX Runtime Web 的 WebGPU 后端；演示支持任意图像，非正方形图像会进行信箱式填充。

rss · Simon Willison · 6月22日 23:43

**背景**: 图像修复是一种填充图像中被移除或损坏部分的技术。WebGPU 是一种现代 API，允许 Web 应用直接利用 GPU。CUDA 是 NVIDIA 的专有 GPU 计算平台，常用于机器学习。将模型移植到 WebGPU 可实现无需额外安装的浏览器端机器学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU</a></li>
<li><a href="https://en.wikipedia.org/wiki/Image_inpainting">Image inpainting</a></li>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA</a></li>

</ul>
</details>

**标签**: `#webgpu`, `#image-inpainting`, `#machine-learning`, `#browser`, `#porting-to-web`

---

<a id="item-6"></a>
## [加拿大计划到 2040 年建造多达 10 座 CANDU 反应堆](https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509) ⭐️ 7.0/10

加拿大公布了一项联邦战略，计划到 2040 年建造多达 10 座新核反应堆，其中两座大型反应堆将于 2035 年前开工，利用本国铀资源和 CANDU 技术。 该计划可增强加拿大能源独立性，减少西方对俄浓缩铀的依赖，并为间歇性可再生能源提供关键基荷电力，提升核能在气候目标中的作用。 CANDU 反应堆使用天然铀无需浓缩，但批评者指出首批大型反应堆 2035 年才开工不够积极，且铀浓缩能力仍为短板。

hackernews · geox · 6月22日 19:06 · [社区讨论](https://news.ycombinator.com/item?id=48634585)

**背景**: CANDU（加拿大重水铀）是一种加压重水反应堆，使用天然铀燃料和重水慢化剂，20 世纪 50 年代起在加研发。加拿大拥有世界第三大铀储量及丰富反应堆经验，该计划与全球核能复兴趋势相符。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CANDU_reactor">CANDU reactor - Wikipedia</a></li>
<li><a href="https://www.atkinsrealis.com/en/projects/candu-technology">CANDU technology: helping Ontario achieve Net Zero – AtkinsRéalis</a></li>

</ul>
</details>

**社区讨论**: 社区情绪谨慎乐观：用户称赞 CANDU 优势和铀资源，但质疑时间表过于雄心勃勃，称其“不严肃”且开工太晚。有人建议成为全球浓缩铀供应国。

**标签**: `#nuclear-energy`, `#canada`, `#energy-policy`, `#CANDU`, `#uranium`

---

<a id="item-7"></a>
## [Oak：专为 AI 代理设计的 Git 替代品，采用虚拟挂载](https://oak.space/oak/oak) ⭐️ 7.0/10

Oak 是一个早期阶段的版本控制系统，通过虚拟挂载让 AI 代理无需完整克隆仓库即可工作，旨在提升速度并减少上下文消耗。 它针对 AI 代理在大型代码库中的效率瓶颈，有望降低 token 成本并支持并行任务，但相对于模型已深度掌握的 Git，其优势尚未被证实。 Oak 目前缺乏 CI、问题跟踪和 Windows 构建，且其虚拟挂载方法如何比 Git 的稀疏检出或工作树更降低 token 数尚不明确。

hackernews · zdgeier · 6月22日 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48631726)

**背景**: Git 工作树允许同时检出多个分支，但代理通常需要完整克隆或手动管理。Oak 引入了虚拟挂载，类似于微软的 VFS for Git，按需惰性获取文件，减少初始设置和存储。这一概念借鉴了谷歌内部大仓系统的设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git-scm.com/docs/git-worktree">Git - git-worktree Documentation</a></li>
<li><a href="https://github.blog/ai-and-ml/github-copilot/what-are-git-worktrees-and-why-should-i-use-them/">What are git worktrees, and why should I use them? - The GitHub Blog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论持怀疑态度，许多人认为 AI 模型在 Git 上的深度训练使新版本控制系统难以推广。部分人称赞惰性挂载的想法并建议基于 Git 构建，其他人则指出项目处于早期阶段且创作者低估了其进展。

**标签**: `#version-control`, `#AI-agents`, `#developer-tools`, `#show-hn`, `#git-alternative`

---

<a id="item-8"></a>
## [sqlite-utils 4.0rc1 发布，新增迁移与嵌套事务支持](https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/#atom-everything) ⭐️ 7.0/10

sqlite-utils 4.0rc1 引入了从 sqlite-migrate 移植的迁移系统，以及通过 db.atomic 上下文管理器实现的嵌套事务。这是主版本 4 的首个候选发布版。 这些功能支持生产级的模式演化与复杂事务逻辑，使 sqlite-utils 更适合稳健的应用。候选版本邀请社区在稳定版发布前进行测试。 迁移系统特意保持精简，没有反向迁移功能；嵌套事务通过 db.atomic 实现。该版本还包含少量向后不兼容的变更。

rss · Simon Willison · 6月21日 23:35

**背景**: sqlite-utils 是一个为 SQLite 数据库提供高级实用工具的 Python 库和 CLI 工具。数据库迁移管理增量式、版本控制的模式变更。嵌套事务允许在大事务内创建子事务，但只有最外层提交后更改才对外可见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for manipulating SQLite databases · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Database_migration">Database migration</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nested_transaction">Nested transaction</a></li>

</ul>
</details>

**标签**: `#python`, `#sqlite`, `#database`, `#migration`, `#release`

---

<a id="item-9"></a>
## [Cloudflare 推出无需账户的临时 Workers 部署](https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/#atom-everything) ⭐️ 7.0/10

Cloudflare 现在支持通过 'npx wrangler deploy --temporary' 命令直接部署 Workers 项目，无需注册账号，部署有效期 60 分钟。该功能虽面向 AI 代理，但对临时任务也很有用。 这降低了快速测试和原型设计的门槛，无需账号就能进行临时无服务器部署，可加速开发与实验，尤其适用于 CI/CD 流程和 AI 代理工作流。 使用 --temporary 标志，项目运行 60 分钟后自动删除；部署后会提供申请链接，可用来转为永久账号。作者用 GPT-5.5 在 Codex Desktop 中构建了重定向解析器作为实际测试案例。

rss · Simon Willison · 6月21日 22:01

**背景**: Cloudflare Workers 是一个无服务器计算平台，可在 Cloudflare 全球网络上运行代码，无需管理服务器。Wrangler 是其官方命令行工具，用于构建和部署 Workers 项目。过去必须先创建账户，现在临时部署模式省去了这一前提，方便快速试用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler · Cloudflare Workers docs</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#serverless`, `#ephemeral`, `#deployment`, `#workers`

---

<a id="item-10"></a>
## [WeightsLab：面向计算机视觉的开源数据调试工具](https://www.reddit.com/r/MachineLearning/comments/1ubwcat/datacentric_debugging_for_teams_training_neural/) ⭐️ 7.0/10

WeightsLab 经过重大改版，现已成为一款开源且原生支持 PyTorch 的工具，允许用户在训练过程中暂停以检查实时损失信号，并识别数据问题，如错误标签、类别不平衡和异常值。 数据质量问题是机器学习训练失败的主要原因之一；通过将调试直接集成到 PyTorch 工作流程中，WeightsLab 为工程师节省了大量排错时间，有助于提升模型可靠性。 该工具支持图像、视频和 LiDAR 点云数据，并与 PyTorch 训练循环无缝集成。它已在 PyPI 上发布 1.0.3 版本，并在 GitHub 上的 GrayboxTech 组织下开源。

reddit · r/MachineLearning · /u/taranpula39 · 6月21日 17:47

**背景**: 在深度学习中，错误标记的数据会误导模型训练，而类别不平衡则导致模型在少数类别上表现不佳。LiDAR 点云是通过激光扫描仪收集的三维空间数据，广泛应用于自动驾驶和地理测绘。WeightsLab 通过在训练过程中提供实时损失检查，帮助工程师及早发现数据问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://libraries.io/pypi/weightslab">weightslab 1.0.3 on PyPI - Libraries.io - security & maintenance data for open source software</a></li>
<li><a href="https://github.com/GrayboxTech">Graybx · GitHub</a></li>
<li><a href="https://www.yellowscan.com/knowledge/lidar-point-cloud-basics/">LiDAR Point Clouds: Basics for 3D Mapping by Yellowscan</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#debugging`, `#computer vision`, `#PyTorch`, `#data quality`

---

<a id="item-11"></a>
## [无需文字即可沟通的日本符号设计](https://arun.is/blog/japan-symbols/) ⭐️ 6.0/10

一篇博文探讨了日本多种符号（如新驾驶员的‘若葉’标志和‘特急’标识）如何不用文字就能优雅地传达信息。 这篇文章突显了深思熟虑的设计和文化价值观在创造直观视觉沟通中的作用，为用户体验设计和跨文化理解提供了启示。 尽管这些符号赏心悦目，但像‘特急’标志这类符号在没有事先学习的情况下仍然含义模糊，揭示了纯图形系统的局限性。

hackernews · msephton · 6月22日 19:22 · [社区讨论](https://news.ycombinator.com/item?id=48634803)

**背景**: 日本有着悠久的符号沟通历史，从传统的纹章到现代的象形图。讨论指出，许多国家也使用类似的标志（如学习驾驶员的‘L’牌），但日本的设计往往强调微妙的社会线索和对他人的体谅。

**社区讨论**: 评论者指出，像‘L’标志这样的符号在全球都存在，但日本的符号反映了礼貌文化。有人认为这类符号必须像文字一样学习，另一些人则欣赏其美学但质疑其独特性。

**标签**: `#design`, `#japan`, `#symbols`, `#culture`, `#communication`

---

<a id="item-12"></a>
## [Papers with Code 新增 SOTA 徽章与热度评分](https://www.reddit.com/r/MachineLearning/comments/1ucm508/some_new_updates_to_papers_with_code_p/) ⭐️ 6.0/10

Hugging Face 的 Niels Rogge 宣布了为复兴的 Papers with Code 平台带来的多项更新，包括当论文在某基准测试中排名前三时显示的 SOTA 徽章、结合 GitHub star 增速与相关 Hugging Face 制品热度计算的新趋势评分、对第三方评测结果的支持，以及更丰富的任务和基准集。 这些改进有助于更有效地发现高影响力研究并促进合作，顺应“研究时代”的趋势，让社区能更高效地在前人工作基础上开拓创新，并借助 Hugging Face 生态系统的丰富信号来突出重要论文。 趋势评分现在不仅考虑 GitHub star 增速，还纳入 Hugging Face 模型、数据集和 Spaces 的热度。SOTA 徽章会在各种论文流中为取得基准前三名的论文显示。外部评测则会展示诸如 FrontierSWE 和 Artificial Analysis 等独立基准的结果，超越了论文自身报告的数据。

reddit · r/MachineLearning · /u/NielsRogge · 6月22日 14:29

**背景**: Papers with Code 是一个将机器学习论文与其代码实现及基准分数关联的知名平台，旨在推动可复现研究。该平台曾一度沉寂，现由 Hugging Face 复兴以更好地服务研究社区。SOTA 徽章用于突出表现最佳的方法（例如 GLM‑5.2 在 PostTrainBench 上的成果），趋势评分则帮助发现快速上升的论文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/technology/comments/1uc5hjh/what_is_glm52_another_opensource_chinese_ai_model/">r/technology on Reddit: What is GLM-5.2? Another open-source Chinese AI model has Silicon Valley's attention.</a></li>
<li><a href="https://posttrainbench.com/">PostTrainBench</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#research tools`, `#state-of-the-art`, `#hugging face`, `#papers with code`

---

<a id="item-13"></a>
## [改进的 DVD-JEPA 演示突出噪声鲁棒性](https://www.reddit.com/r/MachineLearning/comments/1ubtf09/a_slightly_improved_dvdjepa_demo_p/) ⭐️ 6.0/10

发布了 DVD-JEPA 演示的改进版本，增加了环境噪声和像素空间基线，以提供更公平的比较，展示 JEPA 对不可预测细节的鲁棒性。 该演示直观地证实了 JEPA 的一个关键动机——忽略无关噪声的能力，正如 Yann LeCun 所强调的，有助于社区更好地理解联合嵌入预测架构相对于生成模型的实际优势。 比较使用参数数量和计算预算大致相等的模型，将线性探针和解码器成本视为与核心训练分开。该分支删除了网页演示和异常检测以聚焦核心概念，修改是在 AI 协助下快速完成的。

reddit · r/MachineLearning · /u/Kirne · 6月21日 15:49

**背景**: JEPA（联合嵌入预测架构）是一种自监督学习方法，它预测被遮挡数据的抽象表示而不是重建原始像素。原始的 DVD-JEPA 是一个基于浏览器的小型世界模型，学习预测弹跳 DVD 标志的轨迹。这个改进版本在背景中添加了视觉噪声，并引入了一个像素空间基线模型来重建像素而非嵌入，以此说明为何 JEPA 的预测表示更鲁棒。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dvd-jepa.vercel.app/">DVD-JEPA — a world model that dreams a bouncing logo</a></li>
<li><a href="https://www.digitado.com.br/a-slightly-improved-dvd-jepa-demo-p/">A slightly improved DVD-JEPA demo [P] – digitado</a></li>
<li><a href="https://medium.com/@frinktyler1445/the-anatomy-of-jepa-the-architecture-behind-embedded-predictive-representation-learning-994bfa0bffe0">The Anatomy of JEPA: The Architecture Behind embedded Predictive Representation Learning | by Tyler Frink | Medium</a></li>

</ul>
</details>

**标签**: `#JEPA`, `#demo`, `#self-supervised learning`, `#noise robustness`, `#machine learning`

---