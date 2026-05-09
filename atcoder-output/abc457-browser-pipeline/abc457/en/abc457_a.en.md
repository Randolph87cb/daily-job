# A - Array

Source: https://atcoder.jp/contests/abc457/tasks/abc457_a?lang=en

Score : $100$ points

### Problem Statement

You are given a sequence $A = (A_1, A_2, \cdots , A_N)$ of length $N$.

After that, an integer $X$ between $1$ and $N$, inclusive, is given.

Output the value of $A_X$.

### Constraints

-   $1 \le X \le N \le 100$
-   $1 \le A_i \le 100$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$A_1$ $A_2$ $\ldots$ $A_N$
$X$
```

### Output

Output the value of $A_X$.

### Sample Input 1

```text
5
1 2 3 4 5
3
```

### Sample Output 1

```text
3
```

We have $(A_1, A_2, A_3, A_4 , A_5) = (1, 2, 3, 4, 5)$. Since $A_3 = 3$, output $3$.

### Sample Input 2

```text
10
6 6 9 6 10 5 7 2 8 2
4
```

### Sample Output 2

```text
6
```

### Sample Input 3

```text
10
4 4 4 3 4 2 1 1 2 1
10
```

### Sample Output 3

```text
1
```
