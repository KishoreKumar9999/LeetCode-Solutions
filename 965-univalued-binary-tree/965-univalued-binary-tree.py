# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def recurse(node, val):
            if not node:
                return True
            if node.val == val:
                return recurse(node.left, val) and recurse(node.right, val)
            return False
        return recurse(root, root.val)