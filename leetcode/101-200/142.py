"""
142. 环形链表 II
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针判断是否存在环
            环中相对速度为1，所以快指针一定会追上慢指针
        相遇时，设非环路径为a，环内长度为b
            
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while slow is not head:
                    head = head.next
                    slow = slow.next
                return slow

        return None
