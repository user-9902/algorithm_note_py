"""
72. 编辑距离
word1 -> word2 等价于 word2 -> word1
问题转化将word1和word2转化为相同字符的最小操作数
对word1的插入，删除，替换
等价于word1插入，word2插入，word1或word2替换
dp[i][j] 表示为 word1第i位之前的字符，转为word2第j位之前的字符所需的最小操作步骤

word[i] = word[j]: dp[i][j] = dp[i-1][j-1]
word[i] != word[j]: dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1 = len(word1)
        len_2 = len(word2)

        dp = []
        for i in range(len_1 + 1):
            dp.append([i] + [0]*len_2)
        for j in range(len_2 + 1):
            dp[0][j] = j
        for x in range(1, len_1+1):
            for y in range(1, len_2+1):
                # 当前位置的字符相同，则无需操作，最小操作不步速即为dp[i - 1][j - 1]
                if  word1[x - 1] == word2[y - 1]: 
                    dp[x][y] = dp[x -1 ][y-1]
                else:
                    # 否则最小步长为 dp[i-1][j]：word1 添加一个元素 dp[i][j-1] word2 添加一个元素 或者替换实现
                    dp[x][y] = min(dp[x][y-1], dp[x-1][y], dp[x-1][y-1]) + 1
        return dp[len_1][len_2]



Solution().minDistance('intention', 'execution')
