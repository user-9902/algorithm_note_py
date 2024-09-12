"""
@title:      131. 分割回文串
@difficulty: 中等
@importance: 5/5
@tags:       dp 回溯
"""


class Solution:
    def minCut(self, s: str) -> int:
        """
        @tags:              dp 回溯
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       区间dp 方便判断[l, r)是否是回文串。回溯生成结果
        """
        n = len(s)
        # dp [l, r) 方便下面的回文串判断
        f = [[""] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if j - i == 1:
                    f[i][j] = s[i:j]
                elif j - i == 2 and s[i] == s[j - 1]:
                    f[i][j] = s[i:j]
                elif s[i] == s[j - 1] and f[i + 1][j - 1]:
                    f[i][j] = s[i:j]
        ans = []
        path = []

        def dfs(l):
            if l == n:
                return ans.append(path.copy())
            for r in range(l + 1, n + 1):
                if f[l][r]:
                    path.append(f[l][r])
                    dfs(r)
                    path.pop()
        dfs(0)
        return ans
