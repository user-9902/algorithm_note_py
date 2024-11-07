"""
@title:      410. 分割数组的最大值
@difficulty: 中等
@importance: 4/5
@tags:       dp 二分 贪心
"""

from typing import List
from math import inf
from functools import cache


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        @tags:              记忆化搜索
        @time complexity:   O(nk)
        @space complexity:  O(nk)
        @deacription:       f[i][k] = min(max(f[x][k-1], sum(x+1:i)))
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = nums[i] + pre[i]

        @cache
        def dfs(r, k):
            if k == 1:
                return pre[r]
            res = inf
            for i in range(k-1, r):
                cur = pre[r] - pre[i]
                v = max(cur, dfs(i, k-1))
                if v < res:
                    res = v
            return res
        return dfs(n, k)

    def splitArray(self, nums: List[int], k: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(nk)
        @space complexity:  O(nk)
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = nums[i] + pre[i]

        f = [[inf] * (k + 1) for _ in range(n+1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for x in range(i):
                    f[i][j] = min(
                        f[i][j],
                        # 子问题，当前区间的和
                        max(f[x][j - 1], pre[i] - pre[x])
                    )
        return f[n][k]

    def splitArray(self, nums: List[int], k: int) -> int:
        """
        @tags:              二分
        @time complexity:   O(nlog(sum−maxn))
        @space complexity:  O(1)
        @description:       尝试所有的分组上限可能，组的最大值[max(nums), sum(nums)], 二分查找答案
        """
        # 尝试按照x分组，
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= k

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
