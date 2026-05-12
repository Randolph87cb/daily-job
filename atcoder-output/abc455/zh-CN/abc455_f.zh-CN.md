# F - Merge Slimes 2

分值：$525525525$ 分

---

### Problem Statement

There is a sequence $AAA$ of $NNN$ non-negative integers, all initially $000$. Process $QQQ$ queries given in order.  
For the $qqq$\-th query, you are given integers $lq,rql_q, r_qlq​,rq​$ satisfying $1≤lq≤rq≤N1 \leq l_q \leq r_q \leq N1≤lq​≤rq​≤N$ and a positive integer $aqa_qaq​$. Perform the following in order:

有一个长度为 $NNN$ 的非负整数序列 $AAA$，初始时所有元素均为 $000$。请按顺序处理 $QQQ$ 个查询。
对于第 $qqq$ 个查询，给定满足 $1≤lq≤rq≤N1 \leq l_q \leq r_q \leq N1≤lq​≤rq​≤N$ 的整数 $lq,rql_q, r_qlq​,rq​$ 和一个正整数 $aqa_qaq​$，请按顺序执行以下操作：

---

-   Add $aqa_qaq​$ to each of $Alq,Alq+1,…,ArqA_{l_q}, A_{{l_q}+1}, \dots, A_{r_q}Alq​​,Alq​+1​,…,Arq​​$.
-   Then, letting $M=rq−lq+1M=r_q-l_q+1M=rq​−lq​+1$ and $B=(B1,B2,…,BM)=(Alq,Alq+1,…,Arq)B=(B_1,B_2,\dots,B_M)=(A_{l_q}, A_{l_q+1}, \dots, A_{r_q})B=(B1​,B2​,…,BM​)=(Alq​​,Alq​+1​,…,Arq​​)$, find the answer to the following problem:

- 给 $Alq,Alq+1,…,ArqA_{l_q}, A_{{l_q}+1}, \dots, A_{r_q}Alq​​,Alq​+1​,…,Arq​​$ 中的每个元素都加上 $aqa_qaq​$。
- 然后，设 $M=rq−lq+1M=r_q-l_q+1M=rq​−lq​+1$ 和 $B=(B1,B2,…,BM)=(Alq,Alq+1,…,Arq)B=(B_1,B_2,\dots,B_M)=(A_{l_q}, A_{l_q+1}, \dots, A_{r_q})B=(B1​,B2​,…,BM​)=(Alq​​,Alq​+1​,…,Arq​​)$，求解以下问题的答案：

---

> There are $MMM$ slimes $1,2,…,M1,2,\dots,M1,2,…,M$, where the $mmm$\-th slime has weight $BmB_mBm​$.  
> Repeat the operation of choosing two slimes and merging them $M−1M-1M−1$ times.  
> When slimes of weights $xxx$ and $yyy$ are merged, a slime of weight $x+yx+yx+y$ appears and the original two slimes disappear. This incurs a cost of $x×yx \times yx×y$.  
> Find, modulo $998244353998244353998244353$, the minimum possible total cost of the $M−1M-1M−1$ operations.

> 有 $MMM$ 只史莱姆 $1,2,…,M1,2,\dots,M1,2,…,M$，其中第 $mmm$ 只史莱姆的重量为 $BmB_mBm​$。
> 重复执行选择两只史莱姆进行合并的操作共 $M−1M-1M−1$ 次。
> 当重量为 $xxx$ 和 $yyy$ 的史莱姆合并时，会产生一只重量为 $x+yx+yx+y$ 的史莱姆，原来的两只史莱姆消失，该操作会产生 $x×yx \times yx×y$ 的代价。
> 求 $M−1M-1M−1$ 次操作的最小总代价，结果对 $998244353998244353998244353$ 取模。

---

Note that the changes made on $AAA$ in each query carry over to subsequent queries.

注意每个查询中对 $AAA$ 所做的修改会延续到后续的查询中。

---

### Constraints

-   $1≤N≤1051 \leq N \leq 10^51≤N≤105$
-   $1≤Q≤1051 \leq Q \leq 10^51≤Q≤105$
-   $1≤lq≤rq≤N1 \leq l_q \leq r_q \leq N1≤lq​≤rq​≤N$
-   $1≤aq≤1091 \leq a_q \leq 10^91≤aq​≤109$
-   All input values are integers.

- $1≤N≤1051 \leq N \leq 10^51≤N≤105$
- $1≤Q≤1051 \leq Q \leq 10^51≤Q≤105$
- $1≤lq≤rq≤N1 \leq l_q \leq r_q \leq N1≤lq​≤rq​≤N$
- $1≤aq≤1091 \leq a_q \leq 10^91≤aq​≤109$
- 所有输入值均为整数。

---

### Input

The input is given from Standard Input in the following format:

输入按照以下格式从标准输入给出：

$NNN$ $QQQ$  
$l1l_1l1​$ $r1r_1r1​$ $a1a_1a1​$  
$l2l_2l2​$ $r2r_2r2​$ $a2a_2a2​$  
$⋮\vdots⋮$  
$lQl_QlQ​$ $rQr_QrQ​$ $aQa_QaQ​$

---

### Output

Output the answers over $QQQ$ lines in total. The $qqq$\-th line should contain the answer to the $qqq$\-th query.

总共输出 $QQQ$ 行答案，第 $qqq$ 行应包含第 $qqq$ 个查询的答案。

---

### Sample Input 1

```text
5 4
1 3 22
3 4 13
5 5 455
1 5 1000000000
```

---

### Sample Output 1

```text
1452
455
0
21421644
```

---

After the first query, $A=(22,22,22,0,0)A=(22,22,22,0,0)A=(22,22,22,0,0)$ and $B=(22,22,22)B=(22,22,22)B=(22,22,22)$. Merging the first and third slimes first incurs a cost of $22×22=48422 \times 22=48422×22=484$. Then merging the remaining two slimes incurs a cost of $22×44=96822 \times 44=96822×44=968$. The total cost is $484+968=1452484+968=1452484+968=1452$. Moreover, the total cost cannot be made smaller than this.  
After the second query, $A=(22,22,35,13,0)A=(22,22,35,13,0)A=(22,22,35,13,0)$ and $B=(35,13)B=(35,13)B=(35,13)$. The answer is $35×13=45535 \times 13 = 45535×13=455$.

第一个查询结束后，$A=(22,22,22,0,0)A=(22,22,22,0,0)A=(22,22,22,0,0)$ 且 $B=(22,22,22)B=(22,22,22)B=(22,22,22)$。先合并第一只和第三只史莱姆会产生 $22×22=48422 \times 22=48422×22=484$ 的代价，接着合并剩余的两只史莱姆会产生 $22×44=96822 \times 44=96822×44=968$ 的代价，总代价为 $484+968=1452484+968=1452484+968=1452$，且不存在更小的总代价。
第二个查询结束后，$A=(22,22,35,13,0)A=(22,22,35,13,0)A=(22,22,35,13,0)$ 且 $B=(35,13)B=(35,13)B=(35,13)$，答案为 $35×13=45535 \times 13 = 45535×13=455$。
