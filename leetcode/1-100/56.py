"""
@title:      56. 合并区间
@difficulty: 中等
@importance: 5/5
@tags:       sort
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(1)
        @description:       排序，判断是否重合即可
        """
        n = len(intervals)
        intervals.sort()
        ans = []
        cur = intervals[0]
        for i in range(1, n):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[i][1])
            else:
                ans.append(cur)
                cur = intervals[i]
        ans.append(cur)
        return ans
