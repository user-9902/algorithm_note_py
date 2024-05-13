"""
275. H 指数 II
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        遍历
        """
        n = len(citations)
        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0

    def hIndex(self, citations: List[int]) -> int:
        """
        二分
        """
        n = len(citations)
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            if citations[n-mid] >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r


Solution().hIndex([100])
Solution().hIndex([0])

