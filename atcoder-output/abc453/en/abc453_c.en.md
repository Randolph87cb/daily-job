# C - Sneaking Glances

Source: https://atcoder.jp/contests/abc453/tasks/abc453_c?lang=en

Score : $300$ points

### Problem Statement

Takahashi is at coordinate $0.5$ on a number line.

He will make $N$ moves.  
In the $i$\-th move, he chooses either the positive direction or the negative direction, and moves $L_i$ in that direction.

What is the maximum number of times he can pass through coordinate $0$?  
Under the constraints of this problem, no move will end at coordinate $0$.

### Constraints

-   $1 \le N \le 20$
-   $1 \le L_i \le 10^9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$L_1$ $L_2$ $\dots$ $L_N$
```

### Output

Output the answer.

### Sample Input 1

```text
5
2 5 2 2 1
```

### Sample Output 1

```text
4
```

For example, by choosing the directions of movement as follows, he can pass through coordinate $0$ four times, which is the maximum.

-   In the first move, choose the negative direction and move $2$. He moves from coordinate $0.5$ to $-1.5$, passing through coordinate $0$.
-   In the second move, choose the positive direction and move $5$. He moves from coordinate $-1.5$ to $3.5$, passing through coordinate $0$.
-   In the third move, choose the negative direction and move $2$. He moves from coordinate $3.5$ to $1.5$.
-   In the fourth move, choose the negative direction and move $2$. He moves from coordinate $1.5$ to $-0.5$, passing through coordinate $0$.
-   In the fifth move, choose the positive direction and move $1$. He moves from coordinate $-0.5$ to $0.5$, passing through coordinate $0$.

### Sample Input 2

```text
5
100 1 2 3 4
```

### Sample Output 2

```text
1
```

### Sample Input 3

```text
20
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

### Sample Output 3

```text
20
```
