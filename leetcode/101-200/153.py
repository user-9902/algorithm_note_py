"""
153. 寻找旋转排序数组中的最小值
binary search
二分的关键在于'分'
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]


Solution().findMin([3, 4, 5, 1, 2])
