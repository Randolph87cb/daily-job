# E - Tree Distance

分值：$475$ 分

---

### Problem Statement

Determine whether there exists a weighted undirected tree with $N$ vertices satisfying the following condition.

判断是否存在一个含有 $N$ 个顶点的带权无向树满足以下条件。

---

-   For any two integers $i$ and $j$ with $1 \le i \lt j \le N$, the distance between vertices $i$ and $j$ is $A_{i,j}$.

- 对于任意满足 $1 \le i \lt j \le N$ 的整数 $i$ 和 $j$，顶点 $i$ 和 $j$ 之间的距离为 $A_{i,j}$。

---

Here, the distance between vertices $i$ and $j$ is defined as the sum of the weights of the edges on the unique simple path connecting these two vertices.

其中，顶点 $i$ 和 $j$ 之间的距离定义为连接这两个顶点的唯一简单路径上的所有边的权值之和。

---

### Constraints

-   $2 \le N \le 3000$
-   $1 \le A_{i,j} \le 9999$
-   All input values are integers.

- $2 \le N \le 3000$
- $1 \le A_{i,j} \le 9999$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$N$  
$A_{1, 2}$ $A_{1, 3}$ $\ldots$ $A_{1, N}$  
$A_{2, 3}$ $\ldots$ $A_{2, N}$  
$\vdots$  
$A_{N-1,N}$

---

### Output

If a tree satisfying the condition exists, output `Yes`; otherwise, output `No`.

如果存在满足条件的树，输出 `Yes`；否则输出 `No`。

---

### Sample Input 1

```text
4
2 5 4
3 2
5
```

---

### Sample Output 1

```text
Yes
```

---

For example, the tree with the following edges satisfies the condition.

例如，包含以下边的树满足该条件。

---

-   Edge $(1, 2)$ has weight $2$.
-   Edge $(2, 3)$ has weight $3$.
-   Edge $(2, 4)$ has weight $2$.

- 边 $(1, 2)$ 的权值为 $2$。
- 边 $(2, 3)$ 的权值为 $3$。
- 边 $(2, 4)$ 的权值为 $2$。

---

Thus, output `Yes`.

因此，输出 `Yes`。

---

### Sample Input 2

```text
4
2 5 4
3 2
6
```

---

### Sample Output 2

```text
No
```

---

No tree satisfying the condition exists. Thus, output `No`.

不存在满足条件的树。因此，输出 `No`。

---

### Sample Input 3

```text
10
1039 1802 3781 231 5828 1944 392 262 1481
763 2742 1270 4789 905 1431 1301 442
1979 2033 5552 142 2194 2064 1205
4012 7531 2121 4173 4043 3184
6059 2175 161 493 1712
5694 6220 6090 5231
2336 2206 1347
654 1873
1743
```

---

### Sample Output 3

```text
Yes
```
