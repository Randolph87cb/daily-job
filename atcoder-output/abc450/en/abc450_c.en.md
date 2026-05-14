# C - Puddles

Source: https://atcoder.jp/contests/abc450/tasks/abc450_c?lang=en

Score : $300$ points

### Problem Statement

There is a grid with $H$ rows and $W$ columns.  
The cell at the $i$\-th row from the top and $j$\-th column from the left is painted black if $S_{i,j}$ is `#`, and white if $S_{i,j}$ is `.`.

Among the four-directionally connected regions consisting of white cells, find the number of those that are surrounded by black cells.

Below is a more formal statement.

We denote the cell at the $i$\-th row from the top and $j$\-th column from the left as cell $(i, j)$.  
Two cells $(i, j)$ and $(i', j')$ are said to be adjacent if and only if $|i-i'|+|j-j'|=1$.  
A set $C$ of white cells is said to be connected if and only if, for any two cells $c$ and $c'$ in $C$, it is possible to move from $c$ to $c'$ by repeatedly moving to an adjacent cell in $C$.  
A non-empty connected set of white cells that is maximal is called a connected component of white cells.  
Find the number of connected components of white cells that do not contain any cell on the outermost border of the grid (that is, in row $1$, row $H$, column $1$, or column $W$).

### Constraints

-   $3 \leq H, W \leq 10^3$
-   $H$ and $W$ are integers.
-   $S_{i,j}$ is `#` or `.`.

### Input

The input is given from Standard Input in the following format:

```text
$H$ $W$
$S_{1,1}S_{1,2}\dots S_{1,W}$
$\vdots$
$S_{H,1}S_{H,2}\dots S_{H,W}$
```

### Output

Output the answer.

### Sample Input 1

```text
5 15
##########..###
#...#######.###
####....###..##
######.########
########....###
```

### Sample Output 1

```text
2
```

There are two such regions: the region consisting of the three cells in row $2$ from the top and columns $2, 3, 4$ from the left, and the region consisting of a total of five cells: columns $5, 6, 7, 8$ from the left in row $3$ from the top and column $7$ from the left in row $4$ from the top.

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

### Sample Output 2

```text
4
```
