"""
二叉平衡树
同一个int list可以用多个二叉排序树表示
为了使得排序树深度尽可能小（深度小，操作效率高）
我们定义：二叉树的每个节点的左子树和右子树的差至多为1时，我们称这样的树为二叉平衡树（AVLtree）
这使得我们在插入数据时候需要注意满足AVLtree的定义

相较于二叉排序树，二叉平衡树用更多的插入的时间，换来了读取操作时更高的效率
"""
from typing import Optional, List

DIRECT_MAP = ('left', 'right')


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.height = 1
        self.left = None
        self.right = None

    def get_balance_factor(self) -> int:
        """
        获取当前节点平衡因子
        """
        l = 0 if self.left is None else self.left.height
        r = 0 if self.right is None else self.right.height
        return l - r

    def set_height(self):
        """
        设置当前节点高度
        """
        l_height = 0 if self.left is None else self.left.height
        r_height = 0 if self.right is None else self.right.height
        self.height = max(l_height, r_height) + 1

    def __str__(self):
        return '%s' % self.val


def r_rotate(node: TreeNode):
    """
    右旋方法
    """
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
    """
    左旋方法
    """
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


def rotate_unit(node: TreeNode) -> TreeNode:
    """
    通用旋转方法
    """
    # 重置高度
    node.set_height()
    # 获取平很因子
    direct_parent = node.get_balance_factor()
    # 无需旋转
    if abs(direct_parent) < 2:
        return node

    direct_child = node.left.get_balance_factor() \
        if direct_parent > 0 else node.right.get_balance_factor()
    # 4 cases
    if direct_parent > 0:
        # ll型
        if direct_child >= 0:
            node = r_rotate(node)
        # lr型
        else:
            node.left = l_rotate(node.left)
            node = r_rotate(node)
    else:
        # rr型
        if direct_child <= 0:
            node = l_rotate(node)
        # rl型
        else:
            node.right = r_rotate(node.right)
            node = l_rotate(node)

    return node


def rotate_by_path(path: List[TreeNode]) -> TreeNode:
    n = len(path)

    for i in range(n-1, -1, -1):
        node = rotate_unit(path[i])
        if i == 0:
            return node
        else:
            if path[i - 1].left == path[i]:
                path[i-1].left = node
            else:
                path[i-1].right = node
    return node


class AVLTree:
    def __init__(self, val: Optional[int]):
        self.root = None if val is None else TreeNode(val)

    def search_node(self, val: int) -> bool:
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

    def insert_node(self, val: int) -> bool:
        # 插入存在的值
        if self.search_node(val):
            return False
        # 空树
        if self.root is None:
            self.root = TreeNode(val)
            return True

        path = []   # 路径

        def dfs(node, val):
            path.append(node)

            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    dfs(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right, val)
        # 插入节点
        dfs(self.root, val)

        # 沿着路径调整平衡
        self.root = rotate_by_path(path)

        return True

    def delete_node(self, val: int, _node=None) -> bool:
        path = []

        def dfs(node, val):
            if node is None:
                return None
            if node.val == val:
                return node
            elif val < node.val:
                path.append(node)
                return dfs(node.left, val)
            else:
                path.append(node)
                return dfs(node.right, val)

        node = dfs(_node or self.root, val)

        # 不存在需删除的节点
        if node is None:
            return False

        parent = path[-1] if path else None
        n = len(path)

        # 删除节点无child
        if node.left is None and node.right is None:
            if n == 0:
                self.root = None
                return True
            # 删除节点
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            # 沿着路径调整平衡
            root = rotate_by_path(path)
            if _node is None:
                self.root = root

        # 删除节点有两个child
        elif node.left and node.right:
            # 用后继节点代替当前节点，
            # 后继节点最多只有一个右子节点，删除时可以递归调用dele_node
            successor_node = node.right
            while successor_node.left:
                successor_node = successor_node.left

            self.delete_node(successor_node.val, node)
            node.val = successor_node.val

        # 删除节点有一个child
        else:
            if n == 0:
                self.root = node.left or node.right
                return True
            # 用child代替删除节点
            if parent.left == node:
                parent.left = node.left or node.right
            else:
                parent.right = node.left or node.right
            node.left = node.right = None
            # 沿着路径调整平衡
            root = rotate_by_path(path)
            if _node is None:
                self.root = root

        return True

    def print_tree(self):
        def p(node, level=0):
            if node is not None:
                p(node.right, level + 1)
                print(' ' * 4 * level + '->', node.val)
                p(node.left, level + 1)

        p(self.root)
        print('------------------------------')


tree = AVLTree(2)
tree.insert_node(1)
tree.insert_node(0)
tree.insert_node(3)
tree.insert_node(4)
tree.insert_node(5)
tree.delete_node(3)
tree.print_tree()
