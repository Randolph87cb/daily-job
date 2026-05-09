# F - Buckets

分值：$700$ 分

---

### Problem Statement

**Problems F and F2 are the same problem with different constraints on $M$. In Problem F, $1 \le M \le 4$.**

**问题F和F2是同一道题，仅在$M$的约束条件上有所区别。在问题F中，$1 \le M \le 4$。**

---

You are given a positive integer $M$. Consider the following problem.

给定一个正整数$M$。请考虑如下问题。

---

> **Bucket**
> 
> You are given a positive integer $N$ and non-negative integer sequences $A=(A_1,A_2,\dots,A_N)$ and $B=(B_1,B_2,\dots,B_N)$ of length $N$. All elements of $A$ and $B$ are between $0$ and $M$, inclusive.
> 
> There are $N$ buckets numbered $1$ to $N$. Each bucket can hold up to $M$ liters of water. Initially, bucket $i$ contains $A_i$ liters of water.
> 
> You may perform the following operation any number of times.
> 
> -   Choose two distinct buckets $i$ and $j$. Continue pouring water from bucket $i$ into bucket $j$ as long as both of the following conditions are satisfied:
>     -   Bucket $i$ still has water remaining.
>     -   The amount of water in bucket $j$ is less than $M$ liters.
> 
> Your goal is to have exactly $B_i$ liters of water in bucket $i$ for all $i$. Determine whether the goal can be achieved.

> **桶**
> 
> 给定正整数$N$，以及两个长度为$N$的非负整数序列$A=(A_1,A_2,\dots,A_N)$和$B=(B_1,B_2,\dots,B_N)$。$A$和$B$的所有元素均在$0$到$M$之间（包含两端）。
> 
> 有$N$个桶，编号为$1$到$N$。每个桶最多可装$M$升水。初始时，第$i$个桶装有$A_i$升水。
> 
> 你可以执行任意次以下操作：
> 
> -   选择两个不同的桶$i$和$j$。只要同时满足以下两个条件，就持续将水从桶$i$倒入桶$j$中：
>     -   桶$i$中还有剩余的水。
>     -   桶$j$中的水量小于$M$升。
> 
> 你的目标是对于所有$i$，桶$i$中恰好装有$B_i$升水。请判断是否可以达成目标。

---

You are given a non-negative integer matrix $X=(X_{i,j})(0 \le i,j \le M)$ of $(M+1)$ rows and $(M+1)$ columns. Process the following queries $Q$ times.

给定一个$(M+1)$行$(M+1)$列的非负整数矩阵$X=(X_{i,j})(0 \le i,j \le M)$。请处理$Q$次查询。

---

-   You are given non-negative integers $i,j,Y$ with $0 \le i,j \le M$. Change $X_{i,j}$ to $Y$. Then, obtain non-negative integer sequences $A$ and $B$ by the following procedure.
    -   Initialize non-negative integer sequences $A$ and $B$ as empty sequences.
    -   For $i = 0,1,\dots,M$ in this order:

-   给定满足$0 \le i,j \le M$的非负整数$i,j,Y$。将$X_{i,j}$修改为$Y$。然后通过以下步骤得到非负整数序列$A$和$B$：
    -   将非负整数序列$A$和$B$初始化为空序列。
    -   按顺序对$i = 0,1,\dots,M$执行：

---

-   For $j = 0,1,\dots,M$ in this order:

-   按顺序对$j = 0,1,\dots,M$执行：

---

-   Do this $X_{i,j}$ times: append $i$ to the end of $A$ and $j$ to the end of $B$.

-   重复此操作$X_{i,j}$次：将$i$追加到$A$的末尾，将$j$追加到$B$的末尾。

---

-   Solve **Bucket** for the non-negative integer sequences $A$ and $B$ of length $N = \sum_{i=0}^{M} \sum_{j=0}^{M} X_{i,j}$.

-   以长度为$N = \sum_{i=0}^{M} \sum_{j=0}^{M} X_{i,j}$的非负整数序列$A$和$B$作为输入，求解**桶**问题。

---

### Constraints

-   **$1 \le M \le 4$**
-   $1 \le Q \le 10^6$
-   $0 \le X_{i,j},Y \le 10^{17}$
-   $0 \le i,j \le M$
-   $\sum_{i=0}^{M} \sum_{j=0}^{M} X_{i,j} \ge 1$ at any time.
-   All input values are integers.

