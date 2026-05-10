# AtCoder ARC218 Statement Tools

这个目录现在包含“抓取英文题面”和“翻译成中文”的基础框架，先保证流程可跑，再逐步优化翻译质量。

当前包含：

- `scripts/fetch_atcoder_tasks.py`
  - 从 `tasks_print?lang=en` 抓取整场比赛的英文题面。
  - 按题目拆分为单独的 Markdown 文件。
  - 采集后使用 `scripts/atcoder_better_turndown.cjs` 按 `Atcoder Better` 风格把 HTML 转成 Markdown。
- `scripts/translate_markdown.py`
  - 把英文 Markdown 翻译成中文 Markdown。
  - 当前支持两种 provider：
    - `rule-based`：本地规则翻译器，用于跑通流程和验证结构。
    - `openai`：调用模型翻译，适合后续优化质量。
- `scripts/run_atcoder_pipeline.py`
  - 串起“抓取英文题面 -> 翻译中文题面”两步流程。
- `translation_guidelines.md`
  - 面向算法题的翻译约定与术语建议。
- `translation_assets/algorithm_glossary.json`
  - 术语表与固定译法配置。
- `.env.example`
  - 环境变量示例文件。
- `samples/arc218_a.zh-CN.md`
  - `A - Many Sets` 的中文试译样例。

## 依赖

- Python 3
- Node.js
- 当前目录下的 npm 依赖：

```powershell
npm install
```

## 第一步：抓取英文题面

```powershell
python .\scripts\fetch_atcoder_tasks.py --contest arc218 --output-dir .\output\arc218\en
```

运行后会生成：

```text
output/
  arc218/
    en/
      arc218_a.en.md
      arc218_b.en.md
      ...
```

## 第二步：翻译成中文

先用本地规则翻译器跑通框架：

```powershell
python .\scripts\translate_markdown.py --input-dir .\output\arc218\en --output-dir .\output\arc218\zh-CN --provider rule-based
```

如果后续要接模型翻译：

```powershell
Copy-Item .\.env.example .\.env
# 然后编辑 .env，填入真实的 OPENAI_API_KEY，并按需设置 OPENAI_API_MODE / OPENAI_BASE_URL
python .\scripts\translate_markdown.py --input-dir .\output\arc218\en --output-dir .\output\arc218\zh-CN --provider openai --model gpt-4
```

默认输出格式是 `bilingual`，即同一个文件里同时保留中文译文和英文原文，方便对照阅读。
如果只想保留中文译文，可以显式指定：

```powershell
python .\scripts\translate_markdown.py --input-dir .\output\arc218\en --output-dir .\output\arc218\zh-CN --provider openai --output-format translation-only
```

如果要在翻译结束后直接导出 PDF：

```powershell
python .\scripts\translate_markdown.py --input-dir .\output\arc218\en --output-dir .\output\arc218\zh-CN --provider openai --env-file .\.env --output-format bilingual --export-pdf
```

脚本会默认读取当前项目目录下的 `.env`。
如果你的 `.env` 在别的位置，也可以手动指定：

```powershell
python .\scripts\translate_markdown.py --input-dir .\output\arc218\en --output-dir .\output\arc218\zh-CN --provider openai --env-file 'D:\path\to\.env'
```

