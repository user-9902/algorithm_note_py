"""
@title:      2433. 找出前缀异或的原始数组
@difficulty: 简单
@importance: 4/5
@tags:       前缀异或和
"""
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        @tags:              前缀异或和
        @time complexity:   O(n) 
        @space complexity:  O(1)
        @description:       前缀异或和数组，还原原始数组
        """
        n = len(pref)
        ans = [0] * n
        ans[0] = pref[0]
        for i in range(1, n):
            ans[i] = pref[i] ^ pref[i-1]
        return ans
