# F - Make it Palindrome 2

Source: https://atcoder.jp/contests/abc454/tasks/abc454_f?lang=en

Score : $525$ points

### Problem Statement

You are given a positive integer $N$, a positive integer $M$, and an integer sequence $A=(A_1,A_2,\ldots,A_N)$ of length $N$. It is guaranteed that each element of $A$ is between $0$ and $M-1$, inclusive.

You can perform the following operation on the integer sequence $A$ any number of times, possibly zero:

-   Choose a pair of integers $(l,r)$ satisfying $1\le l\le r\le N$, and replace $A_i$ with $(A_i+1) \bmod M$ for each $i=l,l+1,\ldots,r$.

Find the minimum number of operations required to make $A$ a palindrome.

Here, $A$ is a palindrome if $A_i=A_{N+1-i}$ holds for $i=1,2,\ldots,N$.

You are given $T$ test cases; solve each of them.

### Constraints

-   $1\le T$
-   $1\le N\le 2\times 10^5$
-   $1\le M\le 10^9$
-   $0\le A_i < M$
-   The sum of $N$ over all test cases is at most $2\times 10^5$.
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
$N$ $M$
$A_1$ $A_2$ $\ldots$ $A_N$
```

### Output

Output the answers for the test cases in order, separated by newlines.

### Sample Input 1

```text
3
4 5
0 3 1 2
1 20260418
454
7 12
3 1 4 1 5 9 2
```

### Sample Output 1

```text
3
0
5
```

Consider the first test case.

You can make $A$ a palindrome in three operations as follows:

-   Choose $(l,r)=(2,4)$. $A$ becomes $(0,4,2,3)$.
-   Choose $(l,r)=(3,4)$. $A$ becomes $(0,4,3,4)$.
-   Choose $(l,r)=(3,4)$. $A$ becomes $(0,4,4,0)$.

It is impossible to make $A$ a palindrome in fewer than three operations, so output $3$.
