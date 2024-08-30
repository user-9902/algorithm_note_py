"""
@title:      55. 跳跃游戏 I
@difficulty: 简单
@importance: 4/5
@tags:       贪心
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        @tags:              贪心
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       从左向右遍历，维护一个能最远跳到的下标。
                            每个元素都去判断能否到达，若当前下标 > 最远能到达，说明无法跳到当前下标。
                            存在无法跳到的下标就说明无法跳到最后。
        """
        max_r = 0
        for i, v in enumerate(nums):
            if max_r < i:
                return False
            max_r = max(max_r, i+v)
        return True
