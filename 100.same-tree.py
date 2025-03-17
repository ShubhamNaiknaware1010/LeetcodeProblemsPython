#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are None (empty trees), so they are the same
        if not p and not q:
            return True
        
        # Base case 2: One of the nodes is None (empty tree), but the other is not
        # If one tree is empty and the other is not, the trees are different
        if p and not q or q and not p:
            return False
        
        # Recursive case 3: Both nodes are not None, so we compare their values
        # and recursively check the left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end

