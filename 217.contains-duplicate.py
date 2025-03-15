#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
"""



"""

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Creates  a set to store nums values in set
        s = set()   
        # Iterate over the loop 
        for num in nums:
            # check if number exists in set 
            if num in s:
                # return true if number exists
                return True
            # if number does not exist add it to set
            s.add(num)
        # return len(nums) !=  len(set(nums))
        #return false if no duplicates found
        return False

