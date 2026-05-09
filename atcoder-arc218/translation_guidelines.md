# Algorithm Translation Guidelines

这份约定是为了把 AtCoder 英文题面翻译成更自然的中文算法题表述，同时尽量避免术语漂移。

## 核心原则

1. 保留算法语义优先，不追求逐词直译。
2. 变量名、公式、上下标、样例输入输出保持原样。
3. 对常见 OI / ACM 术语使用固定译法，减少同义词混用。
4. `Problem Statement` 部分优先翻成自然中文叙述，不机械保留英文句式。
5. 样例解释可以适度润色，但不能改变原意或补充原题没有给出的结论。

## 推荐译法

| English | Recommended Chinese |
| --- | --- |
| sequence | 序列 |
| positive integers | 正整数 |
| distinct integers | 不同整数 |
| number of distinct integers | 不同整数的个数 |
| choose one element from each sequence | 从每个序列中各选一个元素 |
| modulo 998244353 | 对 `998244353` 取模 |
| Constraints | 约束条件 |
| The input is given from Standard Input in the following format: | 输入从标准输入按如下格式给出： |
| Output the answer. | 输出答案。 |
| Sample Input | 样例输入 |
| Sample Output | 样例输出 |
| points | 分 |

## 不建议的译法

- `distinct` 不建议翻成“独特的”。
- `sequence` 在数值题里不建议反复混用“数列 / 列表 / 数组”，除非题意明确要求数组语境。
- `modulo` 不建议机械翻成“模掉”。
- `constraints` 不建议在同一项目里混用“限制 / 约束 / 数据范围”。

## 这类题的翻译习惯

- 叙述性正文：优先使用“给定……请你求……”的中文算法题句式。
- 数学对象：保留 `$N$`、`$M$`、`$A_{i,j}$` 这类写法。
- 样例说明：优先使用“例如”“此时”“因此答案为”这样的连接方式。
- 如果英文原文里已经存在歧义，先忠实保留，再在需要时单独备注，不在译文里擅自补题解。
