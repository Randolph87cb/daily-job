# A - Chompers

分值：$100$ 分

---

### Problem Statement

You are given a string $S$ consisting of lowercase English letters and a positive integer $N$. The length of $S$ is at least $2N+1$.

给定一个由小写英文字母组成的字符串 $S$ 和一个正整数 $N$。$S$ 的长度至少为 $2N+1$。

---

Find the string obtained by removing $N$ characters from the beginning and $N$ characters from the end of $S$.

求将 $S$ 删掉开头 $N$ 个字符、删掉末尾 $N$ 个字符后得到的字符串。

---

### Constraints

-   $S$ is a string consisting of lowercase English letters.
-   $N$ is an integer.
-   $2N+1 \leq |S| \leq 30$
-   $1 \leq N \leq 10$

-   $S$ 是一个由小写英文字母组成的字符串。
-   $N$ 是一个整数。
-   $2N+1 \leq |S| \leq 30$
-   $1 \leq N \leq 10$

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$S$  
$N$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
chemotherapy
3
```

---

### Sample Output 1

```text
mother
```

---

Removing the first three characters (`che`) and the last three characters (`apy`) from `chemotherapy` gives `mother`.

将 `chemotherapy` 删掉前三个字符（`che`）和后三个字符（`apy`），得到 `mother`。

---

### Sample Input 2

```text
thermometer
4
```

---

### Sample Output 2

```text
mom
```

---

### Sample Input 3

```text
burger
1
```

---

### Sample Output 3

```text
urge
```
