from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        dic = {}
        for i in p:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        left = 0
        right = 0
        dic_s = {}
        res = []
        for i, v in enumerate(s):
            if v in dic:
                # 当前字符需要统计的时候
                right += 1
                
                # 维护字典表
                if v in dic_s:
                    dic_s[v] += 1
                else:
                    dic_s[v] = 1
                if right - left > len(p):
                    dic_s[s[left]] -= 1
                    left += 1
                
                # hash表相同时
                if dic_s == dic:
                    res.append(left)
            else:
                # 当前字符串不在字典表中时
                # 就直接重置条件，跳过该字符重新开始统计
                left = i + 1
                right = i + 1
                dic_s = {}

        return res
