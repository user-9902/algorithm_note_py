"""
300. 最长递增子序列
dp; greedy
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        dp
        dp[i] = max(dp[j] + 1, dp[i]) ; j <= 0
        """
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        """
        贪心+二分
        """
        res = [nums[0]]
        for v in nums:
            if v > res[-1]:
                res.append(v)
            else:
                # 二分寻找插入位置
                l, r = 0, len(res) - 1
                loc = r
                while l <= r:
                    mid = (l + r) >> 1
                    if res[mid] >= v:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                res[loc] = v
        return len(res)
