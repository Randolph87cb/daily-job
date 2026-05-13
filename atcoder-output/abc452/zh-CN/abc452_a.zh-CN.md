# A - Gothec

分值：$100$ 分

---

### Problem Statement

The following five days are called the five seasonal festivals (gosekku).

以下五天被称为五节句（gosekku）。

---

-   January $\color{red}{\mathbf{7}}$
-   March $3$
-   May $5$
-   July $7$
-   September $9$

-   一月 $\color{red}{\mathbf{7}}$ 日
-   三月 $3$ 日
-   五月 $5$ 日
-   七月 $7$ 日
-   九月 $9$ 日

---

If month $M$, day $D$ is one of the five seasonal festivals, output `Yes`; otherwise, output `No`.

如果 $M$ 月 $D$ 日是五节句之一，输出 `Yes`，否则输出 `No`。

---

### Constraints

-   $M$ and $D$ are integers.
-   Month $M$, day $D$ is a valid date in a leap year in the Gregorian calendar.

-   $M$ 和 $D$ 是整数。
-   $M$ 月 $D$ 日是公历闰年中的有效日期。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$M$ $D$

---

### Output

If month $M$, day $D$ is one of the five seasonal festivals, output `Yes`; otherwise, output `No`.

如果 $M$ 月 $D$ 日是五节句之一，输出 `Yes`，否则输出 `No`。

---

### Sample Input 1

```text
3 3
```

---

### Sample Output 1

```text
Yes
```

---

March $3$ is one of the five seasonal festivals, so output `Yes`.

三月 $3$ 日是五节句之一，因此输出 `Yes`。

---

### Sample Input 2

```text
1 1
```

---

### Sample Output 2

```text
No
```

---

January $1$ is not one of the five seasonal festivals, so output `No`.

一月 $1$ 日不是五节句之一，因此输出 `No`。

---

### Sample Input 3

```text
4 4
```

---

### Sample Output 3

```text
No
```

---

### Sample Input 4

```text
11 7
```

---

### Sample Output 4

```text
No
```
