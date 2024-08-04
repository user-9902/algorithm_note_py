"""
@title:      406. 根据身高重建队列
@difficulty: 中等
@importance: 3/5
@tags:       sort
"""


from sortedcontainers import SortedList
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        @tags:              sort
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       按照身高从小到大排序，按身高低到高排队，没有比当前需要排队的人更矮的人了，因此其位置是确定的。
        @example：          假设第一个排队的值 ans[i] = [1,4]，由于没有比 ans[i][0] 小的值了，所以 ans[i] 前面元素的值ans[j]一定满足 ans[j][0] >= ans[i][0]，那么就意味着 ans[i] 前面一定刚好摆放着 ans[i][1] 个元素，即 ans[i] 的位置一定是5
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [0] * n
        for p in people:
            v = p[1] + 1
            for i in range(n):
                if not ans[i]:
                    v -= 1
                    if v == 0:
                        ans[i] = p
        return ans

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        @tags:              sort
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       同上方的思路，优化了寻找插入位置的过程
        """
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [0] * n
        # 剩余空位
        s = SortedList([i for i in range(n)])
        for p in people:
            i = p[1]
            ans[s[i]] = p
            s.remove(s[i])  # 去除被占据的位置
        return ans
