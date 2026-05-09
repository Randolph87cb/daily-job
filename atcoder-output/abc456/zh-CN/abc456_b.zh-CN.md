# B - 456

分值：$200$ 分

---

### Problem Statement

There are three dice, each with six faces.  
The $j$\-th face of the $i$\-th die has $A_{i,j}$ written on it.  
For each die, each face comes up with probability $\frac{1}{6}$.

有三个骰子，每个骰子有六个面。
第 $i$ 个骰子的第 $j$ 面上写着 $A_{i,j}$。
对于每个骰子，每个面朝上的概率为 $\frac{1}{6}$。

---

When these dice are rolled simultaneously, find the probability that the values $4,5,6$ each appear exactly once.

同时掷出这三个骰子时，求每个 $4,5,6$ 恰好出现一次的概率。

---

### Constraints

-   $A_{i,j}$ is an integer between $1$ and $6$, inclusive.

- $A_{i,j}$ 是介于 $1$ 和 $6$ 之间（含两端）的整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$A_{1,1}$ $A_{1,2}$ $A_{1,3}$ $A_{1,4}$ $A_{1,5}$ $A_{1,6}$  
$A_{2,1}$ $A_{2,2}$ $A_{2,3}$ $A_{2,4}$ $A_{2,5}$ $A_{2,6}$  
$A_{3,1}$ $A_{3,2}$ $A_{3,3}$ $A_{3,4}$ $A_{3,5}$ $A_{3,6}$

---

### Output

Output the answer. The answer is considered correct if the absolute or relative error from the true answer is at most $10^{-6}$.

输出答案。如果你的输出与正确答案的绝对误差或相对误差不超过 $10^{-6}$，则视为正确。

---

### Sample Input 1

```text
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
```

---

### Sample Output 1

```text
0.0277777778
```

---

The desired probability is $\frac{1}{36}$. An output such as `0.027778` is also accepted.

所求概率为 $\frac{1}{36}$。类似 `0.027778` 的输出也会被接受。

---

### Sample Input 2

```text
4 5 6 4 5 6
4 4 5 5 6 6
6 5 4 4 5 6
```

---

### Sample Output 2

```text
0.2222222222
```

---

The desired probability is $\frac{2}{9}$.

所求概率为 $\frac{2}{9}$。
