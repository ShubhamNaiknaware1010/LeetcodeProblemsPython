#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # Check if the length of the string is odd, because
        # valid parentheses must have even length
        if len(s) % 2 != 0:
            return False
        
        # Stack to keep track of opening parentheses
        stack = []
        
        # Dictionary to match opening parentheses with closing parentheses
        d = {"{": "}", "(": ")", "[": "]"}
        
        # Iterate through each character in the string
        for ch in s:
            # If the character is an opening bracket, push it onto the stack
            if ch in d:
                stack.append(ch)
            else:
                # If the stack is empty or the top of the stack doesn't match
                # the current closing bracket, return False
                if not stack or ch != d[stack.pop()]:
                    return False
        
        # If the stack is empty, all opening brackets were matched correctly
        # Otherwise, there are unmatched opening brackets left in the stack
        return not stack
    
# @lc code=end

