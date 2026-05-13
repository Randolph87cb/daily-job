# ABC455 B - Spiral Galaxy 题解

## 题意概括

给定一个黑白网格，统计有多少个矩形区域满足“颜色关于矩形中心点中心对称”。

也就是说，如果矩形内某个格子是 `(i, j)`，那么它与关于矩形中心对称的位置 `(h1 + h2 - i, w1 + w2 - j)` 颜色必须相同。

## 解题思路

这题的关键是数据范围很小：`H, W <= 10`。

因此可以直接枚举每个矩形：

1. 枚举上边界 `h1`；
2. 枚举下边界 `h2`；
3. 枚举左边界 `w1`；
4. 枚举右边界 `w2`；
5. 对这个矩形中的每个格子 `(i, j)`，检查它和中心对称位置的颜色是否相同。

只要有一对不相同，这个矩形就不合法；如果全部相同，就把答案加一。

## 正确性说明

我们枚举了所有可能的矩形区域，所以不会漏掉任何候选答案。

对于固定矩形，我们又检查了其中每个格子与它的中心对称格子是否颜色相同：

- 如果全部相同，那么这个矩形恰好满足题目定义的中心对称条件，应计入答案；
- 如果存在一对不同，那么这个矩形不满足条件，不应计入答案。

因此，程序统计出的正是所有满足条件的矩形数量，算法正确。

## 复杂度

设矩形总数为 `O(H^2 W^2)`，检查一个矩形最多需要 `O(HW)`。

- 时间复杂度：`O(H^3 W^3)`
- 空间复杂度：`O(1)`（不计输入存储）

在 `H, W <= 10` 的范围内完全可以通过。

## 参考实现

```cpp
#include<bits/stdc++.h>
using namespace std;

string s[15];

int main(){

    int h, w;
    cin >> h >> w;
    for(int i=0; i<h; i++){
        cin >> s[i];
    }

    int ans = 0;
    for(int top=0; top<h; top++){
        for(int bottom=top; bottom<h; bottom++){
            for(int left=0; left<w; left++){
                for(int right=left; right<w; right++){
                    bool ok = true;

                    for(int i=top; i<=bottom && ok; i++){
                        for(int j=left; j<=right; j++){
                            int ii = top + bottom - i;
                            int jj = left + right - j;
                            if(s[i][j] != s[ii][jj]){
                                ok = false;
                                break;
                            }
                        }
                    }

                    if(ok){
                        ans++;
                    }
                }
            }
        }
    }

    cout << ans;
    return 0;
}
```
