"""
@title:      142. 环形链表 II
@difficulty: 中等
@importance: 5/5
@tags:       快慢指针 math
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        @tags:              hasmap
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       记录遍历过的每个节点，存在重复则是入环点
        """
        pass

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        @tags:              快慢指针 math
        @time complexity:   O(2n)
        @space complexity:  O(1)
        @description:       是否存在环的判断见leetcode 141
                            https://leetcode.cn/problems/linked-list-cycle-ii/solutions/1999271/mei-xiang-ming-bai-yi-ge-shi-pin-jiang-t-nvsq/
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
