"""
合并k个升序链表
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _merge_two_list(self, la: Optional[ListNode], lb: Optional[ListNode]) -> Optional[ListNode]:
        """
        辅助方法，合并两个有序链表
        """
        if la is None or lb is None:
            return la or lb

        setry = ListNode()  # 头节点守卫
        curr = setry
        while la and lb:
            if la.val <= lb.val:
                curr.next = la
                la = la.next
            else:
                curr.next = lb
                lb = lb.next
            curr = curr.next

        curr.next = la or lb
        return setry.next

    def solution1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        按照合并两条链表的方式，顺序合并多有序链表
        """
        setry = ListNode() # 守卫节点
        for l in lists:
            if l:
                setry.next = self._merge_two_list(setry.next, l)
        return setry.next

    def solution2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        堆排，将多链表视为乱序数组即可
        """
        pass


if __name__ == '__main__':
    lists=[
        ListNode(2),
        None,
        ListNode(-1)
    ]
    test=Solution()
    res=test.solution1(lists)

