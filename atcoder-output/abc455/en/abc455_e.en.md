# E - Unbalanced ABC Substrings

Source: https://atcoder.jp/contests/abc455/tasks/abc455_e?lang=en

Score : $450450450$ points

### Problem Statement

You are given a string $SSS$ of length $NNN$ consisting of the three characters `A`, `B`, and `C`.  
There are $N(N+1)2\frac{N(N+1)}{2}2N(N+1)​$ non-empty substrings of $SSS$; find how many of them satisfy the following condition:

-   The numbers of occurrences of `A`, `B`, and `C` are all distinct from each other.

Count two substrings separately if they are taken from different positions in $SSS$, even if they are identical as strings.

**What is a substring?**

A **substring** of $SSS$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $SSS$. For example, `AB` is a substring of `ABC`, but `AC` is not a substring of `ABC`.

### Constraints

-   $1≤N≤2×1051 \leq N \leq 2 \times 10^51≤N≤2×105$
-   $∣S∣=N|S|=N∣S∣=N$
-   $NNN$ is an integer.
-   $SSS$ is a string consisting of the three characters `A`, `B`, and `C`.

### Input

The input is given from Standard Input in the following format:

```text
$NNN$
$SSS$
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

Deleting $000$ characters from the beginning and $333$ characters from the end of $SSS$ gives `AAB`, which satisfies the condition.  
Deleting $111$ character from the beginning and $222$ characters from the end of $SSS$ gives `ABB`, which satisfies the condition.  
Deleting $222$ characters from the beginning and $111$ character from the end of $SSS$ gives `BBC`, which satisfies the condition.  
Deleting $333$ characters from the beginning and $000$ characters from the end of $SSS$ gives `BCC`, which satisfies the condition.  
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
