"""
@title:      HJ93 数组分组
@difficulty: 中等
@importance: 3/5
@tags:       hash
@desc:       本题类似leetcode 416。但不能使用01背包求解，因为存在负数。
"""

n = int(input())
nums = [int(i) for i in input().split()]
sum_n = sum(nums)
target = sum_n // 2

if target * 2 < sum_n:
    print("false")
else:
    # 统计 3 的倍数
    s = set([0])
    ans = "false"
    a = 0
    for i in nums:
        if i % 3 == 0:
            a += i
    target = target - a

    for i in nums:
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            for j in list(s):
                s.add(j + i)
            s.add(i)
    if target in s:
        ans = "true"
    print(ans)
