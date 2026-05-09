---
name: attendance-sheet-monthly-update
description: 批量维护 Excel 签到表的月份和学生名单。适用于当前目录或指定目录内使用固定模板的 `.xlsx` 签到表，需要把“某月签到表”切换到新月份、按班级新增或删除学生、并尽量保留原始格式、边框、合并单元格时使用。
---

# 签到表月度维护

## 概览

- 优先使用 `scripts/update-attendance-sheets.ps1` 批量处理签到表。
- 保持 Excel 原样式，不改模板结构，只修改标题中的月份和名单区域的学生姓名。
- 完成后核对标题文本和目标班级名单，避免漏改或误删。

## 适用前提

- 在 Windows 环境执行，并且本机安装了 Microsoft Excel。
- 工作簿第一页使用固定模板：
  - 标题单元格中包含 `YYYY年M月签到表`
  - 学生名单从第 6 行开始
  - 学生姓名在第 3 列
  - 名单区域结束前存在 `课导老师签字`

如果模板不满足这些前提，先读取脚本逻辑再局部调整，不要直接盲跑。

## 工作流

1. 进入包含签到表的目录，确认待处理文件是 `.xlsx`。
2. 准备一个 JSON 变更文件，按文件名声明 `add` 和 `remove`。
3. 运行 `scripts/update-attendance-sheets.ps1` 批量切换月份并应用名单变更。
4. 再次读取标题和名单区，确认目标月份、目标学生和空白名额都符合预期。
5. 如果当前项目维护了 `AI工作记录`，同步补充本次修改摘要。

## 名单变更文件格式

使用 UTF-8 JSON。键名写 Excel 文件名，值里只放需要改动的学生。

```json
{
  "26春季CSP班B1签到表.xlsx": {
    "add": ["郭宸宇"]
  },
  "26春季进阶班B2签到表.xlsx": {
    "remove": ["朱致远"]
  }
}
```

规则：

- `remove` 先执行，再执行 `add`。
- `remove` 会删除名单中匹配到的所有同名项。
- `add` 只在名单里不存在同名学生时追加到末尾。
- 如果更新后的名单长度超过模板可用行数，脚本会直接报错，不会悄悄截断。

## 运行方式

在签到表目录中执行：

```powershell
powershell -ExecutionPolicy Bypass -File ".\\skills\\attendance-sheet-monthly-update\\scripts\\update-attendance-sheets.ps1" `
  -FolderPath . `
  -Year 2026 `
  -FromMonth 4 `
  -ToMonth 5 `
  -RosterChangesJson ".\\roster-changes.json"
```

如果只切换月份、不改名单，可以省略 `-RosterChangesJson`。

## 核对重点

- 每个文件的标题都已经从旧月份改成新月份。
- 指定班级的新增学生已经出现，删除学生已经消失。
- 非目标班级只改月份，不改名单。
- 模板尾部的 `课导老师签字`、说明区、空白名额行没有被覆盖。

## 资源

### scripts/

- `update-attendance-sheets.ps1`
  - 批量打开指定目录下的 `.xlsx`
  - 通过 Excel COM 修改标题月份
  - 读取和回写名单区，保留原格式
  - 输出每个文件的处理结果，适合重复执行
