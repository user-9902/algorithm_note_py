"""
@title:      481. 神奇字符串
@difficulty: 中等
@importance: 3/5
@tags:       模拟
"""


class Solution:
    def magicalString(self, n: int) -> int:
        """
        @tags:              模拟字符串是生成过程即可
        @time complexity:   O(n)   
        @space complexity:  O(n)
        """
        s = '122'
        res = 1
        i = 2
        l = len(s)
        while l < n:
            # 需要生成的字符串数量
            m = int(s[i])
            if m + l > n:
                m = n - l
            # 下个一字符 1 还是 2
            c = '2' if s[-1] == '1' else '1'
            if c == '1':
                res += m
            s += c * m
            i += 1
            l += m
        return res
