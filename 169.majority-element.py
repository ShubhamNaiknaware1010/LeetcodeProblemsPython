#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the initial count is zero 
        count = 0
        # el is the first element of list
        el = nums[0]
        # iterating over the list
        for num in nums:
            # if element matches the number increase count by 1
            if el==num:
                #increse count by 1
                count += 1
            else:
                # reduce count by 1
                count -=1
            #if the count of element is negative
            if count<0:
                # change el to num
                el = num
                #increase count by 1
                count = 1
        # returning the most frequent element
        return el
# @lc code=end

