# B - Split Ticketing

Source: https://atcoder.jp/contests/abc450/tasks/abc450_b?lang=en

Score : $200$ points

### Problem Statement

There are $N$ stations $1, 2, \dots, N$, arranged in a straight line from west to east in this order.  
The AtCoder Railway train passes through these $N$ stations and runs from west to east.  
For any two integers $i, j$ satisfying $1 \leq i \lt j \leq N$, the cost of boarding the train at station $i$ and getting off at station $j$ is $C_{i,j}$.

Determine whether there exist three integers $a, b, c$ such that:

-   $1 \leq a \lt b \lt c \leq N$
-   The total cost of boarding the train at station $a$, getting off at station $b$, then boarding the train again at station $b$, and getting off at station $c$ is less than the cost of boarding the train at station $a$ and getting off at station $c$.

### Constraints

-   $3 \leq N \leq 100$
-   $1 \leq C_{i,j} \leq 10^9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$C_{1,2}$ $C_{1,3}$ $\dots$ $C_{1,N}$
$C_{2,3}$ $\dots$ $C_{2,N}$
$\vdots$
$C_{N-1,N}$
```

### Output

If there exist three integers $a, b, c$ satisfying the conditions, output `Yes`; otherwise, output `No`, on a single line.

### Sample Input 1

```text
3
45 450
45
```

### Sample Output 1

```text
Yes
```

Choosing $(a, b, c) = (1, 2, 3)$,  
$C_{a,b}+C_{b,c}=C_{1,2}+C_{2,3}=45+45$  
$C_{a,c}=C_{1,3}=450$  
so the conditions are satisfied.

### Sample Input 2

```text
4
25 40 65
30 55
25
```

### Sample Output 2

```text
No
```

No choice of $(a, b, c)$ satisfies the conditions.
