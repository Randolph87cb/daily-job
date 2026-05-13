# D - Go Straight

Source: https://atcoder.jp/contests/abc453/tasks/abc453_d?lang=en

Score : $425$ points

### Problem Statement

There is a grid of $H$ rows $\times$ $W$ columns, and Takahashi moves through this grid up, down, left, and right.  
The state of the cell at the $i$\-th row from the top and $j$\-th column from the left $(1\leq i\leq H, 1\leq j\leq W)$ is represented by the character $S_{i,j}$.  
$S_{i,j}$ is one of `#`, `.`, `o`, `x`, `S`, `G`.

-   If $S_{i,j}=$`#`: This cell cannot be entered.
-   If $S_{i,j}=$`.`: This cell can be freely entered and exited. That is, after entering this cell, Takahashi can move to any adjacent cell (if it exists) in the up, down, left, or right direction.
-   If $S_{i,j}=$`o`: In this cell, **Takahashi must move in the same direction as the immediately preceding move**. That is, after entering this cell, he must move to the next cell without changing direction.
-   If $S_{i,j}=$`x`: In this cell, **Takahashi cannot move in the same direction as the immediately preceding move**. That is, after entering this cell, he must change direction to move to the next cell. Turning $180$ degrees to return to the previous cell is considered as changing direction.
-   If $S_{i,j}=$`S`: This cell is Takahashi's starting position. This cell can be freely entered and exited.
-   If $S_{i,j}=$`G`: This cell is Takahashi's destination. This cell can be freely entered and exited.

There is exactly one $(i,j)$ with $1\leq i\leq H, 1\leq j\leq W$ satisfying $S_{i,j}=$`S`, and exactly one satisfying $S_{i,j}=$`G`.

Takahashi wants to reach the destination by repeatedly moving to adjacent cells up, down, left, or right from his starting position.  
Determine whether this is possible, and if so, output one valid sequence of moves with at most $5\times 10^6$ moves between adjacent cells.  
It can be proved that if a valid sequence of moves exists under the problem's conditions, then there exists one with at most $5\times 10^6$ moves.  
As long as the number of moves is at most $5\times 10^6$, it is not necessary to minimize the number of moves.

### Constraints

-   $1 \leq H,W\leq 1000$
-   $S_{i,j}$ is one of `#`, `.`, `o`, `x`, `S`, `G`.
-   There is exactly one $(i,j)$ satisfying $S_{i,j}=$`S` and exactly one satisfying $S_{i,j}=$`G`.
-   $H$ and $W$ are integers.

### Input

The input is given from Standard Input in the following format:

```text
$H$ $W$
$S_{1,1} S_{1,2} \ldots S_{1,W}$
$S_{2,1} S_{2,2} \ldots S_{2,W}$
$\vdots$
$S_{H,1} S_{H,2} \ldots S_{H,W}$
```

### Output

If it is impossible to reach the destination while satisfying the conditions, output `No` on the first line, and nothing on the second line.  
If it is possible to reach the destination while satisfying the conditions, output `Yes` on the first line.  
On the second line, output a string $T$ representing a sequence of moves. $T$ must satisfy all of the following conditions.

-   The length $\lvert T\rvert$ of $T$ is between $1$ and $5\times 10^6$, inclusive.
-   Each character of $T$ is one of `U`, `D`, `L`, `R`.
    -   The $i$\-th character of $T$ being `U`, `D`, `L`, `R` means that in the $i$\-th move after departing, Takahashi moves to the adjacent cell above, below, to the left, or to the right, respectively.
-   For $1\leq i\leq \lvert T\rvert$, Takahashi is not outside the grid after the $i$\-th move.
-   During the moves, the conditions of each cell are not violated.
-   After the $\lvert T\rvert$\-th move, Takahashi is at the destination cell. As long as this condition is satisfied, he may pass through the destination cell before the $\lvert T\rvert$\-th move.

### Sample Input 1

```text
3 5
.#...
.Sooo
..x.G
```

### Sample Output 1

```text
Yes
DRUUDDRR
```

Let cell $(i,j)$ denote the cell at the $i$\-th row from the top and $j$\-th column from the left.  
Following the sample output, the path goes: cell $(2,2)$ $\to$ cell $(3,2)$ $\to$ cell $(3,3)$ $\to$ cell $(2,3)$ $\to$ cell $(1,3)$ $\to$ cell $(2,3)$ $\to$ cell $(3,3)$ $\to$ cell $(3,4)$ $\to$ cell $(3,5)$, reaching the destination.  
Other solutions such as `DRUURLRRDD` are also accepted. On the other hand, since Takahashi cannot go straight through cell $(3,3)$, solutions such as `DRRR` are not accepted.

### Sample Input 2

```text
3 3
#So
xoG
..#
```

### Sample Output 2

```text
Yes
DDLURR
```

### Sample Input 3

```text
2 2
So
oG
```

### Sample Output 3

```text
No
```

It is impossible to reach the destination while satisfying the conditions.
