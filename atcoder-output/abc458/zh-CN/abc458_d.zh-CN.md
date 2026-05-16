# D - Chalkboard Median

分值：$400$ 分

---

### Problem Statement

There is one integer $X$ written on a blackboard.

黑板上初始写有一个整数 $X$。

---

You are given $Q$ queries to process in order. The $i$\-th query $(1 \le i \le Q)$ is as follows.

给定 $Q$ 个询问，你需要按顺序处理它们。第 $i$ 个询问 $(1 \le i \le Q)$ 的内容如下。

---

> Two integers $A_i$ and $B_i$ are given. Write two new integers $A_i$ and $B_i$ on the blackboard.
> 
> Then, output the median of the $2i+1$ integers written on the blackboard.

> 给定两个整数 $A_i$ 和 $B_i$，在黑板上写下两个新整数 $A_i$ 和 $B_i$。
> 
> 之后，输出当前黑板上所有 $2i+1$ 个整数的中位数。

---

### Constraints

-   $1 \le X \le 10^9$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le A_i, B_i \le 10^9$
-   All input values are integers.

-   $1 \le X \le 10^9$
-   $1 \le Q \le 2 \times 10^5$
-   $1 \le A_i, B_i \le 10^9$
-   所有输入值都是整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$X$  
$Q$  
$A_1$ $B_1$  
$A_2$ $B_2$  
$\vdots$  
$A_Q$ $B_Q$

---

### Output

Output $Q$ lines.

输出 $Q$ 行。

---

The $i$\-th line should contain the answer to the $i$\-th query.

第 $i$ 行应输出第 $i$ 个询问的答案。

---

### Sample Input 1

```text
5
3
2 3
1 2
8 9
```

---

### Sample Output 1

```text
3
2
3
```

---

In the first query, the integers written on the blackboard become $5, 2, 3$, and their median is $3$.

处理第一个询问后，黑板上的整数变为 $5, 2, 3$，它们的中位数是 $3$。

---

In the second query, the integers written on the blackboard become $5, 2, 3, 1, 2$, and their median is $2$.

处理第二个询问后，黑板上的整数变为 $5, 2, 3, 1, 2$，它们的中位数是 $2$。

---

In the third query, the integers written on the blackboard become $5, 2, 3, 1, 2, 8, 9$, and their median is $3$.

处理第三个询问后，黑板上的整数变为 $5, 2, 3, 1, 2, 8, 9$，它们的中位数是 $3$。

---

### Sample Input 2

```text
1
4
2 3
4 5
6 7
8 9
```

---

### Sample Output 2

```text
2
3
4
5
```

---

### Sample Input 3

```text
278117031
7
167642909 517897721
148434323 567739597
319926999 481642530
659199879 252516557
49913403 798318034
89701408 892537201
199166668 742285869
```

---

### Sample Output 3

```text
278117031
278117031
319926999
319926999
319926999
319926999
319926999
```
