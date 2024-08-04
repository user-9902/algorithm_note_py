"""
name:       41. 缺失的第一个正数
difficulty: 中等
importance: 4/5
tags:       array
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       ❌ 结果一定出现在 1 至 n+1 中，我们创建一个n+1长度的数组来记录nums中的数字是否出现，出现过的数字打上标记。这里未满足题意的常数空间复杂度，但是是一个正确解的降级实现，便于理清思路。
        """
        n = len(nums)
        # 用来记录 0 - n+1 之间的数字是否出现
        arr = [0] * (n + 1)
        for i in nums:
            if 0 < i < n + 1:
                # 出现的打上标记 1
                arr[i - 1] = 1
        # 查看那个数字未出现
        for i in range(n):
            if arr[i] == 0:
                return i + 1
        return n + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        @tags:              hashmap
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       上个解创造了一个额外数组来进行记录，通过0和1来标记数字是否出现，这里我们不使用额外空间，在原数组上用正负号来表示数字是否出现。注意标记前先去除nums中负数，nums中负数不会影响结果，但会影响标记过程。
        """
        n = len(nums)

        # 去除对标记阶段有影响的值：负数和0（0可去除可不去除）
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 标记数字是否出现
        for i in range(n):
            num = abs(nums[i])
            if num < n + 1:
                nums[num - 1] = -abs(nums[num - 1])

        # 获取结果
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        @tags:              swap
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       nums中的数字是乱序的，我们整理下即可，将元素置换至正确的位置
        """
        n = len(nums)
        for i in range(n):
            # 将元素交换至正确位置 交换的两个元素值相同会死循环
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                a = nums[i] - 1
                b = i
                nums[a], nums[b] = nums[b], nums[a]
        # 查找缺失的元素
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
