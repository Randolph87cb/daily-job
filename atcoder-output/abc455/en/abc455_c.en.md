# C - Vanish

Source: https://atcoder.jp/contests/abc455/tasks/abc455_c?lang=en

Score : $300$ points

### Problem Statement

You are given an integer sequence $A = (A_1, A_2, \ldots, A_N)$.

Find the minimum possible sum of all elements of $A$ after performing the following operation exactly $K$ times.

-   Choose an integer $x$. For each $i$ such that $A_i = x$, replace the value of $A_i$ with $0$.

### Constraints

-   $1 \leq K \leq N \leq 3 \times 10^5$
-   $1 \leq A_i \leq 10^9$
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
6 2
7 2 7 2 2 9
```

### Sample Output 1

```text
6
```

Initially, $A = (7, 2, 7, 2, 2, 9)$.

Performing the operation with $x = 9$ gives $A = (7, 2, 7, 2, 2, 0)$.

Next, performing the operation with $x = 7$ gives $A = (0, 2, 0, 2, 2, 0)$.

At this point, the sum of all elements of $A$ is $0 + 2 + 0 + 2 + 2 + 0 = 6$.

### Sample Input 2

```text
8 6
1 2 3 4 1 2 3 4
```

### Sample Output 2

```text
0
```

### Sample Input 3

```text
10 2
3 3 4 1 1 3 3 1 5 1
```

### Sample Output 3

```text
8
```
