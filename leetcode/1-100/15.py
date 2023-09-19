"""
15. 三数之和
三数之和，等价于两数之和问题（两数的和为0转为动态的值）
将数组转为有序，双指针
去重
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(0, n-2):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 极值优化
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                s = nums[l] + nums[r] + nums[i]
                # 移动双指针
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # 去重
                    while nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    # 去重
                    while nums[r] == nums[r+1]:
                        r -= 1
        return ans


a = Solution().threeSum([0, 1, 2, -1, 4, 1])
print(a)
