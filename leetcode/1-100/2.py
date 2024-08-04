"""
name:       2. 两数相加
difficulty: 简单
importance: 3/5
tags:       math
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = node = ListNode(0)
        rest = 0
        while l1 or l2 or rest:
            # 数学从低位到高位相加 同时加上进位数
            summ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rest

            node.next = ListNode(summ % 10)
            node = node.next

            rest = summ // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next
