# ChatGPT 在线问答侧栏

点击网站右上角 ChatGPT 可打开或关闭侧栏，默认使用在线方式，不需要本机服务、API Key 或新增 API 费用。

1. 在学习页选中原文、题目或自己的草稿，再在侧栏点“引用选中文本”；也可手动粘贴。
2. 填写疑问，确认附上的材料。
3. 点击“复制问题并打开 ChatGPT”，在官方窗口粘贴并发送。首次使用在 chatgpt.com 登录自己的 Plus 账号，后续沿用该浏览器的官方登录状态。
4. 需要长期记录时，将回答复制到侧栏“把这次解答留下”，点击保存。问题本保留最近 60 条，可单独导出，也随完整学习备份导出。

## 实际边界

2026-11-16 实测 ChatGPT 官方主页返回 CSP `frame-ancestors 'self'`（另外列出有限的官方扩展来源），不允许本网站的 iframe 嵌入。因此没有制作会被浏览器拦截的内嵌登录框，也不代理、删改官方安全响应头。

侧栏负责提问准备与笔记，ChatGPT 在独立小窗中生成回答。本站不能读取该窗口中的账号、Plus 身份、对话和回答，不显示伪造的“Plus 已连接”状态，不声称已实现自动同步。小窗尺寸和位置由浏览器决定；手机或阻止弹窗的浏览器可能打开为标签页。若弹窗/剪贴板受限，使用侧栏提供的普通链接和完整提问文本即可。

打开官方网页仍受账号现有订阅额度限制。本站不会调用任何模型接口、申请 OAuth 权限、使用 ChatGPT Cookie、配置付款或启用额外积分。已有的“设置 → 可选模型连接”是独立功能，默认关闭，不被这个在线侧栏调用。

## 隐私与保存

问题和附文只写入本机 IndexedDB。只在点击复制时写入剪贴板；打开的 URL 固定为 `https://chatgpt.com/`，不把问题、作文或 token 放进网址。不自动上传整页、所有草稿、录音或学习档案。用户在官方窗口粘贴并发送后，内容由 ChatGPT 按其账号设置处理。

官方资料：[ChatGPT 主页和登录](https://help.openai.com/en/articles/9125172-the-chatgpt-home-page)、[Plus 权益与独立 API 计费](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus)。官方订阅授权的本地应用方案另见 [Sign in with ChatGPT](https://developers.openai.com/siwc/token-sharing-open-source)，不是本次默认在线侧栏的实现。
