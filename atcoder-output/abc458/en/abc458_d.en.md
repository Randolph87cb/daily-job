# D - Chalkboard Median

Source: https://atcoder.jp/contests/abc458/tasks/abc458_d?lang=en

Score : $400$ points

### Problem Statement

There is one integer $X$ written on a blackboard.

You are given $Q$ queries to process in order. The $i$\-th query $(1 \le i \le Q)$ is as follows.

> Two integers $A_i$ and $B_i$ are given. Write two new integers $A_i$ and $B_i$ on the blackboard.
> 
> Then, output the median of the $2i+1$ integers written on the blackboard.

### Constraints

-   $1 \le X \le 10^9$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le A_i, B_i \le 10^9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$X$
$Q$
$A_1$ $B_1$
$A_2$ $B_2$
$\vdots$
$A_Q$ $B_Q$
```

### Output

Output $Q$ lines.

The $i$\-th line should contain the answer to the $i$\-th query.

### Sample Input 1

```text
5
3
2 3
1 2
8 9
```

### Sample Output 1

```text
3
2
3
```

In the first query, the integers written on the blackboard become $5, 2, 3$, and their median is $3$.

In the second query, the integers written on the blackboard become $5, 2, 3, 1, 2$, and their median is $2$.

In the third query, the integers written on the blackboard become $5, 2, 3, 1, 2, 8, 9$, and their median is $3$.

### Sample Input 2

```text
1
4
2 3
4 5
6 7
8 9
```

### Sample Output 2

```text
2
3
4
5
```

### Sample Input 3

```text
278117031
7
167642909 517897721
148434323 567739597
319926999 481642530
659199879 252516557
49913403 798318034
89701408 892537201
199166668 742285869
```

### Sample Output 3

```text
278117031
278117031
319926999
319926999
319926999
319926999
319926999
```
