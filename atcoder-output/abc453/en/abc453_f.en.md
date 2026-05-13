# F - Avoid Division

Source: https://atcoder.jp/contests/abc453/tasks/abc453_f?lang=en

Score : $550$ points

### Problem Statement

You are given a tree with $N$ vertices.  
The vertices are numbered vertex $1$, vertex $2$, $\ldots$, vertex $N$, and the $i$\-th edge $(1\leq i\leq N-1)$ connects vertices $U_i$ and $V_i$.

Takahashi will color each vertex with one of colors $1$, $2$, $\ldots$, $K$.  
Color $i$ can be used to color at most $C_i$ vertices.

Determine whether it is possible to color the vertices satisfying the following condition, and if so, output one valid coloring.

-   For every edge, there exists some $i$ $(1\leq i\leq K)$ such that both of the two subtrees obtained by cutting the tree at that edge contain at least one vertex colored with color $i$.

You are given $T$ test cases; solve each of them.

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

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

$\mathrm{case}_i$ represents the $i$\-th test case. Each test case is given in the following format:

```text
$N$ $K$
$U_1$ $V_1$
$U_2$ $V_2$
$\vdots$
$U_{N-1}$ $V_{N-1}$
$C_1$ $C_2$ $\ldots$ $C_K$
```

### Output

Output $T$ lines.  
On the $i$\-th line $(1\leq i\leq T)$, output the answer for the $i$\-th test case as follows.

If it is impossible to color the vertices satisfying the condition, output $-1$ alone.  
Otherwise, output $N$ integers $X_1,X_2,\ldots,X_N$ $(1\leq X_i\leq K)$ separated by spaces, such that coloring vertex $i$ with color $X_i$ for $i=1,2,\ldots,N$ satisfies the condition.

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

### Sample Output 1

```text
3 2 2 1 1
-1
```

For the first test case, suppose the vertices are colored as in the sample output.  
That is, vertex $1$ is colored with color $3$, vertex $2$ with color $2$, vertex $3$ with color $2$, vertex $4$ with color $1$, and vertex $5$ with color $1$.

If we cut the edge connecting vertices $1$ and $2$, the tree splits into the subtree consisting of vertices $1,3$ and the subtree consisting of vertices $2,4,5$; both subtrees contain a vertex colored with color $2$ (vertex $3$ or vertex $2$, respectively).  
Such a color exists no matter which edge of the given tree is cut, so the coloring in the sample output satisfies the condition.

For the second test case, there is no valid coloring satisfying the condition.
