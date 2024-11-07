"""
@title:      HJ26 字符串排序
@difficulty: 简单
@importance: 2/5
@tags:       sort
"""
s = input()
s_split = s.split()
c_arr = []

for i, c in enumerate(s):
    if str.isalpha(c):
        c_arr.append((c.lower(), i))
c_arr.sort()

idx = 0
res = ""
for c in s:
    if str.isalpha(c):
        res += s[c_arr[idx][1]]
        idx += 1
    else:
        res += c
print(res)
