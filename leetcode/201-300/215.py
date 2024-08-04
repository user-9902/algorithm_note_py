"""
name:       215. 数组中的第K个最大元素
difficulty: 中等
importance: 5/5
tags:       sort
"""
from typing import List
import heapq


class Solution:
    """
    这里明显是排序题，但由于题目O(n)时间复杂度的限制，需要我们借助排序算法并进行优化。
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        @tags:              hape sort
        @time complexity:   O(n)
        @space complexity:  O(1)
        @description:       堆（大顶堆）化后，去除k-1个元素，最后堆的顶就是结果
        """
        n = len(nums)

        def heapfiy(i, n):
            lagest = i
            l = 2 * i + 1
            r = l + 1

            if l < n and nums[l] > nums[lagest]:
                lagest = l
            if r < n and nums[r] > nums[lagest]:
                lagest = r

            if lagest != i:
                nums[lagest], nums[i] = nums[i], nums[lagest]
                heapfiy(lagest, n)
        # 堆化
        for i in range(n-1, -1, -1):
            heapfiy(i, n)
        # 去除k-1个顶
        for j in range(1, k):
            nums[0], nums[n - j] = nums[n - j], nums[0]
            heapfiy(0, n - j)

        return nums[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        @tags:              hape sort
        @time complexity:   O(n)
        @space complexity:  O(n)
        @description:       同上解，借助内置api实现
        """
        pq = []   # 将数组加入小顶堆，堆中维护当前值最大的k个数
        for num in nums:
            heapq.heappush(pq, num)  # 当前元素入堆
            if len(pq) > k:
                heapq.heappop(pq)   # 堆中元素超过k个，弹出最小的那个
        return pq[0]    # 最后堆顶的即为第k大的数

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            @tags:              fast sort
            @time complexity:   O(n)
            @space complexity:  O(1)
            @description:       基于快速排序的筛选过程，快排过程中，当选中间元素的时候，我们还能知道左右两边元素的个数，估计k值我们可以选择左边或右边继续快排
            """
        def fast_sort(l, r, k):
            x = r-1
            counter = l  # ❌这里守卫元素的选择不好
            for i in range(l, r):
                if nums[x] > nums[i]:
                    nums[i], nums[counter] = nums[counter],  nums[i]
                    counter += 1
            nums[x], nums[counter] = nums[counter], nums[x]

            if counter == k:
                return nums[counter]
            elif counter > k:
                return fast_sort(l, counter, k)
            else:
                return fast_sort(counter+1, r, k)

        n = len(nums)
        return fast_sort(0, n, n - k)
