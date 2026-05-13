# C - Fishbones

Source: https://atcoder.jp/contests/abc452/tasks/abc452_c?lang=en

Score : $300$ points

### Problem Statement

Artist Takasago has created an object in the shape of a fish skeleton.

The object consists of $N$ ribs and one spine. The ribs are numbered $1$ through $N$.

He wants to write one string on each of the $N+1$ bones, satisfying all of the following conditions.

-   The length of the string written on the spine is $N$.
-   For each rib $i = 1, \dots, N$, the following hold.
    -   The length of the string written on rib $i$ is $A_i$.
    -   The $B_i$\-th character of the string written on rib $i$ equals the $i$\-th character of the string written on the spine.
-   Each of the strings written on the $N+1$ bones is one of $S_1, \cdots, S_M$ (duplicates allowed).

$S_1, \cdots, S_M$ are strings consisting of lowercase English letters, and they are all distinct.

For each $j = 1, \cdots, M$, answer the following question.

-   Among the ways to write strings satisfying the conditions, is there one where the string written on the spine is $S_j$?

### Constraints

-   $N$ is an integer.
-   $1 \leq N \leq 10$
-   $A_i$ and $B_i$ are integers. ($1 \leq i \leq N$)
-   $1 \leq B_i \leq A_i \leq 10$ ($1 \leq i \leq N$)
-   $M$ is an integer.
-   $1 \leq M \leq 200\,000$
-   $S_j$ is a string consisting of lowercase English letters. ($1 \leq j \leq M$)
-   $1 \leq |S_j| \leq 10$ ($1 \leq j \leq M$)
-   $S_1, \cdots, S_M$ are pairwise distinct.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$A_1$ $B_1$
$\vdots$
$A_N$ $B_N$
$M$
$S_1$
$\vdots$
$S_M$
```

### Output

Output $M$ lines.

The $j$\-th line ($1 \leq j \leq M$) should contain `Yes` if there exists a way to write strings satisfying the conditions with $S_j$ written on the spine, and `No` otherwise.

### Sample Input 1

```text
5
5 3
5 2
4 1
5 1
3 2
8
retro
chris
itchy
tuna
crab
rock
cod
ash
```

### Sample Output 1

```text
Yes
Yes
No
No
No
No
No
No
```

By writing `chris`, `retro`, `tuna`, `retro`, `cod` on ribs $1,2,3,4,5$ respectively, the conditions are satisfied with `retro` written on the spine.

![](https://img.atcoder.jp/abc452/28d388773281d2bb1e90cd50063b6539.png)

-   The length of `retro` is $5$.
-   For each rib, the following hold.
    -   The string written on rib $1$ is `chris`, which has length $5$. Its third character is `r`, which equals the first character of `retro`.
    -   The string written on rib $2$ is `retro`, which has length $5$. Its second character is `e`, which equals the second character of `retro`.
    -   The string written on rib $3$ is `tuna`, which has length $4$. Its first character is `t`, which equals the third character of `retro`.
    -   The string written on rib $4$ is `retro`, which has length $5$. Its first character is `r`, which equals the fourth character of `retro`.
    -   The string written on rib $5$ is `cod`, which has length $3$. Its second character is `o`, which equals the fifth character of `retro`.

By writing `itchy`, `chris`, `rock`, `itchy`, `ash` on ribs $1,2,3,4,5$ respectively, the conditions are satisfied with `chris` written on the spine.

![](https://img.atcoder.jp/abc452/5323501d2dc7ce95e9216d1c20484be5.png)

### Sample Input 2

```text
5
5 1
5 2
5 3
5 4
5 5
8
retro
chris
itchy
tuna
crab
rock
cod
ash
```

### Sample Output 2

```text
Yes
Yes
Yes
No
No
No
No
No
```
