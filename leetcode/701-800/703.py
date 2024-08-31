"""
@title:      703. 数据流中的第 K 大元素
@difficulty: 简单
@importance: 1/5  重复
@tags:       优先队列 sort
"""
from typing import List
from sortedcontainers import SortedList


class KthLargest:
    """
    @tags:              
    @time complexity:   O(nlogn)
    @space complexity:  O(n)
    @description:       
    """

    def __init__(self, k: int, nums: List[int]):
        self.arr = SortedList(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.arr.add(val)      # 可优化空间复杂度 只需要保存长度k的队列
        return self.arr[-self.k]
