# G - Copy Query

分值：$600$ 分

---

### Problem Statement

There are $N$ sequences of length $M$: $A_1,A_2,\dots,A_N$. Initially, all elements of all sequences are $0$.  
Hereafter, the $j$\-th element of sequence $A_i$ is denoted by $A_{i,j}$.

共有 $N$ 个长度为 $M$ 的序列：$A_1,A_2,\dots,A_N$。初始时，所有序列的所有元素均为 $0$。
以下，序列 $A_i$ 的第 $j$ 个元素记为 $A_{i,j}$。

---

Process the following three types of queries in the given order, $Q$ queries in total.

按给定顺序处理以下三种类型的查询，总共有 $Q$ 个查询。

---

-   Type $1$: Overwrite sequence $A_{X_i}$ with sequence $A_{Y_i}$. That is, for every integer $j$ ($1 \le j \le M$), change $A_{X_i,j}$ to $A_{Y_i,j}$.
-   Type $2$: Change the $Y_i$\-th element of sequence $A_{X_i}$, that is, $A_{X_i,Y_i}$, to $Z_i$.
-   Type $3$: For sequence $A_{X_i}$, output the sum of elements from the $L_i$\-th through the $R_i$\-th, that is, $A_{X_i,L_i}+A_{X_i,L_i+1}+\dots+A_{X_i,R_i}$.

- 类型 $1$：用序列 $A_{Y_i}$ 覆盖序列 $A_{X_i}$。即对于每个整数 $j$（$1 \le j \le M$），将 $A_{X_i,j}$ 修改为 $A_{Y_i,j}$。
- 类型 $2$：修改序列 $A_{X_i}$ 的第 $Y_i$ 个元素，即将 $A_{X_i,Y_i}$ 修改为 $Z_i$。
- 类型 $3$：对于序列 $A_{X_i}$，输出第 $L_i$ 个到第 $R_i$ 个元素的和，即 $A_{X_i,L_i}+A_{X_i,L_i+1}+\dots+A_{X_i,R_i}$。

---

### Constraints

-   $1 \le N,M \le 2 \times 10^5$
-   $1 \le Q \le 2 \times 10^5$
-   Type $1$ queries satisfy the following constraints:
    -   $1 \le X_i,Y_i \le N$
-   Type $2$ queries satisfy the following constraints:
    -   $1 \le X_i \le N$
    -   $1 \le Y_i \le M$
    -   $0 \le Z_i \le 10^9$
-   Type $3$ queries satisfy the following constraints:
    -   $1 \le X_i \le N$
    -   $1 \le L_i \le R_i \le M$
-   All input values are integers.

- $1 \le N,M \le 2 \times 10^5$
- $1 \le Q \le 2 \times 10^5$
- 类型 $1$ 的查询满足以下约束条件：
  - $1 \le X_i,Y_i \le N$
- 类型 $2$ 的查询满足以下约束条件：
  - $1 \le X_i \le N$
  - $1 \le Y_i \le M$
  - $0 \le Z_i \le 10^9$
- 类型 $3$ 的查询满足以下约束条件：
  - $1 \le X_i \le N$
  - $1 \le L_i \le R_i \le M$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $M$ $Q$  
${\rm Query}_1$  
${\rm Query}_2$  
$\vdots$  
${\rm Query}_Q$

---

Here, ${\rm Query}_i$ represents the $i$\-th query.

其中，${\rm Query}_i$ 表示第 $i$ 个查询。

---

A type $1$ query is given in the following format:

类型 $1$ 的查询按照以下格式给出：

$1$ $X_i$ $Y_i$

---

A type $2$ query is given in the following format:

类型 $2$ 的查询按照以下格式给出：

$2$ $X_i$ $Y_i$ $Z_i$

---

A type $3$ query is given in the following format:

类型 $3$ 的查询按照以下格式给出：

$3$ $X_i$ $L_i$ $R_i$

---

### Output

For each type $3$ query, output the answer to that query. If there are no type $3$ queries, the output should be empty.

对于每个类型 $3$ 的查询，输出该查询的答案。如果没有类型 $3$ 的查询，则输出为空。

---

### Sample Input 1

```text
4 5 10
2 2 1 2
2 2 2 7
2 2 4 8
1 1 2
2 2 3 1
1 3 2
2 3 2 10
3 1 2 4
3 2 1 4
3 3 2 2
```

---

### Sample Output 1

```text
15
18
10
```

---

In this input, prepare four sequences of length $5$.

在该输入中，准备四个长度为 $5$ 的序列。

---

-   In the $1$st query, set $A_{2,1}=2$. At this point, $A_2=(2,0,0,0,0)$.
-   In the $2$nd query, set $A_{2,2}=7$. At this point, $A_2=(2,7,0,0,0)$.
-   In the $3$rd query, set $A_{2,4}=8$. At this point, $A_2=(2,7,0,8,0)$.
-   In the $4$th query, overwrite sequence $A_1$ with sequence $A_2$. At this point, $A_1=(2,7,0,8,0)$.
-   In the $5$th query, set $A_{2,3}=1$. At this point, $A_2=(2,7,1,8,0)$.
-   In the $6$th query, overwrite sequence $A_3$ with sequence $A_2$. At this point, $A_3=(2,7,1,8,0)$.
-   In the $7$th query, set $A_{3,2}=10$. At this point, $A_3=(2,10,1,8,0)$.
-   In the $8$th query, output $A_{1,2}+A_{1,3}+A_{1,4}=7+0+8=15$.
-   In the $9$th query, output $A_{2,1}+A_{2,2}+A_{2,3}+A_{2,4}=2+7+1+8=18$.
-   In the $10$th query, output $A_{3,2}=10$.

- 第 $1$ 个查询中，设置 $A_{2,1}=2$。此时 $A_2=(2,0,0,0,0)$。
- 第 $2$ 个查询中，设置 $A_{2,2}=7$。此时 $A_2=(2,7,0,0,0)$。
- 第 $3$ 个查询中，设置 $A_{2,4}=8$。此时 $A_2=(2,7,0,8,0)$。
- 第 $4$ 个查询中，用序列 $A_2$ 覆盖序列 $A_1$。此时 $A_1=(2,7,0,8,0)$。
- 第 $5$ 个查询中，设置 $A_{2,3}=1$。此时 $A_2=(2,7,1,8,0)$。
- 第 $6$ 个查询中，用序列 $A_2$ 覆盖序列 $A_3$。此时 $A_3=(2,7,1,8,0)$。
- 第 $7$ 个查询中，设置 $A_{3,2}=10$。此时 $A_3=(2,10,1,8,0)$。
- 第 $8$ 个查询中，输出 $A_{1,2}+A_{1,3}+A_{1,4}=7+0+8=15$。
- 第 $9$ 个查询中，输出 $A_{2,1}+A_{2,2}+A_{2,3}+A_{2,4}=2+7+1+8=18$。
- 第 $10$ 个查询中，输出 $A_{3,2}=10$。
