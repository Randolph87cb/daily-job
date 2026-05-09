# F - Buckets

Source: https://atcoder.jp/contests/arc218/tasks/arc218_f?lang=en

Score: $700$ points

## Problem Statement

Problems F and F2 are the same problem with different constraints on $M$. In Problem F, $1 \le M \le 4$.

You are given a positive integer $M$. Consider the following problem.

> **Bucket**
>
> You are given a positive integer $N$ and non-negative integer sequences $A=(A_1,A_2,\dots,A_N)$ and $B=(B_1,B_2,\dots,B_N)$ of length $N$. All elements of $A$ and $B$ are between $0$ and $M$, inclusive.
>
> There are $N$ buckets numbered $1$ to $N$. Each bucket can hold up to $M$ liters of water. Initially, bucket $i$ contains $A_i$ liters of water.
>
> You may perform the following operation any number of times.
>
> - Choose two distinct buckets $i$ and $j$. Continue pouring water from bucket $i$ into bucket $j$ as long as both of the following conditions are satisfied:
>   - Bucket $i$ still has water remaining.
>   - The amount of water in bucket $j$ is less than $M$ liters.
>
> Your goal is to have exactly $B_i$ liters of water in bucket $i$ for all $i$. Determine whether the goal can be achieved.

You are given a non-negative integer matrix $X=(X_{i,j})(0 \le i,j \le M)$ of $(M+1)$ rows and $(M+1)$ columns. Process the following queries $Q$ times.

- You are given non-negative integers $i,j,Y$ with $0 \le i,j \le M$. Change $X_{i,j}$ to $Y$. Then, obtain non-negative integer sequences $A$ and $B$ by the following procedure.
  - Initialize non-negative integer sequences $A$ and $B$ as empty sequences.
  - For $i = 0,1,\dots,M$ in this order:
- Solve **Bucket** for the non-negative integer sequences $A$ and $B$ of length $N = \sum_{i=0}^{M} \sum_{j=0}^{M} X_{i,j}$.

## Constraints

- **$1 \le M \le 4$**
- $1 \le Q \le 10^6$
- $0 \le X_{i,j},Y \le 10^{17}$
- $0 \le i,j \le M$
- $\sum_{i=0}^{M} \sum_{j=0}^{M} X_{i,j} \ge 1$ at any time.
- All input values are integers.

## Input

The input is given from Standard Input in the following format:

```text
M Q
X_{0,0}\ X_{0,1}\ \dots\ X_{0,M}
X_{1,0}\ X_{1,1}\ \dots\ X_{1,M}
\vdots
X_{M,0}\ X_{M,1}\ \dots\ X_{M,M}
\mathrm{query}_1
\mathrm{query}_2
\vdots
\mathrm{query}_Q
```

Each query is given in the following format:

```text
i\ j\ Y
```

## Output

Output $Q$ lines. The $i$-th line should contain Yes if the goal can be achieved in $\mathrm{query}_i$, and No otherwise.

## Sample Input 1

```text
3 3
0 0 0 0
0 0 2 0
1 0 0 0
0 0 0 0
0 0 0
2 3 1
2 1 1
```

## Sample Output 1

```text
Yes
No
Yes
```

The first query makes $X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$, and we obtain $A=(1,1,2),B=(2,2,0)$.

In this case, the goal can be achieved by the following sequence of operations, for example.

- Set $i = 1,j = 2$. The amount of water in each bucket changes from $(1,1,2)$ to $(0,2,2)$.
- Set $i = 3,j = 1$. The amount of water in each bucket changes from $(0,2,2)$ to $(2,2,0)$.

The second query makes $X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$, and we obtain $A=(1,1,2,2),B=(2,2,0,3)$.

In this case, the goal cannot be achieved no matter how operations are performed.

The third query makes $X=\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ \end{pmatrix}$, and we obtain $A=(1,1,2,2,2),B=(2,2,0,1,3)$.

In this case, the goal can be achieved by the following sequence of operations, for example.

- Set $i = 1,j = 2$. The amount of water in each bucket changes from $(1,1,2,2,2)$ to $(0,2,2,2,2)$.
- Set $i = 3,j = 1$. The amount of water in each bucket changes from $(0,2,2,2,2)$ to $(2,2,0,2,2)$.
- Set $i = 4,j = 5$. The amount of water in each bucket changes from $(2,2,0,2,2)$ to $(2,2,0,1,3)$.

## Sample Input 2

```text
4 10
45636788580181785 16131322312654301 43477244591521823 6505049084010674 86530627327096446
95921187347997793 55491565467039163 87684565747362311 80318628430974482 12308092878301956
75570615154690027 96403707363045776 14150012766408204 6612197700307407 64417022692908525
5530468643826479 41731276604630756 15675296751519388 59461896803210859 66666666666666666
72767956047192820 18258893791516726 58852629621892634 33333333333333333 29923985408775019
2 1 26541245644686826
2 4 29485791833729050
4 1 21832826336874318
3 2 4953499115446612
2 0 69217973349997921
2 4 23133150029036944
3 4 55834224798559242
1 2 98517007615469735
2 3 3768060024403703
0 4 87241661746072372
```

## Sample Output 2

```text
No
Yes
No
Yes
No
Yes
No
No
No
No
```
