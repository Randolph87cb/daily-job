# G - 221 Substring

Source: https://atcoder.jp/contests/abc452/tasks/abc452_g?lang=en

Score : $600$ points

### Problem Statement

For a sequence $X = (X_1, \dots, X_n)$ of positive integers, we call $X$ a **221 sequence** if and only if the length and value are equal for every (length, value) pair in its run-length encoding. More formally, a sequence satisfying the following condition is called a 221 sequence.

-   For any integer pair $(l, r)$ satisfying $1 \leq l \leq r \leq n$, if all three of the following conditions hold, then $(r-l+1) = X_l$.
    -   $l = 1$ or ($l \geq 2$ and $X_{l-1} \neq X_l$)
    -   $r = n$ or ($r \leq n-1$ and $X_{r+1} \neq X_r$)
    -   $X_l = X_{l+1} = \dots = X_r$

For example, $(2,2,3,3,3,1,2,2)$ is a 221 sequence, but $(1,1)$ and $(4,4,1,4,4)$ are not 221 sequences.

You are given a sequence $A = (A_1, \dots, A_N)$ of positive integers of length $N$. Find the number of distinct 221 sequences that appear as a non-empty **contiguous subsequence** of $A$.

Even if two subsequences are extracted from different positions, they are counted as one if they are equal as sequences.

### Constraints

-   $1 \leq N \leq 500\,000$
-   $1 \leq A_i \leq 9$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$A_1$ $A_2$ $\cdots$ $A_N$
```

### Output

Output the answer on a single line.

### Sample Input 1

```text
23
2 2 3 3 3 1 1 1 3 3 3 1 2 2 2 1 9 1 4 4 4 4 4
```

### Sample Output 1

```text
14
```

The 221 sequences that appear as a non-empty contiguous subsequence of $A$ are the following $14$:

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

### Sample Input 2

```text
2
6 7
```

### Sample Output 2

```text
0
```

No 221 sequences appear as a non-empty contiguous subsequence of $A$.
