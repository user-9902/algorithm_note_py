"""
11. 盛最多水的容器
difficulty: 中等
importance: 5/5
tags:       双指针，贪心
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[r], height[l]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return ans
