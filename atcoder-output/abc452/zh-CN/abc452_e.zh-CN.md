# E - You WILL Like Sigma Problem

分值：$450$ 分

---

### Problem Statement

> Your lucky Greek letter for today is sigma. Solve this problem that uses sigma twice, and good fortune will surely come your way.

> 你今日的幸运希腊字母是 sigma（Σ）。解决这个用到了两次 sigma 的问题，好运一定会降临到你身上。

---

You are given a sequence of positive integers $A = (A_1, \cdots, A_N)$ of length $N$ and a sequence of positive integers $B = (B_1, \cdots, B_M)$ of length $M$.

给定长度为 $N$ 的正整数序列 $A = (A_1, \cdots, A_N)$，以及长度为 $M$ 的正整数序列 $B = (B_1, \cdots, B_M)$。

---

Find the value, modulo $998244353$, of $\displaystyle \sum_{i=1}^{N} \sum_{j=1}^{M} A_i \cdot B_j \cdot (i \bmod j)$.

求 $\displaystyle \sum_{i=1}^{N} \sum_{j=1}^{M} A_i \cdot B_j \cdot (i \bmod j)$ 的值模 $998244353$ 的结果。

---

### Constraints

-   $1 \leq N,M \leq 5 \times 10^5$
-   $1 \leq A_i, B_j \leq 5 \times 10^5$
-   All input values are integers.

-   $1 \leq N,M \leq 5 \times 10^5$
-   $1 \leq A_i, B_j \leq 5 \times 10^5$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $M$  
$A_1$ $A_2$ $\cdots$ $A_N$  
$B_1$ $B_2$ $\cdots$ $B_M$

---

### Output

Output the answer on a single line.

将答案输出在一行内。

---

### Sample Input 1

```text
6 4
1 6 9 2 3 1
1 10 3 7
```

---

### Sample Output 1

```text
508
```

---

The sum of the following $24$ values is $508$.

以下 $24$ 个值的和为 $508$。

---

-   $A_1 \cdot B_1 \cdot (1 \bmod 1) = 1 \cdot 1 \cdot 0 = 0$
-   $A_1 \cdot B_2 \cdot (1 \bmod 2) = 1 \cdot 10 \cdot 1 = 10$
-   $A_1 \cdot B_3 \cdot (1 \bmod 3) = 1 \cdot 3 \cdot 1 = 3$
-   $A_1 \cdot B_4 \cdot (1 \bmod 4) = 1 \cdot 7 \cdot 1 = 7$
-   $A_2 \cdot B_1 \cdot (2 \bmod 1) = 6 \cdot 1 \cdot 0 = 0$
-   $A_2 \cdot B_2 \cdot (2 \bmod 2) = 6 \cdot 10 \cdot 0 = 0$
-   $A_2 \cdot B_3 \cdot (2 \bmod 3) = 6 \cdot 3 \cdot 2 = 36$
-   $A_2 \cdot B_4 \cdot (2 \bmod 4) = 6 \cdot 7 \cdot 2 = 84$
-   $A_3 \cdot B_1 \cdot (3 \bmod 1) = 9 \cdot 1 \cdot 0 = 0$
-   $A_3 \cdot B_2 \cdot (3 \bmod 2) = 9 \cdot 10 \cdot 1 = 90$
-   $A_3 \cdot B_3 \cdot (3 \bmod 3) = 9 \cdot 3 \cdot 0 = 0$
-   $A_3 \cdot B_4 \cdot (3 \bmod 4) = 9 \cdot 7 \cdot 3 = 189$
-   $A_4 \cdot B_1 \cdot (4 \bmod 1) = 2 \cdot 1 \cdot 0 = 0$
-   $A_4 \cdot B_2 \cdot (4 \bmod 2) = 2 \cdot 10 \cdot 0 = 0$
-   $A_4 \cdot B_3 \cdot (4 \bmod 3) = 2 \cdot 3 \cdot 1 = 6$
-   $A_4 \cdot B_4 \cdot (4 \bmod 4) = 2 \cdot 7 \cdot 0 = 0$
-   $A_5 \cdot B_1 \cdot (5 \bmod 1) = 3 \cdot 1 \cdot 0 = 0$
-   $A_5 \cdot B_2 \cdot (5 \bmod 2) = 3 \cdot 10 \cdot 1 = 30$
-   $A_5 \cdot B_3 \cdot (5 \bmod 3) = 3 \cdot 3 \cdot 2 = 18$
-   $A_5 \cdot B_4 \cdot (5 \bmod 4) = 3 \cdot 7 \cdot 1 = 21$
-   $A_6 \cdot B_1 \cdot (6 \bmod 1) = 1 \cdot 1 \cdot 0 = 0$
-   $A_6 \cdot B_2 \cdot (6 \bmod 2) = 1 \cdot 10 \cdot 0 = 0$
-   $A_6 \cdot B_3 \cdot (6 \bmod 3) = 1 \cdot 3 \cdot 0 = 0$
-   $A_6 \cdot B_4 \cdot (6 \bmod 4) = 1 \cdot 7 \cdot 2 = 14$

