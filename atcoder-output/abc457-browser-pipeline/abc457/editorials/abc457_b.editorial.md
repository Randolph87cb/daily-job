# ABC457 B - Arrays 题解

## 题目信息

- 原题链接：[B - Arrays](https://atcoder.jp/contests/abc457/tasks/abc457_b)
- 题面对照：[../zh-CN/abc457_b.zh-CN.md](../zh-CN/abc457_b.zh-CN.md)
- 分值：200

## 题意概括

给定 $N$ 个序列 $A_1, A_2, \ldots, A_N$，其中每个序列的长度都可能不同。最后给出 `X` 和 `Y`，要求输出 $A_{X,Y}$。

## 解题思路

这题仍然是按题意直接存储和查询。

因为每个序列的长度 $L_i$ 不同，所以可以用二维 `vector` 来保存：

- `a[i]` 表示第 `i` 个序列
- `a[i][j]` 表示第 `i` 个序列中的第 `j` 个数

为了和题面里的下标保持一致，我们让每个序列多开一个位置，从下标 `1` 开始存值。

处理步骤：

1. 读入 `N`
2. 依次读入每个序列的长度 $L_i$ 和内容
3. 读入 `X`、`Y`
4. 直接输出 `a[X][Y]`

## 正确性说明

程序按输入顺序，把第 `i` 个序列中的第 `j` 个元素存入 `a[i][j]`。

因此，所有数据读入完成后：

- `a[X][Y]` 保存的正是题目要求的 $A_{X,Y}$

程序最后直接输出 `a[X][Y]`，也就是 $A_{X,Y}$，所以结果正确。

## 复杂度

- 时间复杂度：$O\left(\sum L_i\right)$
- 空间复杂度：$O\left(\sum L_i\right)$

这里的 $\sum L_i$ 就是把每个序列的长度全部加起来。

## 参考实现（C++，遵守代码规范）

```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){

    // 读取序列个数
    int n;
    cin >> n;

    // a[i][j] 表示第 i 个序列中的第 j 个数
    vector<vector<int>> a(n + 1);

    // 读入每个序列
    for(int i=1; i<=n; i++){
        int l;
        cin >> l;

        a[i].resize(l + 1);
        for(int j=1; j<=l; j++){
            cin >> a[i][j];
        }
    }

    // 读取查询位置
    int x, y;
    cin >> x >> y;

    // 输出第 x 个序列中的第 y 个数
    cout << a[x][y];

    return 0;
}
```
