---
name: kb-policy-ai-nr
description: 政策与开源：人工智能+自然资源实施意见八大场景逐条映射GitHub开源项目并标出空白区。问政策要求、找现成开源项目、做立项对标时用。
---

# 政策与开源供给映射

## 收录文章

1. 《对标《"人工智能+自然资源"实施意见》的 GitHub AI 项目梳理》（不存在的城市，2026-11-15 09:00）

---

# 正文
---

## 1. 《对标《"人工智能+自然资源"实施意见》的 GitHub AI 项目梳理》

**公众号**：不存在的城市　**发布**：2026-11-15 09:00　**字数**：8199　**配图**：0

**原文**：https://mp.weixin.qq.com/s?__biz=MzA4OTQ1MjMzOA==&mid=2247485124&idx=1&sn=29adea8d633f7607c4755f2494bc1f58&chksm=91f7a56098705f788ddf51fe4955085bd6ace06c7fffdfbae855f1b3b7c0187683cb8f2bde5e&mpshare=1&scene=1&srcid=1115lbZo5fpRDGZTMg0jvWB9&sharer_shareinfo=04e9e3970e5a8b598168620c89b29b6b&sharer_shareinfo_first=04e9e3970e5a8b598168620c89b29b6b#rd

# 对标《"人工智能+自然资源"实施意见》的 GitHub AI 项目梳理

> 公众号：不存在的城市　发布：2026-11-15 09:00　正文字数：8199　配图：0
> 原文：https://mp.weixin.qq.com/s?__biz=MzA4OTQ1MjMzOA==&mid=2247485124&idx=1&sn=29adea8d633f7607c4755f2494bc1f58&chksm=91f7a56098705f788ddf51fe4955085bd6ace06c7fffdfbae855f1b3b7c0187683cb8f2bde5e&mpshare=1&scene=1&srcid=1115lbZo5fpRDGZTMg0jvWB9&sharer_shareinfo=04e9e3970e5a8b598168620c89b29b6b&sharer_shareinfo_first=04e9e3970e5a8b598168620c89b29b6b#rd

政策依据：《自然资源部 国家发展改革委关于"人工智能+自然资源"的实施意见》，2026 年 11 月 4 日印发、11 月 11 日公开

一、政策框架速览
两个时间节点：2028 年形成可复制推广的示范应用；2030 年深度融入管理全链条。
5 个中试平台方向：时空地理信息、国土空间规划与治理、海洋、地质矿产、林业草原。
8 项重点应用场景：
- AI+"天空地海网"一体化监测监管

- AI+国土空间规划与治理

- AI+自然资源资产管理

- AI+自然资源灾害治理

- AI+海洋资源开发与治理

- AI+地质矿产勘查开发

- AI+林业草原保护利用

- AI+地球科学

4 项基础支撑：标准规范体系、高质量数据底座、算力基础设施、专业算法模型体系（含"一张图"算法工具库、模型协同平台、智能体集群）。
二、总体结论
把 8 个场景逐一对到 GitHub 上，得到一个非常不均衡的图景：
供给状态
场景
说明

有成熟生态，可直接复用天空地海网监测监管、实景三维支撑、林草物种识别
工业级项目，接口稳定，仍在本月提交

有硬核但窄，需二次开发灾害治理（形变监测侧）、地质矿产（工具层）
单一环节有强项目，端到端链条缺失

近乎空白，需自研自然资源资产管理（地籍）、国土空间规划与治理、海洋
最高星项目 1–6 星

一句话：政策列了 8 个方向，开源社区只在其中 3 个方向上完成了合格交付（监测监管、灾害形变、林草物种）。另外 4 个方向——资产管理、规划治理、海洋、地球科学的模型层——GitHub 上连一个能跑通业务闭环的项目都没有；地质矿产只有工具、没有模型。这不是坏消息，这是位置。
三、逐场景映射
场景 1｜AI+"天空地海网"一体化监测监管 🟢 供给充足
政策要点：多手段协同智能感知，土地利用、资源破坏、生态安全风险、矿产开采的一体化动态监测。
环节
项目
星数
状态

