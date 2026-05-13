# B - Mapping

Source: https://atcoder.jp/contests/abc454/tasks/abc454_b?lang=en

Score : $200$ points

### Problem Statement

There are $N$ people numbered $1$ through $N$.  
There are $M$ types of clothes numbered $1$ through $M$. Person $i$ is wearing clothes $F_i$.  
Answer the following two questions with Yes or No.

-   Question $1$: Are all $N$ people wearing different types of clothes?
-   Question $2$: For every one of the $M$ types of clothes, is there at least one person wearing that type?

### Constraints

-   $1 \leq N \leq 100$
-   $1 \leq M \leq 100$
-   $1 \leq F_i \leq M$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $M$
$F_1$ $F_2$ $\dots$ $F_N$
```

### Output

Output two lines. The $i$\-th line should contain `Yes` if the answer to question $i$ is Yes, and `No` if it is No.

### Sample Input 1

```text
3 4
1 2 4
```

### Sample Output 1

```text
Yes
No
```

Everyone is wearing a different type of clothes, so the answer to question $1$ is Yes.  
There is no person wearing clothes $3$, so the answer to question $2$ is No.

### Sample Input 2

```text
4 2
1 2 1 2
```

### Sample Output 2

```text
No
Yes
```

### Sample Input 3

```text
4 4
1 3 2 1
```

### Sample Output 3

```text
No
No
```

### Sample Input 4

```text
5 5
1 3 4 2 5
```

### Sample Output 4

```text
Yes
Yes
```
