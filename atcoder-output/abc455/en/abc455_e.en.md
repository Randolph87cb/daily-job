# E - Unbalanced ABC Substrings

Source: https://atcoder.jp/contests/abc455/tasks/abc455_e?lang=en

Score : $450$ points

### Problem Statement

You are given a string $S$ of length $N$ consisting of the three characters `A`, `B`, and `C`.  
There are $\frac{N(N+1)}{2}$ non-empty substrings of $S$; find how many of them satisfy the following condition:

-   The numbers of occurrences of `A`, `B`, and `C` are all distinct from each other.

Count two substrings separately if they are taken from different positions in $S$, even if they are identical as strings.

**What is a substring?**

A **substring** of $S$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $S$. For example, `AB` is a substring of `ABC`, but `AC` is not a substring of `ABC`.

### Constraints

-   $1 \leq N \leq 2 \times 10^5$
-   $|S|=N$
-   $N$ is an integer.
-   $S$ is a string consisting of the three characters `A`, `B`, and `C`.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$S$
```

### Output

Output the answer on a single line.

### Sample Input 1

```text
6
AABBCC
```

### Sample Output 1

```text
4
```

Deleting $0$ characters from the beginning and $3$ characters from the end of $S$ gives `AAB`, which satisfies the condition.  
Deleting $1$ character from the beginning and $2$ characters from the end of $S$ gives `ABB`, which satisfies the condition.  
Deleting $2$ characters from the beginning and $1$ character from the end of $S$ gives `BBC`, which satisfies the condition.  
Deleting $3$ characters from the beginning and $0$ characters from the end of $S$ gives `BCC`, which satisfies the condition.  
No other substrings satisfy the condition.

### Sample Input 2

```text
6
ABCABC
```

### Sample Output 2

```text
0
```

No substring satisfies the condition.

### Sample Input 3

```text
10
ACABCAABAB
```

### Sample Output 3

```text
17
```
