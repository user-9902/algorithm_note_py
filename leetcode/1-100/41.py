"""
41. 缺失的第一个正数
题目要求O(n)的时间复杂度
需要明确的一点是，结果一定的在[1, len(nums) + 1]中
ps：两种解法均参考leetcode官方
    理顺数组的方式还算能想到
    标记的方法实在是巧妙
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        哈希表
        为出现过的数字打上标记，这里的标记即是符号。
        既然标记是负号，这里就需要将 <= 0 的值转正，这里转为 nums_len + 1 就不会对结果产生干扰了
        数组中出现过的正数，将对应下标的数打上标记（-不会对后续的遍历产生影响，取绝对值即可），当然不能越界
        标记完后，遍历数组，第一正数（既没被打上标记的数）就是结果
        """
        nums_len = len(nums)

        for i in range(nums_len):
            if nums[i] <= 0:
                nums[i] = nums_len + 1

        for i in range(nums_len):
            num = abs(nums[i])
            if num <= nums_len:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(nums_len):
            if nums[i] > 0:
                return i + 1

        return nums_len + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        """
        将nums理顺
        遍历nums，通过置换的方式来理顺nums
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] < n + 1 and nums[nums[i] - 1] != nums[i]:
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
