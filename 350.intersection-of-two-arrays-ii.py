#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the frequency of elements in nums1
        d = {}
        
        # List to store the result of the intersection
        arr = []
        # Step 1: Build the frequency dictionary for nums1
        # For each number in nums1, count its occurrences
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        # Step 2: Iterate over nums2 and find intersections with nums1
        # If a number in nums2 is also in nums1 and still has a positive count, add it to the result
        for num in nums2:
            if num in d and d[num] > 0:  # Check if num exists in nums1 and is still available
                arr.append(num)  # Append the number to the result list
                d[num] -= 1  # Decrement its count in the dictionary to handle duplicates correctly
    
        # Step 3: Return the result array containing the intersection of nums1 and nums2
        return arr
                
# @lc code=end

