# C - Amidakuji

分值：$600$ 分

---

### Problem Statement

> Prepare as few types of ladder lotteries as possible and combine them so that all permutations can be produced.

> 准备尽可能少的 ladder lottery 类型，将它们组合后可以生成所有排列。

---

This is an **interactive problem** (in which your program and the judge program interact via input and output).

本题是**交互题**（你的程序需要与评测程序通过输入输出进行交互）。

---

You are given a positive integer $N$.

给定一个正整数 $N$。

---

Choose any positive integer $m$ and $m$ permutations of $(1,2,\dots,N)$, and output them. Let the $i$\-th permutation be $P_i=(P_{i,1},P_{i,2},\dots,P_{i,N})$.

选择任意正整数 $m$ 和 $m$ 个 $(1,2,\dots,N)$ 的排列，然后输出这些排列。记第 $i$ 个排列为 $P_i=(P_{i,1},P_{i,2},\dots,P_{i,N})$。

---

Then, a permutation $Q=(Q_1,Q_2,\dots,Q_N)$ of $(1,2,\dots,N)$ is given. Output a sequence of positive integers $A=(A_1,A_2,\dots,A_k)$ satisfying all of the following conditions.

接下来你会得到一个 $(1,2,\dots,N)$ 的排列 $Q=(Q_1,Q_2,\dots,Q_N)$。输出一个满足以下所有条件的正整数序列 $A=(A_1,A_2,\dots,A_k)$。

---

-   $0 \le k \le 2N^2$
-   All elements of $A$ are between $1$ and $m$, inclusive.
-   Starting from the sequence $R=(1,2,\dots,N)$, performing the following operation for $i = 1,2,\dots,k$ in order results in $R = Q$.

- $0 \le k \le 2N^2$
- $A$ 的所有元素都在 $1$ 到 $m$ 之间（含两端）。
- 初始为序列 $R=(1,2,\dots,N)$，按顺序对每个 $i = 1,2,\dots,k$ 执行以下操作后，结果等于 $R = Q$。

---

-   Let $p = P_{A_i}$. Simultaneously replace $R_{j}$ with $R_{p_j}$ for each $j = 1,2,\dots,N$.

- 令 $p = P_{A_i}$。对每个 $j = 1,2,\dots,N$，同时将 $R_{j}$ 替换为 $R_{p_j}$。

---

**Let $m_{\min}$ be the minimum value of $m$ for which the above problem can be solved regardless of $Q$. Your output $m$ must equal $m_{\min}$.**

**记 $m_{\min}$ 为无论 $Q$ 是什么，上述问题都有解的 $m$ 的最小值。你输出的 $m$ 必须等于 $m_{\min}$。**

---

**More precisely**

**更准确地说**

---

For a sequence of permutations $P=(P_1,P_2,\dots,P_m)$ of $(1,2,\dots,N)$, we call $P$ a **good sequence of permutations** if the following condition is satisfied:

对于由 $(1,2,\dots,N)$ 的排列组成的序列 $P=(P_1,P_2,\dots,P_m)$，如果满足以下条件，我们就称 $P$ 为**好排列序列**：

---

-   For any permutation $Q=(Q_1,Q_2,\dots,Q_N)$ of $(1,2,\dots,N)$, there exists a sequence of positive integers $A=(A_1,A_2,\dots,A_k)$ satisfying all of the following conditions.
    -   $0 \le k \le 2N^2$
    -   All elements of $A$ are between $1$ and $m$, inclusive.
    -   Starting from the sequence $R=(1,2,\dots,N)$, performing the following operation for $i = 1,2,\dots,k$ in order results in $R = Q$.
        -   Let $p = P_{A_i}$. Simultaneously replace $R_{j}$ with $R_{p_j}$ for each $j = 1,2,\dots,N$.

