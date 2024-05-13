"""
2698. 求一个整数的惩罚数
math; dfs
为减少测试用例的重复计算可以利用打表的方式
本题的关键就是判断一个数是否是 惩罚数
"""


def check(n: int, target: int) -> bool:
    if n == target:
        return True
    # 减少字符串和数字之间的转换
    d = 10
    # dfs
    while n >= d and n % d <= target:
        if check(n // d, target - (n % d)):
            return True
        d *= 10

    return False


# 打标的方式来减少测试用例的重复计算
max_cnt = 1000
arr = [False]*(max_cnt+1)
for i in range(max_cnt+1):
    arr[i] = check(i*i, i)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            if arr[i]:
                ans += i * i
        return ans
