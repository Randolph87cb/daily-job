# D - Card Pile Query

Source: https://atcoder.jp/contests/abc455/tasks/abc455_d?lang=en

Score : $400$ points

### Problem Statement

There are $N$ cards and $N$ piles of cards.

The cards and the piles are numbered $1, 2, \ldots, N$. Initially, pile $i$ contains only card $i$.

Perform the following operation for each $i = 1, 2, \ldots, Q$ in order:

-   Move card $C_i$ and all cards stacked on top of card $C_i$, preserving their order, on top of card $P_i$. It is guaranteed that immediately before performing the operation, cards $C_i$ and $P_i$ are in different piles, and card $P_i$ is on top of some pile.

Find the number of cards in each pile after all operations are completed.

### Constraints

-   $1 \leq N, Q \leq 3 \times 10^5$
-   $1 \leq C_i, P_i \leq N$
-   When the operations are performed in order, immediately before each operation, cards $C_i$ and $P_i$ are in different piles.
-   When the operations are performed in order, immediately before each operation, card $P_i$ is on top of some pile.
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $Q$
$C_1$ $P_1$
$C_2$ $P_2$
$\vdots$
$C_Q$ $P_Q$
```

### Output

Let $A_i$ be the number of cards in pile $i$ at the end. Output $A_1, A_2, \ldots, A_N$ in this order, separated by spaces.

### Sample Input 1

```text
5 4
1 3
4 5
1 4
4 2
```

### Sample Output 1

```text
0 3 1 0 1
```

The sequence of operations proceeds as shown in the figure below.

![](https://img.atcoder.jp/abc455/aca7dea26cc92ed4ff7e4992208922ab.png)

### Sample Input 2

```text
7 8
3 1
5 4
2 5
5 7
2 3
6 2
3 4
5 1
```

### Sample Output 2

```text
2 0 0 4 0 0 1
```
