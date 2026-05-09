# E - Crossing Table Cloth

Source: https://atcoder.jp/contests/abc457/tasks/abc457_e?lang=en

Score : $475$ points

### Problem Statement

There are $N$ cells arranged in a horizontal row. The $i$\-th cell from the left $(1 \le i \le N)$ is called cell $i$.

There are $M$ pieces of cloth. Laying cloth $i$ $(1 \le i \le M)$ covers cells $L_i$ through $R_i$.

Answer $Q$ queries. For the $q$\-th query $(1 \le q \le Q)$, integers $S_q$ and $T_q$ are given, so answer the following problem.

-   Determine whether it is possible to choose exactly two pieces of cloth from the $M$ pieces and lay them so that the following condition is satisfied.
    -   Cells $S_q$ through $T_q$ are covered by at least one piece of cloth, and no other cells are covered by any cloth.

### Constraints

-   $1 \le N \le 2 \times 10^5$
-   $2 \le M \le 2 \times 10^5$
-   $1 \le L_i \le R_i \le N$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le S_q \le T_q \le N$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $M$
$L_1$ $R_1$
$L_2$ $R_2$
$\vdots$
$L_M$ $R_M$
$Q$
$S_1$ $T_1$
$S_2$ $T_2$
$\vdots$
$S_Q$ $T_Q$
```

### Output

Output the answers for the queries, separated by newlines.

For each query, output `Yes` if it is possible to choose two pieces of cloth satisfying the condition, and `No` otherwise.

### Sample Input 1

```text
4 3
1 3
1 1
2 4
4
1 4
2 4
1 3
1 1
```

### Sample Output 1

```text
Yes
No
Yes
No
```

For the first query, the condition can be satisfied by choosing cloth $1$ and cloth $3$.

For the third query, the condition can be satisfied by choosing cloth $1$ and cloth $2$.

For the second and fourth queries, no choice of two pieces of cloth can satisfy the condition.

### Sample Input 2

```text
7 10
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
2 3
1 2
10
1 2
3 5
1 4
1 5
1 5
5 7
1 6
2 3
5 7
2 4
```

### Sample Output 2

```text
Yes
No
No
Yes
Yes
No
Yes
Yes
No
No
```
