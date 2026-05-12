# B - Spiral Galaxy

分值：$200$ 分

---

### Problem Statement

There is a grid with $H$ rows and $W$ columns. The cell at the $i$\-th row from the top and $j$\-th column from the left is denoted as cell $(i, j)$.

有一个包含 $H$ 行和 $W$ 列的网格。从上往下第 $i$ 行、从左往右第 $j$ 列的单元格记为 $(i, j)$。

---

Each cell of the grid is colored white or black. The information of the grid is given by $H$ strings $S_1, S_2, \ldots, S_H$ each of length $W$: cell $(i, j)$ is white if the $j$\-th character of $S_i$ is `.`, and black if it is `#`.

网格的每个单元格被染为黑色或白色。网格的信息由 $H$ 个长度为 $W$ 的字符串 $S_1, S_2, \ldots, S_H$ 给出：若 $S_i$ 的第 $j$ 个字符为 `.`，则单元格 $(i, j)$ 是白色；若为 `#` 则是黑色。

---

Find the number of rectangular regions of the grid that are point-symmetrically colored.

求网格中满足颜色中心对称的矩形区域的数量。

---

More formally, find the number of integer tuples $(h_1, h_2, w_1, w_2)$ satisfying all of the following conditions:

更正式地，求满足以下所有条件的整数元组 $(h_1, h_2, w_1, w_2)$ 的数量：

---

-   $1 \leq h_1 \leq h_2 \leq H$
-   $1 \leq w_1 \leq w_2 \leq W$
-   For all integers $i, j$ satisfying $h_1 \leq i \leq h_2$ and $w_1 \leq j \leq w_2$, cell $(i, j)$ and cell $(h_1 + h_2 - i, w_1 + w_2 - j)$ have the same color.

-   $1 \leq h_1 \leq h_2 \leq H$
-   $1 \leq w_1 \leq w_2 \leq W$
-   对于所有满足 $h_1 \leq i \leq h_2$ 和 $w_1 \leq j \leq w_2$ 的整数 $i, j$，单元格 $(i, j)$ 和单元格 $(h_1 + h_2 - i, w_1 + w_2 - j)$ 颜色相同。

---

### Constraints

-   $1 \leq H, W \leq 10$
-   $H$ and $W$ are integers.
-   $S_i$ is a string of length $W$ consisting of `.` and `#`.

-   $1 \leq H, W \leq 10$
-   $H$ 和 $W$ 是整数。
-   $S_i$ 是一个长度为 $W$、由 `.` 和 `#` 组成的字符串。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$H$ $W$  
$S_1$  
$S_2$  
$\vdots$  
$S_H$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
3 2
.#
#.
##
```

---

### Sample Output 1

```text
10
```

---

![](https://img.atcoder.jp/abc455/b5fd99061ef5ae0708d54785dde2ed84.png)

![](https://img.atcoder.jp/abc455/b5fd99061ef5ae0708d54785dde2ed84.png)

---

As shown in the figure above, the answer is $10$.

如上图所示，答案为 $10$。

---

### Sample Input 2

```text
4 5
.#.#.
####.
##..#
....#
```

---

### Sample Output 2

```text
54
```
