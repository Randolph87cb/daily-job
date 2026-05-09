# G - Catch All Apples

Source: https://atcoder.jp/contests/abc457/tasks/abc457_g?lang=en

Score : $625$ points

### Problem Statement

$N$ apples fall on a number line. Apple $i$ falls at coordinate $X_i$ at time $T_i$.

You want to place some robots on the number line to collect all $N$ apples. The robots can be placed at any coordinates.

Each robot starts operating from time $0$ and can move freely along the number line at a speed of at most $1$. Multiple robots may occupy the same coordinate at the same time. Each robot can collect apple $i$ if and only if it is at coordinate $X_i$ at time $T_i$.

Find the minimum number of robots needed to collect all apples.

### Constraints

-   $1 \le N \le 3 \times 10^5$
-   $0 \le T_i \le 3 \times 10^5$
-   $0 \le X_i \le 3 \times 10^5$
-   $(T_i, X_i) \neq (T_j, X_j)$ $(i \neq j)$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$T_1$ $X_1$
$T_2$ $X_2$
$\vdots$
$T_N$ $X_N$
```

### Output

Output the answer.

### Sample Input 1

```text
4
0 2
1 0
2 1
2 3
```

### Sample Output 1

```text
2
```

All apples can be collected with two robots by moving them as follows:

-   Place robot $1$ at coordinate $0$ and robot $2$ at coordinate $2$.
-   Time $0$: Robot $2$ collects apple $1$.
-   Time $1$: Robot $1$ collects apple $2$. Move both robots in the positive direction at speed $1$ until time $2$.
-   Time $2$: Robot $1$ collects apple $3$ and robot $2$ collects apple $4$.

It is impossible to collect all apples with fewer than two robots, so output $2$.

### Sample Input 2

```text
5
0 1
0 2
0 3
0 4
0 5
```

### Sample Output 2

```text
5
```

### Sample Input 3

```text
8
10 4
4 2
7 10
5 3
1 9
0 6
3 8
0 9
```

### Sample Output 3

```text
2
```
