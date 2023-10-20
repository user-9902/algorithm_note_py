"""
154. 寻找旋转排序数组中的最小值 II

"""
from typing import List
from math import inf


class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     """
    #     单调栈 可以解33 153 154
    #     不符合题意O(logn)的复杂度, 而且使用了额外的空间
    #     """
    #     stack = [-inf]
    #     for i in nums:
    #         if i >= stack[-1]:
    #             stack.append(i)
    #         else:
    #             return i
    #     return stack[1]

    def findMin(self, nums: List[int]) -> int:
        """
        二分
        在153题的基础上进阶
        nums[-1]将集合分为了 >= nums[-1] 和 <= nums[-1]的两个部分，集合存在交集
        去除交集的部分即可
        即将 >= nums[-1] 转化为 > nums[-1] 就变回了 l53题了
        """
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

        return nums[left]
