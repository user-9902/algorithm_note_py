"""
81. 搜索旋转排序数组 II
binary search
leetcode 33 题改
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        binary search
        """
        # 154 找到最小的下标
        n = len(nums)
        left = 0
        right = n - 2
        while left <= right:
            while nums[left] == nums[-1] and left < right:
                left += 1

            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        l = 0 if target > nums[-1] else left
        r = left - 1 if target > nums[-1] else n - 1
        if l == 0:
            while nums[l] == nums[-1] and l < r:
                l += 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return nums[r] == target

    


Solution().search([2, 2, 2, 3, 2, 2, 2], 3)
