"""
30. 串联所有单词的子串
因为words中所参数的长度的是相同的，
所以先使用滑块s中存在的所有字符串的可能。
退阶问题 leetcode 438
"""
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        滑动窗口
        """
        s_len = len(s)
        word_len = len(words[0])

        words_dic = {}
        for i in words:
            if i in words_dic:
                words_dic[i] += 1
            else:
                words_dic[i] = 1

        res = []
        for i in range(word_len):
            # 字符串的左右边界
            left = i
            right = word_len + i
            counter = {}
            # 滑块的左边界,右边界即上方的right
            l = left
            while right <= s_len:
                s_slice = s[left:right]

                if s_slice in words_dic:
                    if s_slice in counter:
                        counter[s_slice] += 1
                    else:
                        counter[s_slice] = 1
                    if right - l > len(words[0]) * len(words):
                        counter[s[l: l + word_len]] -= 1
                        l += word_len
                    if counter == words_dic:
                        res.append(l)
                else:
                    counter = {}
                    l = right
                left += word_len
                right += word_len
        return res

    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     """
    #     暴力遍历
    #     截取定长字符串生成hash，比较截取字符串生成的hash和words的hash是否相等
    #     """
    #     words_len = len(words[0]) * len(words)
    #     if len(s) < words_len: return []
    #     words_dic = {}
    #     for i in words:
    #         if i in words_dic:
    #             words_dic[i] += 1
    #         else:
    #             words_dic[i] = 1

    #     res = []
    #     for i in range(len(s) - words_len + 1):
    #         left = i
    #         right = i +  words_len
    #         s_slice = s[left:right]
    #         dic = {}
    #         for i in range(len(words)):
    #             l = i * len(words[0])
    #             r = (i + 1) * len(words[0])
    #             ss = s_slice[l:r]
    #             if ss not in words_dic:
    #                 break
    #             else:
    #                 if ss in dic:
    #                     dic[ss] += 1
    #                 else:
    #                     dic[ss] = 1
    #         if dic == words_dic:
    #             res.append(left)
    #     return res


if __name__ == '__main__':
    test = Solution()
    test.findSubstring("wordgoodgoodgoodbestword", [
                       "word", "good", "best", "word"])
