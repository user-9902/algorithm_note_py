"""
@title:      Rabin-Karp
@difficulty: 简单
@importance: 5/5
@tags:       滑动窗口 hash
"""

"""
寻找字符串子串的算法
流程如下：
    计算模式串的hash值，在文本串中寻找相同的hash值。
    在文本串中，创建一个和模式串长度相同的窗口。计算窗口的hash值。
    右移窗口，并更新hash值。（注意：更新hash值的操作必须是常数时间的，否则算法整体的复杂度不是线性的）
    窗口中的hash和模式串的hash相同时，即“可能”找到了目标字符串。（存在hash碰撞，hash相同还需要比较下具体的内容）
"""


def rabin_karp(pattern, text, prime_modulus=10**9 + 7, base=256):
    """
    Rabin-Karp 算法用于搜索模式串在文本串中的所有出现位置。
    :param pattern: 模式串
    :param text: 文本串
    :param prime_modulus: 用于计算哈希值的大素数
    :param base: 用于计算哈希值的基数
    :return: 一个列表，包含模式串在文本串中出现的所有起始索引
    """
    # hash计算 和 hash更新 没有不是固定的,确保是常数时间复杂度即可.
    def hash_func(s):
        """ 计算给定字符串 s 的哈希值 """
        h = 0
        for char in s:
            h = (h * base + ord(char)) % prime_modulus
        return h

    def update_hash(prev_char, new_char, old_hash, length):
        """ 更新哈希值，移除 prev_char 并加入 new_char """
        return ((old_hash - ord(prev_char) * pow_base[length - 1]) * base + ord(new_char)) % prime_modulus

    m = len(pattern)
    n = len(text)
    if m > n:
        return []

    # 计算模式串的哈希值
    pattern_hash = hash_func(pattern)
    # 计算文本串前 m 个字符的哈希值
    text_hash = hash_func(text[:m])
    # 预计算 base 的幂次方
    pow_base = [1] * (m + 1)
    for i in range(1, m + 1):
        pow_base[i] = (pow_base[i - 1] * base) % prime_modulus

    results = []
    # 遍历文本串
    for i in range(n - m + 1):
        # 如果当前窗口的哈希值与模式串的哈希值相等，则进一步检查，防止hash碰撞
        if text_hash == pattern_hash:
            # 检查是否真正匹配
            if text[i:i+m] == pattern:
                results.append(i)

        # 更新哈希值
        if i < n - m:
            text_hash = update_hash(text[i], text[i + m], text_hash, m)

    return results


if __name__ == "__main__":
    pattern = "ABCD"
    text = "ABC ABCDAB ABCDABCDABDE"
    matches = rabin_karp(pattern, text)
    print("Pattern found at indices:", matches)
