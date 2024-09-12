"""
@title:      258. 各位相加
@difficulty: 中等
@importance: 3/5
@tags:       数字根 math
"""


class Solution:
    def addDigits(self, num: int) -> int:
        """
        @tags:              循环
        @time complexity:   O(logn)
        @space complexity:  O(1)
        """
        while num >= 10:
            num = (num // 10) + (num % 10)
        return num

    def addDigits(self, num: int) -> int:
        """
        @tags:              数字根 math
        @time complexity:   O(1)
        @space complexity:  O(1)
        @description:       数字根的一些特性
                            a + 9 (a != 0)的数字根 == a 的数字根
                            9 * a (a != 0)的数字根 == 9
                            两数数字根之和 == 两数之和的数字根
                            两数数字根之积 == 两数之积的数字根
        """
        return 0 if num == 0 else (num - 1) % 9 + 1
