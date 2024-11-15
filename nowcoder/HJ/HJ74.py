"""
@title:      HJ74 参数解析
@difficulty: 简单
@importance: 3/5
@tags:       业务模拟 快慢指针
"""

s = " " + input() + " "
l = 1
endStr = " "
ans = []
for i, c in enumerate(s):
    if c == endStr:
        if s[l:i]:
            ans.append(s[l:i])
        endStr = " "
        l = i + 1
    if endStr == " " and c == '"' and s[i - 1] == " ":
        endStr = '"'
        l += 1

print(len(ans))
for i in ans:
    print(i)
