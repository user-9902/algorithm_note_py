"""
@title:      623. 在二叉树中增加一行
@difficulty: 简单
@importance: 4/5
@tags:       bfs 
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        """
        @tags:              bfs
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       拿到第depth-1行即可
        """
        # 一般化处理第一层
        res = TreeNode()
        res.left = root
        # 得到depth行
        queue = [res]
        while queue:
            if depth == 1:
                break
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if cur is None:
                    continue
                queue.append(cur.left)
                queue.append(cur.right)
            depth -= 1

        for node in queue:
            if node is None:
                continue
            tmp = node.left
            node.left = TreeNode(val, left=tmp)
            tmp = node.right
            node.right = TreeNode(val, right=tmp)

        return res.left
