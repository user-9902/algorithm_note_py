"""
12. 整数转罗马数字
difficulty: 简单
importance: 3/5
tags:       数组
"""


NUMS = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
ROMANS = ("I", "IV", "V", "IX", "X", "XL",
          "L", "XC", "C", "CD", "D", "CM", "M")


class Solution:
    def intToRoman(self, num: int) -> str:
        n = len(NUMS)
        r = n - 1
        ans = ""
        while num:
            if num // NUMS[r] == 0:
                r -= 1
            else:
                ans += (num // NUMS[r]) * ROMANS[r]
                num = num % NUMS[r]
        return ans
