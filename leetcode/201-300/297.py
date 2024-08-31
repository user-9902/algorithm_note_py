"""
@title:      297. 二叉树的序列化与反序列化
@difficulty: 中等
@importance: 5/5
@tags:       bfs
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    @tags:              bfs
    @time complexity:   O(n)
    @space complexity:  O(n)
    @description:       bfs序列化 反序列化💲leetcode上输入 arr -> tree 就需要类似的反序列化方法
    """

    def serialize(self, root):
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            for _ in range(n):
                cur = queue.pop(0)
                if cur is None:
                    res.append('n')
                    continue
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
        return ';'.join(res)

    def deserialize(self, data):
        arr = data.split(';')
        n = len(arr)
        root = None if arr[0] == 'n' else TreeNode(int(arr[0]))
        if n == 1:
            return root

        queue = [root]
        idx = 1
        while queue and idx < n:
            cur = queue.pop(0)
            if arr[idx] != 'n':
                cur.left = TreeNode(int(arr[idx]))
                queue.append(cur.left)
            idx += 1

            if arr[idx] != 'n':
                cur.right = TreeNode(int(arr[idx]))
                queue.append(cur.right)
            idx += 1
        return root


Codec().deserialize('1;2;3;n;n;4;5')
