# mika-mining-kb

矿业知识库技能包，供 Kelivo 通过 GitHub 导入。

## 导入方法

在 Kelivo：设置 → 工作区与环境 → 技能 → 导入技能 → **从 GitHub**，粘贴：

```
https://github.com/Star1ver-an/mika-mining-kb/tree/main/mining-kb
```

导入后是**一个**技能 `mining-kb`，内含 11 个知识文件（`knowledge/`），模型按需 `read_file` 读取。

## 内容

- 28 篇微信公众号文章，正文合计 10.9 万字
- 主题：AI找矿、地质灾害（重点）、深地科学、矿产战略、矿山机器人、政策、世界模型、物理AI、数据资源、地质基础
- `mining-kb/knowledge/11-maintenance.md` 是新文章入库规则

## 新增文章

```bash
# 直接给公众号完整链接（自动抓正文）
python mining-kb/tools/add_article.py --url "https://mp.weixin.qq.com/s?__biz=...&chksm=..."

# 微信里复制出来的正文存成 txt
python mining-kb/tools/add_article.py --file article.txt --title "标题" --account "公众号" --date 2026-11-16

# 自动判主题不准时强制指定
python mining-kb/tools/add_article.py --file article.txt --topic 02-geohazard

# 只看会写到哪，不落盘
python mining-kb/tools/add_article.py --file article.txt --dry-run
```

脚本会：判主题 → 追加到对应卡片 → 更新「收录文章」列表 → 更新 `SKILL.md` 的收录编号。
详见 [mining-kb/tools/README.md](mining-kb/tools/README.md)。

## 更新

```bash
git add -A && git commit -m "add: <标题>" && git push
```

然后在 Kelivo 里重新导入同一个 URL 即可覆盖（不用重装、不用换地址）。

## 注意

- 公众号链接必须是**完整分享链**（带 `chksm`/`mpshare`），短链会返回空壳页。
- 图片型文章（正文很短、图很多）入库前请人工确认，文字通道覆盖不到图内信息。
