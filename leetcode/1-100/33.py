"""
33. 搜索旋转排序数组
binary search
二分 != 单调。二分的本质是存在一个特性，当一段满足时，则另一端不满足，单调性只是一种特性。
leetcode 153 的进阶问题
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        binary search
        """
        n = len(nums)
        left = 0
        right = n - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        # 确认在哪段上
        l = 0 if target > nums[-1] else left
        r = left - 1 if target > nums[-1] else n - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return r if nums[r] == target else -1


Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
