"""
@title:      60. 排列序列
@difficulty: 中等
@importance: 5/5
@tags:       dfs bfs
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        @tags:              dfs
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       遍历所有可能直至第k个
        """
        f = "".join([str(i + 1) for i in range(n)])
        res = None
        cur = ""
        cnt = 0

        def dfs(f):
            nonlocal res, cnt, cur
            if f == "":
                cnt += 1
                if cnt == k:
                    res = cur
                return
            if res:
                return
            for i, v in enumerate(f):
                cur += v
                dfs(f[:i] + f[i + 1:])
                cur = cur[:-1]

        dfs(f)
        return res

    def getPermutation(self, n: int, k: int) -> str:
        """
        @tags:              bfs
        @time complexity:   O(logn)
        @space complexity:  O(1)
        @description:       观察bfs树，我们发现每个节点的子节点个数是确定的，这样就能利用bfs直接找到答案了
        """
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i - 1] * (i + 1)
        res = [str(i + 1) for i in range(n)]
        ans = ""
        i = n - 2
        k = k - 1
        while k and res:
            ans += res[k // f[i]]
            res.pop(k // f[i])
            k %= f[i]
            i -= 1

        return ans + "".join(res)
