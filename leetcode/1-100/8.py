"""
8. 字符串转换整数 (atoi)
字符串; 自动机
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        index = 0
        sign = 1
        res = 0
        while index < n and s[index] == ' ':
            index += 1

        if index < n and (s[index] == '+' or s[index] == '-'):
            sign = 1 if s[index] == '+' else -1
            index += 1

        while index < n and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1

        if res * sign > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res * sign < -(2 ** 31):
            return -(2 ** 31)

        return res * sign


Solution().myAtoi("-91283472332")
