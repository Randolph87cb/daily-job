# E - Fibonacci String

Source: https://atcoder.jp/contests/abc450/tasks/abc450_e?lang=en

Score : $450$ points

### Problem Statement

You are given strings $X$ and $Y$. Define a sequence of strings $S_1, S_2, \dots$ as follows.

-   $S_1 = X$
-   $S_2 = Y$
-   For $i \geq 3$, $S_i$ is the concatenation of $S_{i-1}$ and $S_{i-2}$ in this order.

For each $i = 1, 2, \ldots, Q$, answer the following problem.

Problem: You are given integers $L_i, R_i$ and a character $C_i$. Find how many times character $C_i$ appears in the $L_i$\-th through $R_i$\-th characters of $S_{10^{18}}$.

### Constraints

-   $X$ and $Y$ are strings of lowercase English letters of length between $1$ and $10^4$, inclusive.
-   $1 \leq Q \leq 10^5$
-   $1 \leq L_i \leq R_i \leq 10^{18}$
-   $C_i$ is a lowercase English letter.
-   All given numerical values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$X$
$Y$
$Q$
$L_1$ $R_1$ $C_1$
$L_2$ $R_2$ $C_2$
$\vdots$
$L_Q$ $R_Q$ $C_Q$
```

### Output

Output $Q$ lines.  
The $i$\-th line should contain how many times character $C_i$ appears in the $L_i$\-th through $R_i$\-th characters of $S_{10^{18}}$.

### Sample Input 1

```text
a
b
6
2 7 a
1 3 b
3 7 b
1 9 c
1 1000000000000000000 b
1000000000000000000 1000000000000000000 a
```

### Sample Output 1

```text
3
2
3
0
618033988749894848
1
```

$S_3$, $S_4$, $S_5$ are `ba`, `bab`, `babba`, respectively.

$S_{10^{18}}$ is `babbababbabba...`, and the second through seventh characters contain three occurrences of `a`.
