"""
@title:      HJ38 求小球落地5次后所经历的路程和第5次反弹的高度
@difficulty: 简单
@importance: 3/5
@tags:       math
"""

h = int(input())

print(2 * h + h / 2 + h / 4 + h / 8)
print(h * (1 / 2) ** 5)
