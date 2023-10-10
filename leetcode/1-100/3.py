"""
3. 无重复字符的最长子串
滑动窗口
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = -1  # 慢指针 从-1开始满足长度为1的字符串
        res = 0
        dic = {}
        for j in range(len(s)):  # j 是快指针
            cur_s = s[j]
            if cur_s in dic:
                i = max(dic[s[j]], i)
            dic[cur_s] = j
            res = max(j - i, res)
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 获取索引 i
            dic[s[j]] = j  # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res
