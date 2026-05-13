# D - No-Subsequence Substring

Source: https://atcoder.jp/contests/abc452/tasks/abc452_d?lang=en

Score : $400$ points

### Problem Statement

You are given strings $S$ and $T$ consisting of lowercase English letters.

Among the non-empty substrings $s$ of $S$, count those that do **not** contain $T$ as a (not necessarily contiguous) subsequence.

Here, two substrings of $S$ are distinguished if they are taken from different positions, even if they are equal as strings.

**What is a substring?**

A substring of a string $X$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $X$.

 

**What is a subsequence?**

A subsequence of a string $X$ is a string obtained by deleting zero or more elements from $X$ and arranging the remaining elements in their original order.

### Constraints

-   $S$ is a string consisting of lowercase English letters.
-   $1\le |S|\le2\times10 ^ 5$, where $|S|$ is the length of $S$.
-   $T$ is a string consisting of lowercase English letters.
-   $1\le |T|\le50$, where $|T|$ is the length of $T$.

### Input

The input is given from Standard Input in the following format:

```text
$S$
$T$
```

### Output

Output the answer.

### Sample Input 1

```text
abrakadabra
aba
```

### Sample Output 1

```text
51
```

For example, the substring `abr` consisting of the first through third characters of $S$ does not contain $T$ as a subsequence. Including this, there are $51$ substrings satisfying the condition, such as `k` (only the fifth character of $S$) and `akada` (the fourth through eighth characters of $S$).

Note that the string `abr` can be obtained both as the substring from the first to third characters of $S$ and as the substring from the eighth to tenth characters of $S$, but they are taken from different positions, so they are counted separately.

### Sample Input 2

```text
aaaaa
a
```

### Sample Output 2

```text
0
```

All non-empty substrings of $S$ contain $T$ as a subsequence.

Thus, there are no substrings satisfying the condition, so output $0$.

### Sample Input 3

```text
rdddrdtdcdrrdcredctdordoeecrotet
dcre
```

### Sample Output 3

```text
263
```
