# B - All Minus

Source: https://atcoder.jp/contests/arc218/tasks/arc218_b?lang=en

Score: $400$ points

## Problem Statement

There are $N$ non-negative integers $A_1,A_2,\dots,A_N$ written on a blackboard.

Alice and Bob play a game. Starting with Alice, they alternately perform the following operation, and the player who reduces the number of integers written on the blackboard to $0$ wins.

- Let $m$ be the minimum non-negative integer currently written on the blackboard.
  - If $m > 0$, choose a positive integer $x$ between $1$ and $m$, inclusive. Replace every integer written on the blackboard with its current value minus $x$.
  - If $m = 0$, erase one or more of the $0$s written on the blackboard.

Determine who wins when both players play optimally to win.

$T$ test cases are given; solve each of them.

## Constraints

- $1 \le T \le 2 \times 10^5$
- $1 \le N \le 2 \times 10^5$
- $0 \le A_i \le 10^9$
- The sum of $N$ over all test cases is at most $2 \times 10^5$.
- All input values are integers.

## Input

The input is given from Standard Input in the following format:

```text
T
\mathrm{case}_1
\mathrm{case}_2
\vdots
\mathrm{case}_T
```

Each test case is given in the following format:

```text
N
A_1 A_2 \dots A_N
```

## Output

Output $T$ lines. The $i$-th line should contain Alice if Alice wins in $\mathrm{case}_i$, or Bob if Bob wins.

## Sample Input 1

```text
5
1
2
3
1 1 1
4
1 2 3 4
7
3 1 4 1 5 9 2
3
218 503 2026
```

## Sample Output 1

```text
Alice
Bob
Bob
Bob
Alice
```

For the first test case, one possible game progression is as follows:

- Initially, $2$ is written on the blackboard.
- Alice chooses $x = 1$. Now $1$ is written on the blackboard.
- Bob chooses $x = 1$. Now $0$ is written on the blackboard.
- Alice chooses and erases one $0$. Now nothing is written on the blackboard.

When both players play optimally to win, Alice wins.

For the second test case, one possible game progression is as follows:

- Initially, $1,1,1$ are written on the blackboard.
- Alice chooses $x = 1$. Now $0,0,0$ are written on the blackboard.
- Bob chooses and erases one $0$. Now $0,0$ are written on the blackboard.
- Alice chooses and erases one $0$. Now $0$ is written on the blackboard.
- Bob chooses and erases one $0$. Now nothing is written on the blackboard.

When both players play optimally to win, Bob wins.
