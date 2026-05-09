# A - Array

分值：$100$ 分

---

### Problem Statement

You are given a sequence $A = (A_1, A_2, \cdots , A_N)$ of length $N$.

给定一个长度为$N$的序列$A = (A_1, A_2, \cdots , A_N)$。

---

After that, an integer $X$ between $1$ and $N$, inclusive, is given.

接下来给出一个整数$X$，其取值范围是$1$到$N$（含两端）。

---

Output the value of $A_X$.

输出$A_X$的值。

---

### Constraints

-   $1 \le X \le N \le 100$
-   $1 \le A_i \le 100$
-   All input values are integers.

-   $1 \le X \le N \le 100$
-   $1 \le A_i \le 100$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$A_1$ $A_2$ $\ldots$ $A_N$  
$X$

---

### Output

Output the value of $A_X$.

输出$A_X$的值。

---

### Sample Input 1

```text
5
1 2 3 4 5
3
```

---

### Sample Output 1

```text
3
```

---

We have $(A_1, A_2, A_3, A_4 , A_5) = (1, 2, 3, 4, 5)$. Since $A_3 = 3$, output $3$.

我们有$(A_1, A_2, A_3, A_4 , A_5) = (1, 2, 3, 4, 5)$。由于$A_3 = 3$，输出$3$。

---

### Sample Input 2

```text
10
6 6 9 6 10 5 7 2 8 2
4
```

---

### Sample Output 2

```text
6
```

---

### Sample Input 3

```text
10
4 4 4 3 4 2 1 1 2 1
10
```

---

### Sample Output 3

```text
1
```
