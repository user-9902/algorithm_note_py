"""
673. 最长递增子序列的个数
dp; greedy
同leetcode300
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        dp
        dp dp[i]表示nums[0:i+1]最长递增子序列类的长度
        dpc dpc[i]表示nums[0:i+1]最长子序列的数量
        """
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        for i in range(0, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
        print(cnt)
        return cnt[-1]


Solution().findNumberOfLIS([2, 2, 2, 2, 2])