- 对于任意一个 $(1,2,\dots,N)$ 的排列 $Q=(Q_1,Q_2,\dots,Q_N)$，都存在一个正整数序列 $A=(A_1,A_2,\dots,A_k)$ 满足以下所有条件：
  - $0 \le k \le 2N^2$
  - $A$ 的所有元素都在 $1$ 到 $m$ 之间（含两端）。
  - 初始为序列 $R=(1,2,\dots,N)$，按顺序对每个 $i = 1,2,\dots,k$ 执行以下操作后，结果等于 $R = Q$。
    - 令 $p = P_{A_i}$。对每个 $j = 1,2,\dots,N$，同时将 $R_{j}$ 替换为 $R_{p_j}$。

---

It is guaranteed that at least one **good sequence of permutations** exists. Thus, the minimum value $m_{\min}$ of the length $m$ of a **good sequence of permutations** is determined. Your output $m$ must equal $m_{\min}$.  
Note that your output $P$ does not need to be a **good sequence of permutations**. Your submission is judged correct if you can output an $A$ satisfying the conditions for the given $Q$.

题目保证至少存在一个**好排列序列**，因此**好排列序列**长度 $m$ 的最小值 $m_{\min}$ 是确定的。你输出的 $m$ 必须等于 $m_{\min}$。
注意你输出的 $P$ 不需要是**好排列序列**。只要你能对给定的 $Q$ 输出满足条件的 $A$，你的提交就会被判定为正确。

---

### Constraints

-   $3 \le N \le 500$
-   $Q$ is a permutation of $(1,2,\dots,N)$.
-   All input values are integers.

- $3 \le N \le 500$
- $Q$ 是 $(1,2,\dots,N)$ 的一个排列。
- 所有输入值均为整数。

---

### Input/Output

This is an **interactive problem** (in which your program and the judge program interact via input and output).

本题是**交互题**（你的程序需要与评测程序通过输入输出进行交互）。

---

First, the judge gives you a positive integer $N$ in the following format:

首先，评测程序会按照以下格式给你一个正整数 $N$：

$N$

---

Then, output your chosen positive integer $m$ and $m$ permutations of $(1,2,\dots,N)$ in the following format over $m+1$ lines. Here, the $j$\-th element of the $i$\-th permutation is $P_{i,j}$. Be sure to output a newline at the end.

然后，按照以下格式，用 $m+1$ 行输出你选择的正整数 $m$ 和 $m$ 个 $(1,2,\dots,N)$ 的排列。这里第 $i$ 个排列的第 $j$ 个元素为 $P_{i,j}$。输出末尾必须换行。

$m$  
$P_{1,1}$ $P_{1,2}$ $\dots$ $P_{1,N}$  
$P_{2,1}$ $P_{2,2}$ $\dots$ $P_{2,N}$  
$\vdots$  
$P_{m,1}$ $P_{m,2}$ $\dots$ $P_{m,N}$

---

The following conditions must be satisfied:

必须满足以下条件：

---

-   $m \le 1000$
-   $(P_{i,1},P_{i,2},\dots,P_{i,N})$ is a permutation of $(1,2,\dots,N)$.

- $m \le 1000$
- $(P_{i,1},P_{i,2},\dots,P_{i,N})$ 是 $(1,2,\dots,N)$ 的一个排列。

---

If your output $P$ does not satisfy the above conditions, the judge outputs `-1`. At that point, your submission has already been judged as incorrect. The judge program terminates at that point, so it is advisable for your program to terminate as well.

如果你的输出 $P$ 不满足上述条件，评测程序会输出 `-1`。此时你的提交已经被判定为错误，评测程序会终止，因此建议你的程序也立即终止。

---

Then, the judge gives you a permutation $Q=(Q_1,Q_2,\dots,Q_N)$ of $(1,2,\dots,N)$ in the following format:

接下来，评测程序会按照以下格式给你一个 $(1,2,\dots,N)$ 的排列 $Q=(Q_1,Q_2,\dots,Q_N)$：

$Q_1$ $Q_2$ $\dots$ $Q_N$

---

Then, output a sequence of positive integers $A=(A_1,A_2,\dots,A_k)$ in the following format. Be sure to output a newline at the end.

