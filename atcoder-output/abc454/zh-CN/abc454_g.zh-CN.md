# G - Mode in the Subtree

分值：$625$ 分

---

### Problem Statement

You are given a rooted tree with $N$ vertices numbered $1$ through $N$. Vertex $1$ is the root, and the parent of vertex $i$ is vertex $p_i$ ($p_i \lt i$).  
Each vertex is colored: vertex $i$ is colored with color $c_i$ ($1 \leq c_i \leq N$).  
For each $v = 1, 2, \dots, N$, solve the following problem:

给定一棵包含 $N$ 个顶点的有根树，顶点编号为 $1$ 到 $N$。顶点 $1$ 是根，且对于 $p_i \lt i$，顶点 $i$ 的父节点为顶点 $p_i$。
每个顶点都有颜色：顶点 $i$ 的颜色为 $c_i$（$1 \leq c_i \leq N$）。
对每个 $v = 1, 2, \dots, N$，求解以下问题：

---

> Let $f_i$ be the number of vertices colored with color $i$ among the vertices in the subtree rooted at vertex $v$.
> 
> Find:
> 
> -   the maximum value $m$ among the values in the sequence $(f_1, f_2, \dots, f_N)$, and
> -   the number $k$ of positive integers $i$ not greater than $N$ such that $f_i = m$.

> 定义 $f_i$ 为以顶点 $v$ 为根的子树中，颜色为 $i$ 的顶点数量。
> 
> 求：
> 
> - 序列 $(f_1, f_2, \dots, f_N)$ 中的最大值 $m$，以及
> - 不超过 $N$ 且满足 $f_i = m$ 的正整数 $i$ 的个数 $k$。

---

### Input/Output Format

The input and output for this problem follow a special format.

本题的输入和输出采用特殊格式。

---

#### Input Format

From Standard Input, you are given the integer $N$ along with integers $\mathrm{seed}, M, F$ and $q_2, q_3, \dots, q_M$, $d_1, d_2, \dots, d_M$. Reconstruct $p_2, p_3, \dots, p_N$ and $c_1, c_2, \dots, c_N$ using the computation described by the following pseudocode. (Here, `2^31` means $2^{31}=2147483648$. Note that $\mathrm{state}$ is a variable, and that a $64$\-bit integer type is required for computing $\mathrm{state}$.)

从标准输入读取整数 $N$，以及整数 $\mathrm{seed}, M, F$ 和 $q_2, q_3, \dots, q_M$（$d_1, d_2, \dots, d_M$）。按照以下伪代码描述的计算过程重构 $p_2, p_3, \dots, p_N$ 和 $c_1, c_2, \dots, c_N$。（此处 `2^31` 表示 $2^{31}=2147483648$。注意 $\mathrm{state}$ 是变量，计算 $\mathrm{state}$ 时需要使用 $64$ 位整数类型。）

---

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

---

#### Output Format

Let $m_i$ and $k_i$ denote $m$ and $k$ when $v=i$, respectively. Output this value:

设 $m_i$ 和 $k_i$ 分别为当 $v=i$ 时的 $m$ 和 $k$。输出以下值：

---

$\left(\displaystyle \sum_{i=1}^N (m_i \oplus i)\times (k_i \oplus i)\right) \bmod 998244353$

$\left(\displaystyle \sum_{i=1}^N (m_i \oplus i)\times (k_i \oplus i)\right) \bmod 998244353$

---

Here, $\oplus$ denotes bitwise XOR. Beware of overflow during computation.

此处 $\oplus$ 表示按位异或。计算过程中请注意溢出问题。

---

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

- $2 \leq N \leq 2.5 \times 10^6$
- $1 \leq p_i \lt i$
- $1 \leq c_i \leq N$
- $1 \leq \mathrm{seed} \lt 2^{31}$
- $2 \leq M \leq \min(N, 10^5)$
- $1 \leq F \leq N$
- $1 \leq q_i \lt i$
- $1 \leq d_i \leq N$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $\mathrm{seed}$ $M$ $F$  
$q_2$ $q_3$ $\dots$ $q_M$  
$d_1$ $d_2$ $\dots$ $d_M$

---

### Output

Output $\left(\displaystyle \sum_{i=1}^N (m_i \oplus i)\times (k_i \oplus i)\right) \bmod 998244353$.

输出 $\left(\displaystyle \sum_{i=1}^N (m_i \oplus i)\times (k_i \oplus i)\right) \bmod 998244353$。

---

### Sample Input 1

```text
4 454 4 2
1 2 2
1 2 2 3
```

---

### Sample Output 1

```text
29
```

---

-   $i=1$ : $m_1=2,k_1=1, (m_1 \oplus 1) \times (k_1 \oplus 1) = 0$
-   $i=2$ : $m_2=2,k_2=1, (m_2 \oplus 2) \times (k_2 \oplus 2) = 0$
-   $i=3$ : $m_3=1,k_3=1, (m_3 \oplus 3) \times (k_3 \oplus 3) = 4$
-   $i=4$ : $m_4=1,k_4=1, (m_4 \oplus 4) \times (k_4 \oplus 4) = 25$

- $i=1$ : $m_1=2,k_1=1, (m_1 \oplus 1) \times (k_1 \oplus 1) = 0$
- $i=2$ : $m_2=2,k_2=1, (m_2 \oplus 2) \times (k_2 \oplus 2) = 0$
- $i=3$ : $m_3=1,k_3=1, (m_3 \oplus 3) \times (k_3 \oplus 3) = 4$
- $i=4$ : $m_4=1,k_4=1, (m_4 \oplus 4) \times (k_4 \oplus 4) = 25$

---

Thus, output $0+0+4+25=29$.

因此，输出 $0+0+4+25=29$。

---

### Sample Input 2

```text
6 123 2 2
1
1 2
```

---

### Sample Output 2

```text
101
```

---

The values of $p_i, c_i$ in this test case are as follows:

该测试用例中 $p_i, c_i$ 的值如下：

---

-   $p = (1, 2, 1, 2, 3)$
-   $c = (1, 2, 2, 1, 2, 1)$

- $p = (1, 2, 1, 2, 3)$
- $c = (1, 2, 2, 1, 2, 1)$

---

### Sample Input 3

```text
15 1 4 5
1 2 3
5 3 1 3
```

---

### Sample Output 3

```text
1199
```

---

The values of $p_i, c_i$ in this test case are as follows:

该测试用例中 $p_i, c_i$ 的值如下：

---

-   $p = (1, 2, 3, 2, 1, 4, 7, 6, 5, 10, 1, 10, 2, 8)$
-   $c = (5, 3, 1, 3, 4, 2, 2, 2, 4, 2, 2, 5, 3, 5, 3)$

- $p = (1, 2, 3, 2, 1, 4, 7, 6, 5, 10, 1, 10, 2, 8)$
- $c = (5, 3, 1, 3, 4, 2, 2, 2, 4, 2, 2, 5, 3, 5, 3)$
