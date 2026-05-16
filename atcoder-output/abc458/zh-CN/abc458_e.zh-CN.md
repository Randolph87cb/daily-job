# E - Count 123

分值：$450$ 分

---

### Problem Statement

Find the number, modulo $998244353$, of sequences $A = (a_1, \cdots, a_{X_1 + X_2 + X_3})$ of length $X_1+X_2+X_3$ that satisfy all of the following conditions.

求满足以下全部条件、长度为 $X_1+X_2+X_3$ 的序列 $A = (a_1, \cdots, a_{X_1 + X_2 + X_3})$ 的数量，答案对 $998244353$ 取模。

---

-   $A$ contains exactly $X_1$ copies of $1$, exactly $X_2$ copies of $2$, and exactly $X_3$ copies of $3$.
-   The absolute difference between adjacent elements is at most $1$. That is, for every integer $i$ satisfying $1 \leq i \leq X_1+X_2+X_3-1$, we have $|a_{i+1} - a_i| \leq 1$.

-   $A$ 中恰好包含 $X_1$ 个 $1$、$X_2$ 个 $2$，以及 $X_3$ 个 $3$。
-   相邻元素的绝对值之差不超过 $1$。即，对于所有满足 $1 \leq i \leq X_1+X_2+X_3-1$ 的整数 $i$，都有 $|a_{i+1} - a_i| \leq 1$。

---

### Constraints

-   $1 \leq X_1, X_2, X_3 \leq 10^6$
-   All input values are integers.

-   $1 \leq X_1, X_2, X_3 \leq 10^6$
-   所有输入值都是整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$X_1$ $X_2$ $X_3$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
2 2 1
```

---

### Sample Output 1

```text
9
```

---

The sequences satisfying the conditions are the following nine:

满足条件的序列共有以下 9 个：

---

-   $(1, 1, 2, 2, 3)$
-   $(1, 1, 2, 3, 2)$
-   $(1, 2, 1, 2, 3)$
-   $(1, 2, 3, 2, 1)$
-   $(2, 1, 1, 2, 3)$
-   $(2, 3, 2, 1, 1)$
-   $(3, 2, 1, 1, 2)$
-   $(3, 2, 1, 2, 1)$
-   $(3, 2, 2, 1, 1)$

---

### Sample Input 2

```text
5 3 4
```

---

### Sample Output 2

```text
204
```

---

### Sample Input 3

```text
998244 998353 998107
```

---

### Sample Output 3

```text
701926019
```
