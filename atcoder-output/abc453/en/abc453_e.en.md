# E - Team Division

Source: https://atcoder.jp/contests/abc453/tasks/abc453_e?lang=en

Score : $475$ points

### Problem Statement

Divide $N$ players, player $1$, player $2$, $\ldots$, player $N$, into two (distinguishable) teams $A$ and $B$ satisfying all of the following conditions.

-   Each team consists of at least one player.
-   Each player belongs to either team $A$ or team $B$, but not both.
-   The number of players in the team that player $i$ belongs to is at least $L_i$ and at most $R_i$.

Find the number of ways to divide the players satisfying the conditions, and output the count modulo $998244353$.  
Two divisions are considered different if there exists a player who belongs to different teams in the two divisions.

### Constraints

-   $2\leq N\leq 2\times 10^5$
-   $1\leq L_i\leq R_i\leq N-1$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$L_1$ $R_1$
$L_2$ $R_2$
$\vdots$
$L_N$ $R_N$
```

### Output

Output the number of valid divisions, modulo $998244353$.

### Sample Input 1

```text
3
1 1
1 2
2 2
```

### Sample Output 1

```text
2
```

The following two divisions satisfy the conditions.

-   Player $1$: Team $A$, Player $2$: Team $B$, Player $3$: Team $B$
-   Player $1$: Team $B$, Player $2$: Team $A$, Player $3$: Team $A$

Since $2$ modulo $998244353$ is $2$, output $2$.

### Sample Input 2

```text
6
1 5
1 5
2 5
1 3
3 5
2 5
```

### Sample Output 2

```text
30
```

There are $30$ valid divisions.
