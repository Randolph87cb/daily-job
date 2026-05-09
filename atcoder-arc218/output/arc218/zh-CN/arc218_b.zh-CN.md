# B - All Minus

分值：$400$ 分

---

### Problem Statement

There are $N$ non-negative integers $A_1,A_2,\dots,A_N$ written on a blackboard.

黑板上写有 $N$ 个非负整数 $A_1,A_2,\dots,A_N$。

---

Alice and Bob play a game. Starting with Alice, they alternately perform the following operation, and the player who reduces the number of integers written on the blackboard to $0$ wins.

Alice 和 Bob 在玩一个游戏。从 Alice 开始，两人轮流执行以下操作，将黑板上的整数数量减少到 $0$ 的玩家获胜。

---

-   Let $m$ be the minimum non-negative integer currently written on the blackboard.
    -   If $m > 0$, choose a positive integer $x$ between $1$ and $m$, inclusive. Replace every integer written on the blackboard with its current value minus $x$.
    -   If $m = 0$, erase one or more of the $0$s written on the blackboard.

- 设 $m$ 是当前黑板上写的最小非负整数。
- 如果 $m > 0$，选择一个介于 $1$ 和 $m$ 之间（含两端）的正整数 $x$。将黑板上的每个整数都减去 $x$。
- 如果 $m = 0$，擦去黑板上一个或多个 $0$。

---

Determine who wins when both players play optimally to win.

假设双方都采取最优策略，判断谁会获胜。

---

$T$ test cases are given; solve each of them.

共有 $T$ 组测试数据，对于每组数据给出答案。

---

### Constraints

-   $1 \le T \le 2 \times 10^5$
-   $1 \le N \le 2 \times 10^5$
-   $0 \le A_i \le 10^9$
-   The sum of $N$ over all test cases is at most $2 \times 10^5$.
-   All input values are integers.

- $1 \le T \le 2 \times 10^5$
- $1 \le N \le 2 \times 10^5$
- $0 \le A_i \le 10^9$
- 所有测试数据的 $N$ 之和不超过 $2 \times 10^5$。
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按以下格式从标准输入给出：

$T$  
$\mathrm{case}_1$  
$\mathrm{case}_2$  
$\vdots$  
$\mathrm{case}_T$

---

Each test case is given in the following format:

每组测试数据按以下格式给出：

$N$  
$A_1$ $A_2$ $\dots$ $A_N$

---

### Output

Output $T$ lines. The $i$\-th line should contain `Alice` if Alice wins in $\mathrm{case}_i$, or `Bob` if Bob wins.

输出 $T$ 行。第 $i$ 行中，若第 $\mathrm{case}_i$ 组测试数据 Alice 获胜则输出 `Alice`，Bob 获胜则输出 `Bob`。

---

### Sample Input 1

```text
5
1
2
3
1 1 1
4
1 2 3 4
7
3 1 4 1 5 9 2
3
218 503 2026
```

---

### Sample Output 1

```text
Alice
Bob
Bob
Bob
Alice
```

---

For the first test case, one possible game progression is as follows:

对于第一组测试数据，一种可能的游戏过程如下：

---

-   Initially, $2$ is written on the blackboard.
-   Alice chooses $x = 1$. Now $1$ is written on the blackboard.
-   Bob chooses $x = 1$. Now $0$ is written on the blackboard.
-   Alice chooses and erases one $0$. Now nothing is written on the blackboard.

- 初始时，黑板上写有 $2$。
- Alice 选择 $x = 1$，现在黑板上写有 $1$。
- Bob 选择 $x = 1$，现在黑板上写有 $0$。
- Alice 选择并擦去一个 $0$，现在黑板上没有数字了。

---

When both players play optimally to win, Alice wins.

当双方都采取最优策略时，Alice 获胜。

---

For the second test case, one possible game progression is as follows:

对于第二组测试数据，一种可能的游戏过程如下：

---

-   Initially, $1,1,1$ are written on the blackboard.
-   Alice chooses $x = 1$. Now $0,0,0$ are written on the blackboard.
-   Bob chooses and erases one $0$. Now $0,0$ are written on the blackboard.
-   Alice chooses and erases one $0$. Now $0$ is written on the blackboard.
-   Bob chooses and erases one $0$. Now nothing is written on the blackboard.

- 初始时，黑板上写有 $1,1,1$。
- Alice 选择 $x = 1$，现在黑板上写有 $0,0,0$。
- Bob 选择并擦去一个 $0$，现在黑板上写有 $0,0$。
- Alice 选择并擦去一个 $0$，现在黑板上写有 $0$。
- Bob 选择并擦去一个 $0$，现在黑板上没有数字了。

---

When both players play optimally to win, Bob wins.

当双方都采取最优策略时，Bob 获胜。
