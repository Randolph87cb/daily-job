# E - Tree Growing

分值：$900$ 分

---

### Problem Statement

You are given a tree with $N$ vertices numbered $1$ to $N$. Here, $N$ is at least $2$. The $i$\-th edge $(1\le i\le N-1)$ connects vertices $u_i$ and $v_i$.

给定一棵有 $N$ 个顶点的树，顶点编号为 $1$ 到 $N$。保证 $N$ ≥ $2$。第 $i$ 条边 $(1\le i\le N-1)$ 连接顶点 $u_i$ 和 $v_i$。

---

Perform the following operation on this tree exactly $K$ times. The $k$\-th operation $(1\le k\le K)$ is as follows.

对这棵树恰好执行 $K$ 次操作。第 $k$ 次操作 $(1\le k\le K)$ 的内容如下。

---

-   Choose one of the $N-2+k$ edges of the tree at that point uniformly at random. Let $u$ and $v$ be the vertices connected by the chosen edge. Prepare a new vertex $N+k$, add edges connecting vertices $u$ and $N+k$ and connecting vertices $v$ and $N+k$, then delete the chosen edge.

- 从当前树的 $N-2+k$ 条边中等概率随机选择一条。设所选边连接的顶点为 $u$ 和 $v$。新建一个顶点 $N+k$，添加边 $u$-$N+k$ 和 $v$-$N+k$，然后删除选中的边。

---

Note that for $k=1,2,\ldots,K$, the tree will have $N+k$ vertices after the $k$\-th operation.

注意，对于 $k=1,2,\ldots,K$，第 $k$ 次操作结束后，树将有 $N+k$ 个顶点。

---

Find the expected value, modulo $998244353$, of $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ after $K$ operations. Here, $\text{dist}(i,j)$ denotes the distance between vertices $i$ and $j$ in the tree.

求 $K$ 次操作后 $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ 的期望值，结果对 $998244353$ 取模。其中 $\text{dist}(i,j)$ 表示树中顶点 $i$ 和 $j$ 之间的距离。

---

You are given $T$ test cases; solve each of them.

共有 $T$ 组测试数据，你需要处理每组数据。

---

**Definition of expected value \ \text{mod}\ 998244353**

**期望值对 998244353 取模的定义**

---

It can be proved that the expected value to be found is always a rational number. Moreover, under the constraints of this problem, when this rational number is expressed as an irreducible fraction $\displaystyle \frac{P}{Q}$, it can be proved that $Q \neq 0 \bmod 998244353$. Thus, there is a unique integer $R$ satisfying $R \times Q \equiv P \bmod 998244353, 0 \leq R \lt 998244353$. Find this $R$.

可以证明所求的期望值总是有理数。此外，在本题的约束条件下，将该有理数化为既约分数 $\displaystyle \frac{P}{Q}$ 时，可证 $Q \neq 0 \bmod 998244353$。因此存在唯一的整数 $R$ 满足 $R \times Q \equiv P \bmod 998244353, 0 \leq R \lt 998244353$，你需要求出这个 $R$。

---

### Constraints

-   $1\le T$
-   $2\le N$
-   The sum of $N$ over all test cases is at most $3\times 10^5$.
-   $1\le K$
-   The sum of $K$ over all test cases is at most $10^6$.
-   $1\le u_i < v_i \le N$
-   The given graph is a tree.
-   All input values are integers.

- $1\le T$
- $2\le N$
- 所有测试数据的 $N$ 之和不超过 $3\times 10^5$。
- $1\le K$
- 所有测试数据的 $K$ 之和不超过 $10^6$。
- $1\le u_i < v_i \le N$
- 给定的图是一棵树。
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

$N$ $K$  
$u_1$ $v_1$  
$u_2$ $v_2$  
$\vdots$  
$u_{N-1}$ $v_{N-1}$

---

### Output

Output the answers for the test cases in order, separated by newlines.

按顺序输出每组测试数据的答案，相邻答案用换行分隔。

---

### Sample Input 1

```text
3
4 2
1 2
1 3
1 4
4 5
1 2
2 3
3 4
6 13
1 2
1 3
2 4
2 5
3 6
```

---

### Sample Output 1

```text
499122208
120
713032723
```

---

Consider the first test case.

考虑第一组测试数据。

---

For example, the two operations proceed as follows.

例如，两次操作的过程如下。

---

-   Operation $1$: The edge connecting vertices $1$ and $2$ is chosen. After adding edges connecting vertices $1$ and $5$ and connecting vertices $2$ and $5$, the edge connecting vertices $1$ and $2$ is deleted.
-   Operation $2$: The edge connecting vertices $2$ and $5$ is chosen. After adding edges connecting vertices $2$ and $6$ and connecting vertices $5$ and $6$, the edge connecting vertices $2$ and $5$ is deleted.

- 第 $1$ 次操作：选中连接顶点 $1$ 和 $2$ 的边。添加边 $1$-$5$ 和 $2$-$5$ 后，删除连接顶点 $1$ 和 $2$ 的边。
- 第 $2$ 次操作：选中连接顶点 $2$ 和 $5$ 的边。添加边 $2$-$6$ 和 $5$-$6$ 后，删除连接顶点 $2$ 和 $5$ 的边。

---

In this case, the value of $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ is $32$.

这种情况下，$\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ 的值为 $32$。

---

The value of $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ is $31$ with probability $\displaystyle \frac12$ and $32$ with probability $\displaystyle \frac12$.

$\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ 的值为 $31$ 的概率是 $\displaystyle \frac12$，为 $32$ 的概率是 $\displaystyle \frac12$。
