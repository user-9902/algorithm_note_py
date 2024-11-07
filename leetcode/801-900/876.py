"""
@title:      876. 链表的中间结点
@difficulty: 简单
@importance: 5/5
@tags:       快慢指针
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        @tags:              快慢指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       假设节点共有n个
                            n % 2 == 0: 返回第 n // 2 + 1 个节点
                            n % 2 == 1: 返回第 (n+1) // 2 个节点 
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
