"""
@title:      91. 解码方法
@difficulty: 中等
@importance: 5/5
@tags:       线性dp
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n) 能压缩空间复杂度至一维
        @description:       模板dp题，将问题简化为:以当前字符串结尾能解码的方式。
        """
        n = len(s)
        f = [0] * n
        f[0] = int(s[0] != "0")
        for i in range(1, n):
            if s[i] != "0":  # 当前字符能转码
                f[i] += f[i - 1]
            if s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6"):  # 和前面一个字符能一同组成合法字符
                f[i] += f[i - 2] if i > 1 else 1
        return f[n - 1]
