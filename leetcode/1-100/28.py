"""
28. 找出字符串中第一个匹配项的下标
KMP
题目的规模能通过暴力求解来实现，
题目规模稍微严格，则变为考察KMP的题目。
"""


def get_next_val(s: str):
    n = len(s)
    ans = [0]

    i = 1
    length = 0
    while i < n:
        if s[i] == s[length]:
            length += 1
            ans.append(length)
            i += 1
            if i < n and s[i] == s[length]:
                ans[i-1] = ans[length - 1]
        else:
            if length == 0:
                ans.append(0)
                i += 1
            else:
                length = ans[length - 1]
    return ans


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        next_v = get_next_val(needle)

        n = len(haystack)
        m = len(needle)
        i = j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = next_v[j-1]
                else:
                    i += 1
            if j == m:
                return i - m

        return -1
