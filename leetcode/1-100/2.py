from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 递归，函数上下文的创建开销大
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode],
                      carry=0) -> Optional[ListNode]:
        # 当都为空节点的时候即可返回
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        # 交换两个链表，l1和l2是同质的，这样确保l1比l2长，减少后续代码复杂度
        if l1 is None:
            l1, l2 = l2, l1
        # 两数和加上进位
        sum = l1.val + (l2.val if l2 else 0) + carry
        l1.val = sum % 10

        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None,
                                     sum // 10)
        return l1

    # 迭代
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
