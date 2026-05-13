# B - Mapping

分值：$200$ 分

---

### Problem Statement

There are $N$ people numbered $1$ through $N$.  
There are $M$ types of clothes numbered $1$ through $M$. Person $i$ is wearing clothes $F_i$.  
Answer the following two questions with Yes or No.

共有 $N$ 个人，编号为 $1$ 到 $N$。
共有 $M$ 种衣物，编号为 $1$ 到 $M$。第 $i$ 个人穿着编号为 $F_i$ 的衣物。
请用 Yes 或 No 回答以下两个问题。

---

-   Question $1$: Are all $N$ people wearing different types of clothes?
-   Question $2$: For every one of the $M$ types of clothes, is there at least one person wearing that type?

- 问题 $1$：所有 $N$ 个人穿的衣物种类都互不相同吗？
- 问题 $2$：对于 $M$ 种衣物中的每一种，都至少有一个人穿着该种衣物吗？

---

### Constraints

-   $1 \leq N \leq 100$
-   $1 \leq M \leq 100$
-   $1 \leq F_i \leq M$
-   All input values are integers.

- $1 \leq N \leq 100$
- $1 \leq M \leq 100$
- $1 \leq F_i \leq M$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $M$  
$F_1$ $F_2$ $\dots$ $F_N$

---

### Output

Output two lines. The $i$\-th line should contain `Yes` if the answer to question $i$ is Yes, and `No` if it is No.

输出两行。第 $i$ 行如果对应问题 $i$ 的答案为 Yes 则输出 `Yes`，为 No 则输出 `No`。

---

### Sample Input 1

```text
3 4
1 2 4
```

---

### Sample Output 1

```text
Yes
No
```

---

Everyone is wearing a different type of clothes, so the answer to question $1$ is Yes.  
There is no person wearing clothes $3$, so the answer to question $2$ is No.

所有人穿着的衣物种类都互不相同，因此问题 $1$ 的答案是 Yes。
没有人穿着编号为 $3$ 的衣物，因此问题 $2$ 的答案是 No。

---

### Sample Input 2

```text
4 2
1 2 1 2
```

---

### Sample Output 2

```text
No
Yes
```

---

### Sample Input 3

```text
4 4
1 3 2 1
```

---

### Sample Output 3

```text
No
No
```

---

### Sample Input 4

```text
5 5
1 3 4 2 5
```

---

### Sample Output 4

```text
Yes
Yes
```
