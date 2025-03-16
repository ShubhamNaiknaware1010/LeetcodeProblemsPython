#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    # Function to find the first occurrence of 'needle' in 'haystack'
    def strStr(self, haystack: str, needle: str) -> int:
        # Get the length of the needle string
        l = len(needle)
        
        # Loop through the haystack up to the point where a substring of length 'l' can still fit
        for i in range(len(haystack) - l + 1):
            # Check if the current substring of length 'l' matches the needle
            if haystack[i:i+l] == needle:
                # If a match is found, return the index of the first character of the match
                return i
        
        # If no match is found, return -1
        return -1

# @lc code=end

