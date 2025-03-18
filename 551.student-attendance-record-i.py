#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        late = 0
        for i in range(len(s)):
            if s[i] == "A":
                absents += 1
                if absents > 1:
                    return False
                late = 0
            elif s[i] == "L":
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
        return True
# @lc code=end

