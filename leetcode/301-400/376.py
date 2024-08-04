"""
@title:      376. 摆动序列
@difficulty: 3/5
@importance: 4/5
@tags:       dp
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       见下方注释
        """
        n = len(nums)

        up = [1] + [0] * (n - 1)    # 结尾为上升的最长子序列
        down = [1] + [0] * (n - 1)  # 结尾为下降的最长子序列
        for i in range(1, n):
            if nums[i] > nums[i - 1]:   # 当前为上升
                # up[i] = max(up[i-1], down[i-1] + 1)
                up[i] = max(down[i - 1] + 1, up[i - 1])
                down[i] = down[i - 1]   # 当前为上升，结尾为下降的down保持不变
            elif nums[i] < nums[i - 1]:
                down[i] = max(up[i - 1] + 1, down[i - 1])
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n-1], down[n-1])

    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       状态转移方程中，不难发现下标为 i 时的状态只与下标 i-1 时有关，因此可以压缩状态数组的空间复杂度。
        """
        n = len(nums)

        up = 1
        down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = max(down + 1, up)
            elif nums[i] < nums[i - 1]:
                down = max(up + 1, down)

        return max(up, down)
