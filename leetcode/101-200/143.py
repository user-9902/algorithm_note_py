"""
@title:      143. 重排链表
@difficulty: 中等
@importance: 5/5
@tags:       快慢指针 math
"""

from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        @tags:              线性表
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       线性表，存储下所有节点，重新构建
        """
        pass

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        @tags:              寻找链表中间节点 + 反转链表
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       1 -> 2 -> 3 -> 4 -> 5
                            1 -> 2      3 -> 4 -> 5
                            1 -> 2      5 -> 4 -> 3
                            1 -> 5 -> 2 -> 4 -> 3   
        """
        # 寻找中间节点 见 leetcode 876
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        end = slow  # 给第三步拼接
        # 反转  见 leetcode 206
        pre = None
        while slow:
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        # 拼接
        while head != end:
            tmp1 = head.next
            tmp2 = pre.next
            head.next = pre
            pre.next = tmp1
            head = tmp1
            pre = tmp2
        if head.next == head:
            head.next = None
