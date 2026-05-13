# B - Sensor Data Logging

Source: https://atcoder.jp/contests/abc453/tasks/abc453_b?lang=en

Score : $200$ points

### Problem Statement

In a certain measurement, the sensor readings at times $0,1,\dots,T$ are recorded according to the following rules.

-   At time $0$, the reading is saved.
-   At times $1,2,\dots,T$, the reading is saved if and only if the absolute difference between the current reading and the most recently saved reading is at least $X$.

The sensor reading at time $i=0,1,\dots,T$ was $A_i$.

Output the times at which readings were saved and the saved values, in ascending order of time.

### Constraints

-   $1 \le T \le 100$
-   $1 \le X \le 100$
-   $0 \le A_i \le 100$
-   All input values are integers.

### Input

The input is given from Standard Input in the following format:

```text
$T$ $X$
$A_0$ $A_1$ $\dots$ $A_T$
```

### Output

If $k$ readings were saved, and the $i$\-th saved reading in ascending order of time was at time $t_i$ with value $a_i$, output in the following format:

```text
$t_1$ $a_1$
$t_2$ $a_2$
$\vdots$
$t_k$ $a_k$
```

### Sample Input 1

```text
6 10
30 35 40 21 30 12 31
```

### Sample Output 1

```text
0 30
2 40
3 21
6 31
```

The measurement proceeds as follows.

-   The reading at time $0$ is $30$. Save it.
-   The reading at time $1$ is $35$. The most recently saved reading is $30$, and the absolute difference is less than $10$, so it is not saved.
-   The reading at time $2$ is $40$. The most recently saved reading is $30$, and the absolute difference is at least $10$, so it is saved.
-   The reading at time $3$ is $21$. The most recently saved reading is $40$, and the absolute difference is at least $10$, so it is saved.
-   The reading at time $4$ is $30$. The most recently saved reading is $21$, and the absolute difference is less than $10$, so it is not saved.
-   The reading at time $5$ is $12$. The most recently saved reading is $21$, and the absolute difference is less than $10$, so it is not saved.
-   The reading at time $6$ is $31$. The most recently saved reading is $21$, and the absolute difference is at least $10$, so it is saved.
