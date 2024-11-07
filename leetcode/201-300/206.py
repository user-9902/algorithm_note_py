"""
@title:      206. 反转链表
@difficulty: 简单
@importance: 5/5
@tags:       指针
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        @tags:              守卫指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        """
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
