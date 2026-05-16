# B - Count Adjacent Cells

Source: https://atcoder.jp/contests/abc458/tasks/abc458_b?lang=en

Score : $200$ points

### Problem Statement

There is a grid with $H$ rows and $W$ columns. The cell at the $i$\-th row from the top and the $j$\-th column from the left is denoted as cell $(i, j)$.

Cells $(x_1, y_1)$ and $(x_2, y_2)$ are said to be **edge-adjacent** when $|x_1 - x_2| + |y_1 - y_2| = 1$.

For every cell, find the number of cells that are edge-adjacent to it.

### Constraints

-   $1 \leq H, W \leq 50$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$H$ $W$
```

### Output

Output the answer in the following format:

```text
$x_{1,1}$ $x_{1,2}$ $\cdots$ $x_{1,W}$
$x_{2,1}$ $x_{2,2}$ $\cdots$ $x_{2,W}$
$\vdots$
$x_{H,1}$ $x_{H,2}$ $\cdots$ $x_{H,W}$
```

Here, $x_{i,j}$ represents the number of cells that are edge-adjacent to cell $(i, j)$.

### Sample Input 1

```text
4 5
```

### Sample Output 1

```text
2 3 3 3 2
3 4 4 4 3
3 4 4 4 3
2 3 3 3 2
```

The cells edge-adjacent to cell $(1, 5)$ are cells $(1, 4), (2, 5)$, for a total of two cells.

The cells edge-adjacent to cell $(2, 3)$ are cells $(1, 3), (2, 2), (2, 4), (3, 3)$, for a total of four cells.

The cells edge-adjacent to cell $(4, 2)$ are cells $(3, 2), (4, 1), (4, 3)$, for a total of three cells.

### Sample Input 2

```text
1 1
```

### Sample Output 2

```text
0
```

There are no cells edge-adjacent to cell $(1, 1)$.

### Sample Input 3

```text
12 8
```

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
