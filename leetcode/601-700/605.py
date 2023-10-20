"""
605. 种花问题
greedy, 数组
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], m: int) -> bool:
        # 左右添加0，同步处理第一个和最后一个元素
        flowerbed.append(0)
        flowerbed.insert(0, 0)

        n = len(flowerbed)
        # for i in range(1, n-1):
        #     if flowerbed[i] == 1:
        #         continue
        #     # 这里存在重复判断
        #     elif flowerbed[i-1] == flowerbed[i+1] == 0:
        #         m -= 1
        #         flowerbed[i] = 1
        i = 1
        while i < n:
            if flowerbed[i-1] == flowerbed[i+1] == 0:
                m -= 1
                i += 2
            else:
                i += 1

        return m < 1


Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1)
