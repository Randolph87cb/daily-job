# C - Vanish

分值：$300300300$ 分

---

### Problem Statement

You are given an integer sequence $A=(A1,A2,…,AN)A = (A_1, A_2, \ldots, A_N)A=(A1​,A2​,…,AN​)$.

给定一个整数序列 $A=(A1,A2,…,AN)A = (A_1, A_2, \ldots, A_N)A=(A1​,A2​,…,AN​)$。

---

Find the minimum possible sum of all elements of $AAA$ after performing the following operation exactly $KKK$ times.

求恰好执行 $KKK$ 次下述操作后，$AAA$ 的所有元素之和的最小可能值。

---

-   Choose an integer $xxx$. For each $iii$ such that $Ai=xA_i = xAi​=x$, replace the value of $AiA_iAi​$ with $000$.

- 选择一个整数 $xxx$。对于每个满足 $Ai=xA_i = xAi​=x$ 的 $iii$，将 $AiA_iAi​$ 的值替换为 $000$。

---

### Constraints

-   $1≤K≤N≤3×1051 \leq K \leq N \leq 3 \times 10^51≤K≤N≤3×105$
-   $1≤Ai≤1091 \leq A_i \leq 10^91≤Ai​≤109$
-   All input values are integers.

- $1≤K≤N≤3×1051 \leq K \leq N \leq 3 \times 10^51≤K≤N≤3×105$
- $1≤Ai≤1091 \leq A_i \leq 10^91≤Ai​≤109$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$NNN$ $KKK$  
$A1A_1A1​$ $A2A_2A2​$ $…\ldots…$ $ANA_NAN​$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
6 2
7 2 7 2 2 9
```

---

### Sample Output 1

```text
6
```

---

Initially, $A=(7,2,7,2,2,9)A = (7, 2, 7, 2, 2, 9)A=(7,2,7,2,2,9)$.

初始时，$A=(7,2,7,2,2,9)A = (7, 2, 7, 2, 2, 9)A=(7,2,7,2,2,9)$。

---

Performing the operation with $x=9x = 9x=9$ gives $A=(7,2,7,2,2,0)A = (7, 2, 7, 2, 2, 0)A=(7,2,7,2,2,0)$.

选择 $x=9x = 9x=9$ 执行一次操作后，得到 $A=(7,2,7,2,2,0)A = (7, 2, 7, 2, 2, 0)A=(7,2,7,2,2,0)$。

---

Next, performing the operation with $x=7x = 7x=7$ gives $A=(0,2,0,2,2,0)A = (0, 2, 0, 2, 2, 0)A=(0,2,0,2,2,0)$.

接下来，选择 $x=7x = 7x=7$ 执行一次操作后，得到 $A=(0,2,0,2,2,0)A = (0, 2, 0, 2, 2, 0)A=(0,2,0,2,2,0)$。

---

At this point, the sum of all elements of $AAA$ is $0+2+0+2+2+0=60 + 2 + 0 + 2 + 2 + 0 = 60+2+0+2+2+0=6$.

此时，$AAA$ 的所有元素之和为 $0+2+0+2+2+0=60 + 2 + 0 + 2 + 2 + 0 = 60+2+0+2+2+0=6$。

---

### Sample Input 2

```text
8 6
1 2 3 4 1 2 3 4
```

---

### Sample Output 2

```text
0
```

---

### Sample Input 3

```text
10 2
3 3 4 1 1 3 3 1 5 1
```

---

### Sample Output 3

```text
8
```
