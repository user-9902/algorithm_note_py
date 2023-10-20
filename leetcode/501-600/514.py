"""
514. 自由之路
dp
本题局部最优解并不是全局最优解 如 从 abccccdbe 找 abd
个人感觉，挺抽象的一道题
"""

from math import inf


class Solution:
    def findRotateSteps2(self, ring: str, key: str) -> int:
        """
        hash map
        ❌ dadr rda 该例子无法解决
        """
        n = len(ring)
        r_map = [{} for i in range(n)]
        for i in range(n):
            for j, w in enumerate(ring):
                if w not in r_map[i] or abs(i - r_map[i][w]) > abs(i - j) or abs(i - r_map[i][w]) > abs(n - abs(i - j)):
                    r_map[i][w] = j

        ans = 0
        cur = 0
        for s in key:
            tmp = r_map[cur][s]
            ans += min(abs(tmp - cur), abs(n - abs(tmp - cur))) + 1
            cur = tmp
        return ans

    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        dp[i][j] = dp[i - 1][j]
        """
        s_map = {}
        for i, v in enumerate(ring):
            if v in s_map:
                s_map[v].append(i)
            else:
                s_map[v] = [i]

        n = len(ring)
        m = len(key)
        f = [[inf] * n for _ in range(m)]

        for i, v in enumerate(key):
            for j in s_map[v]:
                if i == 0:
                    f[i][j] = f[i][j] = min(j, abs(n-j))
                else:
                    for k in s_map[key[i-1]]:
                        f[i][j] = min(f[i][j], f[i-1][k] +
                                      min(abs(j-k), abs(n-abs(j-k))))

        return min(f[-1]) + m