如果你希望明确指定为 Chat 模式，可以在 `.env` 中写：

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_MODE=chat
OPENAI_BASE_URL=https://api.openai.com/v1/chat/completions
```

也可以不用 `.env`，直接命令行指定：

```powershell
python .\scripts\translate_markdown.py --input-dir .\output\arc218\en --output-dir .\output\arc218\zh-CN --provider openai --api-mode chat --base-url https://api.openai.com/v1/chat/completions
```

## 一键跑两步

```powershell
python .\scripts\run_atcoder_pipeline.py --contest arc218 --provider rule-based
```

使用模型翻译时同样会自动读取 `.env`：

```powershell
python .\scripts\run_atcoder_pipeline.py --contest arc218 --provider openai --model gpt-4
```

如果要走 Chat 模式：

```powershell
python .\scripts\run_atcoder_pipeline.py --contest arc218 --provider openai --api-mode chat --base-url https://api.openai.com/v1/chat/completions
```

## 提交验证脚本

`scripts/submit_atcoder_solution.py` 用来把本地参考代码真正提交到 AtCoder，并轮询直到拿到终态 verdict。它的目标不是替代在线评测页面，而是为“题解里的参考代码是否真的能过”提供一个可复用的本地验证入口。

### 依赖

- Python 3
- `requests`
- `lxml`
- `browser-cookie3`

安装示例：

```powershell
python -m pip install requests lxml browser-cookie3
```

### 认证方式

- 优先支持本机浏览器登录态：
  - 默认 `--auth-mode auto --browser-cookies auto`
  - 会按 `chrome -> edge -> brave -> chromium -> firefox -> opera -> vivaldi` 顺序尝试读取 `atcoder.jp` Cookie
- 支持显式用户名/密码登录作为备选：
  - 传 `--auth-mode password --username <用户名> --password <密码>`
  - 如果只传 `--username` 不传 `--password`，脚本会在运行时交互式读取密码

### 常用命令

先打印当前提交页可选语言：

```powershell
python .\scripts\submit_atcoder_solution.py --contest-id arc218 --task arc218_a --source-file .\samples\answer.py --language Python --print-languages
```

只做认证、任务和语言解析，不真正提交：

```powershell
python .\scripts\submit_atcoder_solution.py --contest-id arc218 --task arc218_a --source-file .\samples\answer.py --language "Python (CPython 3.11.4)" --dry-run
```

使用浏览器 Cookie 直接提交并轮询：

```powershell
python .\scripts\submit_atcoder_solution.py --contest-id arc218 --task arc218_a --source-file .\samples\answer.py --language 5078
```

强制使用用户名/密码登录后提交：

```powershell
python .\scripts\submit_atcoder_solution.py --contest-id arc218 --task arc218_a --source-file .\samples\answer.py --language "Python (CPython 3.11.4)" --auth-mode password --username your_name
```

### 输出

真实提交时，脚本会在检测到新提交并进入终态后输出：

- `submission_id`
- `verdict`
- `url`

### 已知限制

- 当前实现依赖 AtCoder 当前网页结构：
  - 会动态解析提交页中的表单、CSRF、任务下拉框、语言下拉框和源码输入框
  - 但如果 AtCoder 后续明显改版，脚本仍可能需要同步调整
- 当前仓库环境下还不能做真实提交验证，原因是：
  - 这台机器现在没有可直接复用的 AtCoder 浏览器登录 Cookie
  - 本线程也没有提供可用于备选登录的 AtCoder 用户名/密码
  - 因此只能完成脚本实现和本地静态检查，不能在 2026-05-10 这次会话里完成真实提交闭环
- 轮询逻辑依赖“我的提交”列表中最新一条记录来识别本次提交；如果同一账号在极短时间内有并发提交，识别风险会上升

## 当前框架说明

- 这版采集默认抓取英文题面，便于后续统一翻译成中文。
- 采集逻辑直接读取 AtCoder 的 `tasks_print` 页面，不需要逐题翻页。
- Markdown 转换采用 `Atcoder Better` 风格的 `turndown` 规则，并针对 AtCoder 题面补了少量本地增强，重点保留：
  - 标题
  - Score
  - Problem Statement
  - Constraints
  - Input / Output
  - Sample Input / Output
  - 样例解释段落
- 数学变量会尽量保留为 `$...$` 形式，样例输入输出会保留为代码块。
- 带边框表格会优先按 Markdown 表格输出；像 `C` 题这种单元格内多行内容，会保留为 `<br>` / `<code>...</code>` 形式，避免结构被压扁。
- 翻译脚本会优先保留：
  - 代码块
  - 数学公式
  - 变量名
  - Markdown 结构
- 对于会干扰公式渲染的写法，脚本会在输出前自动做安全规范化：
  - `` `$N$` `` -> `$N$`
  - 三反引号代码块中如果内容本身只是纯公式，也会自动去掉代码块外层，恢复成正常公式
- `rule-based` provider 的目标不是最终翻译质量，而是先把整条流水线搭起来。
- `openai` provider 的目标是后续在不破坏结构的前提下提升算法题中文可读性。
- `translate_markdown.py` 和 `run_atcoder_pipeline.py` 会在启动时优先读取项目根目录下的 `.env`，并且不会覆盖当前 shell 里已经存在的同名环境变量。
- `OPENAI_API_MODE` 支持 `responses` 和 `chat` 两种模式。
- `output format` 支持：
  - `bilingual`：同一文件中按“英文在上、中文在下”的对照形式输出
  - `translation-only`：只输出中文译文
- 题目标题和章节标题默认保留英文原文，不再翻译。
- `Source` 默认删除，`Score` 只保留中文一行。
- 样例输入输出这类不需要翻译的代码块只保留一份，不重复生成中文版本。
- `md2pdf` 导出通过本地 `md2pdf` 命令完成。
- `md2pdf` 导出使用默认参数，不再显式传 `--no-watermark`。
- 如果没有显式传 `--base-url`，脚本会按下面顺序决定接口地址：
  - `.env` 或当前环境里的 `OPENAI_BASE_URL`
  - 若未配置，则根据 `api mode` 自动选择默认值
  - `responses` -> `https://api.openai.com/v1/responses`
  - `chat` -> `https://api.openai.com/v1/chat/completions`

## 下一步建议

如果这版框架符合预期，下一步可以继续补：

1. 扩充术语表和固定句式。
2. 给模型翻译加 chunk 策略与缓存。
3. 增加“英文原文 + 中文译文”双栏输出。
4. 对交互题、表格、复杂说明块增加专项优化。
