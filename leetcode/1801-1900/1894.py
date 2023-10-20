"""
1894. 找到需要补充粉笔的学生编号
binary search + 前缀和
"""

from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        for i in range(1, n):
            chalk[i] = chalk[i-1] + chalk[i]
        k %= chalk[-1]
        # 二分寻找 > k
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r) // 2
            if chalk[mid] <= k:
                l = mid + 1
            else:
                r = mid - 1
        return r


Solution.chalkReplacer(chalk=[5, 1, 5], k=22)
