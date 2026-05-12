# A - 455

Source: https://atcoder.jp/contests/abc455/tasks/abc455_a?lang=en

Score : $100100100$ points

### Problem Statement

You are given integers $A,B,CA, B, CA,B,C$. If $A≠BA \neq BA=B$ and $B=CB = CB=C$, output `Yes`; otherwise, output `No`.

### Constraints

-   $1≤A,B,C≤91 \leq A, B, C \leq 91≤A,B,C≤9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$AAA$ $BBB$ $CCC$
```

### Output

Output `Yes` or `No` according to the instructions in the problem statement.

### Sample Input 1

```text
4 5 5
```

### Sample Output 1

```text
Yes
```

Since $4≠54 \neq 54=5$ and $5=55 = 55=5$, output `Yes`.

### Sample Input 2

```text
1 3 7
```

### Sample Output 2

```text
No
```

Although $1≠31 \neq 31=3$, we don't have $3=73 = 73=7$, so output `No`.

### Sample Input 3

```text
6 6 6
```

### Sample Output 3

```text
No
```
