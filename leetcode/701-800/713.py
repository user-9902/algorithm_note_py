"""
713. 乘积小于 K 的子数组
滑动窗口
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        multi = 1
        ans = 0

        for r in range(0, n):
            multi *= nums[r]
            while multi >= k:
                multi /= nums[l]
                l += 1
            # [a] -> [a,b] [a,...,b] -> [a,...,b,c] 的过程中ans刚好加r-l+1
            ans += r - l + 1
        return ans


Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)
