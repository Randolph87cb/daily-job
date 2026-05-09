# F - Plan Holidays

分值：$525$ 分

---

### Problem Statement

Takahashi is trying to decide his schedule for $N$ days. Initially, none of the days are holidays.

高桥正规划 $N$ 天的日程安排。初始时所有天都不是假期。

---

He can repeat either of the following operations any number of times:

他可以任意多次执行以下两种操作之一：

---

-   Choose an integer $i$ between $1$ and $N$, inclusive, and make day $i$ a holiday. This operation costs $A_i$.
-   Choose an integer $i$ between $2$ and $N-1$, inclusive, such that both day $i-1$ and day $i+1$ are already holidays, and make day $i$ a holiday. This operation is free.

-   选择一个介于 $1$ 和 $N$ 之间（含两端）的整数 $i$，将第 $i$ 天设为假期。该操作花费 $A_i$。
-   选择一个介于 $2$ 和 $N-1$ 之间（含两端）的整数 $i$，满足第 $i-1$ 天和第 $i+1$ 天均已为假期，将第 $i$ 天设为假期。该操作免费。

---

Find the minimum total cost required to create a consecutive block of $K$ or more holidays.

求构造出长度至少为 $K$ 的连续假期段所需的最小总花费。

---

$T$ test cases are given; solve each of them.

共有 $T$ 组测试用例，你需要处理每一组数据。

---

### Constraints

-   $1 \leq T \leq 2 \times 10^5$
-   $1 \leq K \leq N \leq 2 \times 10^5$
-   $1 \leq A_i \leq 10^9$
-   All input values are integers.
-   The sum of $N$ over all test cases is at most $2\times 10^5$.

-   $1 \leq T \leq 2 \times 10^5$
-   $1 \leq K \leq N \leq 2 \times 10^5$
-   $1 \leq A_i \leq 10^9$
-   所有输入值均为整数。
-   所有测试用例的 $N$ 之和不超过 $2\times 10^5$。

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

其中 $\mathrm{case}_i$ 表示第 $i$ 个测试用例的输入内容。每个测试用例按照以下格式给出：

$N$ $K$  
$A_1$ $A_2$ $\dots$ $A_N$

---

### Output

Output $T$ lines. The $i$\-th line should contain the answer for the $i$\-th test case.

输出共 $T$ 行，第 $i$ 行应包含第 $i$ 个测试用例的答案。

---

### Sample Input 1

```text
3
5 2
3 1 4 1 5
6 4
24 3 22 39 4 29
15 7
220651272 302798780 874479994 657822311 613294668 479624013 241168404 610547619 762548286 256160531 823041612 951553052 226556081 649525901 153805947
```

---

### Sample Output 1

```text
2
29
1902064780
```

---

For the first test case, a consecutive block of at least two holidays can be created by performing operations as follows:

对于第一个测试用例，可以通过如下操作构造出长度至少为 2 的连续假期段：

---

-   Make day $2$ a holiday using the first type of operation. This costs $1$.
-   Make day $4$ a holiday using the first type of operation. This costs $1$.
-   Make day $3$ a holiday using the second type of operation. This is free.

-   使用第一种操作将第 $2$ 天设为假期，花费 $1$。
-   使用第一种操作将第 $4$ 天设为假期，花费 $1$。
-   使用第二种操作将第 $3$ 天设为假期，免费。

---

The total cost of this sequence of operations is $2$. It is impossible to create a consecutive block of two or more holidays with a cost less than $2$, so output $2$.

该操作序列的总花费为 $2$。不存在花费小于 $2$ 的方案可以构造出长度至少为 2 的连续假期段，因此输出 $2$。
