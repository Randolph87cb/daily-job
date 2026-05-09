# C - Long Sequence

Source: https://atcoder.jp/contests/abc457/tasks/abc457_c?lang=en

Score : $300$ points

### Problem Statement

You are given integers $N$ and $K$, along with $N$ integer sequences $A_1, A_2, \ldots, A_N$ and a length-$N$ integer sequence $C = (C_1, C_2, \ldots, C_N)$. The length of integer sequence $A_i$ is $L_i$, and $A_i = (A_{i,1}, A_{i,2}, \ldots, A_{i,L_i})$. It is guaranteed that $\displaystyle 1 \le K \le \sum_{i=1}^N C_iL_i$.

Construct an integer sequence $B = (B_1, B_2, \ldots, B_{\sum_{i=1}^N C_iL_i})$ from $A$ and $C$ using the following procedure.

-   Let $B$ be an integer sequence of length $0$.
-   For $i = 1, 2, \ldots, N$ in this order, perform the following operation:
    -   Do this $C_i$ times: append $A_i$ to the end of $B$.

Find the value of $B_K$.

### Constraints

-   $1 \le N$
-   $1 \le L_i$
-   $\displaystyle \sum_{i=1}^N L_i \le 2 \times 10^5$
-   $1 \le A_{i,j} \le 10^9$ $(1 \le j \le L_i)$
-   $1 \le C_i \le 10^9$
-   $\displaystyle 1 \le K \le \sum_{i=1}^N C_iL_i$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $K$
$L_1$ $A_{1,1}$ $A_{1,2}$ $\ldots$ $A_{1,L_1}$
$L_2$ $A_{2,1}$ $A_{2,2}$ $\ldots$ $A_{2,L_2}$
$\vdots$
$L_N$ $A_{N,1}$ $A_{N,2}$ $\ldots$ $A_{N,L_N}$
$C_1$ $C_2$ $\ldots$ $C_N$
```

### Output

Output the answer.

### Sample Input 1

```text
3 9
3 1 3 2
1 3
2 4 3
1 3 2
```

### Sample Output 1

```text
4
```

$B$ is constructed as follows:

-   Let $B = ()$.
-   Append $A_1$ to the end of $B$ once. We get $B = (1, 3, 2)$.
-   Append $A_2$ to the end of $B$ three times. We get $B = (1, 3, 2, 3, 3, 3)$.
-   Append $A_3$ to the end of $B$ twice. We get $B = (1, 3, 2, 3, 3, 3, 4, 3, 4, 3)$.

For $B = (1, 3, 2, 3, 3, 3, 4, 3, 4, 3)$, we have $B_9 = 4$, so output $4$.

### Sample Input 2

```text
3 1
1 7
1 111
1 5
1 100 10000
```

### Sample Output 2

```text
7
```

### Sample Input 3

```text
3 3163812
5 1 2 3 4 5
4 9 8 7 6
2 10 11
87043 908415 9814
```

### Sample Output 3

```text
9
```
