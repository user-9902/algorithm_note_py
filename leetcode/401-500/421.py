"""
@title:      421. 数组中两个数的最大异或值
@difficulty: 中等
@importance: 5/5
@tags:       字典树
"""

from typing import List


class TrieNode:
    def __init__(self):
        # 0
        self.left = None
        # 1
        self.right = None


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        @tags:              字典树
        @time complexity:   O(32n)
        @space complexity:  O(32n)
        @description:       字典树 dfs
        """
        maax = max(nums)
        h = maax.bit_length()
        root = TrieNode()
        for num in nums:
            m = h
            cur = root
            while m:
                v = num & (1 << (m - 1))
                if v:
                    if cur.right is None:
                        cur.right = TrieNode()
                    cur = cur.right
                else:
                    if cur.left is None:
                        cur.left = TrieNode()
                    cur = cur.left
                m -= 1

        # 我们要寻找两个数。要使得两个数异或和尽可能大，在同层时，尽可能 一个数选 0 一个数选 1
        def dfs(node1: TrieNode, node2: TrieNode, h):
            if h == -1:
                return 0
            res = 0
            if node1.left and node2.right:
                res = (1 << h) + dfs(node1.left, node2.right, h - 1)
            if node1.right and node2.left:
                a = (1 << h) + dfs(node1.right, node2.left, h - 1)
                if a > res:
                    res = a
            if res == 0:
                if node1.left and node2.left:
                    res = dfs(node1.left, node2.left, h - 1)
                if node1.right and node2.right:
                    res = dfs(node1.right, node2.right, h - 1)
            return res

        return dfs(root, root, h - 1)

    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        @tags:              字典树
        @time complexity:   O(32n)
        @space complexity:  O(32n)
        @description:       该解法 search 的过程与上方不同，这里是枚举
        """
        maax = max(nums)
        h = maax.bit_length()
        root = TrieNode()
        for num in nums:
            m = h
            cur = root
            while m:
                v = num & (1 << (m - 1))
                if v:
                    if cur.right is None:
                        cur.right = TrieNode()
                    cur = cur.right
                else:
                    if cur.left is None:
                        cur.left = TrieNode()
                    cur = cur.left
                m -= 1

        res = 0
        f = (1 << h) - 1
        for num in nums:
            # 寻找类似target的数
            target = f ^ num
            r = 0
            m = h
            cur = root
            while m:
                v = target & (1 << (m - 1))
                if v:
                    if cur.right:
                        cur = cur.right
                        r |= v
                    else:
                        cur = cur.left
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur = cur.right
                        r |= (1 << (m - 1))
                m -= 1
            if num ^ r > res:
                res = num ^ r
            # 剪枝
            if res == f:
                break
        return res
