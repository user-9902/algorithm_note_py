"""
寻找两个正序数组的中位数
本题目复杂的是处理边界条件
"""

from typing import List


class Solution:
    def solution2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        双指针 O(n)
        可以通过双指针来创建一个新的数组,再算出结果
        优化，遍历时只存下目标次数的值即可
        """
        p1 = p2 = 0
        # 总长度是否是奇数
        is_odd = (len(nums1) + len(nums2)) % 2 == 1
        # 需要移动的总次数
        times = int((len(nums1) + len(nums2))/2) + 1
        target_time = [times - 1]if is_odd else [times - 2, times - 1]
        res = []

        for i in range(times):
            if p1 == len(nums1):
                if i in target_time:
                    res.append(nums2[p2])
                p2 += 1
            elif p2 == len(nums2):
                if i in target_time:
                    res.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                if i in target_time:
                    res.append(nums1[p1])
                p1 += 1
            else:
                if i in target_time:
                    res.append(nums2[p2])
                p2 += 1

        return float(res[0] if is_odd else (res[0] + res[1]) / 2)

    def solution3(self, nums1: List[int], nums2: List[int]) -> float:
        """
        折半查找 O(log(n))
        将题目转化为，在两个有序数组中查找第k小的元素
        """
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    # 数组一被全部丢弃
                    return nums2[index2 + k - 1]
                if index2 == n:
                    # 数组二被全部丢弃
                    return nums1[index1 + k - 1]
                if k == 1:
                    # 寻找最小的数的情况
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]

                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


if __name__ == '__main__':
    test = Solution()
    test.solution2([1, 2], [-1, 3])
    test.solution3([3, 4], [1, 3])
    test.solution3([3, 4], [1, 3, 4])
