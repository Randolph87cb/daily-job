# D - Concat Power of 2

Source: https://atcoder.jp/contests/abc451/tasks/abc451_d?lang=en

Score : $400$ points

### Problem Statement

We call a positive integer a **good integer** if it satisfies the following condition.

-   Condition: It can be obtained by choosing one or more powers of $2$ ($1, 2, 4, 8, 16, \dots$) (repetition and reordering allowed), concatenating them as strings, and interpreting the result as an integer.

Find the $N$\-th smallest good integer. It is guaranteed that the $N$\-th smallest good integer is at most $10^9$.

### Constraints

-   $N$ is a positive integer.
-   The $N$\-th smallest good integer is at most $10^9$.

### Input

The input is given from Standard Input in the following format:

```text
$N$
```

### Output

Output the answer.

### Sample Input 1

```text
10
```

### Sample Output 1

```text
21
```

Listing good integers in ascending order gives $1, 2, 4, 8, 11, 12, 14, 16, 18, 21, \dots$.

### Sample Input 2

```text
69
```

### Sample Output 2

```text
328
```

### Sample Input 3

```text
1099898
```

### Sample Output 3

```text
819264512
```
