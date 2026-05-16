# A - Chompers

Source: https://atcoder.jp/contests/abc458/tasks/abc458_a?lang=en

Score : $100$ points

### Problem Statement

You are given a string $S$ consisting of lowercase English letters and a positive integer $N$. The length of $S$ is at least $2N+1$.

Find the string obtained by removing $N$ characters from the beginning and $N$ characters from the end of $S$.

### Constraints

-   $S$ is a string consisting of lowercase English letters.
-   $N$ is an integer.
-   $2N+1 \leq |S| \leq 30$
-   $1 \leq N \leq 10$

### Input

The input is given from Standard Input in the following format:

```text
$S$
$N$
```

### Output

Output the answer.

### Sample Input 1

```text
chemotherapy
3
```

### Sample Output 1

```text
mother
```

Removing the first three characters (`che`) and the last three characters (`apy`) from `chemotherapy` gives `mother`.

### Sample Input 2

```text
thermometer
4
```

### Sample Output 2

```text
mom
```

### Sample Input 3

```text
burger
1
```

### Sample Output 3

```text
urge
```
