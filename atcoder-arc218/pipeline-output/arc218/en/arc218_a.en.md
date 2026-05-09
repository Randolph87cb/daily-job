# A - Many Sets

Source: https://atcoder.jp/contests/arc218/tasks/arc218_a?lang=en

Score: $400$ points

## Problem Statement

You are given $N$ sequences of positive integers, each of length $M$. The $i$-th sequence is $A_i=(A_{i,1},A_{i,2},\dots,A_{i,M})$.

There are $M^N$ ways to choose one element from each of these $N$ sequences. Find the sum, modulo $998244353$, of "the number of distinct integers among the chosen elements" over all such ways.

## Constraints

- $1 \le N,M \le 500$
- $1 \le A_{i,j} \le NM$
- All input values are integers.

## Input

The input is given from Standard Input in the following format:

```text
N M
A_{1,1} A_{1,2} \dots A_{1,M}
A_{2,1} A_{2,2} \dots A_{2,M}
\vdots
A_{N,1} A_{N,2} \dots A_{N,M}
```

## Output

Output the answer.

## Sample Input 1

```text
2 2
1 3
2 3
```

## Sample Output 1

```text
7
```

For example, if $A_{1,1}$ and $A_{2,1}$ are chosen, there are two distinct integers among the chosen elements: $1$ and $2$.

The number of distinct integers is $1$ only when $A_{1,2}$ and $A_{2,2}$ are chosen, and it is $2$ in the other three cases, so the answer is $7$.

## Sample Input 2

```text
2 2
1 1
1 2
```

## Sample Output 2

```text
6
```

## Sample Input 3

```text
3 5
3 1 3 4 2
5 2 1 2 3
4 6 2 5 6
```

## Sample Output 3

```text
327
```
