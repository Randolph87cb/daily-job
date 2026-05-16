# F - Critical Misread

分值：$525$ 分

---

### Problem Statement

You are given $K$ strings $S_i$ consisting of lowercase English letters.  
Find the number, modulo $998244353$, of strings of length $N$ consisting of lowercase English letters that do not contain any of $S_1, S_2, \dots, S_K$ as a substring (contiguous subsequence).

给定 $K$ 个由小写英文字母组成的字符串 $S_i$。
求所有长度为 $N$、由小写英文字母组成，且不以任何 $S_1, S_2, \dots, S_K$ 作为子串（连续子序列）的字符串的数量，答案对 $998244353$ 取模。

---

### Constraints

-   $N$ is an integer between $1$ and $10^9$, inclusive.
-   $K$ is an integer between $1$ and $10$, inclusive.
-   $S_i$ is a string consisting of lowercase English letters with length between $1$ and $10$, inclusive.

-   $N$ 是一个介于 $1$ 和 $10^9$ 之间的整数（包含两端）。
-   $K$ 是一个介于 $1$ 和 $10$ 之间的整数（包含两端）。
-   $S_i$ 是一个由小写英文字母组成的字符串，长度在 $1$ 到 $10$ 之间（包含两端）。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$ $K$  
$S_1$  
$S_2$  
$\vdots$  
$S_K$

---

### Output

Output the answer.

输出答案。

---

### Sample Input 1

```text
3 2
aa
ab
```

---

### Sample Output 1

```text
17474
```

---

-   The number of strings of length $3$ consisting of lowercase English letters is $26^3=17576$.
-   The number of strings of length $3$ consisting of lowercase English letters whose first two characters are `aa` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose last two characters are `aa` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose first two characters are `ab` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose last two characters are `ab` is $26$.
-   The number of strings of length $3$ consisting of lowercase English letters whose entirety is `aaa` is $1$.
-   The number of strings of length $3$ consisting of lowercase English letters whose entirety is `aab` is $1$.
-   Combining the above facts, it can be confirmed that the answer for this test case is $17474$.

-   长度为 $3$、由小写英文字母组成的字符串共有 $26^3=17576$ 个。
-   长度为 $3$、由小写英文字母组成，且前两个字符为 `aa` 的字符串共有 $26$ 个。
-   长度为 $3$、由小写英文字母组成，且最后两个字符为 `aa` 的字符串共有 $26$ 个。
-   长度为 $3$、由小写英文字母组成，且前两个字符为 `ab` 的字符串共有 $26$ 个。
-   长度为 $3$、由小写英文字母组成，且最后两个字符为 `ab` 的字符串共有 $26$ 个。
-   长度为 $3$、由小写英文字母组成，且整个串为 `aaa` 的字符串共有 $1$ 个。
-   长度为 $3$、由小写英文字母组成，且整个串为 `aab` 的字符串共有 $1$ 个。
-   结合以上信息，可以确认该测试用例的答案为 $17474$。

---

### Sample Input 2

```text
1 1
ab
```

---

### Sample Output 2

```text
26
```

---

### Sample Input 3

```text
1000000000 10
contest
tester
error
orange
angel
elegant
antitese
sextuple
pleasure
surely
```

---

### Sample Output 3

```text
698570468
```

---

Find the count modulo $998244353$.

求数量对 $998244353$ 取模的结果。
