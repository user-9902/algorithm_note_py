"""
162. 寻找峰值

和寻找单个峰顶一样
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 这里不枚举至最后一个元素，统一处理了最后一个元素为峰值的情况
        l, r = 0, len(nums) - 2
        while l <= r:
            mid = (l+r) // 2
            # 这里是利用的单调性来作为二分的条件
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        return l


Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
