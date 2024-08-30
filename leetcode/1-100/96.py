"""
@title:      96. 不同的二叉搜索树
@difficulty: 中等
@importance: 5/5
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
        @tags:              dp 打表
        @time complexity:   O(n^2)
        @space complexity:  O(n)
        @description:       f[i] 表示当n为i时解构的可能性，f[i] 的左子树可能为 f[0]...f[i-1]，因此可以得到dp公式 f[i] = Σ(f[i-j] * f[j])
        """
        return f[n]
