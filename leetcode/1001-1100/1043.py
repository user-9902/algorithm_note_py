"""
1043. 分隔数组以得到最大和
"""

from typing import List
from math import inf


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        参考自leetcode
        dp[i] = dp[i - k] + max(arr[i-k+1:i]) * k
        """
        n = len(arr)
        dp = [0] * (n + 1)
        dp[1] = arr[0]
        for i in range(1, n + 1):
            max_val = arr[i - 1]
            for j in range(1, min(i, k) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * (j))

        return dp[-1]

    def maxSumAfterPartitioning2(self, arr: List[int], k: int) -> int:
        """
        dp[i][j] arr[i:j+1] 区间内的最优解
        自己解法，用的区间dp
        算法没错，复杂度又炸了（n^3）😓
        """
        n = len(arr)

        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i] = arr[i]

        # 区间dp [i,j)
        for i in range(n, -1, - 1):
            for j in range(i+1, n):
                if j - i < k:
                    dp[i][j] = max(arr[i:j+1]) * (j - i + 1)
                else:
                    val = 0
                    for x in range(1, j - i + 1):
                        val = max(val, dp[i][i + x - 1] + dp[i + x][j])
                    dp[i][j] = val
        return dp[0][-1]


Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)
