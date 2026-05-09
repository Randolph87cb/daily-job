# B - Not High Element

Source: https://atcoder.jp/contests/arc217/tasks/arc217_b?lang=en

Score : $700$ points

### Problem Statement

You are given integers $N,K$ and an integer sequence $A=(A_1,A_2,\ldots,A_K)$ of length $K$. It is guaranteed that each element of $A$ is between $1$ and $N$, inclusive, and all elements are distinct.

For a permutation $P=(P_1,P_2,\ldots,P_N)$ of $(1,2,\ldots,N)$, define $f(P)$ as follows.

-   The maximum number of times the following operation can be performed on $P$.
    -   Choose $2\le i\le N$ satisfying $P_i < \max(P_1,P_2,\ldots,P_{i-1})$, and move $P_i$ to the front. That is, replace $P$ with $(P_i,P_1,P_2,\ldots,P_{i-1},P_{i+1},\ldots,P_N)$.

There are $(N-K)!$ permutations $P$ of $(1,2,\ldots,N)$ satisfying $P_i=A_i$ for $i=1,2,\ldots,K$. Find the sum, modulo $998244353$, of $f(P)$ over all such permutations.

You are given $T$ test cases; solve each of them.

### Constraints

-   $1\le T\le 10^5$
-   $1\le K\le N$
-   The sum of $N$ over all test cases is at most $5\times 10^5$.
-   $1\le A_i\le N$
-   All elements of $A$ are distinct.
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
$A_1$ $A_2$ $\ldots$ $A_K$
```

### Output

Output the answer for the test cases in order, separated by newlines.

### Sample Input 1

```text
3
3 1
1
4 2
3 2
10 3
2 1 7
```

### Sample Output 1

```text
2
6
1382640
```

Consider the first test case.

The permutations $P$ of $(1,2,\ldots,N)$ satisfying $P_i=A_i$ for $i=1,2,\ldots,K$ are $P=(1,2,3)$ and $P=(1,3,2)$, giving two permutations.

When $P=(1,2,3)$, no operation can be performed, so $f(P)=0$.

When $P=(1,3,2)$, the operation can be performed twice as follows.

-   Choose $i=3$. Now $P=(2,1,3)$.
-   Choose $i=2$. Now $P=(1,2,3)$.

The operation cannot be performed three or more times, so $f(P)=2$ in this case.

Thus, the answer is $0+2=2$.
