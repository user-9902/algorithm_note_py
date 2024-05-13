"""
5. 最长回文子串
difficulty: 中
importance: 5/5
tags:       数组，dp，马拉车
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩散法
        遍历中心（一个字符可以视为一个中心，多个连续字符也可视为中心），从中心向左向右拓展以寻找子串
        """
        n = len(s)
        ans = "" if n == 0 else s[0]
        i = 0
        while i < n-1:
            l = i - 1  # 中心的左边界
            r = i + 1  # 中心的右边界
            # 回文串的中心可能是技术或偶数，寻找最大中心
            while r < n and s[i] == s[r]:
                r += 1
            # 下次遍历的起点
            i = r
            # 开始向左向右扩散
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(ans):
                ans = s[l+1: r]

        return ans

    def longestPalindrome2(self, s: str) -> str:
        """
        dp
        区间dp
        dp[i][j]表示s[i:j]的最长子序列
        """
        pass

    def longestPalindrome3(self, s: str) -> str:
        """
        Manacher
        马拉车算法，中心拓展+dp的思想
        """
        # 预处理 兼容奇偶中心
        s = '?' + s.replace('', '#') + '!'
        n = len(s)
        f = [0] * n
        right = 0
        center = 0
        max_center = 0
        max_radius = 0

        for i in range(1, n-1):
            mirror = 2 * center - i
            f[i] = 1 if i >= right else min(right - i, f[mirror])
            while s[i-f[i]] == s[i+f[i]]:
                f[i] += 1

            # 右端点
            if f[i] + i > right:
                right = f[i] + i
                center = i

            # 记录下更大半径
            if f[i] > max_radius:
                max_radius = f[i]
                max_center = i

        return ''.join([s[i] for i in range(max_center - max_radius+2, max_center + max_radius, 2)])
