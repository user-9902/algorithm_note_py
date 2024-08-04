"""
@title:      300. 最长递增子序列
@difficulty: 中等
@importance: 5/5
@tags:       dp greedy
"""


class Solution:
    """
    经典题：https://leetcode.cn/problems/longest-increasing-subsequence/solutions/147667/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
    """

    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       dp[i] = max(dp[j] + 1, dp[i]) ; j <= 0
        """
        n = len(nums)
        f = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

    def lengthOfLIS2(self, nums: list[int]) -> int:
        """
        @tags:              greedy binary_search
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        """
        n = len(nums)
        res = [0] * n
        idx = 0
        res[0] = nums[0]
        for i in range(1, n):
            if nums[i] > res[idx]:
                idx += 1
                res[idx] = nums[i]
            else:
                l = 0
                r = idx + 1
                while l < r:
                    mid = (l + r) // 2
                    if res[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                res[r] = nums[i]
        return idx + 1


Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
