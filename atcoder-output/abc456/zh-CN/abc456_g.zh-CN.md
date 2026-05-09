# G - Count Holidays

分值：$600$ 分

---

### Problem Statement

Takahashi is creating a work schedule for $N$ days by designating each day as a workday or a holiday.

高桥正在制定 $N$ 天的工作安排，他需要将每一天设定为工作日或休息日。

---

You are given a string $S$ of length $N$ representing the constraints on work days. If the $i$\-th character of $S$ is `x`, day $i$ must be a workday. If it is `.`, day $i$ can be either a workday or a holiday.

给定一个长度为 $N$ 的字符串 $S$，它表示工作日的约束条件。如果 $S$ 的第 $i$ 个字符是 `x`，那么第 $i$ 天必须是工作日；如果是 `.`，那么第 $i$ 天既可以是工作日也可以是休息日。

---

There are $2^q$ valid work schedules satisfying the constraints, where $q$ is the number of `.` characters in $S$. For each $k=1,2,\dots,N$, solve the following problem:

满足约束条件的有效工作安排共有 $2^q$ 种，其中 $q$ 是 $S$ 中 `.` 字符的个数。对于每个 $k=1,2,\dots,N$，求解以下问题：

---

> Among the $2^q$ valid work schedules satisfying the constraints, find the number, modulo $998244353$, of schedules in which the longest consecutive block of holidays is exactly $k$ days.

> 在所有满足约束条件的 $2^q$ 种有效工作安排中，统计最长连续休息日恰好为 $k$ 天的安排数量，结果对 $998244353$ 取模。

---

### Constraints

-   $N$ is an integer between $1$ and $2 \times 10^5$, inclusive.
-   $S$ is a string of length $N$ consisting of `.`, `x`.

-   $N$ 是介于 $1$ 和 $2 \times 10^5$ 之间（含两端）的整数。
-   $S$ 是长度为 $N$ 的字符串，仅由 `.` 和 `x` 组成。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$S$

---

### Output

Output $N$ lines. The $i$\-th line should contain the answer for $k=i$.

输出 $N$ 行，第 $i$ 行应包含 $k=i$ 对应的答案。

---

### Sample Input 1

```text
5
.x...
```

---

### Sample Output 1

```text
9
4
2
0
0
```

---

Denoting holidays as `o`, the valid work schedules are as follows:

用 `o` 表示休息日，有效工作安排如下：

---

-   $k=1$: `oxxxx`, `oxoxx`, `oxoxo`, `oxxox`, `oxxxo`, `xxoxx`, `xxoxo`, `xxxox`, `xxxxo`
-   $k=2$: `oxoox`, `oxxoo`, `xxoox`, `xxxoo`
-   $k=3$: `oxooo`, `xxooo`

-   $k=1$：`oxxxx`、`oxoxx`、`oxoxo`、`oxxox`、`oxxxo`、`xxoxx`、`xxoxo`、`xxxox`、`xxxxo`
-   $k=2$：`oxoox`、`oxxoo`、`xxoox`、`xxxoo`
-   $k=3$：`oxooo`、`xxooo`

---

### Sample Input 2

```text
7
.......
```

---

### Sample Output 2

```text
33
47
27
12
5
2
1
```

---

### Sample Input 3

```text
20
.....x...x..........
```

---

### Sample Output 3

```text
9359
75312
94664
46840
23680
7168
3072
1280
512
256
0
0
0
0
0
0
0
0
0
0
```
