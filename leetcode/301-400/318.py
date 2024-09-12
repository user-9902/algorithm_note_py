"""
@title:      318. 最大单词长度乘积
@difficulty: 简单
@importance: 4/5
@tags:       位运算
"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        @tags:              fs 位运算优化
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       fs两两对比比较低效，我们用二进制位来存储字母的信息：
                            a : 00000_00000_00000_00000_00000_1
                            b : 00000_00000_00000_00000_00001_0
                                ...
                            z : 10000_00000_00000_00000_00000_0
                            这样一个32位的整数就能作为set表来存储一个字符串的字母信息了，而是否存在重复字母的操作直接用与运算即可。
                            💲位运算优化模板题，分析题目规模，元素少于32个时，可以将问题带入该模板来思考。
        """
        base = ord('a')
        n = len(words)
        f = [0] * n
        for i, word in enumerate(words):
            for c in word:
                f[i] |= 1 << (ord(c) - base)
        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if f[i] & f[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res


Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
