#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        distinctCandies = len(set(candyType))
        halfCandies = len(candyType) // 2
        return min(halfCandies,distinctCandies)
# @lc code=end

