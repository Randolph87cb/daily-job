---
name: atcoder-statement-bilingual-pdf
description: 处理 AtCoder 比赛题面的抓取、翻译和导出。适用于用户给出 AtCoder 比赛链接或 contest id，希望复用 `browser-session-manager` 管理的登录态批量提取整场比赛英文题面；如果未登录则自动弹出浏览器完成登录、保存会话，再继续生成逐段穿插的中英对照 Markdown，并导出单题 PDF 与整场合并 PDF。
---

# AtCoder 双语题面导出

## 概览

- 这个 skill 自带运行所需脚本与词表，不依赖外部项目目录。
- 当前保留的主流程只有一条：
  - 默认复用 `browser-session-manager` 管理的 AtCoder `profile` 会话
  - 必要时通过 `browser-session-manager -ManualOpen` 打开真实 Chrome / Edge profile 窗口完成人工登录
  - 登录阶段优先使用完整 profile 通过 Cloudflare
  - 抓取阶段优先复用保存下来的会话 cookie 直接请求 `tasks_print?lang=en`
  - 对偶发的 TLS / SSL EOF 或连接关闭，抓取阶段会先做有限次重试
  - Windows 下如果 Python `requests` 遇到 TLS / SSL 兼容问题，会自动回退到 PowerShell `Invoke-WebRequest`
  - 只有前两条都失败时才回退 Playwright
  - 翻译成逐段中英对照 Markdown
  - 导出每题一个 PDF
  - 额外导出整场合并 Markdown 和整场合并 PDF

## 资源

- `scripts/fetch_atcoder_tasks.py`
- `scripts/translate_markdown.py`
- `scripts/run_atcoder_pipeline.py`
- `scripts/atcoder_better_turndown.cjs`
- `translation_assets/algorithm_glossary.json`
- `package.json`

首次在新环境使用时，如果 `node_modules/` 不存在，先在 skill 根目录运行：

```powershell
npm install
```

## 使用前提

- 当前工作目录中存在可用的 `.env`，至少包含：
  - `OPENAI_API_KEY`
  - `OPENAI_API_MODE=chat`
  - `OPENAI_BASE_URL=...`
  - 如需统一指定模型，额外设置 `OPENAI_MODEL=...`
  - 如需统一指定思考强度，额外设置 `OPENAI_REASONING_EFFORT=...`
- 本机已可调用：
  - `python`
  - `node`
  - `md2pdf`
- 已安装全局 skill：
  - `browser-session-manager`
- 当前 Python 环境已安装 Playwright：
  - `python -m pip install playwright`
- 当前 Node 环境可运行 Playwright CLI：
  - `npx playwright --help`

默认不要求你预先登录 AtCoder。脚本会先检查全局会话；如果没有登录或登录已失效，会自动弹出浏览器让你登录。默认会话模式是 `profile`，优先复用完整浏览器目录处理 Cloudflare 之类的校验。

如果这些前提不满足，先检查环境，不要直接盲跑。

## 工作流

1. 从用户给的链接里提取 contest id。
2. 使用 `browser-session-manager` 读取或初始化 AtCoder 会话槽位。
3. 默认以 `profile` 模式保存完整浏览器目录。
4. 如果检测到未登录，则自动打开可见浏览器进入比赛主页，而不是直接打开 `tasks_print`。
5. 用户在真实浏览器窗口中完成登录和 Cloudflare 校验后关闭窗口。
6. 关闭窗口时自动保存 profile，然后回到导出流程继续抓取 `tasks_print?lang=en`。
7. 抓取阶段默认直接请求 `tasks_print?lang=en`；如果首轮遇到偶发 TLS / SSL 异常，会先做有限次重试。
8. 如果 Python `requests` 在当前 Windows 环境中仍然失败，则自动回退到 PowerShell `Invoke-WebRequest`。
9. 如果前两种 HTTP 抓取都失败，再回退到 Playwright。
10. 生成英文题面到 `en/`。
11. 翻译为逐段穿插对照 Markdown 到 `zh-CN/`。
12. 导出每题一个 PDF，例如 `A.pdf`、`B.pdf`。
13. 自动合并整场 Markdown，并导出整场 PDF；整合版统一使用中文文件名，例如：
  - `abc456题面中英文对照.md`
  - `abc456题面中英文对照.pdf`
14. 完成后检查：
  - `en/` 下是否生成全部英文题面
  - `zh-CN/` 下是否生成全部中英对照 Markdown
  - 是否生成每题 PDF
  - 是否生成整场合并 Markdown 与整场 PDF
  - Markdown 是否仍为逐段穿插对照，而不是 fallback

## Contest ID 提取

- 如果用户给的是类似 `https://atcoder.jp/contests/arc217/tasks` 的链接，contest id 是 `arc217`。
- 如果用户直接给 `abc123`、`arc217` 这类 contest id，可以直接使用。
- 只要路径中含有 `/contests/<id>/`，就按 `<id>` 处理。

## 运行命令

先解析 skill 根目录：

```powershell
$skillRoot = Join-Path ($env:CODEX_HOME ? $env:CODEX_HOME : (Join-Path $HOME '.codex')) 'skills\atcoder-statement-bilingual-pdf'
```

默认命令只需要写比赛 id：

```powershell
python "$skillRoot\scripts\run_atcoder_pipeline.py" <contest-id>
```

例如：

