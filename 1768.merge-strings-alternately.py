#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize the index variable
        i = 0
        # Initialize the result string
        s = ""
        
        # Find the minimum length of the two words to avoid index out of range
        min_len = min(len(word1), len(word2))
        
        # Loop through both strings until we reach the end of the shorter one
        while i < min_len:
            # Add alternating characters from both strings to the result
            s += word1[i] + word2[i]
            # Increment the index to move to the next character
            i += 1
        
        # After the loop, add the remaining characters from the longer string
        s += word1[i:]  # Add the remaining part of word1 if any
        s += word2[i:]  # Add the remaining part of word2 if any
        
        # Return the merged string
        return s

        
# @lc code=end

