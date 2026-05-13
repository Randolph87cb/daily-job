# 题解工作流细则

## 1. 作用范围

本 skill 面向当前项目中算法题题解的这一类任务：

- 新增单题题解 Markdown
- 批量修改题解章节标题、固定结构、公式写法
- 统一参考实现风格
- 从 `editorials/` 目录重导单题 PDF、合并版 Markdown、合并版 PDF

默认目录形态：

```text
atcoder-output/<contest>/editorials/
├─ <contest>_a.editorial.md
├─ <contest>_b.editorial.md
├─ ...
├─ A.pdf
├─ B.pdf
├─ ...
├─ <contest>.editorials.md
└─ <CONTEST>-editorials.pdf
```

## 2. 先改规则，再改题解

如果用户要求修改的是“题解统一写法”，先改这两个文件，再批量动单题：

- 全局 skill `algorithm-editorial-reference/references/题解撰写要求.md`
- 全局 skill `algorithm-editorial-reference/references/代码规范.md`
- 如果变更同时影响项目导出流程，再补改本地 `references/workflow.md`

典型触发场景：

- 删除某个固定章节
- 修改固定章节标题
- 调整数学公式写法
- 调整数组 / `vector` / 全局数组偏好

## 3. 当前稳定下来的题解要求

- 题解与参考实现的正文规范统一遵守全局 skill `algorithm-editorial-reference`
- 默认不保留单独的“题目信息”章节
- 固定结构为：
  1. 标题
  2. `## 题意概括`
  3. `## 解题思路`
  4. `## 正确性说明`
  5. `## 复杂度`
  6. `## 参考实现`
- 公式统一使用 `$...$`
- 参考实现默认使用 `C++`
- 能用普通数组就不用 `vector`
- 数组能放 `main` 外时，优先放到 `main` 外
- 如果必须保留容器，正文里要解释为什么
- 默认只基于当前仓库内的题面 Markdown、本地样例题解和全局规范撰写题解；除非用户明确要求，否则不要用网络搜索补解法或代码。

## 4. 导出规则

使用 `scripts/export-editorials.ps1`，不要临时重拼一套导出命令。

推荐调用方式：

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File ".\.codex\skills\atcoder-editorial-workflow\scripts\export-editorials.ps1" `
  -EditorialDir ".\atcoder-output\abc457-browser-pipeline\abc457\editorials"
```

脚本行为：

- 自动识别 `*.editorial.md`
- 生成单题 PDF：
  - `A.pdf`
  - `B.pdf`
  - ...
- 生成合并版 Markdown：
  - `<contest>.editorials.md`
- 生成合并版 PDF：
  - `<CONTEST>-editorials.pdf`

## 5. 合并版规则

- 合并版 Markdown 顶部写：
  - `# <CONTEST> 题解合集`
- 各题之间插入：

```html
<div style="page-break-after: always;"></div>
```

- 分页标记只应出现在合并版，不要写回单题 Markdown。

## 6. 导出时的坑点

- 调用 `md2pdf` 时，优先进入 `editorials/` 目录后，用相对文件名导出。
- 不要混用“绝对输入路径 + 不合适的 output-dir”，否则可能在 `editorials/` 下面误生成一层嵌套目录。
- 如果脚本里包含中文标题或中文常量，优先用 `pwsh` / PowerShell 7 执行；直接用 `powershell.exe` 可能把合并版标题导成乱码。
- 如果导出过程产生 `.tmp\md2pdf` 之类的一次性缓存，提交前清掉。

## 7. 检查清单

改完并导出后，至少检查：

1. 单题题解里是否残留旧章节标题
2. 合并版 Markdown 是否与单题正文同步
3. `editorials/` 下是否同时存在：
   - 单题 Markdown
   - 单题 PDF
   - 合并版 Markdown
   - 合并版 PDF
4. 如果统一改过标题，例如 `## 参考实现`，单题和合并版里都要命中
5. Git 状态里不要夹带 `.tmp/`、误生成目录或导出缓存

## 8. 记录与提交

完成后同步：

- `AI工作记录/records/YYYY/MM/*.md`
- 必要时更新 `AI工作记录/skill-backlog.md`

如果仓库在 Git 下维护：

1. 先看 `git status`
2. 串行执行 `git add`
3. 使用中文提交信息 `git commit`
4. 再 `git push`
