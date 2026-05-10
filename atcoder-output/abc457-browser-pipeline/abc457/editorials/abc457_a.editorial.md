# ABC457 A - Array 题解

## 题目信息

- 原题链接：[A - Array](https://atcoder.jp/contests/abc457/tasks/abc457_a)
- 题面对照：[../zh-CN/abc457_a.zh-CN.md](../zh-CN/abc457_a.zh-CN.md)
- 分值：100

## 题意概括

给定一个长度为 `N` 的序列 `A`，再给定一个位置 `X`，输出 `A_X` 的值。

## 解题思路

这道题没有复杂处理，按题意直接模拟即可：

1. 读入 `N`
2. 读入整个数组 `A`
3. 读入 `X`
4. 输出 `A[X]`

由于题目中的下标本来就是从 `1` 开始，我们在代码里也直接用从 `1` 开始的数组下标，这样最方便和题面对应。

## 正确性说明

数组 `A` 的第 `i` 个位置存放的就是 `A_i`。

程序读入全部数据后，直接输出数组下标为 `X` 的元素，也就是 `A_X`。这与题目要求完全一致，因此算法正确。

## 复杂度

- 时间复杂度：`O(N)`
- 空间复杂度：`O(N)`

## 参考实现（C++，遵守代码规范）

```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){

    // 读取数组长度
    int n;
    cin >> n;

    // a[i] 表示数组中的第 i 个数
    int a[105] = {0};
    for(int i=1; i<=n; i++){
        cin >> a[i];
    }

    // 读取要查询的位置
    int x;
    cin >> x;

    // 输出第 x 个数
    cout << a[x];

    return 0;
}
```
