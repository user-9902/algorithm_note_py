"""
19. 删除链表的倒数第 N 个结点
difficulty: 简单
importance: 5/5
tags:       双指针
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        注意移动的次数
        特别注意只有一个节点的情况
        """
        ans = ListNode()
        ans.next = head

        s = f = ans
        for n in range(n + 1):
            f = f.next

        while f:
            f = f.next
            s = s.next
        s.next = s.next.next

        return ans.next
