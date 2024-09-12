"""
@title:      1410. HTML 实体解析器
@difficulty: 简单
@importance: 3/5
@tags:       字符串匹配 业务分析
"""

CAR_ENTRIES = {
    "quot": '"',
    "apos": "'",
    "amp": "&",
    "gt": ">",
    "lt": "<",
    "frasl": "/",
}


class Solution:
    def entityParser(self, text: str) -> str:
        """
        @tags:              fs 字符串匹配
        @time complexity:   O(6n)
        @space complexity:  O(n)
        @description:       统计元素出现次数
        """
        n = len(text)
        ans = ""
        left = 0
        idx = 0
        while idx < n:
            if text[idx] == "&":
                for j in range(idx + 1, min(idx + 7, n)):
                    if text[j] == ";" and text[idx + 1: j] in CAR_ENTRIES:
                        ans += text[left:idx]
                        ans += CAR_ENTRIES[text[idx + 1: j]]
                        left = j + 1
                        idx = j
            idx += 1
        ans += text[left:n]
        return ans
