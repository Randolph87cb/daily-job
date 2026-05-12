# G - Balanced Subarrays

Source: https://atcoder.jp/contests/abc455/tasks/abc455_g?lang=en

Score : $625$ points

### Problem Statement

You are given a sequence $A$ of $N$ positive integers.  
Among the $\frac{N(N+1)}{2}$ non-empty (contiguous) subarrays of $A$, we call a sequence $X$ a balanced sequence if and only if it satisfies the following condition:

-   Every integer appearing in $X$ appears the same number of times in $X$.

For each $k=1,2,\dots,K$, find the following two values:

-   The number of balanced sequences in which each integer appears exactly $B_k$ times.
-   The number of balanced sequences in which exactly $B_k$ distinct integers appear.

Count two subarrays separately if they are taken from different positions in $A$, even if they are identical as sequences.

Solve $T$ test cases per input.

### Constraints

-   $1 \leq T \leq 2 \times 10^5$
-   $1 \leq N \leq 2 \times 10^5$
-   $1 \leq K \leq \min(N,10)$
-   $1 \leq A_i \leq N$
-   $1 \leq B_k \leq N$
-   $B_1,B_2,\dots,B_K$ are pairwise distinct.
-   The sum of $N$ over all test cases is at most $2 \times 10^5$.
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

Each case is given in the following format:

```text
$N$ $K$  
$A_1$ $A_2$ $\dots$ $A_N$  
$B_1$ $B_2$ $\dots$ $B_K$  
```

### Output

Output the answers in the following format:

```text
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

For each case, letting $c_{k,1}$ be the number of balanced sequences in which each integer appears exactly $B_k$ times, and $c_{k,2}$ be the number of balanced sequences in which exactly $B_k$ distinct integers appear, output in the following format:

```text
$c_{1,1}$ $c_{1,2}$  
$c_{2,1}$ $c_{2,2}$  
$\vdots$
$c_{K,1}$ $c_{K,2}$  
```

### Sample Input 1

```text
3
4 2
1 2 1 2
2 1
1 1
1
1
7 7
1 5 5 1 5 1 2
1 2 3 4 5 6 7
```

### Sample Output 1

```text
1 4
7 4
1 1
13 8
3 8
1 1
0 0
0 0
0 0
0 0
```

For the first test case, the pairs $(l,r)$ such that the subarray of $A$ from the $l$\-th through the $r$\-th element is a balanced sequence are $(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving eight instances in total.  
Among these, the ones in which each integer appears exactly twice are $(1,4)$, giving one instance, and the ones in which exactly two distinct integers appear are $(1,2),(1,4),(2,3),(3,4)$, giving four instances.  
Thus, for $k=1$, output `1 4`.  
Also, the ones in which each integer appears exactly once are $(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving seven instances, and the ones in which exactly one distinct integer appears are $(1,1),(2,2),(3,3),(4,4)$, giving four instances.  
Thus, for $k=2$, output `7 4`.
