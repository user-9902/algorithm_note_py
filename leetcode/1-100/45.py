"""
45. 跳跃游戏 II
数组
一道很无聊的题
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        index = 0
        ans = 0

        while True:
            print(index)
            ans += 1
            if index + nums[index] >= n - 1:
                break

            max_i = index + 1
            for i in range(2, nums[index]+1):
                if max_i + nums[max_i] < index + i + nums[index + i]:
                    max_i = i + index
            index = max_i

        return ans
