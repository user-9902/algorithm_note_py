"""
19. 删除链表的倒数第 N 个结点
快慢指针
使得slow和fast距离差为n
注意移动的次数
特别注意只有一个节点的情况
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 守卫节点
        n_head = ListNode()
        n_head.next = head
        # 快慢指针
        fast = slow = n_head
        for i in range(n):
            if fast:
                fast = fast.next

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next

        tmp = slow.next.next
        slow.next = tmp
        return n_head.next
