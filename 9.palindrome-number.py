#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    # Function to check if an integer is a palindrome
    def isPalindrome(self, x: int) -> bool:
        # Initialize a variable to store the reversed number
        rev = 0
        
        # Store the original number for comparison later
        temp = x
        
        # Loop to reverse the digits of the number
        while temp > 0:
            # Get the last digit of the number (remainder when divided by 10)
            rem = temp % 10
            
            # Append the digit to the reversed number (multiply rev by 10 to shift left, then add rem)
            rev = rev * 10 + rem
            
            # Remove the last digit from temp by integer division by 10
            temp = temp // 10
        
        # Return True if the reversed number is equal to the original number, False otherwise
        return rev == x
# @lc code=end

