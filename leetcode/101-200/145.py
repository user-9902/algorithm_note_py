"""
@title:      145. 二叉树的后序遍历
@difficulty: 简单
@importance: 5/5
@tags:       后序遍历
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              递归
        @time complexity:   O(n)
        @space complexity:  O(n)    调用栈开销
        @description:       后序的递归实现。对于一个树，先处理其左子树，再处理右子树，然后是根节点
        """
        res = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              非递归实现
        @time complexity:   O(n)
        @space complexity:  O(n)    栈的开销
        @description:       不同于前缀和中缀的实现
        """
        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            res.append(cur.val)
            stack.append(cur.left)
            stack.append(cur.right)
        return res[::-1]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        @tags:              后序 Morris
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:
        """
        # todo
        pass
