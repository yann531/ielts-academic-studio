# 手动发布到 GitHub 与 GitHub Pages

网站已支持仓库子路径、hash 路由与 GitHub Actions 构建，无需购买服务器或配置 API Key。

## 推荐：浏览器建仓库，PowerShell 上传

### 1. 新建空的公开仓库

打开 https://github.com/new，仓库名建议 `ielts-academic-studio`，选择 **Public**。不要勾选添加 README、.gitignore 或许可证，因为本地已经有这些文件。创建仓库。

### 2. 在本机项目目录提交

在 PowerShell 逐行运行（不要把 YOUR_USERNAME 原样保留）：

```powershell
cd D:\english
git init -b main
git add .
git status --short
git commit -m "Build IELTS Academic Studio"
git remote add origin https://github.com/YOUR_USERNAME/ielts-academic-studio.git
git push -u origin main
```

`git status --short` 应只包含源代码、内置原创材料、公开音频、文档和配置。`.gitignore` 已排除 `private/`、`releases/`、`node_modules/`、`.tools/`、`.pnpm-store/`、`dist/`、密钥与日志。不要强行 `git add -f` 这些目录。**网页文件上传不会自动遵循 .gitignore，因此更推荐 Git 上传。**

如果提示缺少提交身份，只设置当前仓库：

```powershell
git config user.name "你的 GitHub 用户名"
git config user.email "你在 GitHub Settings → Emails 中的 noreply 邮箱"
git commit -m "Build IELTS Academic Studio"
```

不要在公开提交中填写不想公开的私人邮箱。GitHub 不支持把网站登录密码作为 HTTPS Git 密码。出现登录提示时走官方浏览器认证，不需要把密码或 token 发给任何人。

如果本机 GitHub CLI 提示旧登录失效，可在你自己的终端登录正确账号：

```powershell
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
git push -u origin main
```

提交 `.github/workflows/` 如出现 workflow 权限错误，再按 GitHub 提示补充对应权限：`gh auth refresh -h github.com -s workflow`。只在官方 GitHub 页面自行完成授权，不把密钥写进项目。

若提示 `remote origin already exists`，先 `git remote -v` 核对；只有确认要替换时再执行 `git remote set-url origin 你的仓库地址`。若远程已有 README 等提交，不要强推覆盖，先保留远程文件再合并，或改用一个新的空仓库。

### 3. 开启 Pages

在仓库打开 **Settings → Pages → Build and deployment → Source → GitHub Actions**。

转到 **Actions → Check and publish Pages**。如果首次运行因尚未开启 Pages 而失败，开启后点 **Re-run all jobs**；也可使用 Run workflow 手动运行。等待 `build` 和 `deploy` 都通过。

网页地址通常为：

```text
https://YOUR_USERNAME.github.io/ielts-academic-studio/
```

以 Pages 设置页或工作流 `deployment` 给出的实际地址为准。源码仓库地址不是学习网站地址。

### 4. 上线验收

- 首页和四科入口可用，无空白页或 404。
- 听力可播放，阅读答题后可查看证据。
- 写作刷新可恢复；词汇复习后今日新词计数变化。
- 口语录音在 HTTPS 下手动允许麦克风后测试，再导出。
- 设置页导出备份，必要时下载离线资料包。

本机开发网址与 GitHub Pages 不共享 IndexedDB；需要迁移学习数据时，在旧网址导出 JSON，再在新网址导入。`D:\english\private\` 内的备份和私人材料不要上传 GitHub。

## 不想使用命令行：GitHub Desktop

从 https://desktop.github.com/ 安装官方客户端并登录。

1. File → New repository，Name 填 `ielts-academic-studio`，Local path 选 `D:\`，先建立 `D:\ielts-academic-studio`。
2. 从交付压缩包解压项目，将项目内容复制到这个新仓库根目录，保留 `.gitignore` 和 `.github`；不要复制 `private`、依赖目录或临时工具。
3. 在 Changes 里检查文件，Commit to main；Publish repository，取消 “Keep this code private” 后发布为公开仓库。
4. 按上面的步骤开启 Pages、检查 Actions。若新仓库最初的默认分支不是 main，先在客户端/仓库设置中改为 main，或对应修改工作流。

不要把 ZIP 文件本身当作网站上传。GitHub Releases 中的 ZIP 只能作为下载包，不能自动变成 Pages 网站。

## 后续更新

修改项目内容，先运行 `pnpm test`、`pnpm check:content`、`pnpm build`；然后：

```powershell
git add .
git commit -m "Update study content"
git push
```

工作流会自动重建部署；已有学习数据仍保存在原网址的浏览器中。若修改用户名、仓库名或域名，先备份。设置页的源码链接默认指向 `oxazoline/ielts-academic-studio`；使用其他仓库时请在 `src/pages/Library.tsx` 替换该链接。

## 每周自动更新

公开仓库免费托管。Pages 启用后，在 Actions 找到 **Weekly question bank release**，可先手动 Run workflow 验证。此流程自带 `contents: write`、Pages 与 OIDC 权限，用于提交已发布的公共题目及部署；无需添加任何 API 密钥。仓库规则若禁止机器人直接提交 main，需要由仓库所有者调整相应规则或改成人工合并流程。

每周日 12:00 UTC（北京时间 20:00）发布下一预备包，当前备有四周。补充时按 batch-005.json 等编号添加同结构数组，先检查答案、证据和原创来源。不要手动清空 released.json。网站会在打开时每七天检查内容，也可在每周计划页点“检查题库更新”。更新频率不是无限生成能力。

## 每日课程是否需要联网

每日排课、自动顺延和作答存档不需要服务器。GitHub Pages 只需沿用前面的公开仓库及 Actions 发布步骤，没有新服务、数据库、密钥或收费配置。

已有仓库更新：在 D:\english 中依次执行 `git add .`、`git commit -m "Add daily lessons and rollover"`、`git push`，等待 Actions 构建部署。首次建仓库则按本文开头操作。发布后先导出学习备份，再刷新页面；如果启用过离线包，联网重新打开设置，等待新版缓存更新。不要清空浏览器数据，否则会删除本机进度。

首次访问需联网加载；安装离线包后可断网练习。本站不会自动跨手机/电脑同步，GitHub Pages 也不提供个人数据数据库。换设备请在设置导出 JSON 备份，再在目标设备导入合并。
