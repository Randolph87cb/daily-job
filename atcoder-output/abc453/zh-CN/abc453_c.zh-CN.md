# C - Sneaking Glances

分值：$300$ 分

---

### Problem Statement

Takahashi is at coordinate $0.5$ on a number line.

高桥位于数轴上的坐标 $0.5$ 处。

---

He will make $N$ moves.  
In the $i$\-th move, he chooses either the positive direction or the negative direction, and moves $L_i$ in that direction.

他将进行 $N$ 次移动。
在第 $i$ 次移动中，他选择正方向或负方向，并沿该方向移动 $L_i$ 的距离。

---

What is the maximum number of times he can pass through coordinate $0$?  
Under the constraints of this problem, no move will end at coordinate $0$.

求他最多能经过坐标 $0$ 多少次？
在本题的约束条件下，任何一次移动都不会在坐标 $0$ 处结束。

---

### Constraints

-   $1 \le N \le 20$
-   $1 \le L_i \le 10^9$
-   All input values are integers.

- $1 \le N \le 20$
- $1 \le L_i \le 10^9$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$L_1$ $L_2$ $\dots$ $L_N$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
5
2 5 2 2 1
```

---

### Sample Output 1

```text
4
```

---

For example, by choosing the directions of movement as follows, he can pass through coordinate $0$ four times, which is the maximum.

例如，通过如下选择每次的移动方向，他可以四次经过坐标 $0$，这是最大值。

---

-   In the first move, choose the negative direction and move $2$. He moves from coordinate $0.5$ to $-1.5$, passing through coordinate $0$.
-   In the second move, choose the positive direction and move $5$. He moves from coordinate $-1.5$ to $3.5$, passing through coordinate $0$.
-   In the third move, choose the negative direction and move $2$. He moves from coordinate $3.5$ to $1.5$.
-   In the fourth move, choose the negative direction and move $2$. He moves from coordinate $1.5$ to $-0.5$, passing through coordinate $0$.
-   In the fifth move, choose the positive direction and move $1$. He moves from coordinate $-0.5$ to $0.5$, passing through coordinate $0$.

- 第一次移动选择负方向，移动 $2$ 的距离。他从坐标 $0.5$ 移动到 $-1.5$，经过坐标 $0$。
- 第二次移动选择正方向，移动 $5$ 的距离。他从坐标 $-1.5$ 移动到 $3.5$，经过坐标 $0$。
- 第三次移动选择负方向，移动 $2$ 的距离。他从坐标 $3.5$ 移动到 $1.5$。
- 第四次移动选择负方向，移动 $2$ 的距离。他从坐标 $1.5$ 移动到 $-0.5$，经过坐标 $0$。
- 第五次移动选择正方向，移动 $1$ 的距离。他从坐标 $-0.5$ 移动到 $0.5$，经过坐标 $0$。

---

### Sample Input 2

```text
5
100 1 2 3 4
```

---

### Sample Output 2

```text
1
```

---

### Sample Input 3

```text
20
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

---

### Sample Output 3

```text
20
```
