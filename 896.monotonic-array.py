#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        rise = nums[-1] > nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1] and rise:
                return False
            elif nums[i] < nums[i + 1] and not rise:
                return False
        return True

        
# @lc code=end

