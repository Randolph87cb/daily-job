# B - Spiral Galaxy

Source: https://atcoder.jp/contests/abc455/tasks/abc455_b?lang=en

Score : $200200200$ points

### Problem Statement

There is a grid with $HHH$ rows and $WWW$ columns. The cell at the $iii$\-th row from the top and $jjj$\-th column from the left is denoted as cell $(i,j)(i, j)(i,j)$.

Each cell of the grid is colored white or black. The information of the grid is given by $HHH$ strings $S1,S2,…,SHS_1, S_2, \ldots, S_HS1​,S2​,…,SH​$ each of length $WWW$: cell $(i,j)(i, j)(i,j)$ is white if the $jjj$\-th character of $SiS_iSi​$ is `.`, and black if it is `#`.

Find the number of rectangular regions of the grid that are point-symmetrically colored.

More formally, find the number of integer tuples $(h1,h2,w1,w2)(h_1, h_2, w_1, w_2)(h1​,h2​,w1​,w2​)$ satisfying all of the following conditions:

-   $1≤h1≤h2≤H1 \leq h_1 \leq h_2 \leq H1≤h1​≤h2​≤H$
-   $1≤w1≤w2≤W1 \leq w_1 \leq w_2 \leq W1≤w1​≤w2​≤W$
-   For all integers $i,ji, ji,j$ satisfying $h1≤i≤h2h_1 \leq i \leq h_2h1​≤i≤h2​$ and $w1≤j≤w2w_1 \leq j \leq w_2w1​≤j≤w2​$, cell $(i,j)(i, j)(i,j)$ and cell $(h1+h2−i,w1+w2−j)(h_1 + h_2 - i, w_1 + w_2 - j)(h1​+h2​−i,w1​+w2​−j)$ have the same color.

### Constraints

-   $1≤H,W≤101 \leq H, W \leq 101≤H,W≤10$
-   $HHH$ and $WWW$ are integers.
-   $SiS_iSi​$ is a string of length $WWW$ consisting of `.` and `#`.

### Input

The input is given from Standard Input in the following format:

```text
$HHH$ $WWW$
$S1S_1S1​$
$S2S_2S2​$
$⋮\vdots⋮$
$SHS_HSH​$
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

As shown in the figure above, the answer is $101010$.

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
