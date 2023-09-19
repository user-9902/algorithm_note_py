"""
140. 单词拆分 II
dfs
这里还可以记忆化搜索优化
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 记录下跨度，无需一个一个字符的遍历
        step = {}
        for i in wordDict:
            step[len(i)] = True
        step = step.keys()

        res = []
        r = []

        def dfs(s):
            for i in step:
                if s[0:i] in wordDict:
                    r.append(s[0:i])
                    dfs(s[i:])
                    if s[i:] == '' and len(s) == i:
                        res.append(" ".join(r))
                    # 回溯
                    r.pop()
        dfs(s)
        return res


Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
