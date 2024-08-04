"""
18. 四数之和
difficulty: 中等
importance: 4/5
tags:       双指针
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        leet code 15变体
        """
        nums.sort()
        n = len(nums)

        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = nums[i] + nums[j] - target
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[l] + nums[r] < -t:
                        l += 1
                    elif nums[l] + nums[r] > -t:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return ans
