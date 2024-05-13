"""
704. 二分查找
difficulty: 简单
importance: 5/5
tags:       binary_search
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r if nums[r] == target else -1


Solution().search([9], 9)
