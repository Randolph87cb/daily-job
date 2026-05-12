# C - Vanish

分值：$300$ 分

---

### Problem Statement

You are given an integer sequence $A = (A_1, A_2, \ldots, A_N)$.

给定一个整数序列 $A = (A_1, A_2, \ldots, A_N)$。

---

Find the minimum possible sum of all elements of $A$ after performing the following operation exactly $K$ times.

你需要恰好执行 $K$ 次下述操作，求操作后 $A$ 的所有元素的最小可能总和。

---

-   Choose an integer $x$. For each $i$ such that $A_i = x$, replace the value of $A_i$ with $0$.

-   选择一个整数 $x$。对于每个满足 $A_i = x$ 的 $i$，将 $A_i$ 的值替换为 $0$。

---

### Constraints

-   $1 \leq K \leq N \leq 3 \times 10^5$
-   $1 \leq A_i \leq 10^9$
-   All input values are integers.

-   $1 \leq K \leq N \leq 3 \times 10^5$
-   $1 \leq A_i \leq 10^9$
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
6 2
7 2 7 2 2 9
```

---

### Sample Output 1

```text
6
```

---

Initially, $A = (7, 2, 7, 2, 2, 9)$.

初始时，$A = (7, 2, 7, 2, 2, 9)$。

---

Performing the operation with $x = 9$ gives $A = (7, 2, 7, 2, 2, 0)$.

选择 $x = 9$ 执行操作后，得到 $A = (7, 2, 7, 2, 2, 0)$。

---

Next, performing the operation with $x = 7$ gives $A = (0, 2, 0, 2, 2, 0)$.

接下来，选择 $x = 7$ 执行操作后，得到 $A = (0, 2, 0, 2, 2, 0)$。

---

At this point, the sum of all elements of $A$ is $0 + 2 + 0 + 2 + 2 + 0 = 6$.

此时，$A$ 的所有元素之和为 $0 + 2 + 0 + 2 + 2 + 0 = 6$。

---

### Sample Input 2

```text
8 6
1 2 3 4 1 2 3 4
```

---

### Sample Output 2

```text
0
```

---

### Sample Input 3

```text
10 2
3 3 4 1 1 3 3 1 5 1
```

---

### Sample Output 3

```text
8
```
