#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for ch in magazine:
            d[ch] = d.get(ch,0) + 1
        
        for ch in ransomNote:
            if d.get(ch,0) > 0:
                d[ch] -= 1
            else:
                return False
        return True 
# @lc code=end

