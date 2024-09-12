"""
@title:      2948. 交换得到字典序最小的数组
@difficulty: 中等
@importance: 4/5
@tags:       sort
"""
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        @tags:              分组 sort
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        """
        n = len(nums)
        nums2 = sorted(zip(nums, range(n)))

        ans = [0] * n
        left = 0
        for i in range(1, n):
            if nums2[i][0] - nums2[i-1][0] > limit:
                idxs = sorted(nums2[j][1] for j in range(left, i))
                for j in range(left, i):
                    ans[idxs[j-left]] = nums2[j][0]
                left = i
        idxs = sorted(nums2[j][1] for j in range(left, n))
        for j in range(left, n):
            ans[idxs[j-left]] = nums2[j][0]
        return ans
