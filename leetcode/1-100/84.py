"""
@title:      84. 柱状图中最大的矩形
@difficulty: 困难
@importance: 5/5
@tags:       单调栈
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        @tags:              fs
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       枚举每个高度height 作为矩形的高，向左向右寻找其最大宽度。❌ 超时
        """
        n = len(heights)
        ans = 0
        for i, v in enumerate(heights):
            l = r = i
            while l > -1 and heights[l] >= v:
                l -= 1
            while r < n and heights[r] >= v:
                r += 1
            ans = max(ans, (r - l - 1) * v)
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        @tags:              单调栈
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       fs的瓶颈在寻找宽度上，我们使用单调栈来快速找到宽度。本题和接雨水相似。
        """
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []
        # 单调栈来寻找左边界
        for i, v in enumerate(heights):
            while stack and v <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()
        # 单调栈来寻找右边界
        for i in range(n-1, -1, -1):
            v = heights[i]
            while stack and v <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i in range(n):
            w = right[i] - left[i] - 1
            h = heights[i]
            ans = max(ans, w * h)
        return ans
