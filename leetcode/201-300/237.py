"""
@title:      203. 移除链表元素
@difficulty: 简单
@importance: 4/5
@tags:       链表
"""
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        """
        @tags:              链表
        @time complexity:   O(1)
        @space complexity:  O(1)
        @description:       💲这里是想考察删除链表当前节点的一种方式。
        """
        node.val = node.next.val
        node.next = node.next.next
