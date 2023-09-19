"""
42. 接雨水
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        按列求解
        算出左右最大
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
        正序最大前缀和后续最大后缀，始终是递增的
        相向指针，找寻min(pre_max, post_max)
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
