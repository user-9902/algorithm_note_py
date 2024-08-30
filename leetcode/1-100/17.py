"""
@title:      17. 电话号码的字母组合
@difficulty: 简单
@importance: 4/5
@tags:       回溯
"""

from typing import List

NUM_MAP = (None, None, "abc", "def", "ghi",
           "jkl", "mno", "pqrs", "tuv", "wxyz")


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        @tags:              回溯 dfs
        @time complexity:   O(n4^n)
        @space complexity:  O(n)
        @description:       枚举所有每一位上字符串的所有可能
        """
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [""] * n

        def dfs(idx):
            # 终止遍历
            if idx == n:
                ans.append("".join(path))
                return

            # 遍历所有可能
            for c in NUM_MAP[int(digits[idx])]:
                # 会覆盖 深度遍历后无需恢复现场
                path[idx] = c
                dfs(idx + 1)

        dfs(0)
        return ans
