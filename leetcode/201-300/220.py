"""
220. 存在重复元素 III
滑动窗口
"""
from sortedcontainers import SortedSet
from typing import List


class Solution:
    # def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    #     """
    #     按照题意枚举i和j O(n^2)
    #     超时 错误❌
    #     """
    #     n = len(nums)
    #     for i in range(n-1):
    #         k = i + indexDiff + 1 if i + indexDiff < n else n
    #         for j in range(i+1, k):
    #             if abs(nums[i] - nums[j]) <= valueDiff:
    #                 return True
    #     return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        l = 0
        r = indexDiff + 1
        sortedset = SortedSet(nums[:r])
        mid = r // 2 - 1
        odd = r % 2 == 0

        print(r, mid, odd)
        while r < n:
            if odd:
                if sortedset[mid] - s
            else:

            r += 1
            l += 1


Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 1, 0)


sortedset = SortedSet([1, 44, 112, 73, 123, 2, 65, 1])
sortedset.add(22)
print(sortedset[1])
sortedset.discard(1)
print(sortedset)
