# C - C Stands for Center

Source: https://atcoder.jp/contests/abc458/tasks/abc458_c?lang=en

Score : $300$ points

### Problem Statement

You are given a string $S$ consisting of uppercase English letters.  
Find the number of substrings (contiguous subsequences) of $S$ that satisfy all of the following conditions.

-   It consists of an odd number of characters.
-   Its middle character is `C`. More formally, if the extracted substring consists of $l$ characters, its $((l+1)/2)$\-th character is `C`.

Even if two substrings are identical as strings, they are counted separately if they are extracted from different positions.

### Constraints

-   $S$ is a string consisting of uppercase English letters with length between $1$ and $5 \times 10^5$, inclusive.

### Input

The input is given from Standard Input in the following format:

```text
$S$
```

### Output

Output the answer.

### Sample Input 1

```text
ABCCA
```

### Sample Output 1

```text
5
```

In this input, $S=$ `ABCCA`.  
The substrings satisfying the conditions in the problem statement are the following five:

-   `ABCCA`, extracted from the $1$st to $5$th characters of $S$
-   `BCC`, extracted from the $2$nd to $4$th characters of $S$
-   `C`, extracted from the $3$rd to $3$rd characters of $S$
-   `CCA`, extracted from the $3$rd to $5$th characters of $S$
-   `C`, extracted from the $4$th to $4$th characters of $S$

### Sample Input 2

```text
XYZ
```

### Sample Output 2

```text
0
```

### Sample Input 3

```text
SMBCPROGRAMMINGCONTEST
```

### Sample Output 3

```text
11
```
