# mika-mining-kb

矿业知识库技能包，供 Kelivo 通过 GitHub 导入。

## 导入方法

在 Kelivo：设置 → 工作区与环境 → 技能 → 导入技能 → **从 GitHub**，粘贴：

```
https://github.com/<你的账号>/mika-mining-kb/tree/main/mining-kb
```

导入后是一个技能 mining-kb，内含 11 个知识文件（knowledge/），模型按需 read_file 读取。

## 内容

- 28 篇微信公众号文章，正文合计 10.9 万字
- 主题：AI找矿、地质灾害（重点）、深地科学、矿产战略、矿山机器人、政策、世界模型、物理AI、数据资源、地质基础
- mining-kb/knowledge/11-maintenance.md 是新文章入库规则

## 更新

改 mining-kb/ 下的文件 → commit → push → 在 Kelivo 里重新导入同一个 URL 即可覆盖。