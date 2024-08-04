"""
@title:      1. 两数之和
@difficulty: 简单
@importance: 5/5
@tags:       hashmap
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       target - a = b 当遍历到a的时我们需要b，提前建立b和b的下标的关系即可
        """
        hash_map = {}
        for i, v in enumerate(nums):
            red = target - v
            if str(red) in hash_map:
                return [hash_map[str(red)], i]
            else:
                hash_map[str(v)] = i
        return []
