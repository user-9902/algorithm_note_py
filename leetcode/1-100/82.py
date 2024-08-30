"""
name:       82. 删除排序链表中的重复元素 II
difficulty: 中等
importance: 5/5
tags:       快慢指针
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
        @description:       分类讨论 快慢指针
        """
        # 一般化处理头节点
        res = s = ListNode(-101)
        f = head

        cur = None
        while f:
            # 不需要当前节点 f
            if f.next and f.val == f.next.val:
                cur = f.val
                while f and f.val == cur:
                    f = f.next
                s.next = None
            # 需要当前节点 f
            else:
                s.next = f
                f = f.next
                s = s.next
        return res.next
