# A - Many Sets

分值：$400$ 分

---

### Problem Statement

You are given $N$ sequences of positive integers, each of length $M$. The $i$\-th sequence is $A_i=(A_{i,1},A_{i,2},\dots,A_{i,M})$.

给定 $N$ 个由正整数构成的序列，每个序列的长度均为 $M$。第 $i$ 个序列是 $A_i=(A_{i,1},A_{i,2},\dots,A_{i,M})$。

---

There are $M^N$ ways to choose one element from each of these $N$ sequences. Find the sum, modulo $998244353$, of "the number of distinct integers among the chosen elements" over all such ways.

从这 $N$ 个序列中各选取一个元素，共有 $M^N$ 种选取方式。对所有这些选取方式，求「所选元素中不同整数的个数」的总和，结果对 $998244353$ 取模。

---

### Constraints

-   $1 \le N,M \le 500$
-   $1 \le A_{i,j} \le NM$
-   All input values are integers.

- $1 \le N,M \le 500$
- $1 \le A_{i,j} \le NM$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $M$  
$A_{1,1}$ $A_{1,2}$ $\dots$ $A_{1,M}$  
$A_{2,1}$ $A_{2,2}$ $\dots$ $A_{2,M}$  
$\vdots$  
$A_{N,1}$ $A_{N,2}$ $\dots$ $A_{N,M}$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
2 2
1 3
2 3
```

---

### Sample Output 1

```text
7
```

---

For example, if $A_{1,1}$ and $A_{2,1}$ are chosen, there are two distinct integers among the chosen elements: $1$ and $2$.

例如，若选取 $A_{1,1}$ 和 $A_{2,1}$，则所选元素包含两个不同整数：$1$ 和 $2$。

---

The number of distinct integers is $1$ only when $A_{1,2}$ and $A_{2,2}$ are chosen, and it is $2$ in the other three cases, so the answer is $7$.

只有当选出 $A_{1,2}$ 和 $A_{2,2}$ 时，不同整数的个数是 $1$，其余三种情况均为 $2$，因此答案是 $7$。

---

### Sample Input 2

```text
2 2
1 1
1 2
```

---

### Sample Output 2

```text
6
```

---

### Sample Input 3

```text
3 5
3 1 3 4 2
5 2 1 2 3
4 6 2 5 6
```

---

### Sample Output 3

```text
327
```
