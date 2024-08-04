"""
name:       220. 存在重复元素 III
difficulty: 中等
importance: 4/5
tags:       滑动窗口 sort
"""
from sortedcontainers import SortedList
from typing import List
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, valueDiff: int) -> bool:
        """
        @tags:              滑动窗口 有序集合
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       219的滑动窗口思路移动窗口 不同的是窗口内的值是有序的，然后比较新加入的值与其左右元素的差值即可
        """
        window = SortedList()
        for i, v in enumerate(nums):  # O(n)
            if i > k:
                window.remove(nums[i - k - 1])   # O(logk) 去除超出窗口的值
            window.add(v)  # O(logk) 加入新加入窗口的值

            # 判断新插入的v与其左右元素的插值即可
            index = bisect.bisect_left(window, v)  # O(logk)
            # 和左侧比
            if index > 0 and window[index] - window[index - 1] <= valueDiff:
                return True
            # 和右侧比
            if index < len(window) - 1 and window[index + 1] - window[index] <= valueDiff:
                return True
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        """
        @tags:              滑动窗口 桶排
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       219的滑动窗口思路移动窗口 这里将
        """
        # 桶
        map = {}
        # 桶的size 桶的大小 确保桶内元素的差 <= valueDiff 这样如果桶内有两个相同的元素就满足题意了
        size = valueDiff + 1

        def getIdx(v):
            # 负数需要特殊处理，将 [-valueDiff 0]装进下标为0的桶
            return ((v + 1) // size) - 1 if v < 0 else v // size

        for i, v in enumerate(nums):  # O(n)
            # 判断v应该放入哪个桶
            idx = getIdx(v)  # O(1)
            # 桶内已有值
            if idx in map:
                return True
            # 检查相邻的桶
            if idx - 1 in map and v - map[idx-1] <= valueDiff:
                return True
            if idx + 1 in map and map[idx+1] - v <= valueDiff:
                return True

            map[idx] = v
            if i >= indexDiff:
                map.pop(getIdx(nums[i - indexDiff]))

        return False
