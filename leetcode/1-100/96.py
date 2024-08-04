"""
@title:      96. 不同的二叉搜索树
@difficulty: 中等
@importance: 4/5
@tags:       dp
"""
f = [0] * 21
f[0] = 1
f[1] = 1
for i in range(2, 21):
    for j in range(i):
        f[i] += (f[j] * f[i-j-1])


class Solution:
    def numTrees(self, n: int) -> int:
        """
        @tags:              dp
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       左子树的可能性
        """
        return f[n]
