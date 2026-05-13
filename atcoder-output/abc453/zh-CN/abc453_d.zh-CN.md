# D - Go Straight

分值：$425$ 分

---

### Problem Statement

There is a grid of $H$ rows $\times$ $W$ columns, and Takahashi moves through this grid up, down, left, and right.  
The state of the cell at the $i$\-th row from the top and $j$\-th column from the left $(1\leq i\leq H, 1\leq j\leq W)$ is represented by the character $S_{i,j}$.  
$S_{i,j}$ is one of `#`, `.`, `o`, `x`, `S`, `G`.

有一个$H$行$\times$$W$列的网格，高桥可以在网格中上下左右移动。
从上往下数第$i$行、从左往右数第$j$列的单元格$(1\leq i\leq H, 1\leq j\leq W)$的状态由字符$S_{i,j}$表示。
$S_{i,j}$是`#`、`.`、`o`、`x`、`S`、`G`中的一个。

---

-   If $S_{i,j}=$`#`: This cell cannot be entered.
-   If $S_{i,j}=$`.`: This cell can be freely entered and exited. That is, after entering this cell, Takahashi can move to any adjacent cell (if it exists) in the up, down, left, or right direction.
-   If $S_{i,j}=$`o`: In this cell, **Takahashi must move in the same direction as the immediately preceding move**. That is, after entering this cell, he must move to the next cell without changing direction.
-   If $S_{i,j}=$`x`: In this cell, **Takahashi cannot move in the same direction as the immediately preceding move**. That is, after entering this cell, he must change direction to move to the next cell. Turning $180$ degrees to return to the previous cell is considered as changing direction.
-   If $S_{i,j}=$`S`: This cell is Takahashi's starting position. This cell can be freely entered and exited.
-   If $S_{i,j}=$`G`: This cell is Takahashi's destination. This cell can be freely entered and exited.

- 若$S_{i,j}=$`#`：该单元格无法进入。
- 若$S_{i,j}=$`.`：该单元格可以自由进出。也就是说，进入该单元格后，高桥可以移动到上下左右四个方向中任意存在的相邻单元格。
- 若$S_{i,j}=$`o`：在该单元格中，**高桥必须沿与上一步移动相同的方向移动**。也就是说，进入该单元格后，他必须保持方向不变移动到下一个单元格。
- 若$S_{i,j}=$`x`：在该单元格中，**高桥不能沿与上一步移动相同的方向移动**。也就是说，进入该单元格后，他必须改变方向再移动到下一个单元格。转向$180$度回到上一个单元格视为改变方向。
- 若$S_{i,j}=$`S`：该单元格是高桥的起点，可以自由进出。
- 若$S_{i,j}=$`G`：该单元格是高桥的终点，可以自由进出。

---

There is exactly one $(i,j)$ with $1\leq i\leq H, 1\leq j\leq W$ satisfying $S_{i,j}=$`S`, and exactly one satisfying $S_{i,j}=$`G`.

恰好存在一个满足$S_{i,j}=$`S`的$(i,j)$与$1\leq i\leq H, 1\leq j\leq W$，且恰好存在一个满足$S_{i,j}=$`G`的$(i,j)$与$1\leq i\leq H, 1\leq j\leq W$。

---

Takahashi wants to reach the destination by repeatedly moving to adjacent cells up, down, left, or right from his starting position.  
Determine whether this is possible, and if so, output one valid sequence of moves with at most $5\times 10^6$ moves between adjacent cells.  
It can be proved that if a valid sequence of moves exists under the problem's conditions, then there exists one with at most $5\times 10^6$ moves.  
As long as the number of moves is at most $5\times 10^6$, it is not necessary to minimize the number of moves.

高桥希望从起点出发，通过不断向上下左右的相邻单元格移动，最终到达终点。
请判断是否存在可行方案，若存在，输出一个满足条件的移动序列，要求相邻单元格之间的移动次数不超过$5\times 10^6$次。
可以证明，在本题的约束条件下，如果存在可行的移动序列，那么一定存在移动次数不超过$5\times 10^6$的方案。
只要移动次数不超过$5\times 10^6$，不需要最小化移动次数。

---

### Constraints

-   $1 \leq H,W\leq 1000$
-   $S_{i,j}$ is one of `#`, `.`, `o`, `x`, `S`, `G`.
-   There is exactly one $(i,j)$ satisfying $S_{i,j}=$`S` and exactly one satisfying $S_{i,j}=$`G`.
-   $H$ and $W$ are integers.

