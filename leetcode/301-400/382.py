"""
@title:      382. 链表随机节点
@difficulty: 中等
@importance: 5/5
@tags:       随机抽样 蓄水池抽样算法

空间复杂度为 O(n) 的解，能通过题目，
但本题拓展需要我们使用O(1)的额外空间来解决
"""


from typing import Optional
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @tags:              💲蓄水池抽样算法
    @time complexity:   init: O(1) getRandom: O(n)
    @space complexity:  O(1)
    @description:       在大数据流处理中，往往无法将所有数据加载至内存中，如何从未知大小的数据流种选取k个数据？
                        抽样数据 k == 1 时（即本题）：
                        我们从第一个元素开始遍历：
                        元素1：1的概率保留 元素1
                        元素2：1/2 的概率替换保留的数
                        元素3：1/3 的概率替换保留的数

                        更通用的，当需要k个样本时：
                        i <= k: 前k个数直接保留
                        i > k:  元素 i 有 k / i 的概率保留（保留通过与选中的 k 个元素随机选一个替换实现）

                        （可通过数学归纳法证明）
    """

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        i = 0
        res = None
        while node:
            if random.randint(1, 1 + i) == 1:
                res = node.val
            i += 1
            node = node.next
        return res
