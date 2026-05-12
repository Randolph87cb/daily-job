# B - Spiral Galaxy

Source: https://atcoder.jp/contests/abc455/tasks/abc455_b?lang=en

Score : $200$ points

### Problem Statement

There is a grid with $H$ rows and $W$ columns. The cell at the $i$\-th row from the top and $j$\-th column from the left is denoted as cell $(i, j)$.

Each cell of the grid is colored white or black. The information of the grid is given by $H$ strings $S_1, S_2, \ldots, S_H$ each of length $W$: cell $(i, j)$ is white if the $j$\-th character of $S_i$ is `.`, and black if it is `#`.

Find the number of rectangular regions of the grid that are point-symmetrically colored.

More formally, find the number of integer tuples $(h_1, h_2, w_1, w_2)$ satisfying all of the following conditions:

-   $1 \leq h_1 \leq h_2 \leq H$
-   $1 \leq w_1 \leq w_2 \leq W$
-   For all integers $i, j$ satisfying $h_1 \leq i \leq h_2$ and $w_1 \leq j \leq w_2$, cell $(i, j)$ and cell $(h_1 + h_2 - i, w_1 + w_2 - j)$ have the same color.

### Constraints

-   $1 \leq H, W \leq 10$
-   $H$ and $W$ are integers.
-   $S_i$ is a string of length $W$ consisting of `.` and `#`.

### Input

The input is given from Standard Input in the following format:

```text
$H$ $W$
$S_1$
$S_2$
$\vdots$
$S_H$
```

### Output

Output the answer.

### Sample Input 1

```text
3 2
.#
#.
##
```

### Sample Output 1

```text
10
```

![](https://img.atcoder.jp/abc455/b5fd99061ef5ae0708d54785dde2ed84.png)

As shown in the figure above, the answer is $10$.

### Sample Input 2

```text
4 5
.#.#.
####.
##..#
....#
```

### Sample Output 2

```text
54
```
