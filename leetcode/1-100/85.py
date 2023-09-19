"""
85. 最大矩形
同84题将每行处理为84题中的矩形

虽然是同样的题，但是看完题解才意识到...
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(matrix[i][j])
                if i > 0 and matrix[i][j] > 0:
                    matrix[i][j] += matrix[i-1][j]
        res = 0
        for i in matrix:
            res = max(res, self.largestRectangleArea(i))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        res = 0

        for i in range(1, len(heights)):
            v = heights[i]
            # 插入的元素使得stack失去单调性
            if heights[stack[-1]] > v:
                # 恢复单调性
                while stack and heights[stack[-1]] > v:
                    h = stack.pop()  # 高度的下标
                    r = i   # 右边界
                    l = stack[-1] if stack else -1  # 左边界
                    res = max(res, (r - l -1) * heights[h])
                stack.append(i)
            else:
                stack.append(i)

        # 清空栈
        while stack:
            h = stack.pop()
            r = len(heights)
            l = stack[-1] if stack else -1
            res = max(res, (r - l -1) * heights[h])

        return res
