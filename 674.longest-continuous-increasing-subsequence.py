#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
                max_count = max(max_count,count)
            else:
                count  = 1
        return max_count

            
# @lc code=end

