# D - (xx)

Source: https://atcoder.jp/contests/abc454/tasks/abc454_d?lang=en

Score : $425$ points

### Problem Statement

You are given a string $A$ consisting of `(`, `x`, `)`.  
You can perform the following two types of operations on $A$ any number of times in any order.

-   Choose one occurrence of the substring `(xx)` in $A$ and replace it with `xx`.
-   Choose one occurrence of the substring `xx` in $A$ and replace it with `(xx)`.

You are given a string $B$ consisting of `(`, `x`, `)`. Determine whether you can make $A$ equal to $B$.

You are given $T$ test cases; solve each of them.

**What is a substring**

A **substring** of $S$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $S$.  
For example, `ab` is a substring of `abc`, but `ac` is not a substring of `abc`.

### Constraints

-   $1 \leq T \leq 3 \times 10^5$
-   $A$ and $B$ are strings of length between $1$ and $2\times 10^6$, inclusive, consisting of `(`, `x`, `)`.
-   The sum of $|A| + |B|$ over all test cases is at most $2 \times 10^6$ (where $|A|$ denotes the length of $A$).

### Input

The input is given from Standard Input in the following format:

```text
$T$
$\mathrm{case}_1$
$\mathrm{case}_2$
$\vdots$
$\mathrm{case}_T$
```

Each test case is given in the following format:

```text
$A$
$B$
```

### Output

Output $T$ lines. The $i$\-th line should contain the answer to the $i$\-th test case.  
For each test case, output `Yes` if you can make $A$ equal to $B$, and `No` otherwise.

### Sample Input 1

```text
6
(xx)x
x(xx)
(x)x
(xx)
)x()x(
)x()x(
x
(x)
(((((xx)))))x
x((((((((((xx))))))))))
((xx)xx)xx
(x((xx))x)(xx)
```

### Sample Output 1

```text
Yes
No
Yes
No
Yes
Yes
```

For example, in the first test case, you can make $A$ equal to $B$ by the following procedure:

-   Replace the `(xx)` from the $1$st through $4$th characters of $A$ with `xx`. After this operation, $A$ is `xxx`.
-   Replace the `xx` from the $2$nd through $3$rd characters of $A$ with `(xx)`. After this operation, $A$ is `x(xx)`.
