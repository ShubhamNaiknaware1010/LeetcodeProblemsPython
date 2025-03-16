#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s) != len(t):
            return False
        d = dict()
        for letter in s:
            d[letter] = d.get(letter,0) + 1
        for letter in t:
            d[letter] = d.get(letter,0) - 1
            if d[letter] < 0:
                return False 
        return True
                """
        return Counter(s) == Counter(t) 
        
                
# @lc code=end
