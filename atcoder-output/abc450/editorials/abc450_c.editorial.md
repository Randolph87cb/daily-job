# ABC450 C - Puddles 题解

## 题意概括

给定一个 $H \times W$ 的黑白网格，`#` 表示黑格，`.` 表示白格。我们要统计白色四联通块中，有多少个连通块完全不碰到网格最外层边界。

换句话说，就是统计“被黑格包围住”的白色连通块个数。

## 解题思路

把每个白色连通块单独找出来，再判断它是否接触边界即可。

具体做法如下：

1. 从左到右、从上到下扫描整个网格。
2. 遇到一个还没有访问过的白格，就以它为起点做一次 BFS，把和它四方向连通的所有白格都找出来，这样就得到一个完整的白色连通块。
3. 在 BFS 过程中，记录这个连通块里是否出现过边界格子，也就是行号为 $1$ 或 $H$，或者列号为 $1$ 或 $W$ 的格子。
4. 如果这个连通块没有碰到边界，说明它被黑格完全围住，答案加一；否则不计入答案。

之所以这样做，是因为题目中的目标正是“白色连通块中，不包含任何外边框格子”的那些连通块。BFS 恰好能把一个连通块一次性完整找出。

由于每个白格只会进入 BFS 一次，总时间复杂度是 $O(HW)$。

## 正确性说明

对于任意一个白色连通块，程序总会在扫描到它的某个尚未访问的白格时启动一次 BFS。由于 BFS 只沿四个方向扩展到相邻白格，所以它会访问到这个连通块中的全部白格，而且不会跑到别的连通块里。

在这次 BFS 中，变量 `touch_border` 会记录该连通块是否包含边界白格：

- 如果 `touch_border = true`，说明这个连通块至少有一个格子在最外层边界上，因此它不符合题意，不能计数；
- 如果 `touch_border = false`，说明这个连通块中没有任何边界格子，因此它完全被黑格围住，应该计入答案。

每个白色连通块恰好会被统计一次，所以最终得到的计数正是题目要求的答案。

## 复杂度

- 时间复杂度：$O(HW)$
- 空间复杂度：$O(HW)$

## 参考实现

```cpp
#include<bits/stdc++.h>
using namespace std;

const int maxn = 1000;
const int maxq = (maxn + 5) * (maxn + 5);

char s[maxn + 5][maxn + 5];
bool vis[maxn + 5][maxn + 5];
int qx[maxq + 5], qy[maxq + 5];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main(){

    int h, w;
    cin >> h >> w;

    // 读入整张网格，后续用 s[i][j] 表示第 i 行第 j 列的颜色。
    for(int i=1; i<=h; i++){
        cin >> (s[i] + 1);
    }

    int ans = 0;

    // 扫描每个格子，遇到新的白色连通块就做一次 BFS。
    for(int i=1; i<=h; i++){
        for(int j=1; j<=w; j++){
            if(s[i][j] == '#' || vis[i][j]){
                continue;
            }

            int head = 1;
            int tail = 1;
            qx[1] = i;
            qy[1] = j;
            vis[i][j] = true;

            // 记录当前这个白色连通块是否碰到了最外层边界。
            bool touch_border = (i == 1 || i == h || j == 1 || j == w);

            while(head <= tail){
                int x = qx[head];
                int y = qy[head];
                head++;

                // 把与当前格子四方向相邻的白格继续加入同一个连通块。
                for(int k=0; k<4; k++){
                    int nx = x + dx[k];
                    int ny = y + dy[k];

                    if(nx < 1 || nx > h || ny < 1 || ny > w){
                        continue;
                    }
                    if(s[nx][ny] == '#' || vis[nx][ny]){
                        continue;
                    }

                    vis[nx][ny] = true;
                    tail++;
                    qx[tail] = nx;
                    qy[tail] = ny;

                    if(nx == 1 || nx == h || ny == 1 || ny == w){
                        touch_border = true;
                    }
                }
            }

            // 只有完全不接触边界的白色连通块才计入答案。
            if(!touch_border){
                ans++;
            }
        }
    }

    cout << ans;

    return 0;
}
```
