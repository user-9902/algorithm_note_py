"""
@title:      284. 窥视迭代器
@difficulty: 简单
@importance: 5/5
@tags:       迭代器
"""


class PeekingIterator:
    """
    @tags:              迭代器
    @time complexity:   O(1)
    @space complexity:  O(1)
    @description:       peek不移动指针，快慢指针的思想
    """

    def __init__(self, iterator):
        self.iter = iterator
        self.tmp = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.tmp

    def next(self):
        res = self.tmp
        self.tmp = self.iter.next() if self.iter.hasNext() else None
        return res

    def hasNext(self):
        return self.tmp is not None
