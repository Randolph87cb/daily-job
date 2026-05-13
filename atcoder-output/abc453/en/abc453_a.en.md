# A - Trimo

Source: https://atcoder.jp/contests/abc453/tasks/abc453_a?lang=en

Score : $100$ points

### Problem Statement

You are given a string $S$ of length $N$.  
Output the string obtained by removing all leading consecutive `o`s from $S$.  
If all characters in $S$ are `o`, output an empty string.

### Constraints

-   $N$ is an integer satisfying $1 \le N \le 50$.
-   $S$ is a string of length $N$ consisting of lowercase English letters.

### Input

The input is given from Standard Input in the following format:

```text
$N$
$S$
```

### Output

Output the answer.

### Sample Input 1

```text
7
ooparts
```

### Sample Output 1

```text
parts
```

Removing all leading consecutive `o`s from `ooparts` gives `parts`.

### Sample Input 2

```text
6
abcooo
```

### Sample Output 2

```text
abcooo
```

The first character may not be `o`.

### Sample Input 3

```text
5
ooooo
```

### Sample Output 3

All characters may be `o`.
