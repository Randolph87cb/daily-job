# E - Tree Growing

Source: https://atcoder.jp/contests/arc217/tasks/arc217_e?lang=en

Score : $900$ points

### Problem Statement

You are given a tree with $N$ vertices numbered $1$ to $N$. Here, $N$ is at least $2$. The $i$\-th edge $(1\le i\le N-1)$ connects vertices $u_i$ and $v_i$.

Perform the following operation on this tree exactly $K$ times. The $k$\-th operation $(1\le k\le K)$ is as follows.

-   Choose one of the $N-2+k$ edges of the tree at that point uniformly at random. Let $u$ and $v$ be the vertices connected by the chosen edge. Prepare a new vertex $N+k$, add edges connecting vertices $u$ and $N+k$ and connecting vertices $v$ and $N+k$, then delete the chosen edge.

Note that for $k=1,2,\ldots,K$, the tree will have $N+k$ vertices after the $k$\-th operation.

Find the expected value, modulo $998244353$, of $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ after $K$ operations. Here, $\text{dist}(i,j)$ denotes the distance between vertices $i$ and $j$ in the tree.

You are given $T$ test cases; solve each of them.

**Definition of expected value \ \text{mod}\ 998244353**

It can be proved that the expected value to be found is always a rational number. Moreover, under the constraints of this problem, when this rational number is expressed as an irreducible fraction $\displaystyle \frac{P}{Q}$, it can be proved that $Q \neq 0 \bmod 998244353$. Thus, there is a unique integer $R$ satisfying $R \times Q \equiv P \bmod 998244353, 0 \leq R \lt 998244353$. Find this $R$.

### Constraints

-   $1\le T$
-   $2\le N$
-   The sum of $N$ over all test cases is at most $3\times 10^5$.
-   $1\le K$
-   The sum of $K$ over all test cases is at most $10^6$.
-   $1\le u_i < v_i \le N$
-   The given graph is a tree.
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\text{case}_1$
$\text{case}_2$
$\vdots$
$\text{case}_T$
```

Each test case is given in the following format:

```text
$N$ $K$
$u_1$ $v_1$
$u_2$ $v_2$
$\vdots$
$u_{N-1}$ $v_{N-1}$
```

### Output

Output the answers for the test cases in order, separated by newlines.

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

### Sample Output 1

```text
499122208
120
713032723
```

Consider the first test case.

For example, the two operations proceed as follows.

-   Operation $1$: The edge connecting vertices $1$ and $2$ is chosen. After adding edges connecting vertices $1$ and $5$ and connecting vertices $2$ and $5$, the edge connecting vertices $1$ and $2$ is deleted.
-   Operation $2$: The edge connecting vertices $2$ and $5$ is chosen. After adding edges connecting vertices $2$ and $6$ and connecting vertices $5$ and $6$, the edge connecting vertices $2$ and $5$ is deleted.

In this case, the value of $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ is $32$.

The value of $\displaystyle \sum_{1\le i < j\le N+K} \text{dist}(i,j)$ is $31$ with probability $\displaystyle \frac12$ and $32$ with probability $\displaystyle \frac12$.
