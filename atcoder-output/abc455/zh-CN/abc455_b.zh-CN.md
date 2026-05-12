# B - Spiral Galaxy

分值：$200200200$ 分

---

### Problem Statement

There is a grid with $HHH$ rows and $WWW$ columns. The cell at the $iii$\-th row from the top and $jjj$\-th column from the left is denoted as cell $(i,j)(i, j)(i,j)$.

有一个 $HHH$ 行 $WWW$ 列的网格。从上往下第 $iii$ 行、从左往右第 $jjj$ 列的单元格记为 $(i,j)(i, j)(i,j)$。

---

Each cell of the grid is colored white or black. The information of the grid is given by $HHH$ strings $S1,S2,…,SHS_1, S_2, \ldots, S_HS1​,S2​,…,SH​$ each of length $WWW$: cell $(i,j)(i, j)(i,j)$ is white if the $jjj$\-th character of $SiS_iSi​$ is `.`, and black if it is `#`.

网格的每个单元格被染为白色或黑色。网格的信息由 $HHH$ 个长度为 $WWW$ 的字符串 $S1,S2,…,SHS_1, S_2, \ldots, S_HS1​,S2​,…,SH​$ 给出：若 $SiS_iSi​$ 的第 $jjj$ 个字符为 `.`，则单元格 $(i,j)(i, j)(i,j)$ 为白色，若为 `#` 则为黑色。

---

Find the number of rectangular regions of the grid that are point-symmetrically colored.

求网格中满足染色是中心对称的矩形区域的数量。

---

More formally, find the number of integer tuples $(h1,h2,w1,w2)(h_1, h_2, w_1, w_2)(h1​,h2​,w1​,w2​)$ satisfying all of the following conditions:

更正式地，求满足以下所有条件的整数元组 $(h1,h2,w1,w2)(h_1, h_2, w_1, w_2)(h1​,h2​,w1​,w2​)$ 的数量：

---

-   $1≤h1≤h2≤H1 \leq h_1 \leq h_2 \leq H1≤h1​≤h2​≤H$
-   $1≤w1≤w2≤W1 \leq w_1 \leq w_2 \leq W1≤w1​≤w2​≤W$
-   For all integers $i,ji, ji,j$ satisfying $h1≤i≤h2h_1 \leq i \leq h_2h1​≤i≤h2​$ and $w1≤j≤w2w_1 \leq j \leq w_2w1​≤j≤w2​$, cell $(i,j)(i, j)(i,j)$ and cell $(h1+h2−i,w1+w2−j)(h_1 + h_2 - i, w_1 + w_2 - j)(h1​+h2​−i,w1​+w2​−j)$ have the same color.

-   $1≤h1≤h2≤H1 \leq h_1 \leq h_2 \leq H1≤h1​≤h2​≤H$
-   $1≤w1≤w2≤W1 \leq w_1 \leq w_2 \leq W1≤w1​≤w2​≤W$
-   对所有满足 $h1≤i≤h2h_1 \leq i \leq h_2h1​≤i≤h2​$ 和 $w1≤j≤w2w_1 \leq j \leq w_2w1​≤j≤w2​$ 的整数 $i,ji, ji,j$，单元格 $(i,j)(i, j)(i,j)$ 和单元格 $(h1+h2−i,w1+w2−j)(h_1 + h_2 - i, w_1 + w_2 - j)(h1​+h2​−i,w1​+w2​−j)$ 颜色相同。

---

### Constraints

-   $1≤H,W≤101 \leq H, W \leq 101≤H,W≤10$
-   $HHH$ and $WWW$ are integers.
-   $SiS_iSi​$ is a string of length $WWW$ consisting of `.` and `#`.

-   $1≤H,W≤101 \leq H, W \leq 101≤H,W≤10$
-   $HHH$ 和 $WWW$ 是整数。
-   $SiS_iSi​$ 是长度为 $WWW$ 的字符串，由 `.` 和 `#` 组成。

---

### Input

The input is given from Standard Input in the following format:

输入按以下格式从标准输入给出：

$HHH$ $WWW$  
$S1S_1S1​$  
$S2S_2S2​$  
$⋮\vdots⋮$  
$SHS_HSH​$

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

As shown in the figure above, the answer is $101010$.

如上图所示，答案为 $101010$。

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
