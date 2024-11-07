"""
@title:      HJ32 密码截取
@difficulty: 中等
@importance: 5/5
@tags:       LPS
@desc:       区别于最长回文子序列，这里要求的是最长回文子数组
"""

s = input()
n = len(s)
f = [[0] * (n) for _ in range(n)]

for i in range(n-1, -1, -1):
    f[i][i] = 1
    for j in range(i + 1, n):
        if s[i] == s[j] and f[i+1][j-1] == j-i-1:
            f[i][j] = f[i+1][j-1] + 2
        else:
            f[i][j] = max(f[i+1][j], f[i][j-1])

print(f[0][n-1])

# ❌ 上方的复杂度超了，不能ac，需要压缩至一维

s = input()
n = len(s)
f = [0] * n

for i in range(n-1, -1, -1):
    f[i] = 1
    pre = 0
    for j in range(i + 1, n):
        # 左 下 左下 数据
        tmp = f[j]
        if s[i] == s[j] and pre == j-i-1:
            f[j] = pre + 2
        else:
            f[j] = max(f[j], f[j-1])
        pre = tmp
print(f[n-1])
