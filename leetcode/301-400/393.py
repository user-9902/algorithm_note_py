"""
@title:      393. UTF-8 编码验证
@difficulty: 中等
@importance: 4/5
@tags:       业务分析
"""
from typing import List

arr = [128 + 64, 128 + 64 + 32, 128 + 64 + 32 + 16, 128 + 64 + 32 + 16 + 8]


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        @tags:              业务分析 
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       分类讨论即可
        """
        n = len(data)
        idx = 0
        while idx < n:
            cur = data[idx]
            # 1
            if cur < (1 << 7):
                idx += 1
                continue
            # 2 - 4
            flag = False
            for i in range(3):
                if arr[i] <= cur < arr[i + 1]:
                    flag = True
                    c = i + 2
                    # 长度检查
                    if idx + c - 1 >= n:
                        return False
                    # 头部 10 检查
                    for k in range(1, c):
                        if data[idx + k] < 128 or data[idx + k] >= 128 + 64:
                            return False
                    idx += c
                    break
            if flag:
                continue
            # else
            return False
        return True
