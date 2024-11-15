"""
@title:      HJ64 MP3光标位置
@difficulty: 简单
@importance: 4/5
@tags:       业务模拟
"""

n = int(input())
cmds = input()

cur = 1
up = 1
down = min(n, 4)

for cmd in cmds:
    if cmd == "U":
        cur -= 1
        # 越界判断：
        if cur < up:
            if cur == 0:
                cur = n
                down = n
                up = max(1, n - 3)
            else:
                up = cur
                down = cur + 3
    else:
        cur += 1
        # 越界判断：
        if cur > down:
            if cur == n + 1:
                cur = 1
                down = min(n, 4)
                up = 1
            else:
                up = cur - 3
                down = cur
print(" ".join([str(i) for i in range(up, down + 1)]))
print(cur)
