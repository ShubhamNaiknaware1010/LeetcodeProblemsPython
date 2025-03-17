#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty (root is None), the depth is 0
        if not root:
            return 0
        
        # Recursively find the max depth of the left and right subtrees
        # Add 1 for the current node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# @lc code=end

