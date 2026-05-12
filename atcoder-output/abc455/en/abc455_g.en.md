# G - Balanced Subarrays

Source: https://atcoder.jp/contests/abc455/tasks/abc455_g?lang=en

Score : $625625625$ points

### Problem Statement

You are given a sequence $AAA$ of $NNN$ positive integers.  
Among the $N(N+1)2\frac{N(N+1)}{2}2N(N+1)​$ non-empty (contiguous) subarrays of $AAA$, we call a sequence $XXX$ a balanced sequence if and only if it satisfies the following condition:

-   Every integer appearing in $XXX$ appears the same number of times in $XXX$.

For each $k=1,2,…,Kk=1,2,\dots,Kk=1,2,…,K$, find the following two values:

-   The number of balanced sequences in which each integer appears exactly $BkB_kBk​$ times.
-   The number of balanced sequences in which exactly $BkB_kBk​$ distinct integers appear.

Count two subarrays separately if they are taken from different positions in $AAA$, even if they are identical as sequences.

Solve $TTT$ test cases per input.

### Constraints

-   $1≤T≤2×1051 \leq T \leq 2 \times 10^51≤T≤2×105$
-   $1≤N≤2×1051 \leq N \leq 2 \times 10^51≤N≤2×105$
-   $1≤K≤min⁡(N,10)1 \leq K \leq \min(N,10)1≤K≤min(N,10)$
-   $1≤Ai≤N1 \leq A_i \leq N1≤Ai​≤N$
-   $1≤Bk≤N1 \leq B_k \leq N1≤Bk​≤N$
-   $B1,B2,…,BKB_1,B_2,\dots,B_KB1​,B2​,…,BK​$ are pairwise distinct.
-   The sum of $NNN$ over all test cases is at most $2×1052 \times 10^52×105$.
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$TTT$
$case1\mathrm{case}_1case1​$
$case2\mathrm{case}_2case2​$
$⋮\vdots⋮$
$caseT\mathrm{case}_TcaseT​$
```

Each case is given in the following format:

```text
$NNN$ $KKK$  
$A1A_1A1​$ $A2A_2A2​$ $…\dots…$ $ANA_NAN​$  
$B1B_1B1​$ $B2B_2B2​$ $…\dots…$ $BKB_KBK​$  
```

### Output

Output the answers in the following format:

```text
$case1\mathrm{case}_1case1​$
$case2\mathrm{case}_2case2​$
$⋮\vdots⋮$
$caseT\mathrm{case}_TcaseT​$
```

For each case, letting $ck,1c_{k,1}ck,1​$ be the number of balanced sequences in which each integer appears exactly $BkB_kBk​$ times, and $ck,2c_{k,2}ck,2​$ be the number of balanced sequences in which exactly $BkB_kBk​$ distinct integers appear, output in the following format:

```text
$c1,1c_{1,1}c1,1​$ $c1,2c_{1,2}c1,2​$  
$c2,1c_{2,1}c2,1​$ $c2,2c_{2,2}c2,2​$  
$⋮\vdots⋮$
$cK,1c_{K,1}cK,1​$ $cK,2c_{K,2}cK,2​$  
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

For the first test case, the pairs $(l,r)(l,r)(l,r)$ such that the subarray of $AAA$ from the $lll$\-th through the $rrr$\-th element is a balanced sequence are $(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving eight instances in total.  
Among these, the ones in which each integer appears exactly twice are $(1,4)(1,4)(1,4)$, giving one instance, and the ones in which exactly two distinct integers appear are $(1,2),(1,4),(2,3),(3,4)(1,2),(1,4),(2,3),(3,4)(1,2),(1,4),(2,3),(3,4)$, giving four instances.  
Thus, for $k=1k=1k=1$, output `1 4`.  
Also, the ones in which each integer appears exactly once are $(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving seven instances, and the ones in which exactly one distinct integer appears are $(1,1),(2,2),(3,3),(4,4)(1,1),(2,2),(3,3),(4,4)(1,1),(2,2),(3,3),(4,4)$, giving four instances.  
Thus, for $k=2k=2k=2$, output `7 4`.
