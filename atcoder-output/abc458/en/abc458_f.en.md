# F - Critical Misread

Source: https://atcoder.jp/contests/abc458/tasks/abc458_f?lang=en

Score : $525$ points

### Problem Statement

You are given $K$ strings $S_i$ consisting of lowercase English letters.  
Find the number, modulo $998244353$, of strings of length $N$ consisting of lowercase English letters that do not contain any of $S_1, S_2, \dots, S_K$ as a substring (contiguous subsequence).

### Constraints

-   $N$ is an integer between $1$ and $10^9$, inclusive.
-   $K$ is an integer between $1$ and $10$, inclusive.
-   $S_i$ is a string consisting of lowercase English letters with length between $1$ and $10$, inclusive.

### Input

The input is given from Standard Input in the following format:

```text
$N$ $K$
$S_1$
$S_2$
$\vdots$
$S_K$
```

### Output

Output the answer.

### Sample Input 1

```text
3 2
aa
ab
```

### Sample Output 1

```text
17474
```

-   The number of strings of length $3$ consisting of lowercase English letters is $26^3=17576$.
-   The number of strings of length $3$ consisting of lowercase English letters whose first two characters are `aa` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose last two characters are `aa` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose first two characters are `ab` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose last two characters are `ab` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose entirety is `aaa` is $1$.
-   The number of strings of length $3$ consisting of lowercase English letters whose entirety is `aab` is $1$.
-   Combining the above facts, it can be confirmed that the answer for this test case is $17474$.

### Sample Input 2

```text
1 1
ab
```

### Sample Output 2

```text
26
```

### Sample Input 3

```text
1000000000 10
contest
tester
error
orange
angel
elegant
antitese
sextuple
pleasure
surely
```

### Sample Output 3

```text
698570468
```

Find the count modulo $998244353$.
