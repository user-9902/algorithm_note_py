"""
14. 最长公共前缀
difficulty: 简单
importance: 4/5
tags:       数组
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in strs:
            n = min(len(i), len(res))
            res = res[:n]
            if n == 0:
                break
            for j in range(n):
                if i[j] != res[j]:
                    res = res[:j]
                    break
        return res
