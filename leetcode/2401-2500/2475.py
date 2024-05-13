"""
2475. 数组中不等三元组的数目
"""
from typing import List
from collections import Counter


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        """
        bf
        O(n^3) 显然是不能接受的
        """
        n = len(nums)

        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        ans += 1
        return ans

    def unequalTriplets1(self, nums: List[int]) -> int:
        """
        sort
        """
        n = len(nums)

        nums.sort()

        i = j = ans = 0
        while i < n:
            while j < n and nums[j] == nums[i]:
                j += 1
            ans += i * (j - i) * (n - j)
            i = j
        return ans

    def unequalTriplets2(self, nums: List[int]) -> int:
        """
        hash map
        """
        a, c = 0, len(nums)
        ans = 0
        for b in Counter(nums).values():
            c -= b
            ans += a * b * c
            a += b
        return ans


Solution().unequalTriplets([4, 4, 2, 4, 3])
