# D - Card Pile Query

分值：$400$ 分

---

### Problem Statement

There are $N$ cards and $N$ piles of cards.

有 $N$ 张卡片和 $N$ 堆卡片。

---

The cards and the piles are numbered $1, 2, \ldots, N$. Initially, pile $i$ contains only card $i$.

卡片和堆的编号为 $1, 2, \ldots, N$。初始时，堆 $i$ 中只有卡片 $i$。

---

Perform the following operation for each $i = 1, 2, \ldots, Q$ in order:

按顺序对每个 $i = 1, 2, \ldots, Q$ 执行以下操作：

---

-   Move card $C_i$ and all cards stacked on top of card $C_i$, preserving their order, on top of card $P_i$. It is guaranteed that immediately before performing the operation, cards $C_i$ and $P_i$ are in different piles, and card $P_i$ is on top of some pile.

- 将卡片 $C_i$ 以及堆在它上方的所有卡片保持原有顺序，移动到卡片 $P_i$ 的上方。题目保证在执行该操作前，卡片 $C_i$ 和 $P_i$ 位于不同的堆中，且卡片 $P_i$ 处于某个堆的顶部。

---

Find the number of cards in each pile after all operations are completed.

求所有操作完成后每堆中的卡片数量。

---

### Constraints

-   $1 \leq N, Q \leq 3 \times 10^5$
-   $1 \leq C_i, P_i \leq N$
-   When the operations are performed in order, immediately before each operation, cards $C_i$ and $P_i$ are in different piles.
-   When the operations are performed in order, immediately before each operation, card $P_i$ is on top of some pile.
-   All input values are integers.

- $1 \leq N, Q \leq 3 \times 10^5$
- $1 \leq C_i, P_i \leq N$
- 按顺序执行操作时，每次操作前，卡片 $C_i$ 和 $P_i$ 都位于不同的堆中。
- 按顺序执行操作时，每次操作前，卡片 $P_i$ 都处于某个堆的顶部。
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $Q$  
$C_1$ $P_1$  
$C_2$ $P_2$  
$\vdots$  
$C_Q$ $P_Q$

---

### Output

Let $A_i$ be the number of cards in pile $i$ at the end. Output $A_1, A_2, \ldots, A_N$ in this order, separated by spaces.

设 $A_i$ 为最终堆 $i$ 中的卡片数量。按顺序输出 $A_1, A_2, \ldots, A_N$，数值之间用空格分隔。

---

### Sample Input 1

```text
5 4
1 3
4 5
1 4
4 2
```

---

### Sample Output 1

```text
0 3 1 0 1
```

---

The sequence of operations proceeds as shown in the figure below.

操作序列的执行过程如下图所示。

---

![](https://img.atcoder.jp/abc455/aca7dea26cc92ed4ff7e4992208922ab.png)

![](https://img.atcoder.jp/abc455/aca7dea26cc92ed4ff7e4992208922ab.png)

---

### Sample Input 2

```text
7 8
3 1
5 4
2 5
5 7
2 3
6 2
3 4
5 1
```

---

### Sample Output 2

```text
2 0 0 4 0 0 1
```
