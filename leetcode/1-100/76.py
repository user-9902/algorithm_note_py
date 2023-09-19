"""
76. 最小覆盖子串
滑动窗口
右边界来满足覆盖
左边界来寻找最小
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        t_map = {}
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1

        l = 0

        res_l = 0
        res_r = 0
        for i, v in enumerate(s):
            if v in t_map:
                t_map[v] -= 1
                # 满足覆盖条件
                if all(_ < 1 for _ in t_map.values()):
                    # 寻找最小覆盖
                    while all(_ < 1 for _ in t_map.values()):
                        if s[l] in t_map:
                            t_map[s[l]] += 1
                        l += 1
                    if (res_r - res_l > i - l) or (res_l == 0 and res_r == 0):
                        res_l = l
                        res_r = i

        return '' if res_l == 0 else s[res_l - 1: res_r + 1]
