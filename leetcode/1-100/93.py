"""
@title:      93. 复原 IP 地址
@difficulty: 中等
@importance: 3/5
@tags:       回溯
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        @tags:              回溯 dfs
        @time complexity:   O(27)
        @space complexity:  O(n)
        @description:       遍历三个分割点
        """
        ans = []
        cur = []

        def dfs(s, idx):
            if idx == 3:
                if len(s) > 1 and s[0] == '0':
                    return
                if 0 <= int(s) <= 255:
                    cur.append(s)
                    ans.append(".".join(cur))
                    cur.pop()
                return

            for i in range(1, len(s)):
                str = s[:i]
                if len(str) > 1 and str[0] == '0':
                    continue
                if 0 <= int(str) <= 255:
                    cur.append(str)
                    dfs(s[i:], idx + 1)
                    cur.pop()

        dfs(s, 0)
        return ans
