"""
dfs
后续遍历
判断 max_cur = max(cur.val, cur.val + left.val, cur.val + right.val)
cur.val + left.val + right.val 会形成回路阻断流程，但同样可能存在最大值
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node) -> int:
            left = 0
            right = 0

            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            r = max(node.val, node.val + left, node.val + right)

            res.append(r)
            if node.left and node.right:
                res.append(node.val + left + right)

            return r

        dfs(root)

        return max(res)
