# F - Avoid Division

分值：$550$ 分

---

### Problem Statement

You are given a tree with $N$ vertices.  
The vertices are numbered vertex $1$, vertex $2$, $\ldots$, vertex $N$, and the $i$\-th edge $(1\leq i\leq N-1)$ connects vertices $U_i$ and $V_i$.

给定一棵包含 $N$ 个顶点的树。
顶点编号为 $1$, $2$, ..., $N$，第 $i$ 条边 $(1\leq i\leq N-1)$ 连接顶点 $U_i$ 和 $V_i$。

---

Takahashi will color each vertex with one of colors $1$, $2$, $\ldots$, $K$.  
Color $i$ can be used to color at most $C_i$ vertices.

高桥将为每个顶点着色，颜色可选值为 $1$, $2$, $\ldots$, $K$。
其中颜色 $i$ 最多可以用于 $C_i$ 个顶点。

---

Determine whether it is possible to color the vertices satisfying the following condition, and if so, output one valid coloring.

判断是否存在满足以下条件的着色方案，若存在则输出任意一种合法方案。

---

-   For every edge, there exists some $i$ $(1\leq i\leq K)$ such that both of the two subtrees obtained by cutting the tree at that edge contain at least one vertex colored with color $i$.

- 对于每条边，存在某个 $i$ $(1\leq i\leq K)$，使得将该边删去后得到的两个子树中，都至少有一个顶点被染为颜色 $i$。

---

You are given $T$ test cases; solve each of them.

共有 $T$ 个测试用例，你需要分别处理每个测试用例。

---

### Constraints

-   $1\leq T\leq 10^5$
-   $2\leq N\leq 3\times 10^5$
-   $1\leq K\leq N$
-   $1\leq U_i,V_i\leq N$
-   The given graph is a tree.
-   $1\leq C_i\leq N$
-   $C_1+C_2+\cdots+C_K\geq N$
-   All input values are integers.
-   The sum of $N$ over all test cases does not exceed $3\times 10^5$.

- $1\leq T\leq 10^5$
- $2\leq N\leq 3\times 10^5$
- $1\leq K\leq N$
- $1\leq U_i,V_i\leq N$
- 给定的图是一棵树。
- $1\leq C_i\leq N$
- $C_1+C_2+\cdots+C_K\geq N$
- 所有输入值均为整数。
- 所有测试用例的 $N$ 之和不超过 $3\times 10^5$。

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

$\mathrm{case}_i$ represents the $i$\-th test case. Each test case is given in the following format:

$\mathrm{case}_i$ 表示第 $i$ 个测试用例。每个测试用例按照以下格式给出：

$N$ $K$  
$U_1$ $V_1$  
$U_2$ $V_2$  
$\vdots$  
$U_{N-1}$ $V_{N-1}$  
$C_1$ $C_2$ $\ldots$ $C_K$

---

### Output

Output $T$ lines.  
On the $i$\-th line $(1\leq i\leq T)$, output the answer for the $i$\-th test case as follows.

输出 $T$ 行。
在第 $i$ 行 $(1\leq i\leq T)$ 中，按如下格式输出第 $i$ 个测试用例的答案。

---

If it is impossible to color the vertices satisfying the condition, output $-1$ alone.  
Otherwise, output $N$ integers $X_1,X_2,\ldots,X_N$ $(1\leq X_i\leq K)$ separated by spaces, such that coloring vertex $i$ with color $X_i$ for $i=1,2,\ldots,N$ satisfies the condition.

如果不存在满足条件的着色方案，单独输出 $-1$。
否则，输出 $N$ 个整数 $X_1,X_2,\ldots,X_N$ $(1\leq X_i\leq K)$，用空格分隔，其中对于每个 $i=1,2,\ldots,N$，顶点 $i$ 被染为颜色 $X_i$，这样的着色方案满足条件。

---

### Sample Input 1

```text
2
5 3
1 2
1 3
2 4
2 5
2 2 2
3 3
1 2
2 3
1 1 1
```

---

### Sample Output 1

```text
3 2 2 1 1
-1
```

---

For the first test case, suppose the vertices are colored as in the sample output.  
That is, vertex $1$ is colored with color $3$, vertex $2$ with color $2$, vertex $3$ with color $2$, vertex $4$ with color $1$, and vertex $5$ with color $1$.

对于第一个测试用例，假设顶点按样例输出的方式着色。
即顶点 $1$ 染为颜色 $3$，顶点 $2$ 染为颜色 $2$，顶点 $3$ 染为颜色 $2$，顶点 $4$ 染为颜色 $1$，顶点 $5$ 染为颜色 $1$。

---

If we cut the edge connecting vertices $1$ and $2$, the tree splits into the subtree consisting of vertices $1,3$ and the subtree consisting of vertices $2,4,5$; both subtrees contain a vertex colored with color $2$ (vertex $3$ or vertex $2$, respectively).  
Such a color exists no matter which edge of the given tree is cut, so the coloring in the sample output satisfies the condition.

如果我们删去连接顶点 $1$ 和 $2$ 的边，树会被拆分为由顶点 $1,3$ 组成的子树和由顶点 $2,4,5$ 组成的子树；两个子树中都包含颜色为 $2$ 的顶点（分别是顶点 $3$ 和顶点 $2$）。
无论删去给定树的哪一条边，都存在这样的颜色，因此样例输出的着色方案满足条件。

---

For the second test case, there is no valid coloring satisfying the condition.

对于第二个测试用例，不存在满足条件的合法着色方案。
