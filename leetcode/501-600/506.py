"""
name:       506. 相对名次
difficulty: 简单
importance: 4/5
tags:       hashmap
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        @tags:              hashmap
        @time complexity:   O(nlogn)
        @space complexity:  O(n)
        @description:       hashmap 需要知道排序前和排序后的键值关系 建立关系后排序即可
        """
        n = len(score)
        entries = [[score[i], i] for i in range(n)]
        print(entries)
        entries.sort(key=lambda x: x[0])
        for i in range(n - 1, -1, -1):
            s = str(n - i)
            if i == n - 1:
                s = "Gold Medal"
            if i == n - 2:
                s = "Silver Medal"
            if i == n - 3:
                s = "Bronze Medal"
            score[entries[i][1]] = s
        return score
