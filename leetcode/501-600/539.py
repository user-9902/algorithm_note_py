"""
@title:      539. 最小时间差
@difficulty: 简单
@importance: 3/5
@tags:       sort
"""

from math import inf
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        @tags:              sort              
        @time complexity:   O(nlogn)
        @space complexity:  O(logn)
        @description:       将时间排序，比较前后两个时间的差值，寻找最小的值。注意首尾的对比。
        """
        n = len(timePoints)
        # 鸽巢原理 这里是优化点 一天一共就 1440 分钟 所以长度超过1440的输入一定有重复结果一定是0
        if n > 1440:
            return 0
        for i in range(n):
            [h, m] = timePoints[i].split(":")
            timePoints[i] = int(h) * 60 + int(m)
        timePoints.sort()
        # 首尾差值
        res = timePoints[0] + 1440 - timePoints[n - 1]
        for i in range(1, n):
            res = min(res, timePoints[i] - timePoints[i - 1])
        return res
