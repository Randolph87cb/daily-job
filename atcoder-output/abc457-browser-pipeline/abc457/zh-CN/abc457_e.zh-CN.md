# E - Crossing Table Cloth

分值：$475$ 分

---

### Problem Statement

There are $N$ cells arranged in a horizontal row. The $i$\-th cell from the left $(1 \le i \le N)$ is called cell $i$.

水平排列着 $N$ 个格子。从左数的第 $i$ 个格子 $(1 \le i \le N)$ 称为格子 $i$。

---

There are $M$ pieces of cloth. Laying cloth $i$ $(1 \le i \le M)$ covers cells $L_i$ through $R_i$.

共有 $M$ 块布。铺设布 $i$ $(1 \le i \le M)$ 会覆盖从 $L_i$ 到 $R_i$ 的所有格子。

---

Answer $Q$ queries. For the $q$\-th query $(1 \le q \le Q)$, integers $S_q$ and $T_q$ are given, so answer the following problem.

你需要回答 $Q$ 个询问。对于第 $q$ 个询问 $(1 \le q \le Q)$，会给出整数 $S_q$ 和 $T_q$，请回答如下问题。

---

-   Determine whether it is possible to choose exactly two pieces of cloth from the $M$ pieces and lay them so that the following condition is satisfied.
    -   Cells $S_q$ through $T_q$ are covered by at least one piece of cloth, and no other cells are covered by any cloth.

- 判断是否可以从 $M$ 块布中恰好选择两块并铺设，使得满足以下条件：
    - 从 $S_q$ 到 $T_q$ 的所有格子都被至少一块布覆盖，且除此之外没有其他格子被任何布覆盖。

---

### Constraints

-   $1 \le N \le 2 \times 10^5$
-   $2 \le M \le 2 \times 10^5$
-   $1 \le L_i \le R_i \le N$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le S_q \le T_q \le N$
-   All input values are integers.

- $1 \le N \le 2 \times 10^5$
- $2 \le M \le 2 \times 10^5$
- $1 \le L_i \le R_i \le N$
- $1 \le Q \le 2 \times 10^5$
- $1 \le S_q \le T_q \le N$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $M$  
$L_1$ $R_1$  
$L_2$ $R_2$  
$\vdots$  
$L_M$ $R_M$  
$Q$  
$S_1$ $T_1$  
$S_2$ $T_2$  
$\vdots$  
$S_Q$ $T_Q$

---

### Output

Output the answers for the queries, separated by newlines.

输出每个询问的答案，用换行分隔。

---

For each query, output `Yes` if it is possible to choose two pieces of cloth satisfying the condition, and `No` otherwise.

对于每个询问，如果存在满足条件的两块布则输出 `Yes`，否则输出 `No`。

---

### Sample Input 1

```text
4 3
1 3
1 1
2 4
4
1 4
2 4
1 3
1 1
```

---

### Sample Output 1

```text
Yes
No
Yes
No
```

---

For the first query, the condition can be satisfied by choosing cloth $1$ and cloth $3$.

对于第一个询问，选择布 $1$ 和布 $3$ 即可满足条件。

---

For the third query, the condition can be satisfied by choosing cloth $1$ and cloth $2$.

对于第三个询问，选择布 $1$ 和布 $2$ 即可满足条件。

---

For the second and fourth queries, no choice of two pieces of cloth can satisfy the condition.

对于第二个和第四个询问，不存在任何选择两块布的方案能满足条件。

---

### Sample Input 2

```text
7 10
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
2 3
1 2
10
1 2
3 5
1 4
1 5
1 5
5 7
1 6
2 3
5 7
2 4
```

---

### Sample Output 2

```text
Yes
No
No
Yes
Yes
No
Yes
Yes
No
No
```
