"""
@title:      1353. 最多可以参加的会议数目
@difficulty: 中等
@importance: 5/5
@tags:       sort greedy 优先队列
"""


from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        @tags:              sort greedy 优先队列
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       维护时间线，在能参加的会议中挑选先结束的参加
        """
        n = len(events)
        que = []
        events.sort()
        ans = 0
        idx = 0
        time = 0
        for _ in range(n):  # 遍历每个会议
            if not que:
                que.append(events[idx][::-1])
                idx += 1
            cur = heapq.heappop(que)
            if cur[0] >= time + 1:  # 最先结束的会议能否参加
                time = max(cur[1], time + 1)
                ans += 1
            while idx < n and time + 1 >= events[idx][0]:  # 将能参加的会议加入优先队列
                heapq.heappush(que, events[idx][::-1])  # 按结束时间的优先级排队
                idx += 1
        return ans
