# F - Make it Palindrome 2

分值：$525$ 分

---

### Problem Statement

You are given a positive integer $N$, a positive integer $M$, and an integer sequence $A=(A_1,A_2,\ldots,A_N)$ of length $N$. It is guaranteed that each element of $A$ is between $0$ and $M-1$, inclusive.

给定正整数 $N$、正整数 $M$，以及长度为 $N$ 的整数序列 $A=(A_1,A_2,\ldots,A_N)$。保证 $A$ 的每个元素都在 $0$ 到 $M-1$（含两端）的范围内。

---

You can perform the following operation on the integer sequence $A$ any number of times, possibly zero:

你可以对整数序列 $A$ 执行任意次（可以是 0 次）如下操作：

---

-   Choose a pair of integers $(l,r)$ satisfying $1\le l\le r\le N$, and replace $A_i$ with $(A_i+1) \bmod M$ for each $i=l,l+1,\ldots,r$.

-   选择一对满足 $1\le l\le r\le N$ 的整数 $(l,r)$，对每个 $i=l,l+1,\ldots,r$，将 $A_i$ 替换为 $(A_i+1) \bmod M$。

---

Find the minimum number of operations required to make $A$ a palindrome.

求将 $A$ 变为回文序列所需的最少操作次数。

---

Here, $A$ is a palindrome if $A_i=A_{N+1-i}$ holds for $i=1,2,\ldots,N$.

在这里，对于 $i=1,2,\ldots,N$，当 $A_i=A_{N+1-i}$ 成立时，我们称 $A$ 是回文的。

---

You are given $T$ test cases; solve each of them.

共有 $T$ 组测试数据，你需要解决每组数据。

---

### Constraints

-   $1\le T$
-   $1\le N\le 2\times 10^5$
-   $1\le M\le 10^9$
-   $0\le A_i < M$
-   The sum of $N$ over all test cases is at most $2\times 10^5$.
-   All input values are integers.

-   $1\le T$
-   $1\le N\le 2\times 10^5$
-   $1\le M\le 10^9$
-   $0\le A_i < M$
-   所有测试数据的 $N$ 之和不超过 $2\times 10^5$。
-   所有输入值均为整数。

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

按顺序输出每组测试数据的答案，答案之间用换行分隔。

---

### Sample Input 1

```text
3
4 5
0 3 1 2
1 20260418
454
7 12
3 1 4 1 5 9 2
```

---

### Sample Output 1

```text
3
0
5
```

---

Consider the first test case.

考虑第一组测试数据。

---

You can make $A$ a palindrome in three operations as follows:

你可以通过如下三次操作将 $A$ 变为回文序列：

---

-   Choose $(l,r)=(2,4)$. $A$ becomes $(0,4,2,3)$.
-   Choose $(l,r)=(3,4)$. $A$ becomes $(0,4,3,4)$.
-   Choose $(l,r)=(3,4)$. $A$ becomes $(0,4,4,0)$.

-   选择 $(l,r)=(2,4)$，此时 $A$ 变为 $(0,4,2,3)$。
-   选择 $(l,r)=(3,4)$，此时 $A$ 变为 $(0,4,3,4)$。
-   选择 $(l,r)=(3,4)$，此时 $A$ 变为 $(0,4,4,0)$。

---

It is impossible to make $A$ a palindrome in fewer than three operations, so output $3$.

无法用少于三次操作将 $A$ 变为回文序列，因此输出 $3$。
