# E - Endless Holidays

分值：$450$ 分

---

### Problem Statement

The Kingdom of AtCoder has $N$ cities, called city $1,2,\dots,N$. There are $M$ bidirectional roads connecting pairs of cities, where the $i$\-th road connects cities $U_i$ and $V_i$. Any pair of cities can be reached from each other by traversing some roads.

AtCoder 王国有 $N$ 座城市，编号为 $1,2,\dots,N$。共有 $M$ 条双向道路连接城市对，其中第 $i$ 条道路连接城市 $U_i$ 和 $V_i$。任意两座城市都可以通过若干条道路互相到达。

---

In the Kingdom of AtCoder, a week consists of $W$ days. A week proceeds through days $1,2,\dots,W$, and the day after day $W$ is day $1$.

在 AtCoder 王国，一周包含 $W$ 天，按顺序为 $1,2,\dots,W$，且第 $W$ 天的下一天是第 $1$ 天。

---

Each city has certain days of the week that are holidays. The holiday information for city $i$ is given as a string $S_i$ of length $W$: if the $j$\-th character of $S_i$ is `o`, day $j$ is a holiday; if it is `x`, day $j$ is a weekday.

每座城市在一周中有固定的休息日。城市 $i$ 的休息日信息由一个长度为 $W$ 的字符串 $S_i$ 给出：若 $S_i$ 的第 $j$ 个字符为 `o`，则第 $j$ 天是休息日；若为 `x`，则第 $j$ 天是工作日。

---

Takahashi chooses a city he likes and visits it at noon on day $1$. Each night thereafter, he repeatedly chooses to either stay in his current city or move to a city directly connected by a road. Output `Yes` if it is possible for him to keep moving so that the city he is in at noon every day is a holiday, and `No` otherwise.

高桥选择一个他喜欢的城市，在第 $1$ 天的中午抵达该城市。之后每天晚上，他可以选择留在当前城市，或者移动到与当前城市直接有道路相连的城市。如果存在一种移动方式，使得他每天中午所在的城市当天都是休息日，则输出 `Yes`，否则输出 `No`。

---

$T$ test cases are given; solve each of them.

共有 $T$ 组测试数据，你需要对每组数据分别求解。

---

### Constraints

-   $1 \leq T \leq 10^5$
-   $1 \leq N \leq 10^5$
-   $N-1 \leq M \leq 10^5$
-   $1 \leq U_i \lt V_i \leq N$
-   Any pair of cities can be reached from each other by traversing some roads.
-   $2 \leq W \leq 10$
-   $T,N,M,U_i,V_i,W$ are integers.
-   $S_i$ is a string of length $W$ consisting of `o`, `x`.
-   The sum of $N$ over all test cases is at most $10^5$.
-   The sum of $M$ over all test cases is at most $10^5$.

-   $1 \leq T \leq 10^5$
-   $1 \leq N \leq 10^5$
-   $N-1 \leq M \leq 10^5$
-   $1 \leq U_i \lt V_i \leq N$
-   任意两座城市都可以通过若干条道路互相到达。
-   $2 \leq W \leq 10$
-   $T,N,M,U_i,V_i,W$ 是整数。
-   $S_i$ 是长度为 $W$ 的字符串，仅由 `o` 和 `x` 组成。
-   所有测试数据的 $N$ 之和不超过 $10^5$。
-   所有测试数据的 $M$ 之和不超过 $10^5$。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$T$  
$\mathrm{case}_1$  
$\mathrm{case}_2$  
$\vdots$  
$\mathrm{case}_T$

---

Here, $\mathrm{case}_i$ denotes the input for the $i$\-th test case. Each test case is given in the following format:

其中 $\mathrm{case}_i$ 表示第 $i$ 组测试数据的输入。每组测试数据按照以下格式给出：

$N$ $M$  
$U_1$ $V_1$  
$U_2$ $V_2$  
$\vdots$  
$U_M$ $V_M$  
$W$  
$S_1$  
$S_2$  
$\vdots$  
$S_N$

---

### Output

Output $T$ lines. The $i$\-th line should contain the answer for the $i$\-th test case.

输出 $T$ 行，第 $i$ 行应包含第 $i$ 组测试数据的答案。

---

### Sample Input 1

```text
3
4 4
1 2
1 4
2 4
2 3
3
xxo
xox
oxo
oxx
1 0
4
oooo
5 5
1 4
2 3
4 5
3 4
2 5
7
oxxxxxx
xxoxxxo
xxxoxox
xoxxoxx
oxxxoxx
```

---

### Sample Output 1

```text
Yes
Yes
No
```

---

For the first test case, for example, the condition can be satisfied by repeatedly moving along cities $4 \to 2 \to 1 \to 4 \to 2 \to 1 \to \cdots$. Alternatively, the condition can also be satisfied by repeatedly moving along cities $3 \to 2 \to 3 \to 3 \to 2 \to 3 \to \cdots$.

对于第一组测试数据，例如，按顺序反复移动经过城市 $4 \to 2 \to 1 \to 4 \to 2 \to 1 \to \cdots$ 即可满足条件。另外，按顺序反复移动经过城市 $3 \to 2 \to 3 \to 3 \to 2 \to 3 \to \cdots$ 也可以满足条件。

---

For the second test case, the condition can be satisfied by staying in city $1$ indefinitely.

对于第二组测试数据，无限期停留在城市 $1$ 即可满足条件。

---

For the third test case, it is impossible to keep moving while satisfying the condition.

对于第三组测试数据，不存在满足条件的持续移动方式。
