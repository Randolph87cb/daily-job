# G - Balanced Subarrays

分值：$625625625$ 分

---

### Problem Statement

You are given a sequence $AAA$ of $NNN$ positive integers.  
Among the $N(N+1)2\frac{N(N+1)}{2}2N(N+1)​$ non-empty (contiguous) subarrays of $AAA$, we call a sequence $XXX$ a balanced sequence if and only if it satisfies the following condition:

给定一个由 $NNN$ 个正整数组成的序列 $AAA$。  
在 $AAA$ 的总共 $N(N+1)2\frac{N(N+1)}{2}2N(N+1)​$ 个非空（连续）子数组中，我们称序列 $XXX$ 为平衡序列当且仅当它满足以下条件：

---

-   Every integer appearing in $XXX$ appears the same number of times in $XXX$.

- 所有在 $XXX$ 中出现过的整数，在 $XXX$ 中的出现次数均相等。

---

For each $k=1,2,…,Kk=1,2,\dots,Kk=1,2,…,K$, find the following two values:

对于每个 $k=1,2,…,Kk=1,2,\dots,Kk=1,2,…,K$，请求出以下两个值：

---

-   The number of balanced sequences in which each integer appears exactly $BkB_kBk​$ times.
-   The number of balanced sequences in which exactly $BkB_kBk​$ distinct integers appear.

- 满足「每个整数恰好出现 $BkB_kBk​$ 次」的平衡序列的数量。
- 满足「恰好出现 $BkB_kBk​$ 个不同整数」的平衡序列的数量。

---

Count two subarrays separately if they are taken from different positions in $AAA$, even if they are identical as sequences.

只要两个子数组在 $AAA$ 中的位置不同，即使它们作为序列完全相同，也需要分别计数。

---

Solve $TTT$ test cases per input.

每个输入包含 $TTT$ 组测试用例，你需要处理所有测试用例。

---

### Constraints

-   $1≤T≤2×1051 \leq T \leq 2 \times 10^51≤T≤2×105$
-   $1≤N≤2×1051 \leq N \leq 2 \times 10^51≤N≤2×105$
-   $1≤K≤min⁡(N,10)1 \leq K \leq \min(N,10)1≤K≤min(N,10)$
-   $1≤Ai≤N1 \leq A_i \leq N1≤Ai​≤N$
-   $1≤Bk≤N1 \leq B_k \leq N1≤Bk​≤N$
-   $B1,B2,…,BKB_1,B_2,\dots,B_KB1​,B2​,…,BK​$ are pairwise distinct.
-   The sum of $NNN$ over all test cases is at most $2×1052 \times 10^52×105$.
-   All input values are integers.

- $1≤T≤2×1051 \leq T \leq 2 \times 10^51≤T≤2×105$
- $1≤N≤2×1051 \leq N \leq 2 \times 10^51≤N≤2×105$
- $1≤K≤min⁡(N,10)1 \leq K \leq \min(N,10)1≤K≤min(N,10)$
- $1≤Ai≤N1 \leq A_i \leq N1≤Ai​≤N$
- $1≤Bk≤N1 \leq B_k \leq N1≤Bk​≤N$
- $B1,B2,…,BKB_1,B_2,\dots,B_KB1​,B2​,…,BK​$ 两两不同。
- 所有测试用例的 $NNN$ 之和不超过 $2×1052 \times 10^52×105$。
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$TTT$  
$case1\mathrm{case}_1case1​$  
$case2\mathrm{case}_2case2​$  
$⋮\vdots⋮$  
$caseT\mathrm{case}_TcaseT​$

---

Each case is given in the following format:

每个测试用例按照以下格式给出：

$NNN$ $KKK$  
$A1A_1A1​$ $A2A_2A2​$ $…\dots…$ $ANA_NAN​$  
$B1B_1B1​$ $B2B_2B2​$ $…\dots…$ $BKB_KBK​$

---

### Output

Output the answers in the following format:

