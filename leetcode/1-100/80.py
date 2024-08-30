"""
name:       80. 删除有序数组中的重复项 II
difficulty: 中等
importance: 4/5
tags:       快慢指针
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int], k=2) -> int:
        """
        @tags:              快慢指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       见注释。
        """
        slow = k
        for i in range(k, len(nums)):
            # 新元素与倒数第二个元素不同，则加入
            # 将题目退阶为不在原数组操作更便于理解
            if nums[slow - k] != nums[i]:
                nums[slow] = nums[i]
                slow += 1
        return slow
