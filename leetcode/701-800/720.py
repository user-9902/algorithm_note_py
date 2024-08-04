"""
@title:      720. 词典中最长的单词
@difficulty: 中等
@importance: 4/5
@tags:       字典树Trie
"""

from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_text_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, string):
        cur = self.root
        for c in string:
            cur = cur.children[c]
        cur.is_text_end = True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
        @tags:              字典树
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       根据题目的描述，前缀+字典查找，我们可以联想到字典树
        """
        trie = Trie()
        words.sort()
        res = ''

        for word in words:
            if trie.startsWith(word[:-1]):
                if len(word) > len(res):
                    res = word
                trie.insert(word)

        return res

    def longestWord(self, words: List[str]) -> str:
        """
        @tags:              sort hashmap
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       思路同上，存储的结构换成了hashset
        """
        words.sort()
        s = set([""])
        res = ""

        for word in words:
            if word[:-1] in s:
                s.add(word)
                if len(word) > len(res):
                    res = word
        return res
