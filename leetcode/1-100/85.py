"""
@title:      85. 最大矩形
@difficulty: 困难
@importance: 5/5
@tags:       前缀和 单调栈
"""
from typing import List


def largestRectangleArea(self, nums):
    n = len(nums)
    stack = []
    left = [-1] * n
    for i in range(n):
        v = nums[i]
        while stack and v <= nums[stack[-1]]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    ans = 0
    stack.clear()
    for i in range(n - 1, -1, -1):
        v = nums[i]
        while stack and v <= nums[stack[-1]]:
            stack.pop()
        right = stack[-1] if stack else n
        ans = max(ans, (right - left[i] - 1) * v)
        stack.append(i)
    return ans


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        @tags:              前缀和 单调栈
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       前缀和先处理下数组，就同leetcode84（前一题）一样了
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                if i > 0 and matrix[i][j] and matrix[i - 1][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]
        return max([largestRectangleArea(matrix[i]) for i in range(n)])
