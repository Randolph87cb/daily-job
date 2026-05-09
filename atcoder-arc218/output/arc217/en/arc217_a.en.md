# A - Min of Sum of XOR

Source: https://atcoder.jp/contests/arc217/tasks/arc217_a?lang=en

Score : $500$ points

### Problem Statement

You are given a positive integer $N$.

Find one permutation $P=(P_1,P_2,\ldots,P_N)$ of $(1,2,\ldots,N)$ that minimizes $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$.

Here, $\displaystyle \bigoplus_{1\le j\le i} P_j$ is defined as the bitwise $\mathrm{XOR}$ of $P_1,P_2,\ldots,P_i$.

You are given $T$ test cases; solve each of them.

**What is bitwise \mathrm{XOR}?**

The bitwise $\mathrm{XOR}$ of non-negative integers $A$ and $B$, $A \oplus B$, is defined as follows.

-   In the binary representation of $A \oplus B$, the digit at the $2^k$ ($k \geq 0$) place is $1$ if exactly one of the digits at the $2^k$ place in the binary representations of $A$ and $B$ is $1$, and $0$ otherwise.

For example, $3 \oplus 5 = 6$ (in binary: $011 \oplus 101 = 110$).  
In general, the bitwise $\mathrm{XOR}$ of $k$ non-negative integers $p_1, p_2, p_3, \dots, p_k$ is defined as $(\dots ((p_1 \oplus p_2) \oplus p_3) \oplus \dots \oplus p_k)$, and it can be proved that this does not depend on the order of $p_1, p_2, p_3, \dots, p_k$.

### Constraints

-   $1\le T\le 10^3$
-   $1\le N$
-   The sum of $N$ over all test cases is at most $2\times 10^5$.
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
$N$
```

### Output

Output the answers for the test cases in order, separated by newlines.

For each test case, output a permutation $P=(P_1,P_2,\ldots,P_N)$ of $(1,2,\ldots,N)$ that minimizes $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$, separated by spaces.

If there are multiple permutations $P$ that achieve the minimum, any of them will be accepted.

### Sample Input 1

```text
3
3
1
7
```

### Sample Output 1

```text
1 3 2
1
4 5 3 2 6 7 1
```

Consider the first test case.

If $P=(1,3,2)$, then $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j=1 + (1 \oplus 3) + (1 \oplus 3 \oplus 2) = 1+2+0=3$.

The value of $\displaystyle \sum_{i=1}^N \bigoplus_{1\le j\le i} P_j$ cannot be made less than $3$, so outputting $P=(1,3,2)$ is correct.

Outputting $P=(2,3,1)$ is also correct.
