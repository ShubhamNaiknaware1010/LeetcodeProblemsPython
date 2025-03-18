#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt = int(area ** 0.5)
        l,w = area,1
        for i in range(1,sqrt + 1):
            if area % i == 0:
                w = i
                l = area  // i
        return [l,w]
# @lc code=end

