"""
149. 直线上最多的点数
计算斜率，为防止浮点误差，这里转为字符串的表现形式。
"""
from typing import List
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        def calcu(x1, y1, x2, y2):
            """
            计算斜率
            """
            if x1 == x2:
                return '1'
            if y1 == y2:
                return 'inf'
            c = gcd(abs(x1-x2), abs(y1-y2))  # 计算最大公约数
            s = str(abs(x1-x2) / c) + '-' + str(abs(y1-y2) / c)
            # 公约数计算的时候排除了负号，结果要区分
            return s if (y2 - y1) / (x2 - x1) > 0 else '-' + s

        ans = 0
        for i in range(n):
            key_map = {}
            for j in range(i+1, n):
                # 斜率使用字符串保存
                key = calcu(*points[i], *points[j])
                if key in key_map:
                    key_map[key] += 1
                else:
                    key_map[key] = 1

                ans = max(key_map[key] + 1, ans)

        return ans


Solution().maxPoints([[-6, -1], [3, 1], [12, 3]])
