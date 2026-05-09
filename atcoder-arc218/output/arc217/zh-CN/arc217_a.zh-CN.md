# A - Min of Sum of XOR

分值：$500$ 分

---

### Problem Statement

You are given a positive integer $N$.

给定一个正整数 $N$。

---

Find one permutation $P=(P_1,P_2,\ldots,P_N)$ of $(1,2,\ldots,N)$ that minimizes $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$.

找到一个 $(1,2,\ldots,N)$ 的排列 $P=(P_1,P_2,\ldots,P_N)$，使得 $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$ 最小。

---

Here, $\displaystyle \bigoplus_{1\le j\le i} P_j$ is defined as the bitwise $\mathrm{XOR}$ of $P_1,P_2,\ldots,P_i$.

这里，$\displaystyle \bigoplus_{1\le j\le i} P_j$ 的定义是 $P_1,P_2,\ldots,P_i$ 的按位 $\mathrm{XOR}$。

---

You are given $T$ test cases; solve each of them.

给定 $T$ 组测试用例，每组测试用例都需要解决。

---

**What is bitwise \mathrm{XOR}?**

**什么是按位 \mathrm{XOR}？**

---

The bitwise $\mathrm{XOR}$ of non-negative integers $A$ and $B$, $A \oplus B$, is defined as follows.

非负整数 $A$ 和 $B$ 的按位 $\mathrm{XOR}$ 运算结果 $A \oplus B$ 定义如下。

---

-   In the binary representation of $A \oplus B$, the digit at the $2^k$ ($k \geq 0$) place is $1$ if exactly one of the digits at the $2^k$ place in the binary representations of $A$ and $B$ is $1$, and $0$ otherwise.

- 在 $A \oplus B$ 的二进制表示中，若 $A$ 和 $B$ 的二进制表示中第 $2^k$ 位的数字恰好有一个是 $1$，则第 $2^k$（$k \geq 0$）位的数字为 $1$，否则为 $0$。

---

For example, $3 \oplus 5 = 6$ (in binary: $011 \oplus 101 = 110$).  
In general, the bitwise $\mathrm{XOR}$ of $k$ non-negative integers $p_1, p_2, p_3, \dots, p_k$ is defined as $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$, and it can be proved that this does not depend on the order of $p_1, p_2, p_3, \dots, p_k$.

例如，$3 \oplus 5 = 6$（二进制表示为：$011 \oplus 101 = 110$）。
一般来说，$k$ 个非负整数 $p_1, p_2, p_3, \dots, p_k$ 的按位 $\mathrm{XOR}$ 运算结果定义为 $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$，可以证明该结果与 $p_1, p_2, p_3, \dots, p_k$ 的运算顺序无关。

---

### Constraints

-   $1\le T\le 10^3$
-   $1\le N$
-   The sum of $N$ over all test cases is at most $2\times 10^5$.
-   All input values are integers.

- $1\le T\le 10^3$
- $1\le N$
- 所有测试用例的 $N$ 之和不超过 $2\times 10^5$。
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

每组测试用例按照以下格式给出：

$N$

---

### Output

Output the answers for the test cases in order, separated by newlines.

按顺序输出所有测试用例的答案，答案之间用换行分隔。

---

For each test case, output a permutation $P=(P_1,P_2,\ldots,P_N)$ of $(1,2,\ldots,N)$ that minimizes $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$, separated by spaces.

对于每组测试用例，输出一个使得 $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$ 最小的 $(1,2,\ldots,N)$ 的排列 $P=(P_1,P_2,\ldots,P_N)$，排列中的元素用空格分隔。

---

If there are multiple permutations $P$ that achieve the minimum, any of them will be accepted.

如果存在多个达到最小值的排列 $P$，输出其中任意一个即可。

---

### Sample Input 1

```text
3
3
1
7
```

---

### Sample Output 1

```text
1 3 2
1
4 5 3 2 6 7 1
```

---

Consider the first test case.

考虑第一组测试用例。

---

If $P=(1,3,2)$, then $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j=1 + (1 \oplus 3) + (1 \oplus 3 \oplus 2) = 1+2+0=3$.

如果 $P=(1,3,2)$，则 $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j=1 + (1 \oplus 3) + (1 \oplus 3 \oplus 2) = 1+2+0=3$。

---

The value of $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$ cannot be made less than $3$, so outputting $P=(1,3,2)$ is correct.

$\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$ 的值无法小于 $3$，因此输出 $P=(1,3,2)$ 是正确的。

---

Outputting $P=(2,3,1)$ is also correct.

输出 $P=(2,3,1)$ 也是正确的。
