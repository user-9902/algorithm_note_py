"""
@title:      987. 二叉树的垂序遍历
@difficulty: 中等
@importance: 4/5
@tags:       bfs sort
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        @tags:              bfs sort
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       统计所有节点的行列数据,然后排序,排序优先级为 col > row > val
        """
        arr = []
        # bfs
        queue = [[root, 0, 0]]
        while queue:
            [n, weight, level] = queue.pop(0)
            arr.append([weight, n.val, level])
            if n.left:
                queue.append([n.left, weight - 1, level + 1])
            if n.right:
                queue.append([n.right, weight + 1, level + 1])
        arr.sort(key=lambda x: (x[0], x[2], x[1]))

        ans = []
        l = 0
        for i, v in enumerate(arr):
            if v[0] > arr[l][0]:
                ans.append([arr[j][1] for j in range(l, i)])
                l = i
        ans.append([arr[j][1] for j in range(l, len(arr))])
        return ans
