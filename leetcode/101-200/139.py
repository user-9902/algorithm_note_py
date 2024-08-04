"""
@title:      139. 单词拆分
@difficulty: 中等
@importance: 4/5
@tags:       hasmap dp
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)  
        @description:       f[i] = f[i-k] and s[k:i] in set
        """
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        for i in range(n):
            for j in range(i+1):
                if s[j: i + 1] in wordDict and f[j]:
                    f[i + 1] = True
                    continue
        return f[n]
