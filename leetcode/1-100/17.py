"""
17. 电话号码的字母组合
string 回溯
每轮维护一个数组的内存开销太大了，这里用回溯实现。
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        NUM_MAP = (None, None, ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
                   'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z'])

        n = len(digits)
        # special case
        if n == 0:
            return []

        ans = []
        cur = ''

        def dfs(index=0):
            nonlocal cur
            if index == n:
                ans.append(cur)
                return
            m = NUM_MAP[int(digits[index])]

            for i in m:
                cur += i
                dfs(index+1)
                cur = cur[:-1]

        dfs()

        return ans
