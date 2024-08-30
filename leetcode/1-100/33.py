"""
@title:      33. 搜索旋转排序数组
@difficulty: 中等
@importance: 4/5
@tags:       二分
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        @tags:              二分
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       leetcode 153 的进阶问题 先找到最小元素下标 将数组分段寻找target
        """
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[n - 1]:
                l = mid + 1  # [mid+1, r)
            else:
                r = mid  # [l,mid)
        # 找到最小的元素 确认target在哪段上

        left = 0 if target > nums[-1] else l
        right = l if target > nums[-1] else n

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1  # [mid, r)
            else:
                right = mid  # [l, mid)

        return left if nums[left] == target else -1
