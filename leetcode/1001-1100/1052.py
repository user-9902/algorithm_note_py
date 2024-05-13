"""
1052. 爱生气的书店老板
difficulty: 简单
importance: 3/5
tags:       滑动窗口
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        res = 0
        # 先收割无技巧时的满意度
        for i in range(n):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0

        # 能通过技巧在剩余满意度中获取的最大值
        cur = max1 = sum(customers[0:minutes])
        for i in range(minutes, n):
            cur -= customers[i-minutes]
            cur += customers[i]
            max1 = max(cur, max1)

        return res + max1
