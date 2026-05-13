# A - Gothec

Source: https://atcoder.jp/contests/abc452/tasks/abc452_a?lang=en

Score : $100$ points

### Problem Statement

The following five days are called the five seasonal festivals (gosekku).

-   January $\color{red}{\mathbf{7}}$
-   March $3$
-   May $5$
-   July $7$
-   September $9$

If month $M$, day $D$ is one of the five seasonal festivals, output `Yes`; otherwise, output `No`.

### Constraints

-   $M$ and $D$ are integers.
-   Month $M$, day $D$ is a valid date in a leap year in the Gregorian calendar.

### Input

The input is given from Standard Input in the following format:

```text
$M$ $D$
```

### Output

If month $M$, day $D$ is one of the five seasonal festivals, output `Yes`; otherwise, output `No`.

### Sample Input 1

```text
3 3
```

### Sample Output 1

```text
Yes
```

March $3$ is one of the five seasonal festivals, so output `Yes`.

### Sample Input 2

```text
1 1
```

### Sample Output 2

```text
No
```

January $1$ is not one of the five seasonal festivals, so output `No`.

### Sample Input 3

```text
4 4
```

### Sample Output 3

```text
No
```

### Sample Input 4

```text
11 7
```

### Sample Output 4

```text
No
```
