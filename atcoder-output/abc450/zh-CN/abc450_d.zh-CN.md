# D - Minimize Range

分值：$400$ 分

---

### Problem Statement

You are given a sequence $A$ of $N$ positive integers and a positive integer $K$.  
You can perform the following operation on the sequence $A$ any number of times.

给定一个由 $N$ 个正整数组成的序列 $A$，以及一个正整数 $K$。
你可以对序列 $A$ 执行任意次以下操作。

---

-   Choose an integer $i$ with $1 \leq i \leq N$, and add $K$ to $A_i$.

-   选择一个满足 $1 \leq i \leq N$ 的整数 $i$，将 $K$ 加到 $A_i$ 上。

---

Find the minimum possible value of $\max(A) - \min(A)$.

求 $\max(A) - \min(A)$ 的最小可能值。

---

### Constraints

-   $1 \leq N \leq 2 \times 10^5$
-   $1 \leq K \leq 10^9$
-   $1 \leq A_i \leq 10^9$
-   All input values are integers.

-   $1 \leq N \leq 2 \times 10^5$
-   $1 \leq K \leq 10^9$
-   $1 \leq A_i \leq 10^9$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入以如下格式从标准输入给出：

$N$ $K$  
$A_1$ $A_2$ $\dots$ $A_N$

---

### Output

Output the answer on a single line.

输出答案，占一行。

---

### Sample Input 1

```text
3 10
3 21 9
```

---

### Sample Output 1

```text
4
```

---

First, choosing $i=1$ makes the sequence $A=(13,21,9)$.  
Next, choosing $i=3$ makes the sequence $A=(13,21,19)$.  
Next, choosing $i=1$ makes the sequence $A=(23,21,19)$.  
At this point, $\max(A)-\min(A)=23-19=4$.  
It is impossible to make $\max(A)-\min(A)$ at most $3$, so the answer is $4$.

首先，选择 $i=1$，使得序列变为 $A=(13,21,9)$。
接下来，选择 $i=3$，使得序列变为 $A=(13,21,19)$。
然后，选择 $i=1$，使得序列变为 $A=(23,21,19)$。
此时，$\max(A)-\min(A)=23-19=4$。
无法使 $\max(A)-\min(A)$ 不超过 $3$，因此答案是 $4$。

---

### Sample Input 2

```text
5 6
4 100 5 10 450
```

---

### Sample Output 2

```text
2
```
