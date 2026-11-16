# 内容格式、导入与贡献

内置内容位于 `src/data/`，UTF-8 JSON，与界面分离。运行 `pnpm check:content` 和 `pnpm test` 后再提交。

## 客观题 Paper

参考可下载示例 `public/examples/paper.json` 和 TypeScript 定义 `src/types.ts`。顶层必须有：

`id, skill, title, subtitle, minutes, source, kind, review, updated, difficulty, passages`。

`skill` 仅为 `reading` 或 `listening`。段落对象 `id,title,paragraphs,questions`；`paragraphs` 是 `{label,text}` 数组；听力 `audio` 为本站 `audio/` 路径、HTTPS 原始音频或个人导入的 `data:audio/`。生产外链可能受防盗链或 CORS 影响，个人导入后可在资料架附加本机音频。

题目：`id,type,prompt,answers,evidence,explanation`。`type` 是 `text` 或 `select`；填空有 `maxWords`，选项题有 `options`。答案是完整可接受字符串数组；选择题答案必须直接存在于 options。可另有 `paraphrase,trap`。True/False/Not Given、Yes/No/Not Given 都作为选项题；不可把两套标签混用。

判分只统一 Unicode 宽度、大小写、空白和弯引号，不擅自删标点、词尾或冠词。连字符词和缩略词视作一个词，时间与小数为一个数字 token。不同可接受写法需要明确列入 answers。校验会拒绝空答案、重复题号和不安全音频协议。

每篇给证据位置与解释；有明确相反才判 False/No，信息不足为 Not Given。题目不能靠文章外常识回答。当前数据是教学练习，篇幅/题型不足要直接说明，不能宣称“完整官方真题”。

个人导入时会添加 `user-` 命名空间并标作“个人导入”，按 ID 合并；不会覆盖内置题目。自有完整卷可以导入，PDF 不会自动 OCR 成可靠题库；请人工整理、核对。

## 词库 Word

JSON 数组，每条：`id,term,pos,meaning,topic,collocation,example,register,error,kind,source`；`kind` 是 `word`/`phrase`。JSON 字段需完整；CSV 至少 `term,meaning`，其余可按模板补充。CSV 支持带引号、逗号、换行。导入前预览，英文忽略大小写和多余空白去重。

优先常用学术、公共议题与听说场景；不将词表标为官方。例句自然且能说明具体义项。CEFR 等级如未经核实不标到单词。发音提供浏览器朗读与词典链接，未伪造 IPA。

## 写作、口语与来源审阅

写作需准确任务指令、图表（Task 1）、分析、具体思路、提纲、错误提醒、来源与审核说明。示例至少达到该任务字数，不标未经考官确认的分数。口语主题关联 P1、P2 cue points 和 P3，鼓励真实经历而非记忆稿。

每次内容贡献应说明：原始出处/自编、许可、是否 AI 辅助、谁检查了答案/语言、尚存问题与检查日期。先在 PR 讨论质量，再进入默认题库。没有真人考官终审就如实标记，自动化检查不代表教学认证。

## 重建与持续更新

首批内容来源脚本：`seed-content.py` → `seed-listening.py`；另有 `seed-production.py`、`seed-vocab.py`。**脚本会覆盖对应 JSON**，维护时择一作为真源或同步修改两处。只有改变听力脚本后才在 Windows 运行 `make-audio.ps1` 重建音频，并重新核对。

更新 `CHANGELOG.md`、题目 updated 与审核说明。资源 URL 每月低频检查；403、429、地区限制和超时列人工复查，404/410 才直接报告断链。维护者可根据 GitHub Actions 产物处理，不自动抓取付费书籍。
