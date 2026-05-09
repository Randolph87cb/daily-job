# C - Long Sequence

分值：$300$ 分

---

### Problem Statement

You are given integers $N$ and $K$, along with $N$ integer sequences $A_1, A_2, \ldots, A_N$ and a length-$N$ integer sequence $C = (C_1, C_2, \ldots, C_N)$. The length of integer sequence $A_i$ is $L_i$, and $A_i = (A_{i,1}, A_{i,2}, \ldots, A_{i,L_i})$. It is guaranteed that $\displaystyle 1 \le K \le \sum_{i=1}^N C_iL_i$.

给定整数 $N$ 和 $K$，以及 $N$ 个整数序列 $A_1, A_2, \ldots, A_N$ 和一个长度为 $N$ 的整数序列 $C = (C_1, C_2, \ldots, C_N)$。整数序列 $A_i$ 的长度为 $L_i$，且满足 $A_i = (A_{i,1}, A_{i,2}, \ldots, A_{i,L_i})$。保证 $\displaystyle 1 \le K \le \sum_{i=1}^N C_iL_i$。

---

Construct an integer sequence $B = (B_1, B_2, \ldots, B_{\sum_{i=1}^N C_iL_i})$ from $A$ and $C$ using the following procedure.

通过以下步骤，由 $A$ 和 $C$ 构造整数序列 $B = (B_1, B_2, \ldots, B_{\sum_{i=1}^N C_iL_i})$。

---

-   Let $B$ be an integer sequence of length $0$.
-   For $i = 1, 2, \ldots, N$ in this order, perform the following operation:
    -   Do this $C_i$ times: append $A_i$ to the end of $B$.

- 设 $B$ 是一个长度为 $0$ 的整数序列。
- 按顺序对每个 $i = 1, 2, \ldots, N$ 执行以下操作：
  - 重复 $C_i$ 次：将 $A_i$ 追加到 $B$ 的末尾。

---

Find the value of $B_K$.

求 $B_K$ 的值。

---

### Constraints

-   $1 \le N$
-   $1 \le L_i$
-   $\displaystyle \sum_{i=1}^N L_i \le 2 \times 10^5$
-   $1 \le A_{i,j} \le 10^9$ $(1 \le j \le L_i)$
-   $1 \le C_i \le 10^9$
-   $\displaystyle 1 \le K \le \sum_{i=1}^N C_iL_i$
-   All input values are integers.

- $1 \le N$
- $1 \le L_i$
- $\displaystyle \sum_{i=1}^N L_i \le 2 \times 10^5$
- $1 \le A_{i,j} \le 10^9$ $(1 \le j \le L_i)$
- $1 \le C_i \le 10^9$
- $\displaystyle 1 \le K \le \sum_{i=1}^N C_iL_i$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $K$  
$L_1$ $A_{1,1}$ $A_{1,2}$ $\ldots$ $A_{1,L_1}$  
$L_2$ $A_{2,1}$ $A_{2,2}$ $\ldots$ $A_{2,L_2}$  
$\vdots$  
$L_N$ $A_{N,1}$ $A_{N,2}$ $\ldots$ $A_{N,L_N}$  
$C_1$ $C_2$ $\ldots$ $C_N$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
3 9
3 1 3 2
1 3
2 4 3
1 3 2
```

---

### Sample Output 1

```text
4
```

---

$B$ is constructed as follows:

$B$ 的构造过程如下：

---

-   Let $B = ()$.
-   Append $A_1$ to the end of $B$ once. We get $B = (1, 3, 2)$.
-   Append $A_2$ to the end of $B$ three times. We get $B = (1, 3, 2, 3, 3, 3)$.
-   Append $A_3$ to the end of $B$ twice. We get $B = (1, 3, 2, 3, 3, 3, 4, 3, 4, 3)$.

- 设 $B = ()$。
- 将 $A_1$ 追加到 $B$ 的末尾一次，得到 $B = (1, 3, 2)$。
- 将 $A_2$ 追加到 $B$ 的末尾三次，得到 $B = (1, 3, 2, 3, 3, 3)$。
- 将 $A_3$ 追加到 $B$ 的末尾两次，得到 $B = (1, 3, 2, 3, 3, 3, 4, 3, 4, 3)$。

---

For $B = (1, 3, 2, 3, 3, 3, 4, 3, 4, 3)$, we have $B_9 = 4$, so output $4$.

对于 $B = (1, 3, 2, 3, 3, 3, 4, 3, 4, 3)$，有 $B_9 = 4$，因此输出 $4$。

---

### Sample Input 2

```text
3 1
1 7
1 111
1 5
1 100 10000
```

---

### Sample Output 2

```text
7
```

---

### Sample Input 3

```text
3 3163812
5 1 2 3 4 5
4 9 8 7 6
2 10 11
87043 908415 9814
```

---

### Sample Output 3

```text
9
```
