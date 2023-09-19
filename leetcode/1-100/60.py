"""
60. 排列序列
迭代实现的，这里是独创的题解
一共有 !n 种可能的排列组合，以同一数字开头的一共有 !n-1 中组合，同理以同两位组合开头的一共有 !n-2 种可能
k // !(k-m) 不断的确认是第m位数，注意取数的时候是取剩余参数
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i + 1) for i in range(n)]
        res = ''
        # 跨度
        fac = 1
        for i in range(1, n):
            fac *= i

        rest = k
        while rest > 1:
            index = rest // fac
            # special case 以res开头的最后一种情况
            if rest % fac == 0:
                index -= 1
                res += nums[index]
                del nums[index]
                nums.reverse()
                return res + ''.join(nums)
            rest %= fac
            fac //= len(nums) - 1
            res += nums[index]
            del nums[index]

        res += ''.join(nums)
        return res
