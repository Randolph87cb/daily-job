# B - Personnel Change

分值：$200$ 分

---

### Problem Statement

The company where Takahashi works has $N$ employees, each assigned an employee number from $1, 2, \dots, N$. There are $M$ departments in the company, called departments $1, 2, \dots, M$.

高桥所在的公司共有 $N$ 名员工，每位员工都有一个从 $1, 2, \dots, N$ 开始编号的工号。公司共有 $M$ 个部门，编号为 $1, 2, \dots, M$。

---

Employee $i$ belongs to department $A_i$ this term and will belong to department $B_i$ next term.

员工 $i$ 本学期属于部门 $A_i$，下学期将调入部门 $B_i$。

---

For each of departments $1, 2, \dots, M$, find the number of members next term minus the number of members this term.

对于编号为 $1, 2, \dots, M$ 的每个部门，计算其下学期成员数减去本学期成员数的差值。

---

### Constraints

-   $1 \leq N \leq 100$
-   $1 \leq M \leq 100$
-   $1 \leq A_i \leq M$
-   $1 \leq B_i \leq M$
-   All input values are integers.

-   $1 \leq N \leq 100$
-   $1 \leq M \leq 100$
-   $1 \leq A_i \leq M$
-   $1 \leq B_i \leq M$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $M$  
$A_1$ $B_1$  
$A_2$ $B_2$  
$\vdots$  
$A_N$ $B_N$

---

### Output

Output $M$ lines. The $j$\-th line should contain the answer for department $j$.

输出 $M$ 行。第 $j$ 行应包含部门 $j$ 对应的答案。

---

### Sample Input 1

```text
5 4
1 2
2 1
3 1
2 2
2 4
```

---

### Sample Output 1

```text
1
-1
-1
1
```

---

-   For department $1$: this term, one employee (employee number $1$) belongs; next term, two employees (employee numbers $2, 3$) belong.
-   For department $2$: this term, three employees (employee numbers $2, 4, 5$) belong; next term, two employees (employee numbers $1, 4$) belong.
-   For department $3$: this term, one employee (employee number $3$) belongs; next term, no one belongs.
-   For department $4$: this term, no one belongs; next term, one employee (employee number $5$) belongs.

-   部门 $1$：本学期有 1 名员工（工号 $1$）；下学期有 2 名员工（工号 $2, 3$）。
-   部门 $2$：本学期有 3 名员工（工号 $2, 4, 5$）；下学期有 2 名员工（工号 $1, 4$）。
-   部门 $3$：本学期有 1 名员工（工号 $3$）；下学期没有成员。
-   部门 $4$：本学期没有成员；下学期有 1 名员工（工号 $5$）。

---

### Sample Input 2

```text
10 5
3 2
3 4
1 2
2 2
4 4
3 1
3 4
4 2
3 3
3 2
```

---

### Sample Output 2

```text
0
4
-5
1
0
```
