"""
@title:      954. 二倍数对数组
@difficulty: 中等
@importance: 4/5
@tags:       sort
"""
from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        @tags:              hashmap
        @time complexity:   O(m*n)
        @space complexity:  O(m)
        @description:       当数组中存在x就需要一个2*x与之匹配, 为了寻找(x,2*x)对,我们需要根据x距离0的远近开始遍历
        """
        cnt = Counter(arr)
        # 0 只有自身与之匹配, 因此0的数量必须是偶数
        if cnt[0] % 2:
            return False
        for i in sorted(cnt, key=abs):
            if cnt[2 * i] < cnt[i]:
                return False
            cnt[2 * i] -= cnt[i]    # 💲操作counter不存在的键值对时是安全的
        return True
