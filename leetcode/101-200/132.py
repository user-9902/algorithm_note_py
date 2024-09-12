"""
@title:      132. 分割回文串 II
@difficulty: 中等
@importance: 5/5
@tags:       dp
"""
from math import inf


class Solution:
    def minCut(self, s: str) -> int:
        """
        @tags:              dp 回溯
        @time complexity:   O(n^2)
        @space complexity:  O(n^2)
        @description:       区间dp，预处理同 leetcode 131
                            f[i] 表示 s[:i] 的最小切割次数
                                若 s[:i] 是回文串，不用分割：f[i] = 0

                                若 s[:i] 不是回文串：则切割 s[:i] 为 s[:j] 和 s[j+1:i] (0<j<i)
                                    s[:j] 便是同样的子问题了，分析 s[j+1:i] 即可：
                                        s[j+1:i] 是回文串 f[i] = f[:j] + 1
                                        s[j+1:i] 不是回文串 则当前分割方案不行。
        """
        n = len(s)
        # dp [l, r) 方便下面的回文串判断
        f = [[""] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if j - i == 1:
                    f[i][j] = True
                elif j - i == 2 and s[i] == s[j - 1]:
                    f[i][j] = True
                elif s[i] == s[j - 1] and f[i + 1][j - 1]:
                    f[i][j] = True
        if f[0][n]:
            return 0

        # [l, r)
        dp = [inf] * (n + 1)
        for r in range(1, n + 1):
            if f[0][r]:
                dp[r] = 0
            else:
                for l in range(1, r):
                    if f[l][r]:
                        dp[r] = min(dp[r], dp[l] + 1)

        return dp[n]


Solution().minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece")
