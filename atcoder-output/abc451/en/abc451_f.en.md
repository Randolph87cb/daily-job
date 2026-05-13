# F - Make Bipartite 3

Source: https://atcoder.jp/contests/abc451/tasks/abc451_f?lang=en

Score : $500$ points

### Problem Statement

There is an undirected graph $G$ with $N$ vertices numbered $1$ through $N$ and zero edges.

$Q$ queries are given. In the $i$\-th query, an edge connecting vertices $u_i$ and $v_i$ is added to graph $G$.

Immediately after processing each query, determine whether it is possible to color each vertex of $G$ white or black so that the following condition is satisfied, and if possible, find the minimum possible number of vertices colored black.

-   For every edge, the two endpoints have different colors.

### Constraints

-   $2 \le N \le 2 \times 10^5$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le u_i \lt v_i \le N$
-   $(u_i, v_i) \ne (u_j, v_j) \ (i \ne j)$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $Q$
$u_1$ $v_1$
$u_2$ $v_2$
$\vdots$
$u_Q$ $v_Q$
```

### Output

Output $Q$ lines.

The $i$\-th line should contain the following value for graph $G$ immediately after processing the $i$\-th query.

-   If a valid coloring is possible, the minimum possible number of vertices colored black.
-   If no valid coloring is possible, $-1$.

### Sample Input 1

```text
4 4
1 2
2 3
3 4
1 3
```

### Sample Output 1

```text
1
1
2
-1
```

Immediately after processing queries $1, 2, 3$, a valid coloring exists.

For example, immediately after processing the third query, vertices $1, 2, 3, 4$ can be colored `white`, `black`, `white`, `black`, respectively. No valid coloring with fewer `black` vertices exists, so output $2$.

Immediately after processing the fourth query, no valid coloring exists. Thus, output $-1$.

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
