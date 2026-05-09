# C - Amidakuji

Source: https://atcoder.jp/contests/arc218/tasks/arc218_c?lang=en

Score: $600$ points

## Problem Statement

> Prepare as few types of ladder lotteries as possible and combine them so that all permutations can be produced.

This is an interactive problem (in which your program and the judge program interact via input and output).

You are given a positive integer $N$.

Choose any positive integer $m$ and $m$ permutations of $(1,2,\dots,N)$, and output them. Let the $i$-th permutation be $P_i=(P_{i,1},P_{i,2},\dots,P_{i,N})$.

Then, a permutation $Q=(Q_1,Q_2,\dots,Q_N)$ of $(1,2,\dots,N)$ is given. Output a sequence of positive integers $A=(A_1,A_2,\dots,A_k)$ satisfying all of the following conditions.

- $0 \le k \le 2N^2$
- All elements of $A$ are between $1$ and $m$, inclusive.
- Starting from the sequence $R=(1,2,\dots,N)$, performing the following operation for $i = 1,2,\dots,k$ in order results in $R = Q$.

Let $m_{\min}$ be the minimum value of $m$ for which the above problem can be solved regardless of $Q$. Your output $m$ must equal $m_{\min}$.

**More precisely**

For a sequence of permutations $P=(P_1,P_2,\dots,P_m)$ of $(1,2,\dots,N)$, we call $P$ a **good sequence of permutations** if the following condition is satisfied:

- For any permutation $Q=(Q_1,Q_2,\dots,Q_N)$ of $(1,2,\dots,N)$, there exists a sequence of positive integers $A=(A_1,A_2,\dots,A_k)$ satisfying all of the following conditions.
  - $0 \le k \le 2N^2$
  - All elements of $A$ are between $1$ and $m$, inclusive.
  - Starting from the sequence $R=(1,2,\dots,N)$, performing the following operation for $i = 1,2,\dots,k$ in order results in $R = Q$.
    - Let $p = P_{A_i}$. Simultaneously replace $R_{j}$ with $R_{p_j}$ for each $j = 1,2,\dots,N$.

It is guaranteed that at least one **good sequence of permutations** exists. Thus, the minimum value $m_{\min}$ of the length $m$ of a **good sequence of permutations** is determined. Your output $m$ must equal $m_{\min}$.

Note that your output $P$ does not need to be a **good sequence of permutations**. Your submission is judged correct if you can output an $A$ satisfying the conditions for the given $Q$.

## Constraints

- $3 \le N \le 500$
- $Q$ is a permutation of $(1,2,\dots,N)$.
- All input values are integers.

## Input/Output

This is an interactive problem (in which your program and the judge program interact via input and output).

First, the judge gives you a positive integer $N$ in the following format:

```text
N
```

Then, output your chosen positive integer $m$ and $m$ permutations of $(1,2,\dots,N)$ in the following format over $m+1$ lines. Here, the $j$-th element of the $i$-th permutation is $P_{i,j}$. Be sure to output a newline at the end.

```text
m
P_{1,1}\ P_{1,2}\ \dots\ P_{1,N}
P_{2,1}\ P_{2,2}\ \dots\ P_{2,N}
\vdots
P_{m,1}\ P_{m,2}\ \dots\ P_{m,N}
```

The following conditions must be satisfied:

- $m \le 1000$
- $(P_{i,1},P_{i,2},\dots,P_{i,N})$ is a permutation of $(1,2,\dots,N)$.

If your output $P$ does not satisfy the above conditions, the judge outputs -1. At that point, your submission has already been judged as incorrect. The judge program terminates at that point, so it is advisable for your program to terminate as well.

Then, the judge gives you a permutation $Q=(Q_1,Q_2,\dots,Q_N)$ of $(1,2,\dots,N)$ in the following format:

```text
Q_1\ Q_2\ \dots\ Q_N
```

Then, output a sequence of positive integers $A=(A_1,A_2,\dots,A_k)$ in the following format. Be sure to output a newline at the end.

```text
k\ A_1\ A_2\ \dots\ A_k
```

Your output is judged as correct if and only if the following conditions are all satisfied:

- $m = m_{\min}$
- $0 \le k \le 2N^2$
- All elements of $A$ are between $1$ and $m$, inclusive.
- Starting from the sequence $R=(1,2,\dots,N)$, performing the following operation for $i = 1,2,\dots,k$ in order results in $R = Q$.

## Notes

- **After each output, insert a newline and flush the standard output. Failure to do so may result in a judge verdict of TLE.**
- **If you receive -1, terminate your program immediately. If you do, the judge verdict will be WA, but if you do not, the judge verdict will be indeterminate.**
- Terminate your program immediately after outputting your answer as well. Otherwise, the judge verdict will be indeterminate.
- Do not output unnecessary newlines, as they will be considered malformatted.
- The judge for this problem is not adaptive. The judge program determines $Q$ before the interaction begins.

## Sample Input/Output

The following is a case with $N=3,Q=(2,3,1)$.

| Input | Output | Explanation |
| --- | --- | --- |
| 3 |  | $N$ is given. |
|  | 2

2 1 3

3 2 1 | Choose $m = 2,P_1=(2,1,3),P_2=(3,2,1)$ and output them. |
| 2 3 1 |  | Since $P$ satisfies the conditions, $Q=(2,3,1)$ is given. |
|  | 2 2 1 | $A=(2,1)$ satisfies the conditions. $R$ becomes $(1,2,3) \rightarrow (3,2,1) \rightarrow (2,3,1)$, which matches $Q$.

Also, $m_{\min} = 2$ for $N = 3$, and $m = m_{\min}$ is satisfied.

Thus, this output is judged as correct.

Be sure to output $k$ as well, all on one line. |
