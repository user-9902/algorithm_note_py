"""
二叉平衡树
同一个int list可以用多个二叉排序树表示
为了使得排序树深度尽可能小（深度小，操作效率高）
我们定义：二叉树的每个节点的左子树和右子树的差至多为1时，我们称这样的树为二叉平衡树（AVLtree）
这使得我们在插入数据时候需要注意满足AVLtree的定义

相较于二叉排序树，二叉平衡树用更多的插入的时间，换来了读取操作时更高的效率
"""
from typing import Optional

DIRECT_MAP = ('left', 'right')


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.height = 1
        self.left = None
        self.right = None

    def get_balance_factor(self) -> int:
        l = 0 if self.left is None else self.left.height
        r = 0 if self.right is None else self.right.height
        return l - r

    def set_height(self):
        l_height = 0 if self.left is None else self.left.height
        r_height = 0 if self.right is None else self.right.height
        self.height = max(l_height, r_height) + 1

    def __str__(self):
        return '%s' % self.val


def r_rotate(node: TreeNode):
    # 守卫
    defend1 = node.left
    defend2 = node.left.right

    # 调整指向
    node.left.right = node
    node.left = defend2

    # 维护高度
    node.set_height()
    defend1.set_height()

    return defend1


def l_rotate(node: TreeNode):
    # 守卫
    defend1 = node.right
    defend2 = node.right.left

    # 调整指向
    node.right.left = node
    node.right = defend2

    # 维护高度
    node.set_height()
    defend1.set_height()

    return defend1


class AVLTree:
    def __init__(self, val: Optional[int]):
        self.root = None if val is None else TreeNode(val)

    def search_node(self, val: int):
        def dfs(node):
            if node is None:
                return False
            if node.val == val:
                return True
            elif val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(self.root)

    def insert_node(self, val: int):
        # 插入存在的值
        if self.search_node(val):
            return False
        # 空树
        if self.root is None:
            self.root = TreeNode(val)
            return True

        path = []   # 路径
        direct = []  # 方向
        change_height = False  # 高度是否发生变化

        def dfs(node, val):
            nonlocal change_height
            path.append(node)

            if val < node.val:
                direct.append(0)
                if node.left is None:
                    node.left = TreeNode(val)
                    if node.right is None:
                        change_height = True
                else:
                    dfs(node.left, val)
            else:
                direct.append(1)
                if node.right is None:
                    node.right = TreeNode(val)
                    if node.left is None:
                        change_height = True
                else:
                    dfs(node.right, val)
        # 插入节点
        dfs(self.root, val)

        # 高度发生变化的时候，可能需要旋转
        if change_height:
            # 维护高度
            for i in path:
                i.height += 1

            n = len(path)
            for i in range(n-1, -1, -1):
                n = path[i]
                equal_factor = n.get_balance_factor()

                # 需要旋转
                if abs(equal_factor) > 1:
                    # four cases
                    if direct[i] == 1 and direct[i+1] == 1:
                        r = l_rotate(n)
                    if direct[i] == 0 and direct[i+1] == 0:
                        r = r_rotate(n)
                    if direct[i] == 0 and direct[i+1] == 1:
                        n.left = l_rotate(path[i+1])
                        r = r_rotate(n)
                    if direct[i] == 1 and direct[i+1] == 0:
                        n.right = r_rotate(path[i+1])
                        r = l_rotate(n)
                    # 旋转后的节点挂到父节点上
                    if i == 0:
                        self.root = r
                    else:
                        if direct[i - 1] == 0:
                            path[i-1].left = r
                        else:
                            path[i-1].right = r

        return True

    def delete_node(self, val: int):
        path = []
        direct = []

        def dfs(node, val):
            if node is None:
                return None
            if node.val == val:
                return node
            elif val < node.val:
                direct.append(0)
                path.append(node)
                return dfs(node.left, val)
            else:
                direct.append(1)
                path.append(node)
                return dfs(node.right, val)

        node = dfs(self.root, val)
        # 不存在需删除的节点
        if node is None:
            return False

        for i in path:
            print(i)
        for i in direct:
            print(i)

        if node.left is None and node.right is None:
            return

    def print_tree(self):
        def p(node, level=0):
            if node is not None:
                p(node.right, level + 1)
                print(' ' * 4 * level + '->', node.val)
                p(node.left, level + 1)

        p(self.root)


tree = AVLTree(2)
tree.insert_node(1)
tree.insert_node(0)
tree.insert_node(3)
tree.insert_node(4)
tree.print_tree()
tree.delete_node(4)

a = '123'
a += '123'
