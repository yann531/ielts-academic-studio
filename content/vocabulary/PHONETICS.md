# 音标来源与范围 · 2026-11-17

内置 767 个词条均提供 IPA。原有 38 条英式整理音标保留，页面优先显示“英”；其余显示“美”或“美 · 逐词音标”。不是把美式音标标成英式。朗读请求的浏览器语言与当前显示口音一致；浏览器声线的实际可用性取决于设备。

## 公开数据

- 数据源：[open-dict-data/ipa-dict 的 en_US.txt](https://github.com/open-dict-data/ipa-dict/blob/972cd67dd5f96bc5660e28070cde26e3928abcd7/data/en_US.txt)。固定上游提交 `972cd67dd5f96bc5660e28070cde26e3928abcd7`，不是运行时请求外部 API。
- 英文美式数据基于 [lingz/cmudict-ipa](https://github.com/lingz/cmudict-ipa) 及 CMU Pronouncing Dictionary；上游使用 syllabify 辅助添加重音。
- 所选数据和许可留在 `phonetics-us.json` 及 `licenses/`：保留 ipa-dict、cmudict-ipa 的 MIT 许可和 CMUdict 的 BSD 风格上游声明。原始整本词典没有打包进网站。
- `phonetics-supplement.tsv` 中 12 个补充项为本站 AI 辅助整理，不宣称它们在该数据集中，也未标作真人辞书编辑终审。
- 原有英式字段在 `pronunciation-forms.tsv`；与新增美式数据分别维护。未使用 ipa-dict 的 en_UK 数据。

## 短语与变体

430 个条目有完整美式条目音标，337 个条目由对应单词音标组成（包括含连字符的合成词）。逐词形式会分别显示单词及其音标，**不把机械拼接冒充整句连读、弱读或短语整体重音**。部分词有多个读音，数据按上游保留变体，学习时需结合词性和上下文。

这批数据解决覆盖与可查来源，不意味着每个读音都经过真人语音教师复核。没有可靠内置音标的个人新词提供词典查询入口，不凭拼写编造 IPA。中文释义的个人编辑不会改变发音字段。

## 重建

平常修改只需运行 `python -X utf8 scripts/curate-vocabulary.py`，不联网。刷新上游选集时，先取得上述固定版本的 TSV，再运行：

```text
python -X utf8 scripts/import-phonetics.py path/to/en_US.txt
python -X utf8 scripts/curate-vocabulary.py
```

词形不同但发音相同的英美拼写采用显式别名映射；缺失部分必须补充或报错，不填占位符。原始文件 SHA-256 记录在选集 JSON。页面只读取生成的 `src/data/vocab.json`。
