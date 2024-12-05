"""
@title:      3274. 检查棋盘方格颜色是否相同
@difficulty: 简单
@importance: 2/5
@tags:       业务模拟
"""

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        """ 
        @tags:              求余
        @time complexity:   O(1)
        @space complexity:  O(1)
        """
        idx = ord('a')
        a = (ord(coordinate1[0]) - idx + int(coordinate1[1]) - 1) % 2
        b = (ord(coordinate2[0]) - idx + int(coordinate2[1]) - 1) % 2
        return a == b
