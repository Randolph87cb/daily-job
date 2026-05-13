# E - Team Division

分值：$475$ 分

---

### Problem Statement

Divide $N$ players, player $1$, player $2$, $\ldots$, player $N$, into two (distinguishable) teams $A$ and $B$ satisfying all of the following conditions.

将 $N$ 名选手（选手 $1$、选手 $2$、$\ldots$、选手 $N$）分成两个**可区分**的队伍 $A$ 和 $B$，满足以下所有条件。

---

-   Each team consists of at least one player.
-   Each player belongs to either team $A$ or team $B$, but not both.
-   The number of players in the team that player $i$ belongs to is at least $L_i$ and at most $R_i$.

- 每支队伍至少包含一名选手。
- 每名选手属于队伍 $A$ 或队伍 $B$ 中的恰好一个，不能同时属于两个队伍。
- 选手 $i$ 所在的队伍的选手人数至少为 $L_i$，至多为 $R_i$。

---

Find the number of ways to divide the players satisfying the conditions, and output the count modulo $998244353$.  
Two divisions are considered different if there exists a player who belongs to different teams in the two divisions.

求满足条件的选手分队方案数，结果对 $998244353$ 取模后输出。
如果存在至少一名选手在两种分队方案中属于不同的队伍，则认为这两种分队方案是不同的。

---

### Constraints

-   $2\leq N\leq 2\times 10^5$
-   $1\leq L_i\leq R_i\leq N-1$
-   All input values are integers.

- $2\leq N\leq 2\times 10^5$
- $1\leq L_i\leq R_i\leq N-1$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$L_1$ $R_1$  
$L_2$ $R_2$  
$\vdots$  
$L_N$ $R_N$

---

### Output

Output the number of valid divisions, modulo $998244353$.

输出合法的分队方案数，对 $998244353$ 取模。

---

### Sample Input 1

```text
3
1 1
1 2
2 2
```

---

### Sample Output 1

```text
2
```

---

The following two divisions satisfy the conditions.

以下两种分队方案满足条件。

---

-   Player $1$: Team $A$, Player $2$: Team $B$, Player $3$: Team $B$
-   Player $1$: Team $B$, Player $2$: Team $A$, Player $3$: Team $A$

- 选手 $1$：队伍 $A$，选手 $2$：队伍 $B$，选手 $3$：队伍 $B$
- 选手 $1$：队伍 $B$，选手 $2$：队伍 $A$，选手 $3$：队伍 $A$

---

Since $2$ modulo $998244353$ is $2$, output $2$.

由于 $2$ 模 $998244353$ 的结果是 $2$，输出 $2$。

---

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

---

### Sample Output 2

```text
30
```

---

There are $30$ valid divisions.

共有 $30$ 种合法的分队方案。
