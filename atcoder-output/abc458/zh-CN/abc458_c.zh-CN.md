# C - C Stands for Center

分值：$300$ 分

---

### Problem Statement

You are given a string $S$ consisting of uppercase English letters.  
Find the number of substrings (contiguous subsequences) of $S$ that satisfy all of the following conditions.

给定一个由大写英文字母组成的字符串 $S$。
求 $S$ 的所有满足以下全部条件的子串（连续子序列）的数量。

---

-   It consists of an odd number of characters.
-   Its middle character is `C`. More formally, if the extracted substring consists of $l$ characters, its $((l+1)/2)$\-th character is `C`.

-   子串长度为奇数。
-   子串的中间字符为 `C`。更正式地，若取出的子串长度为 $l$，则其第 $((l+1)/2)$ 个字符是 `C`。

---

Even if two substrings are identical as strings, they are counted separately if they are extracted from different positions.

即使两个子串的内容完全相同，只要它们取自原串的不同位置，就需要分开计数。

---

### Constraints

-   $S$ is a string consisting of uppercase English letters with length between $1$ and $5 \times 10^5$, inclusive.

-   $S$ 是一个由大写英文字母组成的字符串，长度在 $1$ 到 $5 \times 10^5$ 之间（包含两端）。

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
ABCCA
```

---

### Sample Output 1

```text
5
```

---

In this input, $S=$ `ABCCA`.  
The substrings satisfying the conditions in the problem statement are the following five:

在该输入中，$S=$ `ABCCA`。
满足题目条件的子串共有以下 5 个：

---

-   `ABCCA`, extracted from the $1$st to $5$th characters of $S$
-   `BCC`, extracted from the $2$nd to $4$th characters of $S$
-   `C`, extracted from the $3$rd to $3$rd characters of $S$
-   `CCA`, extracted from the $3$rd to $5$th characters of $S$
-   `C`, extracted from the $4$th to $4$th characters of $S$

-   `ABCCA`，取自 $S$ 的第 $1$ 个字符到第 $5$ 个字符
-   `BCC`，取自 $S$ 的第 $2$ 个字符到第 $4$ 个字符
-   `C`，取自 $S$ 的第 $3$ 个字符到第 $3$ 个字符
-   `CCA`，取自 $S$ 的第 $3$ 个字符到第 $5$ 个字符
-   `C`，取自 $S$ 的第 $4$ 个字符到第 $4$ 个字符

---

### Sample Input 2

```text
XYZ
```

---

### Sample Output 2

```text
0
```

---

### Sample Input 3

```text
SMBCPROGRAMMINGCONTEST
```

---

### Sample Output 3

```text
11
```
