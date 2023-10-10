"""
901. 股票价格跨度
单调栈
维护一个单调递减stack
栈中需要保存下标（即第几天）以及对应的price
"""


from math import inf


class StockSpanner:

    def __init__(self):
        # date, price
        self.stack = [(-1, inf)]
        self.date = -1

    def next(self, price: int) -> int:
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.date += 1
        self.stack.append((self.date, price))
        return self.date - self.stack[-2][0]


instance = StockSpanner()
instance.next(100)
instance.next(80)
instance.next(60)
instance.next(70)
instance.next(75)
