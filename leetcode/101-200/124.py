"""
@title:      124. 二叉树中的最大路径和
@difficulty: 中等
@importance: 5/5
@tags:       dfs 后续遍历
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        @tags:              dp
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       后序遍历，分析左右子节点能和当前节点组成的路径可能，cur + left, cur + right, cur, cur + left + right
                            但注意返回给 cur 父节点时，需要减少 cur + left + right 这个情况
        """
        res = []

        def dfs(node) -> int:
            # 左右节点的最大值
            left = right = 0

            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            r = max(node.val, node.val + left, node.val + right)
            res.append(max(r, node.val + left + right))
            return r

        dfs(root)

        return max(res)
