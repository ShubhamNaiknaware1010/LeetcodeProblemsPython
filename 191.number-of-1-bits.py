#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize the count of '1' bits
        count = 0
        
        # Loop until n becomes 0
        while n > 0:
            # Check if the least significant bit is '1'
            if n & 1 != 0:
                # Increment count if the LSB is '1'
                count += 1
            
            # Right shift n by 1 to check the next bit
            n = n >> 1
        
        # Return the total count of '1' bits
        return count    
# @lc code=end

