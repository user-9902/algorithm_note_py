from typing import List


class Node:
    def __init__(self, val=None):
        self.val = val
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self, val=None):
        self.root = Node(val)

    @classmethod
    def preOrderTraverse(cls, node: Node):
        """
        先序遍历
        """
        if node:
            print(node.val)
            cls.preOrderTraverse(node.lchild)
            cls.preOrderTraverse(node.rchild)

    @classmethod
    def inOrderTraverse(cls, node: Node):
        """
        中序遍历
        """
        if node:
            cls.inOrderTraverse(node.lchild)
            print(node.val)
            cls.inOrderTraverse(node.rchild)

    @classmethod
    def postOrderTraverse(cls, node: Node):
        """
        后续遍历
        """
        if node:
            cls.postOrderTraverse(node.lchild)
            cls.postOrderTraverse(node.rchild)
            print(node.val)

    @classmethod
    def bfsTraverse(cls, node: Node):
        """
        广度优先遍历
        """
        # 利用队列实现
        queue = [node]
        while queue:
            n = queue[0]
            del queue[0]

            if n is None:
                continue
            print(n.val)
            if n.lchild or n.rchild:
                queue.append(n.lchild)
                queue.append(n.rchild)

    @classmethod
    def createBinaryTree(cls, vals: List[str]):
        tree = cls()
        if len(vals) == 0:
            return tree

        def preOrder(rest):
            if len(rest) == 0:
                return

            v = rest.pop(0)
            if v != '#':
                n = Node(v)
                n.lchild = preOrder(rest)
                n.rchild = preOrder(rest)
                return n

        tree.root = preOrder(vals)
        return tree


tree = BinaryTree.createBinaryTree(
    ['A', 'B', 'C', "#", '#', 'D', '#', '#', 'E', '#', '#'])
