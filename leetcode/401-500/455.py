"""
455. 分发饼干
greedy sort 双指针
喂给孩子尽可能小尺寸的饼干
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans = 0
        n = len(s)
        m = len(g)
        p1 = p2 = 0

        while p2 < n and p1 < m:
            if g[p1] <= s[p2]:
                p1 += 1
                p2 += 1
                ans += 1
            else:
                p2 += 1
        return ans
