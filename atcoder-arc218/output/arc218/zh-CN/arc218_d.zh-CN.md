# D - I like Increasing

分值：$700$ 分

---

### Problem Statement

You are given a permutation $P=(P_1,P_2,\dots,P_N)$ of $(1,2,\dots,N)$.

给定一个长度为 $(1,2,\dots,N)$ 的排列 $P=(P_1,P_2,\dots,P_N)$。

---

For a sequence of integers $x=(x_1,x_2,\dots,x_k)$, define the **score** of $x$ as the number of indices $i$ satisfying $x_i < x_{i+1}$.

对于整数序列 $x=(x_1,x_2,\dots,x_k)$，定义 $x$ 的**得分**为满足 $x_i < x_{i+1}$ 的下标 $i$ 的数量。

---

Process the following query $Q$ times.

共需要处理 $Q$ 次如下询问。

---

-   You are given positive integers $l$ and $r$ with $1 \le l \le r \le N$. For $X = (P_l,P_{l+1},\dots,P_r)$, solve the following problem.
    -   Let $M$ be the maximum **score** of a non-empty subsequence of $X$. Find the minimum length of a non-empty subsequence of $X$ whose **score** equals $M$.

-   给定正整数 $l$ 和 $r$，满足 $1 \le l \le r \le N$。对于 $X = (P_l,P_{l+1},\dots,P_r)$，求解以下问题：
    -   设 $M$ 是 $X$ 的非空子序列能达到的最大**得分**，求所有得分等于 $M$ 的 $X$ 的非空子序列中，长度的最小值。

---

**What is a subsequence?**

**什么是子序列？**

---

A subsequence of a sequence $A$ is a sequence obtained by removing zero or more elements from $A$ and arranging the remaining elements in their original order.

序列 $A$ 的子序列是指从 $A$ 中删除零个或多个元素后，剩余元素保持原有顺序排列得到的序列。

---

### Constraints

-   $1 \le N,Q \le 2 \times 10^5$
-   $P$ is a permutation of $(1,2,\dots,N)$.
-   $1 \le l \le r \le N$
-   All input values are integers.

-   $1 \le N,Q \le 2 \times 10^5$
-   $P$ 是 $(1,2,\dots,N)$ 的一个排列。
-   $1 \le l \le r \le N$
-   所有输入值均为整数。

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

$l$ $r$

---

### Output

Output $Q$ lines. The $i$\-th line should contain the answer to $\mathrm{query}_i$.

输出 $Q$ 行，第 $i$ 行应包含第 $\mathrm{query}_i$ 个询问的答案。

---

### Sample Input 1

```text
6 4
2 1 4 6 3 5
1 3
3 6
2 2
1 6
```

---

### Sample Output 1

```text
2
4
1
5
```

---

For the first query, $X = (2,1,4)$. The maximum **score** $M = 1$ is achieved by $(2,4),(1,4),(2,1,4)$. The minimum length among these is $2$, achieved by $(2,4),(1,4)$.

对于第一个询问，$X = (2,1,4)$。最大得分 $M = 1$ 可由子序列 $(2,4),(1,4),(2,1,4)$ 达到，其中长度最小的是 $2$，由子序列 $(2,4),(1,4)$ 达到。

---

For the second query, $X = (4,6,3,5)$ and $M = 2$. $(4,6,3,5)$ achieves the minimum length $4$ among those with **score** $2$.

对于第二个询问，$X = (4,6,3,5)$，$M = 2$。在所有得分等于 $2$ 的子序列中，$(4,6,3,5)$ 达到了最小长度 $4$。

---

For the third query, $X = (1)$ and $M = 0$. $(1)$ achieves the minimum length $1$ with **score** $0$.

对于第三个询问，$X = (1)$，$M = 0$。子序列 $(1)$ 达到了最小长度 $1$，其得分为 $0$。

---

For the fourth query, $X = (2,1,4,6,3,5)$ and $M = 3$. $(2,4,6,3,5)$ achieves the minimum length $5$ with **score** $3$.

对于第四个询问，$X = (2,1,4,6,3,5)$，$M = 3$。子序列 $(2,4,6,3,5)$ 达到了最小长度 $5$，其得分为 $3$。

---

### Sample Input 2

```text
12 8
8 3 5 7 9 6 11 1 10 4 12 2
3 4
10 11
5 8
3 8
4 10
2 10
5 7
1 8
```

---

### Sample Output 2

```text
2
2
2
4
5
7
2
5
```
