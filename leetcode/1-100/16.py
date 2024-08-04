"""
16. 最接近的三数之和
difficulty: 中等
importance: 4/5
tags:       双指针
"""
from typing import List
from math import inf


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        同leet code 15，这里更简单无需去重，但可以去重优化。
        优化点有：
            abs 如在变大即可停止
            获得最优解既target 即可停止
            当前枚举的值比ans大
        """
        n = len(nums)
        nums.sort()

        ans = inf
        for i in range(n - 2):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1

            while l < r:
                cur = nums[l] + nums[r] + nums[i]
                if cur == target:
                    return target

                if abs(cur - target) < abs(ans - target):
                    ans = cur

                elif cur > target:
                    r -= 1
                else:
                    l += 1
        return ans
