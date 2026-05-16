# G - Children Yearn for the Evil Kindergarten

Source: https://atcoder.jp/contests/abc458/tasks/abc458_g?lang=en

Score : $625$ points

### Problem Statement

There are $10^{100}$ kids at a game venue. Initially, no kid has any medals.

A kid leaves the venue exactly when they either **drop out** or **escape**.

The game consists of $N$ days. On day $i$ ($1 \leq i \leq N$), the following sequence of operations is performed in order.

-   Collect all medals held by the kids at the venue, and let $s$ be the total number of collected medals.
-   Distribute $s + A_i$ medals freely among the kids at the venue (if there are no kids at the venue, do nothing).
-   Among the kids at the venue, those with fewer than $B_i$ medals drop out. Those with at least $B_i$ medals each lose $B_i$ medals.
-   Among the kids at the venue, those with at least $C_i$ medals each choose whether to escape at this point or remain at the venue.

Kids who remain at the venue at the end of the $N$ days drop out.

Find the maximum possible number of kids who ultimately escape.

You are given $T$ test cases; solve each of them.

### Constraints

-   $1 \leq T \leq 3 \times 10^5$
-   $1 \leq N \leq 3 \times 10^5$
-   $1 \leq A_i \leq 10^6$
-   $1 \leq B_i \leq 10^6$
-   $1 \leq C_i \leq 10^6$
-   The sum of $N$ over all test cases is at most $3 \times 10^5$.
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\mathrm{case}_{1}$
$\mathrm{case}_{2}$
$\vdots$
$\mathrm{case}_{T}$
```

Each test case is given in the following format:

```text
$N$
$A_1$ $B_1$ $C_1$
$A_2$ $B_2$ $C_2$
$\vdots$
$A_N$ $B_N$ $C_N$
```

### Output

Output the answers for the test cases in order, separated by newlines.

### Sample Input 1

```text
2
4
16 2 3
15 2 4
1 3 5
20 5 5
2
41404 1 941738
211877 205711 417821
```

### Sample Output 1

```text
5
0
```

Consider the first test case. By acting as follows, five kids can escape.

-   At the start of day $1$, collect $s = 0$ medals from $10^{100}$ kids. Then, proceed as follows.
    -   Distribute $0 + 16 = 16$ medals so that the kids' medal counts become $(5, 5, 2, 2, 2, 0, \dots, 0)$.
    -   The $10^{100} - 5$ kids with no medals drop out, and the remaining $5$ kids' medal counts become $(3, 3, 0, 0, 0)$.
    -   The $2$ kids with $3$ medals each choose to escape, and the remaining $3$ kids' medal counts become $(0, 0, 0)$.
-   At the start of day $2$, collect $s = 0$ medals from $3$ kids. Then, proceed as follows.
    -   Distribute $0 + 15 = 15$ medals so that the kids' medal counts becomes $(6, 6, 3)$.
    -   No one drops out, and the remaining $3$ kids' medal counts become $(4, 4, 1)$.
    -   $1$ kid with $4$ medals chooses to escape, and the remaining $2$ kids' medal counts become $(4, 1)$.
-   At the start of day $3$, collect $s = 5$ medals from $2$ kids. Then, proceed as follows.
    -   Distribute $5 + 1 = 6$ medals so that the kids' medal counts becomes $(3, 3)$.
    -   No one drops out, and the remaining $2$ kids' medal counts become $(0, 0)$.
    -   No one escapes.
-   At the start of day $4$, collect $s = 0$ medals from $2$ kids. Then, proceed as follows.
    -   Distribute $0 + 20 = 20$ medals so that the kids' medal counts becomes $(10, 10)$.
    -   No one drops out, and the remaining $2$ kids' medal counts become $(5, 5)$.
    -   The $2$ kids with $5$ medals each choose to escape, and the venue becomes empty.

In the second test case, not a single kid can escape.
