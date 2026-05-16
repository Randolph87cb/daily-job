# B - Count Adjacent Cells

分值：$200$ 分

---

### Problem Statement

There is a grid with $H$ rows and $W$ columns. The cell at the $i$\-th row from the top and the $j$\-th column from the left is denoted as cell $(i, j)$.

有一个 $H$ 行 $W$ 列的网格。从上往下第 $i$ 行、从左往右第 $j$ 列的格子记为 $(i, j)$。

---

Cells $(x_1, y_1)$ and $(x_2, y_2)$ are said to be **edge-adjacent** when $|x_1 - x_2| + |y_1 - y_2| = 1$.

当 $|x_1 - x_2| + |y_1 - y_2| = 1$ 时，我们称格子 $(x_1, y_1)$ 和 $(x_2, y_2)$ **边相邻**。

---

For every cell, find the number of cells that are edge-adjacent to it.

对于每个格子，求与它边相邻的格子数量。

---

### Constraints

-   $1 \leq H, W \leq 50$
-   All input values are integers.

-   $1 \leq H, W \leq 50$
-   所有输入值都是整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$H$ $W$

---

### Output

Output the answer in the following format:

按照以下格式输出答案：

---

```text
$x_{1,1}$ $x_{1,2}$ $\cdots$ $x_{1,W}$
$x_{2,1}$ $x_{2,2}$ $\cdots$ $x_{2,W}$
$\vdots$
$x_{H,1}$ $x_{H,2}$ $\cdots$ $x_{H,W}$
```

---

Here, $x_{i,j}$ represents the number of cells that are edge-adjacent to cell $(i, j)$.

其中，$x_{i,j}$ 表示与格子 $(i, j)$ 边相邻的格子数量。

---

### Sample Input 1

```text
4 5
```

---

### Sample Output 1

```text
2 3 3 3 2
3 4 4 4 3
3 4 4 4 3
2 3 3 3 2
```

---

The cells edge-adjacent to cell $(1, 5)$ are cells $(1, 4), (2, 5)$, for a total of two cells.

与格子 $(1, 5)$ 边相邻的格子是 $(1, 4), (2, 5)$，共 2 个。

---

The cells edge-adjacent to cell $(2, 3)$ are cells $(1, 3), (2, 2), (2, 4), (3, 3)$, for a total of four cells.

与格子 $(2, 3)$ 边相邻的格子是 $(1, 3), (2, 2), (2, 4), (3, 3)$，共 4 个。

---

The cells edge-adjacent to cell $(4, 2)$ are cells $(3, 2), (4, 1), (4, 3)$, for a total of three cells.

与格子 $(4, 2)$ 边相邻的格子是 $(3, 2), (4, 1), (4, 3)$，共 3 个。

---

### Sample Input 2

```text
1 1
```

---

### Sample Output 2

```text
0
```

---

There are no cells edge-adjacent to cell $(1, 1)$.

没有与格子 $(1, 1)$ 边相邻的格子。

---

### Sample Input 3

```text
12 8
```

---

### Sample Output 3

```text
2 3 3 3 3 3 3 2
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
3 4 4 4 4 4 4 3
2 3 3 3 3 3 3 2
```
