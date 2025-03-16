#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            rev = rev * 10  + rem
            temp = temp // 10
        return rev == x
# @lc code=end

