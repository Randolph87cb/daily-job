---
name: atcoder-editorial-workflow
description: 处理 AtCoder 题解 Markdown 的撰写、批量格式调整和导出。适用于当前项目 `atcoder-output/比赛目录/editorials/` 下需要新增题解、统一章节标题或格式、同步 `代码规范.md` 与 `atcoder-output/题解撰写要求.md`、并重新生成单题 PDF 与合并版 Markdown/PDF 时使用。
---

# AtCoder 题解工作流

## 概览

- 先同步规则，再改单题 Markdown，再重导出，再验证，再更新工作记录。
- 题解正文规则以：
  - `D:\workspace\daily-job\atcoder-output\题解撰写要求.md`
  - `D:\workspace\daily-job\代码规范.md`
  为准。
- 批量导出优先使用 `scripts/export-editorials.ps1`，不要每次临时拼一套 `md2pdf` 命令。

## 何时使用

- 用户要求撰写或补全 AtCoder 题解。
- 用户要求批量修改题解模板、章节标题、公式写法或参考实现标题。
- 用户要求把 `editorials/` 下的题解重新导出为单题 PDF、合并版 Markdown 或合并版 PDF。
- 用户要求把题解流程沉淀为可重复执行的规范、脚本或工作流。

## 工作流

1. 先确认目标比赛目录，例如 `atcoder-output/<contest>/editorials/`。
2. 如果用户的新要求会改变模板或代码风格，先更新：
   - `atcoder-output/题解撰写要求.md`
   - `代码规范.md`
3. 再修改单题题解 Markdown，不要先导出后回头补正文。
4. 单题题解改完后，运行 `scripts/export-editorials.ps1` 重生成：
   - 单题 PDF
   - 合并版 Markdown
   - 合并版 PDF
5. 导出后检查标题、合并版同步情况和 PDF 产物。
6. 最后更新：
   - `AI工作记录/records/YYYY/MM/*.md`
   - 如有流程沉淀变化，再更新 `AI工作记录/skill-backlog.md`

## 导出

在仓库根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File ".\.codex\skills\atcoder-editorial-workflow\scripts\export-editorials.ps1" `
  -EditorialDir ".\atcoder-output\abc457-browser-pipeline\abc457\editorials"
```

- 脚本会自动识别 `*.editorial.md`。
- 单题 PDF 输出为 `A.pdf`、`B.pdf` 这类命名。
- 合并版输出为 `<contest>.editorials.md` 和 `<CONTEST>-editorials.pdf`。

## 资源

### references/

- `references/workflow.md`
  - 需要看完整检查清单、命名规则、导出坑点和提交流程时再读。

### scripts/

- `scripts/export-editorials.ps1`
  - 批量重建 `editorials/` 目录下的单题 PDF、合并版 Markdown 和合并版 PDF。
