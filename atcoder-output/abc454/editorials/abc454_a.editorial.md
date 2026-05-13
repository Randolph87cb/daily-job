# ABC454 A - Closed interval 题解

## 题意概括

给定整数 `L` 和 `R`，求闭区间 `[L, R]` 中一共有多少个整数。

## 解题思路

从 `L` 到 `R` 且包含两端的整数个数，直接用公式：

$R - L + 1$

即可。

## 正确性说明

区间 `[L, R]` 中的整数依次为：

`L, L + 1, ..., R`

它们的个数正好是终点减起点再加一，也就是：

$R - L + 1$

因此程序输出的就是答案，算法正确。

## 复杂度

- 时间复杂度：`O(1)`
- 空间复杂度：`O(1)`

## 参考实现

```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){

    int l, r;
    cin >> l >> r;

    cout << r - l + 1;
    return 0;
}
```
