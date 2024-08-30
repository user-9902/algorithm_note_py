"""
@title:      105. 从前序与中序遍历序列构造二叉树
@difficulty: 中等
@importance: 5/5
@tags:       bfs
"""
from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        @tags:              dfs递归
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       dfs
        """
        def dfs(pre_s, in_s):
            n = len(pre_s)
            if n == 0:
                return None
            root = TreeNode(pre_s[0])

            if n == 1:
                return root

            idx = 0
            for i, v in enumerate(in_s):
                if v == pre_s[idx]:
                    idx = i
                    break
            root.left = dfs(pre_s[1:idx+1], in_s[:idx])
            root.right = dfs(pre_s[idx+1:], in_s[idx+1:])
            return root

        return dfs(preorder, inorder)
