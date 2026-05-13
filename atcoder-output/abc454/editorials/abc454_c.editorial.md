# ABC454 C - Straw Millionaire 题解

## 题意概括

有 `N` 种物品，初始时只有物品 `1`。

每个朋友提供一种交换方式：如果你手里有物品 `A_i`，就可以把它交给这位朋友并得到物品 `B_i`。

问最终一共能获得多少种不同物品。

## 解题思路

把每种交换方式看成一条有向边：

$A_i \to B_i$

那么题目就变成：

- 从点 `1` 出发，在这张有向图里能到达多少个点。

因此直接从 `1` 做一次图的遍历即可。这里用广度优先搜索。

做法：

1. 建邻接表；
2. 从点 `1` 入队；
3. 每次取出一个当前能拿到的物品 `u`，把所有 `u -> v` 的 `v` 加入队列；
4. 统计一共有多少个点被访问过。

## 正确性说明

如果某种物品 `v` 能从物品 `1` 经过若干次交换得到，那么图上就存在一条从 `1` 到 `v` 的有向路径，因此在 BFS 中一定会访问到 `v`。

反过来，如果 BFS 访问到了某个点 `v`，说明存在一条从 `1` 到 `v` 的有向路径，也就表示存在一串合法交换操作可以得到物品 `v`。

因此，被 BFS 访问到的点恰好就是所有可以获得的物品种类，统计它们的数量就是答案。算法正确。

## 复杂度

- 时间复杂度：`O(N + M)`
- 空间复杂度：`O(N + M)`

## 参考实现

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> g[300005];
int vis[300005];

int main(){

    int n, m;
    cin >> n >> m;

    for(int i=1; i<=m; i++){
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }

    queue<int> q;
    q.push(1);
    vis[1] = 1;

    int ans = 0;
    while(!q.empty()){
        int u = q.front();
        q.pop();
        ans++;

        for(int v : g[u]){
            if(vis[v]){
                continue;
            }
            vis[v] = 1;
            q.push(v);
        }
    }

    cout << ans;
    return 0;
}
```
