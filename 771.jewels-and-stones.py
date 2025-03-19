#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for ch in stones:
            if ch in s:
                count += 1
        return count

            
# @lc code=end

