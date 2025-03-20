#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#TODO

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for ch1,ch2 in zip(s,t):
            if ch1 in d and d[ch1] == ch2:
                continue
            if (ch1 in d and d[ch1] != ch2) or ch2 in d.values() :
                return False
            d[ch1] = ch2
        return True            


# @lc code=end

