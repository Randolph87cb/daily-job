# G - Catch All Apples

分值：$625$ 分

---

### Problem Statement

$N$ apples fall on a number line. Apple $i$ falls at coordinate $X_i$ at time $T_i$.

$N$ 个苹果掉落在数轴上。苹果 $i$ 在时刻 $T_i$ 掉落在坐标 $X_i$ 处。

---

You want to place some robots on the number line to collect all $N$ apples. The robots can be placed at any coordinates.

你需要在数轴上放置若干机器人来收集全部 $N$ 个苹果。机器人可以被放置在任意坐标处。

---

Each robot starts operating from time $0$ and can move freely along the number line at a speed of at most $1$. Multiple robots may occupy the same coordinate at the same time. Each robot can collect apple $i$ if and only if it is at coordinate $X_i$ at time $T_i$.

每个机器人从时刻 $0$ 开始工作，可沿数轴自由移动，最大速度不超过 $1$。允许多个机器人在同一时刻处于同一坐标。当且仅当某个机器人在时刻 $T_i$ 恰好位于坐标 $X_i$ 时，它可以收集到苹果 $i$。

---

Find the minimum number of robots needed to collect all apples.

求收集所有苹果所需的最少机器人数量。

---

### Constraints

-   $1 \le N \le 3 \times 10^5$
-   $0 \le T_i \le 3 \times 10^5$
-   $0 \le X_i \le 3 \times 10^5$
-   $(T_i, X_i) \neq (T_j, X_j)$ $(i \neq j)$
-   All input values are integers.

-   $1 \le N \le 3 \times 10^5$
-   $0 \le T_i \le 3 \times 10^5$
-   $0 \le X_i \le 3 \times 10^5$
-   $(T_i, X_i) \neq (T_j, X_j)$ $(i \neq j)$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$T_1$ $X_1$  
$T_2$ $X_2$  
$\vdots$  
$T_N$ $X_N$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
4
0 2
1 0
2 1
2 3
```

---

### Sample Output 1

```text
2
```

---

All apples can be collected with two robots by moving them as follows:

按照如下方式移动两个机器人即可收集所有苹果：

---

-   Place robot $1$ at coordinate $0$ and robot $2$ at coordinate $2$.
-   Time $0$: Robot $2$ collects apple $1$.
-   Time $1$: Robot $1$ collects apple $2$. Move both robots in the positive direction at speed $1$ until time $2$.
-   Time $2$: Robot $1$ collects apple $3$ and robot $2$ collects apple $4$.

-   将机器人 $1$ 放置在坐标 $0$ 处，机器人 $2$ 放置在坐标 $2$ 处。
-   时刻 $0$：机器人 $2$ 收集苹果 $1$。
-   时刻 $1$：机器人 $1$ 收集苹果 $2$。让两个机器人都以速度 $1$ 沿正方向移动，直到时刻 $2$。
-   时刻 $2$：机器人 $1$ 收集苹果 $3$，机器人 $2$ 收集苹果 $4$。

---

It is impossible to collect all apples with fewer than two robots, so output $2$.

使用少于两个机器人不可能收集所有苹果，因此输出 $2$。

---

### Sample Input 2

```text
5
0 1
0 2
0 3
0 4
0 5
```

---

### Sample Output 2

```text
5
```

---

### Sample Input 3

```text
8
10 4
4 2
7 10
5 3
1 9
0 6
3 8
0 9
```

---

### Sample Output 3

```text
2
```
