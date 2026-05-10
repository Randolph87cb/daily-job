# 日常事务 项目协作规则

## 项目定位

- 这个目录是一个“日常事务工作集”，同时承载：
  - 课时与签到相关 Excel 素材
  - 项目内 Codex skills
  - AtCoder 题面抓取、翻译与导出脚本
  - 运行产物、工作记录与后续沉淀

## 项目目录结构

```text
日常事务/
├─ .codex/
│  └─ skills/
│     ├─ atcoder-statement-bilingual-pdf/
│     ├─ attendance-sheet-monthly-update/
│     └─ class-hours-statistics/
├─ AI工作记录/
│  ├─ records/YYYY/MM/*.md
│  └─ skill-backlog.md
├─ atcoder-arc218/
│  ├─ scripts/
│  ├─ samples/
│  ├─ translation_assets/
│  ├─ output/
│  └─ pipeline-output/
├─ atcoder-output/
│  └─ <contest-id>/
│     ├─ en/
│     ├─ zh-CN/
│     └─ editorials/
├─ 签到表/
└─ 课时统计/
```

## 文档同步规则

- 只要根目录结构、主要子目录职责、产物落点或项目协作方式发生变化，必须同步更新：
  - 根目录 `README.md`
  - 当前文件 `AGENTS.md`
  - 受影响子项目自己的文档，例如 `atcoder-arc218/README.md` 或相关 skill 文档
- 如果只是临时调试，不修改正式结构；如果新增了会长期保留的目录，必须补进目录结构说明。
- 更新目录结构时，文档里的路径、示例命令、输出位置说明要一起校对，不允许只改代码不改文档。

## 临时文件与忽略规则

- 提交前清理一次性临时产物，重点包括：
  - 根目录或子目录下的 `.tmp/`
  - `.playwright-mcp/`
  - `__pycache__/`
  - 调试日志、临时导出缓存和本地凭据文件
- 对明显属于本机环境或可再生成的内容，优先加入 `.gitignore`，避免反复清理。
- `.env`、浏览器/工具缓存、`node_modules/` 默认不入库。

## Git 规则

- Git 命令必须串行执行。
- 任何会改变仓库状态的 Git 操作前，先看 `git status`。
- 完成修改后要检查状态，使用中文提交信息提交，并推送到远端。

## 编码与验证

- Windows / PowerShell 下统一使用 PowerShell 兼容命令。
- 读写中文内容、Markdown、配置文件优先使用 UTF-8。
- 能运行验证就运行；无法完整验证时，要在工作记录和最终说明里写明原因与替代检查。
