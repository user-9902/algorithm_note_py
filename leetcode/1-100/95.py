"""
@title:      95. 不同的二叉搜索树 II
@difficulty: 简单
@importance: 5/5
@tags:       分治
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        @tags:              分治
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        """
        # 分治  [lo, hi)
        def dfs(lo, hi):
            if lo == hi:
                return [None]
            res = []
            for i in range(lo, hi):
                left = dfs(lo, i)
                right = dfs(i + 1, hi)
                # merge
                for a in left:
                    for b in right:
                        res.append(TreeNode(i, a, b))
            return res

        return dfs(1, n + 1)
