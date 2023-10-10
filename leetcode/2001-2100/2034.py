"""
2034. 股票价格波动
哈希表，设计
需要花心思设计
显然update的执行会影响maximum minimum current的结果
因此在update中维护这些值是最合理的
参考：leetcode官方题解
"""

from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.pricelist = SortedList()
        self.timestamp_map = {}
        self.max_i = 0

    def update(self, timestamp: int, price: int) -> None:
        # 需要维护价格队列
        if timestamp in self.timestamp_map:
            self.pricelist.discard(self.timestamp_map[timestamp])
        self.pricelist.add(price)
        self.timestamp_map[timestamp] = price

        self.max_i = max(self.max_i, timestamp)

    def current(self) -> int:
        return self.timestamp_map[self.max_i]

    def maximum(self) -> int:
        return self.pricelist[-1]

    def minimum(self) -> int:
        return self.pricelist[0]


test = StockPrice()
test.update(1, 10)
test.update(2, 5)
test.current()
test.maximum()
test.update(1, 3)
test.maximum()
test.update(4, 2)
test.minimum()
