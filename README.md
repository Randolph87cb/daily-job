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
├─ atcoder-arc218/                             # AtCoder 脚本实验目录与参考文档
├─ atcoder-output/                             # 比赛题面抓取、翻译、PDF 与题解输出
├─ 签到表/                                      # 月度签到表 Excel
├─ 课时统计/                                    # 课时统计表与历史月份数据
├─ AGENTS.md                                   # 项目协作规则
└─ .gitignore                                  # 忽略策略
```

## 目录说明

- `.codex/skills/` 保存项目内使用的本地 skill，实现和项目流程一起维护；当前已包含题面抓取翻译、题解撰写导出、签到表维护和课时统计等流程。
- `AI工作记录/` 保存当前项目的任务摘要、关键决策、验证结果和 skill 沉淀线索。
- `atcoder-arc218/` 保留 AtCoder 相关脚本、样例和说明文档，适合继续开发或验证流程。
- `atcoder-output/` 保存比赛输出结果，通常按 `比赛 ID / 语言或流水线目录` 组织；单场目录下可包含英文题面、双语题面、PDF，以及 `editorials/` 中的题解 Markdown、单题 PDF、合并 Markdown 和合并 PDF。
- `签到表/` 与 `课时统计/` 保存实际业务 Excel 素材。

## 文档维护约定

- 目录结构或主要职责发生变化时，需要同步更新 `README.md` 与 `AGENTS.md`。
- 如果变更影响某个子项目的使用方式，还要同步更新对应子目录文档，例如 `atcoder-arc218/README.md` 或相关 skill 文档。
- 新增长期保留目录时，路径、用途和产物位置要在文档中写清楚。

## Git 与清理约定

- 仓库提交前清理临时目录、缓存和调试日志。
- 本机环境文件与可再生成内容通过 `.gitignore` 排除，例如 `.env`、`node_modules/`、`.tmp/`、`.playwright-mcp/`、`__pycache__/`。
- 使用中文提交信息，并在每次修改后检查 Git 状态。
