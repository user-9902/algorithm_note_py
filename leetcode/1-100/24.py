"""
24. 两两交换链表中的节点
ListNode
注意头节点为空的情况即可
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        defend = ListNode()
        defend.next = head

        pre = a = b = defend

        while True:
            # 存在练习两个后续节点
            if a.next is None or a.next.next is None:
                break
            pre = a
            a = pre.next
            b = a.next

            pre.next = b
            a.next = b.next
            b.next = a

        return defend.next
