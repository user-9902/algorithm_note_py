"""
@title:      969. 煎饼排序
@difficulty: 简单
@importance: 5/5    背景参考百科:煎饼排序
@tags:       sort
"""
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        @tags:              swap sort
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       每轮将一个数字交换至末尾, 交换至末尾需要两部 先交换至头部 再交换至尾部
        """
        n = len(arr)
        res = []

        # 一次次将最大的数交换至末尾
        def reverse(r):
            res.append(r + 1)
            l = 0
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        def step(right):
            idx = 0
            for i in range(right+1):    # O(n)
                if arr[i] > arr[idx]:
                    idx = i
            if right == idx:
                return
            reverse(idx)    # O(n)
            reverse(right)  # O(n)

        # O(n^2)
        for i in range(n - 1, 0, -1):
            step(i)
        return res
