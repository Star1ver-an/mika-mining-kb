#!/usr/bin/env python3
"""增量入库：把一篇公众号文章追加到 mining-kb 的对应知识卡片。

用法：
  # 直接给公众号链接（自动抓取正文）
  python tools/add_article.py --url "https://mp.weixin.qq.com/s?__biz=...&chksm=..."

  # 用本地文本（微信里复制出来的正文）
  python tools/add_article.py --file article.txt --title "标题" --account "公众号" --date 2026-11-16

  # 指定卡片，跳过自动判主题
  python tools/add_article.py --file a.txt --topic 02-geohazard

  # 只看会写到哪、不落盘
  python tools/add_article.py --file a.txt --dry-run

改完之后：
  git add -A && git commit -m "add: <标题>" && git push
再到 Kelivo 里重新导入同一个 GitHub 地址即可。
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import os
import re
import subprocess
import sys

try:  # Windows 控制台默认 cp950/cp936，避免中文输出崩溃
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../mining-kb
KB = os.path.join(ROOT, "knowledge")
SKILL = os.path.join(ROOT, "SKILL.md")

UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN"
)

# 卡片 -> (文件名, 关键词)
CARDS = {
    "01-ai-prospectivity": ("01-ai-prospectivity.md", ["找矿", "成矿", "靶区", "物探", "化探", "遥感", "勘查", "矿床", "钻探", "矿点", "大模型", "报告解读", "预测"]),
    "02-geohazard": ("02-geohazard.md", ["地质灾害", "滑坡", "泥石流", "崩塌", "危险性", "易发性", "风险区划", "InSAR", "预警", "致灾", "防治"]),
    "03-deep-earth": ("03-deep-earth.md", ["深地", "深部", "地球物理", "透明地球", "地壳", "钻探", "反射地震"]),
    "04-mineral-strategy": ("04-mineral-strategy.md", ["关键矿产", "战略性矿产", "绿色矿产", "转型矿产", "资源安全", "十五五", "供需"]),
    "05-mining-robotics": ("05-mining-robotics.md", ["矿山机器人", "智能矿山", "掘进", "采煤", "监管平台", "安全生产", "智能化"]),
    "06-policy": ("06-policy.md", ["实施意见", "自然资源部", "国常会", "政策", "开源", "立项", "规划"]),
    "07-world-model": ("07-world-model.md", ["世界模型", "表征", "空间智能", "JEPA", "预测未来"]),
    "08-physical-ai": ("08-physical-ai.md", ["物理AI", "物理 AI", "具身", "仿真", "VLA", "人形", "sim-to-real"]),
    "09-data": ("09-data.md", ["数据集", "灾害点", "预警数据", "统计数据", "shapefile", "矢量", "开放数据"]),
    "10-geology-basics": ("10-geology-basics.md", ["地质年代", "宙", "代", "纪", "定年", "演化史"]),
}


def strip_tags(s: str) -> str:
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</(p|section|div|li|h[1-6]|tr|blockquote)\s*>", "\n", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "- ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace("\u200b", "").replace("\xa0", " ")
    s = re.sub(r"[ \t\u3000]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def balanced(s: str, start_pat: str):
    m = re.search(start_pat, s)
    if not m:
        return None
    body_start = s.find(">", m.end()) + 1
    depth, pos = 1, body_start
    tag = re.compile(r"<(/?)div\b[^>]*?(/?)>", re.I)
    while True:
        t = tag.search(s, pos)
        if not t:
            return s[body_start:]
        if t.group(2) == "/":
            pos = t.end()
            continue
        if t.group(1) == "/":
            depth -= 1
            if depth == 0:
                return s[body_start:t.start()]
        else:
            depth += 1
        pos = t.end()


def fetch(url: str):
    import tempfile

    tmp = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
    tmp.close()
    try:
        subprocess.run(
            [
                "curl", "-sS", "-L", "--compressed", "--max-time", "60",
                "-A", UA,
                "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "-H", "Accept-Language: zh-CN,zh;q=0.9",
                "-H", "Referer: https://mp.weixin.qq.com/",
                "-o", tmp.name, url,
            ],
            check=True,
        )
        with open(tmp.name, encoding="utf-8", errors="ignore") as f:
            s = f.read()
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass

    if "js_content" not in s:
        raise SystemExit(
            "抓取失败：页面里没有 js_content。\n"
            "常见原因：用了短链（缺 chksm/mpshare 参数）、文章被删、或触发了风控。\n"
            "请用微信里「复制链接」得到的完整分享链接。"
        )
    title = ""
    m = re.search(r'<meta property="og:title" content="([^"]*)"', s)
    if m:
        title = html.unescape(m.group(1)).strip()
    m = re.search(r'var nickname = "(.*?)"', s)
    account = m.group(1) if m else ""
    m = re.search(r'var ct = "(\d+)"', s)
    date = _dt.datetime.fromtimestamp(int(m.group(1))).strftime("%Y-%m-%d") if m else ""
    body = strip_tags(balanced(s, r'<div[^>]*id="js_content"') or "")
    if len(body) < 100:
        raise SystemExit(f"正文太短（{len(body)} 字），可能是图片型文章，请人工确认后再入库。")
    return title, account, date, body


def detect_topic(text: str) -> tuple[str, dict]:
    scores = {}
    for key, (_, kws) in CARDS.items():
        scores[key] = sum(text.count(k) for k in kws)
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        best = "01-ai-prospectivity"
    return best, scores


def card_path(key: str) -> str:
    return os.path.join(KB, CARDS[key][0])


def existing_numbers(text: str) -> list[int]:
    """卡片内的小节编号（每张卡从 1 开始）。"""
    return [int(x) for x in re.findall(r"^## (\d+)\. ", text, flags=re.M)]


def skill_article_ids() -> list[int]:
    """SKILL.md 表格「收录」列里的全局文章编号。"""
    if not os.path.exists(SKILL):
        return []
    with open(SKILL, encoding="utf-8") as f:
        text = f.read()
    ids: list[int] = []
    for cell in re.findall(r"\| `knowledge/[^`]+` \| ([^|]*) \|", text):
        ids += [int(x) for x in re.findall(r"\d+", cell)]
    return ids


def next_global_number() -> int:
    """新文章的全局编号（继续 29、30 …）。"""
    ids = skill_article_ids()
    return (max(ids) if ids else 28) + 1


def next_section_number(key: str) -> int:
    p = card_path(key)
    if not os.path.exists(p):
        return 1
    with open(p, encoding="utf-8") as f:
        nums = existing_numbers(f.read())
    return (max(nums) if nums else 0) + 1


def append_to_card(key: str, number: int, title: str, account: str, date: str, url: str, body: str) -> str:
    p = card_path(key)
    with open(p, encoding="utf-8") as f:
        text = f.read()

    src_line = f"**原文**：{url}\n\n" if url else ""
    section = (
        f"\n---\n\n## {number}. 《{title}》\n\n"
        f"**公众号**：{account}　**发布**：{date}　**字数**：{len(body)}\n\n"
        f"{src_line}{body}\n"
    )
    # 在「## 收录文章」列表末尾追加一行（按行处理，比整块正则稳）
    lines = text.split("\n")
    try:
        start = lines.index("## 收录文章")
    except ValueError:
        start = -1
    if start >= 0:
        last_item = start
        i = start + 1
        while i < len(lines):
            if re.match(r"^\d+\. ", lines[i]):
                last_item = i
                i += 1
                continue
            if lines[i].strip() == "" and last_item == start:
                i += 1
                continue
            break
        count = sum(1 for ln in lines[start:last_item + 1] if re.match(r"^\d+\. ", ln))
        lines.insert(last_item + 1, f"{count + 1}. 《{title}》（{account}，{date}）")
        text = "\n".join(lines)
    text = text.rstrip() + "\n" + section
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    return p


def update_skill_index(key: str, number: int) -> None:
    """把新编号补进 SKILL.md 的「收录」列。"""
    if not os.path.exists(SKILL):
        return
    with open(SKILL, encoding="utf-8") as f:
        text = f.read()
    fname = CARDS[key][0]
    # 表格行形如：| AI 找矿 | `knowledge/01-ai-prospectivity.md` | 01、03、04、15 | 何时读 |
    pattern = re.compile(r"(\| `knowledge/" + re.escape(fname) + r"` \| )([^|]*)( \|)")
    m = pattern.search(text)
    if not m:
        return
    current = m.group(2).strip()
    if str(number) in [x.strip() for x in re.split(r"[、,，]", current)]:
        return
    updated = (current + "、" + str(number)) if current else str(number)
    text = text[: m.start(2)] + updated + text[m.end(2):]
    with open(SKILL, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    ap = argparse.ArgumentParser(description="把一篇公众号文章追加到 mining-kb 知识卡")
    ap.add_argument("--url", help="公众号文章链接（需完整分享链）")
    ap.add_argument("--file", help="本地正文文件（UTF-8）")
    ap.add_argument("--title")
    ap.add_argument("--account")
    ap.add_argument("--date")
    ap.add_argument("--topic", choices=sorted(CARDS), help="强制指定卡片")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.url and not args.file:
        ap.print_help()
        return 2

    if args.url:
        title, account, date, body = fetch(args.url)
        url = args.url
        for k, v in (("title", args.title), ("account", args.account), ("date", args.date)):
            if v:
                if k == "title":
                    title = v
                elif k == "account":
                    account = v
                else:
                    date = v
    else:
        with open(args.file, encoding="utf-8") as f:
            body = f.read().strip()
        title, account, date, url = args.title or "", args.account or "", args.date or "", ""

    key, scores = (args.topic, {}) if args.topic else detect_topic(title + "\n" + body)
    number = next_global_number()          # 全局文章编号（29、30…），写进 SKILL.md
    section = next_section_number(key)     # 卡内小节号（1、2、3…）

    print(f"标题   : {title}")
    print(f"公众号 : {account}　日期：{date}")
    print(f"字数   : {len(body)}")
    print(f"卡片   : {key}（{CARDS[key][0]}）")
    if scores:
        top = sorted(scores.items(), key=lambda kv: -kv[1])[:3]
        print("打分   : " + "，".join(f"{k}={v}" for k, v in top))
    print(f"文章编号: {number}　卡内小节: {section}")

    if args.dry_run:
        print("\n[dry-run] 未写入任何文件")
        return 0

    p = append_to_card(key, section, title, account, date, url, body)
    update_skill_index(key, number)
    print(f"\n已写入 {p}")
    print("下一步：git add -A && git commit -m \"add: " + title[:40] + "\" && git push")
    print("然后在 Kelivo 里重新导入同一个 GitHub 地址。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
