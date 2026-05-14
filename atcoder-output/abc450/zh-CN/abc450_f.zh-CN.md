# F - Strongly Connected 2

分值：$525$ 分

---

### Problem Statement

There is a directed graph with $N$ vertices and $N-1+M$ edges, with edges and vertices numbered.  
For $1 \leq i \leq M$, edge $i$ is a directed edge from vertex $X_i$ to vertex $Y_i$, and for $1 \leq i \leq N-1$, edge $M+i$ is a directed edge from vertex $i+1$ to vertex $i$.

有一个包含 $N$ 个顶点和 $N-1+M$ 条边的有向图，边和顶点均已编号。
对于 $1 \leq i \leq M$，边 $i$ 是从顶点 $X_i$ 到顶点 $Y_i$ 的有向边；对于 $1 \leq i \leq N-1$，边 $M+i$ 是从顶点 $i+1$ 到顶点 $i$ 的有向边。

---

There are $2^M$ ways to choose some (possibly zero) edges from among edges $1, 2, \dots, M$. Among these ways, how many result in the graph being strongly connected after deleting the chosen edges? Find the count modulo $998244353$.

从边 $1, 2, \dots, M$ 中选择若干条（可以是 0 条），共有 $2^M$ 种选择方式。在这些方式中，有多少种方式使得删除选中的边后，图仍然是强连通的？求答案对 $998244353$ 取模后的结果。

---

### Constraints

-   $2 \leq N \leq 2\times 10^5$
-   $1 \leq M \leq 2\times 10^5$
-   $1 \leq X_i < Y_i \leq N$
-   All input values are integers.

-   $2 \leq N \leq 2\times 10^5$
-   $1 \leq M \leq 2\times 10^5$
-   $1 \leq X_i < Y_i \leq N$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入以如下格式从标准输入给出：

$N$ $M$  
$X_1$ $Y_1$  
$X_2$ $Y_2$  
$\vdots$  
$X_M$ $Y_M$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
4 3
1 4
1 3
2 4
```

---

### Sample Output 1

```text
5
```

---

The graph is strongly connected when the set of chosen edge indices is one of $\{\}, \{1\}, \{2\}, \{3\}, \{2,3\}$, giving five ways.

当选中的边的下标集合为 $\{\}, \{1\}, \{2\}, \{3\}, \{2,3\}$ 中的任意一个时，图都是强连通的，因此共有 5 种方式。

---

### Sample Input 2

```text
10 11
1 4
1 4
3 9
2 5
3 4
9 10
6 9
4 10
1 3
8 10
4 7
```

---

### Sample Output 2

```text
1297
```

---

The given graph may have multi-edges.

给定的图可能存在重边。
