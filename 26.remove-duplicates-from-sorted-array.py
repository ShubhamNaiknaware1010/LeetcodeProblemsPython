#
# @lc app=leetcode id=26 lang=python3
#TODO
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                nums[k] = nums[i]
                k += 1
# @lc code=end

