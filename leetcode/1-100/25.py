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
        ans = None

        cur = head  # 遍历
        start = cur  # 反转起始点
        cnt = 0  # 计数

        pre_s = None  # 前一轮反转，反转后的尾巴
        while cur:
            cnt += 1
            cur = cur.next
            # 开始反转
            if cnt == k:
                cnt = 0

                s = start
                pre = None
                for _ in range(k):
                    nxt = start.next
                    start.next = pre
                    pre = start
                    start = nxt
                # 前一轮反转后的尾巴，指向本轮反转后的头
                if pre_s:
                    pre_s.next = pre
                pre_s = s
                # 是否发生反转影响结果
                if ans is None:
                    ans = pre
        # 存在剩余未反转部分
        if cnt > 0 and pre_s:
            pre_s.next = start

        return ans or head

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
