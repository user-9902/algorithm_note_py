
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp
        参考 leetcode 题解
        动态规划最关键的是能分析出 状态转移方程
        dp[i][j] 表示  s[:i]中包含的t[:j]的子串的个数

        case s[i] == t[j]: dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        case s[i] != t[j]: dp[i][j] = dp[i-1][j]

        dp[i-1][j] s[i] != t[j] 说明s[i]的加入不影响结果
        dp[i-1][j-1] s[i] == t[j]  s: bag | g  t: b | g 说明g的加入能延续 s: bag  t: b 的结果
        """
        s_len = len(s)
        t_len = len(t)

        # special case
        if s_len < t_len:
            return 0
        if s_len == t_len:
            return 1 if s == t else 0

        dp = [[0]*(s_len+1) for i in range(t_len+1)]

        # 初始化数据
        for _ in range(t_len+1):
            dp[_][0] = 0
        for _ in range(s_len+1):
            dp[0][_] = 1

        for j in range(1, t_len+1):
            for i in range(1, s_len+1):
                dp[j][i] = dp[j][i-1]
                if s[i - 1] == t[j - 1]:
                    dp[j][i] += dp[j-1][i-1]

        return dp[t_len][s_len]

    def numDistinct2(self, s: str, t: str) -> int:
        """
        笛卡尔积
        算出笛卡尔积后，计算单调性即可
        本人的解法，算法没错，但是复杂度指数级，直接炸掉😅
        """
        s_map = {}
        for i, c in enumerate(s):
            if c in t:
                if c in s_map:
                    s_map[c].append(i)
                else:
                    s_map[c] = [i]

        if not s_map:
            return 0

        s_cou = []
        for i in t:
            s_cou.append(s_map[i])

        def cartesian_product(*iterables):
            # 笛卡尔积的计算公式
            if not iterables:
                return [[]]
            return [[x] + p for x in iterables[0] for p in cartesian_product(*iterables[1:])]

        map = cartesian_product(*s_cou)
        res = 0

        # 遍历所有解，单调递增的记入结果
        for x in range(len(map)):
            for y in range(len(map[0])):
                if y > 0 and map[x][y] <= map[x][y - 1]:
                    break
                elif y == len(map[0]) - 1:
                    res += 1
        return res
