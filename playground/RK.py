"""
Rabin-Karp
查找字符串子串的算法
通过hash指纹的方式来实现的线性时间复杂度的算法。
RK算法改进了BF(Brute Force)算法的对比过程：
    BF算法中子串匹配的时间复杂度是O(m)然后一共需要对比n次因此总共的时间复杂度为O(nm)
    RK算法中子串的hash匹配的时间复杂度将为了O(1)，因此总的线性复杂度为O(n)
    RK算法需要解决hash碰撞

hash算法有很多种，为了节省hash计算的开销。我们可以利用父串中重复的部分。
    abcaaaded              abcaaaded
    |||          ————>     -||+
    ccc                     ccc
如上图中，每一次移动，父串的之间的hash只有两个字符。因此这里的hash值的计算要利用这里重复的部分。
"""


def Rk(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    t_hash = get_hash(t)
    s_hash = get_hash(s[0:m])
    print(t_hash, s_hash)
    for i in range(n - m):
        if t_hash == s_hash and s[i:i+m] == t:  # 可能存在hash碰撞，需要严格对比下字符串
            return i
        s_hash /= ord(s[i]) // 26   # 取模防止浮点误差
        s_hash *= ord(s[i+m]) // 26
        print(s_hash)

    return n-m if s[n-m:] == t else -1


# 计算hash
def get_hash(s: str) -> int:
    n = len(s)
    ans = 1
    for i in range(n):
        ans *= ord(s[i]) // 26
    return ans


"""
可以通过 leetcode 28 来验证
"""
