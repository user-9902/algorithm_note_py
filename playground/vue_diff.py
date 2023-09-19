from typing import List
"""
算法非常的精巧，但脱离的具体的实践场景，又不免让人觉得有些空洞。
vue中的diff，就是求最长递增子序列的一个不错的工程实践。
diff的作用就是，对比新旧list，判断出新list中的元素在旧list中对应的位置，以便dom的复用。
下面是diff的py实现
"""


def is_same_vnode_type(n1: str, n2: str):
    # 比较是否是可复用的type
    return n1 == n2


def patch(n1, n2):
    # if n2 != None n1 == None 则为新建
    # if n2 != None n1 != None 则为更新
    # if n2 == None n1 != None 则为卸载，vue中有独立的卸载方法。
    pass


def patch_keyed_child(c1: List[str], c2: List[str]):
    i = 0
    l1 = len(c1) - 1
    l2 = len(c2) - 2

    # (a b) c
    # (a b) d e
    # 1.去除掉头部相同的节点
    while i <= l1 and i <= l2:
        if (is_same_vnode_type(c1[i], c2[i])):
            patch(c1[i], c2[i])
        else:
            break
        i += 1

    # a (b c)
    # d e (b c)
    # 2.去除掉尾部相同的节点
    while i <= l1 and i <= l2:
        if (is_same_vnode_type(c1[l1], c2[l2])):
            patch(c1[l1], c2[l2])
        else:
            break
        l1 -= 1
        l2 -= 1

    # (a b)
    # (a b) c
    # 3.当为仅添加元素的场景
    if i > l1 and i <= l2:
        # 旧list遍历完，新list还有剩余，既需要新增元素场景。
        while i <= l2:
            patch(None, c2[i])
            i += 1

    # (a b) c
    # (a b)
    # 4.当为仅删除元素的场景
    elif i > l2:
        while i <= l1:
            patch(c2[i], None)
            i += 1

    # (a b) c d e (f g)
    # (a b) e d h c (f g)
    # 5.乱序场景，
    else:
        # a.
        s1 = i
        s2 = i
        key2new_index_map = {}
        for i in range(s2, l2):
            key2new_index_map[s2] = i
