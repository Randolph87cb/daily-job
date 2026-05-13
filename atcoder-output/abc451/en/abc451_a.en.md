# A - illegal

Source: https://atcoder.jp/contests/abc451/tasks/abc451_a?lang=en

Score : $100$ points

### Problem Statement

In the country of AtCoder where Takahashi lives, there is a peculiar law: "You must not write a string whose length is a multiple of $5$."

Takahashi wrote a string $S$. Determine whether he is violating this law.

### Constraints

-   $S$ is a string of length between $1$ and $10$, inclusive.
-   $S$ consists of lowercase English letters.

### Input

The input is given from Standard Input in the following format:

```text
$S$
```

### Output

If Takahashi is violating the law, output `Yes`; otherwise, output `No`.

### Sample Input 1

```text
legal
```

### Sample Output 1

```text
Yes
```

`legal` is a string of length $5$. Thus, Takahashi is violating the law, so output `Yes`.

### Sample Input 2

```text
atcoder
```

### Sample Output 2

```text
No
```

`atcoder` is a string of length $7$. Thus, Takahashi is not violating the law, so output `No`.

### Sample Input 3

```text
illegal
```

### Sample Output 3

```text
No
```
