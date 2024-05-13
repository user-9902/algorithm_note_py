"""
二分
二分，就是把一个集合，分为两个无交集的集合。

红蓝染色法
红蓝，既两个集合
染色，如何将数据放入两个集合中。
"""

from typing import List


def searchInsert(list: List[int], target: int):
    # 在递增的有序数组中寻找target
    # 这里将list分为两个部分，既 >= target 的一个集合和 < target的一个集合；当然分为 > target  和 <= target 的两个集合也是可以的
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        # mid >= target 所以mid以及mid右侧的数都可以放入值 >= target 的集合中
        if list[mid] >= target:
            # 移动边界，以将剩余的数填入红蓝两个集合中
            right = mid - 1
        # 否则即 mid < target 时 mid及mid左侧的所有的元素都放置到 < target 的集合中
        else:
            left = mid + 1
        # 最后一步也是十分关键的，即分析right和left的中止状态 right < target
        return left
