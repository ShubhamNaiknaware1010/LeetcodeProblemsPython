#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # Function to check if a given string is a palindrome, ignoring non-alphanumeric characters and case
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase to handle case insensitivity
        s = s.lower()
        
        # Initialize two pointers: one at the beginning (left) and one at the end (right)
        left = 0
        right = len(s) - 1
        
        # Loop until the left pointer is greater than the right pointer
        while left <= right:
            # If the left character is not alphanumeric, skip it
            if not s[left].isalnum():
                left += 1
            # If the right character is not alphanumeric, skip it
            elif not s[right].isalnum():
                right -= 1
            # If both characters are equal, move both pointers inward
            elif s[left] == s[right]:
                left += 1
                right -= 1
   

# @lc code=end

