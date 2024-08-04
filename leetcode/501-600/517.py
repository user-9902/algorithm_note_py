"""
@title:      517. 超级洗衣机
@difficulty: 中等
@importance: 4/5
@tags:       greedy
"""
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        @tags:              greedy
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       见下方注释
        """
        n = len(machines)
        sum_m = sum(machines)
        if sum_m % n != 0:
            return -1
        avg = sum_m // n

        pre = 0  # 前缀和
        ans = 0
        for i, num in enumerate(machines):
            post = sum_m - pre - num    # 后缀和
            l = pre - avg * i   # i 左侧多多少个 (ps:如为负数则表示缺多少个)
            r = post - avg * (n - 1 - i)    # i 右侧多多少个

            if l < 0 and r < 0:  # 左右都缺，只能从i上拿
                ans = max(0-l-r, ans)
            else:
                # 左右都多可以同时向 i 输送 ； 一边缺一边少，可以一边朝 i 输送，i可也一边向外输出
                ans = max(abs(l), abs(r), ans)
            pre += num
        return ans


Solution().findMinMoves([0, 0, 11, 5])
