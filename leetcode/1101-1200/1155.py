"""
1155. 掷骰子等于目标和的方法数
dp
完全背包
f[i][j] 其中 i 表示筛子的数量 j 表示target

    0 1 2 3 4 5 6 7
0   1 x x x x x x x
1   x 1 1 1 1 1 1 x
2   x x 1 2 3 4 5 6
3   x x x 1 3 6 10 15

f[i][j] = ∑f[i-1][j-x] (1<x<k)

第i个筛子抛到的数字x可能为 1-k。前面的i-1个筛子抛出数字的和为 j - x
x 表示无需枚举的位置这些位置初始化为0即可
"""
MOD = 10**9+7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n+1):
            for j in range(i, min(i*k, target) + 1):
                for x in range(max(0, j-k), j):
                    f[i][j] = (f[i][j] + f[i-1][x]) % MOD
        return f[n][target]


Solution().numRollsToTarget(3, 6, 7)
