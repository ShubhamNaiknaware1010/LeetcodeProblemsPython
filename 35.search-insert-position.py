#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    # Function to find the index where the target should be inserted in a sorted list
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the low and high pointers for binary search
        low = 0
        high = len(nums) - 1
        
        # Perform binary search
        while low <= high:
            # Calculate the middle index of the current search range
            mid = low + ((high - low) // 2)
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            
            # If the target is less than the middle element, narrow the search to the left half
            elif nums[mid] > target:
                high = mid - 1
            
            # If the target is greater than the middle element, narrow the search to the right half
            else:
                low = mid + 1
        
        # If the target is not found, return the index where it should be inserted
        return low



    # @lc code=end

