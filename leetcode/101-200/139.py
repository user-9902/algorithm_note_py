"""
139. 单词拆分
dp
dp[i] 表示s[0:i+1]的字符能否由字典拼出
dp[i] = dp[0:j] == true and dp[j:i+1] in wordDict
j为wordDict中字符的长度即可
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True

        n = len(s)
        dp = [False] * (n + 1)

        lens = []
        for w in wordDict:
            if len(w) not in lens:
                lens.append(len(w))

        for i in range(n+1):
            for l in lens:
                if i - l == 0:
                    dp[i] = s[i - l:i] in wordDict
                if i - l > 0:
                    dp[i] = dp[i - l] and s[i - l:i] in wordDict
                if dp[i]:
                    break
        return dp[-1]
