# G - Children Yearn for the Evil Kindergarten

分值：$625$ 分

---

### Problem Statement

There are $10^{100}$ kids at a game venue. Initially, no kid has any medals.

游戏场馆里共有 $10^{100}$ 个孩子。初始时，所有孩子都没有奖牌。

---

A kid leaves the venue exactly when they either **drop out** or **escape**.

当且仅当孩子**被淘汰**或**逃离**时，他们会离开场馆。

---

The game consists of $N$ days. On day $i$ ($1 \leq i \leq N$), the following sequence of operations is performed in order.

游戏持续 $N$ 天。在第 $i$ 天（$1 \leq i \leq N$），将按顺序执行以下操作序列。

---

-   Collect all medals held by the kids at the venue, and let $s$ be the total number of collected medals.
-   Distribute $s + A_i$ medals freely among the kids at the venue (if there are no kids at the venue, do nothing).
-   Among the kids at the venue, those with fewer than $B_i$ medals drop out. Those with at least $B_i$ medals each lose $B_i$ medals.
-   Among the kids at the venue, those with at least $C_i$ medals each choose whether to escape at this point or remain at the venue.

- 收回场馆内所有孩子持有的奖牌，记收回的奖牌总数为 $s$。
- 将 $s + A_i$ 枚奖牌自由分配给场馆内的孩子（如果场馆内没有孩子则不执行操作）。
- 在场馆内的孩子中，奖牌数少于 $B_i$ 的孩子将被淘汰；奖牌数不少于 $B_i$ 的孩子每人扣除 $B_i$ 枚奖牌。
- 在场馆内的孩子中，奖牌数不少于 $C_i$ 的孩子可以选择此时逃离，或者留在场馆内。

---

Kids who remain at the venue at the end of the $N$ days drop out.

在 $N$ 天结束后仍留在场馆内的孩子将被淘汰。

---

Find the maximum possible number of kids who ultimately escape.

求最终能够逃离的孩子的最大可能数量。

---

You are given $T$ test cases; solve each of them.

给定 $T$ 组测试数据，你需要解决每组数据。

---

### Constraints

-   $1 \leq T \leq 3 \times 10^5$
-   $1 \leq N \leq 3 \times 10^5$
-   $1 \leq A_i \leq 10^6$
-   $1 \leq B_i \leq 10^6$
-   $1 \leq C_i \leq 10^6$
-   The sum of $N$ over all test cases is at most $3 \times 10^5$.
-   All input values are integers.

- $1 \leq T \leq 3 \times 10^5$
- $1 \leq N \leq 3 \times 10^5$
- $1 \leq A_i \leq 10^6$
- $1 \leq B_i \leq 10^6$
- $1 \leq C_i \leq 10^6$
- 所有测试数据的 $N$ 之和不超过 $3 \times 10^5$。
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$T$  
$\mathrm{case}_{1}$  
$\mathrm{case}_{2}$  
$\vdots$  
$\mathrm{case}_{T}$

---

Each test case is given in the following format:

每组测试数据按照以下格式给出：

$N$  
$A_1$ $B_1$ $C_1$  
$A_2$ $B_2$ $C_2$  
$\vdots$  
$A_N$ $B_N$ $C_N$

---

### Output

Output the answers for the test cases in order, separated by newlines.

按顺序输出每组测试数据的答案，答案之间用换行分隔。

---

### Sample Input 1

```text
2
4
16 2 3
15 2 4
1 3 5
20 5 5
2
41404 1 941738
211877 205711 417821
```

---

### Sample Output 1

```text
5
0
```

---

Consider the first test case. By acting as follows, five kids can escape.

考虑第一组测试数据。通过如下操作，可以让5个孩子逃离。

---

-   At the start of day $1$, collect $s = 0$ medals from $10^{100}$ kids. Then, proceed as follows.
    -   Distribute $0 + 16 = 16$ medals so that the kids' medal counts become $(5, 5, 2, 2, 2, 0, \dots, 0)$.
    -   The $10^{100} - 5$ kids with no medals drop out, and the remaining $5$ kids' medal counts become $(3, 3, 0, 0, 0)$.
    -   The $2$ kids with $3$ medals each choose to escape, and the remaining $3$ kids' medal counts become $(0, 0, 0)$.
-   At the start of day $2$, collect $s = 0$ medals from $3$ kids. Then, proceed as follows.
    -   Distribute $0 + 15 = 15$ medals so that the kids' medal counts becomes $(6, 6, 3)$.
    -   No one drops out, and the remaining $3$ kids' medal counts become $(4, 4, 1)$.
    -   $1$ kid with $4$ medals chooses to escape, and the remaining $2$ kids' medal counts become $(4, 1)$.
-   At the start of day $3$, collect $s = 5$ medals from $2$ kids. Then, proceed as follows.
    -   Distribute $5 + 1 = 6$ medals so that the kids' medal counts becomes $(3, 3)$.
    -   No one drops out, and the remaining $2$ kids' medal counts become $(0, 0)$.
    -   No one escapes.
-   At the start of day $4$, collect $s = 0$ medals from $2$ kids. Then, proceed as follows.
    -   Distribute $0 + 20 = 20$ medals so that the kids' medal counts becomes $(10, 10)$.
    -   No one drops out, and the remaining $2$ kids' medal counts become $(5, 5)$.
    -   The $2$ kids with $5$ medals each choose to escape, and the venue becomes empty.

- 在第 $1$ 天开始时，从 $10^{100}$ 个孩子处收回 $s = 0$ 枚奖牌。然后执行如下操作：
  - 分配 $0 + 16 = 16$ 枚奖牌，使得孩子们的奖牌数变为 $(5, 5, 2, 2, 2, 0, \dots, 0)$。
  - $10^{100} - 5$ 个没有奖牌的孩子被淘汰，剩余 $5$ 个孩子的奖牌数变为 $(3, 3, 0, 0, 0)$。
  - 拥有 $3$ 枚奖牌的 $2$ 个孩子选择逃离，剩余 $3$ 个孩子的奖牌数变为 $(0, 0, 0)$。
- 在第 $2$ 天开始时，从 $3$ 个孩子处收回 $s = 0$ 枚奖牌。然后执行如下操作：
  - 分配 $0 + 15 = 15$ 枚奖牌，使得孩子们的奖牌数变为 $(6, 6, 3)$。
  - 没有人被淘汰，剩余 $3$ 个孩子的奖牌数变为 $(4, 4, 1)$。
  - 拥有 $4$ 枚奖牌的 $1$ 个孩子选择逃离，剩余 $2$ 个孩子的奖牌数变为 $(4, 1)$。
- 在第 $3$ 天开始时，从 $2$ 个孩子处收回 $s = 5$ 枚奖牌。然后执行如下操作：
  - 分配 $5 + 1 = 6$ 枚奖牌，使得孩子们的奖牌数变为 $(3, 3)$。
  - 没有人被淘汰，剩余 $2$ 个孩子的奖牌数变为 $(0, 0)$。
  - 没有人逃离。
- 在第 $4$ 天开始时，从 $2$ 个孩子处收回 $s = 0$ 枚奖牌。然后执行如下操作：
  - 分配 $0 + 20 = 20$ 枚奖牌，使得孩子们的奖牌数变为 $(10, 10)$。
  - 没有人被淘汰，剩余 $2$ 个孩子的奖牌数变为 $(5, 5)$。
  - 拥有 $5$ 枚奖牌的 $2$ 个孩子选择逃离，场馆变为空。

---

In the second test case, not a single kid can escape.

在第二组测试数据中，没有孩子能够逃离。
