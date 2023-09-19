"""
87. 扰乱字符串
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        dp
        将s1至s2的转换变为规模更小的子问题
        """
        n = len(s1)
        dp = [[[False for _ in range(n + 1)] for _ in range(n + 1)]
              for _ in range(n + 1)]

        for k in range(1, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    if k == 1:
                        # 长度为1的时候直接判断
                        dp[i][j][k] = s1[i] == s2[j]
                    else:
                        # w 为旋转点
                        for w in range(1, k):
                            # s1 | s2 ——> s1 | s2 旋转点同侧的字符串，是否为scramble
                            case1 = dp[i][j][w] and dp[i+w][j+w][k - w]
                            # s1 | s2 ——> s2 | s1 旋转点对角侧的字符串，是否为scramble
                            case2 = dp[i][j + k - w][w] and dp[i+w][j][k - w]
                            if case1 or case2:
                                dp[i][j][k] = True
        return dp[0][0][n]

    def _isSame(self, s1: str, s2: str) -> bool:
        map = {}
        for i in s1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        for i in s2:
            if i in map:
                map[i] -= 1
            else:
                return False

        return all(i == 0 for i in map.values())

    # def isScramble(self, s1: str, s2: str) -> bool:
    #     """
    #     dfs 递归
    #     时间复杂度会炸掉
    #     """
    #     s1_len = len(s1)
    #     s2_len = len(s2)

    #     if s1 == s2:
    #         return True

    #     if s1_len != s2_len:
    #         return False

    #     if self._isSame(s1, s2):
    #         for i in range(1, s1_len):
    #             if (self.isScramble(s1[0:i], s2[s1_len-i:s1_len]) and self.isScramble(s1[i:s1_len], s2[0: s1_len-i])) \
    #                     or (self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i: s1_len], s2[i: s1_len])):
    #                 return True

    #     return False


Solution().isScramble('great', 'rgeat')
