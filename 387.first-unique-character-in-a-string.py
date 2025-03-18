#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i,ch in enumerate(s):
            if ch in d:
                d[ch] = -1
            else:
                d[ch] = i
        for index in d.values():
            if index != -1:
                return index
        return -1
# @lc code=end

