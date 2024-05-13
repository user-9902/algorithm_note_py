"""
1. 两数之和
difficulty: 简单
importance: 4/5
tags:       hashmap
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        我们要寻找的是"一对"数a和b，他们的和为target
        a和b满足 target - a = b
        如果a是满足结果的value，那么另一个value一定是target-a
        更具a和b满足的数学性质，我们只要记录遍历过的元素的下标即可
        """
        hash_map = {}
        for i, v in enumerate(nums):
            red = target - v
            if str(red) in hash_map:
                return [hash_map[str(red)], i]
            else:
                hash_map[str(v)] = i
        return []