然后按照以下格式输出正整数序列 $A=(A_1,A_2,\dots,A_k)$。输出末尾必须换行。

$k$ $A_1$ $A_2$ $\dots$ $A_k$

---

Your output is judged as correct if and only if the following conditions are all satisfied:

当且仅当以下所有条件都满足时，你的输出会被判定为正确：

---

-   $m = m_{\min}$
-   $0 \le k \le 2N^2$
-   All elements of $A$ are between $1$ and $m$, inclusive.
-   Starting from the sequence $R=(1,2,\dots,N)$, performing the following operation for $i = 1,2,\dots,k$ in order results in $R = Q$.

- $m = m_{\min}$
- $0 \le k \le 2N^2$
- $A$ 的所有元素都在 $1$ 到 $m$ 之间（含两端）。
- 初始为序列 $R=(1,2,\dots,N)$，按顺序对每个 $i = 1,2,\dots,k$ 执行以下操作后，结果等于 $R = Q$。

---

-   Let $p = P_{A_i}$. Simultaneously replace $R_{j}$ with $R_{p_j}$ for each $j = 1,2,\dots,N$.

- 令 $p = P_{A_i}$。对每个 $j = 1,2,\dots,N$，同时将 $R_{j}$ 替换为 $R_{p_j}$。

---

### Notes

-   **After each output, insert a newline and flush the standard output. Failure to do so may result in a judge verdict of TLE.**
-   **If you receive `-1`, terminate your program immediately. If you do, the judge verdict will be WA, but if you do not, the judge verdict will be indeterminate.**
-   Terminate your program immediately after outputting your answer as well. Otherwise, the judge verdict will be indeterminate.
-   Do not output unnecessary newlines, as they will be considered malformatted.
-   The judge for this problem is not adaptive. The judge program determines $Q$ before the interaction begins.

- **每次输出后都要换行并刷新标准输出。否则可能导致评测结果为 TLE。**
- **如果收到 `-1`，立即终止你的程序。这么做的话评测结果会是 WA，否则评测结果是不确定的。**
- 输出答案后也请立即终止程序，否则评测结果是不确定的。
- 不要输出多余的换行，否则会被视为格式错误。
- 本题的评测是非适应性的，评测程序会在交互开始前就确定 $Q$。

---

### Sample Input/Output

The following is a case with $N=3,Q=(2,3,1)$.

以下是 $N=3,Q=(2,3,1)$ 的一个样例。

---

| Input | Output | Explanation |
|  --- | --- | ---  |
| `3` |  | $N$ is given. |
|  | <code>2<br>2 1 3<br>3 2 1</code> | Choose $m = 2,P_1=(2,1,3),P_2=(3,2,1)$ and output them. |
| `2 3 1` |  | Since $P$ satisfies the conditions, $Q=(2,3,1)$ is given. |
|  | `2 2 1` | $A=(2,1)$ satisfies the conditions. $R$ becomes $(1,2,3) \rightarrow (3,2,1) \rightarrow (2,3,1)$, which matches $Q$.  <br>Also, $m_{\min} = 2$ for $N = 3$, and $m = m_{\min}$ is satisfied.  <br>Thus, this output is judged as correct.  <br>Be sure to output $k$ as well, all on one line. |

| 输入 | 输出 | 说明 |
| --- | --- | --- |
| `3` | | 给出 $N$。 |
| | <code>2<br>2 1 3<br>3 2 1</code> | 选择 $m = 2,P_1=(2,1,3),P_2=(3,2,1)$ 并输出。 |
| `2 3 1` | | 因为 $P$ 满足条件，所以给出 $Q=(2,3,1)$。 |
| | `2 2 1` | $A=(2,1)$ 满足条件。$R$ 变为 $(1,2,3) \rightarrow (3,2,1) \rightarrow (2,3,1)$，与 $Q$ 一致。<br>同时对于 $N = 3$，有 $m_{\min} = 2$，满足 $m = m_{\min}$。<br>因此该输出被判定为正确。<br>注意也要将 $k$ 完整输出在一行内。
