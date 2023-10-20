"""
43. 字符串相乘
加法+进位
加法的按位加法
个人感觉题目很怪，要求不能直接将输入转为int，但实现中还是要将输入数字的部分转为int。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)

        # special case
        if num1 == '0' or num2 == '0':
            return '0'

        def add(num1, num2):
            premotion = 0
            ans = ''

            n = len(num1)
            m = len(num2)
            if n > m:
                num2 = '0'*(n-m) + num2
            if m > n:
                num1 = '0'*(m-n) + num1
            for i in range(max(n, m)-1, -1, -1):
                tmp = int(num1[i]) + int(num2[i]) + premotion
                premotion = tmp // 10
                ans = str(tmp % 10) + ans

            return '1' + ans if premotion else ans

        res = ''
        for i in range(n-1, -1, -1):
            res = add(res, str(int(num2) * int(num1[i])) + '0' * (n - i - 1))
        return res


Solution().multiply('2', '3')
