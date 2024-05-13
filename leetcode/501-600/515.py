"""
515. 在每个树行中找最大值
dfs; bfs
同leetcode102，补充了dfs的解
遍历时带上层号即可
"""
from typing import List, Optional
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = [(root, 0)]
        ans = []

        while queue:
            node, cnt = queue.pop(0)

            if node is None:
                continue

            if cnt == len(ans):
                ans.append(-inf)
            ans[-1] = max(ans[-1], node.val)

            if node.left:
                queue.append((node.left, cnt + 1))
            if node.right:
                queue.append((node.right, cnt + 1))

        return ans

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, cnt):
            if node is None:
                return
            if cnt > len(ans) - 1:
                ans.append(-inf)
            ans[cnt] = max(ans[cnt], node.val)

            if node.left:
                dfs(node.left, cnt + 1)
            if node.right:
                dfs(node.right, cnt + 1)
        dfs(root, 0)
        return ans
