# D - Card Pile Query

Source: https://atcoder.jp/contests/abc455/tasks/abc455_d?lang=en

Score : $400400400$ points

### Problem Statement

There are $NNN$ cards and $NNN$ piles of cards.

The cards and the piles are numbered $1,2,…,N1, 2, \ldots, N1,2,…,N$. Initially, pile $iii$ contains only card $iii$.

Perform the following operation for each $i=1,2,…,Qi = 1, 2, \ldots, Qi=1,2,…,Q$ in order:

-   Move card $CiC_iCi​$ and all cards stacked on top of card $CiC_iCi​$, preserving their order, on top of card $PiP_iPi​$. It is guaranteed that immediately before performing the operation, cards $CiC_iCi​$ and $PiP_iPi​$ are in different piles, and card $PiP_iPi​$ is on top of some pile.

Find the number of cards in each pile after all operations are completed.

### Constraints

-   $1≤N,Q≤3×1051 \leq N, Q \leq 3 \times 10^51≤N,Q≤3×105$
-   $1≤Ci,Pi≤N1 \leq C_i, P_i \leq N1≤Ci​,Pi​≤N$
-   When the operations are performed in order, immediately before each operation, cards $CiC_iCi​$ and $PiP_iPi​$ are in different piles.
-   When the operations are performed in order, immediately before each operation, card $PiP_iPi​$ is on top of some pile.
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$NNN$ $QQQ$
$C1C_1C1​$ $P1P_1P1​$
$C2C_2C2​$ $P2P_2P2​$
$⋮\vdots⋮$
$CQC_QCQ​$ $PQP_QPQ​$
```

### Output

Let $AiA_iAi​$ be the number of cards in pile $iii$ at the end. Output $A1,A2,…,ANA_1, A_2, \ldots, A_NA1​,A2​,…,AN​$ in this order, separated by spaces.

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
