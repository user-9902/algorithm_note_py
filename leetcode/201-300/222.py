"""
222. 完全二叉树的节点个数
dfs; binary search
朴素的解法没啥意思，可以获取层高，然后二分查找最后一层的最后一个元素
       1
    2     3
  4   5 6   7
 8 9
如查找节点10是否存在（这里是不存在的），就需要知道如何从根节点遍历至节点10
根据父元素  10 // 2 = 5; 5 // 2 = 2; 2 // 2 = 1
获取路径方向 2 % 2 == 0左; 5 % 2 = 1右; 10 % 2 = 0 左
"""
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        dfs
        """
        if root is None:
            return 0

        height = 0

        def dfs(node):
            if node is None:
                return

            nonlocal height
            height += 1

            if node.left:
                dfs(node.left)
        dfs(root)

        # 二分查找最底层
        def exist(num: int) -> bool:
            arr = []
            while num != 1:
                arr.append(num % 2)
                num //= 2
            node = root
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == 0:
                    node = node.left
                else:
                    node = node.right
            return node is not None

        left = 2 ** (height - 1)
        right = 2 ** height - 1
        while left <= right:
            mid = (left+right) // 2
            if exist(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1


Solution().countNodes(None)
