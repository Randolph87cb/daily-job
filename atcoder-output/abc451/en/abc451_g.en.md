# G - Minimum XOR Walk

Source: https://atcoder.jp/contests/abc451/tasks/abc451_g?lang=en

Score : $600$ points

### Problem Statement

You are given a simple connected undirected graph with $N$ vertices and $M$ edges. The vertices are numbered $1$ through $N$ and the edges are numbered $1$ through $M$; edge $i$ is an undirected edge of weight $W_i$ connecting vertices $U_i$ and $V_i$.

The weight of a walk connecting two vertices is defined as the total XOR of the weights of the edges contained in the walk. If the same edge is traversed multiple times, that edge's weight contributes to the total XOR that many times.

You are given a non-negative integer $K$. Find the number of pairs of integers $(x, y)$ $(1 \leq x \lt y \leq N)$ such that the minimum weight of a walk connecting vertices $x$ and $y$ is at most $K$.

$T$ test cases are given; solve each one.

**What is a walk?**

For vertices $X$ and $Y$ in an undirected graph $G$, a sequence of $k$ vertices and $k-1$ edges alternately arranged $(v_1, e_1, v_2, \dots, v_{k-1}, e_{k-1}, v_k)$ such that $v_1 = X$, $v_k = Y$, and for each $i = 1, 2, \dots, k-1$, $e_i$ is an edge connecting $v_i$ and $v_{i+1}$, is called a **walk** from vertex $X$ to vertex $Y$.

**What is XOR?**

The bitwise XOR of non-negative integers $A$ and $B$, $A \oplus B$, is defined as follows.

-   The digit at the $2^k$ ($k \geq 0$) place in the binary representation of $A \oplus B$ is $1$ if exactly one of the digits at the $2^k$ place in the binary representations of $A$ and $B$ is $1$, and $0$ otherwise.

For example, $3 \oplus 5 = 6$ (in binary: $011 \oplus 101 = 110$). In general, the bitwise XOR of $k$ non-negative integers $p_1, p_2, p_3, \dots, p_k$ is defined as $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$, and it can be proved that this does not depend on the order of $p_1, p_2, p_3, \dots, p_k$.

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

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

Here, $\mathrm{case}_i$ denotes the input for the $i$\-th test case. Each test case is given in the following format:

```text
$N$ $M$ $K$
$U_1$ $V_1$ $W_1$
$U_2$ $V_2$ $W_2$
$\vdots$
$U_M$ $V_M$ $W_M$
```

### Output

Output $T$ lines. The $i$\-th line should contain the answer for the $i$\-th test case.

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

### Sample Output 1

```text
4
9
22
```

In the first test case, for example, the weight of the walk visiting vertices $1, 3, 2, 1, 3$ in order is $4 \oplus 2 \oplus 3 \oplus 4 = 1$.

It can be shown that the minimum weight of a walk connecting each pair of distinct vertices is as follows.

-   Vertices $1$ and $2$: minimum $3$
-   Vertices $1$ and $3$: minimum $1$
-   Vertices $1$ and $4$: minimum $2$
-   Vertices $2$ and $3$: minimum $2$
-   Vertices $2$ and $4$: minimum $1$
-   Vertices $3$ and $4$: minimum $3$

Among these, four pairs have a minimum value of at most $K(=2)$. Thus, output $4$ on the first line.
