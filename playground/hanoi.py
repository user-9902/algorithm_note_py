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
    pass


hanoi(3, 'A', 'B', 'C')
