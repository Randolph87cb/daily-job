# B - Personnel Change

Source: https://atcoder.jp/contests/abc451/tasks/abc451_b?lang=en

Score : $200$ points

### Problem Statement

The company where Takahashi works has $N$ employees, each assigned an employee number from $1, 2, \dots, N$. There are $M$ departments in the company, called departments $1, 2, \dots, M$.

Employee $i$ belongs to department $A_i$ this term and will belong to department $B_i$ next term.

For each of departments $1, 2, \dots, M$, find the number of members next term minus the number of members this term.

### Constraints

-   $1 \leq N \leq 100$
-   $1 \leq M \leq 100$
-   $1 \leq A_i \leq M$
-   $1 \leq B_i \leq M$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $M$
$A_1$ $B_1$
$A_2$ $B_2$
$\vdots$
$A_N$ $B_N$
```

### Output

Output $M$ lines. The $j$\-th line should contain the answer for department $j$.

### Sample Input 1

```text
5 4
1 2
2 1
3 1
2 2
2 4
```

### Sample Output 1

```text
1
-1
-1
1
```

-   For department $1$: this term, one employee (employee number $1$) belongs; next term, two employees (employee numbers $2, 3$) belong.
-   For department $2$: this term, three employees (employee numbers $2, 4, 5$) belong; next term, two employees (employee numbers $1, 4$) belong.
-   For department $3$: this term, one employee (employee number $3$) belongs; next term, no one belongs.
-   For department $4$: this term, no one belongs; next term, one employee (employee number $5$) belongs.

### Sample Input 2

```text
10 5
3 2
3 4
1 2
2 2
4 4
3 1
3 4
4 2
3 3
3 2
```

### Sample Output 2

```text
0
4
-5
1
0
```
