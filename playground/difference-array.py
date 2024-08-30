"""
@title:      差分数组
@difficulty: 简单
@importance: 5/5
@tags:       差分数组
@description:   保存着原数组相邻元素差值的数组 f[i] = nums[i] - nums[i-1]。类似于前缀和数组，用以辅助计算的数组结构
                arr      : 1,2,3,6,2,9,10   假设需要 [1, 5) 范围内的数同时 +2

                diff_arr : 1,1,1,3,-4,7,1   获取差分数组
                             3        5     diff_arr[1] += val; diff_arr[5] -= val
                diff_res : 1,3,1,3,-4,5,1   
                
                res      : 1,4,5,8,4,9,10   还原出结果
                单次区间同增无优势,多次连续操作时更高效.
"""

from typing import List


def get_diff_arr(nums: List[int]) -> List[int]:
    """
    获取差分数组
    """
    n = len(nums)
    arr = [0] * n
    for i in range(1, n):
        arr[i] = nums[i] - nums[i-1]
    return arr


def add_nums(nums, val, lo: int, hi: int):
    """
    应用场景：数组区间[l,r)内的元素 同增val
    """
    arr = get_diff_arr(nums)
    arr[lo] += val
    arr[hi] -= val
    a = 0
    res = [0] * len(nums)
    for i in range(len(nums)):
        a += arr[i]
        res[i] = a
    return res
