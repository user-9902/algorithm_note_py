"""
@title:      669. 修剪二叉搜索树
@difficulty: 中等
@importance: 5/5
@tags:       二叉搜索树
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        """
        @tags:              二叉搜索树
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       利用二叉搜索树的特性:
                                如果node.left < low 那么 node.left.left 显然也 < low
                                同样的node.right > high 那么 node.right.right 显然也 > high
        """
        # 根节点单独处理
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left

        res = root
        while root:
            while root.left and root.left.val < low:
                root.left = root.left.right
            root = root.left

        root = res
        while root:
            while root.right and root.right.val > high:
                root.right = root.right.left
            root = root.right
        return res
