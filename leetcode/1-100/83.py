"""
@title:      83. 删除排序链表中的重复元素
@difficulty: 简单
@importance: 5/5
@tags:       快慢指针 链表
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        @tags:              快慢指针
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       快慢指针
        """
        if head is None:
            return head
        ans = ListNode(next=head)
        slow = head
        fast = head.next
        while fast:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return ans.next
