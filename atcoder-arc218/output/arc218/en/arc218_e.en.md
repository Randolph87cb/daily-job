# E - Reverse and Reverse

Source: https://atcoder.jp/contests/arc218/tasks/arc218_e?lang=en

Score : $800$ points

### Problem Statement

For a permutation $p=(p_1,p_2,\dots,p_N)$ of $(1,2,\dots,N)$ and a positive integer $M$, let $f(p,M)$ denote the answer to the following problem.

> Perform the following operation $M$ times on $p$.
> 
> -   Choose an integer $i$ with $1 \le i \le N-1$, and reverse each of $(p_1,p_2,\dots,p_i)$ and $(p_{i+1},p_{i+2},\dots,p_N)$. Formally, replace $p$ with $(p_i,p_{i-1},\dots,p_1,p_N,p_{N-1},\dots,p_{i+1})$.
> 
> There are $(N-1)^M$ possible sequences of operations. Find the sum, modulo $998244353$, of "the number of inversions of $p$ after $M$ operations" over all such sequences.

You are given a permutation $P=(P_1,P_2,\dots,P_N)$ of $(1,2,\dots,N)$. Process the following query $Q$ times.

-   You are given an integer $x$ with $1 \le x \le N-1$ and a positive integer $K$. Swap $P_x$ and $P_{x+1}$. Then, find $f(P,K)$.

### Constraints

-   $2 \le N \le 2 \times 10^5$
-   $1 \le Q \le 2 \times 10^5$
-   $P$ is a permutation of $(1,2,\dots,N)$.
-   $1 \le x \le N-1$
-   $1 \le K \le 10^9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $Q$
$P_1\ P_2\ \dots\ P_N$
$\mathrm{query}_1$
$\mathrm{query}_2$
$\vdots$
$\mathrm{query}_Q$
```

Each query is given in the following format:

```text
$x$ $K$
```

### Output

Output $Q$ lines. The $i$\-th line should contain the answer to $\mathrm{query}_i$.

### Sample Input 1

```text
3 2
1 3 2
1 1
2 1
```

### Sample Output 1

```text
4
4
```

For the first query, swapping $P_1$ and $P_2$ gives $P=(3,1,2)$. There are two possible sequences of operations as follows:

-   Choose $i = 1$. $P$ becomes $(3,2,1)$. The number of inversions is $3$.
-   Choose $i = 2$. $P$ becomes $(1,3,2)$. The number of inversions is $1$.

Thus, the answer is $3+1=4$.

For the second query, swapping $P_2$ and $P_3$ gives $P=(3,2,1)$. There are two possible sequences of operations as follows:

-   Choose $i = 1$. $P$ becomes $(3,1,2)$. The number of inversions is $2$.
-   Choose $i = 2$. $P$ becomes $(2,3,1)$. The number of inversions is $2$.

Thus, the answer is $2+2=4$.

### Sample Input 2

```text
4 4
3 2 4 1
2 1
2 2
3 3
1 4
```

### Sample Output 2

```text
11
28
67
242
```

### Sample Input 3

```text
10 7
7 9 3 10 5 2 4 6 8 1
2 29
1 86
3 30
8 64
1 24
1 9
5 55
```

### Sample Output 3

```text
29362950
633265500
847469581
741165544
385334408
653522086
169485402
```
