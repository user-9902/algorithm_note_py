"""
968. 监控二叉树
dfs
分别考虑当前节点被监控的情况时，花费的摄像头
被当前节点监控，被父节点监控，被子节点监控
变形题：
    最少花费，即每个节点的花费不同，求最小花费
"""


from typing import Optional
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        分类讨论当前节点被监控时花费了多少摄像头
        当前节点 cur： min(l_cur, l_parent, l_child) + min(r_cur, r_parent, r_child) + 1
        父节点 parent：min(l_cur, l_child) + min(r_cur, r_child)
        子节点 child：min(l_cur+r_child, l_child + r_cur, l_cur + r_cur)
        """

        def dfs(node):
            if node is None:
                return inf, 0, 0

            l_cur, l_par, l_chi = dfs(node.left)
            r_cur, r_par, r_chi = dfs(node.right)

            cur = min(l_cur, l_par, l_chi) + min(r_cur, r_par, r_chi) + 1
            par = min(l_cur, l_chi) + min(r_cur, r_chi)
            chi = min(l_cur + r_chi, r_cur + l_chi, l_cur + r_cur)

            return cur, par, chi

        cu, _, ch = dfs(root)
        return min(cu, ch)
