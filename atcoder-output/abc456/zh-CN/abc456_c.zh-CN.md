# C - Not Adjacent

分值：$300$ 分

---

### Problem Statement

You are given a string $S$ consisting of `a`, `b`, `c`.

给定一个字符串 $S$，其字符组成为 `a`、`b`、`c`。

---

Find the number of non-empty **substrings** of $S$ in which no two adjacent characters are the same, modulo $998244353$.

求 $S$ 的所有非空 **子串** 中，满足相邻两个字符互不相同的子串数量，结果对 $998244353$ 取模。

---

Two substrings are considered distinct if they are taken from different positions, even if they are identical as strings.

只要两个子串的位置不同，即使内容完全相同，也视为不同的子串。

---

**What is a substring?**

**什么是子串？**

---

A **substring** of $S$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $S$. For example, `ab` is a substring of `abc`, but `ac` is not a substring of `abc`.

$S$ 的 **子串** 是指从 $S$ 的开头删除若干个（可以是0个）字符，再从末尾删除若干个（可以是0个）字符后得到的字符串。例如，`ab` 是 `abc` 的子串，但 `ac` 不是 `abc` 的子串。

---

### Constraints

-   $S$ is a string of length between $1$ and $3 \times 10^5$, inclusive, consisting of `a`, `b`, `c`.

-   $S$ 是长度在 $1$ 到 $3 \times 10^5$ 之间（包含两端）的字符串，由 `a`、`b`、`c` 组成。

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
6
```

---

The substrings in which no two adjacent characters are the same are the following six:

满足相邻字符互不相同的子串共有以下6个：

---

-   `a` (from the $1$st to the $1$st character of $S$)
-   `b` (from the $2$nd to the $2$nd character of $S$)
-   `b` (from the $3$rd to the $3$rd character of $S$)
-   `c` (from the $4$th to the $4$th character of $S$)
-   `ab` (from the $1$st to the $2$nd character of $S$)
-   `bc` (from the $3$rd to the $4$th character of $S$)

-   `a`（取自 $S$ 的第 $1$ 个字符到第 $1$ 个字符）
-   `b`（取自 $S$ 的第 $2$ 个字符到第 $2$ 个字符）
-   `b`（取自 $S$ 的第 $3$ 个字符到第 $3$ 个字符）
-   `c`（取自 $S$ 的第 $4$ 个字符到第 $4$ 个字符）
-   `ab`（取自 $S$ 的第 $1$ 个字符到第 $2$ 个字符）
-   `bc`（取自 $S$ 的第 $3$ 个字符到第 $4$ 个字符）

---

Note that, as with the $2$nd and $3$rd entries, two substrings are considered distinct if they are taken from different positions, even if they are identical as strings.

注意，正如第 $2$ 项和第 $3$ 项所示，只要子串的位置不同，即使内容完全相同，也视为不同的子串。

---

### Sample Input 2

```text
cabcabcbcaccacbcbcaabacbacaabccacbccbcacbacbacabcacabcaccaaaaabababcbabacaccabbcacbcbcbcababcbcbabca
```

---

### Sample Output 2

```text
760
```
