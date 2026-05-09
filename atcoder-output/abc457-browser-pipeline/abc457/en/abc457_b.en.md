# B - Arrays

Source: https://atcoder.jp/contests/abc457/tasks/abc457_b?lang=en

Score : $200$ points

### Problem Statement

You are given $N$ sequences $A_1, A_2, \ldots, A_N$.

The length of sequence $A_i$ is $L_i$, and $A_i = (A_{i,1}, A_{i,2}, \ldots, A_{i,L_i})$.

After that, integers $X$ and $Y$ are given. Output the value of $A_{X,Y}$.

### Constraints

-   $1 \le N \le 2 \times 10^5$
-   $1 \le L_i$
-   The sum of $L_i$ is at most $2 \times 10^5$.
-   $1 \le A_{i,j} \le 1000$
-   $1 \le X \le N$
-   $1 \le Y \le L_X$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$L_1$ $A_{1,1}$ $A_{1,2}$ $\ldots$ $A_{1,L_1}$
$L_2$ $A_{2,1}$ $A_{2,2}$ $\ldots$ $A_{2,L_2}$
$\vdots$
$L_N$ $A_{N,1}$ $A_{N,2}$ $\ldots$ $A_{N,L_N}$
$X$ $Y$
```

### Output

Output the value of $A_{X,Y}$.

### Sample Input 1

```text
3
3 10 20 30
1 7
4 5 6 7 8
3 4
```

### Sample Output 1

```text
8
```

We have $(A_1, A_2, A_3) = ((10,20,30), (7), (5,6, 7,8))$.  
Since $A_3 = (5, 6, 7, 8)$ and $A_{3,4} = 8$, output $8$.

### Sample Input 2

```text
4
2 9 1
3 8 2 6
1 5
2 4 3
2 2
```

### Sample Output 2

```text
2
```

Since $A_2 = (8, 2, 6)$, we have $A_{2,2} = 2$.

### Sample Input 3

```text
1
5 100 200 300 400 500
1 5
```

### Sample Output 3

```text
500
```
