"""
34. 在排序数组中查找元素的第一个和最后一个位置
二分
"""
from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    """
    二分
    求大于等于target的第一个值
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        # 奇偶是会影响左右mid的取值
        # 但完全不用去关注，我们只是要选举出一个数能尽可能快的压缩可能性，中间显然是个不错的选择，一次可以压缩一般，至于是否是不是刚刚好一半不重要
        mid = (l + r) // 2 
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        # 是否存在需要查找的元素
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target+1) - 1
        return [start, end]
