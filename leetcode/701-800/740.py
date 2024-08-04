"""
@title:      740. 删除并获得点数
@difficulty: 中等
@importance: 4/5
@tags:       dp 
"""
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       打家劫舍模型题，将题目转化为打家劫舍即可。 💲经典题一定要熟悉，变体题才能一眼识破
        """
        max_v = max(nums)
        arr = [0] * (max_v+1)
        for i in nums:
            arr[i] += i

        f = [0] * (max_v+1)
        f[0] = arr[0]
        f[1] = max(arr[0], arr[1])

        for i in range(2, max_v+1):
            f[i] = max(f[i-1], f[i-2]+arr[i])

        return f[max_v]
