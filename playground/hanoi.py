"""
汉诺塔
简单的递归实现 如 要整体从a->c 就需要将n-1先移动至b ... 直至n==1
"""

STEP = ('A', 'B', 'C')


def move(x, y):
    print('%s -> %s' % (x, y))


def hanoi(n, start, end, trans):
    # 递归实现的hanoi
    if n == 1:
        move(start, end)
    else:
        # 将n-1个块，移动到过渡节点上
        hanoi(n-1, start, trans, end)
        # 将最底下的块，移动到end上
        hanoi(1, start, end, None)
        # 将n-1个块，从过渡节点移到end上
        hanoi(n-1, trans, end, start)


def hanoi2(n, start, end, trans):
    # 非递归汉诺塔
    stack = [(n, start, end, trans)]
    while stack:
        cur = stack.pop()
        if cur[0] == 1:
            move(cur[1], cur[2])
        else:
            stack.append((cur[0] - 1, cur[3], cur[2], cur[1]))
            stack.append((1, cur[1], cur[2], None))
            stack.append((cur[0] - 1, cur[1], cur[3], cur[2]))


hanoi(3, 'A', 'B', 'C')
print('----------------')
hanoi2(3, 'A', 'B', 'C')
