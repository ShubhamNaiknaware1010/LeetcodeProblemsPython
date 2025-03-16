#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    # Function to add one to a number represented by a list of digits
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate over the digits starting from the least significant (rightmost) digit
        for i in range(len(digits)):
            # Calculate the index of the current digit to be updated
            idx = len(digits) - 1 - i
            
            # Add 1 to the current digit
            digits[idx] += 1
            
            # If the digit is less than 10 after adding 1, no carry-over occurs, return the updated list
            if digits[idx] < 10:
                return digits
            
            # If the digit is 10 or more (carry-over), set it to 0 and continue
            digits[idx] = digits[idx] - 10
        
        # If all digits are processed and carry is still left (e.g., [9, 9] -> [1,

        

            
# @lc code=end

