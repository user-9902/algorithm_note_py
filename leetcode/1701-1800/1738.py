"""
@title:      1738. 找出第 K 大的异或坐标值
@difficulty: 中等
@importance: 4/5
@tags:       前缀异或和
"""

from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """
        @tags:              前缀异或和 + 第k大的数
        @time complexity:   O(nm)
        @space complexity:  O(nm)
        @description:       
        """
        # 前缀异或和
        n, m = len(matrix), len(matrix[0])
        f = [[0] * (m + 1) for _ in range(n + 1)]

        # 第k大的数，最小堆
        heap = [-1] * k

        def heapfiy(arr, n, idx):
            i = idx
            l = 2 * idx + 1
            r = l + 1
            if l < n and arr[l] < arr[i]:
                i = l

            if r < n and arr[r] < arr[i]:
                i = r

            if i != idx:
                arr[idx], arr[i] = arr[i], arr[idx]
                heapfiy(arr, n, i)

        # 第k大
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = f[i][j + 1] ^ f[i +
                                                  1][j] ^ f[i][j] ^ matrix[i][j]
                if f[i + 1][j + 1] > heap[0]:
                    heap[0] = f[i + 1][j + 1]
                    heapfiy(heap, k, 0)

        return heap[0]
