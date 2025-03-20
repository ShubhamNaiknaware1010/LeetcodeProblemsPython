#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        temp = abs(x)
        rev = 0
        while temp > 0:
            rem = temp % 10
            rev = rev * 10 + rem
            temp = temp // 10
        if rev > 2 ** 31:
            return 0
        return rev * sign
# @lc code=end

