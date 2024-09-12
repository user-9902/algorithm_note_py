"""
@title:      141. 环形链表
@difficulty: 简单
@importance: 5/5
@tags:       快慢指针 
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        @tags:              快慢指针
        @time complexity:   O(2n)
        @space complexity:  O(1)
        @description:       快慢指针，快指针“速度”为 2， 慢指针“速度”为 1
                                存在环：快指针相对慢指针“速度”为 1，两者一定会在环中相遇
                                不存在环：快指针会优先指向None
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
