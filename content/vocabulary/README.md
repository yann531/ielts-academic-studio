# 可维护词汇批次

页面读取 `src/data/vocab.json`；此目录是它的可审阅来源，不保存学习者记录。

- `legacy-base.json`：旧 700 条原始基线，仅用于保持 ID。包含旧文案，不直接用于页面。
- `quality-core.tsv`、`quality-social.tsv`：旧核心词的释义、搭配中文、例句译文和具体辨析。
- `quality-extra.tsv`、`meanings-extra.tsv`：226 条扩展词的中文资料。
- `additions.tsv`：新增和重点重写条目；按规范化词条去重，已有词沿用旧 ID。
- `example-revisions.tsv`、`examples-academic.tsv`、`examples-core.tsv`：语境重写及对应译文，后批次优先；旧搭配子卡同步译文。
- `pronunciation-forms.tsv`：有把握的英式音标、词形和显式可接受拼写变体，未覆盖的留空，不伪造。
- `phonetics-us.json`、`phonetics-supplement.tsv`：固定来源的美式音标选集及缺失项补充；来源、许可与短语分词规则见 [音标说明](PHONETICS.md)。

格式用 `|` 分隔，首行 `#` 为注释。修改后运行 `python -X utf8 scripts/curate-vocabulary.py`。脚本确定性生成，不需要在线接口，重复运行不会增加重复词条。新增批次应检查词义、自然搭配、译文一致性和是否保留既有 ID。不要用通用提示代替具体辨析。

选编来源、核查限度、数量与手动验收见 [交付说明](../../docs/VOCABULARY-V2.md)。词典链接的 `lookup` 表示查证入口，`reference` 才表示具体参考页面；不把生成的链接当作已逐页审阅的证据。此次没有逐页核验全词库，没有真人雅思教师终审。
