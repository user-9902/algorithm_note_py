"""
22. 括号生成
bfs; 回溯
每一步可以添加左括号或右括号，同时添加的右括号数量不能超过左括号数量
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = '('
        max_r = n
        max_l = n+1

        def bfs(r=1, l=0):
            nonlocal cur
            # 每一步可以添加左括号或右括号
            if r == max_r and l == max_r:
                ans.append(cur)
                return
            if r < max_r:
                cur += '('
                bfs(r+1, l)
                cur = cur[:-1]
            # 限制条件 未加入左括号的时候不能添加右括号
            if l < max_l and r > l:
                cur += ')'
                bfs(r, l+1)
                cur = cur[:-1]
        bfs()

        return ans
