# G - Minimum XOR Walk

分值：$600$ 分

---

### Problem Statement

You are given a simple connected undirected graph with $N$ vertices and $M$ edges. The vertices are numbered $1$ through $N$ and the edges are numbered $1$ through $M$; edge $i$ is an undirected edge of weight $W_i$ connecting vertices $U_i$ and $V_i$.

给定一张包含 $N$ 个顶点和 $M$ 条边的简单连通无向图。顶点编号为 $1$ 到 $N$，边编号为 $1$ 到 $M$；其中边 $i$ 是一条连接顶点 $U_i$ 和 $V_i$ 的无向边，权值为 $W_i$。

---

The weight of a walk connecting two vertices is defined as the total XOR of the weights of the edges contained in the walk. If the same edge is traversed multiple times, that edge's weight contributes to the total XOR that many times.

连接两个顶点的路径（walk）的权值定义为路径中所有边的权值的异或和。若同一条边被经过多次，则其权值会在异或和中被计算对应次数。

---

You are given a non-negative integer $K$. Find the number of pairs of integers $(x, y)$ $(1 \leq x \lt y \leq N)$ such that the minimum weight of a walk connecting vertices $x$ and $y$ is at most $K$.

给定一个非负整数 $K$，求满足以下条件的整数对 $(x, y)$ $(1 \leq x \lt y \leq N)$ 的数量：连接顶点 $x$ 和 $y$ 的路径的最小权值不超过 $K$。

---

$T$ test cases are given; solve each one.

共有 $T$ 组测试数据，请你分别求解每组数据。

---

**What is a walk?**

**什么是路径（walk）？**

---

For vertices $X$ and $Y$ in an undirected graph $G$, a sequence of $k$ vertices and $k-1$ edges alternately arranged $(v_1, e_1, v_2, \dots, v_{k-1}, e_{k-1}, v_k)$ such that $v_1 = X$, $v_k = Y$, and for each $i = 1, 2, \dots, k-1$, $e_i$ is an edge connecting $v_i$ and $v_{i+1}$, is called a **walk** from vertex $X$ to vertex $Y$.

对于无向图 $G$ 中的顶点 $X$ 和 $Y$，由 $k$ 个顶点和 $k-1$ 条边交替排列构成的序列 $(v_1, e_1, v_2, \dots, v_{k-1}, e_{k-1}, v_k)$，若满足 $v_1 = X$、$v_k = Y$，且对于每个 $i = 1, 2, \dots, k-1$，$e_i$ 都是连接 $v_i$ 和 $v_{i+1}$ 的边，则该序列被称为从顶点 $X$ 到顶点 $Y$ 的 **路径（walk）**。

---

**What is XOR?**

**什么是异或？**

---

The bitwise XOR of non-negative integers $A$ and $B$, $A \oplus B$, is defined as follows.

非负整数 $A$ 和 $B$ 的按位异或 $A \oplus B$ 定义如下。

---

-   The digit at the $2^k$ ($k \geq 0$) place in the binary representation of $A \oplus B$ is $1$ if exactly one of the digits at the $2^k$ place in the binary representations of $A$ and $B$ is $1$, and $0$ otherwise.

- 若 $A$ 和 $B$ 的二进制表示中 $2^k$ 位恰好有一个是 $1$，则 $A \oplus B$ 的二进制表示的 $2^k$（即 $k \geq 0$）位为 $1$，否则为 $0$。

---

For example, $3 \oplus 5 = 6$ (in binary: $011 \oplus 101 = 110$). In general, the bitwise XOR of $k$ non-negative integers $p_1, p_2, p_3, \dots, p_k$ is defined as $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$, and it can be proved that this does not depend on the order of $p_1, p_2, p_3, \dots, p_k$.

例如，$3 \oplus 5 = 6$（二进制表示为：$011 \oplus 101 = 110$）。一般地，$k$ 个非负整数 $p_1, p_2, p_3, \dots, p_k$ 的按位异或定义为 $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$，可以证明该结果与 $p_1, p_2, p_3, \dots, p_k$ 的顺序无关。

