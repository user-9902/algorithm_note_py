"""
84. 柱状图中最大的矩形
遍历每个元素
找寻其左侧第一个比当前小的值及右侧第一个比当前小的值
暴力枚举 or 单调栈

参考自 https://www.bilibili.com/video/BV1dY4y1q7tL/?spm_id_from=333.788&vd_source=51614d2a49bfb1ec0bdf64b53b2dacd5
"""

from typing import List


class Solution:
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
