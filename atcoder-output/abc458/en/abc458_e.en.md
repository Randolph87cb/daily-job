# E - Count 123

Source: https://atcoder.jp/contests/abc458/tasks/abc458_e?lang=en

Score : $450$ points

### Problem Statement

Find the number, modulo $998244353$, of sequences $A = (a_1, \cdots, a_{X_1 + X_2 + X_3})$ of length $X_1+X_2+X_3$ that satisfy all of the following conditions.

-   $A$ contains exactly $X_1$ copies of $1$, exactly $X_2$ copies of $2$, and exactly $X_3$ copies of $3$.
-   The absolute difference between adjacent elements is at most $1$. That is, for every integer $i$ satisfying $1 \leq i \leq X_1+X_2+X_3-1$, we have $|a_{i+1} - a_i| \leq 1$.

### Constraints

-   $1 \leq X_1, X_2, X_3 \leq 10^6$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$X_1$ $X_2$ $X_3$
```

### Output

Output the answer.

### Sample Input 1

```text
2 2 1
```

### Sample Output 1

```text
9
```

The sequences satisfying the conditions are the following nine:

-   $(1, 1, 2, 2, 3)$
-   $(1, 1, 2, 3, 2)$
-   $(1, 2, 1, 2, 3)$
-   $(1, 2, 3, 2, 1)$
-   $(2, 1, 1, 2, 3)$
-   $(2, 3, 2, 1, 1)$
-   $(3, 2, 1, 1, 2)$
-   $(3, 2, 1, 2, 1)$
-   $(3, 2, 2, 1, 1)$

### Sample Input 2

```text
5 3 4
```

### Sample Output 2

```text
204
```

### Sample Input 3

```text
998244 998353 998107
```

### Sample Output 3

```text
701926019
```
