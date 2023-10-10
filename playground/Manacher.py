"""
马拉车算法 Manacher
专门用来解决最长回文子串问题的算法
最长回文子串的经典算法是中心拓展，其的时间复杂度是O(n^2)。拉车算法在中心拓展的基础上运用了dp的思想，使得复杂度降至O(n)

以 aaabaaa 为例
在中心拓展中
    遍历至b时我们得到一个最大的回文串aaabaaa
    遍历至b右侧的第二个a时，根据 “b为中心子串的对称性” 可以知道b右侧第二个a至少能组成长度为3的回文串。
    因为右侧第二个a与左侧第二个a堆成，而左侧第二个a能组成aaa的回文串，所以b右侧第二个a在中心拓展的时候可以直接从 aaa 开始。
"""


def Manacher(s: str):
    # 预处理 兼容奇偶中心
    s = '?' + s.replace('', '#') + '!'
    n = len(s)
    f = [0] * n

    right = 0
    center = 0
    max_center = 0
    max_radius = 0

    for i in range(1, n-1):
        # 获取对称位置的半径
        mirror = 2 * center - i
        # 能跳过对比的半径（单个字符自身的半径视为 1）
        f[i] = 1 if i >= right else min(right - i, f[mirror])
        while s[i-f[i]] == s[i+f[i]]:
            f[i] += 1

        # 移动right，i < right 的时候可以利用对称性
        if f[i] + i > right:
            right = f[i] + i
            center = i

        # 记录下更大半径
        if f[i] > max_radius:
            max_radius = f[i]
            max_center = i

    # 跳过range步长为2，跳过#
    # 对应原字符开始的位置为 (maxCenter - p[maxCenter]) // 2
    return ''.join([s[i] for i in range(max_center - max_radius + 2, max_center + max_radius, 2)])


print(Manacher('mabakabat'))

"""
可借助leetcode 5 来验证算法
"""
