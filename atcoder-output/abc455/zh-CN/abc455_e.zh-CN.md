# E - Unbalanced ABC Substrings

分值：$450450450$ 分

---

### Problem Statement

You are given a string $SSS$ of length $NNN$ consisting of the three characters `A`, `B`, and `C`.  
There are $N(N+1)2\frac{N(N+1)}{2}2N(N+1)​$ non-empty substrings of $SSS$; find how many of them satisfy the following condition:

给定长度为 $NNN$ 的字符串 $SSS$，仅包含 `A`、`B`、`C` 三种字符。

$SSS$ 共有 $N(N+1)2\frac{N(N+1)}{2}2N(N+1)​$ 个非空子串，请计算其中满足以下条件的子串数量：

---

-   The numbers of occurrences of `A`, `B`, and `C` are all distinct from each other.

- `A`、`B`、`C` 三者的出现次数互不相同。

---

Count two substrings separately if they are taken from different positions in $SSS$, even if they are identical as strings.

即使两个子串的内容完全相同，只要它们在 $SSS$ 中的位置不同，就视为不同的子串，需分别计数。

---

**What is a substring?**

**什么是子串？**

---

A **substring** of $SSS$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $SSS$. For example, `AB` is a substring of `ABC`, but `AC` is not a substring of `ABC`.

$SSS$ 的**子串**是指通过删除 $SSS$ 开头的零个或多个字符、以及结尾的零个或多个字符得到的字符串。例如，`AB` 是 `ABC` 的子串，但 `AC` 不是 `ABC` 的子串。

---

### Constraints

-   $1≤N≤2×1051 \leq N \leq 2 \times 10^51≤N≤2×105$
-   $∣S∣=N|S|=N∣S∣=N$
-   $NNN$ is an integer.
-   $SSS$ is a string consisting of the three characters `A`, `B`, and `C`.

- $1≤N≤2×1051 \leq N \leq 2 \times 10^51≤N≤2×105$
- $∣S∣=N|S|=N∣S∣=N$
- $NNN$ 是整数。
- $SSS$ 是仅由 `A`、`B`、`C` 三种字符构成的字符串。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$NNN$  
$SSS$

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

Deleting $000$ characters from the beginning and $333$ characters from the end of $SSS$ gives `AAB`, which satisfies the condition.  
Deleting $111$ character from the beginning and $222$ characters from the end of $SSS$ gives `ABB`, which satisfies the condition.  
Deleting $222$ characters from the beginning and $111$ character from the end of $SSS$ gives `BBC`, which satisfies the condition.  
Deleting $333$ characters from the beginning and $000$ characters from the end of $SSS$ gives `BCC`, which satisfies the condition.  
No other substrings satisfy the condition.

从 $SSS$ 开头删除 $000$ 个字符、结尾删除 $333$ 个字符，得到满足条件的 `AAB`。
从 $SSS$ 开头删除 $111$ 个字符、结尾删除 $222$ 个字符，得到满足条件的 `ABB`。
从 $SSS$ 开头删除 $222$ 个字符、结尾删除 $111$ 个字符，得到满足条件的 `BBC`。
从 $SSS$ 开头删除 $333$ 个字符、结尾删除 $000$ 个字符，得到满足条件的 `BCC`。
没有其他满足条件的子串。

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

不存在满足条件的子串。

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
