"""
80. 删除有序数组中的重复项 II
快慢指针;
快指针遍历nums
慢指针指向新数组的末尾，当nums[n] == nums[n-2]的时候，说明新数组中出现了两个重复的数字。 
nums[fast] == nums[slow-2] 的时候，舍弃nums[fast]

将题目退阶为不在原数组操作更便于理解
"""


from typing import List


class Solution:
    def removeDuplicates2(self, nums: List[int]) -> int:
        """
        这里是退阶的实现
        """
        # 新数组的元素少于2时，重复的数不可能大于2
        ans = nums[:2]
        # 遍历剩余的元素
        for i in range(2, len(nums)):
            n = len(ans)
            # num是新填入的数字
            num = nums[i]
            # 当 nums[n-2] == num 时，说明重复大于2了，不填入num
            if nums[n-2] != num:
                ans.append(num)
        return ans

    def removeDuplicates(self, nums: List[int], k=2) -> int:
        """
        快慢指针
        """
        slow = k
        for i in range(k, len(nums)):
            if nums[slow - k] != nums[i]:
                nums[slow] = nums[i]
                slow += 1
        return slow


Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
Solution().removeDuplicates2([1, 1, 1, 2, 2, 3])
