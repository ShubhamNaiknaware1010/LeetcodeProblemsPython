#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ord(ch) > ord(target):
                return ch
        return letters[0]
# @lc code=end

