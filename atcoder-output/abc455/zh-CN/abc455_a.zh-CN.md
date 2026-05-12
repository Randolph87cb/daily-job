# A - 455

分值：$100100100$ 分

---

### Problem Statement

You are given integers $A,B,CA, B, CA,B,C$. If $A≠BA \neq BA=B$ and $B=CB = CB=C$, output `Yes`; otherwise, output `No`.

给定整数 $A,B,CA, B, CA,B,C$。如果 $A≠BA \neq BA=B$ 且 $B=CB = CB=C$，输出 `Yes`，否则输出 `No`。

---

### Constraints

-   $1≤A,B,C≤91 \leq A, B, C \leq 91≤A,B,C≤9$
-   All input values are integers.

- $1≤A,B,C≤91 \leq A, B, C \leq 91≤A,B,C≤9$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$AAA$ $BBB$ $CCC$

---

### Output

Output `Yes` or `No` according to the instructions in the problem statement.

根据题目描述的要求输出 `Yes` 或 `No`。

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

Since $4≠54 \neq 54=5$ and $5=55 = 55=5$, output `Yes`.

由于 $4≠54 \neq 54=5$ 且 $5=55 = 55=5$，输出 `Yes`。

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

Although $1≠31 \neq 31=3$, we don't have $3=73 = 73=7$, so output `No`.

虽然满足 $1≠31 \neq 31=3$，但不满足 $3=73 = 73=7$，因此输出 `No`。

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
