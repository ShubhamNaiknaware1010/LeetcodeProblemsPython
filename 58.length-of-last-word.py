#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    # Function to find the length of the last word in the given string
    def lengthOfLastWord(self, s: str) -> int:
        # Remove any leading or trailing spaces from the string
        s = s.strip(" ")
        
        # Initialize the index to point to the last character of the string
        i = len(s) - 1
        
        # Traverse the string from the end, looking for the first space
        while i >= 0 and s[i] != " ":
            i -= 1
        
        # The length of the last word is the difference between the string length and the position of the last space
        return len(s) - i - 1


# @lc code=end

