# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the node is null, return zero
        if root == None:
            return 0
        # Recursive case: return one plus the maximum of the depths of the left and right subtrees
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
