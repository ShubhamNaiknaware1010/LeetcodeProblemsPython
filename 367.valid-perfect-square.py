#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <=   high:
            mid = (low + high)  // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            else:
                low = mid +  1
        return False

# @lc code=end

