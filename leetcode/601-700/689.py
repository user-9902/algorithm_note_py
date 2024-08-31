"""
@title:      689. 三个无重叠子数组的最大和
@difficulty: 中等
@importance: 5/5
@tags:       前缀和 dp
"""

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        @tags:              fs
        @time complexity:   O(n^3) ❌超时
        @space complexity:  O(n)
        @description:       枚举三个空间的所有组合可能
        """
        n = len(nums)
        pre = [i for i in nums]
        for i in range(1, n):
            pre[i] += pre[i-1]
        for i in range(n-1, k-1, -1):
            pre[i] -= pre[i-k]
        max_v = 0
        ans = []
        for i in range(k-1, n-2*k):
            for j in range(i+k, n-k):
                for x in range(j+k, n):
                    total = pre[i] + pre[j] + pre[x]
                    if total > max_v:
                        max_v = total
                        ans = [i-k+1, j-k+1, x-k+1]
        return ans

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        @tags:              前缀和
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       k=1时，题目变简化为了数组中三数的最大和，枚举每个元素，其最大前缀其最大后缀便是该点能组成的最大值。推广至k>1的情况即可
        """
        n = len(nums)
        pre = [i for i in nums]
        for i in range(1, n):
            pre[i] += pre[i-1]
        for i in range(n-1, k-1, -1):
            pre[i] -= pre[i-k]

        pre_max = [k-1] * n
        for i in range(k-1, n):
            if pre[i] > pre[pre_max[i-1]]:
                pre_max[i] = i
            else:
                pre_max[i] = pre_max[i-1]

        post_max = [n-1] * n
        for i in range(n-2, -1, -1):
            if pre[i] >= pre[post_max[i+1]]:
                post_max[i] = i
            else:
                post_max[i] = post_max[i+1]
        max_v = 0
        ans = []
        for i in range(2*k-1, n-k):
            total = pre[pre_max[i-k]] + pre[i] + pre[post_max[i+k]]
            if total > max_v:
                max_v = total
                ans = [pre_max[i-k]-k+1, i-k+1, post_max[i+k]-k+1]
        return ans


Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
