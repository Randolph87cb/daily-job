# D - Greedy Customer

Source: https://atcoder.jp/contests/arc217/tasks/arc217_d?lang=en

Score : $700$ points

### Problem Statement

You are given positive integers $N,M$ and a sequence of positive integers $A=(A_1,A_2,\ldots,A_N)$ of length $N$.

For a positive integer $k$, define $f(k)$ as the answer to the following problem.

> Takahashi has $k$ yen. AtCoder Store has $N$ items, and the $i$\-th item costs $A_i$ yen.
> 
> He performs the following action for $i=1,2,\ldots,N$ in order.
> 
> -   If the amount of money he currently has is at least $A_i$ yen, he purchases the $i$\-th item.
> 
> Find the total price of the items he purchased.

Find $\displaystyle \bigoplus_{1\le k\le M} (k\times f(k))$. Here, $\displaystyle \bigoplus_{1\le k\le M} (k\times f(k))$ is defined as the bitwise $\mathrm{XOR}$ of $1\times f(1), 2\times f(2), \ldots, M\times f(M)$.

You are given $T$ test cases; solve each of them.

**What is bitwise \mathrm{XOR}?**

The bitwise $\mathrm{XOR}$ of non-negative integers $A$ and $B$, $A \oplus B$, is defined as follows.

-   In the binary representation of $A \oplus B$, the digit at the $2^k$ ($k \geq 0$) place is $1$ if exactly one of the digits at the $2^k$ place in the binary representations of $A$ and $B$ is $1$, and $0$ otherwise.

For example, $3 \oplus 5 = 6$ (in binary: $011 \oplus 101 = 110$).  
In general, the bitwise $\mathrm{XOR}$ of $k$ non-negative integers $p_1, p_2, p_3, \dots, p_k$ is defined as $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$, and it can be proved that this does not depend on the order of $p_1, p_2, p_3, \dots, p_k$.

### Constraints

-   $1\le T \le 10$
-   $1\le N,M$
-   The sum of $N$ over all test cases is at most $5\times 10^5$.
-   The sum of $M$ over all test cases is at most $5\times 10^7$.
-   $1\le A_i \le M$
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
$N$ $M$
$A_1$ $A_2$ $\ldots$ $A_N$
```

### Output

Output the answers for the test cases in order, separated by newlines.

### Sample Input 1

```text
3
3 6
2 3 1
5 10
3 1 4 1 5
7 12
4 2 3 4 2 3 3
```

### Sample Output 1

```text
61
115
190
```

Consider the first test case.

For example, when Takahashi's initial amount of money is $3$ yen, he acts as follows.

-   For $i=1$: he has $3$ yen, which is at least $2$ yen, so he purchases the first item.
-   For $i=2$: he has $1$ yen, which is less than $3$ yen, so he does not purchase the second item.
-   For $i=3$: he has $1$ yen, which is at least $1$ yen, so he purchases the third item.

From this, we get $f(3)=2+1=3$.

The values of $f(1),f(2),f(3),f(4),f(5),f(6)$ are $1,2,3,3,5,6$, respectively. Thus, the answer is the bitwise $\mathrm{XOR}$ of $1,4,9,12,25,36$, which is $61$.
