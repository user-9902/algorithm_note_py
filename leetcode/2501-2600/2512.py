"""
2512. 奖励最顶尖的 K 名学生
hash; sort
"""
from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        words = {}
        for i in positive_feedback:
            words[i] = 3
        for i in negative_feedback:
            words[i] = -1

        ans = []
        for s, i in zip(report, student_id):
            score = 0
            for j in s.split(' '):
                score += words.get(j, 0)
            ans.append([-score, i])

        ans.sort()
        return [i[1] for i in ans[:k]]
