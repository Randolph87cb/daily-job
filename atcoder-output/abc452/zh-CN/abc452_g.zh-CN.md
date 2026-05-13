# G - 221 Substring

分值：$600$ 分

---

### Problem Statement

For a sequence $X = (X_1, \dots, X_n)$ of positive integers, we call $X$ a **221 sequence** if and only if the length and value are equal for every (length, value) pair in its run-length encoding. More formally, a sequence satisfying the following condition is called a 221 sequence.

对于由正整数构成的序列$X = (X_1, \dots, X_n)$，当且仅当其游程编码中每一组（长度, 数值）的长度和数值相等时，我们称$X$为**221序列**。更正式地，满足以下条件的序列称为221序列。

---

-   For any integer pair $(l, r)$ satisfying $1 \leq l \leq r \leq n$, if all three of the following conditions hold, then $(r-l+1) = X_l$.
    -   $l = 1$ or ($l \geq 2$ and $X_{l-1} \neq X_l$)
    -   $r = n$ or ($r \leq n-1$ and $X_{r+1} \neq X_r$)
    -   $X_l = X_{l+1} = \dots = X_r$

- 对于任意满足$1 \leq l \leq r \leq n$的整数对$(l, r)$，若以下三个条件同时成立，则$(r-l+1) = X_l$。
    - $l = 1$ 或 ($l \geq 2$ 且 $X_{l-1} \neq X_l$)
    - $r = n$ 或 ($r \leq n-1$ 且 $X_{r+1} \neq X_r$)
    - $X_l = X_{l+1} = \dots = X_r$

---

For example, $(2,2,3,3,3,1,2,2)$ is a 221 sequence, but $(1,1)$ and $(4,4,1,4,4)$ are not 221 sequences.

例如，$(2,2,3,3,3,1,2,2)$是221序列，但$(1,1)$和$(4,4,1,4,4)$不是221序列。

---

You are given a sequence $A = (A_1, \dots, A_N)$ of positive integers of length $N$. Find the number of distinct 221 sequences that appear as a non-empty **contiguous subsequence** of $A$.

给定一个长度为$N$的正整数序列$A = (A_1, \dots, A_N)$，求其中作为非空**连续子序列**出现的不同221序列的个数。

---

Even if two subsequences are extracted from different positions, they are counted as one if they are equal as sequences.

即使两个子序列从不同位置提取，只要作为序列相等，就只计为一次。

---

### Constraints

-   $1 \leq N \leq 500\,000$
-   $1 \leq A_i \leq 9$
-   All input values are integers.

- $1 \leq N \leq 500\,000$
- $1 \leq A_i \leq 9$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按以下格式从标准输入给出：

$N$  
$A_1$ $A_2$ $\cdots$ $A_N$

---

### Output

Output the answer on a single line.

将答案输出在一行中。

---

### Sample Input 1

```text
23
2 2 3 3 3 1 1 1 3 3 3 1 2 2 2 1 9 1 4 4 4 4 4
```

---

### Sample Output 1

```text
14
```

---

The 221 sequences that appear as a non-empty contiguous subsequence of $A$ are the following $14$:

作为$A$的非空连续子序列出现的221序列共有以下$14$个：

---

-   $(1)$
-   $(1,2,2)$
-   $(1,3,3,3)$
-   $(1,3,3,3,1)$
-   $(1,3,3,3,1,2,2)$
-   $(1,4,4,4,4)$
-   $(2,2)$
-   $(2,2,1)$
-   $(2,2,3,3,3)$
-   $(2,2,3,3,3,1)$
-   $(3,3,3)$
-   $(3,3,3,1)$
-   $(3,3,3,1,2,2)$
-   $(4,4,4,4)$

- $(1)$
- $(1,2,2)$
- $(1,3,3,3)$
- $(1,3,3,3,1)$
- $(1,3,3,3,1,2,2)$
- $(1,4,4,4,4)$
- $(2,2)$
- $(2,2,1)$
- $(2,2,3,3,3)$
- $(2,2,3,3,3,1)$
- $(3,3,3)$
- $(3,3,3,1)$
- $(3,3,3,1,2,2)$
- $(4,4,4,4)$

---

### Sample Input 2

```text
2
6 7
```

---

### Sample Output 2

```text
0
```

---

No 221 sequences appear as a non-empty contiguous subsequence of $A$.

$A$中不存在作为非空连续子序列出现的221序列。