- $1 \leq H,W\leq 1000$
- $S_{i,j}$是`#`、`.`、`o`、`x`、`S`、`G`中的一个。
- 恰好存在一个满足$S_{i,j}=$`S`的$(i,j)$，且恰好存在一个满足$S_{i,j}=$`G`的$(i,j)$。
- $H$和$W$是整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$H$ $W$  
$S_{1,1} S_{1,2} \ldots S_{1,W}$  
$S_{2,1} S_{2,2} \ldots S_{2,W}$  
$\vdots$  
$S_{H,1} S_{H,2} \ldots S_{H,W}$

---

### Output

If it is impossible to reach the destination while satisfying the conditions, output `No` on the first line, and nothing on the second line.  
If it is possible to reach the destination while satisfying the conditions, output `Yes` on the first line.  
On the second line, output a string $T$ representing a sequence of moves. $T$ must satisfy all of the following conditions.

如果满足条件的前提下无法到达终点，第一行输出`No`，第二行不输出任何内容。
如果满足条件的前提下可以到达终点，第一行输出`Yes`。
第二行输出表示移动序列的字符串$T$。$T$必须满足以下所有条件：

---

-   The length $\lvert T\rvert$ of $T$ is between $1$ and $5\times 10^6$, inclusive.
-   Each character of $T$ is one of `U`, `D`, `L`, `R`.
    -   The $i$\-th character of $T$ being `U`, `D`, `L`, `R` means that in the $i$\-th move after departing, Takahashi moves to the adjacent cell above, below, to the left, or to the right, respectively.
-   For $1\leq i\leq \lvert T\rvert$, Takahashi is not outside the grid after the $i$\-th move.
-   During the moves, the conditions of each cell are not violated.
-   After the $\lvert T\rvert$\-th move, Takahashi is at the destination cell. As long as this condition is satisfied, he may pass through the destination cell before the $\lvert T\rvert$\-th move.

- $T$的长度$\lvert T\rvert$介于$1$和$5\times 10^6$之间（含两端）。
- $T$的每个字符都是`U`、`D`、`L`、`R`中的一个。
  - 若$T$的第$i$个字符为`U`、`D`、`L`、`R`，分别表示高桥在出发后的第$i$次移动中，向上、下、左、右方向的相邻单元格移动。
- 对于$1\leq i\leq \lvert T\rvert$，第$i$次移动结束后高桥不在网格外。
- 移动过程中没有违反每个单元格的规则。
- 第$\lvert T\rvert$次移动结束后，高桥位于终点单元格。只要满足该条件，在第$\lvert T\rvert$次移动之前他可以经过终点单元格。

---

### Sample Input 1

```text
3 5
.#...
.Sooo
..x.G
```

---

### Sample Output 1

```text
Yes
DRUUDDRR
```

---

Let cell $(i,j)$ denote the cell at the $i$\-th row from the top and $j$\-th column from the left.  
Following the sample output, the path goes: cell $(2,2)$ $\to$ cell $(3,2)$ $\to$ cell $(3,3)$ $\to$ cell $(2,3)$ $\to$ cell $(1,3)$ $\to$ cell $(2,3)$ $\to$ cell $(3,3)$ $\to$ cell $(3,4)$ $\to$ cell $(3,5)$, reaching the destination.  
Other solutions such as `DRUURLRRDD` are also accepted. On the other hand, since Takahashi cannot go straight through cell $(3,3)$, solutions such as `DRRR` are not accepted.

记单元格$(i,j)$表示从上往下数第$i$行、从左往右数第$j$列的单元格。
根据样例输出，路径为：单元格$(2,2)$ → 单元格$(3,2)$ → 单元格$(3,3)$ → 单元格$(2,3)$ → 单元格$(1,3)$ → 单元格$(2,3)$ → 单元格$(3,3)$ → 单元格$(3,4)$ → 单元格$(3,5)$，到达终点。
其他方案如`DRUURLRRDD`也会被接受。但由于高桥不能直接直行通过单元格$(3,3)$，因此`DRRR`这类方案是不被接受的。

---

### Sample Input 2

```text
3 3
#So
xoG
..#
```

---

### Sample Output 2

```text
Yes
DDLURR
```

---

### Sample Input 3

```text
2 2
So
oG
```

---

### Sample Output 3

```text
No
```

---

It is impossible to reach the destination while satisfying the conditions.

在满足条件的前提下无法到达终点。
