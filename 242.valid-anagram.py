#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimized version using Counter (hash map approach)
        return Counter(s) == Counter(t)
        
        """
        # Commented-out original version using a dictionary to track character counts
        # If the lengths of s and t are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create a dictionary to count the occurrences of each letter in s
        d = dict()
        
        # Count the occurrences of each letter in s
        for letter in s:
            d[letter] = d.get(letter, 0) + 1
        
        # Subtract the occurrences based on letters in t
        for letter in t:
            d[letter] = d.get(letter, 0) - 1
            # If any letter count becomes negative, s and t cannot be anagrams
            if d[letter] < 0:
                return False
        
        # If all counts are zero, s and t are anagrams
        return True
        """

        
                
# @lc code=end
