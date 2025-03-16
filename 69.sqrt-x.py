#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    # Function to compute the integer square root of a non-negative integer
    def mySqrt(self, x: int) -> int:
        # Calculate the square root of x and return the integer part of the result
        return int(x ** 0.5)

        
# @lc code=end

