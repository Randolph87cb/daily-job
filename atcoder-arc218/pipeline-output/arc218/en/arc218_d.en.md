# D - I like Increasing

Source: https://atcoder.jp/contests/arc218/tasks/arc218_d?lang=en

Score: $700$ points

## Problem Statement

You are given a permutation $P=(P_1,P_2,\dots,P_N)$ of $(1,2,\dots,N)$.

For a sequence of integers $x=(x_1,x_2,\dots,x_k)$, define the score of $x$ as the number of indices $i$ satisfying $x_i < x_{i+1}$.

Process the following query $Q$ times.

- You are given positive integers $l$ and $r$ with $1 \le l \le r \le N$. For $X = (P_l,P_{l+1},\dots,P_r)$, solve the following problem.
  - Let $M$ be the maximum score of a non-empty subsequence of $X$. Find the minimum length of a non-empty subsequence of $X$ whose score equals $M$.

**What is a subsequence?**

A subsequence of a sequence $A$ is a sequence obtained by removing zero or more elements from $A$ and arranging the remaining elements in their original order.

## Constraints

- $1 \le N,Q \le 2 \times 10^5$
- $P$ is a permutation of $(1,2,\dots,N)$.
- $1 \le l \le r \le N$
- All input values are integers.

## Input

The input is given from Standard Input in the following format:

```text
N Q
P_1\ P_2\ \dots\ P_N
\mathrm{query}_1
\mathrm{query}_2
\vdots
\mathrm{query}_Q
```

Each query is given in the following format:

```text
l\ r
```

## Output

Output $Q$ lines. The $i$-th line should contain the answer to $\mathrm{query}_i$.

## Sample Input 1

```text
6 4
2 1 4 6 3 5
1 3
3 6
2 2
1 6
```

## Sample Output 1

```text
2
4
1
5
```

For the first query, $X = (2,1,4)$. The maximum score $M = 1$ is achieved by $(2,4),(1,4),(2,1,4)$. The minimum length among these is $2$, achieved by $(2,4),(1,4)$.

For the second query, $X = (4,6,3,5)$ and $M = 2$. $(4,6,3,5)$ achieves the minimum length $4$ among those with score $2$.

For the third query, $X = (1)$ and $M = 0$. $(1)$ achieves the minimum length $1$ with score $0$.

For the fourth query, $X = (2,1,4,6,3,5)$ and $M = 3$. $(2,4,6,3,5)$ achieves the minimum length $5$ with score $3$.

## Sample Input 2

```text
12 8
8 3 5 7 9 6 11 1 10 4 12 2
3 4
10 11
5 8
3 8
4 10
2 10
5 7
1 8
```

## Sample Output 2

```text
2
2
2
4
5
7
2
5
```
