# G - Mode in the Subtree

Source: https://atcoder.jp/contests/abc454/tasks/abc454_g?lang=en

Score : $625$ points

### Problem Statement

You are given a rooted tree with $N$ vertices numbered $1$ through $N$. Vertex $1$ is the root, and the parent of vertex $i$ is vertex $p_i$ ($p_i \lt i$).  
Each vertex is colored: vertex $i$ is colored with color $c_i$ ($1 \leq c_i \leq N$).  
For each $v = 1, 2, \dots, N$, solve the following problem:

> Let $f_i$ be the number of vertices colored with color $i$ among the vertices in the subtree rooted at vertex $v$.
> 
> Find:
> 
> -   the maximum value $m$ among the values in the sequence $(f_1, f_2, \dots, f_N)$, and
> -   the number $k$ of positive integers $i$ not greater than $N$ such that $f_i = m$.

### Input/Output Format

The input and output for this problem follow a special format.

#### Input Format

From Standard Input, you are given the integer $N$ along with integers $\mathrm{seed}, M, F$ and $q_2, q_3, \dots, q_M$, $d_1, d_2, \dots, d_M$. Reconstruct $p_2, p_3, \dots, p_N$ and $c_1, c_2, \dots, c_N$ using the computation described by the following pseudocode. (Here, `2^31` means $2^{31}=2147483648$. Note that $\mathrm{state}$ is a variable, and that a $64$\-bit integer type is required for computing $\mathrm{state}$.)

```text
state = seed

for i=2 to N:
  if i <= M:
    p\[i\] = q\[i\]
  else:
    p\[i\] = (state mod (i-1)) + 1
    state = (state \* 1103515245 + 12345) mod 2^31

for i=1 to N:
  if i <= M:
    c\[i\] = d\[i\]
  else:
    c\[i\] = (state mod F) + 1
    state = (state \* 1103515245 + 12345) mod 2^31
```

#### Output Format

Let $m_i$ and $k_i$ denote $m$ and $k$ when $v=i$, respectively. Output this value:

$\left(\displaystyle \sum_{i=1}^N (m_i \oplus i)\times (k_i \oplus i)\right) \bmod 998244353$

Here, $\oplus$ denotes bitwise XOR. Beware of overflow during computation.

### Constraints

-   $2 \leq N \leq 2.5 \times 10^6$
-   $1 \leq p_i \lt i$
-   $1 \leq c_i \leq N$
-   $1 \leq \mathrm{seed} \lt 2^{31}$
-   $2 \leq M \leq \min(N, 10^5)$
-   $1 \leq F \leq N$
-   $1 \leq q_i \lt i$
-   $1 \leq d_i \leq N$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $\mathrm{seed}$ $M$ $F$
$q_2$ $q_3$ $\dots$ $q_M$
$d_1$ $d_2$ $\dots$ $d_M$
```

### Output

Output $\left(\displaystyle \sum_{i=1}^N (m_i \oplus i)\times (k_i \oplus i)\right) \bmod 998244353$.

### Sample Input 1

```text
4 454 4 2
1 2 2
1 2 2 3
```

### Sample Output 1

```text
29
```

-   $i=1$ : $m_1=2,k_1=1, (m_1 \oplus 1) \times (k_1 \oplus 1) = 0$
-   $i=2$ : $m_2=2,k_2=1, (m_2 \oplus 2) \times (k_2 \oplus 2) = 0$
-   $i=3$ : $m_3=1,k_3=1, (m_3 \oplus 3) \times (k_3 \oplus 3) = 4$
-   $i=4$ : $m_4=1,k_4=1, (m_4 \oplus 4) \times (k_4 \oplus 4) = 25$

Thus, output $0+0+4+25=29$.

### Sample Input 2

```text
6 123 2 2
1
1 2
```

### Sample Output 2

```text
101
```

The values of $p_i, c_i$ in this test case are as follows:

-   $p = (1, 2, 1, 2, 3)$
-   $c = (1, 2, 2, 1, 2, 1)$

### Sample Input 3

```text
15 1 4 5
1 2 3
5 3 1 3
```

### Sample Output 3

```text
1199
```

The values of $p_i, c_i$ in this test case are as follows:

-   $p = (1, 2, 3, 2, 1, 4, 7, 6, 5, 10, 1, 10, 2, 8)$
-   $c = (5, 3, 1, 3, 4, 2, 2, 2, 4, 2, 2, 5, 3, 5, 3)$
