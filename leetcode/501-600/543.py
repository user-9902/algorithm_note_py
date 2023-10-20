"""
543. 二叉树的直径
dfs
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        dfs 左右子树高度和
        """

        ans = 0

        def dfs(node):
            if node is None:
                return 0
            l_height = dfs(node.left)
            r_height = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_height + r_height + 1)
            return max(l_height, r_height) + 1
        dfs(root)
        return ans
