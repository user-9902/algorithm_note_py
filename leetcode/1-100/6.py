"""
@title:      6. Z 字形变换
@difficulty: 中等
@importance: 3/5
@tags:       模拟
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        @tags:              模拟
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       模拟打印过程，到达边界时转向。
        """
        if numRows == 1:
            return s
        arrs = [""] * numRows
        l = 0  # 当前组
        dire = -1  # 方向
        for i, c in enumerate(s):
            arrs[l] += c
            if l == 0 or l == numRows - 1:
                dire = -dire
            l += dire
        return "".join(arrs)