---

### Constraints

-   $1 \leq T \leq 10^5$
-   $2 \leq N \leq 2 \times 10^5$
-   $N-1 \leq M \leq 2 \times 10^5$
-   $0 \leq K \lt 2^{30}$
-   $1 \leq U_i \lt V_i \leq N$
-   $0 \leq W_i \lt 2^{30}$
-   The given graph is simple and connected.
-   All input values are integers.
-   The sum of $N$ over all test cases in a single input is at most $2 \times 10^5$.
-   The sum of $M$ over all test cases in a single input is at most $2 \times 10^5$.

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2 \times 10^5$
- $N-1 \leq M \leq 2 \times 10^5$
- $0 \leq K \lt 2^{30}$
- $1 \leq U_i \lt V_i \leq N$
- $0 \leq W_i \lt 2^{30}$
- 给定的图是简单连通图。
- 所有输入值均为整数。
- 单组输入中所有测试数据的 $N$ 之和不超过 $2 \times 10^5$。
- 单组输入中所有测试数据的 $M$ 之和不超过 $2 \times 10^5$。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$T$  
$\mathrm{case}_1$  
$\mathrm{case}_2$  
$\vdots$  
$\mathrm{case}_T$

---

Here, $\mathrm{case}_i$ denotes the input for the $i$\-th test case. Each test case is given in the following format:

其中 $\mathrm{case}_i$ 表示第 $i$ 组测试数据的输入。每组测试数据按照以下格式给出：

$N$ $M$ $K$  
$U_1$ $V_1$ $W_1$  
$U_2$ $V_2$ $W_2$  
$\vdots$  
$U_M$ $V_M$ $W_M$

---

### Output

Output $T$ lines. The $i$\-th line should contain the answer for the $i$\-th test case.

输出 $T$ 行，第 $i$ 行应包含第 $i$ 组测试数据的答案。

---

### Sample Input 1

```text
3
4 4 2
3 4 3
1 3 4
1 2 3
2 3 2
5 7 14032
1 2 24681
3 5 25665
1 5 14154
2 3 23215
1 3 21259
4 5 24874
3 4 26495
8 10 109312507
6 8 793188457
7 8 501937135
1 2 954888411
2 7 109497327
1 6 791995625
2 6 665857693
1 3 101233808
1 7 114788578
4 6 953503358
5 8 624700613
```

---

### Sample Output 1

```text
4
9
22
```

---

In the first test case, for example, the weight of the walk visiting vertices $1, 3, 2, 1, 3$ in order is $4 \oplus 2 \oplus 3 \oplus 4 = 1$.

在第一组测试数据中，例如，按顺序经过顶点 $1, 3, 2, 1, 3$ 的路径的权值为 $4 \oplus 2 \oplus 3 \oplus 4 = 1$。

---

It can be shown that the minimum weight of a walk connecting each pair of distinct vertices is as follows.

可以证明，每对不同顶点之间的最小路径权值如下所示。

---

-   Vertices $1$ and $2$: minimum $3$
-   Vertices $1$ and $3$: minimum $1$
-   Vertices $1$ and $4$: minimum $2$
-   Vertices $2$ and $3$: minimum $2$
-   Vertices $2$ and $4$: minimum $1$
-   Vertices $3$ and $4$: minimum $3$

- 顶点 $1$ 和 $2$：最小值 $3$
- 顶点 $1$ 和 $3$：最小值 $1$
- 顶点 $1$ 和 $4$：最小值 $2$
- 顶点 $2$ 和 $3$：最小值 $2$
- 顶点 $2$ 和 $4$：最小值 $1$
- 顶点 $3$ 和 $4$：最小值 $3$

---

Among these, four pairs have a minimum value of at most $K(=2)$. Thus, output $4$ on the first line.

其中有四对的最小值不超过 $K(=2)$，因此第一行输出 $4$。
