# A - Trimo

分值：$100$ 分

---

### Problem Statement

You are given a string $S$ of length $N$.  
Output the string obtained by removing all leading consecutive `o`s from $S$.  
If all characters in $S$ are `o`, output an empty string.

给定一个长度为 $N$ 的字符串 $S$。  
输出将 $S$ 中所有前导连续 `o` 移除后得到的字符串。  
如果 $S$ 中的所有字符都是 `o`，则输出空字符串。

---

### Constraints

-   $N$ is an integer satisfying $1 \le N \le 50$.
-   $S$ is a string of length $N$ consisting of lowercase English letters.

-   $N$ 是满足 $1 \le N \le 50$ 的整数。
-   $S$ 是长度为 $N$、由小写英文字母组成的字符串。

---

### Input

The input is given from Standard Input in the following format:

输入按以下格式从标准输入给出：

$N$  
$S$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
7
ooparts
```

---

### Sample Output 1

```text
parts
```

---

Removing all leading consecutive `o`s from `ooparts` gives `parts`.

将 `ooparts` 中所有前导连续 `o` 移除后得到 `parts`。

---

### Sample Input 2

```text
6
abcooo
```

---

### Sample Output 2

```text
abcooo
```

---

The first character may not be `o`.

第一个字符可能不是 `o`。

---

### Sample Input 3

```text
5
ooooo
```

---

### Sample Output 3

All characters may be `o`.

所有字符都可能是 `o`。
