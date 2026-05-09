# A - Many Sets

来源：https://atcoder.jp/contests/arc218/tasks/arc218_a?lang=en

分值：$400$ 分

## 题目描述

You are given $N$ sequences of positive integers, each of length $M$. The $i$-th sequence is $A_i=(A_{i,1},A_{i,2},\dots,A_{i,M})$.

There are $M^N$ ways to choose one element from each of these $N$ sequences. Find the sum, modulo $998244353$, of "the number of distinct integers among the chosen elements" over all such ways.

## 约束条件

- $1 \le N,M \le 500$
- $1 \le A_{i,j} \le NM$
- All input values are integers.

## 输入

输入从标准输入按如下格式给出：

```text
N M
A_{1,1} A_{1,2} \dots A_{1,M}
A_{2,1} A_{2,2} \dots A_{2,M}
\vdots
A_{N,1} A_{N,2} \dots A_{N,M}
```

## 输出

输出答案。

## 样例输入 1

```text
2 2
1 3
2 3
```

## 样例输出 1

```text
7
```

For example, if $A_{1,1}$ and $A_{2,1}$ are chosen, there are two distinct integers among the chosen elements: $1$ and $2$.

The number of distinct integers is $1$ only when $A_{1,2}$ and $A_{2,2}$ are chosen, and it is $2$ in the other three cases, so the answer is $7$.

## 样例输入 2

```text
2 2
1 1
1 2
```

## 样例输出 2

```text
6
```

## 样例输入 3

```text
3 5
3 1 3 4 2
5 2 1 2 3
4 6 2 5 6
```

## 样例输出 3

```text
327
```
