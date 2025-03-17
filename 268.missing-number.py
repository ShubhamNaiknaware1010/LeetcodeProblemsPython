#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        nsum = n * (n + 1) // 2
        for num in nums:
            sum += num  
        return nsum - sum

# @lc code=end

