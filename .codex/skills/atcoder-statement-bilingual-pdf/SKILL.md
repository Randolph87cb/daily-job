---
name: atcoder-statement-bilingual-pdf
description: 处理 AtCoder 比赛题面的抓取、翻译和导出。适用于用户给出 AtCoder 比赛链接或 contest id，希望复用本机浏览器登录态批量提取整场比赛英文题面，翻译成中文，生成逐段穿插的中英对照 Markdown，并导出单题 PDF 与整场合并 PDF 时使用。
---

# AtCoder 双语题面导出

## 概览

- 这个 skill 自带运行所需脚本与词表，不依赖外部项目目录。
- 当前保留的主流程只有一条：
  - 复用本机浏览器登录态抓取 `tasks_print?lang=en`
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
- 本机已可调用：
  - `python`
  - `node`
  - `md2pdf`
- 本机已安装浏览器 Cookie 读取依赖：
  - `python -m pip install browser-cookie3`
- 你已经在本机浏览器中登录 AtCoder。

如果这些前提不满足，先检查环境，不要直接盲跑。

## 工作流

1. 从用户给的链接里提取 contest id。
2. 使用浏览器登录态抓取 `tasks_print?lang=en`。
3. 生成英文题面到 `en/`。
4. 翻译为逐段穿插对照 Markdown 到 `zh-CN/`。
5. 导出每题一个 PDF，例如 `A.pdf`、`B.pdf`。
6. 自动合并整场 Markdown，并导出整场 PDF，例如 `ABC456.pdf`。
7. 完成后检查：
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

默认直接走本机浏览器登录态，而且大多数情况下只需要写比赛 id：

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
- `--browser-cookies auto`
- `--overwrite`
- `--output-format bilingual`
- `--export-pdf`

如果自动探测浏览器不理想，可以显式指定浏览器：

```powershell
python "$skillRoot\scripts\run_atcoder_pipeline.py" <contest-id> --browser-cookies chrome
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
  - `atcoder-output/<contest>/zh-CN/<contest>.zh-CN.md`
  - `atcoder-output/<contest>/zh-CN/<CONTEST>.pdf`

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

- 如果读取浏览器登录态失败：
  - 先确认 `browser-cookie3` 已安装。
  - 再确认 AtCoder 已在本机浏览器中完成登录。
  - 默认先试 `auto`；如果失败，再显式指定 `chrome`。
  - 如果 `edge` 报需要管理员权限，不要继续硬试，优先改用 `chrome`。
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
