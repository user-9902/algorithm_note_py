"""
1726. 同积元组
hashmap
"""

from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        bf 
        超时😓 ❌
        显然会超时的，不知道我在想什么
        """
        nums.sort()
        n = len(nums)

        ans = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for x in range(j+1, n-1):
                    for y in range(x + 1, n):
                        if nums[i] * nums[j] == nums[x] * nums[y] or nums[i] * nums[x] == nums[j] * nums[y] or nums[i] * nums[y] == nums[x] * nums[j]:
                            ans += 1
        return ans * 8

    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums_map = {}
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] * nums[j] in nums_map:
                    nums_map[nums[i] * nums[j]] += 1
                else:
                    nums_map[nums[i] * nums[j]] = 1

        for v in nums_map.values():
            if v > 1:
                ans += v * (v - 1) // 2
        return ans * 8


Solution().tupleSameProduct([1, 2, 4, 5, 10])
