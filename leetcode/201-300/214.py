"""
214. 最短回文串
KMP; 马拉车
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        manacher 马拉车
        """
        # 预处理
        s2 = '?' + s.replace('', '#') + '!'
        n = len(s2)
        f = [0] * n

        right = 0
        center = 0
        ans_center = 0

        for i in range(1, n-1):
            mirror = (2 * center) - i
            f[i] = 1 if i > right else min(f[mirror], right - i)

            while s2[i - f[i]] == s2[i + f[i]]:
                f[i] += 1

            if f[i] + i > right:
                right = f[i] + i
                center = i
            # 记录下，半径能到达字符串最左端的回文串中心
            if f[i] > ans_center and i - f[i] == 0:
                ans_center = i

        ans = ''
        for i in range(n-3, 2*ans_center-1, -2):
            ans += s2[i]

        return ans + s

    def shortestPalindrome2(self, s: str) -> str:
        """
        KMP 最长公共前后缀(get_next)
        """
        s2 = s + '?!' + s[::-1] # 中间加上盐值，防止s2自身是个回文串

        n = len(s2)
        
        length = 0
        i = 1
        f = [0]

        while i < n:
            if s2[length] == s2[i]:
                length += 1
                i += 1
                f.append(length)
            else:
                if length == 0:
                    f.append(0)
                    i += 1
                else:
                    length = f[length-1]
        return s[:f[-1]-1:-1] + s

    # def shortestPalindrome(self, s: str) -> str:
    #     """
    #     中心扩散 O(n^2)
    #     时间复杂度会炸掉 ❌
    #     """
    #     l = 0
    #     r = len(s) - 1

    #     if r == -1:
    #         return ''


    #     while True:
    #         cur = r
    #         while s[cur] == s[l] and cur > l:
    #             cur -= 1
    #             l += 1
    #         if cur - l < 1:
    #             break
    #         else:
    #             r -= 1
    #             l = 0
    #     ans = s
    #     for i in range(r+1, len(s)):
    #         ans = s[i] + ans
    #     return ans
Solution().shortestPalindrome2('abaa')
