"""
@title:      208. 实现 Trie (前缀树)
@difficulty: 中等
@importance: 5/5
@tags:       字典树Trie
"""

"""
前缀树也称谓字典树，用于高效的存储和检索字符串。
[a, ab, ac, ad, abd, acc]
        a
    ab      ac      ab
 abd       acc
 
字典树有以下特性：
    快速查找: O(len(s)) 的时间复杂度
    节省空间：通过公共前缀节省存储空间

字典树有以下应用：
    自动补全：根据用户的输入，提示补全内容。
    词频统计：某字符串出现的次数
    路由查找：文件系统中，ip路由系统中的路由表常使用字典树来组织，以提高查找效率。
"""




from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False


class Trie:
    """
    @tags:              字典树数据结构
    @time complexity:   O(len(n))
    @space complexity:  O(n)
    @description:       💲字典树数据结构的实现
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            cur = cur.children.get(c)
            if cur is None:
                return False
        return cur.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return True

    def delete(self, word: str) -> bool:
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            # 不存在 word
            if cur == None:
                return False

        res = cur.is_end_of_word
        cur.is_end_of_word = False
        if len(cur.children) == 0:
            del cur.children

        return res


node = TrieNode()
print(node.children['a'])
print(node.children)
