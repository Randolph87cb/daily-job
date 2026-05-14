# G - Random Subtraction

分值：$575$ 分

---

### Problem Statement

You are given a sequence $A$ of $N$ non-negative integers.  
Repeat the following operation until $A$ has exactly one element.

给定一个由 $N$ 个非负整数组成的序列 $A$。
重复执行以下操作，直到 $A$ 中恰好剩下一个元素。

---

-   Choose two distinct integers $i$ and $j$ satisfying $1 \leq i, j \leq |A|$ uniformly at random.
-   Let $a$ and $b$ be $A_i$ and $A_j$, respectively.
-   Remove the $i$\-th and $j$\-th elements from $A$.
-   Append $a - b$ to the end of $A$.

-   均匀随机地选择两个满足 $1 \leq i, j \leq |A|$ 的不同整数 $i$ 和 $j$。
-   令 $a$ 和 $b$ 分别为 $A_i$ 和 $A_j$。
-   从 $A$ 中移除第 $i$ 个和第 $j$ 个元素。
-   将 $a - b$ 追加到 $A$ 的末尾。

---

Let $x$ be the only element of $A$ at the end. Find the expected value of $x^2$, modulo $998244353$.

令 $x$ 为最终 $A$ 中剩下的唯一元素。求 $x^2$ 的期望值，对 $998244353$ 取模。

---

**Definition of expected value modulo 998244353**

**期望值对 998244353 取模的定义**

---

It can be proved that the expected value to be found is always a rational number. It can also be proved that under the constraints of this problem, when expressed as an irreducible fraction $\frac{P}{Q}$, we have $Q \neq 0 \pmod{998244353}$. Thus, there is a unique integer $R$ satisfying $R \times Q \equiv P \pmod{998244353}, 0 \leq R &lt 998244353$. Find this $R$.

可以证明所求的期望值总是一个有理数。同时可以证明，在本题的约束条件下，将该期望值表示为既约分数 $\frac{P}{Q}$ 时，满足 $Q \neq 0 \pmod{998244353}$。因此存在唯一的整数 $R$ 满足 $R \times Q \equiv P \pmod{998244353}, 0 \leq R &lt 998244353$，请求出这个 $R$。

---

### Constraints

-   $1 \leq N \leq 2 \times 10^5$
-   $0 \leq A_i \leq 998244352$
-   All input values are integers.

-   $1 \leq N \leq 2 \times 10^5$
-   $0 \leq A_i \leq 998244352$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$A_1$ $A_2$ $\dots$ $A_N$

---

### Output

Output the answer on a single line.

将答案输出在一行中。

---

### Sample Input 1

```text
3
4 5 0
```

---

### Sample Output 1

```text
665496263
```

---

First, choosing $(i, j) = (3, 1)$ makes the sequence $(5, -4)$.  
Next, choosing $(i, j) = (1, 2)$ makes the sequence $(9)$.  
$x^2$ equals $81$ with probability $\frac{1}{3}$ and $1$ with probability $\frac{2}{3}$, so the expected value is $\frac{83}{3}$.

首先，选择 $(i, j) = (3, 1)$ 后序列变为 $(5, -4)$。
接下来，选择 $(i, j) = (1, 2)$ 后序列变为 $(9)$。
$x^2$ 有 $\frac{1}{3}$ 的概率等于 $81$，有 $\frac{2}{3}$ 的概率等于 $1$，因此期望值为 $\frac{83}{3}$。

---

### Sample Input 2

```text
5
450 2026 3 21 100
```

---

### Sample Output 2

```text
669406799
```
