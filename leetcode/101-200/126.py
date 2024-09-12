"""
@title:      126. 单词接龙 II
@difficulty: 中等
@importance: 5/5
@tags:       最短路径

为相差一个字符的单词建立联系，构建无向图
"""

from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.parents = []

    def append_parent(self, node):
        self.parents.append(node)


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        @tags:              建图 bfs
        @time complexity:   O()
        @space complexity:  O()
        """
        if beginWord not in wordList:
            wordList.append(beginWord)
            fromIdx = len(wordList) - 1
        else:
            fromIdx = wordList.index(beginWord)

        # 无终点
        if endWord not in wordList:
            return []
        toIdx = wordList.index(endWord)

        def check(w1, w2):
            m = len(w1)
            cnt = 0
            for k in range(m):
                if w1[k] != w2[k]:
                    cnt += 1
            return cnt <= 1

        # 建图 邻接表
        n = len(wordList)
        f = [[] for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                if check(wordList[i], wordList[j]):
                    f[i].append(j)
                    f[j].append(i)
        # 起点 终点无边
        if len(f[fromIdx]) == 0 or len(f[toIdx]) == 0:
            return []

        # 防止同层重复
        visited = [False] * n
        # 防止子重复
        added = [False] * n
        # bfs 正向寻找终点，反向建立多叉树
        nodes = [Node(word) for word in wordList]
        que = [fromIdx]
        _idx = 0
        while que:
            l = len(que)
            if _idx == l:
                break
            # 当该层找到结果时就不用继续遍历了
            flag = False
            # 防止同层的环
            for i in range(_idx, l):
                visited[que[i]] = True
            # 添加下一层
            for i in range(_idx, l):
                # 父节点 优化 pop
                cur = que[i]
                for k in f[cur]:
                    if visited[k]:
                        continue
                    nodes[k].append_parent(nodes[cur])
                    # 子节点存储 parents
                    if not added[k]:
                        que.append(k)
                        added[k] = True
                    if k == toIdx:
                        flag = True
            _idx = l
            if flag:
                break
        # 生成结果
        res = []
        path = []

        def dfs(node: Node):
            path.append(node.val)
            if node.parents:
                for n in node.parents:
                    dfs(n)
            elif node.val == beginWord:
                res.append(path[::-1])
            path.pop()
        dfs(nodes[toIdx])
        return res


test2 = ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
Solution().findLadders(*test2)
