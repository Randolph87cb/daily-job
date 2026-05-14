# C - Puddles

分值：$300$ 分

---

### Problem Statement

There is a grid with $H$ rows and $W$ columns.  
The cell at the $i$\-th row from the top and $j$\-th column from the left is painted black if $S_{i,j}$ is `#`, and white if $S_{i,j}$ is `.`.

有一个 $H$ 行 $W$ 列的网格。
从上往下第 $i$ 行、从左往右第 $j$ 列的单元格，如果 $S_{i,j}$ 为 `#` 则被涂为黑色，如果 $S_{i,j}$ 为 `.` 则被涂为白色。

---

Among the four-directionally connected regions consisting of white cells, find the number of those that are surrounded by black cells.

在所有由白色单元格组成的四连通区域中，统计被黑色单元格包围的区域的数量。

---

Below is a more formal statement.

以下是更正式的题面描述。

---

We denote the cell at the $i$\-th row from the top and $j$\-th column from the left as cell $(i, j)$.  
Two cells $(i, j)$ and $(i', j')$ are said to be adjacent if and only if $|i-i'|+|j-j'|=1$.  
A set $C$ of white cells is said to be connected if and only if, for any two cells $c$ and $c'$ in $C$, it is possible to move from $c$ to $c'$ by repeatedly moving to an adjacent cell in $C$.  
A non-empty connected set of white cells that is maximal is called a connected component of white cells.  
Find the number of connected components of white cells that do not contain any cell on the outermost border of the grid (that is, in row $1$, row $H$, column $1$, or column $W$).

我们将从上往下第 $i$ 行、从左往右第 $j$ 列的单元格记为单元格 $(i, j)$。
两个单元格 $(i, j)$ 和 $(i', j')$ 相邻当且仅当 $|i-i'|+|j-j'|=1$。
一个白色单元格构成的集合 $C$ 被称为连通的，当且仅当对于 $C$ 中的任意两个单元格 $c$ 和 $c'$，可以通过在 $C$ 中反复移动到相邻单元格的方式，从 $c$ 到达 $c'$。
非空的极大白色单元格连通集合称为白色单元格的连通分量。
统计不包含任何网格最外层边界上的单元格（即第 $1$ 行、第 $H$ 行、第 $1$ 列或第 $W$ 列）的白色连通分量的数量。

---

### Constraints

-   $3 \leq H, W \leq 10^3$
-   $H$ and $W$ are integers.
-   $S_{i,j}$ is `#` or `.`.

-   $3 \leq H, W \leq 10^3$
-   $H$ 和 $W$ 是整数。
-   $S_{i,j}$ 是 `#` 或 `.`。

---

### Input

The input is given from Standard Input in the following format:

输入以如下格式从标准输入给出：

$H$ $W$  
$S_{1,1}S_{1,2}\dots S_{1,W}$  
$\vdots$  
$S_{H,1}S_{H,2}\dots S_{H,W}$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
5 15
##########..###
#...#######.###
####....###..##
######.########
########....###
```

---

### Sample Output 1

```text
2
```

---

There are two such regions: the region consisting of the three cells in row $2$ from the top and columns $2, 3, 4$ from the left, and the region consisting of a total of five cells: columns $5, 6, 7, 8$ from the left in row $3$ from the top and column $7$ from the left in row $4$ from the top.

共有两个这样的区域：一个是由从上往下第 $2$ 行、从左往右第 $2, 3, 4$ 列的三个单元格组成的区域；另一个区域共包含五个单元格，分别是从上往下第 $3$ 行、从左往右第 $5, 6, 7, 8$ 列的单元格，以及从上往下第 $4$ 行、从左往右第 $7$ 列的单元格。

---

### Sample Input 2

```text
10 22
######################
####.#################
###...################
##.###.##.....########
##.....##.####.#######
.######.#......#.....#
.######.#.####.#.#####
#########.....##.#####
################.#####
################.....#
```

---

### Sample Output 2

```text
4
```
