#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max = 0
        smax = 0 
        for i,num in enumerate(nums):
            if num > max:
                smax = max
                max  = num
                idx = i
            elif num > smax:
                smax = num
            
        print(smax,max,idx)
        if smax * 2 <= max:
            return idx
        return -1
# @lc code=end

