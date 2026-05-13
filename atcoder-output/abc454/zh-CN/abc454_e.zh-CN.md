# E - LRUD Moving

分值：$450$ 分

---

### Problem Statement

You are given positive integers $N,A,B$. It is guaranteed that both $A$ and $B$ are between $1$ and $N$, inclusive.

给定正整数 $N,A,B$。保证 $A$ 和 $B$ 均介于 $1$ 和 $N$ 之间（含两端）。

---

There is an $N\times N$ grid. The cell at the $i$\-th row from the top and $j$\-th column from the left is denoted as cell $(i,j)$. Initially, a piece is placed at cell $(1,1)$.

有一个 $N\times N$ 的网格。从上往下第 $i$ 行、从左往右第 $j$ 列的单元格记为 $(i,j)$。初始时，一枚棋子被放置在单元格 $(1,1)$。

---

By repeating $N^2-2$ moves, each of which moves the piece to an adjacent cell (up, down, left, or right), you want to move the piece to cell $(N,N)$ while visiting every cell except cell $(A,B)$. You must not visit the same cell more than once (you must not visit cells $(1,1)$ and $(N,N)$ in the middle, either).

你需要通过重复 $N^2-2$ 次移动，每次将棋子移至相邻单元格（上、下、左、右之一），将棋子移动到单元格 $(N,N)$，同时访问除 $(A,B)$ 外的所有单元格。你不能重复访问同一个单元格（移动过程中也不能访问 $(1,1)$ 和 $(N,N)$）。

---

Determine whether such a sequence of moves is possible, and if so, output one such sequence.

判断是否存在这样的移动序列。若存在，输出其中一种合法序列。

---

You are given $T$ test cases; solve each of them.

给定 $T$ 组测试用例，你需要分别处理每组数据。

---

### Constraints

-   $1\le T \le 5000$
-   $2\le N\le 10^3$
-   $1\le A,B\le N$
-   $(A,B)\neq (1,1),(N,N)$
-   The sum of $N^2$ over all test cases is at most $10^6$.
-   All input values are integers.

-   $1\le T \le 5000$
-   $2\le N\le 10^3$
-   $1\le A,B\le N$
-   $(A,B)\neq (1,1),(N,N)$
-   所有测试用例的 $N^2$ 之和不超过 $10^6$。
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$T$  
$\text{case}_1$  
$\text{case}_2$  
$\vdots$  
$\text{case}_T$

---

Each test case is given in the following format:

每组测试用例按照以下格式给出：

$N$ $A$ $B$

---

### Output

Output the answers for the test cases in order, separated by newlines.

按顺序输出每个测试用例的答案，答案之间用换行分隔。

---

For each test case, if it is impossible to perform a sequence of moves satisfying the conditions, output `No`.

对于每组测试用例，如果不存在满足条件的移动序列，输出 `No`。

---

If it is possible, output in the following format:

如果存在，按照以下格式输出：

---

```text
Yes
$S_1S_2\ldots S_{N^2-2}$
```

```text
Yes
$S_1S_2\ldots S_{N^2-2}$
```

---

Here, $S_k$ is defined as follows, where the coordinates of the piece before the $k$\-th move is cell $(i,j)$.

其中 $S_k$ 的定义如下：第 $k$ 次移动前棋子所在的坐标为单元格 $(i,j)$。

---

-   $S_k=$ `L` if the piece moves from cell $(i,j)$ to cell $(i,j-1)$
-   $S_k=$ `R` if the piece moves from cell $(i,j)$ to cell $(i,j+1)$
-   $S_k=$ `U` if the piece moves from cell $(i,j)$ to cell $(i-1,j)$
-   $S_k=$ `D` if the piece moves from cell $(i,j)$ to cell $(i+1,j)$

-   若棋子从单元格 $(i,j)$ 移动到单元格 $(i,j-1)$，则 $S_k=$ 为 `L`
-   若棋子从单元格 $(i,j)$ 移动到单元格 $(i,j+1)$，则 $S_k=$ 为 `R`
-   若棋子从单元格 $(i,j)$ 移动到单元格 $(i-1,j)$，则 $S_k=$ 为 `U`
-   若棋子从单元格 $(i,j)$ 移动到单元格 $(i+1,j)$，则 $S_k=$ 为 `D`

---

If multiple sequences of moves satisfy the conditions, any of them will be accepted.

如果存在多个满足条件的移动序列，你可以输出任意一个。

---

### Sample Input 1

```text
3
2 1 2
3 2 2
4 3 2
```

---

### Sample Output 1

```text
Yes
DR
No
Yes
RRRDLLLDDRRURD
```

---

Consider the first test case.

考虑第一组测试用例。

---

Starting with the piece at cell $(1,1)$, move it twice as follows:

初始时棋子位于单元格 $(1,1)$，按如下方式移动两次：

---

-   Move the piece downward. The piece moves to cell $(2,1)$.
-   Move the piece rightward. The piece moves to cell $(2,2)$.

-   将棋子向下移动，棋子移动到单元格 $(2,1)$。
-   将棋子向右移动，棋子移动到单元格 $(2,2)$。

---

This sequence of moves satisfies the conditions.

该移动序列满足条件。