数据底座
OSGeo/gdal
6,154
2026-11-13 更新，事实标准

大影像推理
obss/sahi
5,603
切片推理，必用

模型训练框架
torchgeo/torchgeo
4,245
2026-11-14 更新，最活跃

遥感解译工具链
opengeos/geoai
3,474
2026-11-09 更新

GEE 封装
gee-community/geemap
4,070
在线分析首选

变化检测
ChenHongruixuan/ChangeMamba
660
TGRS 2024，当前最强基线

变化检测（持续维护）
xwmaxwma/rschange
226
2026-04 仍更新

遥感大模型
mbzuai-oryx/GeoChat
757
CVPR 2024，首个 grounded RS VLM；2024-11 后停更，勿作长期依赖

遥感大模型
TianHuiLab/Falcon
387
2026-03 更新

超高分辨率 VLM
Yunkaidang/UHR-BAT
148
ICML 2026，token 压缩思路适合大图

缺口：全在"单点模型"，没有"多源协同调度"的编排层。政策要的"一体化协同智能感知"，本质是一个调度系统，开源无对应物。
建议路径：torchgeo + sahi 搭推理底座，ChangeMamba 做变化发现，GeoChat/Falcon 做语义问答，编排层自研。
场景 2｜AI+国土空间规划与治理 🔴 近乎空白
政策要点：以 TIM 为基础，覆盖规划编制、审批、实施、监督预警全流程；用途管制推演；体检评估；要素保障与智慧选址；生态修复成效评估；城市安全韧性。
GitHub 现状：检索 "urban planning generative AI"，最高 1 星，且是学生项目。整个方向没有可用开源资产。
可借用：
能力
借什么
星数

三维场景推演与可视化
CesiumGS/cesium
15,949

AI 控制三维场景
gaopengbin/cesium-mcp
151

空间分析 Agent
mahdin75/gis-mcp
205

全栈空间分析 Agent
geumjin99/GISclaw
72

Agent-前端交互协议
ag-ui-protocol/ag-ui
17,211

缺口：TIM 模型本身、规划方案自动生成、用途管制推演、体检评估指标模型——全部无开源实现。这是 8 个场景里业务复杂度最高、开源供给最少的一块。
建议路径：不要指望找现成方案。这块的正确做法是"LLM/智能体 + 自建规则库 + 三维可视化"，参考 GISclaw 的 Agent 架构，但业务规则必须自己沉淀。
场景 3｜AI+自然资源资产管理 🔴 近乎空白
政策要点：确权登记（AI 协同解译地籍边界与建筑物）、耕地保护智能体、权益管理与资产核算。
环节
最高星项目
星数
评价

地籍/宗地自动提取
印度 hackathon 项目
1
无参考价值

建筑物轮廓提取
knwin/Building-Footprint...
29
2021 年后无更新

耕地变化监测
复用场景 1 的 ChangeMamba
660
可行

缺口：地籍边界解译是这个场景的核心，而 GitHub 上完全没有工程化实现。原因很现实——地籍数据涉密，没人能公开数据集。
建议路径：地籍 AI 只能自研，可参考 SAM 系（ViTAE-Transformer/SAMRS 384★）的提示式分割范式。耕地保护智能体可以基于场景 1 的变化检测能力封装。
场景 4｜AI+自然资源灾害治理 🟡 半空白，但有硬资产
政策要点：地灾早期识别与监测预警、海洋防灾减灾、林草防火、多灾合一。
子方向
项目
星数
状态

InSAR 时序形变insarlab/MintPy
8452026-11-07 更新，本场景最有价值的项目

InSAR 时序分析
yumorishita/LiCSBAS2
80
2026-10 更新，优先选用；原版 LiCSBAS（287★）已于 2024-11 停更

InSAR 可视化
eodeck/insar-explorer
42
QGIS 插件，可直接用

SAR 批量处理
AMSTerUsers/AMSTer_Distribution
54
自动化程度高

滑坡深度学习识别
rknaebel/landslide
56
仓库已归档只读，2019 年后无更新，仅作方法参考

