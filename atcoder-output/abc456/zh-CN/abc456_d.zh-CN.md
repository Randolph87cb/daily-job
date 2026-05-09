# D - Not Adjacent 2

分值：$400$ 分

---

### Problem Statement

You are given a string $S$ consisting of `a`, `b`, `c`.

给定一个仅由 `a`、`b`、`c` 组成的字符串 $S$。

---

Find the number of non-empty **subsequences** of $S$ in which no two adjacent characters are the same, modulo $998244353$.

请计算 $S$ 的满足「不存在两个相邻字符相同」的非空**子序列**的数量，结果对 $998244353$ 取模。

---

Two subsequences are considered distinct if they are taken from different positions, even if they are identical as strings.

只要选取的位置不同，即使对应的字符串内容完全相同，也视为不同的子序列。

---

**What is a subsequence?**

**什么是子序列？**

---

A **subsequence** of $S$ is a string obtained by removing zero or more characters from $S$ and concatenating the remaining characters in their original order. For example, `ab`, `ac` are subsequences of `abc`, but `ca`, `bb` are not subsequences of `abc`.

字符串 $S$ 的**子序列**是指：从 $S$ 中删除零个或多个字符后，将剩余字符按原顺序拼接得到的字符串。例如 `ab`、`ac` 是 `abc` 的子序列，但 `ca`、`bb` 不是 `abc` 的子序列。

---

### Constraints

-   $S$ is a string of length between $1$ and $3 \times 10^5$, inclusive, consisting of `a`, `b`, `c`.

- $S$ 是长度在 $1$ 到 $3 \times 10^5$ 之间（含两端）的字符串，仅由 `a`、`b`、`c` 组成。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$S$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
abbc
```

---

### Sample Output 1

```text
11
```

---

The subsequences in which no two adjacent characters are the same are the following $11$:

满足相邻字符互不相同的子序列共有以下 $11$ 个：

---

-   `a` (the $1$st character of $S$)
-   `b` (the $2$nd character of $S$)
-   `b` (the $3$rd character of $S$)
-   `c` (the $4$th character of $S$)
-   `ab` (the $1$st, $2$nd characters of $S$)
-   `ab` (the $1$st, $3$rd characters of $S$)
-   `ac` (the $1$st, $4$th characters of $S$)
-   `bc` (the $2$nd, $4$th characters of $S$)
-   `bc` (the $3$rd, $4$th characters of $S$)
-   `abc` (the $1$st, $2$nd, $4$th characters of $S$)
-   `abc` (the $1$st, $3$rd, $4$th characters of $S$)

- `a`（取自 $S$ 的第 $1$ 个字符）
- `b`（取自 $S$ 的第 $2$ 个字符）
- `b`（取自 $S$ 的第 $3$ 个字符）
- `c`（取自 $S$ 的第 $4$ 个字符）
- `ab`（取自 $S$ 的第 $1$、$2$ 个字符）
- `ab`（取自 $S$ 的第 $1$、$3$ 个字符）
- `ac`（取自 $S$ 的第 $1$、$4$ 个字符）
- `bc`（取自 $S$ 的第 $2$、$4$ 个字符）
- `bc`（取自 $S$ 的第 $3$、$4$ 个字符）
- `abc`（取自 $S$ 的第 $1$、$2$、$4$ 个字符）
- `abc`（取自 $S$ 的第 $1$、$3$、$4$ 个字符）

---

Note that, as with the $2$nd and $3$rd entries, two subsequences are considered distinct if they are taken from different positions, even if they are identical as strings.

注意，正如第 $2$ 项和第 $3$ 项所示，只要选取的位置不同，即使字符串内容相同，也视为不同的子序列。

---

### Sample Input 2

```text
cabcabcbcaccacbcbcaabacbacaabccacbccbcacbacbacabcacabcaccaaaaabababcbabacaccabbcacbcbcbcababcbcbabca
```

---

### Sample Output 2

```text
378217423
```

---

Output the count modulo $998244353$.

输出结果对 $998244353$ 取模。
