# D - (xx)

分值：$425$ 分

---

### Problem Statement

You are given a string $A$ consisting of `(`, `x`, `)`.  
You can perform the following two types of operations on $A$ any number of times in any order.

给定一个由 `(`、`x`、`)` 组成的字符串 $A$。
你可以对 $A$ 以任意顺序执行以下两种操作任意次。

---

-   Choose one occurrence of the substring `(xx)` in $A$ and replace it with `xx`.
-   Choose one occurrence of the substring `xx` in $A$ and replace it with `(xx)`.

-   选择 $A$ 中的一个子串 `(xx)`，将其替换为 `xx`。
-   选择 $A$ 中的一个子串 `xx`，将其替换为 `(xx)`。

---

You are given a string $B$ consisting of `(`, `x`, `)`. Determine whether you can make $A$ equal to $B$.

给定一个由 `(`、`x`、`)` 组成的字符串 $B$，判断你是否可以将 $A$ 变为与 $B$ 相等。

---

You are given $T$ test cases; solve each of them.

共有 $T$ 个测试用例，你需要解决每个测试用例。

---

**What is a substring**

**什么是子串**

---

A **substring** of $S$ is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of $S$.  
For example, `ab` is a substring of `abc`, but `ac` is not a substring of `abc`.

$S$ 的**子串**是指删除 $S$ 开头零个或多个字符、末尾零个或多个字符后得到的字符串。
例如，`ab` 是 `abc` 的子串，但 `ac` 不是 `abc` 的子串。

---

### Constraints

-   $1 \leq T \leq 3 \times 10^5$
-   $A$ and $B$ are strings of length between $1$ and $2\times 10^6$, inclusive, consisting of `(`, `x`, `)`.
-   The sum of $|A| + |B|$ over all test cases is at most $2 \times 10^6$ (where $|A|$ denotes the length of $A$).

-   $1 \leq T \leq 3 \times 10^5$
-   $A$ 和 $B$ 是长度介于 $1$ 和 $2\times 10^6$ 之间（含两端）的字符串，由 `(`、`x`、`)` 组成。
-   所有测试用例的 $|A| + |B|$ 之和不超过 $2 \times 10^6$（其中 $|A|$ 表示 $A$ 的长度）。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$T$  
$\mathrm{case}_1$  
$\mathrm{case}_2$  
$\vdots$  
$\mathrm{case}_T$

---

Each test case is given in the following format:

每个测试用例按照以下格式给出：

$A$  
$B$

---

### Output

Output $T$ lines. The $i$\-th line should contain the answer to the $i$\-th test case.  
For each test case, output `Yes` if you can make $A$ equal to $B$, and `No` otherwise.

输出 $T$ 行，第 $i$ 行应包含第 $i$ 个测试用例的答案。
对于每个测试用例，如果你可以将 $A$ 变为与 $B$ 相等，则输出 `Yes`，否则输出 `No`。

---

### Sample Input 1

```text
6
(xx)x
x(xx)
(x)x
(xx)
)x()x(
)x()x(
x
(x)
(((((xx)))))x
x((((((((((xx))))))))))
((xx)xx)xx
(x((xx))x)(xx)
```

---

### Sample Output 1

```text
Yes
No
Yes
No
Yes
Yes
```

---

For example, in the first test case, you can make $A$ equal to $B$ by the following procedure:

例如，在第一个测试用例中，你可以通过如下步骤将 $A$ 变为与 $B$ 相等：

---

-   Replace the `(xx)` from the $1$st through $4$th characters of $A$ with `xx`. After this operation, $A$ is `xxx`.
-   Replace the `xx` from the $2$nd through $3$rd characters of $A$ with `(xx)`. After this operation, $A$ is `x(xx)`.

-   将 $A$ 中第 $1$ 个字符到第 $4$ 个字符组成的 `(xx)` 替换为 `xx`。操作完成后，$A$ 变为 `xxx`。
-   将 $A$ 中第 $2$ 个字符到第 $3$ 个字符组成的 `xx` 替换为 `(xx)`。操作完成后，$A$ 变为 `x(xx)`。
