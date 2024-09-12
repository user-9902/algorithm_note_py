"""
@title:      113. 路径总和 II
@difficulty: 中等
@importance: 3/5
@tags:       dfs 回溯
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        @tags:              先序dfs 回溯
        @time complexity:   O(n)
        @space complexity:  O(n)
        """
        ans = []
        cur = []
        s = 0
        if root is None:
            return ans

        def dfs(node):
            nonlocal s
            if node is None:
                return
            cur.append(node.val)
            s += node.val
            if node.left or node.right:
                dfs(node.left)
                dfs(node.right)
            else:
                if s == targetSum:
                    ans.append(cur.copy())
            s -= node.val
            cur.pop()

        dfs(root)
        return ans
