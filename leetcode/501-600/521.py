"""
@title:      521. 最长特殊序列 I
@difficulty: 简单
@importance: 3/5
@tags:       脑筋急转弯
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        @tags:              分类讨论
        @time complexity:   O(n+m)
        @space complexity:  O(1)
        @description:       a == b 时他们互为子序列；a != b 时：长度不等，更长度的字符串不可能是短的子序列；长度等的时候，不可能互为子序列
        """
        return -1 if a == b else max(len(a), len(b))
