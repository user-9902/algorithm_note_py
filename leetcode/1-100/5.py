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
        """
        pass
