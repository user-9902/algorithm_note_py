"""
38. 外观数列
difficulty: 简单
importance: 1/5
tags:       打表,数组
"""

ans = ['1']

for i in range(2, 31):
    res = ''

    string = ans[-1]
    n_s = len(string)

    cnt = 1
    cur = string[0]

    for j in range(1, n_s):
        if string[j] == cur:
            cnt += 1
            continue
        res += str(cnt)
        res += cur
        cnt = 1
        cur = string[j]
    res += str(cnt)
    res += cur
    ans.append(res)


class Solution:
    def countAndSay(self, n: int) -> str:
        return ans[n-1]
