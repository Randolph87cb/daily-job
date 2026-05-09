# F - Second Gap

分值：$525$ 分

---

### Problem Statement

You are given an integer $N$ and an integer sequence $D = (D_1, D_2, \ldots, D_{N-1})$ of length $N - 1$.

给定一个整数 $N$ 和一个长度为 $N - 1$ 的整数序列 $D = (D_1, D_2, \ldots, D_{N-1})$。

---

Find the number, modulo $998244353$, of permutations $P = (P_1, P_2, \ldots, P_N)$ of $(1, 2, \ldots, N)$ that satisfy the following condition.

求满足以下条件的 $(1, 2, \ldots, N)$ 的排列 $P = (P_1, P_2, \ldots, P_N)$ 的个数，答案对 $998244353$ 取模。

---

-   For each $1 \le i \le N - 1$, let $P_a$ and $P_b$ be the elements with the largest and the second largest values, respectively, among $(P_i, P_{i+1}, \ldots, P_N)$; then $|a - b| = D_i$.

- 对于每个 $1 \le i \le N - 1$，设 $P_a$ 和 $P_b$ 分别是 $(P_i, P_{i+1}, \ldots, P_N)$ 中值最大和第二大的元素，则满足 $|a - b| = D_i$。

---

### Constraints

-   $2 \le N \le 2 \times 10^5$
-   $1 \le D_i \le N - i$
-   All input values are integers.

- $2 \le N \le 2 \times 10^5$
- $1 \le D_i \le N - i$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$D_1$ $D_2$ $\ldots$ $D_{N-1}$

---

### Output

Output the number, modulo $998244353$, of permutations satisfying the condition.

输出满足条件的排列的个数，答案对 $998244353$ 取模。

---

### Sample Input 1

```text
3
1 1
```

---

### Sample Output 1

```text
4
```

---

For example, we can verify that $(2, 3, 1)$ satisfies the condition as follows.

例如，我们可以按如下方式验证 $(2, 3, 1)$ 满足条件：

---

-   We have $(P_1, P_2, P_3) = (2, 3, 1)$. The largest value is $P_2$ and the second largest value is $P_1$, and $|2 - 1| = 1 = D_1$.

- 我们有 $(P_1, P_2, P_3) = (2, 3, 1)$。最大值为 $P_2$，第二大值为 $P_1$，且 $|2 - 1| = 1 = D_1$。

---

-   We have $(P_2, P_3) = (3, 1)$. The largest value is $P_2$ and the second largest value is $P_3$, and $|2 - 3| = 1 = D_2$.

- 我们有 $(P_2, P_3) = (3, 1)$。最大值为 $P_2$，第二大值为 $P_3$，且 $|2 - 3| = 1 = D_2$。

---

Four permutations satisfy the condition: $(1, 2, 3), (1, 3, 2), (2, 3, 1), (3, 2, 1)$. Thus, output $4$.

共有四个排列满足条件：$(1, 2, 3), (1, 3, 2), (2, 3, 1), (3, 2, 1)$。因此输出 $4$。

---

### Sample Input 2

```text
5
1 2 2 1
```

---

### Sample Output 2

```text
0
```

---

### Sample Input 3

```text
15
4 4 4 4 4 4 3 2 2 2 2 2 1 1
```

---

### Sample Output 3

```text
70270200
```
