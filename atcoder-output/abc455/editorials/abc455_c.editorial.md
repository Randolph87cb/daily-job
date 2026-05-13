# ABC455 C - Vanish 题解

## 题意概括

给定序列 `A`，你需要恰好做 `K` 次操作。每次选择一个整数 `x`，把序列中所有等于 `x` 的元素全部变成 `0`。

问最终整个序列元素和的最小值是多少。

## 解题思路

如果一个数值 `x` 在序列中出现了 `c_x` 次，那么把所有 `x` 清零后，序列总和会减少：

$x \times c_x$

因此，每个不同的数值 `x` 都对应一个“收益”：

$gain_x = x \times c_x$

为了让最终总和最小，我们当然应该优先选择收益最大的 `K` 个不同数值来执行操作。

做法就是：

1. 统计每个数值出现次数；
2. 计算每个数值的收益 `x * c_x`；
3. 把这些收益排序；
4. 去掉最大的 `K` 个收益；
5. 剩余收益之和，就是最终保留下来的元素总和。

注意：不同数值的种类数可能少于 `K`，这时把所有种类都清掉以后答案就是 `0`。

## 正确性说明

一次操作选择某个数值 `x` 时，能减少的总和固定为 `x * c_x`，与其他操作无关。

因此，整个问题等价于：

- 从所有不同数值对应的收益中，选出恰好 `K` 个收益加入“被删除集合”；
- 让被删除收益之和尽可能大。

显然，最优方案就是选择收益最大的 `K` 个数值。

程序正是按这个策略实现的，所以得到的最终总和最小，算法正确。

## 复杂度

设不同数值的个数为 `M`。

- 统计出现次数：`O(N log M)`（使用 `map`）
- 排序收益：`O(M log M)`

整体复杂度可记为：

- 时间复杂度：`O(N log N)`
- 空间复杂度：`O(N)`

## 参考实现

```cpp
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){

    int n, k;
    cin >> n >> k;

    map<ll, ll> cnt;
    for(int i=1; i<=n; i++){
        ll x;
        cin >> x;
        cnt[x]++;
    }

    vector<ll> gain;
    for(auto [x, c] : cnt){
        gain.push_back(x * c);
    }

    sort(gain.begin(), gain.end(), greater<ll>());

    ll removed = 0;
    for(int i=0; i<k && i<(int)gain.size(); i++){
        removed += gain[i];
    }

    ll total = 0;
    for(ll v : gain){
        total += v;
    }

    cout << total - removed;
    return 0;
}
```
