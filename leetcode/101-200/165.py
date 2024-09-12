"""
@title:      165. 比较版本号
@difficulty: 简单
@importance: 2/5
@tags:       顺序比较
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        @tags:              顺序比较
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       从左向右比较
        """
        l1 = version1.split(".")
        l2 = version2.split(".")
        n, m = len(l1), len(l2)
        res = 0
        for i in range(max(n, m)):
            if res != 0:
                break
            a = int(l1[i]) if i < n else 0
            b = int(l2[i]) if i < m else 0
            if a > b:
                res = 1
            if a < b:
                res = -1
        return res
