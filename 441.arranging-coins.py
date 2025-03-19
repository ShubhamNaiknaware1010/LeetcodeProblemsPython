#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        count =0
        while sum <= n:
            count += 1
            sum += count 
        return count - 1
# @lc code=end

