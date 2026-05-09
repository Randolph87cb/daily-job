# C - Greedy Customers 2

Source: https://atcoder.jp/contests/arc217/tasks/arc217_c?lang=en

Score : $700$ points

### Problem Statement

AtCoder Store has $N$ items. The $i$\-th item costs $A_i$ yen.

$N$ people visit the store one by one. Each person has $C$ yen and performs the following procedure.

-   Choose an integer $x$ uniformly at random between $1$ and $C$, inclusive, as the budget for shopping.
-   If there is an item remaining in the store that costs at most $x$ yen, purchase one of the most expensive ones among them. Otherwise, leave the store without purchasing anything.

As the owner of the store, you want to know how many items will be sold. For $k=0,1,2,\ldots,N$, find the probability, modulo $998244353$, that exactly $k$ items are sold in the end.

You are given $T$ test cases; solve each of them.

**Definition of probability \ \text{mod}\ 998244353**

It can be proved that the probabilities to be found are always rational numbers. Moreover, under the constraints of this problem, when each such rational number is expressed as an irreducible fraction $\displaystyle \frac{P}{Q}$, it can be proved that $Q \neq 0 \bmod 998244353$. Thus, there is a unique integer $R$ satisfying $R \times Q \equiv P \bmod 998244353, 0 \leq R \lt 998244353$. Find this $R$.

### Constraints

-   $1\le T$
-   $1\le N$
-   The sum of $N$ over all test cases is at most $100$.
-   $1\le A_i \le C < 998244353$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\text{case}_1$
$\text{case}_2$
$\vdots$
$\text{case}_T$
```

Each test case is given in the following format:

```text
$N$ $C$
$A_1$ $A_2$ $\ldots$ $A_N$
```

### Output

Output the answers for the test cases in order, separated by newlines.

For each test case, output the answers for $k=0,1,\ldots,N$ in order, separated by spaces.

### Sample Input 1

```text
4
2 3
1 3
3 17
9 9 8
5 2025
1 1 1 1 1
6 1000
544 105 450 715 479 992
```

### Sample Output 1

```text
0 776412275 221832079
465698363 588015298 487439081 455335965
0 0 0 0 0 1
366062443 766314649 169448288 553531286 643499511 890090646 604030590
```

Consider the first test case.

For example, the procedure for each person proceeds as follows.

-   Person $1$: Chooses $x=2$. The most expensive item that costs at most $2$ yen is the first item, so they purchase the first item.
-   Person $2$: Chooses $x=1$. There are no items costing at most $1$ yen, so they leave without purchasing anything.

In this case, exactly one item is sold in the end.

The probabilities that exactly $0,1,2$ items are sold are $\displaystyle 0, \frac49,\frac59$, respectively.