SAR 滑坡检测
iprapas/landslide-sar-unet
50
论文代码

林草火灾识别
yueureka/WildFireDetection
85
U-Net 方案

火灾时序数据集
zhaoyutim/TS-SatFire
36
2025-12 更新

关键判断：地质灾害这个方向，真正的生产力工具不是"AI 检测"，而是 InSAR 时序处理。MintPy 一个项目的价值超过所有 landslide-detection 仓库的总和。政策强调"早期识别"，而早期识别在工程上就是形变速率反演——这条链路 MintPy 已经积累十余年。
缺口：预警模型（"机理+数据"双驱动）、智能叫应转移、多灾合一指挥——全部无开源实现。
建议路径：形变监测直接用 MintPy 栈；滑坡识别用 SAM/ChangeMamba 迁移；预警与应急层自研。
场景 5｜AI+海洋资源开发与治理 🔴 最空白
政策要点：空天海潜智能观测、海洋环境预报、深海极地探测、海洋化合物智能筛选。
GitHub 现状：检索 "ocean forecasting deep learning"，19 个仓库，最高 6 星，且多数是课程作业。"海洋化合物智能筛选"方向本次未检索到对应开源项目（未做穷尽检索，不作为定论）。
建议路径：这是 8 个场景中开源供给最差的。国内可关注海洋一所、海洋二所的相关模型；国际上可借鉴气象大模型（GraphCast/Pangu 系）的技术路线迁移到海洋动力预报。短期不具备"拿来即用"条件。
场景 6｜AI+地质矿产勘查开发 🟡 有工具，无模型
政策要点：多模态数据融合预测、隐伏矿体智能识别、智能勘查装备、境外资源潜力评价。
项目
星数
说明

GispoCoding/eis_toolkit
57
芬兰地质调查局的找矿预测 Python 库，唯一工程化项目（2025-07 后无更新，仍在维护状态待观察）

GispoCoding/eis_qgis_plugin
17
对应的 QGIS 插件

Abdallah-M-Ali/Mineral-Prospectivity-Mapping-ML
41
论文级实现

XploraHub/awesome-mineral-exploration
38
2026-11-05 新建，矿产勘查开源软件清单，值得订阅

缺口：隐伏矿体识别、多模态融合预测模型——无开源。eis_toolkit 提供的是传统证据权法/逻辑回归的工程封装，深度学习找矿仍是空白。
建议路径：eis_toolkit 作为基线工具链，深度学习部分需自研；关注 XploraHub 清单的更新，它是这个方向唯一在维护的索引。
场景 7｜AI+林业草原保护利用 🟢 有生态，需适配
政策要点：国家公园旗舰物种保护、野生动植物智能识别与追踪、森林资源与树木生长监测、林草防火。
项目
星数
说明

agentmorris/MegaDetector346红外相机物种检测事实标准，2026-11-10 更新，生态活跃

microsoft/Biodiversity1,091微软 AI for Good 生物多样性中心，项目目录 + 文档，2026-11-13 更新

microsoft/MegaDetector-Classifier
6
官方分类微调仓库，是 MegaDetector 体系的分类环节，星数低但直属主生态

stangandaho/declas
13
红外相机物种检测分类软件，2026-11 更新

yueureka/WildFireDetection
85
火灾识别（同场景 4）

关键判断：红外相机物种识别这一细分领域，微软 MegaDetector 生态是事实标准，主仓 346 星、配套的 Biodiversity 中心 1,091 星，均在本月仍有提交。上一版仅按单一分类仓库的 6 星判断"薄弱"，低估了该方向的实际供给——林草物种识别是可用的，不属于空白区。
真正的缺口：森林资源与树木生长监测、林草产业相关模型，GitHub 上无对应实现。
建议路径：物种识别直接接 MegaDetector 生态；林草火险预测需自研（FireWeather Index 类模型）。
场景 8｜AI+地球科学 ⚪ 待观察
政策要点：地球科学 AI 超级大脑，多圈层相互作用与协同演化机制模拟。
GitHub 现状：这是一个偏科研的方向，开源资产分散在地震学、地球物理、气候模拟各子领域，没有统一的"地球科学 AI"项目。本次未做穷尽检索。
可参考：google-deepmind/mujoco（17,936★，物理仿真）、SkySense 系列（多模态遥感基础模型）。
四、支撑层映射（对应"建强智能底座"）
政策要求
开源对应物
星数
差距

