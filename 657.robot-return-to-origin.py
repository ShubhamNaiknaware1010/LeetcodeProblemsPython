#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = 0
        x = 0
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1 
            else:
                x += 1
        return y == x == 0
            
# @lc code=end

