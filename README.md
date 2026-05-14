# 日常事务

这个仓库用于集中维护几类日常工作资料与自动化工具：签到表、课时统计、项目内 Codex skills，以及 AtCoder 题面抓取翻译相关脚本与样例输出。

## 目录结构

```text
日常事务/
├─ .codex/
│  └─ skills/
│     ├─ atcoder-statement-bilingual-pdf/      # AtCoder 题面抓取、翻译、导出 skill
│     ├─ atcoder-editorial-workflow/           # AtCoder 题解撰写、批量调整与导出 skill
│     ├─ attendance-sheet-monthly-update/      # 月度签到表维护 skill
│     └─ class-hours-statistics/               # 课时统计生成 skill
├─ AI工作记录/
│  ├─ records/YYYY/MM/*.md                     # 项目内 AI 工作摘要
│  └─ skill-backlog.md                         # 可沉淀流程与 skill 候选
├─ scripts/                                    # 项目级统一入口与对外打包基础脚本
├─ atcoder-arc218/                             # AtCoder 脚本实验目录与参考文档
├─ atcoder-output/                             # 比赛题面抓取、翻译、PDF 与题解输出
├─ 签到表/                                      # 月度签到表 Excel
├─ 课时统计/                                    # 课时统计表与历史月份数据
├─ AGENTS.md                                   # 项目协作规则
└─ .gitignore                                  # 忽略策略
```

## 目录说明

- `.codex/skills/` 保存项目内使用的本地 skill，实现和项目流程一起维护；当前已包含题面抓取翻译、题解撰写导出、签到表维护和课时统计等流程。其中题解 workflow 负责项目目录与导出流程，正文与代码规范复用全局 `algorithm-editorial-reference`。
- `AI工作记录/` 保存当前项目的任务摘要、关键决策、验证结果和 skill 沉淀线索。
- `scripts/` 保存项目级包装脚本；当前提供 `run_atcoder_delivery.py` 作为 AtCoder 题面抓取与题解导出的统一入口，也是后续打包成独立程序时优先复用的编排层。
- `atcoder-arc218/` 保留 AtCoder 相关脚本、样例和说明文档，适合继续开发或验证流程。
- `atcoder-output/` 保存比赛输出结果，通常按 `比赛 ID / 语言或流水线目录` 组织；单场目录下可包含英文题面、双语题面、PDF，以及 `editorials/` 中的题解 Markdown、单题 PDF、合并 Markdown 和合并 PDF。
- `签到表/` 与 `课时统计/` 保存实际业务 Excel 素材。

## AtCoder 统一入口

项目根目录现在提供一个项目级统一入口：

```powershell
python .\scripts\run_atcoder_delivery.py abc450 --phase precheck
python .\scripts\run_atcoder_delivery.py abc450 --phase statement
python .\scripts\run_atcoder_delivery.py abc450 --phase all
```

- 默认配置文件是 `scripts/atcoder_delivery.example.json`。
- `statement` 阶段会调用现有题面抓取翻译 pipeline。
- `editorials` 阶段会在 `atcoder-output/<contest>/editorials/` 下存在 `*.editorial.md` 时才执行导出。
- 这个入口当前仍然复用仓库内现有脚本与依赖；如果后续要发给没有 Codex 的用户，优先围绕这个入口继续打包，而不是直接暴露 skill。
- 统一入口支持命令行覆盖：
  - `--with-pdf` / `--no-pdf`
  - `--overwrite` / `--no-overwrite`

如果要生成一份本地“点击即用”的便携发布目录，可执行：

```powershell
python .\scripts\build_click_release.py --clean
```

- 默认输出到 `.tmp/release/atcoder-delivery-click/`。
- 生成物自带：
  - Python 运行时；
  - `node.exe`；
  - 本地 `md2pdf` CLI；
  - 题面抓取与题解导出所需脚本；
  - `run.bat` / `run.ps1` 启动器。
- 发布包默认改用 `browser-cookies` 鉴权，不再依赖 Codex 的 `browser-session-manager`。
- 发布包当前默认偏向“快路径”：
  - 题面 PDF 默认关闭；
  - 已有输出默认复用；
  - 需要完整 PDF 时可显式传 `--with-pdf`；
  - 需要从头重跑时可显式传 `--overwrite`。
- 这个发布包已经内置 `Python`、`node.exe`、本地 `md2pdf` CLI 和流程脚本，因此不依赖对方额外安装这些组件；
  但它仍然依赖：
  - Windows + PowerShell
  - 有效的 `.env` / `OPENAI_API_KEY`
  - 可访问 `atcoder.jp` 与模型 API 的网络
  - 本机可读取的浏览器 cookies，以及已登录的 AtCoder 账户

## 文档维护约定

- 目录结构或主要职责发生变化时，需要同步更新 `README.md` 与 `AGENTS.md`。
- 如果变更影响某个子项目的使用方式，还要同步更新对应子目录文档，例如 `atcoder-arc218/README.md` 或相关 skill 文档。
- 新增长期保留目录时，路径、用途和产物位置要在文档中写清楚。

## Git 与清理约定

- 仓库提交前清理临时目录、缓存和调试日志。
- 本机环境文件与可再生成内容通过 `.gitignore` 排除，例如 `.env`、`node_modules/`、`.tmp/`、`.playwright-mcp/`、`__pycache__/`。
- 使用中文提交信息，并在每次修改后检查 Git 状态。
