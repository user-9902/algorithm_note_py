"""
127. 单词接龙
同126题
能否从图中一点到另一点
bfs遍历(可进阶为双向bfs)，防止回路出现即可
"""
from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        
        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)
        
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        先生成edges内存开销太大
        """
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        b_i = wordList.index(beginWord)
        e_i = wordList.index(endWord)

        n = len(wordList)
        m = len(wordList[0])

        # 获取边的信息
        edges = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        if cnt > 2:
                            break
                        cnt += 1
                if cnt == 1:
                    edges[i].append(j)
                    edges[j].append(i)

        level = 1
        queue = [b_i]
        record = [False] * n
        l = 0
        r = 1
        while l < r:
            r = len(queue)
            for x in range(l, r):
                record[queue[x]] = True
                l += 1
                for y in edges[queue[x]]:
                    if record[y]:
                        continue
                    else:
                        record[y] = True
                    if y == e_i:
                        return level + 1
                    else:
                        queue.append(y)
            level += 1

        return 0


res = Solution().ladderLength("hot", "dog", ["hot", "dog"])
print(res)