```powershell
python "$skillRoot\scripts\run_atcoder_pipeline.py" abc456
```

这条默认命令已经内置：

- `--workspace .\atcoder-output`
- `--provider openai`
- `--env-file .\.env`
- `--auth-mode session`
- `--session-site atcoder`
- `--session-env prod`
- `--session-account default`
- `--session-browser chrome`
- `--session-mode profile`
- `--overwrite`
- `--output-format bilingual`
- `--export-pdf`

默认情况下，`run_atcoder_pipeline.py` 和底层 `translate_markdown.py` 会优先读取 `.env` 里的 `OPENAI_MODEL` 作为模型名、读取 `OPENAI_REASONING_EFFORT` 作为思考强度；只有你显式传了 `--model` 或 `--reasoning-effort` 时才会覆盖这些值。不传思考强度时，会继续使用服务端默认值。

如果要显式指定会话槽位，可以补：

```powershell
python "$skillRoot\scripts\run_atcoder_pipeline.py" <contest-id> `
  --session-browser chrome `
  --session-account default
```

如果你想显式切回 `hybrid`，可以：

```powershell
python "$skillRoot\scripts\run_atcoder_pipeline.py" <contest-id> `
  --session-mode hybrid
```

如果只想兼容旧的浏览器 cookie 读取模式，可以手动切回：

```powershell
python "$skillRoot\scripts\run_atcoder_pipeline.py" <contest-id> `
  --auth-mode browser-cookies `
  --browser-cookies chrome
```

## 产物位置

- 英文题面：
  - `atcoder-output/<contest>/en/*.en.md`
- 中英对照题面：
  - `atcoder-output/<contest>/zh-CN/*.zh-CN.md`
- 单题 PDF：
  - `atcoder-output/<contest>/zh-CN/A.pdf`
  - `atcoder-output/<contest>/zh-CN/B.pdf`
  - 依此类推
- 合并产物：
  - `atcoder-output/<contest>/zh-CN/<contest>题面中英文对照.md`
  - `atcoder-output/<contest>/zh-CN/<contest>题面中英文对照.pdf`

## 检查点

- 不要接受“整篇中文 + 整篇英文”的 fallback 结果，目标必须是逐段穿插对照。
- 不要接受 HTML 实体残留，例如：
  - `&gt;`
  - `&lt;`
  - `&amp;`
- 不要接受题面里官方自带分隔线和我们自己的分隔线叠加，避免横线过多。
- `Input / Output` 中的格式行应保持为可渲染数学形式，不应出现：
  - `$$P_{1,1}$ $P_{1,2}$$`
- `C` 题这类表格中的 `<code><br></code>` 属于保留结构的合法写法，不要误删。

## 故障处理

- 如果脚本提示会话缺失或失效并弹出浏览器：
  - 直接在弹出的真实 Chrome / Edge 窗口中完成 AtCoder 登录。
  - 如果出现 Cloudflare challenge，就在同一个窗口里先完成 challenge。
  - 登录完成后关闭浏览器窗口，让脚本自动保存 profile。
  - 关闭后脚本会自动继续，不需要手动再跑一次。
- 如果浏览器窗口关闭后仍提示未登录：
  - 先确认你关闭的是 `browser-session-manager` 打开的真实浏览器窗口。
  - 再确认登录是否真的完成，而不是停留在 AtCoder 登录页。
- 如果缺少 `browser-session-manager`：
  - 先确认全局 skill 已安装到 `~\.codex\skills\browser-session-manager`。
- 如果必须回退旧 cookie 模式：
  - 改用 `--auth-mode browser-cookies`。
  - 再确认 `browser-cookie3` 已安装。
- 如果抓取阶段出现 `SSLError`、`UNEXPECTED_EOF_WHILE_READING` 或 `ERR_CONNECTION_CLOSED`：
  - 当前脚本会先在同一抓取通道内做有限次重试。
  - 当前脚本会先自动尝试 PowerShell `Invoke-WebRequest` 抓取 `tasks_print?lang=en`。
  - 如果 PowerShell 也失败，再检查本机网络、代理或安全软件是否拦截了 `atcoder.jp`。
  - 需要手工复核时，可先运行：
    - `Invoke-WebRequest -Uri "https://atcoder.jp/contests/<contest>/tasks_print?lang=en" -Headers @{ 'User-Agent'='Mozilla/5.0'; 'Accept-Language'='en-US,en;q=0.9' }`
- 如果 `tasks_print?lang=en` 返回 `404` 或内容不完整：
  - 先确认比赛是否已经结束或页面是否已经开放。
- 如果接口报 `Unknown message role: developer`，检查 `scripts/translate_markdown.py` 是否仍使用 `system` 而不是 `developer`。
- 如果块级翻译因转义失败，使用当前脚本中的“块标记文本”方案，不要退回 JSON 返回格式。
- 如果结果中出现 Markdown 结构错误，先重跑采集和翻译，再做全量搜索：
  - `&gt;|&lt;|&amp;`
  - 不平衡代码围栏
  - fallback 模式

## 适用话术

以下请求应触发这个 skill：

- “把这个 AtCoder 比赛的所有题面抓下来并翻译成中文”
- “给一个 AtCoder contest 链接，生成中英对照 PDF”
- “重新跑一遍某场 AtCoder 比赛的题面抓取和翻译流程”
- “检查 AtCoder 双语题面导出的 Markdown / PDF 格式问题”
