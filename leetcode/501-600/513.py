"""
@title:      513. 找树左下角的值
@difficulty: 中等
@importance: 1/5
@tags:       bfs
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       bfs 同 leetcode 117 无需二外空间存储层级
        """
        queue = [root]

        while queue:
            leftNode = None

            n = len(queue)
            for _ in range(n):
                cur = queue.pop(0)
                if leftNode is None:
                    leftNode = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if not queue:
                return leftNode.val
