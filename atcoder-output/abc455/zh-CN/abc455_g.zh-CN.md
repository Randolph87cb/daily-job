# G - Balanced Subarrays

分值：$625$ 分

---

### Problem Statement

You are given a sequence $A$ of $N$ positive integers.  
Among the $\frac{N(N+1)}{2}$ non-empty (contiguous) subarrays of $A$, we call a sequence $X$ a balanced sequence if and only if it satisfies the following condition:

给定一个长度为 $N$ 的正整数序列 $A$。
在 $A$ 的所有 $\frac{N(N+1)}{2}$ 个非空（连续）子数组中，我们称序列 $X$ 为平衡序列当且仅当它满足以下条件：

---

-   Every integer appearing in $X$ appears the same number of times in $X$.

- 所有在 $X$ 中出现过的整数，在 $X$ 中的出现次数均相等。

---

For each $k=1,2,\dots,K$, find the following two values:

对于每个 $k=1,2,\dots,K$，请求出以下两个值：

---

-   The number of balanced sequences in which each integer appears exactly $B_k$ times.
-   The number of balanced sequences in which exactly $B_k$ distinct integers appear.

- 每个整数恰好出现 $B_k$ 次的平衡序列的数量。
- 恰好包含 $B_k$ 个不同整数的平衡序列的数量。

---

Count two subarrays separately if they are taken from different positions in $A$, even if they are identical as sequences.

只要两个子数组在 $A$ 中的位置不同，即使它们作为序列完全相同，也需要单独计数。

---

Solve $T$ test cases per input.

每个输入包含 $T$ 组测试用例，你需要依次处理。

---

### Constraints

-   $1 \leq T \leq 2 \times 10^5$
-   $1 \leq N \leq 2 \times 10^5$
-   $1 \leq K \leq \min(N,10)$
-   $1 \leq A_i \leq N$
-   $1 \leq B_k \leq N$
-   $B_1,B_2,\dots,B_K$ are pairwise distinct.
-   The sum of $N$ over all test cases is at most $2 \times 10^5$.
-   All input values are integers.

- $1 \leq T \leq 2 \times 10^5$
- $1 \leq N \leq 2 \times 10^5$
- $1 \leq K \leq \min(N,10)$
- $1 \leq A_i \leq N$
- $1 \leq B_k \leq N$
- $B_1,B_2,\dots,B_K$ 两两不同。
- 所有测试用例的 $N$ 之和不超过 $2 \times 10^5$。
- 所有输入值均为整数。

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

Each case is given in the following format:

每组测试用例按照以下格式给出：

$N$ $K$  
$A_1$ $A_2$ $\dots$ $A_N$  
$B_1$ $B_2$ $\dots$ $B_K$

---

### Output

Output the answers in the following format:

按照以下格式输出答案：

---

```text
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

```text
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

---

For each case, letting $c_{k,1}$ be the number of balanced sequences in which each integer appears exactly $B_k$ times, and $c_{k,2}$ be the number of balanced sequences in which exactly $B_k$ distinct integers appear, output in the following format:

对于每组测试用例，设 $c_{k,1}$ 为每个整数恰好出现 $B_k$ 次的平衡序列的数量，$c_{k,2}$ 为恰好包含 $B_k$ 个不同整数的平衡序列的数量，请按照以下格式输出：

---

```text
$c_{1,1}$ $c_{1,2}$  
$c_{2,1}$ $c_{2,2}$  
$\vdots$
$c_{K,1}$ $c_{K,2}$  
```

```text
$c_{1,1}$ $c_{1,2}$  
$c_{2,1}$ $c_{2,2}$  
$\vdots$
$c_{K,1}$ $c_{K,2}$  
```

---

### Sample Input 1

```text
3
4 2
1 2 1 2
2 1
1 1
1
1
7 7
1 5 5 1 5 1 2
1 2 3 4 5 6 7
```

---

### Sample Output 1

```text
1 4
7 4
1 1
13 8
3 8
1 1
0 0
0 0
0 0
0 0
```

---

For the first test case, the pairs $(l,r)$ such that the subarray of $A$ from the $l$\-th through the $r$\-th element is a balanced sequence are $(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving eight instances in total.  
Among these, the ones in which each integer appears exactly twice are $(1,4)$, giving one instance, and the ones in which exactly two distinct integers appear are $(1,2),(1,4),(2,3),(3,4)$, giving four instances.  
Thus, for $k=1$, output `1 4`.  
Also, the ones in which each integer appears exactly once are $(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving seven instances, and the ones in which exactly one distinct integer appears are $(1,1),(2,2),(3,3),(4,4)$, giving four instances.  
Thus, for $k=2$, output `7 4`.

对于第一组测试用例，所有满足“$A$ 中从第 $l$ 个元素到第 $r$ 个元素的子数组是平衡序列”的数对 $(l,r)$ 为 $(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)$，总共有 8 个。
其中，每个整数恰好出现两次的平衡序列为 $(1,4)$，共 1 个；恰好包含两个不同整数的平衡序列为 $(1,2),(1,4),(2,3),(3,4)$，共 4 个。
因此对于 $k=1$，输出 `1 4`。
此外，每个整数恰好出现一次的平衡序列为 $(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)$，共 7 个；恰好包含一个不同整数的平衡序列为 $(1,1),(2,2),(3,3),(4,4)$，共 4 个。
因此对于 $k=2$，输出 `7 4`。
