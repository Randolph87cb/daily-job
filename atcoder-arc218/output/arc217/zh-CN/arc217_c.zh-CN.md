# C - Greedy Customers 2

分值：$700$ 分

---

### Problem Statement

AtCoder Store has $N$ items. The $i$\-th item costs $A_i$ yen.

AtCoder 商店共有 $N$ 件商品。其中第 $i$ 件商品的价格为 $A_i$ 日元。

---

$N$ people visit the store one by one. Each person has $C$ yen and performs the following procedure.

共有 $N$ 人依次来到商店。每个人都持有 $C$ 日元，并会执行以下操作流程。

---

-   Choose an integer $x$ uniformly at random between $1$ and $C$, inclusive, as the budget for shopping.
-   If there is an item remaining in the store that costs at most $x$ yen, purchase one of the most expensive ones among them. Otherwise, leave the store without purchasing anything.

-   从 $1$ 到 $C$（包含两端）的整数中等概率随机选取一个整数 $x$ 作为本次购物的预算。
-   如果商店中仍有价格不超过 $x$ 日元的剩余商品，则购买其中价格最高的一件。如果不存在这样的商品，则不购买任何商品直接离开商店。

---

As the owner of the store, you want to know how many items will be sold. For $k=0,1,2,\ldots,N$, find the probability, modulo $998244353$, that exactly $k$ items are sold in the end.

作为商店的所有者，你希望知道最终售出的商品数量。对于每个 $k=0,1,2,\ldots,N$，求恰好售出 $k$ 件商品的概率，结果对 $998244353$ 取模。

---

You are given $T$ test cases; solve each of them.

给定 $T$ 组测试数据，你需要分别处理每组数据。

---

**Definition of probability \ \text{mod}\ 998244353**

**概率对 \ \text{mod}\ 998244353 取模的定义**

---

It can be proved that the probabilities to be found are always rational numbers. Moreover, under the constraints of this problem, when each such rational number is expressed as an irreducible fraction $\displaystyle \frac{P}{Q}$, it can be proved that $Q \neq 0 \bmod 998244353$. Thus, there is a unique integer $R$ satisfying $R \times Q \equiv P \bmod 998244353, 0 \leq R \lt 998244353$. Find this $R$.

可以证明，所求的概率均为有理数。此外，在本题的约束条件下，将每个有理数表示为既约分数 $\displaystyle \frac{P}{Q}$ 时，可以证明 $Q \neq 0 \bmod 998244353$。因此存在唯一的整数 $R$ 满足 $R \times Q \equiv P \bmod 998244353, 0 \leq R \lt 998244353$，请你求出这个 $R$。

---

### Constraints

-   $1\le T$
-   $1\le N$
-   The sum of $N$ over all test cases is at most $100$.
-   $1\le A_i \le C < 998244353$
-   All input values are integers.

-   $1\le T$
-   $1\le N$
-   所有测试数据的 $N$ 之和不超过 $100$。
-   $1\le A_i \le C < 998244353$
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

每组测试数据按照以下格式给出：

$N$ $C$  
$A_1$ $A_2$ $\ldots$ $A_N$

---

### Output

Output the answers for the test cases in order, separated by newlines.

按顺序输出每组测试数据的答案，相邻答案之间用换行分隔。

---

For each test case, output the answers for $k=0,1,\ldots,N$ in order, separated by spaces.

对于每组测试数据，按顺序输出 $k=0,1,\ldots,N$ 对应的答案，相邻答案之间用空格分隔。

---

### Sample Input 1

```text
4
2 3
1 3
3 17
9 9 8
5 2025
1 1 1 1 1
6 1000
544 105 450 715 479 992
```

---

### Sample Output 1

```text
0 776412275 221832079
465698363 588015298 487439081 455335965
0 0 0 0 0 1
366062443 766314649 169448288 553531286 643499511 890090646 604030590
```

---

Consider the first test case.

考虑第一组测试数据。

---

For example, the procedure for each person proceeds as follows.

例如，每个人的操作流程如下所示。

---

-   Person $1$: Chooses $x=2$. The most expensive item that costs at most $2$ yen is the first item, so they purchase the first item.
-   Person $2$: Chooses $x=1$. There are no items costing at most $1$ yen, so they leave without purchasing anything.

-   第 $1$ 个人：选择了 $x=2$。价格不超过 $2$ 日元的最贵商品是第一件商品，因此他购买了第一件商品。
-   第 $2$ 个人：选择了 $x=1$。不存在价格不超过 $1$ 日元的商品，因此他没有购买任何商品直接离开。

---

In this case, exactly one item is sold in the end.

在这种情况下，最终恰好售出了一件商品。

---

The probabilities that exactly $0,1,2$ items are sold are $\displaystyle 0, \frac49,\frac59$, respectively.

恰好售出 $0,1,2$ 件商品的概率分别为 $\displaystyle 0, \frac49,\frac59$。
