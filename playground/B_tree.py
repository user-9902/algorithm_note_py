"""


参考：《大话数据结构》
"""

from typing import Optional

DEFAULT_ORDER = 4  # 默认节点的最大子节点数


class TreeNode:
    def __init__(self, val=None):
        self.vals = []
        self.childs = []

        if val is not None:
            self.insert(val)

    def __str__(self):
        return '%s' % self.vals

    def insert(self, nval: int, l=None, r=None):
        if not self.vals:
            self.vals.append(nval)
            self.childs.append(None)
            self.childs.append(None)
            return

        index = len(self.vals)
        for i, v in enumerate(self.vals):
            if nval < v:
                index = i
                break

        self.vals.insert(index, nval)
        self.childs.insert(index, None)
        self.childs[index] = l
        self.childs[index+1] = r

    def cut(self, mid):
        # 上溢操作需要切割node
        l = TreeNode()
        l.vals = self.vals[:mid]
        l.childs = self.childs[:mid+1]

        r = TreeNode()
        r.vals = self.vals[mid+1:]
        r.childs = self.childs[mid+1:]

        return l, r


class Btree:
    def __init__(self,  order: int = DEFAULT_ORDER, val: Optional[int] = None):
        self.root = TreeNode(val)
        self.order = order
        self.mid_index = (order - 1) // 2

    def insert(self, nval: int) -> bool:

        path = []

        def dfs(node: TreeNode, nval: int):
            if node is None:
                return
            path.append(node)
            if node.childs:
                for i, v in enumerate(node.vals):
                    if nval < v:
                        dfs(node.childs[i], nval)
                        return
                dfs(node.childs[-1], nval)
        dfs(self.root, nval)

        n = len(path)

        left = None
        right = None
        l, r = None, None
        for i in range(n-1, -1, -1):
            node = path[i]
            # 直接插入操作
            if len(node.childs) < self.order:
                node.insert(nval, left, right)
                left = None
                right = None
                break
            # 需要上溢的操作
            else:
                mid_v = node.vals[self.mid_index]

                left, right = node.cut(self.mid_index)
                if nval < mid_v:
                    left.insert(nval, l, r)
                else:
                    right.insert(nval, l, r)
                nval = mid_v
                l = left
                r = right

        if left and right:
            nroot = TreeNode(nval)
            nroot.childs[0], nroot.childs[1] = left, right
            self.root = nroot

    def print_tree(self):
        def p(node: TreeNode, level=0):
            if node is not None:
                n = len(node.childs)
                for i in range(n-1, -1, -1):
                    if i < n - 1:
                        print(' ' * 4 * level + '->', node.vals[i])
                    p(node.childs[i], level + 1)

        p(self.root)
        print('------------------------------')


tree = Btree(val=0)
for i in range(1, 25):
    tree.insert(i)

tree.print_tree()
