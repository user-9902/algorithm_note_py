"""
@title:      327. 区间和的个数
@difficulty: 困难
@importance: 5/5
@tags:       前缀和 归并分治 树状数组
"""
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        @tags:              前缀和 fs
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       前缀和 ❌超时
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        for l in range(n):
            pre = 0 if l == 0 else nums[l - 1]
            for r in range(l, n):
                if lower <= nums[r] - pre <= upper:
                    ans += 1
        return ans

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        @tags:              前缀和 归并分治
        @time complexity:   O(n*2)
        @space complexity:  O(1)
        @description:       💲归并分治
        """
        # 前缀和
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]

        help = [0] * n

        def merge(l, m, r):
            ans = 0

            # l至m区间 m+1至r区间内的元素是有序的 用双指针来判断符合题意的范围
            a1 = a2 = l
            for i in range(m + 1, r + 1):
                min_v = nums[i] - upper
                max_v = nums[i] - lower
                while a1 <= m and nums[a1] < min_v:
                    a1 += 1
                while a2 <= m and nums[a2] <= max_v:
                    a2 += 1
                ans += a2 - a1

            # 归并排序 这里的排序保证下一轮的 l至m区间和m+1至r区间的有序性
            p1 = l
            p2 = m + 1
            i = 0
            while p1 <= m and p2 <= r:
                if nums[p1] <= nums[p2]:
                    help[i] = nums[p1]
                    p1 += 1
                else:
                    help[i] = nums[p2]
                    p2 += 1
                i += 1

            while p1 <= m:
                help[i] = nums[p1]
                p1 += 1
                i += 1
            while p2 <= r:
                help[i] = nums[p2]
                p2 += 1
                i += 1

            for j in range(i):
                nums[l + j] = help[j]

            return ans

        # 判断区间 [l,r] 之间有多少满足题意的
        def dfs(l, r):
            # 区间长度为 1
            if l == r:
                return int(lower <= nums[l] <= upper)
            else:
                # 区间长度大于 1 进行二分 分别判断左右其中有多少满足题意的，跨左右区间的解交给merge
                m = (l + r) >> 1
                return dfs(l, m) + dfs(m + 1, r) + merge(l, m, r)

        return dfs(0, n - 1)
