"""
@title:      HJ68 成绩排序
@difficulty: 简单
@importance: 2/5
@tags:       sort
"""

n = int(input())
flag = input()

arr = [input() for i in range(n)]

if flag == "0":
    for i in sorted(arr, key=lambda x: -int(x.split()[1])):
        print(i)
else:
    for i in sorted(arr, key=lambda x: int(x.split()[1])):
        print(i)
