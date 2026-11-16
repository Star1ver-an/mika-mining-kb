# 增量入库工具

把一篇新的公众号文章追加到知识库对应卡片，并同步更新 `SKILL.md` 的收录编号。

## 用法

```bash
# 1) 直接给公众号完整链接（自动抓正文）
python tools/add_article.py --url "https://mp.weixin.qq.com/s?__biz=...&chksm=...&mpshare=1..."

# 2) 微信里复制出来的正文存成 txt，再入库
python tools/add_article.py --file article.txt --title "标题" --account "公众号" --date 2026-11-16

# 3) 自动判主题不准时，强制指定卡片
python tools/add_article.py --file article.txt --topic 02-geohazard

# 4) 先看看会写到哪，不落盘
python tools/add_article.py --file article.txt --dry-run
```

卡片名：`01-ai-prospectivity` `02-geohazard` `03-deep-earth` `04-mineral-strategy`
`05-mining-robotics` `06-policy` `07-world-model` `08-physical-ai` `09-data` `10-geology-basics`

## 行为

1. 抓取/读取正文 → 抽标题、公众号、日期
2. 按关键词给 10 张卡打分，落到最高分那张（无命中则落 01）
3. 追加一节 `## N. 《标题》`（N 为全库递增编号），并在「收录文章」列表补一行
4. 更新 `SKILL.md` 表格里该卡的「收录」列
5. 打印下一步的 git 命令

## 注意

- **必须用完整分享链接**（带 `chksm`/`mpshare` 参数）。短链会返回空壳页面，脚本会直接报错退出。
- 图片型文章（正文很短、图很多）会被判为「正文太短」而拒绝，需人工决定是否入库。
- 脚本只做本地文件修改，不联网提交；push 需要你自己执行。
