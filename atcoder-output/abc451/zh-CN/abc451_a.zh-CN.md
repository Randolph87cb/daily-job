# A - illegal

分值：$100$ 分

---

### Problem Statement

In the country of AtCoder where Takahashi lives, there is a peculiar law: "You must not write a string whose length is a multiple of $5$."

在高桥居住的AtCoder国，有一条奇特的法律：「不得编写长度是$5$倍数的字符串。」

---

Takahashi wrote a string $S$. Determine whether he is violating this law.

高桥编写了一个字符串$S$，请判断他是否违反了这条法律。

---

### Constraints

-   $S$ is a string of length between $1$ and $10$, inclusive.
-   $S$ consists of lowercase English letters.

- $S$是一个长度在$1$到$10$之间（含两端）的字符串。
- $S$由小写英文字母组成。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$S$

---

### Output

If Takahashi is violating the law, output `Yes`; otherwise, output `No`.

如果高桥违反了法律，输出`Yes`，否则输出`No`。

---

### Sample Input 1

```text
legal
```

---

### Sample Output 1

```text
Yes
```

---

`legal` is a string of length $5$. Thus, Takahashi is violating the law, so output `Yes`.

`legal`的长度为$5$，因此高桥违反了法律，输出`Yes`。

---

### Sample Input 2

```text
atcoder
```

---

### Sample Output 2

```text
No
```

---

`atcoder` is a string of length $7$. Thus, Takahashi is not violating the law, so output `No`.

`atcoder`的长度为$7$，因此高桥没有违反法律，输出`No`。

---

### Sample Input 3

```text
illegal
```

---

### Sample Output 3

```text
No
```
