"""
25. K 个一组翻转链表
遍历链表
记录遍历次数，达到k次时反转，
注意：有无反转影响返回的头节点；反转的节点如何与后续节点链接
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # special case
        if k == 1 or head is None or head.next is None:
            return head
        # 记录需要反转节点的起止位置
        start = head
        end = head
        res = None  # 首次反转完的头节点
        pre_end = None  # 前一轮反转的尾节点

        while end:
            counter = 0  # 记录遍历次数，达到k次需要反转
            while end and counter != k:
                end = end.next
                counter += 1
            if counter == k:
                # 这里开始反转链表,反转的过程可以参考下面注释掉的 reverseLinkList 方法
                pre = start
                cur = pre.next
                while counter - 1 > 0:
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                    counter -= 1
                # 记录首次反转完的头节点
                res = res or pre
                # 处理上一轮反转的尾节点
                if pre_end:
                    pre_end.next = pre
                pre_end = start
                # 移动start
                start = end
        if pre_end:
            pre_end.next = start
        return res or head

    # def reverseLinkList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     """
    #     反转链表，用来参考反转，题：LCR 024
    #     快慢指针来反转
    #     """
    #     # space cases
    #     if head is None or head.next is None:
    #         return head

    #     pre = head
    #     cur = head.next
    #     pre.next = None   # 头节点变尾节点，next置空
    #     while cur:
    #         tmp = cur.next  # 守卫，防止丢失cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = tmp
    #     return pre
