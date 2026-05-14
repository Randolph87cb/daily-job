# E - Fibonacci String

分值：$450$ 分

---

### Problem Statement

You are given strings $X$ and $Y$. Define a sequence of strings $S_1, S_2, \dots$ as follows.

给定字符串 $X$ 和 $Y$。按如下方式定义字符串序列 $S_1, S_2, \dots$：

---

-   $S_1 = X$
-   $S_2 = Y$
-   For $i \geq 3$, $S_i$ is the concatenation of $S_{i-1}$ and $S_{i-2}$ in this order.

-   $S_1 = X$
-   $S_2 = Y$
-   对于 $i \geq 3$，$S_i$ 是 $S_{i-1}$ 和 $S_{i-2}$ 按此顺序拼接得到的结果。

---

For each $i = 1, 2, \ldots, Q$, answer the following problem.

对于每个 $i = 1, 2, \ldots, Q$，回答以下问题。

---

Problem: You are given integers $L_i, R_i$ and a character $C_i$. Find how many times character $C_i$ appears in the $L_i$\-th through $R_i$\-th characters of $S_{10^{18}}$.

问题：给定整数 $L_i, R_i$ 和一个字符 $C_i$。求 $S_{10^{18}}$ 的第 $L_i$ 到第 $R_i$ 个字符中，字符 $C_i$ 出现的次数。

---

### Constraints

-   $X$ and $Y$ are strings of lowercase English letters of length between $1$ and $10^4$, inclusive.
-   $1 \leq Q \leq 10^5$
-   $1 \leq L_i \leq R_i \leq 10^{18}$
-   $C_i$ is a lowercase English letter.
-   All given numerical values are integers.

-   $X$ 和 $Y$ 是由小写英文字母组成的字符串，长度在 $1$ 到 $10^4$ 之间（含两端）。
-   $1 \leq Q \leq 10^5$
-   $1 \leq L_i \leq R_i \leq 10^{18}$
-   $C_i$ 是小写英文字母。
-   所有给出的数值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入以如下格式从标准输入给出：

$X$  
$Y$  
$Q$  
$L_1$ $R_1$ $C_1$  
$L_2$ $R_2$ $C_2$  
$\vdots$  
$L_Q$ $R_Q$ $C_Q$

---

### Output

Output $Q$ lines.  
The $i$\-th line should contain how many times character $C_i$ appears in the $L_i$\-th through $R_i$\-th characters of $S_{10^{18}}$.

输出 $Q$ 行。
第 $i$ 行应包含 $S_{10^{18}}$ 的第 $L_i$ 到第 $R_i$ 个字符中，字符 $C_i$ 出现的次数。

---

### Sample Input 1

```text
a
b
6
2 7 a
1 3 b
3 7 b
1 9 c
1 1000000000000000000 b
1000000000000000000 1000000000000000000 a
```

---

### Sample Output 1

```text
3
2
3
0
618033988749894848
1
```

---

$S_3$, $S_4$, $S_5$ are `ba`, `bab`, `babba`, respectively.

$S_3$、$S_4$、$S_5$ 分别为 `ba`、`bab`、`babba`。

---

$S_{10^{18}}$ is `babbababbabba...`, and the second through seventh characters contain three occurrences of `a`.

$S_{10^{18}}$ 为 `babbababbabba...`，其第 2 到第 7 个字符中包含 3 个 `a`。