数据底座（地上地下、陆海统筹、三维立体）
GDAL + torchgeo
6,154 / 4,245
缺少"三维立体"统一数据模型

算法模型体系、智能体集群
gis-mcp / cesium-mcp / GISclaw
205 / 151 / 72
有原型，无行业级实现

地理空间信息嵌入引擎
geoai
3,474
最接近的一项

实景三维场景（灾害、城市）
3DGS 全家桶 + COLMAP + ODM
24,471 / 13,221 / 6,603
供给最充足
模型评测与安全标准
无
-
完全空白

实景三维方向单独展开（这是供给最充足的方向）：
项目
星数
许可证
用途

graphdeco-inria/gaussian-splatting
24,471
非商业3DGS 原始实现（Inria 自定义许可，禁止商用；2025-10 后停更）

colmap/colmap
13,221
宽松（BSD 系）
SfM/MVS 标准工具

playcanvas/supersplat
10,641
MIT
3DGS 编辑器，浏览器端

OpenDroneMap/ODM
6,603
AGPL-3.0无人机影像→点云/DEM/三维模型，2026-11-13 更新

dreamgaussian/dreamgaussian
4,365
—
生成式三维

hustvl/4DGaussians
4,026
—
动态场景

MrNeRF/LichtFeld-Studio
3,997
GPL-3.0
原生 3DGS 训练编辑应用，2026-11-13 更新

sparkjsdev/spark
3,903
MIT
three.js 的 3DGS 渲染器

mapillary/OpenSfM
3,819
BSD-2
开源 SfM 管线

WebODM/ODX
113
AGPL-3.0
ODM 新一代，2026-04 新建

注意：3DGS 目前主要解决"好看"，解决"可量测"仍要靠传统摄影测量。实景三维要做汇交、入库、量算，COLMAP/ODM 的成果比 3DGS 更可靠；3DGS 适合做展示层。
五、四个可直接动手的切入点
按"投入产出比"排序，不按政策重要性排序：
1. "一张图"智能体集群（对应支撑层，最匹配现有技术栈）政策明确要建"智能体集群"。开源侧 cesium-mcp 提供了 62 个三维场景控制命令、gis-mcp 提供了 GIS 操作工具集，但没有一个把"数据查询 + 空间分析 + 三维呈现"串成完整业务智能体。这是缺口，也是投入最小的入口。
2. 实景三维 + 灾害推演（对应场景 4，供给最充足）3DGS/ODM/COLMAP 三件套现成，政策要求"建设灾害实景三维场景，动态推演灾情演化"。技术链路完整，缺的是把 MintPy 的形变数据、3DGS 的场景、Cesium 的呈现接起来。
3. 变化检测业务化（对应场景 1、3）ChangeMamba 已验证，sahi 解决大图，缺的是"图斑提取→核查→分发→整改"的闭环。黄山市的公开案例显示这条路已经走通（9678 平方公里全覆盖，发现疑似图斑 104 个），可复制的正是工程化部分。
4. 地籍 AI（对应场景 3，纯空白）风险最高但壁垒也最高。参考 SAMRS 的提示式分割范式，需要自有标注数据。适合有数据资源的单位做，不适合从零起步的团队。
六、许可证核查
上一版只看了星数和活跃度，漏掉了许可证——而这个领域往往要交付给政府客户或做成产品，许可证比星数致命。
项目
许可证
风险等级
说明

graphdeco-inria/gaussian-splatting
非商业许可🔴 高
Inria/MPII 自定义许可，仅限研究非商业用途。任何商业交付都不得直接使用

OpenDroneMap/ODM
AGPL-3.0🟠 中高
做成对外 Web 服务会触发开源义务；内网自用风险较低

