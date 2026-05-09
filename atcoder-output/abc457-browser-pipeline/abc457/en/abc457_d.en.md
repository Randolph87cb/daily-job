# D - Raise Minimum

Source: https://atcoder.jp/contests/abc457/tasks/abc457_d?lang=en

Score : $400$ points

### Problem Statement

You are given a sequence $A = (A_1, A_2, \ldots, A_N)$ of length $N$ and an integer $K$.

You can perform the following operation between $0$ and $K$ times, inclusive.

-   Choose an integer $i$ satisfying $1 \le i \le N$, and add $i$ to $A_i$.

Find the maximum possible value of $\displaystyle \min_{1 \le i \le N} A_i$ for the sequence after the operations.

### Constraints

-   $1 \le N \le 2 \times 10^5$
-   $1 \le A_i \le 10^{18}$
-   $1 \le K \le 10^{18}$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $K$
$A_1$ $A_2$ $\ldots$ $A_N$
```

### Output

Output the answer.

### Sample Input 1

```text
3 3
1 2 3
```

### Sample Output 1

```text
3
```

For example, by choosing $i = 1$ twice and $i = 2$ once, the sequence becomes $(3, 4, 3)$. In this case, the minimum value is $3$.

It is impossible to make the minimum value $4$ or greater, so output $3$.

### Sample Input 2

```text
4 5
10 1 10 1
```

### Sample Output 2

```text
7
```

### Sample Input 3

```text
20 457
8 9 10 9 8 8 4 6 8 1 5 10 2 8 2 6 8 1 6 6
```

### Sample Output 3

```text
132
```
