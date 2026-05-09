# D - Greedy Customer

分值：$700$ 分

---

### Problem Statement

You are given positive integers $N,M$ and a sequence of positive integers $A=(A_1,A_2,\ldots,A_N)$ of length $N$.

给定正整数 $N,M$，以及一个长度为 $N$ 的正整数序列 $A=(A_1,A_2,\ldots,A_N)$。

---

For a positive integer $k$, define $f(k)$ as the answer to the following problem.

对于正整数 $k$，定义 $f(k)$ 为下述问题的答案。

---

> Takahashi has $k$ yen. AtCoder Store has $N$ items, and the $i$\-th item costs $A_i$ yen.
> 
> He performs the following action for $i=1,2,\ldots,N$ in order.
> 
> -   If the amount of money he currently has is at least $A_i$ yen, he purchases the $i$\-th item.
> 
> Find the total price of the items he purchased.

> 高桥有 $k$ 日元。AtCoder 商店有 $N$ 件商品，第 $i$ 件商品的价格为 $A_i$ 日元。
> 
> 他按顺序对 $i=1,2,\ldots,N$ 执行以下操作：
> 
> - 如果他当前持有的钱不少于 $A_i$ 日元，就购买第 $i$ 件商品。
> 
> 求他购买的商品的总价格。

---

Find $\displaystyle \bigoplus_{1\le k\le M} (k\times f(k))$. Here, $\displaystyle \bigoplus_{1\le k\le M} (k\times f(k))$ is defined as the bitwise $\mathrm{XOR}$ of $1\times f(1), 2\times f(2), \ldots, M\times f(M)$.

请求出 $\displaystyle \bigoplus_{1\le k\le M} (k\times f(k))$。其中 $\displaystyle \bigoplus_{1\le k\le M} (k\times f(k))$ 定义为 $1\times f(1), 2\times f(2), \ldots, M\times f(M)$ 的按位 $\mathrm{XOR}$。

---

You are given $T$ test cases; solve each of them.

给定 $T$ 组测试数据，请你分别求解每组数据。

---

**What is bitwise \mathrm{XOR}?**

**什么是按位 $\mathrm{XOR}$？**

---

The bitwise $\mathrm{XOR}$ of non-negative integers $A$ and $B$, $A \oplus B$, is defined as follows.

非负整数 $A$ 和 $B$ 的按位 $\mathrm{XOR}$ 结果记为 $A \oplus B$，其定义如下。

---

-   In the binary representation of $A \oplus B$, the digit at the $2^k$ ($k \geq 0$) place is $1$ if exactly one of the digits at the $2^k$ place in the binary representations of $A$ and $B$ is $1$, and $0$ otherwise.

- 在 $A \oplus B$ 的二进制表示中，若 $A$ 和 $B$ 的二进制表示的 $2^k$ 位恰好有一个是 $1$，则该位为 $1$，否则为 $0$。其中 $2^k$ 位对应 $2^{$k \geq 0$}$ 的位权。

---

For example, $3 \oplus 5 = 6$ (in binary: $011 \oplus 101 = 110$).  
In general, the bitwise $\mathrm{XOR}$ of $k$ non-negative integers $p_1, p_2, p_3, \dots, p_k$ is defined as $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$, and it can be proved that this does not depend on the order of $p_1, p_2, p_3, \dots, p_k$.

例如，$3 \oplus 5 = 6$（二进制表示为：$011 \oplus 101 = 110$）。
一般地，$k$ 个非负整数 $p_1, p_2, p_3, \dots, p_k$ 的按位 $\mathrm{XOR}$ 定义为 $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$，且可以证明该运算结果与 $p_1, p_2, p_3, \dots, p_k$ 的顺序无关。

---

### Constraints

-   $1\le T \le 10$
-   $1\le N,M$
-   The sum of $N$ over all test cases is at most $5\times 10^5$.
-   The sum of $M$ over all test cases is at most $5\times 10^7$.
-   $1\le A_i \le M$
-   All input values are integers.

- $1\le T \le 10$
- $1\le N,M$
- 所有测试数据的 $N$ 之和不超过 $5\times 10^5$。
- 所有测试数据的 $M$ 之和不超过 $5\times 10^7$。
- $1\le A_i \le M$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$T$  
$\text{case}_1$  
$\text{case}_2$  
$\vdots$  
$\text{case}_T$

---

Each test case is given in the following format:

每组测试数据按照以下格式给出：

$N$ $M$  
$A_1$ $A_2$ $\ldots$ $A_N$

---

### Output

Output the answers for the test cases in order, separated by newlines.

按顺序输出每组测试数据的答案，相邻答案之间用换行分隔。

---

### Sample Input 1

```text
3
3 6
2 3 1
5 10
3 1 4 1 5
7 12
4 2 3 4 2 3 3
```

---

### Sample Output 1

```text
61
115
190
```

---

Consider the first test case.

我们来看第一组测试数据。

---

For example, when Takahashi's initial amount of money is $3$ yen, he acts as follows.

例如，当高桥初始持有 $3$ 日元时，他的行为如下：

---

-   For $i=1$: he has $3$ yen, which is at least $2$ yen, so he purchases the first item.
-   For $i=2$: he has $1$ yen, which is less than $3$ yen, so he does not purchase the second item.
-   For $i=3$: he has $1$ yen, which is at least $1$ yen, so he purchases the third item.

- 当 $i=1$ 时：他有 $3$ 日元，不少于 $2$ 日元，因此购买第一件商品。
- 当 $i=2$ 时：他有 $1$ 日元，少于 $3$ 日元，因此不购买第二件商品。
- 当 $i=3$ 时：他有 $1$ 日元，不少于 $1$ 日元，因此购买第三件商品。

---

From this, we get $f(3)=2+1=3$.

由此可得 $f(3)=2+1=3$。

---

The values of $f(1),f(2),f(3),f(4),f(5),f(6)$ are $1,2,3,3,5,6$, respectively. Thus, the answer is the bitwise $\mathrm{XOR}$ of $1,4,9,12,25,36$, which is $61$.

$f(1),f(2),f(3),f(4),f(5),f(6)$ 的值分别为 $1,2,3,3,5,6$。因此答案是 $1,4,9,12,25,36$ 的按位 $\mathrm{XOR}$，即 $61$。
