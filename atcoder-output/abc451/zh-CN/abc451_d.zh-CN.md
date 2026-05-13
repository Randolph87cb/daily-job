# D - Concat Power of 2

分值：$400$ 分

---

### Problem Statement

We call a positive integer a **good integer** if it satisfies the following condition.

我们称满足下述条件的正整数为**好整数**。

---

-   Condition: It can be obtained by choosing one or more powers of $2$ ($1, 2, 4, 8, 16, \dots$) (repetition and reordering allowed), concatenating them as strings, and interpreting the result as an integer.

- 条件：选择一个或多个$2$的幂（即$1, 2, 4, 8, 16, \dots$），允许重复选择和调整顺序，将它们按字符串形式拼接后得到的整数即为好整数。

---

Find the $N$\-th smallest good integer. It is guaranteed that the $N$\-th smallest good integer is at most $10^9$.

求第$N$小的好整数。题目保证第$N$小的好整数不超过$10^9$。

---

### Constraints

-   $N$ is a positive integer.
-   The $N$\-th smallest good integer is at most $10^9$.

- $N$是正整数。
- 第$N$小的好整数不超过$10^9$。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
10
```

---

### Sample Output 1

```text
21
```

---

Listing good integers in ascending order gives $1, 2, 4, 8, 11, 12, 14, 16, 18, 21, \dots$.

将所有好整数按升序排列后得到的序列为$1, 2, 4, 8, 11, 12, 14, 16, 18, 21, \dots$。

---

### Sample Input 2

```text
69
```

---

### Sample Output 2

```text
328
```

---

### Sample Input 3

```text
1099898
```

---

### Sample Output 3

```text
819264512
```
