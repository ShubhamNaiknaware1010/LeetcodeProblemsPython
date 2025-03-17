#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        t  = num % 9
        return 9 if t == 0 else t
# @lc code=end

