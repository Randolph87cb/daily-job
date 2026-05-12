# F - Merge Slimes 2

Source: https://atcoder.jp/contests/abc455/tasks/abc455_f?lang=en

Score : $525$ points

### Problem Statement

There is a sequence $A$ of $N$ non-negative integers, all initially $0$. Process $Q$ queries given in order.  
For the $q$\-th query, you are given integers $l_q, r_q$ satisfying $1 \leq l_q \leq r_q \leq N$ and a positive integer $a_q$. Perform the following in order:

-   Add $a_q$ to each of $A_{l_q}, A_{{l_q}+1}, \dots, A_{r_q}$.
-   Then, letting $M=r_q-l_q+1$ and $B=(B_1,B_2,\dots,B_M)=(A_{l_q}, A_{l_q+1}, \dots, A_{r_q})$, find the answer to the following problem:

> There are $M$ slimes $1,2,\dots,M$, where the $m$\-th slime has weight $B_m$.  
> Repeat the operation of choosing two slimes and merging them $M-1$ times.  
> When slimes of weights $x$ and $y$ are merged, a slime of weight $x+y$ appears and the original two slimes disappear. This incurs a cost of $x \times y$.  
> Find, modulo $998244353$, the minimum possible total cost of the $M-1$ operations.

Note that the changes made on $A$ in each query carry over to subsequent queries.

### Constraints

-   $1 \leq N \leq 10^5$
-   $1 \leq Q \leq 10^5$
-   $1 \leq l_q \leq r_q \leq N$
-   $1 \leq a_q \leq 10^9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $Q$
$l_1$ $r_1$ $a_1$
$l_2$ $r_2$ $a_2$
$\vdots$
$l_Q$ $r_Q$ $a_Q$
```

### Output

Output the answers over $Q$ lines in total. The $q$\-th line should contain the answer to the $q$\-th query.

### Sample Input 1

```text
5 4
1 3 22
3 4 13
5 5 455
1 5 1000000000
```

### Sample Output 1

```text
1452
455
0
21421644
```

After the first query, $A=(22,22,22,0,0)$ and $B=(22,22,22)$. Merging the first and third slimes first incurs a cost of $22 \times 22=484$. Then merging the remaining two slimes incurs a cost of $22 \times 44=968$. The total cost is $484+968=1452$. Moreover, the total cost cannot be made smaller than this.  
After the second query, $A=(22,22,35,13,0)$ and $B=(35,13)$. The answer is $35 \times 13 = 455$.
