# A - 455

分值：$100$ 分

---

### Problem Statement

You are given integers $A, B, C$. If $A \neq B$ and $B = C$, output `Yes`; otherwise, output `No`.

给定整数 $A, B, C$。如果 $A \neq B$ 且 $B = C$，输出 `Yes`；否则输出 `No`。

---

### Constraints

-   $1 \leq A, B, C \leq 9$
-   All input values are integers.

- $1 \leq A, B, C \leq 9$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$A$ $B$ $C$

---

### Output

Output `Yes` or `No` according to the instructions in the problem statement.

根据题目说明输出 `Yes` 或 `No`。

---

### Sample Input 1

```text
4 5 5
```

---

### Sample Output 1

```text
Yes
```

---

Since $4 \neq 5$ and $5 = 5$, output `Yes`.

因为 $4 \neq 5$ 且 $5 = 5$，所以输出 `Yes`。

---

### Sample Input 2

```text
1 3 7
```

---

### Sample Output 2

```text
No
```

---

Although $1 \neq 3$, we don't have $3 = 7$, so output `No`.

虽然 $1 \neq 3$，但不满足 $3 = 7$，因此输出 `No`。

---

### Sample Input 3

```text
6 6 6
```

---

### Sample Output 3

```text
No
```
