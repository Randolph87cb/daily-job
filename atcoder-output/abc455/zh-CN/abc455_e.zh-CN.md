# E - Unbalanced ABC Substrings

分值：$450$ 分

---

### Problem Statement

You are given a string $S$ of length $N$ consisting of the three characters `A`, `B`, and `C`.  
There are $\frac{N(N+1)}{2}$ non-empty substrings of $S$; find how many of them satisfy the following condition:

给定一个长度为 $N$ 的字符串 $S$，其仅包含三种字符 `A`、`B` 和 `C`。
字符串 $S$ 共有 $\frac{N(N+1)}{2}$ 个非空子串，请求出其中满足以下条件的子串数量：

---

-   The numbers of occurrences of `A`, `B`, and `C` are all distinct from each other.

- `A`、`B` 和 `C` 三者的出现次数互不相同。

---

Count two substrings separately if they are taken from different positions in $S$, even if they are identical as strings.

即使两个子串的内容完全相同，只要它们在 $S$ 中的位置不同，就需要被单独计数。

---

**What is a substring?**

**什么是子串？**

---

A **substring** of $S$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $S$. For example, `AB` is a substring of `ABC`, but `AC` is not a substring of `ABC`.

字符串 $S$ 的**子串**是指：通过删除 $S$ 开头的零个或多个字符，以及结尾的零个或多个字符后得到的字符串。例如，`AB` 是 `ABC` 的子串，但 `AC` 不是 `ABC` 的子串。

---

### Constraints

-   $1 \leq N \leq 2 \times 10^5$
-   $|S|=N$
-   $N$ is an integer.
-   $S$ is a string consisting of the three characters `A`, `B`, and `C`.

- $1 \leq N \leq 2 \times 10^5$
- $|S|=N$
- $N$ 是一个整数。
- $S$ 是一个仅由 `A`、`B` 和 `C` 三种字符组成的字符串。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$S$

---

### Output

Output the answer on a single line.

将答案输出在一行中。

---

### Sample Input 1

```text
6
AABBCC
```

---

### Sample Output 1

```text
4
```

---

Deleting $0$ characters from the beginning and $3$ characters from the end of $S$ gives `AAB`, which satisfies the condition.  
Deleting $1$ character from the beginning and $2$ characters from the end of $S$ gives `ABB`, which satisfies the condition.  
Deleting $2$ characters from the beginning and $1$ character from the end of $S$ gives `BBC`, which satisfies the condition.  
Deleting $3$ characters from the beginning and $0$ characters from the end of $S$ gives `BCC`, which satisfies the condition.  
No other substrings satisfy the condition.

删除 $S$ 开头的 $0$ 个字符和结尾的 $3$ 个字符，得到的 `AAB` 满足条件。
删除 $S$ 开头的 $1$ 个字符和结尾的 $2$ 个字符，得到的 `ABB` 满足条件。
删除 $S$ 开头的 $2$ 个字符和结尾的 $1$ 个字符，得到的 `BBC` 满足条件。
删除 $S$ 开头的 $3$ 个字符和结尾的 $0$ 个字符，得到的 `BCC` 满足条件。
没有其他子串满足条件。

---

### Sample Input 2

```text
6
ABCABC
```

---

### Sample Output 2

```text
0
```

---

No substring satisfies the condition.

没有子串满足条件。

---

### Sample Input 3

```text
10
ACABCAABAB
```

---

### Sample Output 3

```text
17
```
