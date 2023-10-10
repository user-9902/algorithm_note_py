"""
5. 最长回文子串
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        双指针，中心扩散法
        依次以每个字符为中心，双指针向左右两边扩散比较，判断是否是回文串
        特殊情况：cbaabc，不是以单个字符为中心的时候，右指针多右移一步即可 
        """
        s_len = len(s)
        res_left = 0
        res_right = 0
        for i in range(s_len):
            left = i
            right = i
            # 连续两个字符处理
            if i+1 < s_len and s[i] == s[i+1]:
                l = left
                r = right + 1
                while -1 < l and r < s_len:
                    if s[l] == s[r]:
                        l -= 1
                        r += 1
                    else:
                        break
                if r - l > res_right - res_left:
                    res_left = l
                    res_right = r

            while -1 < left and right < s_len:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if right - left > res_right - res_left:
                res_left = left
                res_right = right

        return s[res_left+1:res_right]

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
