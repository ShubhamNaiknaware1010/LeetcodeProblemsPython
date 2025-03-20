#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0] *  len(nums)
        left = 0
        right = len(nums) - 1
        t = right
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                squares[t] = nums[right] * nums[right]
                right -= 1
            else:
                squares[t] = nums[left] * nums[left]
                left += 1
            t -=1
        return squares
# @lc code=end

