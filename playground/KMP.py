"""
name:           KMP
description:    一种高效的字符串子串查找算法

朴素的字符串匹配:
朴素的字符串匹配的时间复杂度为O(nm):
    ↓...↓                ↓                    ↓...↓
    abababcaa           abababcaa           abababcaa
    ||||X      ————>     X           ————>    |||||
    ababc                ababc                ababc
第一步中可以发现上方的父串，在从第1个字符对比到第5个字符后，
在第二步中却需要'回退'到第2个字符开始新一轮的比较。

KMP:
KMP解决的便是，朴素算法中'回退'的问题
KMP其实就是利用比较过程中的信息，使得父串中的指针'不用回退'
如果在一次朴素比较中能够匹配上的部分如下:
    ↓↓                    ↓...
    aa......            aa.......
    ||X         ————>   
    aa...                aa..
第一轮中，匹配完字符后，区别于朴素算法，我们不再去回退父串的指针。
不难发现，子串中有重复的部分，a和a，我们不需要再去重复比较。

下面换个例子，将上面的朴素算法例子中的第一步中重复的部分改为'abab'。显然我们可以把ab视为一个整体如上述a中操作一样，步骤如下：
    ↓...↓                   ↓.↓
    abababcaa           abababcaa      
    ||||X      ————>        |||
    ababc                 ababc
这里跳过了2步比较
那么这里跳过的本质是什么呢，是'最长公共前后缀'
还是以ababc为例子,
前缀指的是：从前向后的一个'子串'
——>
ababc
后缀指的是：从后向前的一个'子串'
  <——
ababc
公共前后缀指的是上述前后缀中公共的部分
ababc显然不包含重复的部分，因为a和b不同，后续的就无需考虑了
这里我们一个一个字符来看
    a -> 没有子串           0
    ab -> 也没有            0
    aba -> 存在前缀a和后缀a  1
    abab -> 前后缀最长为ab   2
    ababc ->                0
这里将算出的值保存进一个数组next中 [0, 0, 1, 2, 0]，利用next再次进行一次比较
        ↓                   ↓                    ↓                ↓
    ababaacc           ababaacc             ababaacc        ababaacc
    ||||X      ————>       |X       ————>        X     ————>     |X
    ababc                ababc                  ababc            ababc
    00120                00120                  00120            00120
设指向父串下标的指针为i,指向子串的指针为j。当发生不匹配的情况时我们就将j指针回退next[j-1]次再次开始一轮的比较

KMP改进
上面演示next的例子中有所体现，再来看一个极端的例子
        ↓                   ↓                       ↓
    aaaabc...           aaaabc...               aaaabc...
    ||||X       ————>       X         ————>         X
    aaaax                aaaax                     aaaax
    01230                01230                     01230
next在移动j的时候会发生重复比较，父串s[i] 多次比较了 t[next[j - 1]]
这里可以在生成next的时候改进这种情况 01230 -> 00000
我们将这种改进称的next称为nextval
"""


def kmp_next(string):
    """
    dp
    """
    n = len(string)
    next = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and string[i] != string[j]:
            j = next[j - 1]  # 最关键的一步 dp体现
        if string[i] == string[j]:
            j += 1
        next[i] = j
    return next


def get_child_str(s: str, t: str) -> int:
    m = len(t)
    next = kmp_next(t)
    j = 0
    for i, v in enumerate(s):
        while j > 0 and t[j] != v:
            j = next[j - 1]
        if t[j] == v:
            j += 1
        if j == m:
            return i - m + 1
    return -1


"""
可以借助 leetcode 28 来验证
"""