-   $A_1 \cdot B_1 \cdot (1 \bmod 1) = 1 \cdot 1 \cdot 0 = 0$
-   $A_1 \cdot B_2 \cdot (1 \bmod 2) = 1 \cdot 10 \cdot 1 = 10$
-   $A_1 \cdot B_3 \cdot (1 \bmod 3) = 1 \cdot 3 \cdot 1 = 3$
-   $A_1 \cdot B_4 \cdot (1 \bmod 4) = 1 \cdot 7 \cdot 1 = 7$
-   $A_2 \cdot B_1 \cdot (2 \bmod 1) = 6 \cdot 1 \cdot 0 = 0$
-   $A_2 \cdot B_2 \cdot (2 \bmod 2) = 6 \cdot 10 \cdot 0 = 0$
-   $A_2 \cdot B_3 \cdot (2 \bmod 3) = 6 \cdot 3 \cdot 2 = 36$
-   $A_2 \cdot B_4 \cdot (2 \bmod 4) = 6 \cdot 7 \cdot 2 = 84$
-   $A_3 \cdot B_1 \cdot (3 \bmod 1) = 9 \cdot 1 \cdot 0 = 0$
-   $A_3 \cdot B_2 \cdot (3 \bmod 2) = 9 \cdot 10 \cdot 1 = 90$
-   $A_3 \cdot B_3 \cdot (3 \bmod 3) = 9 \cdot 3 \cdot 0 = 0$
-   $A_3 \cdot B_4 \cdot (3 \bmod 4) = 9 \cdot 7 \cdot 3 = 189$
-   $A_4 \cdot B_1 \cdot (4 \bmod 1) = 2 \cdot 1 \cdot 0 = 0$
-   $A_4 \cdot B_2 \cdot (4 \bmod 2) = 2 \cdot 10 \cdot 0 = 0$
-   $A_4 \cdot B_3 \cdot (4 \bmod 3) = 2 \cdot 3 \cdot 1 = 6$
-   $A_4 \cdot B_4 \cdot (4 \bmod 4) = 2 \cdot 7 \cdot 0 = 0$
-   $A_5 \cdot B_1 \cdot (5 \bmod 1) = 3 \cdot 1 \cdot 0 = 0$
-   $A_5 \cdot B_2 \cdot (5 \bmod 2) = 3 \cdot 10 \cdot 1 = 30$
-   $A_5 \cdot B_3 \cdot (5 \bmod 3) = 3 \cdot 3 \cdot 2 = 18$
-   $A_5 \cdot B_4 \cdot (5 \bmod 4) = 3 \cdot 7 \cdot 1 = 21$
-   $A_6 \cdot B_1 \cdot (6 \bmod 1) = 1 \cdot 1 \cdot 0 = 0$
-   $A_6 \cdot B_2 \cdot (6 \bmod 2) = 1 \cdot 10 \cdot 0 = 0$
-   $A_6 \cdot B_3 \cdot (6 \bmod 3) = 1 \cdot 3 \cdot 0 = 0$
-   $A_6 \cdot B_4 \cdot (6 \bmod 4) = 1 \cdot 7 \cdot 2 = 14$

---

### Sample Input 2

```text
20 20
36625 195265 98908 111868 111868 47382 147644 472464 472464 416653 111868 195265 327972 327972 262769 75439 381156 451275 36625 195265
327972 111868 416653 177330 340019 262769 47382 262769 47382 340019 47382 262769 327972 327972 359676 381156 327972 36625 451275 381156
```

---

### Sample Output 2

```text
58141644
```
