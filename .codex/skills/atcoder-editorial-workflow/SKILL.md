---
name: atcoder-editorial-workflow
description: 处理 AtCoder 题解 Markdown 的撰写、批量格式调整和导出。适用于需要维护 `editorials/` 目录下的题解文件、统一章节标题或格式、同步 skill 目录中的规则文档、并重新生成单题 PDF 与合并版 Markdown/PDF 时使用。
---

# AtCoder 题解工作流

## 概览

- 先同步规则，再改单题 Markdown，再重导出，再验证，再更新工作记录。
- 题解正文与参考实现规范统一复用全局 skill `algorithm-editorial-reference`，不要在本 skill 目录下重复维护一份本地规范。
- 批量导出优先使用 `scripts/export-editorials.ps1`，不要每次临时拼一套 `md2pdf` 命令。
- 默认基于当前仓库里的题面 Markdown、本地样例题解与全局规范完成题解；除非用户明确要求，否则不要使用网络搜索补题解。
- 在委派模式下，主线程负责拆分任务、统一导出、最终验证、工作记录与 Git；subagent 只负责自己名下的题解 Markdown，不要自行执行 `git add`、`git commit`、`git push`。

## 何时使用

- 用户要求撰写或补全 AtCoder 题解。
- 用户要求批量修改题解模板、章节标题、公式写法或参考实现标题。
- 用户要求把 `editorials/` 下的题解重新导出为单题 PDF、合并版 Markdown 或合并版 PDF。
- 用户要求把题解流程沉淀为可重复执行的规范、脚本或工作流。

## 工作流

1. 先确认目标题解目录，例如 `atcoder-output/<contest>/editorials/`。
2. 如果用户的新要求会改变模板或代码风格，先更新：
   - 全局 skill `algorithm-editorial-reference` 的对应规范文档或说明
   - 本 skill 下与项目流程有关的说明文档，例如 `references/workflow.md`
3. 再修改单题题解 Markdown，不要先导出后回头补正文。
4. 单题题解改完后，运行 `scripts/export-editorials.ps1` 重生成：
   - 单题 PDF
   - 合并版 Markdown
   - 合并版 PDF
5. 导出前至少抽查 `1` 篇复杂题题解，确认参考实现不是“零注释核心代码”，并且代码注释能和正文思路段落对应。
6. 导出后检查标题、合并版同步情况和 PDF 产物。
7. 最后更新：
   - `AI工作记录/records/YYYY/MM/*.md`
   - 如有流程沉淀变化，再更新 `AI工作记录/skill-backlog.md`
8. 如果使用委派模式：
   - 先按题目或文件划分不重叠 ownership，再下发 subagent。
   - subagent 只改自己负责的 `*.editorial.md`，不要顺手改导出脚本、其他题解或 Git 状态。
   - 汇总、导出、抽查、提交与推送统一由主线程执行。

## 导出

在仓库根目录执行：

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File ".\.codex\skills\atcoder-editorial-workflow\scripts\export-editorials.ps1" `
  -EditorialDir ".\atcoder-output\abc457-browser-pipeline\abc457\editorials"
```

- 脚本会自动识别 `*.editorial.md`。
- 单题 PDF 输出为 `A.pdf`、`B.pdf` 这类命名。
- 合并版输出为 `<contest>.editorials.md` 和 `<CONTEST>-editorials.pdf`。
- 当前导出目录包含中文标题时，优先使用 `pwsh` 或当前 PowerShell 7 会话执行，避免 `powershell.exe` 读取 UTF-8 脚本时把中文常量导成乱码。

## 资源

### references/

- `references/workflow.md`
  - 需要看完整检查清单、命名规则、导出坑点和提交流程时再读。

### global skills

- `algorithm-editorial-reference`
  - 需要看题解固定结构、公式写法、教学型 `C++` 代码规范时，读取这个全局 skill 及其 `references/题解撰写要求.md`、`references/代码规范.md`。

### scripts/

- `scripts/export-editorials.ps1`
  - 批量重建 `editorials/` 目录下的单题 PDF、合并版 Markdown 和合并版 PDF。
