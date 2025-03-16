#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create dictionary to store complement and its index
        dict = {}
        # iterate over the array 
        for i,num in enumerate(nums):
            # calculate the complement of number
            complement = target - num
            #check if complement exists in dict
            if complement in dict:
                # return index of number (i) and index of complement stored in nums[complement]
                return [i,dict[complement]]
            # Add  the num as a key and complement as value
            dict[num] = i
                
# @lc code=end

