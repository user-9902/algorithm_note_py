"""
@title:      28. 找出字符串中第一个匹配项的下标
@difficulty: 简单
@importance: 6/5
@tags:       KMP RK
"""

"""
题目的规模能通过暴力求解来实现，
题目规模稍微严格，则变为考察KMP或RK的题目了。
"""


def get_next(s):
    n = len(s)
    next = [0] * n
    j = 0
    for i in range(1, n):
        if j > 0 and s[i] != s[j]:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        @tags:              KMP
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:
        """
        m = len(needle)
        next = get_next(needle)
        j = 0
        for i, v in enumerate(haystack):
            while j > 0 and needle[j] != v:
                j = next[j - 1]
            if needle[j] == v:
                j += 1
            if j == m:
                return i - m + 1
        return -1
