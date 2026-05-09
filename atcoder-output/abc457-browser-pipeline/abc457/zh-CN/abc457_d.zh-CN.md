# D - Raise Minimum

分值：$400$ 分

---

### Problem Statement

You are given a sequence $A = (A_1, A_2, \ldots, A_N)$ of length $N$ and an integer $K$.

给定一个长度为 $N$ 的序列 $A = (A_1, A_2, \ldots, A_N)$ 和一个整数 $K$。

---

You can perform the following operation between $0$ and $K$ times, inclusive.

你可以执行操作的次数在 $0$ 到 $K$ 之间（包含两端）。

---

-   Choose an integer $i$ satisfying $1 \le i \le N$, and add $i$ to $A_i$.

-   选择满足 $1 \le i \le N$ 的整数 $i$，将 $i$ 加到 $A_i$ 上。

---

Find the maximum possible value of $\displaystyle \min_{1 \le i \le N} A_i$ for the sequence after the operations.

求操作后的序列中 $\displaystyle \min_{1 \le i \le N} A_i$ 的最大可能值。

---

### Constraints

-   $1 \le N \le 2 \times 10^5$
-   $1 \le A_i \le 10^{18}$
-   $1 \le K \le 10^{18}$
-   All input values are integers.

-   $1 \le N \le 2 \times 10^5$
-   $1 \le A_i \le 10^{18}$
-   $1 \le K \le 10^{18}$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $K$  
$A_1$ $A_2$ $\ldots$ $A_N$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
3 3
1 2 3
```

---

### Sample Output 1

```text
3
```

---

For example, by choosing $i = 1$ twice and $i = 2$ once, the sequence becomes $(3, 4, 3)$. In this case, the minimum value is $3$.

例如，选择 $i = 1$ 两次、$i = 2$ 一次，序列将变为 $(3, 4, 3)$。此时最小值为 $3$。

---

It is impossible to make the minimum value $4$ or greater, so output $3$.

无法让最小值达到 $4$ 或更大，因此输出 $3$。

---

### Sample Input 2

```text
4 5
10 1 10 1
```

---

### Sample Output 2

```text
7
```

---

### Sample Input 3

```text
20 457
8 9 10 9 8 8 4 6 8 1 5 10 2 8 2 6 8 1 6 6
```

---

### Sample Output 3

```text
132
```
