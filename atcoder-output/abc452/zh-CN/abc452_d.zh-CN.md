# D - No-Subsequence Substring

分值：$400$ 分

---

### Problem Statement

You are given strings $S$ and $T$ consisting of lowercase English letters.

给定由小写英文字母组成的字符串 $S$ 和 $T$。

---

Among the non-empty substrings $s$ of $S$, count those that do **not** contain $T$ as a (not necessarily contiguous) subsequence.

统计 $S$ 的所有非空子串 $s$ 中，**不**包含 $T$ 作为（不一定连续的）子序列的数量。

---

Here, two substrings of $S$ are distinguished if they are taken from different positions, even if they are equal as strings.

这里，只要两个子串在 $S$ 中的位置不同，即使它们的字符串内容相同，也视为不同的子串。

---

**What is a substring?**

**什么是子串？**

---

A substring of a string $X$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $X$.

字符串 $X$ 的子串是指从 $X$ 的开头删除零个或多个字符，再从末尾删除零个或多个字符后得到的字符串。

---

**What is a subsequence?**

**什么是子序列？**

---

A subsequence of a string $X$ is a string obtained by deleting zero or more elements from $X$ and arranging the remaining elements in their original order.

字符串 $X$ 的子序列是指从 $X$ 中删除零个或多个元素，并将剩余元素保持原有顺序排列后得到的字符串。

---

### Constraints

-   $S$ is a string consisting of lowercase English letters.
-   $1\le |S|\le2\times10 ^ 5$, where $|S|$ is the length of $S$.
-   $T$ is a string consisting of lowercase English letters.
-   $1\le |T|\le50$, where $|T|$ is the length of $T$.

- $S$ 是由小写英文字母组成的字符串。
- $1\le |S|\le2\times10 ^ 5$，其中 $|S|$ 是 $S$ 的长度。
- $T$ 是由小写英文字母组成的字符串。
- $1\le |T|\le50$，其中 $|T|$ 是 $T$ 的长度。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$S$  
$T$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
abrakadabra
aba
```

---

### Sample Output 1

```text
51
```

---

For example, the substring `abr` consisting of the first through third characters of $S$ does not contain $T$ as a subsequence. Including this, there are $51$ substrings satisfying the condition, such as `k` (only the fifth character of $S$) and `akada` (the fourth through eighth characters of $S$).

例如，由 $S$ 的第 1 到第 3 个字符组成的子串 `abr` 不包含 $T$ 作为子序列。包括这个子串在内，共有 $51$ 个满足条件的子串，例如 `k`（仅 $S$ 的第 5 个字符）和 `akada`（$S$ 的第 4 到第 8 个字符）。

---

Note that the string `abr` can be obtained both as the substring from the first to third characters of $S$ and as the substring from the eighth to tenth characters of $S$, but they are taken from different positions, so they are counted separately.

注意，字符串 `abr` 既可以作为 $S$ 第 1 到第 3 个字符的子串得到，也可以作为 $S$ 第 8 到第 10 个字符的子串得到，但由于它们的位置不同，所以会被分别计数。

---

### Sample Input 2

```text
aaaaa
a
```

---

### Sample Output 2

```text
0
```

---

All non-empty substrings of $S$ contain $T$ as a subsequence.

$S$ 的所有非空子串都包含 $T$ 作为子序列。

---

Thus, there are no substrings satisfying the condition, so output $0$.

因此没有满足条件的子串，输出 $0$。

---

### Sample Input 3

```text
rdddrdtdcdrrdcredctdordoeecrotet
dcre
```

---

### Sample Output 3

```text
263
```
