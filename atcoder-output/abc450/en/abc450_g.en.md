# G - Random Subtraction

Source: https://atcoder.jp/contests/abc450/tasks/abc450_g?lang=en

Score : $575$ points

### Problem Statement

You are given a sequence $A$ of $N$ non-negative integers.  
Repeat the following operation until $A$ has exactly one element.

-   Choose two distinct integers $i$ and $j$ satisfying $1 \leq i, j \leq |A|$ uniformly at random.
-   Let $a$ and $b$ be $A_i$ and $A_j$, respectively.
-   Remove the $i$\-th and $j$\-th elements from $A$.
-   Append $a - b$ to the end of $A$.

Let $x$ be the only element of $A$ at the end. Find the expected value of $x^2$, modulo $998244353$.

**Definition of expected value modulo 998244353**

It can be proved that the expected value to be found is always a rational number. It can also be proved that under the constraints of this problem, when expressed as an irreducible fraction $\frac{P}{Q}$, we have $Q \neq 0 \pmod{998244353}$. Thus, there is a unique integer $R$ satisfying $R \times Q \equiv P \pmod{998244353}, 0 \leq R &lt 998244353$. Find this $R$.

### Constraints

-   $1 \leq N \leq 2 \times 10^5$
-   $0 \leq A_i \leq 998244352$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$A_1$ $A_2$ $\dots$ $A_N$
```

### Output

Output the answer on a single line.

### Sample Input 1

```text
3
4 5 0
```

### Sample Output 1

```text
665496263
```

First, choosing $(i, j) = (3, 1)$ makes the sequence $(5, -4)$.  
Next, choosing $(i, j) = (1, 2)$ makes the sequence $(9)$.  
$x^2$ equals $81$ with probability $\frac{1}{3}$ and $1$ with probability $\frac{2}{3}$, so the expected value is $\frac{83}{3}$.

### Sample Input 2

```text
5
450 2026 3 21 100
```

### Sample Output 2

```text
669406799
```
