"""
背包问题
dp
"""
from typing import List
from functools import cache

"""
1. 0-1背包问题
一共有n件物品，第i件物品的重量w[i];价值为v[i]
在不超过背包重量上限的情况下，如何使背包装入物品的价值最大

显然不能使用暴力求解的方式，时间复杂度为O(2^n)

回溯：
第i个物品可以选或不选，不选剩余空间不变化,选剩余空间变化
dfs(i, c) = max(dfs(i - 1, c), dfs(i - 1, c - w[i]) + v[i])

"""


def zero_one_knapsack(w: List[int], v: List[int], cap: int):
    """
    递归
    使用cache记忆化搜索优化
    """
    # n = len(w)

    # @cache
    # def dfs(i, c):
    #     if i < 0:
    #         return 0
    #     if c < w[i]:
    #         return dfs(i-1, c)
    #     return max(dfs(i-1, c), dfs(i-1, c - w[i]) + v[i])

    # return dfs(n-1, cap)

    """
    dp
    dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])
    当前物品可选可不选，
        不选时则为 dp[i-1][j]，
        选择时则为 j-w[i]时的最大价值 + 当前价值
    """
    # n = len(w)
    # f = [[0] * (cap + 1) for _ in range(n+1)]

    # for i in range(1, n+1):
    #     for j in range(i, cap+1):
    #         f[i][j] = f[i-1][j]
    #         if j - w[i-1] >= 0:
    #             f[i][j] = max(f[i][j], f[i-1][j - w[i-1]] + v[i-1])

    # return f[n][cap]

    """
    dp
    仔细观察状态转移方程
    dp[i][j] 中的 i 依赖的始终是 i-1
    因此 f 压缩至长度为2的数组，交替（取模）遍历即可
    """
    # n = len(w)
    # f = [[0] * (cap + 1)for _ in range(2)]

    # for i in range(1, n+1):
    #     for j in range(i, cap+1):
    #         f[i % 2][j] = f[(i-1) % 2][j]
    #         if j - w[i-1] >= 0:
    #             f[i % 2][j] = max(f[i % 2][j], f[(i-1) %
    #                               2][j - w[i-1]] + v[i-1])

    # return f[n % 2][cap]

    """
    dp
    继续观察状态转移方程
    dp[i][j] 中的 j 依赖的是 >=j 的状态
    因此压缩至一维，从后向前遍历即可
    分析二维f, 当前b始终依赖 a 和 a之前的状态
    [...a...]
    [...b...]
    因此需要从后向前遍历,这样一维数组的组成如下
    [...a
        b...]
    """
    n = len(w)
    f = [0] * (cap + 1)

    for i in range(1, n+1):
        for j in range(cap, w[i-1] - 1, -1):
            f[j] = max(f[j], f[j - w[i-1]] + v[i-1])

    return f[cap]


"""
2. 完全背包问题
01背包进阶问题，01背包中只能选或不选，完全背包中可选多次k(0 < k < j/w[i])次
因此状态转移方程
dp[i][j] = max(dp[i-1][j], dp[i-1][j - k*w[i]] + k*v[i])
"""


def complete_knapstack(w: List[int], v: List[int], cap: int):
    """
    dp
    参照01背包中dp的基础解法
    """
    # n = len(w)

    # f = [[0]* (cap + 1)for _ in range(n+1)]

    # for i in range(1, n+1):
    #     for j in range(1, cap+1):
    #         f[i][j] = f[i-1][j]
    #         for k in range(j // w[i-1] + 1):
    #             f[i][j] = max(f[i][j], f[i-1][j-k*w[i-1]] + k*v[i-1])

    # return f[n][cap]

    """
    dp
    同样01背包一样可以压缩为一维
    分析二维f: 当前的b依赖于a或a及a之后的状态
    [...a...]
    [...b...]
    因此需要从前向后遍历，一维数组组成如下
        a...]
    [...b
    """
    n = len(w)
    f = [0] * (cap + 1)

    for i in range(1, n+1):
        for j in range(w[i-1], cap + 1):
            f[j] = max(f[j], f[j - w[i-1]] + v[i-1])

    return f[cap]


"""
3.多重背包问题
01背包的数量限制是1
完全背包的限制是inf
多重背包的限制是k(0<k<inf)
"""


def multi_knpstack(w: List[int], v: List[int], c: List[int], cap: int):
    """
    转化为完全背包
    dp[i][j] = max(dp[i-1][j], dp[i-1][j - k*w[i]] + k*v[i]) | k < j/w[i] && k < c[i]
    """
    # n = len(w)
    # f = [[0] * (cap + 1)for _ in range(n+1)]

    # for i in range(1, n+1):
    #     for j in range(1, cap+1):
    #         f[i][j] = f[i-1][j]
    #         for k in range(j // w[i-1] + 1):
    #             if k <= c[i - 1]:
    #                 f[i][j] = max(f[i][j], f[i-1][j-k*w[i-1]] + k*v[i-1])
    # return f[n][cap]

    """
    dp
    同样可以压缩为一维
    """
    n = len(w)
    f = [0] * (cap + 1)

    for i in range(1, n+1):
        for j in range(cap, w[i-1] - 1, -1):
            for k in range(1, min(c[i-1], j // w[i-1]) + 1):
                f[j] = max(f[j], f[j - k * w[i-1]] + k * v[i-1])

    return f[cap]
