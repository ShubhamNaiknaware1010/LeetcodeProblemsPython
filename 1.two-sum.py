#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create  a dictionary using the num : complement
        dict = { num : target - num for num in nums }
        # iterate over the array 
        for i,num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [i,nums.index(complement)]
                
# @lc code=end

