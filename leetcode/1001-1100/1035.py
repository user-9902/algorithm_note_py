"""
1035. 不相交的线
LCS, dp
题目完全等价于最长公共子序列
区间dp
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        压缩至一维
        """
        n = len(nums1)
        m = len(nums2)

        f = [0] * (m + 1)

        for i, x in enumerate(nums1):
            pre = 0
            for j, y in enumerate(nums2):
                tmp = f[j+1]
                f[j+1] = pre + 1 if x == y else max(f[j+1], f[j])
                pre = tmp

        return f[-1]


Solution.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])
