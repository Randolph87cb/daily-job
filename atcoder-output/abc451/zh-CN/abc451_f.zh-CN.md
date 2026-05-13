# F - Make Bipartite 3

分值：$500$ 分

---

### Problem Statement

There is an undirected graph $G$ with $N$ vertices numbered $1$ through $N$ and zero edges.

现有一张无向图 $G$，包含 $N$ 个顶点，编号为 $1$ 到 $N$，初始时没有边。

---

$Q$ queries are given. In the $i$\-th query, an edge connecting vertices $u_i$ and $v_i$ is added to graph $G$.

共给出 $Q$ 次操作。第 $i$ 次操作会向图 $G$ 中加入一条连接顶点 $u_i$ 和 $v_i$ 的边。

---

Immediately after processing each query, determine whether it is possible to color each vertex of $G$ white or black so that the following condition is satisfied, and if possible, find the minimum possible number of vertices colored black.

每次操作完成后，判断是否可以将 $G$ 的每个顶点染成黑色或白色并满足以下条件；若可以，求出最少需要将多少个顶点染成黑色。

---

-   For every edge, the two endpoints have different colors.

- 对于每条边，其两个端点的颜色不同。

---

### Constraints

-   $2 \le N \le 2 \times 10^5$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le u_i \lt v_i \le N$
-   $(u_i, v_i) \ne (u_j, v_j) \ (i \ne j)$
-   All input values are integers.

- $2 \le N \le 2 \times 10^5$
- $1 \le Q \le 2 \times 10^5$
- $1 \le u_i \lt v_i \le N$
- $(u_i, v_i) \ne (u_j, v_j) \ (i \ne j)$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $Q$  
$u_1$ $v_1$  
$u_2$ $v_2$  
$\vdots$  
$u_Q$ $v_Q$

---

### Output

Output $Q$ lines.

输出 $Q$ 行。

---

The $i$\-th line should contain the following value for graph $G$ immediately after processing the $i$\-th query.

第 $i$ 行应输出完成第 $i$ 次操作后，图 $G$ 对应的以下结果：

---

-   If a valid coloring is possible, the minimum possible number of vertices colored black.
-   If no valid coloring is possible, $-1$.

- 若存在合法染色方案，输出最少的黑色顶点个数。
- 若不存在合法染色方案，输出 $-1$。

---

### Sample Input 1

```text
4 4
1 2
2 3
3 4
1 3
```

---

### Sample Output 1

```text
1
1
2
-1
```

---

Immediately after processing queries $1, 2, 3$, a valid coloring exists.

完成前 $1, 2, 3$ 次操作后，存在合法染色方案。

---

For example, immediately after processing the third query, vertices $1, 2, 3, 4$ can be colored `white`, `black`, `white`, `black`, respectively. No valid coloring with fewer `black` vertices exists, so output $2$.

例如，完成第三次操作后，可以将顶点 $1, 2, 3, 4$ 分别染为 `white`、`black`、`white`、`black`。不存在 `black` 顶点更少的合法染色方案，因此输出 $2$。

---

Immediately after processing the fourth query, no valid coloring exists. Thus, output $-1$.

完成第四次操作后，不存在合法染色方案，因此输出 $-1$。

---

### Sample Input 2

```text
10 10
1 10
6 7
2 7
4 9
5 9
6 10
7 8
2 5
3 4
8 10
```

---

### Sample Output 2

```text
1
2
2
3
3
3
3
4
4
4
```
