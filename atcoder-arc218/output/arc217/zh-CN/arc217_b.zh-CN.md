# B - Not High Element

分值：$700$ 分

---

### Problem Statement

You are given integers $N,K$ and an integer sequence $A=(A_1,A_2,\ldots,A_K)$ of length $K$. It is guaranteed that each element of $A$ is between $1$ and $N$, inclusive, and all elements are distinct.

给定整数 $N,K$ 和一个长度为 $K$ 的整数序列 $A=(A_1,A_2,\ldots,A_K)$。保证 $A$ 的每个元素都在 $1$ 到 $N$ 之间（含两端），且所有元素互不相同。

---

For a permutation $P=(P_1,P_2,\ldots,P_N)$ of $(1,2,\ldots,N)$, define $f(P)$ as follows.

对于 $(1,2,\ldots,N)$ 的一个排列 $P=(P_1,P_2,\ldots,P_N)$，我们如下定义 $f(P)$。

---

-   The maximum number of times the following operation can be performed on $P$.
    -   Choose $2\le i\le N$ satisfying $P_i < \max(P_1,P_2,\ldots,P_{i-1})$, and move $P_i$ to the front. That is, replace $P$ with $(P_i,P_1,P_2,\ldots,P_{i-1},P_{i+1},\ldots,P_N)$.

- 对 $P$ 最多可以执行如下操作的次数：
    - 选择满足 $P_i < \max(P_1,P_2,\ldots,P_{i-1})$ 的 $2\le i\le N$，将 $P_i$ 移动到最前面。也就是将 $P$ 替换为 $(P_i,P_1,P_2,\ldots,P_{i-1},P_{i+1},\ldots,P_N)$。

---

There are $(N-K)!$ permutations $P$ of $(1,2,\ldots,N)$ satisfying $P_i=A_i$ for $i=1,2,\ldots,K$. Find the sum, modulo $998244353$, of $f(P)$ over all such permutations.

共有 $(N-K)!$ 个 $(1,2,\ldots,N)$ 的排列 $P$ 满足：对于 $i=1,2,\ldots,K$，有 $P_i=A_i$ 成立。求所有这样的排列对应的 $f(P)$ 的和，结果对 $998244353$ 取模。

---

You are given $T$ test cases; solve each of them.

给定 $T$ 组测试数据，你需要处理每一组数据。

---

### Constraints

-   $1\le T\le 10^5$
-   $1\le K\le N$
-   The sum of $N$ over all test cases is at most $5\times 10^5$.
-   $1\le A_i\le N$
-   All elements of $A$ are distinct.
-   All input values are integers.

- $1\le T\le 10^5$
- $1\le K\le N$
- 所有测试数据的 $N$ 之和不超过 $5\times 10^5$。
- $1\le A_i\le N$
- $A$ 的所有元素互不相同。
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

每个测试用例按照以下格式给出：

$N$ $K$  
$A_1$ $A_2$ $\ldots$ $A_K$

---

### Output

Output the answer for the test cases in order, separated by newlines.

按顺序输出每个测试用例的答案，答案之间用换行分隔。

---

### Sample Input 1

```text
3
3 1
1
4 2
3 2
10 3
2 1 7
```

---

### Sample Output 1

```text
2
6
1382640
```

---

Consider the first test case.

考虑第一个测试用例。

---

The permutations $P$ of $(1,2,\ldots,N)$ satisfying $P_i=A_i$ for $i=1,2,\ldots,K$ are $P=(1,2,3)$ and $P=(1,3,2)$, giving two permutations.

满足“对于 $i=1,2,\ldots,K$ 有 $P_i=A_i$ 成立”的 $(1,2,\ldots,N)$ 的排列 $P$ 是 $P=(1,2,3)$ 和 $P=(1,3,2)$，共 2 个排列。

---

When $P=(1,2,3)$, no operation can be performed, so $f(P)=0$.

当 $P=(1,2,3)$ 时，无法执行任何操作，因此 $f(P)=0$。

---

When $P=(1,3,2)$, the operation can be performed twice as follows.

当 $P=(1,3,2)$ 时，可以按照如下方式执行两次操作。

---

-   Choose $i=3$. Now $P=(2,1,3)$.
-   Choose $i=2$. Now $P=(1,2,3)$.

- 选择 $i=3$，此时 $P=(2,1,3)$。
- 选择 $i=2$，此时 $P=(1,2,3)$。

---

The operation cannot be performed three or more times, so $f(P)=2$ in this case.

无法执行三次或更多次操作，因此这种情况下 $f(P)=2$。

---

Thus, the answer is $0+2=2$.

因此，答案为 $0+2=2$。