请按照以下格式输出答案：

---

```text
$case1\mathrm{case}_1case1​$
$case2\mathrm{case}_2case2​$
$⋮\vdots⋮$
$caseT\mathrm{case}_TcaseT​$
```

```text
$case1\mathrm{case}_1case1​$
$case2\mathrm{case}_2case2​$
$⋮\vdots⋮$
$caseT\mathrm{case}_TcaseT​$
```

---

For each case, letting $ck,1c_{k,1}ck,1​$ be the number of balanced sequences in which each integer appears exactly $BkB_kBk​$ times, and $ck,2c_{k,2}ck,2​$ be the number of balanced sequences in which exactly $BkB_kBk​$ distinct integers appear, output in the following format:

对于每个测试用例，设 $ck,1c_{k,1}ck,1​$ 为满足「每个整数恰好出现 $BkB_kBk​$ 次」的平衡序列的数量，$ck,2c_{k,2}ck,2​$ 为满足「恰好出现 $BkB_kBk​$ 个不同整数」的平衡序列的数量，请按照以下格式输出：

---

```text
$c1,1c_{1,1}c1,1​$ $c1,2c_{1,2}c1,2​$  
$c2,1c_{2,1}c2,1​$ $c2,2c_{2,2}c2,2​$  
$⋮\vdots⋮$
$cK,1c_{K,1}cK,1​$ $cK,2c_{K,2}cK,2​$  
```

```text
$c1,1c_{1,1}c1,1​$ $c1,2c_{1,2}c1,2​$  
$c2,1c_{2,1}c2,1​$ $c2,2c_{2,2}c2,2​$  
$⋮\vdots⋮$
$cK,1c_{K,1}cK,1​$ $cK,2c_{K,2}cK,2​$  
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

For the first test case, the pairs $(l,r)(l,r)(l,r)$ such that the subarray of $AAA$ from the $lll$\-th through the $rrr$\-th element is a balanced sequence are $(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving eight instances in total.  
Among these, the ones in which each integer appears exactly twice are $(1,4)(1,4)(1,4)$, giving one instance, and the ones in which exactly two distinct integers appear are $(1,2),(1,4),(2,3),(3,4)(1,2),(1,4),(2,3),(3,4)(1,2),(1,4),(2,3),(3,4)$, giving four instances.  
Thus, for $k=1k=1k=1$, output `1 4`.  
Also, the ones in which each integer appears exactly once are $(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)$, giving seven instances, and the ones in which exactly one distinct integer appears are $(1,1),(2,2),(3,3),(4,4)(1,1),(2,2),(3,3),(4,4)(1,1),(2,2),(3,3),(4,4)$, giving four instances.  
Thus, for $k=2k=2k=2$, output `7 4`.

对于第一个测试用例，所有满足「$AAA$ 中从第 $lll$ 个元素到第 $rrr$ 个元素的子数组是平衡序列」的数对 $(l,r)(l,r)(l,r)$ 为 $(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(1,4),(2,2),(2,3),(3,3),(3,4),(4,4)$，总共有 8 个这样的子数组。  
其中，满足「每个整数恰好出现 2 次」的是 $(1,4)(1,4)(1,4)$，共 1 个；满足「恰好出现 2 个不同整数」的是 $(1,2),(1,4),(2,3),(3,4)(1,2),(1,4),(2,3),(3,4)(1,2),(1,4),(2,3),(3,4)$，共 4 个。  
因此对于 $k=1k=1k=1$，输出 `1 4`。  
此外，满足「每个整数恰好出现 1 次」的是 $(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)(1,1),(1,2),(2,2),(2,3),(3,3),(3,4),(4,4)$，共 7 个；满足「恰好出现 1 个不同整数」的是 $(1,1),(2,2),(3,3),(4,4)(1,1),(2,2),(3,3),(4,4)(1,1),(2,2),(3,3),(4,4)$，共 4 个。  
因此对于 $k=2k=2k=2$，输出 `7 4`。
