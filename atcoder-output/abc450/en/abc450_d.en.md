# D - Minimize Range

Source: https://atcoder.jp/contests/abc450/tasks/abc450_d?lang=en

Score : $400$ points

### Problem Statement

You are given a sequence $A$ of $N$ positive integers and a positive integer $K$.  
You can perform the following operation on the sequence $A$ any number of times.

-   Choose an integer $i$ with $1 \leq i \leq N$, and add $K$ to $A_i$.

Find the minimum possible value of $\max(A) - \min(A)$.

### Constraints

-   $1 \leq N \leq 2 \times 10^5$
-   $1 \leq K \leq 10^9$
-   $1 \leq A_i \leq 10^9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $K$
$A_1$ $A_2$ $\dots$ $A_N$
```

### Output

Output the answer on a single line.

### Sample Input 1

```text
3 10
3 21 9
```

### Sample Output 1

```text
4
```

First, choosing $i=1$ makes the sequence $A=(13,21,9)$.  
Next, choosing $i=3$ makes the sequence $A=(13,21,19)$.  
Next, choosing $i=1$ makes the sequence $A=(23,21,19)$.  
At this point, $\max(A)-\min(A)=23-19=4$.  
It is impossible to make $\max(A)-\min(A)$ at most $3$, so the answer is $4$.

### Sample Input 2

```text
5 6
4 100 5 10 450
```

### Sample Output 2

```text
2
```
