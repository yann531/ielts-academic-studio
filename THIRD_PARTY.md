# 第三方与素材说明

- React / React DOM：MIT。
- Vite、Vitest、Lucide React、@vitejs/plugin-react：MIT。
- TypeScript：Apache-2.0。
- 实际依赖版本与依赖树由 `pnpm-lock.yaml` 锁定；完整许可见各依赖包。无复制其他 IELTS 仓库的源码或题库。
- 内置图表、几何插画、图标排版和全部题目、词义说明、例句为本项目独立编写（AI 辅助）。Lucide 图标使用其软件许可。
- `public/audio/*.wav`：本机 Microsoft Zira Desktop 声线从本站原创脚本离线合成；16 kHz、16-bit mono。不是 IELTS 官方录音，也不声称真人、多口音或标准考试速度。重建脚本需 Windows System.Speech 及该已安装声线；其他平台直接使用已生成文件。
- 浏览器词汇/问题朗读：系统 SpeechSynthesis，声音和离线可用性取决于设备。未将其当作官方录音或发音评价。
- 外链 IELTS、Cambridge、British Council、IDP、UQ、Oxford 和其他机构的商标、PDF、书籍、视频与网页内容归各自所有。本站许可不扩展到这些资源。
- 网页使用本机系统字体，无第三方字体 CDN、分析追踪、广告或隐藏上传。
- 1.4.1 新增美式 IPA 选集来自 open-dict-data/ipa-dict 的 en_US（固定提交 `972cd67dd5f96bc5660e28070cde26e3928abcd7`），基于 lingz/cmudict-ipa / CMU Pronouncing Dictionary。保留 MIT 许可和署名于 `content/vocabulary/licenses/`；未使用该项目 en_UK 数据。少量补充音标由本站整理，短语明确标记为逐词音标，详见 `content/vocabulary/PHONETICS.md`。
