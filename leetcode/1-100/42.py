"""
42. 接雨水
每个块能装的雨水由最大前缀和最大后缀中的小者决定
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        dp
        算出最大前后缀然后，然后计算每个块能装的雨水
        cur = min(max_left, max_right) - cur_height
        左右边界的实现实例和列求解一样，只要存储左边界即可，求有边界的时候同时求解即可。
        """
        n = len(height)
        left_max = [0]
        right_max = 0

        res = 0
        for i in range(1, n):
            left_max.append(max(left_max[i - 1], height[i - 1]))
        del left_max[0]

        for i in range(n-2, 0, -1):
            right_max = max(right_max, height[i + 1])
            m = min(right_max, left_max[i - 1])
            if m - height[i] > 0:
                res += (m - height[i])
        return res

    def trap2(self, height: List[int]) -> int:
        """
        双指针
        初始化前后缀
        相向指针，找寻min(pre_max, post_max)
        如: left = 1 时 right = 7 时的pre_max = 2 post_max = 4
            left的最大前缀为2 最大后缀>=4
            right的最大后缀为4 最大前缀>=2
            此时left下标能接多少雨水已经确定了
        """
        pre_max = 0
        post_max = 0
        l = 0
        r = len(height) - 1
        ans = 0

        while l <= r:
            pre_max = max(pre_max, height[l])
            post_max = max(post_max, height[r])
            if pre_max > post_max:
                ans += post_max - height[r]
                r -= 1
            else:
                ans += pre_max - height[l]
                l += 1
        return ans


Solution().trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
