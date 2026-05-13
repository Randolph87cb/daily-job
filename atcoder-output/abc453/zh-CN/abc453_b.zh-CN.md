# B - Sensor Data Logging

分值：$200$ 分

---

### Problem Statement

In a certain measurement, the sensor readings at times $0,1,\dots,T$ are recorded according to the following rules.

在某次测量中，时刻 $0,1,\dots,T$ 的传感器读数按照以下规则记录。

---

-   At time $0$, the reading is saved.
-   At times $1,2,\dots,T$, the reading is saved if and only if the absolute difference between the current reading and the most recently saved reading is at least $X$.

- 在时刻 $0$，读数一定会被保存。
- 对于时刻 $1,2,\dots,T$，当且仅当当前读数与最近一次保存的读数的绝对差至少为 $X$ 时，该读数才会被保存。

---

The sensor reading at time $i=0,1,\dots,T$ was $A_i$.

时刻 $i=0,1,\dots,T$ 的传感器读数为 $A_i$。

---

Output the times at which readings were saved and the saved values, in ascending order of time.

按时间升序输出所有保存了读数的时刻，以及对应的保存值。

---

### Constraints

-   $1 \le T \le 100$
-   $1 \le X \le 100$
-   $0 \le A_i \le 100$
-   All input values are integers.

- $1 \le T \le 100$
- $1 \le X \le 100$
- $0 \le A_i \le 100$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入从标准输入按照以下格式给出：

$T$ $X$  
$A_0$ $A_1$ $\dots$ $A_T$

---

### Output

If $k$ readings were saved, and the $i$\-th saved reading in ascending order of time was at time $t_i$ with value $a_i$, output in the following format:

假设共保存了 $k$ 个读数，其中按时间升序的第 $i$ 个读数的保存时刻为 $t_i$、数值为 $a_i$，请按照以下格式输出：

---

```text
$t_1$ $a_1$
$t_2$ $a_2$
$\vdots$
$t_k$ $a_k$
```

```text
$t_1$ $a_1$
$t_2$ $a_2$
$\vdots$
$t_k$ $a_k$
```

---

### Sample Input 1

```text
6 10
30 35 40 21 30 12 31
```

---

### Sample Output 1

```text
0 30
2 40
3 21
6 31
```

---

The measurement proceeds as follows.

测量过程如下。

---

-   The reading at time $0$ is $30$. Save it.
-   The reading at time $1$ is $35$. The most recently saved reading is $30$, and the absolute difference is less than $10$, so it is not saved.
-   The reading at time $2$ is $40$. The most recently saved reading is $30$, and the absolute difference is at least $10$, so it is saved.
-   The reading at time $3$ is $21$. The most recently saved reading is $40$, and the absolute difference is at least $10$, so it is saved.
-   The reading at time $4$ is $30$. The most recently saved reading is $21$, and the absolute difference is less than $10$, so it is not saved.
-   The reading at time $5$ is $12$. The most recently saved reading is $21$, and the absolute difference is less than $10$, so it is not saved.
-   The reading at time $6$ is $31$. The most recently saved reading is $21$, and the absolute difference is at least $10$, so it is saved.

- 时刻 $0$ 的读数为 $30$，保存该读数。
- 时刻 $1$ 的读数为 $35$，最近一次保存的读数为 $30$，两者绝对差小于 $10$，因此不保存。
- 时刻 $2$ 的读数为 $40$，最近一次保存的读数为 $30$，两者绝对差至少为 $10$，因此保存该读数。
- 时刻 $3$ 的读数为 $21$，最近一次保存的读数为 $40$，两者绝对差至少为 $10$，因此保存该读数。
- 时刻 $4$ 的读数为 $30$，最近一次保存的读数为 $21$，两者绝对差小于 $10$，因此不保存。
- 时刻 $5$ 的读数为 $12$，最近一次保存的读数为 $21$，两者绝对差小于 $10$，因此不保存。
- 时刻 $6$ 的读数为 $31$，最近一次保存的读数为 $21$，两者绝对差至少为 $10$，因此保存该读数。
