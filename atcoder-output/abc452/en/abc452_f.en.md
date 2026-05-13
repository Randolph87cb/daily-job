# F - Interval Inversion Count

Source: https://atcoder.jp/contests/abc452/tasks/abc452_f?lang=en

Score : $500$ points

### Problem Statement

You are given a positive integer $N$ and a permutation $P=(P _ 1,P _ 2,\ldots,P _ N)$ of $(1,2,\ldots,N)$.

You are given an integer $K$. Find the number of pairs of integers $(l,r)$ satisfying the following two conditions.

-   $1\le l\le r\le N$
-   The inversion number of the sequence $(P _ l,P _ {l+1},\ldots,P _ r)$ equals $K$.

### Constraints

-   $1\le N\le5\times10 ^ 5$
-   $0\le K\le\dfrac{N(N-1)}2$
-   $1\le P _ i\le N\ (1\le i\le N)$
-   $P _ i\ne P _ j\ (1\le i\lt j\le N)$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $K$
$P _ 1$ $P _ 2$ $\ldots$ $P _ N$
```

### Output

Output the number of pairs of integers $(l,r)$ satisfying the conditions.

### Sample Input 1

```text
7 3
6 3 2 1 7 5 4
```

### Sample Output 1

```text
5
```

For example, the inversion number of the sequence $(P _ 1,P _ 2,P _ 3)=(6,3,2)$ is $3$, so $(l,r)=(1,3)$ satisfies the conditions. The other pairs satisfying the conditions are $(l,r)=(2,4),(2,5),(4,7),(5,7)$, so output `5`.

### Sample Input 2

```text
4 1
1 2 3 4
```

### Sample Output 2

```text
0
```

The inversion number of every contiguous subsequence of $P$ is $0$, so there are no pairs $(l,r)$ satisfying the conditions. Thus, output `0`.

### Sample Input 3

```text
25 18
14 19 24 8 12 11 6 5 3 13 22 15 17 2 9 4 7 18 10 25 23 16 1 20 21
```

### Sample Output 3

```text
3
```
