# E - Reverse and Reverse

分值：$800$ 分

---

### Problem Statement

For a permutation $p=(p_1,p_2,\dots,p_N)$ of $(1,2,\dots,N)$ and a positive integer $M$, let $f(p,M)$ denote the answer to the following problem.

对于 $(1,2,\dots,N)$ 的一个排列 $p=(p_1,p_2,\dots,p_N)$ 和一个正整数 $M$，我们用 $f(p,M)$ 表示如下问题的答案。

---

> Perform the following operation $M$ times on $p$.
> 
> -   Choose an integer $i$ with $1 \le i \le N-1$, and reverse each of $(p_1,p_2,\dots,p_i)$ and $(p_{i+1},p_{i+2},\dots,p_N)$. Formally, replace $p$ with $(p_i,p_{i-1},\dots,p_1,p_N,p_{N-1},\dots,p_{i+1})$.
> 
> There are $(N-1)^M$ possible sequences of operations. Find the sum, modulo $998244353$, of "the number of inversions of $p$ after $M$ operations" over all such sequences.

> 对 $p$ 执行 $M$ 次以下操作。
> 
> - 选择满足 $1 \le i \le N-1$ 的整数 $i$，然后分别翻转 $(p_1,p_2,\dots,p_i)$ 和 $(p_{i+1},p_{i+2},\dots,p_N)$。形式化地，将 $p$ 替换为 $(p_i,p_{i-1},\dots,p_1,p_N,p_{N-1},\dots,p_{i+1})$。
> 
> 总共有 $(N-1)^M$ 种可能的操作序列。求所有这些序列对应的「执行 $M$ 次操作后 $p$ 的逆序对个数」之和，结果对 $998244353$ 取模。

---

You are given a permutation $P=(P_1,P_2,\dots,P_N)$ of $(1,2,\dots,N)$. Process the following query $Q$ times.

给定一个 $(1,2,\dots,N)$ 的排列 $P=(P_1,P_2,\dots,P_N)$，你需要处理 $Q$ 次询问。

---

-   You are given an integer $x$ with $1 \le x \le N-1$ and a positive integer $K$. Swap $P_x$ and $P_{x+1}$. Then, find $f(P,K)$.

- 给定满足 $1 \le x \le N-1$ 的整数 $x$ 和一个正整数 $K$。交换 $P_x$ 和 $P_{x+1}$，然后求出 $f(P,K)$。

---

### Constraints

-   $2 \le N \le 2 \times 10^5$
-   $1 \le Q \le 2 \times 10^5$
-   $P$ is a permutation of $(1,2,\dots,N)$.
-   $1 \le x \le N-1$
-   $1 \le K \le 10^9$
-   All input values are integers.

- $2 \le N \le 2 \times 10^5$
- $1 \le Q \le 2 \times 10^5$
- $P$ 是 $(1,2,\dots,N)$ 的一个排列。
- $1 \le x \le N-1$
- $1 \le K \le 10^9$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $Q$  
$P_1$ $P_2$ $\dots$ $P_N$  
$\mathrm{query}_1$  
$\mathrm{query}_2$  
$\vdots$  
$\mathrm{query}_Q$

---

Each query is given in the following format:

每个询问按照以下格式给出：

$x$ $K$

---

### Output

Output $Q$ lines. The $i$\-th line should contain the answer to $\mathrm{query}_i$.

输出 $Q$ 行。第 $i$ 行应包含第 $\mathrm{query}_i$ 个询问的答案。

---

### Sample Input 1

```text
3 2
1 3 2
1 1
2 1
```

---

### Sample Output 1

```text
4
4
```

---

For the first query, swapping $P_1$ and $P_2$ gives $P=(3,1,2)$. There are two possible sequences of operations as follows:

对于第一个询问，交换 $P_1$ 和 $P_2$ 后得到 $P=(3,1,2)$。共有两种可能的操作序列：

---

-   Choose $i = 1$. $P$ becomes $(3,2,1)$. The number of inversions is $3$.
-   Choose $i = 2$. $P$ becomes $(1,3,2)$. The number of inversions is $1$.

- 选择 $i = 1$，$P$ 变为 $(3,2,1)$，逆序对个数为 $3$。
- 选择 $i = 2$，$P$ 变为 $(1,3,2)$，逆序对个数为 $1$。

---

Thus, the answer is $3+1=4$.

因此答案为 $3+1=4$。

---

For the second query, swapping $P_2$ and $P_3$ gives $P=(3,2,1)$. There are two possible sequences of operations as follows:

对于第二个询问，交换 $P_2$ 和 $P_3$ 后得到 $P=(3,2,1)$。共有两种可能的操作序列：

---

-   Choose $i = 1$. $P$ becomes $(3,1,2)$. The number of inversions is $2$.
-   Choose $i = 2$. $P$ becomes $(2,3,1)$. The number of inversions is $2$.

- 选择 $i = 1$，$P$ 变为 $(3,1,2)$，逆序对个数为 $2$。
- 选择 $i = 2$，$P$ 变为 $(2,3,1)$，逆序对个数为 $2$。

---

Thus, the answer is $2+2=4$.

因此答案为 $2+2=4$。

---

### Sample Input 2

```text
4 4
3 2 4 1
2 1
2 2
3 3
1 4
```

---

### Sample Output 2

```text
11
28
67
242
```

---

### Sample Input 3

```text
10 7
7 9 3 10 5 2 4 6 8 1
2 29
1 86
3 30
8 64
1 24
1 9
5 55
```

---

### Sample Output 3

```text
29362950
633265500
847469581
741165544
385334408
653522086
169485402
```
