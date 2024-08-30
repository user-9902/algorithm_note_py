"""
@title:      86. 分隔链表
@difficulty: 简单
@importance: 5/5
@tags:       指针 链表
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        @tags:              指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       分两段 再拼接
        """
        less = ListNode()
        more = ListNode()
        a = less
        b = more
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        less.next = b.next
        more.next = None
        return a.next
