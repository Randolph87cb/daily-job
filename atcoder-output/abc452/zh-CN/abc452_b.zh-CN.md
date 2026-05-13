# B - Draw Frame

分值：$200$ 分

---

### Problem Statement

There is a grid with $H$ rows and $W$ columns. Takahashi is going to paint each cell of this grid black or white.

有一个 $H$ 行 $W$ 列的网格。高桥打算将网格的每个格子涂成黑色或白色。

---

He paints all cells on the border of the grid black, and all other cells white. Output the grid after he has painted it.

他将网格边界上的所有格子涂成黑色，其余所有格子涂成白色。请输出涂色完成后的网格。

---

**More formally**

**更正式地说**

---

There is an $H\times W$ grid.

有一个大小为 $H\times W$ 的网格。

---

We call the cell at the $i$\-th row from the top $(1\le i\le H)$ and the $j$\-th column from the left $(1\le j\le W)$ cell $(i,j)$.

我们将从上往下数第 $i$ 行、从左往右数第 $j$ 列的格子记作 $(i,j)$。

---

Cell $(i,j)\ (1\le i\le H,1\le j\le W)$ and cell $(k,l)\ (1\le k\le H,1\le l\le W)$ are said to be **edge-adjacent** if and only if $|i-k|+|j-l|=1$.

当且仅当 $|i-k|+|j-l|=1$ 时，称格子 $(i,j)\ (1\le i\le H,1\le j\le W)$ 和格子 $(k,l)\ (1\le k\le H,1\le l\le W)$ **边相邻**。

---

Cell $(i,j)$ is said to be **on the border** if and only if the number of cells edge-adjacent to cell $(i,j)$ is at most $3$.

当且仅当与格子 $(i,j)$ 边相邻的格子数量不超过 $3$ 时，称格子 $(i,j)$ **在边界上**。

---

Find $H$ strings $S _ 1,S _ 2,\ldots,S _ H$ satisfying the following condition.

求满足以下条件的 $H$ 个字符串 $S _ 1,S _ 2,\ldots,S _ H$。

---

-   $S _ i$ is a string of length $W$, and the $j$\-th character of $S _ i$ is `#` if cell $(i,j)$ is on the border, and `.` otherwise.

- $S _ i$ 是一个长度为 $W$ 的字符串，若格子 $(i,j)$ 在边界上，则 $S _ i$ 的第 $j$ 个字符为 `#`，否则为 `.`。

---

### Constraints

-   $3\le H\le10$
-   $3\le W\le10$
-   All input values are integers.

- $3\le H\le10$
- $3\le W\le10$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$H$ $W$

---

### Output

Output $H$ lines, each a string of length $W$. The $j$\-th character $(1\le j\le W)$ of the $i$\-th line $(1\le i\le H)$ should be `#` if cell $(i,j)$ is painted black, and `.` if it is painted white.

输出 $H$ 行，每行是一个长度为 $W$ 的字符串。若格子 $(i,j)$ 被涂成黑色，则第 $i$ 行的第 $j$ 个字符 $(1\le j\le W)$ 应为 `#`，若涂成白色则应为 `.`。

---

### Sample Input 1

```text
4 5
```

---

### Sample Output 1

```text
#####
#...#
#...#
#####
```

---

For example, cell $(1,1)$ is on the border. This is because there are only two cells edge-adjacent to cell $(1,1)$: cells $(1,2)$ and $(2,1)$. Thus, cell $(1,1)$ is painted black, so the first character of the first line should be `#`.

例如，格子 $(1,1)$ 在边界上。这是因为与格子 $(1,1)$ 边相邻的格子只有两个：格子 $(1,2)$ 和格子 $(2,1)$。因此格子 $(1,1)$ 被涂成黑色，所以第一行的第一个字符应为 `#`。

---

Conversely, for example, cell $(3,4)$ is not on the border. This is because there are four cells edge-adjacent to cell $(3,4)$: cells $(2,4),$ $(3,3),$ $(3,5),$ and $(4,4)$. Thus, cell $(3,4)$ is painted white, so the fourth character of the third line should be `.`.

反之，例如格子 $(3,4)$ 不在边界上。这是因为与格子 $(3,4)$ 边相邻的格子有四个：格子 $(2,4),$、$(3,3),$、$(3,5),$ 和 $(4,4)$。因此格子 $(3,4)$ 被涂成白色，所以第三行的第四个字符应为 `.`。

---

### Sample Input 2

```text
5 6
```

---

### Sample Output 2

```text
######
#....#
#....#
#....#
######
```
