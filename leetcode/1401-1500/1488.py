"""
1488. 避免洪水泛滥
greedy + 二分
记录下能够进行放水的日期
当会发生i池子发生洪水的时候判断，i池子装入水至i池子发生洪水的那天之间是否存在一天能清空池子
贪心的体现：越早清空池子越好

参考：leetcode官方题解
"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        sl = SortedList()
        mp = {}
        ans = [1] * n

        for i, v in enumerate(rains):
            if not v == 0:
                # 这天无法清空水池
                ans[i] = -1
                # 池子中已经有水了
                if v in mp:
                    # 二分查找，装入水之后直至再次转入水的日期之间能否清空池子
                    r = sl.bisect_right(mp[v])
                    # 不存在能防水的日期了
                    if r == len(sl):
                        return []
                    ans[sl[r]] = v
                    sl.discard(sl[r])
                mp[v] = i
            else:
                sl.add(i)

        return ans
