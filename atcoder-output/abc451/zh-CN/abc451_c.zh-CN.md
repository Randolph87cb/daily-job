# C - Understory

分值：$300$ 分

---

### Problem Statement

Takahashi is managing the number of trees in his garden. Initially, there are no trees in the garden.

高桥正在管理他花园里的树木数量。初始时，花园里没有树。

---

$Q$ queries are given in order. Each query is one of the following two types. Immediately after processing each query, output the number of trees currently in the garden.

按顺序给出 $Q$ 次查询，每次查询属于以下两种类型之一。处理完每次查询后，立即输出当前花园中的树木数量。

---

-   `1 h` : Add one new tree of height $h$ to the garden.
-   `2 h` : Remove all trees currently in the garden whose height is at most $h$.

-   `1 h`：向花园中添加一棵高度为 $h$ 的新树。
-   `2 h`：移除花园中当前所有高度不超过 $h$ 的树。

---

### Constraints

-   $1 \le Q \le 3 \times 10^5$
-   $1 \le h \le 10^9$
-   All input values are integers.

-   $1 \le Q \le 3 \times 10^5$
-   $1 \le h \le 10^9$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$Q$  
$\text{query}_1$  
$\text{query}_2$  
$\vdots$  
$\text{query}_Q$

---

$\text{query}_i$, representing the $i$\-th query, is one of the following two types:

$\text{query}_i$ 代表第 $i$ 次查询，属于以下两种类型之一：

$1$ $h$  
$```$  
$```text$  
$2$ $h$

---

### Output

Output $Q$ lines.

输出 $Q$ 行。

---

The $i$\-th line should contain the number of trees in the garden immediately after processing the $i$\-th query.

第 $i$ 行应包含处理完第 $i$ 次查询后，花园中当前的树木数量。

---

### Sample Input 1

```text
5
1 5
1 7
1 8
2 7
1 3
```

---

### Sample Output 1

```text
1
2
3
1
2
```

---

The number of trees changes as follows.

树木数量的变化过程如下：

---

-   A tree of height $5$ is added. The garden contains one tree of height $5$.
-   A tree of height $7$ is added. The garden contains two trees of heights $5, 7$.
-   A tree of height $8$ is added. The garden contains three trees of heights $5, 7, 8$.
-   Trees of height at most $7$ are removed. The garden contains one tree of height $8$.
-   A tree of height $3$ is added. The garden contains two trees of heights $8, 3$.

-   添加一棵高度为 $5$ 的树，花园中有1棵高度为 $5$ 的树。
-   添加一棵高度为 $7$ 的树，花园中有2棵高度分别为 $5, 7$ 的树。
-   添加一棵高度为 $8$ 的树，花园中有3棵高度分别为 $5, 7, 8$ 的树。
-   移除所有高度不超过 $7$ 的树，花园中有1棵高度为 $8$ 的树。
-   添加一棵高度为 $3$ 的树，花园中有2棵高度分别为 $8, 3$ 的树。

---

### Sample Input 2

```text
12
2 256601193
1 85138616
1 202564041
2 276477192
1 55551662
1 170271057
2 754166580
1 854388209
1 772036624
2 651124113
1 301137866
2 290875185
```

---

### Sample Output 2

```text
0
1
2
0
1
2
0
1
2
2
3
3
```
