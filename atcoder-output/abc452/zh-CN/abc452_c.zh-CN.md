# C - Fishbones

分值：$300$ 分

---

### Problem Statement

Artist Takasago has created an object in the shape of a fish skeleton.

艺术家高砂创作了一个鱼骨架形状的艺术品。

---

The object consists of $N$ ribs and one spine. The ribs are numbered $1$ through $N$.

该艺术品由 $N$ 根肋骨和一根脊椎组成。肋骨编号为 $1$ 到 $N$。

---

He wants to write one string on each of the $N+1$ bones, satisfying all of the following conditions.

他希望在 $N+1$ 根骨头上各写一个字符串，满足以下所有条件。

---

-   The length of the string written on the spine is $N$.
-   For each rib $i = 1, \dots, N$, the following hold.
    -   The length of the string written on rib $i$ is $A_i$.
    -   The $B_i$\-th character of the string written on rib $i$ equals the $i$\-th character of the string written on the spine.
-   Each of the strings written on the $N+1$ bones is one of $S_1, \cdots, S_M$ (duplicates allowed).

- 写在脊椎上的字符串长度为 $N$。
- 对每根肋骨 $i = 1, \dots, N$，满足以下要求：
  - 写在肋骨 $i$ 上的字符串长度为 $A_i$。
  - 肋骨 $i$ 上字符串的第 $B_i$ 个字符与脊椎上字符串的第 $i$ 个字符相同。
- 写在 $N+1$ 根骨头上的每个字符串都属于 $S_1, \cdots, S_M$（允许重复）。

---

$S_1, \cdots, S_M$ are strings consisting of lowercase English letters, and they are all distinct.

$S_1, \cdots, S_M$ 是由小写英文字母组成的字符串，且两两互不相同。

---

For each $j = 1, \cdots, M$, answer the following question.

对每个 $j = 1, \cdots, M$，回答以下问题。

---

-   Among the ways to write strings satisfying the conditions, is there one where the string written on the spine is $S_j$?

- 在所有满足条件的字符串书写方案中，是否存在一种方案使得脊椎上的字符串为 $S_j$？

---

### Constraints

-   $N$ is an integer.
-   $1 \leq N \leq 10$
-   $A_i$ and $B_i$ are integers. ($1 \leq i \leq N$)
-   $1 \leq B_i \leq A_i \leq 10$ ($1 \leq i \leq N$)
-   $M$ is an integer.
-   $1 \leq M \leq 200\,000$
-   $S_j$ is a string consisting of lowercase English letters. ($1 \leq j \leq M$)
-   $1 \leq |S_j| \leq 10$ ($1 \leq j \leq M$)
-   $S_1, \cdots, S_M$ are pairwise distinct.

- $N$ 是一个整数。
- $1 \leq N \leq 10$
- $A_i$ 和 $B_i$ 是整数。（$1 \leq i \leq N$）
- $1 \leq B_i \leq A_i \leq 10$（$1 \leq i \leq N$）
- $M$ 是一个整数。
- $1 \leq M \leq 200\,000$
- $S_j$ 是由小写英文字母组成的字符串。（$1 \leq j \leq M$）
- $1 \leq |S_j| \leq 10$（$1 \leq j \leq M$）
- $S_1, \cdots, S_M$ 两两互不相同。

---

### Input

The input is given from Standard Input in the following format:

输入按以下格式从标准输入给出：

$N$  
$A_1$ $B_1$  
$\vdots$  
$A_N$ $B_N$  
$M$  
$S_1$  
$\vdots$  
$S_M$

---

### Output

Output $M$ lines.

输出 $M$ 行。

---

The $j$\-th line ($1 \leq j \leq M$) should contain `Yes` if there exists a way to write strings satisfying the conditions with $S_j$ written on the spine, and `No` otherwise.

第 $j$ 行（$1 \leq j \leq M$）中，如果存在满足条件的书写方案使得脊椎上写的是 $S_j$，则输出 `Yes`，否则输出 `No`。

---

### Sample Input 1

```text
5
5 3
5 2
4 1
5 1
3 2
8
retro
chris
itchy
tuna
crab
rock
cod
ash
```

---

### Sample Output 1

```text
Yes
Yes
No
No
No
No
No
No
```

---

By writing `chris`, `retro`, `tuna`, `retro`, `cod` on ribs $1,2,3,4,5$ respectively, the conditions are satisfied with `retro` written on the spine.

在肋骨 $1,2,3,4,5$ 上分别写下 `chris`、`retro`、`tuna`、`retro`、`cod`，即可满足条件，此时脊椎上写的是 `retro`。

---

![](https://img.atcoder.jp/abc452/28d388773281d2bb1e90cd50063b6539.png)

![](https://img.atcoder.jp/abc452/28d388773281d2bb1e90cd50063b6539.png)

---

-   The length of `retro` is $5$.
-   For each rib, the following hold.
    -   The string written on rib $1$ is `chris`, which has length $5$. Its third character is `r`, which equals the first character of `retro`.
    -   The string written on rib $2$ is `retro`, which has length $5$. Its second character is `e`, which equals the second character of `retro`.
    -   The string written on rib $3$ is `tuna`, which has length $4$. Its first character is `t`, which equals the third character of `retro`.
    -   The string written on rib $4$ is `retro`, which has length $5$. Its first character is `r`, which equals the fourth character of `retro`.
    -   The string written on rib $5$ is `cod`, which has length $3$. Its second character is `o`, which equals the fifth character of `retro`.

- `retro` 的长度为 $5$。
- 对每根肋骨，满足以下要求：
  - 肋骨 $1$ 上写的字符串是 `chris`，长度为 $5$。它的第三个字符是 `r`，与 `retro` 的第一个字符相同。
  - 肋骨 $2$ 上写的字符串是 `retro`，长度为 $5$。它的第二个字符是 `e`，与 `retro` 的第二个字符相同。
  - 肋骨 $3$ 上写的字符串是 `tuna`，长度为 $4$。它的第一个字符是 `t`，与 `retro` 的第三个字符相同。
  - 肋骨 $4$ 上写的字符串是 `retro`，长度为 $5$。它的第一个字符是 `r`，与 `retro` 的第四个字符相同。
  - 肋骨 $5$ 上写的字符串是 `cod`，长度为 $3$。它的第二个字符是 `o`，与 `retro` 的第五个字符相同。

---

By writing `itchy`, `chris`, `rock`, `itchy`, `ash` on ribs $1,2,3,4,5$ respectively, the conditions are satisfied with `chris` written on the spine.

在肋骨 $1,2,3,4,5$ 上分别写下 `itchy`、`chris`、`rock`、`itchy`、`ash`，即可满足条件，此时脊椎上写的是 `chris`。

---

![](https://img.atcoder.jp/abc452/5323501d2dc7ce95e9216d1c20484be5.png)

![](https://img.atcoder.jp/abc452/5323501d2dc7ce95e9216d1c20484be5.png)

---

### Sample Input 2

```text
5
5 1
5 2
5 3
5 4
5 5
8
retro
chris
itchy
tuna
crab
rock
cod
ash
```

---

### Sample Output 2

```text
Yes
Yes
Yes
No
No
No
No
No
```
