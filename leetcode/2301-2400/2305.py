"""
@title:      2305. 公平分发饼干
@difficulty: 中等
@importance: 0/5    重复的题。见leetcode 1723
@tags:       状压dp
"""

from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """ 
        @tags:              状压dp
        @time complexity:   O(3^n)
        @space complexity:  O(2^n)
        @description:       leetcode 1723 中dp压缩至一维了，这里为压缩。
        """
        n = len(cookies)
        u = 1 << n
        sums = [0] * u
        for i, v in enumerate(cookies):
            idx = 1 << i

            for j in range(idx):
                sums[idx | j] = sums[j] + v

        f = [sums.copy() for _ in range(k)]
        for i in range(1, k):
            # j 表示总集合
            for j in range(u-1, 0, -1):
                t = j
                while t:
                    v = f[i-1][j ^ t]
                    if sums[t] > v:
                        v = sums[t]
                    if v < f[i][j]:
                        f[i][j] = v
                    t = (t - 1) & j
        return f[k-1][u]
