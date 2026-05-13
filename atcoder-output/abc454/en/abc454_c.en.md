# C - Straw Millionaire

Source: https://atcoder.jp/contests/abc454/tasks/abc454_c?lang=en

Score : $300$ points

### Problem Statement

There are $N$ types of items item $1$ through item $N$. Initially, Takahashi has only item $1$.

He has $M$ friends. If he gives item $A_i$ to the $i$\-th friend $(1\le i\le M)$, he will receive item $B_i$.

Find how many types of items he can obtain, including item $1$.

### Constraints

-   $2\le N\le 3\times 10^5$
-   $1\le M\le 3\times 10^5$
-   $1\le A_i,B_i\le N$
-   $A_i \neq B_i$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $M$
$A_1$ $B_1$
$A_2$ $B_2$
$\vdots$
$A_M$ $B_M$
```

### Output

Output the answer.

### Sample Input 1

```text
5 5
1 2
2 3
3 4
2 4
5 2
```

### Sample Output 1

```text
4
```

For example, Takahashi can obtain item $4$ by acting as follows:

-   Give item $1$ to the first friend. Receive item $2$.
-   Give item $2$ to the fourth friend. Receive item $4$.

He can obtain four types of items: items $1,2,3,4$. Thus, output $4$.

### Sample Input 2

```text
3 2
2 1
3 2
```

### Sample Output 2

```text
1
```

He can obtain one type of item: item $1$.

### Sample Input 3

```text
7 8
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
```

### Sample Output 3

```text
6
```
