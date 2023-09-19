"""
10大排序
排序算法还是非常有意思的，使我们初窥递归和迭代的魅力。
"""
from typing import List


class Sort:
    def bubble_sort(self, l: List[int]):
        """
        冒泡排序 O(n^2)
        从左至右依次比较前后两个元素，若前一个元素比后一个元素大，即交换他们。
        一轮循环后，最大的元素已被交换至队尾，再次处理除队尾外的部分。
        E.g.
            [19,2,8,22,7,17] => [2,8,19,7,17,  22] => [2,8,7,17,  19,22]
        """
        len_l = len(l)
        # len - 1 因为至少需要两个元素才能比较
        for i in range(len_l - 1):
            # len - 1 - i 因为需要两个元素才能比较,并且上一轮已经将最大元素置于队尾，无需再次遍历
            for j in range(len_l - 1 - i):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]  # 冒泡排序，交换元素的开销比较大

    def select_sort(self, l: List[int]):
        """
        选择排序 O(n^2)
        遍历list，找寻最小（或最大）值，将最小值置于队首
        一轮循环后，最小的元素已在队头，再次同样的逻辑处理剩余部分 
        E.g.
            [19,2,8,22,7,17] => [2, 19,8,22,7,17] => [2,7, 19,8,22,17]
        """
        len_l = len(l)
        for i in range(len_l):
            min_i = i   # 最小元素的下标
            for j in range(i, len_l):
                if l[j] < l[min_i]:
                    min_i = j
            l[i], l[min_i] = l[min_i], l[i]  # 将最小元素放置交换至队首

    def insert_sort(self, l: List[int]):
        """
        插入排序 O(n^2)
        遍历list中的每个元素，将每个元素插入到一个有序list中。
        如 将 1 插入到 [] 中，插入至 i=0 的位置。2 插入到 [1,3,4] 中，插入至 i=1 的位置。
        为减少内存开销，直接将入参l分为两个部分，有序的部分和无序的部分。
        E.g.
            [19, 2,8,22,7,17] => [2,19, 8,22,7,17] => [2,8,19 ,22,7,17]
        """
        for i, v in enumerate(l):
            for j in range(i + 1):
                # 遍历有序的部分，寻找当前值是否能插入
                # 当前值紧跟在有序部分的后面
                pre = l[j]
                if v < pre:
                    del l[i]
                    l.insert(j, v)
                    # 提前结束，找寻到了插入的位置，就可以结束了
                    break

    def shell_sort(self, l: List[int]):
        """
        希尔排序 最优 O(nlogn) 最差 (On^2)
        插入排序的优化版本，插入排序是可以提前停止的，既list原本越有序，便更容易提前停止。
        希尔排序选择一定的步长 k 将list分为 k 组分别进行插入排序。
        不断缩小 k 的值直至步长 k 为1，随着 k 的不断缩小，数组便得更加有序，最后一轮的插入排序便能更容易提前停止。
        E.g.
            l: [12,7,8,1,24] k: 2 => [8,  12,  24] => [1,7,8,12,24]
                                        1,   7,
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

    def merge_sort(self, l: List[int]) -> List[int]:
        """
        归并排序 O(nlogn)
        将list切割为多个有序数组（乱序list即切割为独立的元素）。
        将问题转化为合并多个有序数组的合并。
        E.g.
            [12,7,8,1,24] => [12] [7] [8] [1] [24] => [7,12] [1,8] [24]
        ps：本人这里的实现内存开销大，懒得优化[doge]
        """
        l_len = len(l)
        if l_len < 2:
            return l

        # 二分，将数组分为两个有序数组
        mid = l_len >> 1
        la = l[:mid]
        lb = l[mid:]
        # 数组的长度大于一，不能保证其有序性，需要递归调用
        la = self.merge_sort(la) if len(la) > 1 else la
        lb = self.merge_sort(lb) if len(lb) > 1 else lb

        # 合并有序数组la和lb
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(la) and p2 < len(lb):
            if la[p1] < lb[p2]:
                res.append(la[p1])
                p1 += 1
            else:
                res.append(lb[p2])
                p2 += 1

        if p1 == len(la):
            res.extend(lb[p2:])
        if p2 == len(la):
            res.extend(la[p1:])

        return res

    def quick_sort(self, l: List[int], left=0, right=0):
        """
        快速排序 O(nlogn)
        选一个元素 m，将剩余的元素分为两堆，<m 的置于 m 前面，>m 的置于 m 后面
        m的位置固定了，再用同样的方法处理分出来的两堆数据。
        E.g.
            [12,7,8,1,24,15] => [7,8,1] 12 [24,15]
        """
        right = right or len(l)
        if right - left < 2:
            return

        mid = left   # 随机选一个元素作为中间值，取第一个元素即可
        for i in range(left, right):
            if l[mid] > l[i]:
                if mid + 1 == i:
                    l[mid], l[i] = l[i], l[mid]
                else:
                    l[i], l[mid + 1] = l[mid + 1], l[i]
                    l[mid], l[mid + 1] = l[mid + 1], l[mid]
                mid = mid + 1

        # 区间（左闭右开）内元素的数量大于一，才能继续迭代排序
        if mid - left > 2:
            self.quick_sort(l, 0, mid)
        if right - mid > 2:
            self.quick_sort(l, mid + 1, right)

    def heap_sort(self, l: List[int]) -> List[int]:
        """
        堆排序 O(nlogn)
        堆（这里以大根堆为例）的根节点是最大的，将根节点和最后一个元素交换，
        这样最大的元素就被置于list的队尾了，然后用交换至根节点的元素再次将堆理顺即可迭代了。
        E.g.
            heap = [12,9,10,2,4,5,6] => [6,9,10,2,4,5,12] => [10,9,6,2,4,5,12]
        """

        # 大根堆的构建 O(nlogn)
        for i in range(len(l)):
            cur = l[i]
            pre_i = i + 1 // 2 - 1
            while pre_i >= 0:
                if cur > l[pre_i]:
                    l[i], l[pre_i] = l[pre_i], l[i]
                    i = pre_i
                else:
                    pre_i = pre_i + 1 // 2 - 1

        # 堆排，堆的根节点一定是最大的元素，每次取堆的根元素，并将堆整理即可。O(nlogn)
        for i in range(len(l) - 1, 1, -1):
            l[0], l[i] = l[i], l[0]  # 将根节点和最后一个元素交换
            # 把最后一个元素从根节点开始遍历，重新找出剩余元素的根节点（最大值）
            j = 0
            while j < i - 1:
                l_child_i = j + j + 1   # 左节点下标
                r_child_i = j + j + 2   # 右节点下标
                if l_child_i >= i - 1:
                    # 没有子节点了
                    break
                elif l_child_i == i or l[l_child_i] > l[r_child_i]:
                    # 有一个子节点 或 左子节点比右子节点的值大
                    l[j], l[l_child_i] = l[l_child_i], l[j]
                    j = l_child_i
                else:
                    l[j], l[r_child_i] = l[r_child_i], l[j]
                    # 右子节点比左子节点大
                    j = r_child_i
        return l

    def counting_sort(self, l: List[int]) -> List[int]:
        """
        计数排序
        大多数排序算法，都是基于元素间的比较实现的，而计数排序则不去进行比较.
        用一个的数组统计list中所有元素出现的个数。
        最后从小到大遍历统计的数组即可。
        E.g.
            counter=[1,0,0,0,2,1,0,1] => res = [0,4,4,5,7]
            index =  0,1,2,3,4,5,6,7
        """
        max_i = max(l)
        min_i = min(l)
        # 统计数组(这里可以优化，min_i为正数的时候，[0,min_i)之间的空间复杂度可以优化掉)
        counter = [0] * (max(max_i, max_i - min_i) + 1)
        # 统计所有是数，这里兼容了负数的处理
        for i in range(len(l)):
            counter[l[i]] += 1
        res = []

        # 是否存在负数 这里兼容了负数的处理
        if min(l) < 0:
            for i in range(min_i, 0, 1):
                while counter[i] > 0:
                    res.append(i)
                    counter[i] -= 1

        for i in range(max_i + 1):
            while counter[i] > 0:
                res.append(i)
                counter[i] -= 1
        return res

    def radix_sort(self, l: List[int]) -> List[int]:
        """
        基数排序
        按数字低位至高位统计，然后从0至9合并统计结果，如：[[0, 40], ... ,[13, 3], ...]  是按个位统计的
        从低位直至最高位统计，即可得到结果。
        在统计高位的时候低位一定是有序的，如：统计 13 14 的十位的时候13在个位统计的时候一定出现在14之前
        E.g.
            [0,3,4,14,50,81,1] => [0,50] [81,1] [3] [4,14] => [00,01,03,04] [14] [50] [81]
        """
        max_len = len(str(max(l)))  # 最大位数

        str_l = [str(i).rjust(max_len, '0') for i in l]
        for i in range(max_len):
            queues = [[] for i in range(10)]
            for s in str_l:
                queues[int(s[max_len - 1 - i])].append(s)
            str_l = []
            for j in queues:
                str_l.extend(j)
        return [int(i) for i in str_l]

    def bucket_sort(self, l: List[int]) -> List[int]:
        """
        桶排序
        桶排没有固定的形式，是一种思想
        将数据分为几类(装入不同的桶中)，然后将分别对每个桶中的数据排序
        最后合并桶中的数据即可
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
