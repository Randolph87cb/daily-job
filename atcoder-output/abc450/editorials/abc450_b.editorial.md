# ABC450 B - Split Ticketing 题解

## 题意概括

有 $N$ 个车站从西到东排成一列，已知任意 $i < j$ 时从车站 $i$ 坐到车站 $j$ 的票价 $C_{i,j}$。判断是否存在 $a < b < c$，使得先买 $a \to b$ 再买 $b \to c$ 的总价严格小于直接买 $a \to c$ 的票价。

## 解题思路

题目只要求判断“是否存在”这样的三元组，所以直接枚举 $a, b, c$ 即可。

先把输入的票价存进数组 `cost[i][j]`。然后三重循环枚举所有满足 $1 \leq a < b < c \leq N$ 的组合，检查是否有

$C_{a,b} + C_{b,c} < C_{a,c}$

一旦找到这样的三元组，就说明拆票更便宜，答案是 `Yes`；如果所有三元组都检查完仍然没有找到，答案就是 `No`。

由于 $N \leq 100$，三重循环的规模是 $O(N^3)$，完全可以接受。

## 正确性说明

程序枚举了所有满足 $a < b < c$ 的三元组，因此任何可能成为答案的方案都不会漏掉。

如果程序输出 `Yes`，说明它找到了某个三元组满足 $C_{a,b} + C_{b,c} < C_{a,c}$，这正是题目要求的条件。

如果程序输出 `No`，说明所有满足 $a < b < c$ 的三元组都不满足这个不等式，因此题目所要求的三元组不存在。故算法判断结果一定正确。

## 复杂度

- 时间复杂度：$O(N^3)$
- 空间复杂度：$O(N^2)$

## 参考实现

```cpp
#include<bits/stdc++.h>
using namespace std;

const int maxn = 100;
long long cost[maxn + 5][maxn + 5];

int main(){

    int n;
    cin >> n;

    // 按题目给出的上三角形式读入每一段直达票价。
    for(int i=1; i<=n - 1; i++){
        for(int j=i + 1; j<=n; j++){
            cin >> cost[i][j];
        }
    }

    bool ok = false;

    // 枚举所有 a < b < c，检查是否存在拆票更便宜的情况。
    for(int a=1; a<=n && !ok; a++){
        for(int b=a + 1; b<=n && !ok; b++){
            for(int c=b + 1; c<=n; c++){
                if(cost[a][b] + cost[b][c] < cost[a][c]){
                    ok = true;
                    break;
                }
            }
        }
    }

    if(ok){
        cout << "Yes";
    } else {
        cout << "No";
    }

    return 0;
}
```
