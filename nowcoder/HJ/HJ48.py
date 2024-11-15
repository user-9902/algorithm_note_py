"""
@title:      HJ48 从单向链表中删除指定值的节点
@difficulty: 简单
@importance: 3/5
@tags:       链表 业务题
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


s = [int(i) for i in input().split()]
n = len(s)
m = {}
head = Node(s[1])
m[s[1]] = head
for i in range(s[0] - 1):
    v, pre = s[2 * i + 2], s[2 * i + 3]
    cur = Node(v)
    m[v] = cur
    if m[pre]:
        tmp = m[pre].next
        m[pre].next = cur
        cur.next = tmp

cur = res = Node(s[n - 1] + 1)
res.next = head
while cur:
    while cur.next:
        if cur.next.val == s[n - 1]:
            cur.next = cur.next.next
        else:
            break
    cur = cur.next
rr = []
res = res.next
while res:
    rr.append(str(res.val))
    res = res.next
print(" ".join(rr))
