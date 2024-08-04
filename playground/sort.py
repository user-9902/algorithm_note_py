"""
name:       十大排序算法
difficulty: 中等
importance: 5/5
tags:       sort
"""
from typing import List


class Sort:
    """
    可借助leetcode 912 来验证
    """

    def bubble_sort(self, arr: List[int]):
        """
        @name:              冒泡排序 
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       从左至右依次比较前后两个元素，若前一个元素比后一个元素大，即交换他们。在一轮交换操作后，最大的元素被交换至队尾，循环处理除队尾以外的部分。
        @example.           [19,2,8,22,7,17] => [2,8,19,7,17,  22] => [2,8,7,17,  19,22]
        """
        n = len(arr)
        # len - 1 因为至少需要两个元素才能比较
        for i in range(n - 1):
            # len - 1 - i 因为需要两个元素才能比较,并且上一轮已经将最大元素置于队尾，无需再次遍历
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 冒泡排序，交换元素的开销比较大

    def select_sort(self, arr: List[int]):
        """
        @name:              选择排序 
        @time complexity:   O(n^2)
        @space complexity:  O(1)
        @description:       遍历整个数组，找寻最小（大）值，将最值置于队首（尾）。在一轮操作后最小元素在队头，循环处理除队头以外的部分。 
        @example:           [19,2,8,22,7,17] => [2,  19,8,22,7,17] => [2,7,  19,8,22,17]
        """
        len_l = len(arr)
        for i in range(len_l):
            min_i = i   # 记录最小元素的下标
            for j in range(i, len_l):
                if arr[j] < arr[min_i]:
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]  # 将最小元素交换至队首

    def insert_sort(self, arr: List[int]):
        """
        @name:              插入排序 
        @time complexity:   O(n) -> O(n^2)
        @space complexity:  O(1)
        @description:       遍历整个数组，将每个元素插入到有序数组中，有序数组初始为空。可以创建一个新数组来插入，还可以将入参的数组分为有序无序两个部分。
        @example:           [19,2,8,22,7,17] => [19,  2,8,22,7,17] => [2,19,  8,22,7,17] => [2,8,19,  22,7,17]
        """
        n = len(arr)
        for i in range(1, n):
            val = arr[i]  # 要插入的数

            # 寻找插入位置
            # 这里可以用二分寻找插入位置，但由于插入操作需要移动每个元素，因此不能降低时间复杂度
            j = i-1
            while j >= 0 and val < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = val

    def shell_sort(self, l: List[int]):
        """
        @name:              希尔排序 
        @time complexity:   O(nlogn) -> O(n^2)
        @space complexity:  O(1)
        @description:       希尔排序是对插入排序的优化，插入排序是不稳地的，原始数据越有序插入排序性能越好。希尔排序便是分多步将数组整理得越来越有序，使得快排变得稳定。
        @example:           [19,2,8,22,7,17] => [19, 8, 7 ]   => [7, 8, 19]
                                                   [2, 22, 17]      [2, 17, 22]
                            按步长将数组视为多个数组，分别插入排序，然后缩短步长直至为1。
        """
        len_l = len(l)
        step = len_l >> 1  # 初始步长

        while step > 0:
            # 步长的迭代
            for i in range(step):
                # 步长为n，既意味着存在n组数据
                for j in range(i, len_l, step):
                    pre_i = j - step
                    while pre_i >= i:
                        # 这里插入的实现类似冒泡，因为步长不同所以无法直接insert
                        if l[pre_i] > l[j]:
                            l[pre_i], l[j] = l[j], l[pre_i]
                        else:
                            # 等价于插入排序中提前结束
                            break
                        pre_i -= step
            step >>= 1

    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        @name:              归并排序 
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       将排序问题转化为合并两个有序数组问题，首先将数组切割为有序数组，即切割为只拥有一个元素的数组，然后两两合并。
        @example:           [12,7,8,1,24] => [12] [7] [8] [1] [24] => [7,12] [8] [1,24] => [7,8,12] [1,24]
        """
        n = len(arr)
        if n < 2:
            return arr

        # 二分，将数组分为两个有序数组
        mid = n >> 1
        left = arr[:mid]
        right = arr[mid:]
        # 数组的长度大于一，不能保证其有序性，需要递归调用
        left = self.merge_sort(left) if len(left) > 1 else left
        right = self.merge_sort(right) if len(right) > 1 else right

        # 合并两个有序数组left和right
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(left) and p2 < len(right):
            if left[p1] < right[p2]:
                res.append(left[p1])
                p1 += 1
            else:
                res.append(right[p2])
                p2 += 1

        # 剩余部分直接拼入
        res.extend(left[p1:])
        res.extend(right[p2:])

        return res

    def quick_sort(self, arr: List[int], left=0, right=None):
        """
        @name:              快速排序 
        @time complexity:   O(nlogn) -> O(n^2)
        @space complexity:  O(1)
        @description:       选择一个元素i，将剩余元素分为两堆，<i的置于一堆，>i的置于一堆，然后同样的方法分别处理分出的两堆数据。
        @example:           [12,7,8,1,24,15] => [7,8,1] 12 [24,15] => [1] 7 [8]   12   15 [24]
        """
        if right is None:
            right = len(arr)
        if right - left < 2:
            return

        # 确认 mid 在 arr 中的位置
        mid = right - 1   # 标准值最好随机生成，
        count = left  # 左边多少元素
        for i in range(left, right - 1):   # [)
            if arr[mid] > arr[i]:
                arr[count], arr[i] = arr[i], arr[count]
                count += 1
        arr[mid], arr[count] = arr[count], arr[mid]
        # mid左侧排序 mid右侧排序
        self.quick_sort(arr, left, count)
        self.quick_sort(arr, count+1, right)

    def heap_sort(self, arr: List[int]) -> List[int]:
        """
        @name:              堆排序 
        @time complexity:   O(nlogn)
        @space complexity:  O(1)
        @description:       将数组整理为堆。大根堆的根节点是最大的，将其与尾部元素交换，此时最大元素在尾巴，堆的根元素是错误的，我们整理完堆，再次重复即可。
        @example:           [19, 2, 8, 22, 7, 17, 9, 13] => 整理为堆 [22, 19, 17, 13, 7, 8, 9, 2] => [2]
        """
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1   # 左节点下标
            r = l + 1       # 右节点下标

            # 记录三节点中最值下标
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                # 交换
                arr[i], arr[largest] = arr[largest], arr[i]  # 交换
                # 被交换节点重新构建堆
                heapify(arr, n, largest)

        n = len(arr)
        # 初始化堆 O(n)
        for i in range(n, -1, -1):
            heapify(arr, n, i)

        # 一个个从堆顶取出最大元素 O(nlogn)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # 最大元素置于尾部
            heapify(arr, i, 0)  # logn

    # -------------- 上述排序都是基于比较的，下面的不是 ---------------#
    def counting_sort(self, arr: List[int]) -> List[int]:
        """
        @name:              计数排序 
        @time complexity:   O(n+k); n 是数组长度，k是数组中最大值和最小值的差值
        @space complexity:  O(k)
        @description:       hashmap的解法，统计数组中每个数字出现的次数，最后再按顺序输出。仅限于整数的排序。
        @example:           [2,8,7,2,10] => [2,0,0,0,0,1,1,0,1] => [2,2,7,8,10]
                                             2,3,4,5,6,7,8,9,10
        """
        if len(arr) == 0:
            return arr

        max_i = max(arr)
        min_i = min(arr)
        # 创建map表 下标对应具体的值 值对应出现的次数
        counter = [0] * (max_i - min_i + 1)
        # 统计所有的数
        for i, v in enumerate(arr):
            counter[v-min_i] += 1
        res = []
        for i, v in enumerate(counter):
            if v == 0:
                continue
            while v > 0:
                res.append(i + min_i)
                v -= 1
        return res

    def radix_sort(self, arr: List[int]) -> List[int]:
        """
        @name:              基数排序 
        @time complexity:   O(nk) 其中 k 是最大数的位数
        @space complexity:  O(n + k) 需要额外的空间存放计数数组和临时结果数组
        @description:       将整数从低位到高位进行分组整理, 统计完后整理数组, 然后升高一位重复。
        @example:           [123,34,5,12,5] => 个位统计后[12,123,34,5,5] => 十位[5,5,12,123,34] => ...
        """
        n = len(arr)
        max_v = max(arr)
        exp = 1
        while max_v // exp > 0:
            # 初始化计数数组
            counter = [0] * 10
            # 计算每个桶内元素的数量
            for i in range(n):
                counter[arr[i] // exp % 10] += 1
            # 更新计数数组，使之变为累计计数
            for i in range(1, 10):
                counter[i] += counter[i-1]

            # 从后往前遍历原始数组，根据计数数组填充结果数组
            res = [0] * n
            for j in range(n-1, -1, -1):
                index = arr[j] // exp % 10
                res[counter[index] - 1] = arr[j]
                counter[index] -= 1

            # 将排序后的结果赋回原数组
            for i in range(n):
                arr[i] = res[i]

            exp *= 10

    def bucket_sort(self, l: List[int]) -> List[int]:
        """
        @name:              桶排序 
        @time complexity:   O(n) ->  O(n^2)
        @space complexity:  O(n)
        @description:       桶排序是一种分布式的排序算法，将数据分散至多个'桶'中，然后分别对每个桶中的数据进行排序，最后再将桶中的数据合并。
        @example:           
        """
        max_i = max(l) >> 2
        buckets = [[] for _ in range(max_i + 1)]

        for i in l:
            # 这里分入几个桶的形式不是固定的
            buckets[i >> 2].append(i)

        for bucket in buckets:
            # 这里以快排为例
            self.quick_sort(bucket)

        res = []
        for bucket in buckets:
            if bucket:
                res.extend(bucket)
        return res


if __name__ == '__main__':
    sort = Sort()
    arr = [123, 34, 5, 12, 5]
    sort.radix_sort(arr)
