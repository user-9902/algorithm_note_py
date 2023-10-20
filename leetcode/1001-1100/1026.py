"""
1026. 节点与其祖先之间的最大差值
dfs
计算点距离线段的最远距离
所以需要保留前缀最大值&前缀最小值
"""

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        dfs 
        """
        ans = 0

        def dfs(node, mi, ma):
            if node is None:
                return

            nonlocal ans
            ans = max(ans, abs(mi-node.val), abs(ma-node.val))

            nmi = min(mi, node.val)
            nma = max(ma, node.val)
            dfs(node.left, nmi, nma)
            dfs(node.right, nmi, nma)

        dfs(root, root.val, root.val)
        return ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(10)
d = TreeNode(9)
a.left = b
b.left = c
b.right = d

Solution().maxAncestorDiff(a)
