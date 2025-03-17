#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head  # Initialize the current pointer to the head of the list
        
        # Traverse the list until the end or the next node is None
        while curr and curr.next:
            # If the current node value is the same as the next node value
            if curr.val == curr.next.val:
                # Skip the next node by pointing current node to the node after the next
                curr.next = curr.next.next
            else:
                # Otherwise, move to the next node
                curr = curr.next
        
        # Return the modified list (head remains the same)
        return head

# @lc code=end

