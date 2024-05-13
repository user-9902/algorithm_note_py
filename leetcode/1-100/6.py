"""
6. Z 字形变换
difficulty: 中
importance: 3/5
tags:       找规律
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
            以4为例，周期打印完模为0的下标；1、5的下标；2、4的下标；3的下标
            0   
            1  5
            2 4
            3
        """
        if numRows == 1:
            return s
        # 获取顺序序列
        matrix = []
        l = 1
        r = numRows * 2 - 3
        for i in range(numRows - 2):
            matrix.append(l)
            matrix.append(r)
            l += 1
            r -= 1

        size = numRows * 2 - 2
        n = len(s)
        ans = ""
        # 周期内一个字符
        i = 0
        while i < len(s):
            ans += s[i]
            i += size
        # 周期内有两个字符
        for i in range(numRows - 2):
            a, b = matrix[2 * i], matrix[2 * i + 1]
            j = 0
            while True:
                if j * size + a < n:
                    ans += s[j * size + a]
                else:
                    break
                if j * size + b < n:
                    ans += s[j * size + b]
                else:
                    break
                j += 1
        # 周期内一个字符
        i = numRows - 1
        while i < len(s):
            ans += s[i]
            i += size

        return ans
