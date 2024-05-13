"""
102. 二叉树的层序遍历
bfs
记录层序即可
"""
from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        bfs
        """
        queue = [(root, 0)]
        ans = []

        while queue:
            node, cnt = queue.pop(0)

            if node is None:
                continue

            if cnt == len(ans):
                ans.append([])
            ans[-1].append(node.val)

            if node.left:
                queue.append((node.left, cnt + 1))
            if node.right:
                queue.append((node.right, cnt + 1))

        return ans