WebODM/ODX
AGPL-3.0
🟠 中高
同上

geumjin99/GISclaw
AGPL-3.0
🟠 中高
作为架构参考没问题，直接改成产品需评估

insarlab/MintPy
GPL-3.0
🟡 中
独立进程调用可规避；与自有代码静态链接则有传染性

yumorishita/LiCSBAS / LiCSBAS2
GPL-3.0
🟡 中
同上

MrNeRF/LichtFeld-Studio
GPL-3.0
🟡 中
3DGS 的可替代实现，仍受 GPL 约束

obss/sahi / torchgeo / geoai / geemap
MIT
🟢 低
可放心商用

playcanvas/supersplat / sparkjsdev/spark
MIT
🟢 低
3DGS 的商业安全替代品
colmap/colmap / mapillary/OpenSfM
BSD 系
🟢 低
可放心商用

gaopengbin/cesium-mcp / mahdin75/gis-mcp
MIT
🟢 低
可放心商用

mbzuai-oryx/GeoChat、ViTAE-Transformer/SAMRS 等
无许可声明🔴 高
仓库无 LICENSE 文件，法律上默认"保留所有权利"，不可直接商用，需联系作者或改用替代实现

Belluxx/Aleph
MIT
🔴 高
许可宽松，但数据获取违反 Google 条款，风险在数据不在代码

bilawalsidhu/gods-eye-view
自定义
🟠 中高
底图涉及 Esri/Google，国内交付不合规

三条实操结论：
- 3DGS 不能默认用原始实现。Inria 那个 24,471 星的仓库是非商业许可，很多团队直接拿来改就交付了，这是真实的法律风险。商业项目请用 supersplat（MIT）或 spark（MIT）做渲染，LichtFeld-Studio（GPL）做训练工具。

- ODM 的 AGPL 要看交付形态。内网部署给自己用，问题不大；打包成 SaaS 或交付给第三方运营，必须开源服务端。

- 优先 MIT/Apache/BSD：sahi、torchgeo、geoai、cesium-mcp、gis-mcp 全在这条线上，够用。

七、风险与合规（本领域不可跳过）
- 数据不出境：涉及高精度地形、DOM/DEM、实景三维的项目，模型必须本地部署。上表推荐的开源项目全部满足（torchgeo/ChangeMamba/MintPy/3DGS 均可离线）。

- 底图合规：三维场景必须用合规底图并标注审图号。gods-eye-view（64,783★）的架构可借鉴，但 Esri + Google 3D Tiles 的底图组合不能用于国内交付。

- 影像来源合法性：Aleph（882★）通过 Google 未公开 API 抓取影像与街景，作者自述违反其条款，不得进入交付系统。

- 测绘资质：地籍、实景三维类项目涉及测绘活动，成果使用受资质约束，开源项目不改变这一点。

八、项目速查表
场景
首选项目
星数
许可证
成熟度

天空地监测
torchgeo / sahi / geoai
4,245 / 5,603 / 3,474
MIT
生产可用

变化检测
ChangeMamba
660
Apache-2.0
需工程化

遥感大模型
GeoChat / Falcon
757 / 387
未标 / MIT
研究级，GeoChat 已停更

规划治理
cesium-mcp + gis-mcp
151 / 205
MIT
原型

资产管理
无（复用变化检测）
-
-
空白

灾害-InSAR
MintPy（+ LiCSBAS2）
845
GPL-3.0
生产可用

灾害-火灾
WildFireDetection
85
CC0
需工程化

海洋
无
6
-
空白

地质矿产
eis_toolkit
57
EUPL-1.2
工具级

林草物种
MegaDetector 主仓346MIT
生产可用

实景三维
COLMAP / ODM / spark
13,221 / 6,603 / 3,903
BSD / AGPL / MIT
生产可用（注意 ODM 为 AGPL）

说明：星数为 2026-11-14 快照；"成熟度"判断依据 README 功能完整度与最近提交时间，非主观印象。政策引文摘自自然资源部官方发布文本。
