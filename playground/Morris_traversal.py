"""
name:       Morris Traversal
difficulty: 中等
importance: 5/5
tags:       dfs morris
"""

"""
Morris Traversal是一种二叉树的遍历方式。可以将空间复杂度优化至O(1)。

递归、非递归的二叉树遍历，都离不开栈，这就使得空间复杂度为O(n)。
遍历时我们在树中向下移动，栈中保存路径信息，直至无法向下时，依据先前栈中保存的路径信息完成向上的移动。

如何“向上”便是能完成遍历的关键，树的叶子节点存在很多空指针，morris遍历便是利用了这些空指针，保存向上的信息来优化空间复杂度的。

先序morris 见leetcode 144
中序morris 见leetcode 94
后序morris 见leetcode 145
"""