-   **$1 \le M \le 4$**
-   $1 \le Q \le 10^6$
-   $0 \le X_{i,j},Y \le 10^{17}$
-   $0 \le i,j \le M$
-   任意时刻满足$\sum_{i=0}^{M} \sum_{j=0}^{M} X_{i,j} \ge 1$。
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$M$ $Q$  
$X_{0,0}$ $X_{0,1}$ $\dots$ $X_{0,M}$  
$X_{1,0}$ $X_{1,1}$ $\dots$ $X_{1,M}$  
$\vdots$  
$X_{M,0}$ $X_{M,1}$ $\dots$ $X_{M,M}$  
$\mathrm{query}_1$  
$\mathrm{query}_2$  
$\vdots$  
$\mathrm{query}_Q$

---

Each query is given in the following format:

每个查询按照以下格式给出：

$i$ $j$ $Y$

---

### Output

Output $Q$ lines. The $i$\-th line should contain `Yes` if the goal can be achieved in $\mathrm{query}_i$, and `No` otherwise.

输出$Q$行。第$i$行如果第$\mathrm{query}_i$次查询可以达成目标则输出`Yes`，否则输出`No`。

---

### Sample Input 1

```text
3 3
0 0 0 0
0 0 2 0
1 0 0 0
0 0 0 0
0 0 0
2 3 1
2 1 1
```

---

### Sample Output 1

```text
Yes
No
Yes
```

---

The first query makes $X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$ , and we obtain $A=(1,1,2),B=(2,2,0)$.

第一次查询修改为$X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$，我们得到$A=(1,1,2),B=(2,2,0)$。

---

In this case, the goal can be achieved by the following sequence of operations, for example.

这种情况下，例如可以通过以下操作序列达成目标。

---

-   Set $i = 1,j = 2$. The amount of water in each bucket changes from $(1,1,2)$ to $(0,2,2)$.
-   Set $i = 3,j = 1$. The amount of water in each bucket changes from $(0,2,2)$ to $(2,2,0)$.

-   选择$i = 1,j = 2$。每个桶的水量从$(1,1,2)$变为$(0,2,2)$。
-   选择$i = 3,j = 1$。每个桶的水量从$(0,2,2)$变为$(2,2,0)$。

---

The second query makes $X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$ , and we obtain $A=(1,1,2,2),B=(2,2,0,3)$.

第二次查询修改为$X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$，我们得到$A=(1,1,2,2),B=(2,2,0,3)$。

---

In this case, the goal cannot be achieved no matter how operations are performed.

这种情况下，无论如何执行操作都无法达成目标。

---

The third query makes $X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$ , and we obtain $A=(1,1,2,2,2),B=(2,2,0,1,3)$.

第三次查询修改为$X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$，我们得到$A=(1,1,2,2,2),B=(2,2,0,1,3)$。

---

In this case, the goal can be achieved by the following sequence of operations, for example.

这种情况下，例如可以通过以下操作序列达成目标。

---

-   Set $i = 1,j = 2$. The amount of water in each bucket changes from $(1,1,2,2,2)$ to $(0,2,2,2,2)$.
-   Set $i = 3,j = 1$. The amount of water in each bucket changes from $(0,2,2,2,2)$ to $(2,2,0,2,2)$.
-   Set $i = 4,j = 5$. The amount of water in each bucket changes from $(2,2,0,2,2)$ to $(2,2,0,1,3)$.

-   选择$i = 1,j = 2$。每个桶的水量从$(1,1,2,2,2)$变为$(0,2,2,2,2)$。
-   选择$i = 3,j = 1$。每个桶的水量从$(0,2,2,2,2)$变为$(2,2,0,2,2)$。
-   选择$i = 4,j = 5$。每个桶的水量从$(2,2,0,2,2)$变为$(2,2,0,1,3)$。

---

### Sample Input 2

```text
4 10
45636788580181785 16131322312654301 43477244591521823 6505049084010674 86530627327096446
95921187347997793 55491565467039163 87684565747362311 80318628430974482 12308092878301956
75570615154690027 96403707363045776 14150012766408204 6612197700307407 64417022692908525
5530468643826479 41731276604630756 15675296751519388 59461896803210859 66666666666666666
72767956047192820 18258893791516726 58852629621892634 33333333333333333 29923985408775019
2 1 26541245644686826
2 4 29485791833729050
4 1 21832826336874318
3 2 4953499115446612
2 0 69217973349997921
2 4 23133150029036944
3 4 55834224798559242
1 2 98517007615469735
2 3 3768060024403703
0 4 87241661746072372
```

---

### Sample Output 2

```text
No
Yes
No
Yes
No
Yes
No
No
No
No
```
