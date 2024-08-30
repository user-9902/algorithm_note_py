# Definition for a Node.
"""
@title:      559. N 叉树的最大深度
@difficulty: 中等
@importance: 1/5
@tags:       bfs
"""

from typing import Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       bfs
        """
        l = 0
        if root is None:
            return l
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if cur == None:
                    continue
                for c in cur.children:
                    queue.append(c)
            l += 1
        return l
