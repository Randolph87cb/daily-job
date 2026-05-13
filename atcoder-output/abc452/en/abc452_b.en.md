# B - Draw Frame

Source: https://atcoder.jp/contests/abc452/tasks/abc452_b?lang=en

Score : $200$ points

### Problem Statement

There is a grid with $H$ rows and $W$ columns. Takahashi is going to paint each cell of this grid black or white.

He paints all cells on the border of the grid black, and all other cells white. Output the grid after he has painted it.

**More formally**

There is an $H\times W$ grid.

We call the cell at the $i$\-th row from the top $(1\le i\le H)$ and the $j$\-th column from the left $(1\le j\le W)$ cell $(i,j)$.

Cell $(i,j)\ (1\le i\le H,1\le j\le W)$ and cell $(k,l)\ (1\le k\le H,1\le l\le W)$ are said to be **edge-adjacent** if and only if $|i-k|+|j-l|=1$.

Cell $(i,j)$ is said to be **on the border** if and only if the number of cells edge-adjacent to cell $(i,j)$ is at most $3$.

Find $H$ strings $S _ 1,S _ 2,\ldots,S _ H$ satisfying the following condition.

-   $S _ i$ is a string of length $W$, and the $j$\-th character of $S _ i$ is `#` if cell $(i,j)$ is on the border, and `.` otherwise.

### Constraints

-   $3\le H\le10$
-   $3\le W\le10$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$H$ $W$
```

### Output

Output $H$ lines, each a string of length $W$. The $j$\-th character $(1\le j\le W)$ of the $i$\-th line $(1\le i\le H)$ should be `#` if cell $(i,j)$ is painted black, and `.` if it is painted white.

### Sample Input 1

```text
4 5
```

### Sample Output 1

```text
#####
#...#
#...#
#####
```

For example, cell $(1,1)$ is on the border. This is because there are only two cells edge-adjacent to cell $(1,1)$: cells $(1,2)$ and $(2,1)$. Thus, cell $(1,1)$ is painted black, so the first character of the first line should be `#`.

Conversely, for example, cell $(3,4)$ is not on the border. This is because there are four cells edge-adjacent to cell $(3,4)$: cells $(2,4),$ $(3,3),$ $(3,5),$ and $(4,4)$. Thus, cell $(3,4)$ is painted white, so the fourth character of the third line should be `.`.

### Sample Input 2

```text
5 6
```

### Sample Output 2

```text
######
#....#
#....#
#....#
######
```
