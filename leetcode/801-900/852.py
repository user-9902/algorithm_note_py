"""
852. 山脉数组的峰顶索引
binary search;

binary的体现:
    if arr[mid] > arr[mid+1] 则mid是山坡的右侧或顶点
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        # special case
        if r == 0:
            return 0

        # 闭区间
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid - 1
            else:
                l = mid + 1
        return l
