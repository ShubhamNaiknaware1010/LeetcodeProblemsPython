#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0 
        for ch in s + t:
            xor ^= ord(ch)
        return chr(xor)
# @lc code=end

