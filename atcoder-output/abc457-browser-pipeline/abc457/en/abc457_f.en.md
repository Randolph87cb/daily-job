# F - Second Gap

Source: https://atcoder.jp/contests/abc457/tasks/abc457_f?lang=en

Score : $525$ points

### Problem Statement

You are given an integer $N$ and an integer sequence $D = (D_1, D_2, \ldots, D_{N-1})$ of length $N - 1$.

Find the number, modulo $998244353$, of permutations $P = (P_1, P_2, \ldots, P_N)$ of $(1, 2, \ldots, N)$ that satisfy the following condition.

-   For each $1 \le i \le N - 1$, let $P_a$ and $P_b$ be the elements with the largest and the second largest values, respectively, among $(P_i, P_{i+1}, \ldots, P_N)$; then $|a - b| = D_i$.

### Constraints

-   $2 \le N \le 2 \times 10^5$
-   $1 \le D_i \le N - i$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$D_1$ $D_2$ $\ldots$ $D_{N-1}$
```

### Output

Output the number, modulo $998244353$, of permutations satisfying the condition.

### Sample Input 1

```text
3
1 1
```

### Sample Output 1

```text
4
```

For example, we can verify that $(2, 3, 1)$ satisfies the condition as follows.

-   We have $(P_1, P_2, P_3) = (2, 3, 1)$. The largest value is $P_2$ and the second largest value is $P_1$, and $|2 - 1| = 1 = D_1$.
    
-   We have $(P_2, P_3) = (3, 1)$. The largest value is $P_2$ and the second largest value is $P_3$, and $|2 - 3| = 1 = D_2$.
    

Four permutations satisfy the condition: $(1, 2, 3), (1, 3, 2), (2, 3, 1), (3, 2, 1)$. Thus, output $4$.

### Sample Input 2

```text
5
1 2 2 1
```

### Sample Output 2

```text
0
```

### Sample Input 3

```text
15
4 4 4 4 4 4 3 2 2 2 2 2 1 1
```

### Sample Output 3

```text
70270200
```
