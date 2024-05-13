"""
209. 长度最小的子数组
滑动窗口

滑动窗口的题常常要求一个"满足条件"的"最优解"
移动右边界来"满足条件"
移动左边界来寻找"最优解"
"""

from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        ans = inf

        sum = 0
        while r < n:
            # 右指针满足条件
            while sum < target and r < n:
                sum += nums[r]
                r += 1

            # 左指针寻找最优解
            while sum >= target and l < r:
                sum -= nums[l]
                l += 1
            ans = min(ans, r-l+1)

        return ans if ans <= n else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        前缀和 + binary search
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i-1] + nums[i]
        ans = inf
        for i in range(n):
            if nums[i] < target:
                continue

            l = 0
            r = i
            while l <= r:
                mid = (l + r) // 2
                if nums[i] - nums[mid] < target:
                    r = mid - 1
                else:
                    l = mid + 1

            ans = min(ans, i - l)

        return ans if ans <= n else 0


Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
