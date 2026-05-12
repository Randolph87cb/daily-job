# F - Merge Slimes 2

分值：$525$ 分

---

### Problem Statement

There is a sequence $A$ of $N$ non-negative integers, all initially $0$. Process $Q$ queries given in order.  
For the $q$\-th query, you are given integers $l_q, r_q$ satisfying $1 \leq l_q \leq r_q \leq N$ and a positive integer $a_q$. Perform the following in order:

给定一个长度为 $N$ 的非负整数序列 $A$，初始时所有元素均为 $0$。请按顺序处理 $Q$ 个查询。

对于第 $q$ 个查询，给定满足 $1 \leq l_q \leq r_q \leq N$ 的整数 $l_q, r_q$ 以及一个正整数 $a_q$，请按以下步骤执行操作：

---

-   Add $a_q$ to each of $A_{l_q}, A_{{l_q}+1}, \dots, A_{r_q}$.
-   Then, letting $M=r_q-l_q+1$ and $B=(B_1,B_2,\dots,B_M)=(A_{l_q}, A_{l_q+1}, \dots, A_{r_q})$, find the answer to the following problem:

- 将 $A_{l_q}, A_{{l_q}+1}, \dots, A_{r_q}$ 中的每个元素都加上 $a_q$。
- 然后，设 $M=r_q-l_q+1$ 和 $B=(B_1,B_2,\dots,B_M)=(A_{l_q}, A_{l_q+1}, \dots, A_{r_q})$，求解以下问题的答案：

---

> There are $M$ slimes $1,2,\dots,M$, where the $m$\-th slime has weight $B_m$.  
> Repeat the operation of choosing two slimes and merging them $M-1$ times.  
> When slimes of weights $x$ and $y$ are merged, a slime of weight $x+y$ appears and the original two slimes disappear. This incurs a cost of $x \times y$.  
> Find, modulo $998244353$, the minimum possible total cost of the $M-1$ operations.

> 现有 $M$ 个史莱姆 $1,2,\dots,M$，其中第 $m$ 个史莱姆的重量为 $B_m$。
> 重复执行选择两个史莱姆合并的操作共 $M-1$ 次。
> 当重量为 $x$ 和 $y$ 的史莱姆合并时，会产生一个重量为 $x+y$ 的史莱姆，原有的两个史莱姆消失，该操作会产生 $x \times y$ 的代价。
> 求这 $M-1$ 次操作的最小总代价，结果对 $998244353$ 取模。

---

Note that the changes made on $A$ in each query carry over to subsequent queries.

注意，每次查询中对 $A$ 做出的修改会延续到后续的查询中。

---

### Constraints

-   $1 \leq N \leq 10^5$
-   $1 \leq Q \leq 10^5$
-   $1 \leq l_q \leq r_q \leq N$
-   $1 \leq a_q \leq 10^9$
-   All input values are integers.

- $1 \leq N \leq 10^5$
- $1 \leq Q \leq 10^5$
- $1 \leq l_q \leq r_q \leq N$
- $1 \leq a_q \leq 10^9$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $Q$  
$l_1$ $r_1$ $a_1$  
$l_2$ $r_2$ $a_2$  
$\vdots$  
$l_Q$ $r_Q$ $a_Q$

---

### Output

Output the answers over $Q$ lines in total. The $q$\-th line should contain the answer to the $q$\-th query.

总共输出 $Q$ 行答案，第 $q$ 行应包含第 $q$ 个查询的答案。

---

### Sample Input 1

```text
5 4
1 3 22
3 4 13
5 5 455
1 5 1000000000
```

---

### Sample Output 1

```text
1452
455
0
21421644
```

---

After the first query, $A=(22,22,22,0,0)$ and $B=(22,22,22)$. Merging the first and third slimes first incurs a cost of $22 \times 22=484$. Then merging the remaining two slimes incurs a cost of $22 \times 44=968$. The total cost is $484+968=1452$. Moreover, the total cost cannot be made smaller than this.  
After the second query, $A=(22,22,35,13,0)$ and $B=(35,13)$. The answer is $35 \times 13 = 455$.

第一个查询处理完成后，$A=(22,22,22,0,0)$ 且 $B=(22,22,22)$。先合并第一个和第三个史莱姆的代价为 $22 \times 22=484$，之后合并剩余两个史莱姆的代价为 $22 \times 44=968$，总代价为 $484+968=1452$，且不存在更小的总代价。

第二个查询处理完成后，$A=(22,22,35,13,0)$ 且 $B=(35,13)$，答案为 $35 \times 13 = 455$。
