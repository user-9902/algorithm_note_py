"""
@title:      99. 恢复二叉搜索树
@difficulty: 中等
@importance: 5/5
@tags:       AVL dfs
"""
from typing import Optional
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        @tags:              中序dfs
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       显然是需要中序遍历整个树。问题的关键是有序序列中存在两个错误的值，如何找到他们。
                            3 2 1       1 3 2 4     
                            ^   ^         ^ ^
        """
        a = b = None
        pre = TreeNode(val=-inf)

        # 中序遍历
        def dfs(node: Optional[TreeNode]):
            nonlocal pre, a, b
            if node is None:
                return

            dfs(node.left)
            if node.val < pre.val:
                # 💲有序数组中寻找错序的两个值
                if a is None:
                    a = pre
                    b = node
                else:
                    b = node
            pre = node
            dfs(node.right)

        dfs(root)
        a.val, b.val = b.val, a.val
