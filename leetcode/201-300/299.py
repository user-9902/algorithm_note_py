"""
@title:      299. 猜数字游戏
@difficulty: 简单
@importance: 3/5
@tags:       模拟
"""
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        @tags:              模拟
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       顺序遍历，即可
        """
        n = len(secret)
        cntA = 0
        cnt = defaultdict(int)
        for i in range(n):
            if secret[i] == guess[i]:
                cntA += 1
            else:
                cnt[secret[i]] += 1
                cnt[guess[i]] -= 1
        cntB = n - cntA - sum(abs(cnt[k]) for k in cnt) // 2
        return '{}A{}B'.format(cntA, cntB)
