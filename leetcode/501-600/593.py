"""
@title:      593. 有效的正方形
@difficulty: 中等
@importance: 5/5
@tags:       math
"""
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        @tags:              math
        @time complexity:   O(1)   
        @space complexity:  O(1)
        @description:       正方形两条斜点连线的长相同；斜边中点相同，垂直
        """
        def tools(p1, p2, p3, p4):
            v1 = (p1[0] - p2[0], p1[1] - p2[1])
            v2 = (p3[0] - p4[0], p3[1] - p4[1])

            return (
                p1[0] + p2[0] == p3[0] + p4[0]  # 斜边中点相同
                and p1[1] + p2[1] == p3[1] + p4[1]  # 斜边中点相同
                and v1[0] * v1[0] + v1[1] * v1[1]
                == v2[0] * v2[0] + v2[1] * v2[1]  # 斜边长相同
                and v1[0] * v2[0] + v1[1] * v2[1] == 0  # 垂直 向量乘法
            )

        if p1 == p2:
            return False
        if tools(p1, p2, p3, p4):
            return True
        if p1 == p3:
            return False
        if tools(p1, p3, p2, p4):
            return True
        if p1 == p4:
            return False
        if tools(p1, p4, p2, p3):
            return True
        return False
