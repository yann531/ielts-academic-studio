# 研究与选择记录

2026-11-13。优先查阅原始网站，未抓取或公开受限教材。

## 权威结构

IELTS.org Academic 样题页面用于核对：听说 A/G 共用、学术阅读写作独立；听力 4 部分 40 题、阅读 3 篇 40 题、写作 2 项、口语 3 部分。Cambridge English 官方备考页当前列出 IELTS 21 Academic、Mindset、The Official Cambridge Guide；只收录 Academic 适用部分。British Council 的公开评分页面与 IELTS.org 写作/口语量表是反馈导读依据。UQ College 介绍 IELTSx 四科系统课程；免费学习与证书/平台期限需到 edX 确认。

- https://ielts.org/take-a-test/preparation-resources/sample-test-questions/academic-test
- https://www.cambridgeenglish.org/exams-and-tests/ielts/preparation/
- https://takeielts.britishcouncil.org/teach-ielts/test-information/assessment
- https://ielts.org/take-a-test/preparation-resources/writing-test-resources
- https://uqcollege.uq.edu.au/study/english-studies/ieltsx

完整分类目录在 `src/data/resources.json`。资料整理日期不表示所有源站在所有地区都保证可访问；`pnpm check:links` 留下逐链接网络检测结果。

## GitHub 候选考察

考察包括原仓库信息、README、目录和部分关键文件；未执行候选项目。Star 为观察时快照，不作为选型理由。

| 项目 | 借鉴点 | 许可/内容/运行限制 |
|---|---|---|
| [RealKai42/qwerty-learner](https://github.com/RealKai42/qwerty-learner) | 成熟的拼写、听音和即时回忆交互；观察时约 2.37 万 Star | GPL-3.0；未复制代码或词库，避免把键入等同掌握 |
| [aimerfeng/ists](https://github.com/aimerfeng/ists) | 日任务、错题队列、导入与练习闭环 | MIT；服务器/SQLite 架构较重，缺少口语；少题正确率放大为 40 题的做法不采用，不读取其他应用凭据 |
| [TuuuuTuu/ielts-speaking-practice](https://github.com/TuuuuTuu/ielts-speaking-practice) | P1–3 关联、准备计时、录音与素材 | 小型 seed 题库；README 标 MIT 但未见独立 LICENSE，作为交互参考 |
| [Jim-Elijah/fluent-any-lang](https://github.com/Jim-Elijah/fluent-any-lang) | 本地媒体、影子跟读、IndexedDB 与备份 | README/package 声明 MIT，根目录未见 LICENSE；默认不含完整雅思材料，外部发音服务不等于零依赖 |
| [Pandlagon/IELTS-Studio](https://github.com/Pandlagon/IELTS-Studio) | 分栏、题目导入与阅读交互 | Vue + Java/MySQL，静态托管不适合；MIT 徽标与“仅学习、非商业”说明存在歧义，未复制源码 |
| [thinkall/easyIELTS](https://github.com/thinkall/easyIELTS) | 四科流程与私有卷隔离思路 | 偏 General Training、需要语音/模型和服务器；未见明确许可，不复用题库和源码 |

本项目选择 React + TypeScript + Vite 静态核心，自己实现界面、判分、间隔复习和内容结构。没有依赖第三方 CORS 代理抓取试卷，也没有从其他软件读取凭据。
