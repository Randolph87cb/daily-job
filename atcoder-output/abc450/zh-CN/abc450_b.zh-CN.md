# B - Split Ticketing

分值：$200$ 分

---

### Problem Statement

There are $N$ stations $1, 2, \dots, N$, arranged in a straight line from west to east in this order.  
The AtCoder Railway train passes through these $N$ stations and runs from west to east.  
For any two integers $i, j$ satisfying $1 \leq i \lt j \leq N$, the cost of boarding the train at station $i$ and getting off at station $j$ is $C_{i,j}$.

共有 $N$ 个车站 $1, 2, \dots, N$，按从西到东的顺序排列在一条直线上。
AtCoder 铁路的列车会经过这 $N$ 个车站，从西向东行驶。
对于满足 $1 \leq i \lt j \leq N$ 的任意两个整数 $i, j$，在车站 $i$ 上车、在车站 $j$ 下车的费用为 $C_{i,j}$。

---

Determine whether there exist three integers $a, b, c$ such that:

判断是否存在三个整数 $a, b, c$ 满足以下条件：

---

-   $1 \leq a \lt b \lt c \leq N$
-   The total cost of boarding the train at station $a$, getting off at station $b$, then boarding the train again at station $b$, and getting off at station $c$ is less than the cost of boarding the train at station $a$ and getting off at station $c$.

-   $1 \leq a \lt b \lt c \leq N$
-   在车站 $a$ 上车、在车站 $b$ 下车，然后在车站 $b$ 再次上车、在车站 $c$ 下车的总费用，小于在车站 $a$ 上车、在车站 $c$ 下车的费用。

---

### Constraints

-   $3 \leq N \leq 100$
-   $1 \leq C_{i,j} \leq 10^9$
-   All input values are integers.

-   $3 \leq N \leq 100$
-   $1 \leq C_{i,j} \leq 10^9$
-   所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入以如下格式从标准输入给出：

$N$  
$C_{1,2}$ $C_{1,3}$ $\dots$ $C_{1,N}$  
$C_{2,3}$ $\dots$ $C_{2,N}$  
$\vdots$  
$C_{N-1,N}$

---

### Output

If there exist three integers $a, b, c$ satisfying the conditions, output `Yes`; otherwise, output `No`, on a single line.

如果存在三个满足条件的整数 $a, b, c$，输出 `Yes`；否则输出 `No`，占一行。

---

### Sample Input 1

```text
3
45 450
45
```

---

### Sample Output 1

```text
Yes
```

---

Choosing $(a, b, c) = (1, 2, 3)$,  
$C_{a,b}+C_{b,c}=C_{1,2}+C_{2,3}=45+45$  
$C_{a,c}=C_{1,3}=450$  
so the conditions are satisfied.

选择 $(a, b, c) = (1, 2, 3)$，
$C_{a,b}+C_{b,c}=C_{1,2}+C_{2,3}=45+45$
$C_{a,c}=C_{1,3}=450$
因此条件被满足。

---

### Sample Input 2

```text
4
25 40 65
30 55
25
```

---

### Sample Output 2

```text
No
```

---

No choice of $(a, b, c)$ satisfies the conditions.

不存在满足条件的 $(a, b, c)$ 的选择。
