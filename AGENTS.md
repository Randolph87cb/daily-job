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
│     ├─ atcoder-editorial-workflow/
│     ├─ attendance-sheet-monthly-update/
│     └─ class-hours-statistics/
├─ AI工作记录/
│  ├─ records/YYYY/MM/*.md
│  └─ skill-backlog.md
├─ scripts/
│  └─ run_atcoder_delivery.py
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

## AtCoder 题解产物约定

- `atcoder-output/<contest>/editorials/` 目录当前除了单题题解 Markdown 外，还可以包含：
  - 单题 PDF，例如 `A.pdf`
  - 合并版 Markdown，例如 `<contest>题解.md`
  - 合并版 PDF，例如 `<contest>题解.pdf`
- `atcoder-output/<contest>/zh-CN/` 目录下的整合版双语题面也统一使用中文文件名：
  - 合并版 Markdown，例如 `<contest>题面中英文对照.md`
  - 合并版 PDF，例如 `<contest>题面中英文对照.pdf`
- 如果题解目录中的产物命名或导出方式发生变化，至少同步更新：
  - `README.md`
  - 当前文件 `AGENTS.md`
  - `.codex/skills/atcoder-editorial-workflow/SKILL.md`
  - `.codex/skills/atcoder-statement-bilingual-pdf/SKILL.md`
  - 如涉及统一题解规范，再同步全局 skill `algorithm-editorial-reference` 的对应说明

## AtCoder 统一入口约定

- 项目级 AtCoder 交付编排入口放在根目录 `scripts/`，当前统一入口为 `scripts/run_atcoder_delivery.py`。
- 这个入口负责串起题面抓取翻译、题解导出和预检查；它是未来对外打包、服务器定时执行或改造成独立程序时的优先复用边界。
- 当前统一入口还支持 `editorial-generate` 阶段，用于按单题请求模型生成题解、编译运行样例、失败后附样例检测结果重试。
- 如果修改了 `scripts/build_click_release.py` 生成的发布目录结构、启动器名称、默认鉴权方式或 bundled runtime 组织方式，也视为项目正式交付边界变更，需要同步更新相关文档和说明。
- 如果调整了统一入口或发布包的默认性能策略，例如：
  - 是否默认导出 PDF
  - 是否默认覆盖已有产物
  - 是否默认启用题解导出
  也要同步更新 `README.md`、当前文件和相关发布说明。
- 如果修改了统一入口的参数、配置文件结构、阶段命名或默认产物目录，至少同步更新：
  - `README.md`
  - 当前文件 `AGENTS.md`
  - 相关示例配置或发布说明
- 如果修改了自动题解阶段的重试策略、样例校验方式、校验报告落点或默认编译参数，也视为统一入口行为变化，同样要同步更新相关文档和 skill 说明。

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
