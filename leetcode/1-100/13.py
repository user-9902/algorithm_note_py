"""
13. 罗马数字转整数
difficulty: 简单
importance: 3/5
tags:       数组
"""


NUMS = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
ROMANS = ("I", "IV", "V", "IX", "X", "XL",
          "L", "XC", "C", "CD", "D", "CM", "M")


class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        i = 0
        r = len(NUMS) - 1
        ans = 0
        while i < n:
            if s[i:].startswith(ROMANS[r]):
                ans += NUMS[r]
                i += len(ROMANS[r])
            else:
                r -= 1
        return ans
