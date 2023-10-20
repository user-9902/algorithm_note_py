"""
12. 整数转罗马数字
string
"""

NUMS = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
ROMAN_NUMS = ('I', 'IV', 'V', 'IX', 'X', 'XL',
              'L', 'XC', 'C', 'CD', 'D', 'CM', 'M')


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []

        index = len(NUMS) - 1
        while num:
            for i in range(index, -1, -1):
                if num >= NUMS[i]:
                    index = i
                    ans.append(ROMAN_NUMS[i])
                    num -= NUMS[i]
                    break

        return ''.join(ans)
