# G - Copy Query

Source: https://atcoder.jp/contests/abc453/tasks/abc453_g?lang=en

Score : $600$ points

### Problem Statement

There are $N$ sequences of length $M$: $A_1,A_2,\dots,A_N$. Initially, all elements of all sequences are $0$.  
Hereafter, the $j$\-th element of sequence $A_i$ is denoted by $A_{i,j}$.

Process the following three types of queries in the given order, $Q$ queries in total.

-   Type $1$: Overwrite sequence $A_{X_i}$ with sequence $A_{Y_i}$. That is, for every integer $j$ ($1 \le j \le M$), change $A_{X_i,j}$ to $A_{Y_i,j}$.
-   Type $2$: Change the $Y_i$\-th element of sequence $A_{X_i}$, that is, $A_{X_i,Y_i}$, to $Z_i$.
-   Type $3$: For sequence $A_{X_i}$, output the sum of elements from the $L_i$\-th through the $R_i$\-th, that is, $A_{X_i,L_i}+A_{X_i,L_i+1}+\dots+A_{X_i,R_i}$.

### Constraints

-   $1 \le N,M \le 2 \times 10^5$
-   $1 \le Q \le 2 \times 10^5$
-   Type $1$ queries satisfy the following constraints:
    -   $1 \le X_i,Y_i \le N$
-   Type $2$ queries satisfy the following constraints:
    -   $1 \le X_i \le N$
    -   $1 \le Y_i \le M$
    -   $0 \le Z_i \le 10^9$
-   Type $3$ queries satisfy the following constraints:
    -   $1 \le X_i \le N$
    -   $1 \le L_i \le R_i \le M$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $M$ $Q$
${\rm Query}_1$
${\rm Query}_2$
$\vdots$
${\rm Query}_Q$
```

Here, ${\rm Query}_i$ represents the $i$\-th query.

A type $1$ query is given in the following format:

```text
1 $X_i$ $Y_i$
```

A type $2$ query is given in the following format:

```text
2 $X_i$ $Y_i$ $Z_i$
```

A type $3$ query is given in the following format:

```text
3 $X_i$ $L_i$ $R_i$
```

### Output

For each type $3$ query, output the answer to that query. If there are no type $3$ queries, the output should be empty.

### Sample Input 1

```text
4 5 10
2 2 1 2
2 2 2 7
2 2 4 8
1 1 2
2 2 3 1
1 3 2
2 3 2 10
3 1 2 4
3 2 1 4
3 3 2 2
```

### Sample Output 1

```text
15
18
10
```

In this input, prepare four sequences of length $5$.

-   In the $1$st query, set $A_{2,1}=2$. At this point, $A_2=(2,0,0,0,0)$.
-   In the $2$nd query, set $A_{2,2}=7$. At this point, $A_2=(2,7,0,0,0)$.
-   In the $3$rd query, set $A_{2,4}=8$. At this point, $A_2=(2,7,0,8,0)$.
-   In the $4$th query, overwrite sequence $A_1$ with sequence $A_2$. At this point, $A_1=(2,7,0,8,0)$.
-   In the $5$th query, set $A_{2,3}=1$. At this point, $A_2=(2,7,1,8,0)$.
-   In the $6$th query, overwrite sequence $A_3$ with sequence $A_2$. At this point, $A_3=(2,7,1,8,0)$.
-   In the $7$th query, set $A_{3,2}=10$. At this point, $A_3=(2,10,1,8,0)$.
-   In the $8$th query, output $A_{1,2}+A_{1,3}+A_{1,4}=7+0+8=15$.
-   In the $9$th query, output $A_{2,1}+A_{2,2}+A_{2,3}+A_{2,4}=2+7+1+8=18$.
-   In the $10$th query, output $A_{3,2}=10$.
